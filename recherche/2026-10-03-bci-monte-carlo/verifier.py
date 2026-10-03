#!/usr/bin/env python3
"""Vérification indépendante des décisions, de la référence et des statistiques."""
import json
import math
import statistics
from pathlib import Path
import numpy as np
from scipy.stats import multivariate_normal
from sklearn.linear_model import Ridge
from analyse import (adapter, ajuster_reference, bruiter, charger, cov_reg,
                     mesures, predire, statistiques)

D = Path(__file__).resolve().parent


def verifier():
    p = json.loads((D/'protocole.json').read_text())
    r = json.loads((D/'resultats.json').read_text())
    profils, _, _ = charger(p)
    rng = np.random.default_rng(np.random.SeedSequence([p['graine'], 0]))
    cible = int(rng.integers(len(profils)))
    sources = [mesures(profil, p['essais_source_par_profil'], rng, 1, 1)
               for j, profil in enumerate(profils) if j != cible]
    stats = statistiques(np.vstack([x for x, _ in sources]), np.concatenate([y for _, y in sources]))
    cal, y_cal = mesures(profils[cible], max(p['budgets_etiquetes']), rng, 1, 1)
    test, y_test = mesures(profils[cible], p['essais_test_independants'], rng, 1, 1)
    conditions = bruiter(cal, test, profils[cible], rng, p)
    decisions = 0
    differences = 0
    for nom, (C, T, _) in conditions.items():
        for j, n in enumerate(p['budgets_etiquetes']):
            mu, cov = adapter(stats, C[:n], y_cal[:n], p)
            covariance = cov_reg(cov, p['covariance_decodeur_retrait_diagonal'])
            # Deux densités gaussiennes explicites, a priori égaux.
            logp = np.column_stack([multivariate_normal.logpdf(T, mean=m, cov=covariance) for m in mu])
            attendu = np.argmax(logp, axis=1)
            calcule = predire((mu, cov), T, p['covariance_decodeur_retrait_diagonal'])
            differences += int(np.sum(attendu != calcule))
            decisions += len(T)
            score = np.mean(attendu == y_test)
            assert abs(score-r['scenarios']['empirique']['conditions'][nom]['scores_par_campagne'][0][j]) < 1e-14
    assert differences == 0
    R = rng.normal(size=(256, 2))
    X = rng.normal(size=(256, 6))+R@rng.normal(size=(2, 6))
    coeff, centre = ajuster_reference(R, X, p['ridge_reference'])
    ref = Ridge(alpha=len(R)*p['ridge_reference'], fit_intercept=True).fit(R, X)
    ecart_reference = float(np.max(np.abs(coeff-ref.coef_.T)))
    assert ecart_reference < 1e-12
    assert np.allclose((R-centre)@coeff, ref.predict(R)-X.mean(0), atol=1e-12)
    ecart_stat = 0.
    seuils_verifies = 0
    for scenario in r['scenarios'].values():
        for condition in scenario['conditions'].values():
            scores = condition['scores_par_campagne']
            valides = []
            for j, budget in enumerate(p['budgets_etiquetes']):
                gains = [ligne[j]-ligne[0] for ligne in scores]
                moyenne = statistics.mean(gains)
                demi = 1.96*statistics.stdev(gains)/math.sqrt(len(gains))
                ecart_stat = max(ecart_stat, abs(moyenne-condition['gain_sur_zero_etiquette']['moyenne'][j]))
                assert np.allclose([moyenne-demi, moyenne+demi], condition['gain_sur_zero_etiquette']['ic_monte_carlo_95'][j], atol=1e-12)
                valides.append(100*moyenne >= p['gain_minimal_points'] and moyenne-demi > 0)
            seuil = next((n for j, n in enumerate(p['budgets_etiquetes']) if n and all(valides[j:])), None)
            assert seuil == condition['minimum_budget_gain']
            seuils_verifies += 1
    assert ecart_stat < 1e-12
    rapport = {'decisions_comparees_aux_densites_scipy': decisions,
               'predictions_differentes': differences, 'ridge_sklearn_max_ecart': ecart_reference,
               'statistiques_stdlib_max_ecart': ecart_stat, 'seuils_recalcules': seuils_verifies,
               'limite': 'Validation des calculs sous le modèle ; pas validation biologique du générateur.'}
    (D/'verification.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(rapport, ensure_ascii=False))


if __name__ == '__main__':
    verifier()
