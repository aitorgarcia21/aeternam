#!/usr/bin/env python3
"""Contre-vérification indépendante (statsmodels et scipy), hors de la chaîne de déploiement.

Refait, avec d'autres logiciels, les tests 1 et 2 de toutes les mesures de la famille principale
(régression linéaire : statsmodels OLS ; modèle de Cox avec troncature à gauche : statsmodels
PHReg, ex aequo de Breslow), et le λ de la pente avec les candidates (scipy, BFGS).
Usage : python3 verifier.py (statsmodels et scipy requis)."""
import json
from pathlib import Path

import math

import numpy as np
from scipy.optimize import minimize
import statsmodels.api as sm
from statsmodels.duration.hazard_regression import PHReg

import analyse as A

ICI = Path(__file__).resolve().parent


def lambda_scipy(lignes, serie, noms):
    """λ de la pente avec les candidates en covariables, refait avec scipy (BFGS)."""
    souris = []
    for x in lignes:
        if x['Diet'] not in ('AL', '40'):
            continue
        age, t = A.nombre(x.get(serie + 'AgeInDays')), A.nombre(x['SurvDays'])
        vals = [A.nombre(x[m]) for m in noms]
        if age is None or t is None or any(v is None for v in vals):
            continue
        e = max(A.PLANCHER, age / A.AN)
        if t / A.AN > e:
            souris.append((e, t / A.AN, 1.0 if x['Died'] == 'TRUE' else 0.0, 1.0 if x['Diet'] == '40' else 0.0, vals))
    e, t, d, g = (np.array([s[i] for s in souris]) for i in range(4))
    Z = np.column_stack([A.rangs_normaux([s[4][j] for s in souris]) for j in range(len(noms))])
    s0 = A.DEBUT_REGIME

    def nll(x):
        la, lb, lt, ll = x[:4]
        a, b = math.exp(la), math.exp(lb)
        bt, kk = b / math.exp(ll), math.exp(lt) * a * math.exp(b * s0)
        H0 = lambda u: (a / b) * np.expm1(b * u)
        H1 = lambda u: (a / b) * math.expm1(b * s0) + kk * np.expm1(bt * (u - s0)) / bt
        lh = np.where(g > 0, lt + la + b * s0 + bt * (t - s0), la + b * t)
        eta = Z @ x[4:]
        v = float((d * (lh + eta)).sum() - (np.exp(eta) * (np.where(g > 0, H1(t), H0(t)) - np.where(g > 0, H1(e), H0(e)))).sum())
        return -v if math.isfinite(v) else 1e12
    best = min((minimize(nll, x0, method='BFGS', options={'maxiter': 5000, 'gtol': 1e-7})
                for x0 in ([-5, 0.5, 0, 0] + [0] * len(noms), [-4, 0.4, -0.3, 0.2] + [0.1] * len(noms))),
               key=lambda r: r.fun)
    return math.exp(best.x[3])


def main():
    lignes, colonnes = A.lire()
    gens = A.generations(lignes)
    res = json.loads((ICI / 'resultats.json').read_text(encoding='utf-8'))
    par_mesure = {e['mesure']: e for e in res['principale']['liste']}
    ecarts1, ecarts2 = [], []
    for prefixe in A.PRINCIPALE:
        for m in A.mesures_de(prefixe, colonnes):
            if m not in par_mesure:
                continue
            souris = A.preparer_serie(lignes, prefixe, m)
            # test 1
            s = [x for x in souris if x['regime'] in A.DOSES]
            y = A.rangs_normaux([x['v'] for x in s])
            age = np.array([x['age'] for x in s])
            X = np.column_stack([np.ones(len(s)), [A.DOSES[x['regime']] for x in s], age - age.mean(),
                                 A.strates([x['generation'] for x in s])])
            ols = sm.OLS(y, X).fit()
            ecarts1.append(abs(ols.tvalues[1] - par_mesure[m]['test1']['dose_z']))
            # test 2
            X2 = A.matrice_cox(souris, gens, True)
            ph = PHReg(np.array([x['sortie'] for x in souris]), X2, status=np.array([x['mort'] for x in souris]),
                       entry=np.array([x['age'] for x in souris]), ties='breslow').fit()
            ecarts2.append(abs(ph.params[0] - par_mesure[m]['test2']['log_hr']))
    sortie = {'mesures': len(ecarts1), 'ecart_max_z_test1': float(max(ecarts1)),
              'ecart_max_log_hr_test2': float(max(ecarts2)),
              'pentes': [{'serie': p['serie'], 'lambda_analyse': p['lambda_avec'],
                          'lambda_scipy': lambda_scipy(lignes, p['serie'], p['mesures'])} for p in res['pentes']]}
    print(json.dumps(sortie, indent=1))
    # résultats arrondis à 6 chiffres significatifs dans resultats.json : tolérance de 1e-3
    assert sortie['ecart_max_z_test1'] < 1e-3 and sortie['ecart_max_log_hr_test2'] < 1e-3, sortie
    assert all(abs(p['lambda_scipy'] / p['lambda_analyse'] - 1) < 1e-3 for p in sortie['pentes']), sortie
    (ICI / 'verification.json').write_text(json.dumps(sortie, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
