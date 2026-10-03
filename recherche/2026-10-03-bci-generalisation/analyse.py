#!/usr/bin/env python3
"""Évaluer un décodeur EEG simple avec des runs et des personnes réservés.

Rejeu léger : NumPy seulement, depuis les caractéristiques extraites des EDF.
Pour reconstruire celles-ci, utiliser extraire.py et requirements-extraction.txt.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np

DOSSIER = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def charger():
    p = json.loads((DOSSIER / 'protocole.json').read_text())
    manifeste = json.loads((DOSSIER / 'donnees/manifest.json').read_text())
    csv_path = DOSSIER / 'donnees/caracteristiques.csv'
    assert sha256(csv_path) == manifeste['caracteristiques_sha256']
    assert sha256(DOSSIER / 'protocole.json') == manifeste['protocole_sha256']
    with csv_path.open(newline='') as f:
        lignes = list(csv.DictReader(f))
    noms = [f'{c}_{a}_{b}' for c in p['canaux'] for a, b in p['bandes_hz_demi_ouvertes']]
    X = np.array([[float(l[n]) for n in noms] for l in lignes])
    y = np.array([int(l['label']) for l in lignes])
    sujets = np.array([int(l['sujet']) for l in lignes])
    runs = np.array([int(l['run']) for l in lignes])
    assert len(lignes) == manifeste['total_essais']
    assert len({(l['sujet'], l['run'], l['essai']) for l in lignes}) == len(lignes)
    assert list(np.unique(sujets)) == p['sujets']
    assert np.all(np.isfinite(X))
    for s in p['sujets']:
        for r in p['runs']:
            index = (sujets == s) & (runs == r)
            assert set(y[index]) == {0, 1}, (s, r)
            nom = f'S{s:03d}R{r:02d}.edf'
            assert index.sum() == next(f['essais'] for f in manifeste['fichiers'] if f['fichier'] == nom)
    return p, manifeste, X, y, sujets, runs


def predire(X_train, y_train, X_test, regularisation):
    """LDA, a priori égaux ; aucun calcul ajusté sur les données de test."""
    assert set(y_train) == {0, 1}
    centre = X_train.mean(axis=0)
    echelle = X_train.std(axis=0)
    echelle[echelle < 1e-12] = 1.0
    A = (X_train - centre) / echelle
    B = (X_test - centre) / echelle
    moyennes = np.stack([A[y_train == k].mean(axis=0) for k in (0, 1)])
    residus = A - moyennes[y_train]
    covariance = residus.T @ residus / (len(A) - 2)
    identite = np.eye(A.shape[1]) * np.trace(covariance) / A.shape[1]
    covariance = (1 - regularisation) * covariance + regularisation * identite
    poids = np.linalg.solve(covariance, moyennes[1] - moyennes[0])
    seuil = 0.5 * (moyennes[1] + moyennes[0]) @ poids
    return (B @ poids > seuil).astype(int)


def exactitude_equilibree(y, predictions):
    return float(np.mean([np.mean(predictions[y == k] == k) for k in (0, 1)]))


def plis(sujets, runs):
    hors_personne, hors_run = [], []
    for s in np.unique(sujets):
        test = np.flatnonzero(sujets == s)
        hors_personne.append((np.flatnonzero(sujets != s), test))
        for r in np.unique(runs[sujets == s]):
            test = np.flatnonzero((sujets == s) & (runs == r))
            train = np.flatnonzero((sujets == s) & (runs != r))
            hors_run.append((train, test))
    for evaluation in (hors_personne, hors_run):
        visites = np.zeros(len(sujets), int)
        for train, test in evaluation:
            assert len(np.intersect1d(train, test)) == 0
            visites[test] += 1
        assert np.all(visites == 1)
    return {'personne_reservee': hors_personne, 'run_reserve': hors_run}


def evaluer(X, y, sujets, folds, reg):
    predictions = np.full(len(y), -1, dtype=int)
    for train, test in folds:
        predictions[test] = predire(X[train], y[train], X[test], reg)
    assert np.all(predictions >= 0)
    individus = []
    for s in np.unique(sujets):
        idx = sujets == s
        confusion = [[int(np.sum(idx & (y == vrai) & (predictions == predit)))
                      for predit in (0, 1)] for vrai in (0, 1)]
        individus.append({'sujet': int(s), 'n': int(idx.sum()),
                          'exactitude_equilibree': exactitude_equilibree(y[idx], predictions[idx]),
                          'confusion_vrai_predit': confusion})
    scores = [i['exactitude_equilibree'] for i in individus]
    return {'moyenne_personnes': float(np.mean(scores)), 'minimum_personnes': min(scores),
            'maximum_personnes': max(scores), 'par_personne': individus,
            'nombre_plis': len(folds), 'predictions': predictions.tolist()}


def holm(p_values):
    ordre = np.argsort(p_values)
    retour = np.empty(len(ordre))
    maximum = 0
    for rang, index in enumerate(ordre):
        maximum = max(maximum, min(1.0, p_values[index] * (len(ordre) - rang)))
        retour[index] = maximum
    return retour.tolist()


def autotests():
    assert exactitude_equilibree(np.array([0, 0, 0, 1]), np.zeros(4, int)) == 0.5
    assert np.allclose(holm([0.02, 0.03]), [0.04, 0.04])
    assert np.allclose(holm([0.6, 0.01]), [0.6, 0.02])
    A = np.array([[-3., 0.], [-2., 1.], [-1., -1.], [1., -1.], [2., 1.], [3., 0.]])
    y = np.array([0, 0, 0, 1, 1, 1])
    B = np.array([[-2., 0.], [2., 0.]])
    attendu = np.array([0, 1])
    assert np.array_equal(predire(A, y, B, 0.1), attendu)
    # Ajouter un test extrême ne doit pas changer les autres prédictions.
    assert np.array_equal(predire(A, y, np.vstack([B, [1e9, -1e9]]), 0.1)[:2], attendu)
    # Changer l'unité des caractéristiques ne doit pas changer la décision.
    assert np.array_equal(predire(A * [100, 0.01], y, B * [100, 0.01], 0.1), attendu)


def analyser():
    autotests()
    p, manifeste, X, y, sujets, runs = charger()
    folds = plis(sujets, runs)
    resultats = {nom: evaluer(X, y, sujets, f, p['regularisation']) for nom, f in folds.items()}
    rng = np.random.default_rng(p['graine'])
    blocs = [np.flatnonzero((sujets == s) & (runs == r)) for s in p['sujets'] for r in p['runs']]
    nuls = {nom: [] for nom in folds}
    for _ in range(p['permutations']):
        permute = y.copy()
        for b in blocs:
            permute[b] = rng.permutation(y[b])
        for nom, f in folds.items():
            nuls[nom].append(evaluer(X, permute, sujets, f, p['regularisation'])['moyenne_personnes'])
    p_values = [(1 + sum(v >= resultats[nom]['moyenne_personnes'] for v in nuls[nom])) /
                (p['permutations'] + 1) for nom in folds]
    corriges = holm(p_values)
    for k, nom in enumerate(folds):
        resultats[nom]['permutation'] = {
            'p_unilateral': p_values[k], 'p_holm_deux_tests': corriges[k],
            'moyenne_nulle': float(np.mean(nuls[nom])),
            'quantiles_nuls_2_5_97_5': np.quantile(nuls[nom], [0.025, 0.975]).tolist(),
            'scores_nuls': nuls[nom],
        }
    return {
        'statut': 'réanalyse exploratoire de vrais EEG ouverts ; pas de collecte Aeternam ni de BCI en ligne',
        'releves': json.loads((DOSSIER / 'releves.json').read_text()),
        'protocole': p,
        'donnees': {'n_personnes': len(p['sujets']), 'n_runs': len(manifeste['fichiers']),
                    'n_essais': len(y), 'n_par_classe': np.bincount(y).tolist(),
                    'n_caracteristiques': X.shape[1], 'bruts_octets': manifeste['total_octets_bruts'],
                    'caracteristiques_sha256': manifeste['caracteristiques_sha256'],
                    'protocole_sha256': manifeste['protocole_sha256'], 'exclusions': manifeste['exclusions']},
        'reference_constante_exactitude_equilibree': 0.5,
        'evaluations': resultats,
        'ecart_run_moins_personne_points': 100 * (resultats['run_reserve']['moyenne_personnes'] -
                                                  resultats['personne_reservee']['moyenne_personnes']),
        'limites': [
            'Sous-ensemble de convenance ; pas de revendication de représentativité.',
            'Les étiquettes décrivent une consigne visuelle ; pas de preuve isolant une intention de ses indices sensoriels ou musculaires.',
            'Trois canaux, modèle simple et paramètres non optimisés ; pas de plafond des BCI.',
            'Un run réservé n’est pas une journée ni une session indépendante ; les deux autres runs peuvent le précéder ou le suivre.',
            'La comparaison des deux évaluations change aussi les données d’apprentissage ; pas d’effet causal de la calibration.',
            'Permutations exploratoires sous échangeabilité dans personne/run ; pas de preuve clinique.',
            'Fenêtre entière de trois secondes après la consigne ; aucune mesure du débit ou des fausses activations en usage libre.'
        ],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER / 'resultats.json')
    args = parser.parse_args()
    r = analyser()
    args.out.write_text(json.dumps(r, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'donnees': r['donnees'], 'evaluations': {k: {
        'exactitude_equilibree': v['moyenne_personnes'], 'minimum': v['minimum_personnes'],
        'maximum': v['maximum_personnes'], 'p_holm': v['permutation']['p_holm_deux_tests']}
        for k, v in r['evaluations'].items()}}, ensure_ascii=False))
