#!/usr/bin/env python3
"""aeternam, test n° 5 : la réalité est-elle « rendue à la demande » d'un observateur ?

Idée testée (Bostrom, FAQ 2025, question 6 ; Campbell, Owhadi, Sauvageau et
Watkinson, « On testing the simulation theory », arXiv:1703.00058, § 4) : une
simulation économe ne calculerait les détails que lorsqu'un observateur peut les
connaître. Campbell et al. en tirent une prédiction précise (§ 4.2) : si
l'information « quel chemin » est détectée ou présente mais JAMAIS enregistrée
ni rendue disponible à un observateur, la figure d'interférence doit subsister.
La mécanique quantique prédit l'inverse : la visibilité V ne dépend que de
l'information physiquement présente dans le marqueur (distinguabilité D), qu'on
la lise ou non, avec D² + V² ≤ 1 (Englert, PRL 77, 2154, 1996).

Hypothèses comparées sur chaque jeu de données :
  MQ  : V = V0 · (réduction prévue par la mécanique quantique, sans observateur) ;
  HR  : « rendu à la demande » au sens de Campbell et al. § 4.2 : tant que
        l'information n'est ni lue ni enregistrée, V = V0 (visibilité sans marquage).

Données (valeurs publiées, dictionnaire VALEURS_PUBLIEES avec source exacte ;
points de mesure relevés dans les figures vectorielles des PDF arXiv par
extraire.py, fichier donnees/figures.json dont l'empreinte est vérifiée) :
  schwindt1999      V mesurée SANS analyseur (marqueur jamais lu) et K mesurée
                    AVEC analyseur (marqueur lu), même appareil : le test direct
                    « lu contre non lu » ;
  walborn2002       fentes d'Young, chemin marqué par des lames quart d'onde,
                    polarisation jamais analysée (fig. 3 et 7), puis effacement ;
  kim2000           effaceur à choix retardé : chemin lu (R03) ou effacé (R01, R02) ;
  hornberger2003    décohérence par collisions : l'information part dans des
                    molécules de gaz que personne ne détecte ;
  hackermuller2004  décohérence par émission thermique : photons absorbés par les
                    parois, jamais détectés ;
  ma2013            effacement quantique avec choix séparé du genre espace
                    (tableaux I et II) : indépendance vis-à-vis de l'ordre temporel.

Règle de décision (fixée avant les calculs) : HR est rejetée si, sur les jeux où
l'information n'est jamais lue ni enregistrée, l'écart combiné à HR dépasse 5 σ ;
les écarts à la MQ sont rapportés tels quels, sans correction. Ajouts décidés
après lecture des résultats, qui ne font que durcir la règle : (1) erreurs des
ajustements de franges multipliées par √(χ²/ddl) quand χ²/ddl > 1 ; (2) version
« prudente » où le χ² de HR sur Hackermüller et al. est divisé par le χ²/ddl de
la MQ (la courbe théorique publiée s'y écarte des points) ; (3) chaque jeu doit
aussi, seul, rejeter HR à plus de 5 σ.

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
FIGURES = ICI / 'donnees' / 'figures.json'
SHA_FIGURES = 'd0628f962815a717726a218f235e37d28e3bd4ea9918777553310d70d9fc649a'
GRAINE = 20260928
N_BOOTSTRAP = 300

# =========================================================================== valeurs publiées
# Chaque entrée : valeur, incertitude (None si l'article n'en donne pas), source exacte.
# Les pages sont celles des PDF arXiv dont les SHA-256 figurent dans sources.md.
VALEURS_PUBLIEES = {
    'schwindt1999': {
        'V2_plus_K2_moyenne_fig2': {
            'valeur': 0.976, 'incertitude': 0.017,
            'source': 'Schwindt, Kwiat, Englert, arXiv:quant-ph/9908072v1, p. 2, § II.A : '
                      '« The average of all the data points in Fig. 2 gives 0.976 ± 0.017 »'},
        'V2_plus_K2_visibilite_minimale': {
            'valeur': 0.998, 'incertitude': None,
            'source': 'idem, p. 2 : « for the minimum-visibility arrangement, V2 + K2 = 0.998 »'},
        'V_residuelle_minimale': {
            'valeur': 0.044, 'incertitude': None,
            'source': 'idem, p. 2 : « V > 4.4% even though L > 99.9% »'},
        'visibilite_intrinseque': {
            'valeur': 0.98, 'incertitude': None,
            'source': 'idem, p. 2 : « the intrinsic visibility of the interferometer [...] is only ~98% »'},
        'V2_plus_K2_melange_fig3a': {
            'valeur': 0.003, 'incertitude': 0.001,
            'source': 'idem, légende de la fig. 3, p. 3 : « average value for V2 + K2 of 0.003 ± 0.001 »'},
        'V2_plus_K2_melange_theorie_fig3a': {
            'valeur': 0.017, 'incertitude': 0.003,
            'source': 'idem, légende de la fig. 3, p. 3 : « the theoretical prediction [...] is 0.017±0.003 »'},
        'protocole_V': {
            'valeur': None, 'incertitude': None,
            'source': 'idem, p. 2 : « For Visibility measurements the polarization analyzer was lowered '
                      'out of the beam path » (le marqueur n\'est pas lu pendant la mesure de V)'},
    },
    'walborn2002': {
        'lambda_nm': {'valeur': 702.2, 'incertitude': None,
                      'source': 'Walborn et al., arXiv:quant-ph/0106078v1, p. 4, § IV'},
        'fentes_largeur_um': {'valeur': 200, 'incertitude': None, 'source': 'idem, p. 4, § IV'},
        'fentes_separation_um': {'valeur': 200, 'incertitude': None,
                                 'source': 'idem, p. 4 : « 200µm wide and separated by a distance of 200µm »'},
        'distance_cristal_fentes_cm': {'valeur': 42, 'incertitude': None, 'source': 'idem, p. 4, § IV'},
        'distance_cristal_Ds_cm': {'valeur': 125, 'incertitude': None, 'source': 'idem, p. 4, § IV'},
        'distance_cristal_Dp_retarde_cm': {'valeur': 200, 'incertitude': None,
                                           'source': 'idem, p. 4 : « a new distance of 2 meters »'},
        'duree_comptage_s': {'valeur': {'fig2': 400, 'fig3': 400, 'fig4': 800, 'fig5': 800,
                                        'fig6': 500, 'fig7': 500, 'fig8': 1000, 'fig9': 1000},
                             'incertitude': None,
                             'source': 'idem, axes des fig. 2 à 9, p. 8 à 15 (« Coincidence counts in … s »)'},
        'fig3_sans_interference': {
            'valeur': None, 'incertitude': None,
            'source': 'idem, p. 5 : « Figure 3 shows the absence of interference due to the quarter-wave plates. '
                      'Nearly all interference present in figure 2 was destroyed. The residual interference '
                      'present is due to a small error in aligning the quarter-wave plates. »'},
    },
    'kim2000': {
        'retard_effacement_ns': {'valeur': 8, 'incertitude': None,
                                 'source': 'Kim et al., arXiv:quant-ph/9903047v1, p. 2 : « at least 8ns later »'},
        'fente_largeur_mm': {'valeur': 0.3, 'incertitude': None, 'source': 'idem, p. 2 (« about 0.3mm »)'},
        'fente_distance_mm': {'valeur': 0.7, 'incertitude': None, 'source': 'idem, p. 2 (« about 0.7mm »)'},
    },
    'hornberger2003': {
        'visibilite_vide_pct': {'valeur': 41, 'incertitude': None,
                                'source': 'Hornberger et al., arXiv:quant-ph/0303093v1, p. 3 : '
                                          '« maximal vacuum visibility of 41% »'},
        'erreur_relative_pression': {'valeur': 0.15, 'incertitude': None,
                                     'source': 'idem, p. 4 : « uncertainty in the pressure measurement (about 15%) »'},
        'erreur_relative_theorie': {'valeur': 0.05, 'incertitude': None,
                                    'source': 'idem, p. 4 : « The uncertainty of the theoretical values amounts '
                                              'to about 5% (not drawn in the figure) »'},
        'sans_parametre_ajustable': {'valeur': None, 'incertitude': None,
                                     'source': 'idem, p. 3 : « our calculation, which contains no adjustable '
                                               'parameters, agrees well with the observed decrease »'},
    },
    'hackermuller2004': {
        'V0_a_pct': {'valeur': 47, 'incertitude': None,
                     'source': 'Hackermüller et al., arXiv:quant-ph/0402146v1, légende de la fig. 4, p. 4'},
        'V0_b_pct': {'valeur': 19, 'incertitude': None, 'source': 'idem, légende de la fig. 4, p. 4'},
        'photons_absorbes_parois': {'valeur': None, 'incertitude': None,
                                    'source': 'idem, p. 4 (Methods) : « the absorbing walls of the apparatus '
                                              'are located in the far-field »'},
        'ecart_theorie_alignement': {'valeur': None, 'incertitude': None,
                                     'source': 'idem, p. 4 : « The difference between the theoretical and the '
                                               'experimental curve is of the order of this variation. »'},
    },
    'ma2013': {
        # Tableau I (expérience de Vienne), p. 11 de arXiv:1206.6578v2 : I(i), V(ii) et relations
        # d'ordre entre la projection Pe du photon « environnement » et les événements Is du photon
        # « système » : 'avant', 'genre espace', 'apres'.
        'tableau_I': {
            'valeur': [
                {'scenario': 'I', 'Pe_vs_Is': 'avant', 'I': 0.956, 'sI': 0.008, 'V': 0.950, 'sV': 0.020},
                {'scenario': 'II', 'Pe_vs_Is': 'genre espace', 'I': 0.955, 'sI': 0.007, 'V': 0.951, 'sV': 0.018},
                {'scenario': 'III', 'Pe_vs_Is': 'genre espace', 'I': 0.953, 'sI': 0.009, 'V': 0.952, 'sV': 0.018},
                {'scenario': 'IV', 'Pe_vs_Is': 'apres', 'I': 0.957, 'sI': 0.007, 'V': 0.946, 'sV': 0.021},
                {'scenario': 'V', 'Pe_vs_Is': 'apres', 'I': 0.957, 'sI': 0.007, 'V': 0.943, 'sV': 0.021},
                {'scenario': 'VI', 'Pe_vs_Is': 'apres', 'I': 0.954, 'sI': 0.008, 'V': 0.950, 'sV': 0.019},
            ],
            'incertitude': 'écart-type entre parenthèses, statistique de Poisson (légende de la fig. 3)',
            'source': 'Ma et al., PNAS 110, 1221 (2013), arXiv:1206.6578v2, tableau I, p. 11'},
        # Tableau II (Canaries, 144 km), p. 13 ; délai du choix Ce par rapport à l'émission Ese :
        # +454 µs (II), 0 µs (II'), -721 µs (III), p. 12.
        'tableau_II': {
            'valeur': [
                {'scenario': 'II', 'Ce_moins_Ese_us': 454, 'I': 0.932, 'sI': 0.002, 'V': 0.756, 'sV': 0.002},
                {'scenario': "II'", 'Ce_moins_Ese_us': 0, 'I': 0.930, 'sI': 0.002, 'V': 0.776, 'sV': 0.002},
                {'scenario': 'III', 'Ce_moins_Ese_us': -721, 'I': 0.928, 'sI': 0.001, 'V': 0.751, 'sV': 0.001},
            ],
            'incertitude': 'écart-type entre parenthèses',
            'source': 'idem, tableau II, p. 13 ; délais p. 12 ; « These three scenarios gave similar results '
                      'up to statistical errors. »'},
        'fig3_I_i': {'valeur': 0.955, 'incertitude': 0.007, 'source': 'idem, p. 5'},
        'fig3_I_ii': {'valeur': 0.077, 'incertitude': 0.022, 'source': 'idem, p. 6'},
        'fig3_V_ii': {'valeur': 0.951, 'incertitude': 0.018, 'source': 'idem, p. 6'},
        'eta_I': {'valeur': 0.97, 'incertitude': None, 'source': 'idem, p. 12 (« a correction factor ηI of about 0.97 »)'},
        'eta_V': {'valeur': 0.95, 'incertitude': None, 'source': 'idem, p. 12 (« a correction factor ηV of about 0.95 »)'},
        'possibilite_suffit': {'valeur': None, 'incertitude': None,
                               'source': 'idem, p. 2 : « The presence of path information anywhere in the universe '
                                         'is sufficient to prohibit any possibility of interference. It is irrelevant '
                                         'whether a future observer might decide to acquire it. »'},
    },
    'campbell2017': {
        'prediction_4_2': {'valeur': None, 'incertitude': None,
                           'source': 'Campbell et al., arXiv:1703.00058v2, § 4.2, p. 9 : en retirant le compteur de '
                                     'coïncidences, « D0 should display the wave pattern if the experiment is successful »'},
    },
}


# =========================================================================== statistique
def log_q_gamma(a: float, x: float) -> float:
    """log de la fonction gamma incomplète supérieure régularisée Q(a, x)."""
    if x <= 0:
        return 0.0
    gln = math.lgamma(a)
    if x < a + 1:                                   # série pour P, puis Q = 1 - P
        ap, s, d = a, 1.0 / a, 1.0 / a
        for _ in range(10000):
            ap += 1
            d *= x / ap
            s += d
            if abs(d) < abs(s) * 1e-15:
                break
        p = math.exp(-x + a * math.log(x) - gln) * s
        return math.log(max(1.0 - p, 1e-300))
    b = x + 1 - a                                   # fraction continue (Lentz)
    c, d = 1e300, 1.0 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c
        c = 1e-300 if abs(c) < 1e-300 else c
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1) < 1e-15:
            break
    return -x + a * math.log(x) - gln + math.log(h)


def log_p_chi2(chi2: float, ddl: int) -> float:
    return log_q_gamma(ddl / 2, chi2 / 2)


def log_p_normale(z: float) -> float:
    """log de la p-valeur bilatérale erfc(|z|/√2), sans dépassement de capacité."""
    z = abs(z)
    if z < 30:
        return math.log(math.erfc(z / math.sqrt(2)))
    return -z * z / 2 - math.log(z * math.sqrt(math.pi / 2)) + math.log(1 - 1 / z**2 + 3 / z**4)


def sigma_equivalent(log_p: float) -> float:
    """z tel que la p-valeur bilatérale gaussienne vaille exp(log_p)."""
    if log_p >= 0:
        return 0.0
    lo, hi = 0.0, 1000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if log_p_normale(mid) > log_p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def moyenne_ponderee(v, s):
    v, s = np.asarray(v, float), np.asarray(s, float)
    w = 1 / s**2
    m = float(np.sum(w * v) / np.sum(w))
    chi2 = float(np.sum(w * (v - m) ** 2))
    return m, float(1 / math.sqrt(np.sum(w))), chi2, len(v) - 1


def nelder_mead(f, x0, pas, iterations=4000, tol=1e-10):
    x0 = np.asarray(x0, float)
    n = len(x0)
    simplexe = [x0] + [x0 + np.eye(n)[i] * pas[i] for i in range(n)]
    valeurs = [f(p) for p in simplexe]
    for _ in range(iterations):
        ordre = np.argsort(valeurs)
        simplexe = [simplexe[i] for i in ordre]
        valeurs = [valeurs[i] for i in ordre]
        if abs(valeurs[-1] - valeurs[0]) < tol * (1 + abs(valeurs[0])):
            break
        c = np.mean(simplexe[:-1], axis=0)
        xr = c + (c - simplexe[-1])
        fr = f(xr)
        if fr < valeurs[0]:
            xe = c + 2 * (c - simplexe[-1])
            fe = f(xe)
            simplexe[-1], valeurs[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < valeurs[-2]:
            simplexe[-1], valeurs[-1] = xr, fr
        else:
            xc = c + 0.5 * (simplexe[-1] - c)
            fc = f(xc)
            if fc < valeurs[-1]:
                simplexe[-1], valeurs[-1] = xc, fc
            else:
                simplexe = [simplexe[0]] + [simplexe[0] + 0.5 * (p - simplexe[0]) for p in simplexe[1:]]
                valeurs = [valeurs[0]] + [f(p) for p in simplexe[1:]]
    i = int(np.argmin(valeurs))
    return simplexe[i], valeurs[i]


# =========================================================================== ajustement de franges
def _lineaire(x, n, s, x0, w, periode):
    """Pour une géométrie donnée, N(x) = sinc²((x−x0)/w)·(a + b cos 2πx/Λ + c sin 2πx/Λ) est
    linéaire en (a, b, c) : moindres carrés pondérés exacts."""
    env = np.sinc((x - x0) / w) ** 2
    ph = 2 * np.pi * x / periode
    m = np.stack([env, env * np.cos(ph), env * np.sin(ph)], axis=1)
    mw = m / s[:, None]
    coef, *_ = np.linalg.lstsq(mw, n / s, rcond=None)
    r = n - m @ coef
    return coef, float(np.sum((r / s) ** 2)), m


def ajuster_franges(x, n, s, periode=None, depart=None, grille=True):
    """Ajuste visibilité V et phase φ. Si periode est donnée, elle est fixée (même géométrie que
    la figure de référence) ; sinon elle est ajustée. Renvoie un dictionnaire."""
    x, n, s = (np.asarray(v, float) for v in (x, n, s))
    libre = periode is None

    def f(p):
        x0, w = p[0], p[1]
        per = p[2] if libre else periode
        if w <= 0.2 or per <= 0.1:
            return 1e30
        coef, chi2, _ = _lineaire(x, n, s, x0, w, per)
        return chi2 if coef[0] > 0 else 1e30

    if depart is None:
        meilleur = None
        centre = float(np.sum(x * n) / np.sum(n))
        largeurs = np.arange(1.0, 12.01, 0.25)
        x0s = centre + np.arange(-1.0, 1.01, 0.1)
        pers = np.arange(0.4, 2.401, 0.01) if libre else [None]
        for per in pers:
            for w in largeurs:
                for x0 in x0s:
                    p = (x0, w, per) if libre else (x0, w)
                    v = f(p)
                    if meilleur is None or v < meilleur[0]:
                        meilleur = (v, p)
        depart = meilleur[1]
    pas = [0.05, 0.2, 0.01] if libre else [0.05, 0.2]
    p, chi2 = nelder_mead(f, depart, pas[:len(depart)])
    per = p[2] if libre else periode
    coef, chi2, m = _lineaire(x, n, s, p[0], p[1], per)
    a, b, c = coef
    return {'x0_mm': float(p[0]), 'largeur_enveloppe_mm': float(p[1]), 'periode_mm': float(per),
            'V': float(math.hypot(b, c) / a), 'phase_rad': float(math.atan2(c, b)),
            'chi2': chi2, 'ddl': len(x) - (6 if libre else 5), 'params': [float(v) for v in p],
            'modele': (m @ coef).tolist()}


def gonfle(ajust):
    """Facteur d'échelle des erreurs quand le modèle décrit mal les données (χ²/ddl > 1)."""
    return math.sqrt(max(1.0, ajust['chi2'] / ajust['ddl']))


