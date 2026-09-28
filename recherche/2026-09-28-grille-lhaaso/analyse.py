#!/usr/bin/env python3
"""aeternam, test n° 1 (version 2) : une grille cubique face à GRB 221009A.

Analyse secondaire : aucun événement LHAASO n'est réanalysé. Les intervalles
publiés (tableau I de arXiv:2402.06009v3) sont traduits en bornes sur la maille
d'un réseau cubique, puis on mesure la robustesse de ces bornes : temps discret
(nombre de Courant), orientation du réseau, maille comobile, artefact linéaire.
Rien ici n'est une probabilité que l'Univers soit simulé.

La version 1 (dossier v1/) traitait le temps continu et l'orientation la moins
favorable. Python >= 3.10, bibliothèque standard uniquement.
Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable

# Constantes SI exactes (CODATA 2022) et conventions des articles repris.
C = 299_792_458.0
H = 6.62607015e-34
EV_J = 1.602176634e-19
HBAR_C_GEV_M = H / (2 * math.pi) * C / (EV_J * 1e9)
MPC_M = (648_000.0 / math.pi) * 149_597_870_700.0 * 1e6
LPL_M = 1.616255e-35           # longueur de Planck, CODATA 2022
EPL_GEV = 1.22e19              # énergie de Planck arrondie, convention LHAASO

# Source et cosmologie de LHAASO (arXiv:2402.06009v3) ; Omega_Lambda = 1 - Omega_m.
Z = 0.151
H0_LHAASO = 67.36              # km/s/Mpc
OMEGA_M = 0.315

# Tableau I : intervalles à 95 % sur eta_2. Une source, trois méthodes corrélées :
# on ne combine PAS les vraisemblances.
ETA2 = {
    'CCF': {'bas': -0.47, 'meilleur': 0.25, 'haut': 0.66},
    'ML_MINOS': {'bas': -0.31, 'meilleur': 0.01, 'haut': 0.32},
    'ML_calibre': {'bas': -0.30, 'meilleur': None, 'haut': 0.29},
}
METHODE_PRUDENTE = 'CCF'       # la moins restrictive, retenue pour le résumé
EQG1_MIN_GEV = 10 * EPL_GEV    # résumé LHAASO : E_QG,1 > 10 E_Pl (effet linéaire)
EQG2_MIN_GEV = 6.9e11          # résumé LHAASO : E_QG,2 > 6,9e11 GeV (quadratique, subluminal)

BEANE_INV_B_GEV = 1e11         # Beane, Davoudi, Savage (2012) : 1/b >~ 10^11 GeV

# Xi et Shu, arXiv:2508.00656v1 : tableau I, éq. (6) et (7), tableau III.
XS_THETA2 = 0.090              # s/TeV^2
XS_EQ6_CONST = 5.7             # eps_QG,1 ~ 5.7 / theta1 (tel qu'imprimé, n = 1)
XS_EQ7_CONST = 7.5e-8          # eps_QG,2 ~ 7.5e-8 / theta2 (tel qu'imprimé, n = 2)
XS_EQG2_IMPRIME_GEV = 10.0e12
XS_H0 = 67.5

SIGMAS = (0.0, 0.5, 0.9, 0.99, 1.0)   # nombre de Courant ; 1 = pas maximal stable
N_DIRECTIONS = 1_000_000
E_VALIDITE_GEV = 20e3                 # au-delà des photons rapportés pour ce sursaut
AK_TEST = 0.03                        # comparaison développement / dispersion exacte


def simpson(f: Callable[[float], float], lo: float, hi: float, n: int = 4096) -> float:
    if n < 2 or n % 2:
        raise ValueError('n doit être un entier pair >= 2')
    step = (hi - lo) / n
    total = f(lo) + f(hi)
    total += 4 * math.fsum(f(lo + i * step) for i in range(1, n, 2))
    total += 2 * math.fsum(f(lo + i * step) for i in range(2, n, 2))
    return total * step / 3


def integrale(n: int, h0: float = H0_LHAASO, steps: int = 4096) -> float:
    """I_n = intégrale de 0 à z de (1+z')^n / H(z') dz', en secondes."""
    h0_si = h0 * 1000.0 / MPC_M
    return simpson(lambda x: (1 + x) ** n / math.sqrt(OMEGA_M * (1 + x) ** 3 + 1 - OMEGA_M),
                   0.0, Z, steps) / h0_si


