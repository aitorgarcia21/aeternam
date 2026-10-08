#!/usr/bin/env python3
"""Audit, réanalyse d'un tableau publié et analyse future de rapports appariés.

Sans --paires, aucune estimation humaine pendant/après n'est calculée.
Les cas artificiels des autotests ne sont jamais ajoutés aux observations.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from math import exp, isclose, isfinite, log
from pathlib import Path
import random
from statistics import fmean
import zipfile

DOSSIER = Path(__file__).resolve().parent
CHAMPS = (
    "personne", "episode", "intervalle", "debut_s", "fin_s", "reponse_pendant_s",
    "reveil_s", "reponse_apres_s", "intervalle_pendant", "intervalle_apres",
    "question_pendant", "question_apres", "estimation_pendant_s", "estimation_apres_s",
    "sommeil_verifie", "signal_verifie", "retour_information_avant_apres", "statut_apres",
)


def empreinte(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nombre(value: str) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    x = float(value)
    if not isfinite(x):
        raise ValueError("Valeur non finie interdite.")
    return x


def quantile(values: list[float], p: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * p
    i = int(position)
    return ordered[i] + (ordered[min(i + 1, len(ordered) - 1)] - ordered[i]) * (position - i)


def resumer_personnes(groupes: dict[str, list[float]], parametres: dict) -> dict:
    moyennes = [fmean(groupes[k]) for k in sorted(groupes) if groupes[k]]
    if not moyennes:
        return {"personnes": 0, "episodes": 0, "moyenne_log_rapport": None,
                "rapport_geometrique_apres_sur_pendant": None, "intervalle_95": None,
                "sensibilite_retrait_personne": None}
    centre = fmean(moyennes)
    intervalle = None
    if len(moyennes) >= parametres["minimum_personnes_intervalle"]:
        rng = random.Random(parametres["graine"])
        tirages = [fmean(rng.choices(moyennes, k=len(moyennes)))
                   for _ in range(parametres["bootstrap_repetitions"])]
        intervalle = [exp(quantile(tirages, 0.025)), exp(quantile(tirages, 0.975))]
    sensibilite = None
    if len(moyennes) >= 2:
        retraits = [exp(fmean(moyennes[:i] + moyennes[i+1:])) for i in range(len(moyennes))]
        sensibilite = {"minimum": min(retraits), "maximum": max(retraits),
                       "nature": "Plage de retrait d'une personne ; pas intervalle de confiance."}
    return {"personnes": len(moyennes), "episodes": sum(map(len, groupes.values())),
            "moyenne_log_rapport": centre,
            "rapport_geometrique_apres_sur_pendant": exp(centre),
            "intervalle_95": intervalle, "sensibilite_retrait_personne": sensibilite}


def analyser_paires(rows: list[dict], parametres: dict) -> dict:
    """Exige un registre de toutes les tentatives, pas seulement des réponses réussies."""
    groupes = defaultdict(list)
    doublons, personnes = set(), set()
    motifs = Counter()
    statuts = Counter()
    for row in rows:
        if set(row) != set(CHAMPS):
            raise ValueError("Schéma de colonnes incorrect.")
        if not all(row[k] for k in ("personne", "episode", "intervalle")):
            raise ValueError("Identifiant manquant.")
        cle = (row["personne"], row["episode"], row["intervalle"])
        if cle in doublons:
            raise ValueError("Intervalle dupliqué pour une personne et un épisode.")
        doublons.add(cle)
        personnes.add(row["personne"])
        if row["statut_apres"] not in ("observe", "absence_rappel", "manquant"):
            raise ValueError("Statut après réveil inconnu.")
        statuts[row["statut_apres"]] += 1
        for key in ("sommeil_verifie", "signal_verifie", "retour_information_avant_apres"):
            if row[key] not in ("oui", "non", "inconnu"):
                raise ValueError("Indicateur attendu : oui, non ou inconnu.")
        nums = {k: nombre(row[k]) for k in (
            "debut_s", "fin_s", "reponse_pendant_s", "reveil_s", "reponse_apres_s",
            "estimation_pendant_s", "estimation_apres_s")}
        avant, apres = nums["estimation_pendant_s"], nums["estimation_apres_s"]
        if any(x is not None and x <= 0 for x in (avant, apres)):
            raise ValueError("Une estimation de durée renseignée doit être positive.")
        if row["statut_apres"] != "observe" and apres is not None:
            raise ValueError("Une absence de rappel ou un manquant ne doit pas contenir une durée.")
        raisons = []
        if row["statut_apres"] != "observe":
            raisons.append(row["statut_apres"])
        if avant is None or (row["statut_apres"] == "observe" and apres is None):
            raisons.append("estimation_absente")
        if not (row["intervalle"] == row["intervalle_pendant"] == row["intervalle_apres"]):
            raisons.append("intervalle_non_apparie")
        if not row["question_pendant"] or row["question_pendant"] != row["question_apres"]:
            raisons.append("question_non_comparable")
        if row["sommeil_verifie"] != "oui" or row["signal_verifie"] != "oui":
            raisons.append("verification_insuffisante")
        if row["retour_information_avant_apres"] != "non":
            raisons.append("ancrage_non_exclu")
        temps = [nums[k] for k in ("debut_s", "fin_s", "reponse_pendant_s", "reveil_s", "reponse_apres_s")]
        if any(t is None for t in temps):
            raisons.append("horodatage_manquant")
        elif not (0 <= temps[0] < temps[1] <= temps[2] < temps[3] <= temps[4]):
            raise ValueError("Chronologie incompatible avec le plan.")
        elif temps[4] - temps[3] > parametres["delai_apres_max_s"]:
            raisons.append("rapport_tardif")
        if raisons:
            motifs.update(set(raisons))
            continue
        # Éviter de former un ratio flottant qui pourrait déborder avant le logarithme.
        groupes[row["personne"]].append(log(apres) - log(avant))
    resultat = resumer_personnes(groupes, parametres)
    resultat.update({"tentatives": len(rows), "personnes_registre": len(personnes),
                     "statuts_apres": dict(sorted(statuts.items())),
                     "motifs_non_admissibles": dict(sorted(motifs.items())),
                     "note_motifs": "Plusieurs motifs possibles pour une même tentative.",
                     "portee": "Rapports numériques appariés disponibles ; absence de rappel conservée, jamais imputée."})
    return resultat


def tableau_publie() -> dict:
    with (DOSSIER / "tableau-signaux.csv").open(newline="") as f:
        lignes = [{k: int(v) for k, v in row.items()} for row in csv.DictReader(f)]
    colonnes = ("yeux_ouverts", "yeux_fermes", "contenu_visuel", "sans_contenu_visuel")
    for ligne in lignes:
        ligne["signaux"] = sum(ligne[k] for k in colonnes)
    comptes = [r["signaux"] for r in lignes]
    total = sum(comptes)
    top2 = sum(sorted(comptes, reverse=True)[:2])
    totaux = {k: sum(r[k] for r in lignes) for k in colonnes}
    assert totaux == {"yeux_ouverts": 41, "yeux_fermes": 43, "contenu_visuel": 43, "sans_contenu_visuel": 23}
    assert total == 150 and len(lignes) == 13
    return {"source": "Konkoly et al. 2026, tableau 1, p. 367",
            "nature": "Réanalyse descriptive des décomptes publiés, pas réanalyse EEG.",
            "personnes_tableau": len(lignes), "personnes_avec_signaux": sum(n > 0 for n in comptes),
            "sessions_tableau": sum(r["sessions"] for r in lignes),
            "sessions_avec_signaux_selon_texte": 19, "signaux": total,
            "deux_plus_grands_contributeurs_signaux": top2,
            "part_deux_plus_grands_contributeurs": top2 / total,
            "totaux_par_type": totaux, "lignes": lignes,
            "limite": "Les tâches et nombres de sessions diffèrent. La concentration n'est ni un effet sur le temps vécu, ni une estimation du nombre de personnes statistiquement équivalent."}


def inspecter_dream() -> dict:
    archive = DOSSIER.parent / "2026-09-29-temps-reve/donnees/tononi_part1.zip"
    attendu = "e4d7932ed96e65fe6ff1e25df9fea0229b2e7e3d3cca1730f9dd637531ff62b0"
    assert empreinte(archive) == attendu
    with zipfile.ZipFile(archive) as z:
        p = "Tononi Serial Awakenings/"
        records = list(csv.DictReader(io.StringIO(z.read(p + "Records.csv").decode("utf-8-sig"))))
        additional = list(csv.DictReader(io.StringIO(z.read(p + "Data/AdditionalData.csv").decode("utf-8-sig"))))
    assert len({r["Filename"] for r in records}) == len(records)
    assert {r["Filename"] for r in records} == {r["Filename"] for r in additional}
    duree = next(k for k in additional[0] if k.startswith("Duration of continuous"))
    classes = Counter(r[duree].strip() for r in additional)
    return {"sha256_archive": attendu, "lignes": len(records),
            "personnes": len({r["Subject ID"] for r in records}),
            "champs_additionnels": list(additional[0]), "classes_duree_brutes": dict(sorted(classes.items())),
            "jugement_pendant_present_dans_schema": False,
            "intervalle_vecu_horodate": False,
            "usage": "Inspection du schéma uniquement ; aucune classe n'est convertie en secondes."}


def identification() -> dict:
    cas = []
    for nom, facteur, biais_pendant, biais_apres in (("A", 1, 1, 2), ("B", 2, 0.5, 1)):
        t = 60
        cas.append({"scenario": nom, "duree_physique_s": t, "facteur_latent_hypothetique": facteur,
                    "biais_rapport_pendant": biais_pendant, "biais_rapport_apres": biais_apres,
                    "rapport_pendant_s": t * facteur * biais_pendant,
                    "rapport_apres_s": t * facteur * biais_apres})
    assert cas[0]["rapport_pendant_s"] == cas[1]["rapport_pendant_s"] == 60
    assert cas[0]["rapport_apres_s"] == cas[1]["rapport_apres_s"] == 120
    return {"nature": "Contre-exemple algébrique choisi, sans donnée humaine ni modèle neuronal validé.",
            "relation": "P=T*F*B_pendant ; A=T*F*B_apres ; A/P=B_apres/B_pendant.",
            "scenarios": cas, "rapport_observable": 2,
            "conclusion": "Même avec deux rapports et une durée physique connue, le facteur latent F n'est pas identifié sans hypothèses supplémentaires sur les biais."}


def fixture(personne="artificielle_A", episode="1", avant=60, apres=120) -> dict:
    """Cas logiciel artificiel, jamais une observation ni un participant."""
    return dict(zip(CHAMPS, [personne, episode, "i1", "0", "60", "65", "80", "100",
                            "i1", "i1", "q1", "q1", str(avant), str(apres), "oui", "oui", "non", "observe"]))


def autotests(parametres: dict) -> list[str]:
    reussis = []
    def ok(nom, condition):
        assert condition, nom
        reussis.append(nom)
    vide = analyser_paires([], parametres)
    ok("absence_de_donnees_ne_vaut_pas_zero", vide["moyenne_log_rapport"] is None)
    absent = fixture(); absent.update(statut_apres="absence_rappel", estimation_apres_s="")
    r = analyser_paires([absent], parametres)
    ok("absence_rappel_conservee", r["tentatives"] == 1 and r["episodes"] == 0 and r["statuts_apres"]["absence_rappel"] == 1)
    r = analyser_paires([fixture()], parametres)
    ok("rapport_connu", isclose(r["rapport_geometrique_apres_sur_pendant"], 2))
    change_unite = fixture(avant=60000, apres=120000)
    ok("invariance_unites_estimations", isclose(analyser_paires([change_unite], parametres)["moyenne_log_rapport"], log(2)))
    inverse = analyser_paires([fixture(avant=120, apres=60)], parametres)
    ok("inversion_des_jugements", isclose(inverse["moyenne_log_rapport"], -r["moyenne_log_rapport"]))
    # Un sujet répété neuf fois ne reçoit pas neuf fois le poids de l'autre.
    imbalance = [fixture()] + [fixture("artificielle_B", str(i), 120, 60) for i in range(9)]
    r = analyser_paires(imbalance, parametres)
    ok("poids_egal_des_personnes", isclose(r["rapport_geometrique_apres_sur_pendant"], 1))
    for cle, valeur, raison in (
        ("intervalle_apres", "autre", "intervalle_non_apparie"),
        ("question_apres", "autre", "question_non_comparable"),
        ("signal_verifie", "inconnu", "verification_insuffisante"),
        ("retour_information_avant_apres", "oui", "ancrage_non_exclu"),
        ("reponse_apres_s", "300", "rapport_tardif")):
        cas = fixture(); cas[cle] = valeur
        r = analyser_paires([cas], parametres)
        ok(raison, r["episodes"] == 0 and raison in r["motifs_non_admissibles"])
    mauvais = [fixture(), fixture()]
    for nom, rows in (("doublons_refuses", mauvais),
                      ("chronologie_refusee", [dict(fixture(), reveil_s="50")]),
                      ("zero_refuse", [dict(fixture(), estimation_apres_s="0")]),
                      ("non_fini_refuse", [dict(fixture(), estimation_apres_s="nan")])):
        try:
            analyser_paires(rows, parametres)
        except ValueError:
            reussis.append(nom)
        else:
            raise AssertionError(nom)
    ok("quantile_reference", quantile([0, 1, 2, 3], 0.25) == 0.75)
    identification()
    reussis.append("facteur_latent_non_identifiable")
    return reussis


def analyser(path_paires: Path | None = None) -> dict:
    protocole = json.loads((DOSSIER / "protocole.json").read_text())
    acces = json.loads((DOSSIER / "disponibilite.json").read_text())
    provenance = json.loads((DOSSIER / "provenance-tableau.json").read_text())
    assert empreinte(DOSSIER / "tableau-signaux.csv") == provenance["sha256_csv"]
    parametres = protocole["parametres_calcul"]
    rows = []
    if path_paires is not None:
        with path_paires.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != list(CHAMPS):
                raise ValueError("En-tête différent de schema-paires.csv.")
            rows = list(reader)
    return {
        "statut": "Audit documentaire, recalcul d'un tableau publié et contrôles mathématiques ; aucune nouvelle collecte humaine.",
        "date": "2026-10-08", "protocole_sha256": empreinte(DOSSIER / "protocole.json"),
        "parametres_calcul": parametres,
        "disponibilite_sha256": empreinte(DOSSIER / "disponibilite.json"),
        "tableau_signaux": tableau_publie(), "inspection_dream": inspecter_dream(),
        "acces": {"candidats_examines": len(acces["sources"]),
                  "jeux_eligibles_reperes": sum(s["eligible"] for s in acces["sources"]),
                  "portee": acces["portee"]},
        "analyse_paires": {"origine": "Aucun fichier humain acquis" if path_paires is None else "Fichier fourni ; provenance à documenter séparément avant interprétation humaine",
                           "sha256_entree": None if path_paires is None else empreinte(path_paires),
                           **analyser_paires(rows, parametres)},
        "identification": identification(), "autotests": autotests(parametres)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DOSSIER / "resultats.json")
    parser.add_argument("--paires", type=Path)
    args = parser.parse_args()
    if args.paires is not None and args.out.resolve() == (DOSSIER / "resultats.json").resolve():
        parser.error("Avec --paires, choisir un --out distinct pour préserver le bilan documentaire publié.")
    resultats = analyser(args.paires)
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(f"Tableau : {resultats['tableau_signaux']['signaux']} signaux ; paires admissibles : {resultats['analyse_paires']['episodes']} ; {len(resultats['autotests'])} autotests.")