def bootstrap_franges(x, s, ajust, periode, rng, n_rep=N_BOOTSTRAP):
    """Erreur sur V et φ par bootstrap paramétrique : données simulées = modèle ajusté + bruit
    gaussien d'écart-type s (les barres publiées), ajustement complet refait à chaque tirage ;
    l'écart-type obtenu est multiplié par √(χ²/ddl) quand χ²/ddl > 1 (choix prudent)."""
    modele = np.asarray(ajust['modele'])
    vs, phs = [], []
    for _ in range(n_rep):
        n_sim = modele + s * rng.standard_normal(len(s))
        r = ajuster_franges(x, n_sim, s, periode=periode, depart=ajust['params'])
        vs.append(r['V'])
        phs.append(r['phase_rad'])
    phs = np.unwrap(np.asarray(phs) - ajust['phase_rad']) + ajust['phase_rad']
    g = gonfle(ajust)
    return g * float(np.std(vs, ddof=1)), g * float(np.std(phs, ddof=1)), vs


# =========================================================================== autotests
def autotests():
    rng = np.random.default_rng(1)
    # 1. loi du χ² : valeurs connues
    assert abs(math.exp(log_p_chi2(3.841458820694124, 1)) - 0.05) < 1e-9
    assert abs(math.exp(log_p_chi2(10.0, 2)) - math.exp(-5)) < 1e-12
    assert abs(math.exp(log_p_chi2(0.5, 4)) - 0.9735009788392561) < 1e-9
    assert abs(sigma_equivalent(math.log(0.0026997960632601866)) - 3.0) < 1e-6
    assert abs(sigma_equivalent(log_p_normale(40.0)) - 40.0) < 1e-6
    # 2. inégalité d'Englert D² + V² ≤ 1 sur des états aléatoires (chemin ⊗ marqueur de dimension m) :
    #    V = 2 |Tr_M ρ12|, D = Tr_M |ρ11 − ρ22| (norme trace) ; égalité pour un marqueur pur et
    #    des chemins équiprobables (Englert 1996, cité par Schwindt et al. éq. (1))
    for m in (2, 3, 5):
        for _ in range(300):
            k = int(rng.integers(1, 2 * m + 1))
            a = rng.standard_normal((2 * m, k)) + 1j * rng.standard_normal((2 * m, k))
            rho = a @ a.conj().T
            rho /= np.trace(rho).real
            r11, r22, r12 = rho[:m, :m], rho[m:, m:], rho[:m, m:]
            v = 2 * abs(np.trace(r12))
            d = float(np.sum(np.abs(np.linalg.eigvalsh(r11 - r22))))
            assert d * d + v * v <= 1 + 1e-9, (d, v)
        for _ in range(100):                       # cas pur et équiprobable : égalité
            m1 = rng.standard_normal(m) + 1j * rng.standard_normal(m)
            m2 = rng.standard_normal(m) + 1j * rng.standard_normal(m)
            m1 /= np.linalg.norm(m1)
            m2 /= np.linalg.norm(m2)
            psi = np.concatenate([m1, m2]) / math.sqrt(2)
            rho = np.outer(psi, psi.conj())
            v = 2 * abs(np.trace(rho[:m, m:]))
            d = float(np.sum(np.abs(np.linalg.eigvalsh(rho[:m, :m] - rho[m:, m:]))))
            assert abs(d * d + v * v - 1) < 1e-9
            assert abs(v - abs(np.vdot(m1, m2))) < 1e-9          # V = |⟨M1|M2⟩|
    # 3. ajustement de franges : on retrouve V connue sur des données simulées
    x = np.linspace(-4.2, 4.2, 29)
    for v_vrai in (0.0, 0.3, 0.8):
        env = np.sinc((x - 0.2) / 3.5) ** 2
        n_vrai = 150 * env * (1 + v_vrai * np.cos(2 * np.pi * x / 1.4 + 0.7)) + 1e-9
        s = np.sqrt(np.maximum(n_vrai, 1))
        r = ajuster_franges(x, n_vrai, s)
        assert abs(r['V'] - v_vrai) < 1e-3 and r['chi2'] < 1e-6, (v_vrai, r['V'], r['chi2'])
        if v_vrai > 0:
            assert abs(r['periode_mm'] - 1.4) < 1e-3
    # 4. Nelder-Mead sur Rosenbrock
    p, _ = nelder_mead(lambda q: (1 - q[0]) ** 2 + 100 * (q[1] - q[0] ** 2) ** 2, [-1.2, 1.0], [0.1, 0.1])
    assert np.allclose(p, [1, 1], atol=1e-4)
    return 'ok'