def unitaire(direction: tuple[float, float, float]) -> list[float]:
    norme = math.sqrt(math.fsum(x * x for x in direction))
    if not norme > 0:
        raise ValueError('direction nulle')
    return [x / norme for x in direction]


def q_facteur(direction: tuple[float, float, float]) -> float:
    """Q = somme des n_i^4 : 1 sur un axe du cube, 1/3 sur une grande diagonale."""
    return math.fsum(x ** 4 for x in unitaire(direction))


def q_effectif(q: float, sigma: float) -> float:
    """Le temps discret (c dt = sigma a / racine 3) retranche sigma^2 / 3."""
    return q - sigma ** 2 / 3


def vitesse_groupe(direction: tuple[float, float, float], ak: float, sigma: float) -> float:
    """v/c radiale exacte du photon sur le réseau (schéma de Yee ; temps continu si sigma = 0).

    Dispersion : (2/(c dt))^2 sin^2(w dt/2) = (2/a)^2 somme sin^2(k_i a/2).
    """
    n = unitaire(direction)
    k = [ak * x for x in n]                       # a k_i
    s2 = math.fsum(math.sin(x / 2) ** 2 for x in k)
    if sigma == 0:
        w = 2 * math.sqrt(s2)                     # w a / c
        grad = [math.sin(x) / w for x in k]
    else:
        tau = sigma / math.sqrt(3)                # c dt / a
        w = 2 / tau * math.asin(tau * math.sqrt(s2))
        grad = [tau * math.sin(x) / math.sin(w * tau) for x in k]
    return math.fsum(g * x for g, x in zip(grad, n))


def eta2(a_m: float, qe: float) -> float:
    """Paramètre de LHAASO : eta_2 = 1e-15 E_Pl^2 / E_QG,2^2, avec E_QG,2 = racine(12) hbar c / (a racine(Qe))."""
    return 1e-15 * EPL_GEV ** 2 * qe * a_m ** 2 / (12 * HBAR_C_GEV_M ** 2)


def borne_a_racine_qe(u: float) -> float:
    """Borne sur a * racine(Q_eff) tirée d'une limite haute u sur eta_2."""
    if not u > 0:
        raise ValueError('limite haute positive attendue')
    return HBAR_C_GEV_M / EPL_GEV * math.sqrt(12e15 * u)


def retard(a_m: float, qe: float, eh_gev: float, el_gev: float, i2_s: float) -> float:
    """Retard prédit (s) du photon d'énergie eh sur celui d'énergie el."""
    return qe * a_m ** 2 * (eh_gev ** 2 - el_gev ** 2) / (8 * HBAR_C_GEV_M ** 2) * i2_s


def distribution_q(n_points: int = N_DIRECTIONS) -> list[float]:
    """Q pour des directions quasi uniformes (sphère de Fibonacci, déterministe), triées."""
    angle_or = math.pi * (3 - math.sqrt(5))
    valeurs = []
    for i in range(n_points):
        z = 1 - (2 * i + 1) / n_points
        r = math.sqrt(max(0.0, 1 - z * z))
        phi = i * angle_or
        x, y = r * math.cos(phi), r * math.sin(phi)
        valeurs.append(x ** 4 + y ** 4 + z ** 4)
    valeurs.sort()
    return valeurs


def quantile(tries: list[float], p: float) -> float:
    return tries[min(len(tries) - 1, int(p * len(tries)))]


