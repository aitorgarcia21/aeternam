#!/usr/bin/env python3
"""Calculs exacts de méthode : information, confusion de cible et détection.

Aucun signal cérébral, entraînement de réseau ou résultat humain n'est simulé
comme s'il était observé. Les scénarios sont des contre-exemples mathématiques.
Usage : python3 analyse.py [--out resultats.json]
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import product
import json
from math import comb, isclose, log2
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent


def canal(brouillage: float | None, complet: bool = False) -> dict:
    """Y=(A,B), deux bits uniformes indépendants ; X voit tout, A ou rien."""
    if brouillage is not None and not 0 <= brouillage <= 1:
        raise ValueError("La probabilité de brouillage doit être entre 0 et 1.")
    joint = defaultdict(float)
    for a, b in product(range(2), repeat=2):
        y = (a, b)
        if complet:
            joint[(y, y)] += 0.25
        elif brouillage is None:
            joint[(None, y)] += 0.25
        else:
            joint[(a, y)] += 0.25 * (1 - brouillage)
            joint[(1 - a, y)] += 0.25 * brouillage
    px, py = defaultdict(float), defaultdict(float)
    for (x, y), p in joint.items():
        px[x] += p
        py[y] += p
    exactitude = sum(max(joint[(x, y)] for y in py) for x in px)
    information = sum(p * log2(p / (px[x] * py[y]))
                      for (x, y), p in list(joint.items()) if p > 0)
    # Énumération indépendante de tous les classifieurs déterministes possibles.
    meilleur_enumere = max(sum(joint[(x, y)] for x, y in zip(px, decisions))
                           for decisions in product(py, repeat=len(px)))
    assert isclose(exactitude, meilleur_enumere, abs_tol=1e-12)
    return {"exactitude_optimale": exactitude,
            "information_bits": max(0.0, information)}


def confusion_son_contenu() -> dict:
    """Le son C et le contenu D sont indépendants ; le modèle prédit C."""
    essais = list(product(range(4), repeat=2))
    return {
        "nature": "énumération de toutes les paires équiprobables, pas des observations",
        "paires": len(essais),
        "exactitude_sur_son": sum(c == c for c, d in essais) / len(essais),
        "exactitude_sur_contenu": sum(c == d for c, d in essais) / len(essais),
    }


def precision(prevalence: float, sensibilite: float, specificite: float) -> float | None:
    if not all(0 <= p <= 1 for p in (prevalence, sensibilite, specificite)):
        raise ValueError("Probabilités invalides.")
    vrais = prevalence * sensibilite
    faux = (1 - prevalence) * (1 - specificite)
    return vrais / (vrais + faux) if vrais + faux else None


def queue_binomiale(n: int, k: int, p: float) -> float:
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j)
               for j in range(k, n + 1))


def scenario_detection(n: int, p_nul: float = 0.25, p_alternatif: float = 0.4,
                       alpha: float = 0.05) -> dict:
    seuil = next(k for k in range(n + 2) if queue_binomiale(n, k, p_nul) <= alpha)
    return {"n_episodes_independants": n, "reussites_minimales": seuil,
            "taux_minimal": seuil / n,
            "alpha_effectif": queue_binomiale(n, seuil, p_nul),
            "puissance": queue_binomiale(n, seuil, p_alternatif)}


def autotests() -> None:
    # Des cas limites et des calculs par une autre méthode éprouvent les formules.
    assert canal(None)["exactitude_optimale"] == 0.25
    assert canal(0, complet=True) == {"exactitude_optimale": 1.0, "information_bits": 2.0}
    assert canal(0) == {"exactitude_optimale": 0.5, "information_bits": 1.0}
    assert isclose(canal(0.2)["exactitude_optimale"], 0.4)
    assert canal(0.5)["information_bits"] == 0
    assert isclose(canal(1)["exactitude_optimale"], canal(0)["exactitude_optimale"])
    assert isclose(precision(0.1, 0.8, 0.9), 8 / 17)
    assert precision(0.1, 1, 1) == 1
    assert precision(0, 1, 1) is None
    assert precision(1, 0.8, 0.9) == 1
    assert isclose(queue_binomiale(4, 2, 0.5), 11 / 16)
    assert queue_binomiale(4, 5, 0.5) == 0
    assert isclose(queue_binomiale(4, 0, 0.25), 1)
    assert confusion_son_contenu()["exactitude_sur_contenu"] == 0.25
    for n in (20, 40, 80):
        resultat = scenario_detection(n)
        seuil = resultat["reussites_minimales"]
        assert resultat["alpha_effectif"] <= 0.05
        assert queue_binomiale(n, seuil - 1, 0.25) > 0.05


def analyser() -> dict:
    releves = json.loads((DOSSIER / "releves.json").read_text(encoding="utf-8"))
    pilote = releves["pilote_2026"]
    return {
        "statut": "analyse documentaire et calculs exacts sur hypothèses explicites",
        "mesure_neuronale_aeternam": None,
        "performance_decodeur_aeternam": None,
        "effet_causal_sur_reves_aeternam": None,
        "releves": releves,
        "pilote": {
            "premier_rem_parmi_rem": pilote["incorporation_premier_rem"] / pilote["participants_rem"],
            "au_moins_un_rem_parmi_rem": pilote["incorporation_au_moins_un_rem"] / pilote["participants_rem"],
            "au_moins_un_rem_parmi_recrutes": pilote["incorporation_au_moins_un_rem"] / pilote["participants_initiaux"],
            "effet_causal": None,
        },
        "information": {
            "hypotheses": "Quatre classes équiprobables Y=(A,B), A et B indépendants ; canaux abstraits, pas des modèles validés de MEG ou EEG.",
            "professeur_complet": canal(0, complet=True),
            "eleve_partiel": canal(0),
            "eleve_partiel_bruite": canal(0.2),
            "aucun_signal": canal(None),
            "brouillage_hypothetique": 0.2,
        },
        "confusion": confusion_son_contenu(),
        "detection_rare": {
            "nature": "hypothèses numériques, sans estimation d'une performance réelle",
            "prevalence": 0.1, "sensibilite": 0.8, "specificite": 0.9,
            "precision_positive": precision(0.1, 0.8, 0.9),
        },
        "detection_quatre_classes": {
            "hypotheses": "Essais binomiaux indépendants, classes équilibrées, test unilatéral fixé à l'avance, une seule comparaison.",
            "p_nul": 0.25, "p_alternatif_hypothetique": 0.4, "alpha_nominal": 0.05,
            "scenarios": [scenario_detection(n) for n in (20, 40, 80)],
            "taille_experience_humaine_recommandee": None,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DOSSIER / "resultats.json")
    args = parser.parse_args()
    autotests()
    resultats = analyser()
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print("Calculs exacts et autotests réussis ; aucune performance cérébrale mesurée.")