# =========================================================================== données
def charger():
    brut = FIGURES.read_bytes()
    sha = hashlib.sha256(brut).hexdigest()
    if sha != SHA_FIGURES:
        raise SystemExit(f'donnees/figures.json : SHA-256 {sha} au lieu de {SHA_FIGURES} (refaire extraire.py ?)')
    return json.loads(brut)


# =========================================================================== Schwindt et al.
def schwindt(fig):
    s = fig['schwindt1999']
    th = np.array([p['angle_deg'] for p in s['V']])
    V = np.array([p['valeur'] for p in s['V']])
    sV = np.array([p['erreur'] for p in s['V']])
    K = np.array([p['valeur'] for p in s['K_optimise']])
    sK = np.array([p['erreur'] for p in s['K_optimise']])
    S_fig = np.array([p['valeur'] for p in s['V2_plus_K2']])
    assert len(th) == 7 and np.allclose(th, np.arange(7) * 7.5, atol=0.05)
    th = np.round(th / 7.5) * 7.5
    # (a) D² + V² ≤ 1 point par point (K optimisé ≈ D, Schwindt et al. p. 1)
    S = V**2 + K**2
    sS = np.sqrt((2 * V * sV) ** 2 + (2 * K * sK) ** 2)
    z_exces = (S - 1) / sS
    pub = VALEURS_PUBLIEES['schwindt1999']
    # contrôles de l'extraction : les points V²+K² tracés par les auteurs = V² + K² des points relevés,
    # et leur moyenne = valeur imprimée
    ecart_trace = float(np.max(np.abs(S - S_fig)))
    assert ecart_trace < 0.02, ecart_trace
    moyenne_fig = float(np.mean(S_fig))
    assert abs(moyenne_fig - pub['V2_plus_K2_moyenne_fig2']['valeur']) < 0.01
    assert abs(S_fig[-1] - pub['V2_plus_K2_visibilite_minimale']['valeur']) < 0.005
    assert abs(V[-1] - pub['V_residuelle_minimale']['valeur']) < 0.002
    # (a') prédiction quantique sans observateur : lame demi-onde à θ → polarisations séparées de 2θ :
    #      V = V0 |cos 2θ|, D = |sin 2θ|
    V0, sV0 = V[0], sV[0]
    V_mq = V0 * np.abs(np.cos(np.radians(2 * th)))
    D_mq = np.abs(np.sin(np.radians(2 * th)))
    # (b) test direct lu / non lu. V est mesurée analyseur retiré (marqueur jamais lu), K avec
    # l'analyseur (marqueur lu). Q = (V/V0)² + K². MQ : Q = 1 (marqueur pur). HR : pendant la mesure
    # de V rien n'est lu, donc V = V0 et Q = 1 + K².
    i = slice(1, None)                                 # θ = 0 sert à fixer V0
    Q = (V[i] / V0) ** 2 + K[i] ** 2
    sQ = np.sqrt((2 * V[i] / V0**2 * sV[i]) ** 2 + (2 * V[i] ** 2 / V0**3 * sV0) ** 2 + (2 * K[i] * sK[i]) ** 2)
    chi2_mq = float(np.sum(((Q - 1) / sQ) ** 2))
    chi2_hr = float(np.sum(((Q - 1 - K[i] ** 2) / sQ) ** 2))
    ddl = len(Q)
    # visibilité observée contre HR, point par point (V attendue = V0)
    z_hr_V = (V0 - V[i]) / np.sqrt(sV[i] ** 2 + sV0**2)
    # fraction de la perte d'interférence prévue par la MQ qui a lieu sans lecture : 1 (MQ), 0 (HR)
    f = (V0 - V[i]) / (V0 - V_mq[i])
    sf = np.sqrt(sV[i] ** 2 + sV0**2) / (V0 - V_mq[i])
    f_moy, f_err, f_chi2, f_ddl = moyenne_ponderee(f, sf)
    return {
        'angles_deg': th.tolist(), 'V_non_lu': V.tolist(), 'sV': sV.tolist(),
        'K_lu': K.tolist(), 'sK': sK.tolist(),
        'V2_plus_K2': [round(v, 4) for v in S.tolist()], 'sV2_plus_K2': [round(v, 4) for v in sS.tolist()],
        'V2_plus_K2_max': round(float(S.max()), 4),
        'z_max_au_dessus_de_1': round(float(z_exces.max()), 2),
        'inegalite_respectee': bool(np.all(z_exces < 2)),
        'controle_extraction': {'ecart_max_V2K2_recalcule_trace': round(ecart_trace, 4),
                                'moyenne_V2K2_relevee': round(moyenne_fig, 4),
                                'moyenne_V2K2_publiee': pub['V2_plus_K2_moyenne_fig2']['valeur'],
                                'V2K2_45deg_releve': round(float(S_fig[-1]), 4),
                                'V_45deg_relevee': round(float(V[-1]), 4)},
        'melange_fig3a_z_mesure_contre_theorie': round(
            (pub['V2_plus_K2_melange_theorie_fig3a']['valeur'] - pub['V2_plus_K2_melange_fig3a']['valeur'])
            / math.hypot(pub['V2_plus_K2_melange_theorie_fig3a']['incertitude'],
                         pub['V2_plus_K2_melange_fig3a']['incertitude']), 1),
        'fraction_min_max': [round(float(f.min()), 3), round(float(f.max()), 3)],
        'V0': round(float(V0), 4),
        'V_mq': [round(v, 4) for v in V_mq.tolist()], 'D_mq': [round(v, 4) for v in D_mq.tolist()],
        'ecart_max_V_moins_V_mq': round(float(np.max(np.abs(V - V_mq))), 4),
        'ecart_max_K_moins_D_mq': round(float(np.max(np.abs(K - D_mq))), 4),
        'Q_lu_non_lu': [round(v, 4) for v in Q.tolist()], 'sQ': [round(v, 4) for v in sQ.tolist()],
        'Q_attendu_HR': [round(v, 4) for v in (1 + K[i] ** 2).tolist()],
        'chi2_MQ': round(chi2_mq, 2), 'chi2_HR': round(chi2_hr, 1), 'ddl': ddl,
        'p_MQ': math.exp(log_p_chi2(chi2_mq, ddl)),
        'sigma_rejet_HR': round(sigma_equivalent(log_p_chi2(chi2_hr, ddl)), 1),
        'V_45deg': round(float(V[-1]), 4), 'z_HR_45deg': round(float(z_hr_V[-1]), 0),
        'z_HR_V_par_angle': [round(v, 1) for v in z_hr_V.tolist()],
        'fraction_perte_MQ_sans_lecture': round(f_moy, 4), 'fraction_err': round(f_err, 4),
        'fraction_chi2': round(f_chi2, 2), 'fraction_ddl': f_ddl,
        'fraction_par_angle': [round(v, 3) for v in f.tolist()],
    }