def audit_xi_shu() -> dict:
    """Recalcule leurs conversions ; ne valide ni ne réanalyse leur intervalle statistique."""
    i1, i2 = integrale(1, XS_H0), integrale(2, XS_H0)
    constante_n1 = i1 * 1e3 / EPL_GEV              # eps_QG,1 = constante / theta1
    carre_n2 = 1.5e6 * i2 / EPL_GEV ** 2           # eps_QG,2^2 = carre / theta2
    coherent = math.sqrt(1.5e6 * i2 / XS_THETA2)
    formule_imprimee = XS_EQ7_CONST / XS_THETA2 * EPL_GEV
    return {
        'statut': 'Incohérence apparente de conversion dans la v1 ; aucune validation des données',
        'theta2_limite_s_par_TeV2': XS_THETA2,
        'n1_constante_recalculee': constante_n1,
        'n1_constante_imprimee_eq6': XS_EQ6_CONST,
        'n2_eps2_fois_theta2_recalcule': carre_n2,
        'n2_constante_coherente_sur_racine_theta2': math.sqrt(carre_n2),
        'n2_constante_imprimee_eq7_sur_theta2': XS_EQ7_CONST,
        'EQG2_GeV_coherent_avec_eq3': coherent,
        'EQG2_GeV_avec_eq7_imprimee': formule_imprimee,
        'EQG2_GeV_imprime_tableau_III': XS_EQG2_IMPRIME_GEV,
        'imprime_sur_coherent': XS_EQG2_IMPRIME_GEV / coherent,
        'imprime_sur_LHAASO': XS_EQG2_IMPRIME_GEV / EQG2_MIN_GEV,
        'coherent_sur_LHAASO': coherent / EQG2_MIN_GEV,
        'hypothese': ("7,5e-8 ressemble à racine(7,5e-16) où la racine n'aurait porté que sur "
                      "la puissance de dix ; l'éq. (7) garde la forme en 1/theta de l'éq. (6)"),
        'utilise_dans_la_borne_principale': False,
    }


def ecart_developpement(ak: float = AK_TEST) -> float:
    """Écart relatif maximal entre le développement et la dispersion exacte."""
    ecarts = []
    for d in ((1, 0, 0), (1, 1, 0), (0.3, 0.5, 0.8), (2, 1, 0.4)):
        for s in SIGMAS:
            attendu = ak ** 2 / 8 * q_effectif(q_facteur(d), s)
            if attendu > 1e-12:
                ecarts.append(abs((1 - vitesse_groupe(d, ak, s)) / attendu - 1))
    return max(ecarts)


def autotests(qs: list[float]) -> None:
    assert math.isclose(q_facteur((1, 0, 0)), 1)
    assert math.isclose(q_facteur((1, 1, 1)), 1 / 3)
    assert math.isclose(integrale(2), integrale(2, steps=8192), rel_tol=2e-13)
    # Développement v/c = 1 - (ak)^2 (Q - sigma^2/3) / 8 contre la dispersion exacte.
    ak = 1e-2
    for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (0.3, 0.5, 0.8)):
        for s in SIGMAS:
            attendu = ak ** 2 / 8 * q_effectif(q_facteur(d), s)
            exact = 1 - vitesse_groupe(d, ak, s)
            if attendu > 1e-12:
                assert math.isclose(exact, attendu, rel_tol=1e-3), (d, s, exact, attendu)
            else:
                assert abs(exact) < 1e-12, (d, s, exact)
    # Au pas maximal stable, la grande diagonale est exactement sans dispersion.
    for ak_grand in (0.1, 0.5, 1.0):
        assert abs(1 - vitesse_groupe((1, 1, 1), ak_grand, 1.0)) < 1e-12
    # Aller-retour eta_2 <-> maille, et retard = formule de Jacob et Piran.
    for u in (0.66, 0.32, 0.29):
        assert math.isclose(eta2(borne_a_racine_qe(u), 1.0), u, rel_tol=1e-13)
    i2 = integrale(2)
    for q in (1 / 3, 1.0):
        eqg = math.sqrt(12) * HBAR_C_GEV_M / (1e-26 * math.sqrt(q))
        assert math.isclose(retard(1e-26, q, 1000, 300, i2),
                            1.5 * (1000 ** 2 - 300 ** 2) / eqg ** 2 * i2, rel_tol=1e-13)
    # Moyenne exacte de Q sur la sphère : 3/5.
    assert math.isclose(math.fsum(qs) / len(qs), 0.6, abs_tol=1e-4)
    assert qs[0] >= 1 / 3 - 1e-12 and qs[-1] <= 1 + 1e-12
    # Continuité avec la version 1.
    assert math.isclose(borne_a_racine_qe(0.66) * math.sqrt(3), 2.4931583193889674e-27, rel_tol=1e-12)


