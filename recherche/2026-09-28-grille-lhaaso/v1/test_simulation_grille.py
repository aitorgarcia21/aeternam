#!/usr/bin/env python3
"""Test secondaire reproductible d'un modèle-jouet de grille spatiale.

Aucune acquisition ni réanalyse des événements LHAASO. Les intervalles du
Tableau I de arXiv:2402.06009v3 sont des entrées publiées. Le code transforme
ces contraintes en bornes sur une maille et calcule des prédictions.
Ce n'est pas une probabilité que l'Univers soit simulé.

Python >= 3.10, bibliothèque standard uniquement.
Usage : python test_simulation_grille.py --out resultats_test_simulation.json

Sources :
- https://arxiv.org/pdf/2402.06009v3 (eq. 2, 3, 5 ; Tableau I, page 6)
- https://physics.nist.gov/cuu/Constants/Table/allascii.txt (CODATA 2022)
- https://arxiv.org/pdf/2508.00656v1 (audit annexe : eq. 3, 5, 7 ; Tables I, III)
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
from typing import Callable

C = 299_792_458.0
H = 6.62607015e-34
EV_J = 1.602176634e-19
HBAR_C_GEV_M = H / (2 * math.pi) * C / (EV_J * 1e9)
AU_M = 149_597_870_700.0
MPC_M = (648000.0 / math.pi) * AU_M * 1e6
EPL_PAPER_GEV = 1.22e19  # convention arrondie de LHAASO ; ne pas mélanger avec une autre.
LPL_CODATA_M = 1.616255e-35
Z = 0.151
H0 = 67.36 * 1000.0 / MPC_M
OMEGA_M = 0.315
OMEGA_L = 0.685

# Une source, trois méthodes : ne PAS multiplier les vraisemblances.
PUBLISHED = {
    'CCF': {'eta2_low_95': -0.47, 'eta2_best': 0.25, 'eta2_high_95': 0.66},
    'ML_MINOS': {'eta2_low_95': -0.31, 'eta2_best': 0.01, 'eta2_high_95': 0.32},
    'ML_calibrated': {'eta2_low_95': -0.30, 'eta2_best': None, 'eta2_high_95': 0.29},
}

def require_positive(value: float, label: str) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{label} doit être fini et strictement positif')
    return value

def simpson(f: Callable[[float], float], lo: float, hi: float, n: int = 4096) -> float:
    if n < 2 or n % 2:
        raise ValueError('n doit être un entier pair >= 2')
    step = (hi-lo)/n
    total = f(lo) + f(hi)
    total += 4 * math.fsum(f(lo+i*step) for i in range(1, n, 2))
    total += 2 * math.fsum(f(lo+i*step) for i in range(2, n, 2))
    return total * step / 3

def integral_i2(h0: float = H0, steps: int = 4096) -> float:
    return simpson(lambda zz: (1+zz)**2 / math.sqrt(OMEGA_M*(1+zz)**3+OMEGA_L),
                   0.0, Z, steps) / require_positive(h0, 'H0')

def q_factor(direction: tuple[float, float, float]) -> float:
    norm = math.sqrt(math.fsum(x*x for x in direction))
    require_positive(norm, 'norme de direction')
    return math.fsum((x/norm)**4 for x in direction)

def eta2_of_spacing(a_m: float, q: float) -> float:
    require_positive(a_m, 'maille')
    if not 1/3-1e-14 <= q <= 1+1e-14:
        raise ValueError('Q doit être compris entre 1/3 et 1')
    return 1e-15 * EPL_PAPER_GEV**2 * q * a_m**2 / (12 * HBAR_C_GEV_M**2)

def spacing_upper(eta_upper: float, q: float) -> float:
    return HBAR_C_GEV_M/EPL_PAPER_GEV * math.sqrt(12e15*require_positive(eta_upper, 'eta')/q)

def lag_seconds(a_m: float, q: float, eh_gev: float, el_gev: float, i2_s: float) -> float:
    require_positive(eh_gev, 'énergie haute')
    if not 0 <= el_gev < eh_gev:
        raise ValueError('Il faut 0 <= énergie basse < énergie haute')
    return q*a_m**2/(8*HBAR_C_GEV_M**2)*(eh_gev**2-el_gev**2)*i2_s

def audit_xi_shu() -> dict:
    # Recalcul de la conversion SEULEMENT ; ne valide pas l'intervalle statistique.
    # Eq.(3): theta2 = (3/2) * I2 * 10^6 / EQG2^2, theta2 en s/TeV^2.
    h0_other = 67.5*1000/MPC_M
    i2_other = integral_i2(h0_other)
    theta2_upper = 0.090
    converted_gev = math.sqrt(1.5*i2_other*1e6/theta2_upper)
    published_gev = 10.0e12
    return {
        'status': 'Incohérence apparente de conversion dans la version v1 ; pas une validation des données',
        'theta2_upper_s_per_TeV2_table_I': theta2_upper,
        'E_QG2_GeV_recomputed_from_equation_3': converted_gev,
        'E_QG2_GeV_printed_table_III': published_gev,
        'printed_divided_by_recomputed': published_gev/converted_gev,
        'use_in_primary_bound': False,
    }

def self_test() -> None:
    assert math.isclose(q_factor((1,0,0)), 1)
    assert math.isclose(q_factor((1,1,1)), 1/3)
    i2 = integral_i2()
    assert math.isclose(i2, integral_i2(steps=8192), rel_tol=2e-13)
    for u in (0.66, 0.32, 0.29):
        for q in (1/3, 0.6, 1):
            aa = spacing_upper(u, q)
            assert math.isclose(eta2_of_spacing(aa,q), u, rel_tol=1e-13)
    for q in (1/3,1):
        aa = 1e-26
        eqg = math.sqrt(12)*HBAR_C_GEV_M/(aa*math.sqrt(q))
        direct = lag_seconds(aa,q,1000,300,i2)
        alternative = 1.5*(1000**2-300**2)/eqg**2*i2
        assert math.isclose(direct,alternative,rel_tol=1e-13)
    # Une grille très grossière pour ce test échoue quelle que soit l'orientation.
    assert eta2_of_spacing(1e-26,1/3) > 0.66
    assert eta2_of_spacing(1e-28,1) < 0.29


def calculate() -> dict:
    self_test()
    i2 = integral_i2()
    bounds = {}
    for name, row in PUBLISHED.items():
        u = row['eta2_high_95']
        bounds[name] = dict(row,
            a_sqrt_Q_upper_m=spacing_upper(u,1),
            a_upper_unknown_orientation_m=spacing_upper(u,1/3))
    rows = []
    for a in (1e-26,1e-27,1e-28,LPL_CODATA_M):
        low, high = eta2_of_spacing(a,1/3), eta2_of_spacing(a,1)
        rows.append({
            'a_m': a, 'eta2_min': low, 'eta2_max': high,
            'lag_1TeV_vs_0p3TeV_s_min': lag_seconds(a,1/3,1000,300,i2),
            'lag_1TeV_vs_0p3TeV_s_max': lag_seconds(a,1,1000,300,i2),
            'outside_CCF_95_all_orientations': low > 0.66,
            'outside_ML_MINOS_95_all_orientations': low > 0.32,
            'outside_ML_calibrated_95_all_orientations': low > 0.29,
        })
    lpl_eta_max = eta2_of_spacing(LPL_CODATA_M,1)
    return {
        'title': 'Confrontation secondaire : grille cubique simple et contraintes LHAASO',
        'date': '2026-09-28',
        'analysis_level': 'Modèle-jouet + transformation de contraintes publiées, sans événements bruts',
        'assumptions': [
            'Grille spatiale cubique ; temps continu ; différences secondes aux plus proches voisins',
            'Propagation du mode lumineux suivant cette dispersion, sans termes compensateurs',
            'Maille physique constante dans un référentiel cosmologique privilégié',
            'Direction de propagation fixe ; Q dans [1/3,1], pas de prior sur Q',
            'Limite basse énergie ; relation énergie-fréquence E = hbar * omega',
            'Même transfert cosmologique et mêmes hypothèses sur la source que la limite reprise',
        ],
        'sources': {
            'LHAASO': 'https://arxiv.org/pdf/2402.06009v3',
            'NIST': 'https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
            'lattice_context': 'https://arxiv.org/abs/1210.1847',
            'conversion_audit': 'https://arxiv.org/pdf/2508.00656v1',
        },
        'constants': {'hbar_c_GeV_m': HBAR_C_GEV_M, 'Eplanck_paper_GeV': EPL_PAPER_GEV,
                      'Planck_length_CODATA_m': LPL_CODATA_M,
                      'H0_s_inverse':H0, 'Omega_m':OMEGA_M, 'z':Z},
        'I2_seconds': i2,
        'published_constraints_and_derived_bounds': bounds,
        'scenario_predictions_not_measured_lags': rows,
        'CCF_upper_divided_by_planck_scale_eta_max': 0.66/lpl_eta_max,
        'audit_other_publication': audit_xi_shu(),
        'self_tests': 'PASS',
        'limitations': [
            'Les intervalles à 95 % ne sont pas des probabilités de simulation',
            'Pas de combinaison des trois méthodes corrélées',
            'Pas de p-valeur extrapolée ni de nombre de sigma calculé hors du profil publié',
            'Maille plus fine non exclue par CE test : ni confirmée ni validée physiquement',
            'Le modèle ne couvre pas toutes les simulations ni toutes les physiques discrètes',
            'La limite la moins restrictive est une enveloppe de présentation, pas un nouvel intervalle combiné',
        ],
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('resultats_test_simulation.json'))
    args = parser.parse_args()
    result = calculate()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