# =========================================================================== Walborn et al.
def walborn(fig, rng):
    w = fig['walborn2002']

    def serie(nom):
        pts = w[nom]['points']
        x = np.array([p['x_mm'] for p in pts])
        n = np.array([p['coups'] for p in pts])
        s = np.array([p['erreur'] if p['erreur'] is not None else math.sqrt(max(p['coups'], 1)) for p in pts])
        return x, n, np.maximum(s, 1.0)

    out = {}
    for ref, marques in (('fig2', ('fig3', 'fig4', 'fig5')), ('fig6', ('fig7', 'fig8', 'fig9'))):
        x, n, s = serie(ref)
        r = ajuster_franges(x, n, s)
        sv, sph, _ = bootstrap_franges(x, s, r, None, rng)
        out[ref] = {'V': r['V'], 'sV': sv, 'phase_rad': r['phase_rad'], 'sphase': sph,
                    'periode_mm': r['periode_mm'], 'chi2': r['chi2'], 'ddl': r['ddl'],
                    'largeur_enveloppe_mm': r['largeur_enveloppe_mm']}
        for nom in marques:
            x, n, s = serie(nom)
            q = ajuster_franges(x, n, s, periode=r['periode_mm'])
            sv, sph, _ = bootstrap_franges(x, s, q, r['periode_mm'], rng)
            out[nom] = {'V': q['V'], 'sV': sv, 'phase_rad': q['phase_rad'], 'sphase': sph,
                        'chi2': q['chi2'], 'ddl': q['ddl']}
        # somme franges + anti-franges (même durée de comptage) : doit redonner la figure sans franges
        a, b = marques[1], marques[2]
        xa, na, sa = serie(a)
        xb, nb, sb = serie(b)
        assert np.allclose(xa, xb, atol=0.01)
        ssum = np.sqrt(sa**2 + sb**2)
        q = ajuster_franges(xa, na + nb, ssum, periode=r['periode_mm'])
        sv, _, _ = bootstrap_franges(xa, ssum, q, r['periode_mm'], rng)
        out[f'{a}+{b}'] = {'V': q['V'], 'sV': sv, 'chi2': q['chi2'], 'ddl': q['ddl'],
                           'z_contre_figure_marquee': (q['V'] - out[marques[0]]['V']) / math.hypot(sv, out[marques[0]]['sV'])}
    # période attendue : λ L / d, L = distance fentes → Ds, d = distance entre centres des fentes
    pub = VALEURS_PUBLIEES['walborn2002']
    L = (pub['distance_cristal_Ds_cm']['valeur'] - pub['distance_cristal_fentes_cm']['valeur']) * 1e-2
    d = (pub['fentes_largeur_um']['valeur'] + pub['fentes_separation_um']['valeur']) * 1e-6
    periode_attendue = pub['lambda_nm']['valeur'] * 1e-9 * L / d * 1e3
    for ref in ('fig2', 'fig6'):        # contrôle : l'interfrange ajusté est celui de la géométrie publiée
        assert abs(out[ref]['periode_mm'] / periode_attendue - 1) < 0.1, (ref, out[ref]['periode_mm'])
    res = {k: {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in out.items()}
    # test HR : fig. 3 et 7, chemin marqué, polarisation jamais analysée ni enregistrée
    tests = {}
    for ref, marq in (('fig2', 'fig3'), ('fig6', 'fig7')):
        vr, sr, vm, sm = out[ref]['V'], out[ref]['sV'], out[marq]['V'], out[marq]['sV']
        rapport = vm / vr
        srap = rapport * math.hypot(sm / vm if vm > 0 else 0, sr / vr)
        z = (vr - vm) / math.hypot(sr, sm)
        tests[f'{marq}_sur_{ref}'] = {'rapport_V': round(rapport, 4), 'rapport_err': round(math.hypot(sm, rapport * sr) / vr, 4),
                                      'z_HR': round(z, 1)}
    # différé contre non différé (Dp à 98 cm puis à 2 m) : l'ordre des détections ne change rien
    ordre = {}
    for a, b in (('fig4', 'fig8'), ('fig5', 'fig9')):
        ra, rb = out[a]['V'] / out['fig2']['V'], out[b]['V'] / out['fig6']['V']
        sra = ra * math.hypot(out[a]['sV'] / out[a]['V'], out['fig2']['sV'] / out['fig2']['V'])
        srb = rb * math.hypot(out[b]['sV'] / out[b]['V'], out['fig6']['sV'] / out['fig6']['V'])
        ordre[f'{a}_contre_{b}'] = {'V_efface_sur_V_ref_non_differe': round(ra, 3),
                                    'V_efface_sur_V_ref_differe': round(rb, 3),
                                    'z_difference': round((ra - rb) / math.hypot(sra, srb), 2)}
    dphi = {}
    for a, b in (('fig4', 'fig5'), ('fig8', 'fig9')):
        dp = (out[b]['phase_rad'] - out[a]['phase_rad']) % (2 * math.pi)
        dphi[f'{a}_{b}'] = {'dephasage_sur_pi': round(dp / math.pi, 3),
                            'err_sur_pi': round(math.hypot(out[a]['sphase'], out[b]['sphase']) / math.pi, 3)}
    ctrl = [w[k]['controle'] for k in w]
    releve = {'ecart_max_a_un_entier': max(c['ecart_max_a_un_entier'] for c in ctrl),
              'erreur_sur_racine_N_moyenne_min': min(c['erreur_sur_racine_N_moyenne'] for c in ctrl),
              'erreur_sur_racine_N_moyenne_max': max(c['erreur_sur_racine_N_moyenne'] for c in ctrl),
              'residu_etalonnage_max_pt': round(max(w[k]['etalonnage']['residu_max_pt'] for k in w), 3)}
    return {'controle_releve': releve, 'ajustements': res, 'periode_attendue_mm': round(periode_attendue, 3), 'test_HR': tests,
            'ordre_des_detections': ordre, 'dephasage_franges_antifranges': dphi}


# =========================================================================== Kim et al.
def kim(fig, rng):
    k = fig['kim2000']

    def serie(nom):
        pts = k[nom]['points']
        x = np.array([p['x_mm'] for p in pts])
        n = np.array([float(round(p['coups'])) for p in pts])      # comptages entiers (écart < 0,1, extraire.py)
        return x, n, np.sqrt(np.maximum(n, 1.0))                 # Poisson : l'article ne trace pas de barres

    x1, n1, s1 = serie('R01')
    r1 = ajuster_franges(x1, n1, s1)
    sv1, sph1, _ = bootstrap_franges(x1, s1, r1, None, rng)
    out = {'R01': {'V': r1['V'], 'sV': sv1, 'phase_rad': r1['phase_rad'], 'sphase': sph1,
                   'periode_mm': r1['periode_mm'], 'chi2': r1['chi2'], 'ddl': r1['ddl']}}
    for nom in ('R02', 'R03'):
        x, n, s = serie(nom)
        q = ajuster_franges(x, n, s, periode=r1['periode_mm'])
        sv, sph, _ = bootstrap_franges(x, s, q, r1['periode_mm'], rng)
        out[nom] = {'V': q['V'], 'sV': sv, 'phase_rad': q['phase_rad'], 'sphase': sph,
                    'chi2': q['chi2'], 'ddl': q['ddl']}
    x2, n2, s2 = serie('R02')
    assert np.allclose(x1, x2, atol=0.01)
    q = ajuster_franges(x1, n1 + n2, np.sqrt(n1 + n2), periode=r1['periode_mm'])
    sv, _, _ = bootstrap_franges(x1, np.sqrt(n1 + n2), q, r1['periode_mm'], rng)
    out['R01+R02'] = {'V': q['V'], 'sV': sv, 'chi2': q['chi2'], 'ddl': q['ddl']}
    dp = (out['R02']['phase_rad'] - out['R01']['phase_rad']) % (2 * math.pi)
    rap = out['R03']['V'] / out['R01']['V']
    srap = math.hypot(out['R03']['sV'], rap * out['R01']['sV']) / out['R01']['V']
    res = {k2: {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k2, v in out.items()}
    return {'ajustements': res,
            'dephasage_R01_R02_sur_pi': round(dp / math.pi, 3),
            'dephasage_err_sur_pi': round(math.hypot(out['R01']['sphase'], out['R02']['sphase']) / math.pi, 3),
            'rapport_V_R03_sur_R01': round(rap, 4), 'rapport_err': round(srap, 4)}


# =========================================================================== Hornberger et al.
def hornberger(fig):
    h = fig['hornberger2003']
    pts = h['fig2']['points']
    p = np.array([q['p_1e-6_mbar'] for q in pts])
    V = np.array([q['visibilite_pct'] for q in pts])
    hi = np.array([q['barre_haute_pct'] for q in pts])
    lo = np.array([q['barre_basse_pct'] if q['barre_basse_pct'] is not None else np.nan for q in pts])
    s_ln = np.where(np.isnan(lo), np.log(hi / V), 0.5 * (np.log(hi) - np.log(np.where(np.isnan(lo), 1, lo))))
    # ajustement exponentiel pondéré en échelle log : ln V = ln V0 − p/p0
    wgt = 1 / s_ln**2
    A = np.stack([np.ones_like(p), p], axis=1)
    cov = np.linalg.inv(A.T @ (A * wgt[:, None]))
    c = cov @ (A.T @ (wgt * np.log(V)))
    p0_fit = -1 / c[1]
    s_p0 = math.sqrt(cov[1, 1]) / c[1] ** 2
    chi2_fit = float(np.sum(wgt * (np.log(V) - A @ c) ** 2))
    # droite théorique tracée par les auteurs (sans paramètre ajustable)
    t = h['fig2']['theorie_extremites']
    Vt0, Vt1, pt0, pt1 = t[0]['visibilite_pct'], t[1]['visibilite_pct'], t[0]['p_1e-6_mbar'], t[1]['p_1e-6_mbar']
    p0_th = (pt1 - pt0) / math.log(Vt0 / Vt1)
    V_th = Vt0 * np.exp(-(p - pt0) / p0_th)
    chi2_th = float(np.sum(((np.log(V) - np.log(V_th)) / s_ln) ** 2))
    # HR : les molécules de gaz ne sont jamais détectées → V constante, égale à la visibilité à
    # pression nulle de la théorie (V0 prise au plus favorable à HR : la plus basse des deux valeurs
    # V0 ajustée / V0 théorique)
    V0_hr = min(Vt0 * math.exp(pt0 / p0_th), math.exp(c[0]))
    z_hr = (math.log(V0_hr) - np.log(V)) / s_ln
    chi2_hr = float(np.sum(z_hr**2))
    ddl = len(p)
    # fig. 3 : dix gaz, p0 mesuré contre p0 calculé
    g = h['fig3']['points']
    pm = np.array([q['p0_mesure'] for q in g])
    sm = np.array([q['p0_erreur'] for q in g])
    pth = np.array([q['p0_theorie'] if q['p0_theorie'] is not None else np.nan for q in g])
    # N2 et air partagent le même σ_eff et un seul carré théorique
    for i, q in enumerate(g):
        if np.isnan(pth[i]):
            j = [k for k, r in enumerate(g) if abs(r['sigma_eff_nm2'] - q['sigma_eff_nm2']) < 0.5 and r['p0_theorie'] is not None]
            assert len(j) == 1
            pth[i] = pth[j[0]]
    err_th = VALEURS_PUBLIEES['hornberger2003']['erreur_relative_theorie']['valeur']
    stot = np.sqrt(sm**2 + (err_th * pth) ** 2)
    chi2_g = float(np.sum(((pm - pth) / stot) ** 2))
    # HR : aucune décohérence → 1/p0 = 0 ; écart de chaque gaz en σ : (1/p0)/(σ_p0/p0²) = p0/σ_p0
    z_g_hr = pm / sm
    chi2_g_hr = float(np.sum(z_g_hr**2))
    rel = sm / pm
    return {
        'fig2': {'n_points': len(p), 'p0_ajuste_1e-6_mbar': round(p0_fit, 3), 'p0_ajuste_err': round(s_p0, 3),
                 'V0_ajustee_pct': round(math.exp(c[0]), 2), 'chi2_exponentielle': round(chi2_fit, 2), 'ddl_exp': ddl - 2,
                 'p0_theorie_1e-6_mbar': round(p0_th, 3), 'V0_theorie_pct': round(Vt0 * math.exp(pt0 / p0_th), 2),
                 'chi2_MQ_sans_parametre': round(chi2_th, 2), 'ddl_MQ': ddl,
                 'p_MQ': math.exp(log_p_chi2(chi2_th, ddl)),
                 'V_derniere_pct': round(float(V[-1]), 2), 'p_derniere': round(float(p[-1]), 3),
                 'chi2_HR': round(chi2_hr, 0), 'sigma_rejet_HR': round(sigma_equivalent(log_p_chi2(chi2_hr, ddl)), 1),
                 'V0_HR_pct': round(V0_hr, 2)},
        'fig3': {'n_gaz': len(g), 'gaz': [q['gaz'] for q in g], 'p0_mesure': pm.tolist(), 'p0_err': sm.tolist(),
                 'p0_theorie': [round(v, 4) for v in pth.tolist()],
                 'erreur_relative_mesure_mediane': round(float(np.median(rel)), 3),
                 'chi2_MQ': round(chi2_g, 2), 'ddl': len(g), 'p_MQ': math.exp(log_p_chi2(chi2_g, len(g))),
                 'rapport_mesure_sur_theorie_moyen': round(float(np.mean(pm / pth)), 3),
                 'chi2_HR': round(chi2_g_hr, 1),
                 'sigma_rejet_HR': round(sigma_equivalent(log_p_chi2(chi2_g_hr, len(g))), 1)},
    }


# =========================================================================== Hackermüller et al.
def hackermuller(fig):
    h = fig['hackermuller2004']
    out = {}
    for pan in ('a', 'b'):
        pts = [q for q in h[pan] if q['erreur'] is not None]
        P = np.array([q['puissance_W'] for q in pts])
        V = np.array([q['visibilite_normalisee'] for q in pts])
        s = np.array([q['erreur'] for q in pts])
        th = h[f'theorie_{pan}']
        Vt = np.interp(P, [q['puissance_W'] for q in th], [q['visibilite_normalisee'] for q in th])
        chi2_mq = float(np.sum(((V - Vt) / s) ** 2))
        chi2_hr = float(np.sum(((V - 1) / s) ** 2))           # HR : photons jamais détectés → V/V0 = 1
        sel = P > 7.5                                        # plus hautes puissances
        g = max(1.0, chi2_mq / len(P))                       # erreurs gonflées pour que la MQ ait χ²/ddl = 1
        out[pan] = {'n_points_avec_barre': len(P), 'n_points_total': len(h[pan]),
                    'chi2_HR_conservateur': round(chi2_hr / g, 0),
                    'sigma_rejet_HR_conservateur': round(sigma_equivalent(log_p_chi2(chi2_hr / g, len(P))), 1),
                    'chi2_MQ': round(chi2_mq, 1), 'ddl': len(P),
                    'chi2_MQ_par_ddl': round(chi2_mq / len(P), 2),
                    'ecart_max_MQ': round(float(np.max(np.abs(V - Vt))), 3),
                    'chi2_HR': round(chi2_hr, 0), 'sigma_rejet_HR': round(sigma_equivalent(log_p_chi2(chi2_hr, len(P))), 1),
                    'V_norm_moyenne_P_sup_7_5W': round(float(np.mean(V[sel])), 3),
                    'V_norm_theorie_moyenne_P_sup_7_5W': round(float(np.mean(Vt[sel])), 3),
                    'n_points_P_sup_7_5W': int(sel.sum())}
    return out


# =========================================================================== Ma et al.
def ma():
    pub = VALEURS_PUBLIEES['ma2013']
    out = {}
    for tab in ('tableau_I', 'tableau_II'):
        L = pub[tab]['valeur']
        mv, sv, cv, dv = moyenne_ponderee([r['V'] for r in L], [r['sV'] for r in L])
        mi, si, ci, di = moyenne_ponderee([r['I'] for r in L], [r['sI'] for r in L])
        out[tab] = {'V_moyenne': round(mv, 4), 'V_err': round(sv, 4), 'chi2_V': round(cv, 2), 'ddl': dv,
                    'p_V_homogene': math.exp(log_p_chi2(cv, dv)),
                    'I_moyenne': round(mi, 4), 'I_err': round(si, 4), 'chi2_I': round(ci, 2),
                    'p_I_homogene': math.exp(log_p_chi2(ci, di))}
    L = pub['tableau_I']['valeur']
    av = [r for r in L if r['Pe_vs_Is'] == 'avant']
    ap = [r for r in L if r['Pe_vs_Is'] == 'apres']
    m_av, s_av, _, _ = moyenne_ponderee([r['V'] for r in av], [r['sV'] for r in av])
    m_ap, s_ap, _, _ = moyenne_ponderee([r['V'] for r in ap], [r['sV'] for r in ap])
    out['tableau_I']['V_projection_avant'] = round(m_av, 4)
    out['tableau_I']['V_projection_apres'] = round(m_ap, 4)
    out['tableau_I']['difference_apres_moins_avant'] = round(m_ap - m_av, 4)
    out['tableau_I']['difference_err'] = round(math.hypot(s_av, s_ap), 4)
    L2 = pub['tableau_II']['valeur']
    ecarts = {}
    for i in range(3):
        for j in range(i + 1, 3):
            a, b = L2[i], L2[j]
            ecarts[f"{a['scenario']}_{b['scenario']}"] = round((a['V'] - b['V']) / math.hypot(a['sV'], b['sV']), 1)
    out['tableau_II']['z_ecarts_V_par_paire'] = ecarts
    I2, V2 = pub['fig3_I_ii']['valeur'], pub['fig3_V_ii']['valeur']
    sI2, sV2 = pub['fig3_I_ii']['incertitude'], pub['fig3_V_ii']['incertitude']
    S = I2**2 + V2**2
    sS = math.hypot(2 * I2 * sI2, 2 * V2 * sV2)
    eI, eV = pub['eta_I']['valeur'], pub['eta_V']['valeur']
    out['complementarite_fig3'] = {'I2_plus_V2': round(S, 4), 'err': round(sS, 4),
                                   'z_au_dessus_de_1': round((S - 1) / sS, 2),
                                   'corrige_eta': round((I2 / eI) ** 2 + (V2 / eV) ** 2, 4),
                                   'corrige_eta_err': round(math.hypot(2 * I2 / eI**2 * sI2, 2 * V2 / eV**2 * sV2), 4)}
    return out


# =========================================================================== principal
def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', type=Path, default=ICI / 'resultats.json')
    args = ap.parse_args()
    res = {'test': 'aeternam, test n° 5 : rendu à la demande', 'autotests': autotests()}
    fig = charger()
    rng = np.random.default_rng(GRAINE)
    res['donnees'] = {'figures_json_sha256': SHA_FIGURES, 'pdf': fig['pdf'], 'graine': GRAINE,
                      'bootstrap_tirages': N_BOOTSTRAP}
    res['donnees']['residu_etalonnage_max_pt_toutes_figures'] = round(max(
        [fig['walborn2002'][k]['etalonnage']['residu_max_pt'] for k in fig['walborn2002']]
        + [fig['kim2000'][k]['etalonnage']['residu_max_pt'] for k in ('R01', 'R02', 'R03')]
        + [fig['schwindt1999']['etalonnage']['residu_max_pt'], fig['hackermuller2004']['etalonnage']['residu_max_pt'],
           fig['hornberger2003']['fig2']['etalonnage']['residu_max_pt'],
           fig['hornberger2003']['fig3']['etalonnage']['residu_max_pt']]), 3)
    res['schwindt1999'] = schwindt(fig)
    res['walborn2002'] = walborn(fig, rng)
    res['kim2000'] = kim(fig, rng)
    res['hornberger2003'] = hornberger(fig)
    res['hackermuller2004'] = hackermuller(fig)
    res['ma2013'] = ma()

    # ------------------------------------------------------------------ lu contre non lu
    sw, wb, km = res['schwindt1999'], res['walborn2002'], res['kim2000']
    non_lu = [(wb['test_HR']['fig3_sur_fig2']['rapport_V'], wb['test_HR']['fig3_sur_fig2']['rapport_err']),
              (wb['test_HR']['fig7_sur_fig6']['rapport_V'], wb['test_HR']['fig7_sur_fig6']['rapport_err'])]
    m_nl, s_nl, _, _ = moyenne_ponderee([v for v, _ in non_lu], [e for _, e in non_lu])
    lu, s_lu = km['rapport_V_R03_sur_R01'], km['rapport_err']
    res['lu_contre_non_lu'] = {
        'description': 'visibilité résiduelle relative V_marqué/V_référence, chemin marqué à fond : '
                       'jamais lu (Walborn fig. 3 et 7) contre lu par un détecteur (Kim R03)',
        'non_lu_walborn': round(m_nl, 4), 'non_lu_err': round(s_nl, 4),
        'lu_kim_R03': lu, 'lu_err': s_lu,
        'difference_non_lu_moins_lu': round(m_nl - lu, 4), 'difference_err': round(math.hypot(s_nl, s_lu), 4),
        'z_difference': round((m_nl - lu) / math.hypot(s_nl, s_lu), 2),
        'HR_predit_difference': 1.0,
        'z_HR': round((1 - (m_nl - lu)) / math.hypot(s_nl, s_lu), 1),
        'schwindt_Q_moyen': round(moyenne_ponderee(sw['Q_lu_non_lu'], sw['sQ'])[0], 4),
        'schwindt_Q_err': round(moyenne_ponderee(sw['Q_lu_non_lu'], sw['sQ'])[1], 4),
    }

    # ------------------------------------------------------------------ verdict
    # rejet combiné de HR sur les jeux où l'information n'est jamais lue ni enregistrée ;
    # jeux indépendants : on additionne les χ² (chaque jeu contribue par son χ² propre)
    composantes = {
        'schwindt1999_Q': (sw['chi2_HR'], sw['ddl']),
        'walborn2002_fig3': (wb['test_HR']['fig3_sur_fig2']['z_HR'] ** 2, 1),
        'walborn2002_fig7': (wb['test_HR']['fig7_sur_fig6']['z_HR'] ** 2, 1),
        'hornberger2003_fig2': (res['hornberger2003']['fig2']['chi2_HR'], res['hornberger2003']['fig2']['ddl_MQ']),
        'hackermuller2004_a': (res['hackermuller2004']['a']['chi2_HR'], res['hackermuller2004']['a']['ddl']),
        'hackermuller2004_b': (res['hackermuller2004']['b']['chi2_HR'], res['hackermuller2004']['b']['ddl']),
    }
    # version prudente : pour Hackermüller, χ² divisé par χ²_MQ/ddl (la MQ elle-même s'y ajuste mal)
    prudentes = dict(composantes)
    for pan in ('a', 'b'):
        hk = res['hackermuller2004'][pan]
        prudentes[f'hackermuller2004_{pan}'] = (hk['chi2_HR_conservateur'], hk['ddl'])
    chi2_pru = sum(c for c, _ in prudentes.values())
    sig_pru = sigma_equivalent(log_p_chi2(chi2_pru, ddl_tot := sum(d for _, d in prudentes.values())))
    chi2_tot = sum(c for c, _ in composantes.values())
    ddl_tot = sum(d for _, d in composantes.values())
    sig_tot = sigma_equivalent(log_p_chi2(chi2_tot, ddl_tot))
    sig_min = min(sigma_equivalent(log_p_chi2(c, d)) for c, d in composantes.values())
    res['verdict'] = {
        'statut': 'Diagnostics exploratoires conditionnels aux erreurs et indépendances supposées. Aucune significativité combinée validée contre erreurs systématiques ou covariances.',
        'regle': 'HR rejetée si l\'écart combiné dépasse 5 σ sur les jeux à information jamais lue ; '
                 'durcie après lecture : version prudente et chaque jeu seul au-delà de 5 σ',
        'composantes': {k: {'chi2': round(c, 1), 'ddl': d, 'sigma': round(sigma_equivalent(log_p_chi2(c, d)), 1)}
                        for k, (c, d) in composantes.items()},
        'chi2_total_HR': round(chi2_tot, 0), 'ddl_total': ddl_tot,
        'sigma_rejet_HR_combine': round(sig_tot, 1),
        'sigma_rejet_HR_plus_faible_jeu': round(sig_min, 1),
        'chi2_total_HR_prudent': round(chi2_pru, 0), 'sigma_rejet_HR_prudent': round(sig_pru, 1),
        'HR_rejetee': bool(sig_pru > 5 and sig_min > 5),
        'inegalite_englert_respectee': bool(sw['inegalite_respectee']
                                            and res['ma2013']['complementarite_fig3']['z_au_dessus_de_1'] < 2),
        'trace_de_rendu_a_la_demande': None,
        'portee': 'Désaccord formel avec HR, pas test de toutes les architectures de simulation.',
    }
    txt = json.dumps(res, ensure_ascii=False, indent=1)
    args.out.write_text(txt + '\n', encoding='utf-8')
    print(json.dumps(res['verdict'], ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