def calculer() -> dict:
    qs = distribution_q()
    autotests(qs)
    i0, i2 = integrale(0), integrale(2)
    q05, q50 = quantile(qs, 0.05), quantile(qs, 0.5)

    bornes = {}
    for nom, ligne in ETA2.items():
        a_rq = borne_a_racine_qe(ligne['haut'])
        pire = a_rq * math.sqrt(3)
        bornes[nom] = dict(ligne,
                           a_racine_Q_max_m=a_rq,
                           a_max_pire_orientation_m=pire,
                           a_max_95pct_orientations_m=a_rq / math.sqrt(q05),
                           a_max_axe_m=a_rq,
                           echelle_min_GeV=HBAR_C_GEV_M / pire)
    a_rq = bornes[METHODE_PRUDENTE]['a_racine_Q_max_m']
    a_pire = bornes[METHODE_PRUDENTE]['a_max_pire_orientation_m']

    temps_discret = []
    for s in SIGMAS:
        qe_min = q_effectif(1 / 3, s)
        temps_discret.append({
            'sigma_courant': s,
            'c_dt_sur_a': s / math.sqrt(3),
            'Q_eff_min': qe_min,
            'a_max_pire_orientation_m': a_rq / math.sqrt(qe_min) if qe_min > 1e-12 else None,
            'a_max_95pct_orientations_m': a_rq / math.sqrt(q_effectif(q05, s)),
            'a_max_orientation_mediane_m': a_rq / math.sqrt(q_effectif(q50, s)),
        })

    predictions = []
    for a in (1e-26, 1e-27, 1e-28, LPL_M):
        bas, haut = eta2(a, 1 / 3), eta2(a, 1.0)
        predictions.append({
            'a_m': a, 'eta2_min': bas, 'eta2_max': haut,
            'retard_1TeV_0p3TeV_s_min': retard(a, 1 / 3, 1000, 300, i2),
            'retard_1TeV_0p3TeV_s_max': retard(a, 1.0, 1000, 300, i2),
            **{f'exclue_{nom}_toutes_orientations': bas > ligne['haut'] for nom, ligne in ETA2.items()},
        })

    b_beane = HBAR_C_GEV_M / BEANE_INV_B_GEV
    a_lineaire = HBAR_C_GEV_M / EQG1_MIN_GEV
    eta2_planck = eta2(LPL_M, 1.0)
    return {
        'titre': 'Test n° 1, version 2 : grille cubique et contraintes LHAASO sur GRB 221009A',
        'date': '2026-09-28',
        'niveau': "Analyse secondaire d'intervalles publiés ; aucun événement réanalysé",
        'hypotheses': [
            'Réseau cubique de maille physique a, au repos dans le référentiel cosmologique',
            "Photon régi par Maxwell discrétisé (schéma de Yee / hamiltonien de Kogut-Susskind), sans terme compensateur",
            'Temps continu (sigma = 0) ou pas c dt = sigma a / racine 3, avec sigma <= 1 (stabilité)',
            'Q = somme des n_i^4 selon la direction de GRB 221009A dans les axes du réseau (1/3 <= Q <= 1)',
            'E = hbar omega ; transfert cosmologique et hypothèses de source de LHAASO',
        ],
        'constantes': {'hbar_c_GeV_m': HBAR_C_GEV_M, 'E_Pl_GeV': EPL_GEV, 'l_Pl_m': LPL_M,
                       'z': Z, 'H0_km_s_Mpc': H0_LHAASO, 'Omega_m': OMEGA_M},
        'integrales_s': {'I0': i0, 'I2': i2},
        'orientation': {'moyenne_Q': math.fsum(qs) / len(qs), 'Q_1pct': quantile(qs, 0.01),
                        'Q_5pct': q05, 'Q_mediane': q50, 'n_directions': len(qs)},
        'bornes_temps_continu': bornes,
        'temps_discret_methode_prudente': temps_discret,
        'maille_comobile': {'rapport_I2_sur_I0': i2 / i0,
                            'facteur_sur_la_borne': math.sqrt(i2 / i0),
                            'a_max_pire_orientation_m': a_pire * math.sqrt(i2 / i0)},
        'comparaison_beane_2012': {'b_max_m': b_beane,
                                   'rapport_borne_prudente_sur_beane': a_pire / b_beane},
        'artefact_lineaire': {'EQG1_min_GeV': EQG1_MIN_GEV, 'a_max_m_coefficient_1': a_lineaire,
                              'rapport_a_longueur_Planck': a_lineaire / LPL_M},
        'maille_de_Planck': {'eta2_max': eta2_planck,
                             'facteur_sous_la_limite_prudente': ETA2[METHODE_PRUDENTE]['haut'] / eta2_planck},
        'validite_developpement': {'E_GeV': E_VALIDITE_GEV,
                                   'a_E_sur_hbar_c': a_pire * E_VALIDITE_GEV / HBAR_C_GEV_M,
                                   'ak_test': AK_TEST,
                                   'ecart_relatif_max_developpement': ecart_developpement()},
        'retard_a_la_limite_1TeV_0p3TeV_s': retard(a_rq, 1.0, 1000, 300, i2),
        'predictions_non_mesurees': predictions,
        'audit_xi_shu': audit_xi_shu(),
        'autotests': 'OK',
        'sources': {
            'LHAASO': 'https://arxiv.org/abs/2402.06009v3',
            'Beane_Davoudi_Savage': 'https://arxiv.org/abs/1210.1847',
            'Xi_Shu': 'https://arxiv.org/abs/2508.00656v1',
            'CODATA': 'https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
        },
        'limites': [
            'Les intervalles à 95 % portent sur un paramètre physique, pas sur la probabilité d’une simulation',
            'Trois méthodes corrélées sur un seul sursaut : pas de combinaison',
            'Les fractions d’orientations sont géométriques, pas des probabilités sur l’Univers',
            'Un schéma amélioré (erreur en a^4) ou des termes compensateurs échappent à cette borne',
        ],
    }


