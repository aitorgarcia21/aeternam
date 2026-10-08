#!/usr/bin/env python3
"""Contrôles de référence, avec NumPy, sur des données logicielles artificielles."""
import importlib.util
import json
from math import exp, isclose, log
from pathlib import Path
import random
import numpy as np

DOSSIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("analyse_reve_recit", DOSSIER / "analyse.py")
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
parametres = json.loads((DOSSIER / "protocole.json").read_text())["parametres_calcul"]
tableau = a.tableau_publie()
# Deuxième relevé, contrôlé contre l'image de la page 367 du PDF original.
totaux_par_ligne = [2, 45, 2, 13, 7, 3, 7, 0, 2, 57, 5, 7, 0]
assert [r["signaux"] for r in tableau["lignes"]] == totaux_par_ligne
assert sum(totaux_par_ligne) == 150
assert (45 + 57) / 150 == .68

# Moyennes de personnes hétérogènes, plusieurs épisodes : tous artificiels.
rows = []
groupes = []
for i in range(12):
    rapports = [exp((i - 5.5) / 20 + j / 100) for j in range(1 + i % 4)]
    groupes.append(np.log(rapports).mean())
    rows.extend(a.fixture(f"artificielle_{i:02}", str(j), 60, 60 * rapport)
                for j, rapport in enumerate(rapports))
r = a.analyser_paires(rows, parametres)
assert isclose(r["moyenne_log_rapport"], float(np.mean(groupes)), abs_tol=1e-12)
# Même plan de rééchantillonnage ; calcul des moyennes et quantiles par NumPy.
rng = random.Random(parametres["graine"])
draws = np.array([rng.choices(groupes, k=len(groupes))
                 for _ in range(parametres["bootstrap_repetitions"])])
reference = np.exp(np.quantile(draws.mean(axis=1), [.025, .975]))
assert np.allclose(r["intervalle_95"], reference, rtol=0, atol=1e-12)
assert r["intervalle_95"][0] <= r["rapport_geometrique_apres_sur_pendant"] <= r["intervalle_95"][1]

# Modifier le nombre d'épisodes d'une seule personne sans changer sa moyenne
# laisse inchangée l'estimation principale. L'analyse par épisode ne le garantit pas.
dupliques = [dict(x, episode=x["episode"] + "_copie") for x in rows if x["personne"] == "artificielle_00"]
r2 = a.analyser_paires(rows + dupliques, parametres)
assert isclose(r2["moyenne_log_rapport"], r["moyenne_log_rapport"], abs_tol=1e-12)
assert np.allclose(r2["intervalle_95"], r["intervalle_95"], rtol=0, atol=1e-12)

resultat = {
    "statut": "Contrôles logiciels et documentaires, aucune validation empirique d'un effet humain.",
    "reference_tableau": "Deuxième lecture du tableau original, image de la page 367.",
    "totaux_par_ligne_conformes": True,
    "bootstrap_numpy_conforme": True,
    "poids_personnes_invariant": True,
    "autotests": a.autotests(parametres),
    "numpy_version": np.__version__,
    "analyse_sha256": a.empreinte(DOSSIER / "analyse.py"),
    "protocole_sha256": a.empreinte(DOSSIER / "protocole.json"),
}
(DOSSIER / "verification.json").write_text(json.dumps(resultat, ensure_ascii=False, indent=2) + "\n")
print("Tableau original, calculs NumPy et poids des personnes : conformes.")
