#!/usr/bin/env python3
"""Contre-vérification indépendante (scipy) des ajustements de la restriction : même
vraisemblance, autre optimiseur, départs multiples. Hors de la chaîne de déploiement.
Usage : python3 verifier.py (scipy requis)."""
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

import analyse as A

ICI = Path(__file__).resolve().parent


def meilleur(f, departs):
    best = None
    for x0 in departs:
        r = minimize(f, x0, method='Powell', options={'xtol': 1e-8, 'ftol': 1e-10, 'maxfev': 40000})
        if best is None or r.fun < best.fun:
            best = r
    return best


def main():
    souris = A.lire_drido()
    res = json.loads((ICI / 'resultats.json').read_text(encoding='utf-8'))['restriction']['regimes']
    sortie = {}
    for reg in ('20', '40', '1D', '2D'):
        st = A.strates_drido(souris, reg)[0]
        for frag in (False, True):
            def f(x):
                v = math.exp(x[4]) if frag else 0.0
                if abs(x[3]) > 2.5 or v > 50:
                    return 1e12
                val = st.log_vraisemblance(x[0], x[1], x[2], x[3], v)
                return -val if math.isfinite(val) else 1e12
            departs = [[-5, 0.5, 0, 0, -2], [-4, 0.3, -0.5, 0.2, -1], [-6, 0.8, 0.3, -0.2, -3]]
            r = meilleur(f, departs)
            cle = 'gamma_gompertz' if frag else 'gompertz'
            publie = res[reg][cle]['lambda_general']
            sortie[f'{reg}_{cle}'] = {'lambda_scipy': math.exp(r.x[3]), 'lambda_analyse': publie,
                                      'ecart_relatif': math.exp(r.x[3]) / publie - 1}
    print(json.dumps(sortie, indent=1))
    assert all(abs(v['ecart_relatif']) < 0.01 for v in sortie.values()), sortie
    (ICI / 'verification.json').write_text(json.dumps(sortie, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