def resume(r: dict) -> str:
    b = r['bornes_temps_continu']
    lignes = [f"{nom:11s} a*racine(Q) <= {v['a_racine_Q_max_m']:.3e} m | pire orientation <= "
              f"{v['a_max_pire_orientation_m']:.3e} m | 95 % des orientations <= "
              f"{v['a_max_95pct_orientations_m']:.3e} m | échelle >= {v['echelle_min_GeV']:.2e} GeV"
              for nom, v in b.items()]
    for t in r['temps_discret_methode_prudente']:
        pire = t['a_max_pire_orientation_m']
        lignes.append(f"sigma = {t['sigma_courant']:<4} pire : {'aucune borne' if pire is None else f'{pire:.3e} m':>12}"
                      f" | 95 % : {t['a_max_95pct_orientations_m']:.3e} m | médiane : {t['a_max_orientation_mediane_m']:.3e} m")
    o, m, x = r['orientation'], r['maille_comobile'], r['audit_xi_shu']
    lignes += [
        f"Q : 1 % = {o['Q_1pct']:.4f}, 5 % = {o['Q_5pct']:.4f}, médiane = {o['Q_mediane']:.4f}, moyenne = {o['moyenne_Q']:.5f}",
        f"Maille comobile : borne x {m['facteur_sur_la_borne']:.4f} -> {m['a_max_pire_orientation_m']:.3e} m",
        f"Beane 2012 : b <= {r['comparaison_beane_2012']['b_max_m']:.3e} m ; rapport {r['comparaison_beane_2012']['rapport_borne_prudente_sur_beane']:.3f}",
        f"Artefact linéaire : a <= {r['artefact_lineaire']['a_max_m_coefficient_1']:.3e} m = {r['artefact_lineaire']['rapport_a_longueur_Planck']:.3f} l_Pl",
        f"Maille de Planck : eta2 <= {r['maille_de_Planck']['eta2_max']:.3e}, {r['maille_de_Planck']['facteur_sous_la_limite_prudente']:.2e} fois sous la limite",
        f"Validité : a E / hbar c = {r['validite_developpement']['a_E_sur_hbar_c']:.2e} à 20 TeV",
        f"Xi et Shu : cohérent {x['EQG2_GeV_coherent_avec_eq3']:.3e} GeV, éq. (7) {x['EQG2_GeV_avec_eq7_imprimee']:.3e} GeV, "
        f"imprimé {x['EQG2_GeV_imprime_tableau_III']:.1e} GeV (x{x['imprime_sur_coherent']:.2f}) ; "
        f"n = 1 : {x['n1_constante_recalculee']:.2f} contre {x['n1_constante_imprimee_eq6']} ; "
        f"eps^2 theta2 = {x['n2_eps2_fois_theta2_recalcule']:.3e}",
    ]
    return '\n'.join(lignes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('resultats.json'))
    args = parser.parse_args()
    resultat = calculer()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2), encoding='utf-8')
    print(resume(resultat))
