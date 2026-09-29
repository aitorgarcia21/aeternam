#!/usr/bin/env python3
"""Synthèse aeternam : de quoi dépend la probabilité d'être simulés ?

Ce script montre, chiffres à l'appui, combien les réponses publiées dépendent
d'hypothèses que les données ne fixent pas. Il ne mesure pas la probabilité que notre Univers soit simulé.
Chaque scénario est une illustration dépendante de choix a priori non mesurés.

1. Bostrom (2003), formule (*) : f_sim = f_P f_I N_I / (f_P f_I N_I + 1). Extension
   (la nôtre, signalée comme telle) : r = observateurs à expérience humaine par
   simulation, rapportés à la population réelle moyenne avant le stade posthumain
   (Bostrom : r = 1) ; c = probabilité que les observateurs simulés soient conscients.
   Avec x = f_P f_I N_I r, la confiance d'être simulé vaut c x / (1 + x).
2. Lois a priori log-uniformes explicites : distribution de log10 x calculée
   par convolution sur une grille discrétisée, puis contrôlée par Monte-Carlo (graine fixe).
3. Kipping (2020), cadre bayésien, reproduit à partir de ses équations (1), (2),
   (3), (7), (8), (12), (22), (27) et (32) (arXiv:2008.12254v1, Universe 6, 109),
   puis généralisé à un a priori quelconque sur son hypothèse H_S.
4. Effet d'un résultat nul de test de grille : facteur de Bayes 1 - w, où w est le
   poids a priori, parmi les simulations envisagées, des architectures exclues.
5. Ordres de grandeur de faisabilité tirés de Lloyd (2000, 2002) et Bostrom (2003).
   Le produit des facteurs de la note 10 de Bostrom vaut 1,5e34 à 1,5e37 opérations,
   quinze fois la valeur imprimée (1e33 à 1e36) ; nous retenons le produit recalculé.
6. Résultats des tests n° 1 à 3, recopiés de leurs resultats.json (empreinte SHA-256).

Usage : python3 analyse.py --out resultats.json      (numpy ; quelques secondes)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
RECHERCHE = ICI.parent
GRAINE = 20260928
PAS = 0.005            # pas de la grille en log10 (décades) pour les convolutions discrétisées
N_MC = 1_000_000       # tirages Monte-Carlo par scénario (contrôle)

# --------------------------------------------------------------------------------------
# Valeurs citées (source primaire, relue le 28/09/2026 ; voir sources.md)
# --------------------------------------------------------------------------------------
CITE = {
    'bostrom_H_humains': 1e11,            # Bostrom 2003, note 10 : « 100 billion humans »
    'bostrom_annees_par_humain': 50,      # id. : « 50 years/human »
    'bostrom_secondes_par_an': 3e7,       # id. : « 30 million secs/year »
    'bostrom_ops_cerveau_min': 1e14,      # id. : « [10^14, 10^17] operations in each human brain per second »
    'bostrom_ops_cerveau_max': 1e17,
    'bostrom_ops_histoire_min_imprime': 1e33,  # id. : « ≈ [10^33, 10^36] operations » (valeur imprimée)
    'bostrom_ops_histoire_max_imprime': 1e36,
    'bostrom_facteur_me_simulations': 1e11,  # p. 13 : « about 100 billion times as many me-simulations »
    'lloyd_laptop_ops_par_s': 5.4258e50,  # Lloyd 2000 : 1 kg, 1 litre
    'lloyd_laptop_bits': 2.13e31,         # id. : « I = S/kB ln 2 = 2.13×10^31 bits »
    'lloyd_univers_ops': 1e120,           # Lloyd 2002 : « no more than 10^120 ops on 10^90 bits »
    'lloyd_univers_bits_matiere': 1e90,
    'lloyd_univers_bits_gravitation': 1e120,  # « ≈10^120 if gravitation is taken into account »
}

# Lois a priori illustratives : bornes de log10 pour f_P, f_I, N_I, r ; c fixé.
# Ce ne sont pas des estimations : elles montrent comment la réponse suit le choix.
SCENARIOS = [
    {'cle': 'genereux', 'libelle': 'fractions proches de 1, N_I grand',
     'log10': {'f_P': (-1, 0), 'f_I': (-1, 0), 'N_I': (3, 9), 'r': (0, 0)}, 'c': 1.0},
    {'cle': 'ignorance', 'libelle': 'f_P et f_I ignorés sur 10 ordres de grandeur chacun',
     'log10': {'f_P': (-10, 0), 'f_I': (-10, 0), 'N_I': (0, 9), 'r': (0, 0)}, 'c': 1.0},
    {'cle': 'ignorance_N_astronomique', 'libelle': 'idem, mais N_I jusqu’à 10^30',
     'log10': {'f_P': (-10, 0), 'f_I': (-10, 0), 'N_I': (0, 30), 'r': (0, 0)}, 'c': 1.0},
    {'cle': 'ignorance_observateurs', 'libelle': 'ignorance, et r de 10^-11 (une seule personne simulée) à 1',
     'log10': {'f_P': (-10, 0), 'f_I': (-10, 0), 'N_I': (0, 9), 'r': (-11, 0)}, 'c': 1.0},
    {'cle': 'genereux_conscience', 'libelle': 'généreux, mais une chance sur deux que les simulés soient conscients',
     'log10': {'f_P': (-1, 0), 'f_I': (-1, 0), 'N_I': (3, 9), 'r': (0, 0)}, 'c': 0.5},
    # Notre choix central, celui de l'accueil : l'ignorance ci-dessus (N_I jusqu'aux « milliards »
    # de Musk, 2016) et c = 1/2, faute de pouvoir départager Chalmers et Searle (section 3).
    {'cle': 'aeternam', 'libelle': 'exemple arbitraire : fractions sur 10 décades, N_I de 1 à 10^9, c = 1/2',
     'log10': {'f_P': (-10, 0), 'f_I': (-10, 0), 'N_I': (0, 9), 'r': (0, 0)}, 'c': 0.5},
]


# --------------------------------------------------------------------------------------
# 1. Bostrom
# --------------------------------------------------------------------------------------
def f_sim(f_P, f_I, N_I, r=1.0):
    """Bostrom (2003), formule (*), étendue par r (r = 1 redonne la formule d'origine)."""
    x = f_P * f_I * N_I * r
    return x / (1.0 + x)


def logistique_log10(y):
    """x/(1+x) avec x = 10**y, stable pour |y| grand."""
    y = np.asarray(y, dtype=float)
    return 0.5 * (1.0 + np.tanh(0.5 * math.log(10.0) * y))


def x_pour_fraction(f):
    """Valeur de x = f_P f_I N_I r qui donne f_sim = f."""
    return f / (1.0 - f)


def bostrom_note10():
    """Produit des facteurs de la note 10 de Bostrom (2003), comparé à la valeur imprimée."""
    base = CITE['bostrom_H_humains'] * CITE['bostrom_annees_par_humain'] * CITE['bostrom_secondes_par_an']
    produit_min = base * CITE['bostrom_ops_cerveau_min']
    produit_max = base * CITE['bostrom_ops_cerveau_max']
    return {
        'produit_min': produit_min, 'produit_max': produit_max,
        'imprime_min': CITE['bostrom_ops_histoire_min_imprime'],
        'imprime_max': CITE['bostrom_ops_histoire_max_imprime'],
        'facteur_ecart': produit_min / CITE['bostrom_ops_histoire_min_imprime'],
    }


# --------------------------------------------------------------------------------------
# 2. Lois a priori : convolution exacte (sur grille) et Monte-Carlo
# --------------------------------------------------------------------------------------
def loi_log10_x(bornes: dict, pas: float = PAS):
    """Loi de log10 x = somme de variables uniformes indépendantes (masses sur une grille).

    Chaque U[a, b] est représentée par n = (b - a)/pas masses égales aux milieux des
    cellules ; une borne dégénérée (a = b) est un simple décalage. Renvoie (y, masses).
    """
    origine, masses = 0.0, np.array([1.0])
    for a, b in bornes.values():
        if b == a:
            origine += a
            continue
        n = int(round((b - a) / pas))
        if abs(n * pas - (b - a)) > 1e-9:
            raise ValueError('bornes non multiples du pas')
        origine += a + pas / 2
        masses = np.convolve(masses, np.full(n, 1.0 / n))
    y = origine + pas * np.arange(masses.size)
    return y, masses


def resume_loi(y, m, c):
    """Probabilité que f_sim dépasse 1/2, espérance de f_sim, confiance c E[f_sim]."""
    f = logistique_log10(y)
    au_dessus = m[y > 1e-12].sum() + 0.5 * m[np.abs(y) <= 1e-12].sum()
    transition = m[(f > 0.01) & (f < 0.99)].sum()
    esperance = float((m * f).sum())
    return {
        'P_f_sim_sup_un_demi': float(au_dessus),
        'esperance_f_sim': esperance,
        'confiance_c_fois_esperance': c * esperance,
        'part_entre_1_et_99_pct': float(transition),
    }


def monte_carlo(bornes: dict, c: float, rng, n: int = N_MC):
    y = np.zeros(n)
    for a, b in bornes.values():
        y += rng.uniform(a, b, n) if b > a else a
    f = logistique_log10(y)
    return {
        'P_f_sim_sup_un_demi': float(np.mean(y > 0)),
        'esperance_f_sim': float(np.mean(f)),
        'confiance_c_fois_esperance': float(c * np.mean(f)),
        'part_entre_1_et_99_pct': float(np.mean((f > 0.01) & (f < 0.99))),
        'n_tirages': n,
    }


def p_triangle_plus_uniforme(a, b):
    """P(T + N > 0), T somme de deux U[-a, 0], N ~ U[0, b] : forme fermée (autotest)."""
    def primitive(t):  # G(t) = intégrale de 0 à t de la fonction de répartition de -T
        if t <= a:
            return t ** 3 / (6 * a * a)
        if t <= 2 * a:
            return a / 6 + (t - a) - (a ** 3 - (2 * a - t) ** 3) / (6 * a * a)
        return t - a
    return primitive(b) / b


def courbe_ignorance(largeurs, borne_N=(0, 9)):
    """Espérance de f_sim quand f_P et f_I sont log-uniformes sur [10^-D, 1] chacun."""
    points = []
    for D in largeurs:
        bornes = {'f_P': (-D, 0), 'f_I': (-D, 0), 'N_I': borne_N}
        y, m = loi_log10_x(bornes)
        r = resume_loi(y, m, 1.0)
        points.append({'decades_par_fraction': D, 'esperance_f_sim': r['esperance_f_sim'],
                       'P_f_sim_sup_un_demi': r['P_f_sim_sup_un_demi']})
    return points


def largeur_critique(borne_N=(0, 9), cible=0.5):
    """Largeur D (décades par fraction) où l'espérance de f_sim vaut la cible (bissection)."""
    def esperance(D):
        y, m = loi_log10_x({'f_P': (-D, 0), 'f_I': (-D, 0), 'N_I': borne_N}, pas=0.01)
        return resume_loi(y, m, 1.0)['esperance_f_sim']
    bas, haut = 0.5, 40.0
    for _ in range(40):
        milieu = round((bas + haut) / 2, 2)
        if milieu in (bas, haut):
            break
        if esperance(milieu) > cible:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


# --------------------------------------------------------------------------------------
# 3. Kipping (2020)
# --------------------------------------------------------------------------------------
def kipping_n_g(p, lam, g):
    """Nombre de simulations à la génération g >= 2 : p^(g-2) λ^(g-1)."""
    return p ** (g - 2) * lam ** (g - 1)


def kipping_n_sim_somme(p, lam, G):
    return sum(kipping_n_g(p, lam, g) for g in range(2, G + 1))


def kipping_n_sim_ferme(p, lam, G):
    """Équation (1) : N_sim = (pλ - (pλ)^G) / (p - p²λ)."""
    return (p * lam - (p * lam) ** G) / (p - p * p * lam)


def kipping_parous(p, lam, G):
    """Réalités parentes sous H_S : la base, plus une fraction p des générations 2..G-1."""
    return 1 + p * sum(kipping_n_g(p, lam, g) for g in range(2, G))


def kipping_p_null_HS_compte(p, lam, G):
    N = kipping_n_sim_somme(p, lam, G)
    return (N + 1 - kipping_parous(p, lam, G)) / (N + 1)


def kipping_p_null_HS_eq7(p, lam, G):
    """Équation (7)."""
    return (lam - 1) / lam + p * (p * lam - 1) / (lam * ((p * lam) ** G - p * (1 + (1 - p) * lam)))


def kipping_p_gG_eq3(p, lam, G):
    """Équation (3), seconde forme (le « + 1 » du dénominateur y est négligé)."""
    return (1 - 1 / (p * lam)) / (1 - (p * lam) ** (1 - G))


def p_base_CES(N, pi_S=0.5):
    """Moyenne bayésienne de modèles avec la seule donnée « cogito » : Kipping (22) si pi_S = 1/2."""
    return pi_S / (N + 1) + (1 - pi_S)


def p_base_nullipare(lam, pi_S=0.5):
    """Donnée « nous n'avons pas créé de simulation », G grand : Kipping (27) si pi_S = 1/2."""
    vraisemblance_S = (lam - 1) / lam          # équation (8)
    return (1 - pi_S) / ((1 - pi_S) + pi_S * vraisemblance_S)


def p_base_parous(N, lam):
    """Équation (32) : si nous produisions des simulations, P(base) = λ / N_sim."""
    return lam / N


# --------------------------------------------------------------------------------------
# 4. Tests de grille : facteur de Bayes 1 - w
# --------------------------------------------------------------------------------------
def posterieur_apres_test(p0, w):
    """P(S | aucun signal) si une part w des simulations envisagées aurait donné un signal.

    Hypothèse : hors de cette part, les données ont la même probabilité avec ou sans
    simulation (équivalence observationnelle) ; dans cette part, un résultat nul est exclu.
    """
    return p0 * (1 - w) / (1 - w * p0)


def w_necessaire(p0, p1):
    """Poids w qu'il faudrait exclure pour faire passer la confiance de p0 à p1."""
    return (p0 - p1) / (p0 * (1 - p1))


# --------------------------------------------------------------------------------------
# 6. Tests n° 1 à 3
# --------------------------------------------------------------------------------------
def lire(chemin: Path):
    donnees = chemin.read_bytes()
    return json.loads(donnees), hashlib.sha256(donnees).hexdigest()


def resultats_des_tests():
    t1, h1 = lire(RECHERCHE / '2026-09-28-grille-lhaaso' / 'resultats.json')
    t2, h2 = lire(RECHERCHE / '2026-09-28-rayons-cosmiques' / 'resultats.json')
    t3, h3 = lire(RECHERCHE / '2026-09-28-dispersion-directionnelle' / 'resultats.json')
    sigma1 = [t for t in t1['temps_discret_methode_prudente'] if t['sigma_courant'] == 1.0][0]
    return {
        'test1': {
            'source': 'recherche/2026-09-28-grille-lhaaso/resultats.json', 'sha256': h1,
            'maille_max_pire_orientation_temps_continu_m': t1['bornes_temps_continu']['CCF']['a_max_pire_orientation_m'],
            'echelle_min_GeV': t1['bornes_temps_continu']['CCF']['echelle_min_GeV'],
            'borne_pire_orientation_pas_maximal': sigma1['a_max_pire_orientation_m'],
            'beane_b_max_m': t1['comparaison_beane_2012']['b_max_m'],
            'facteur_planck_sous_la_limite': t1['maille_de_Planck']['facteur_sous_la_limite_prudente'],
        },
        'test2': {
            'source': 'recherche/2026-09-28-rayons-cosmiques/resultats.json', 'sha256': h2,
            'n_evenements': t2['donnees']['n_evenements'],
            'p_valeur_l4': t2['resultats']['p_valeur_l4'],
            'exces_axes_non_exclu_95': t2['limite_superieure_95']['epsilon_axes_max'],
            'exces_diagonales_non_exclu_95': t2['limite_superieure_95']['epsilon_diagonales_max'],
        },
        'test3': {
            'source': 'recherche/2026-09-28-dispersion-directionnelle/resultats.json', 'sha256': h3,
            'n_sources': t3['n_sources'],
            'maille_exclue_toutes_orientations_m': t3['resume']['maille_exclue_toutes_orientations_m'],
            'echelle_min_GeV': t3['resume']['echelle_min_toutes_orientations_GeV'],
            'rapport_sur_longueur_planck': t3['resume']['rapport_sur_longueur_Planck'],
            'angle_mort_ferme': t3['resume']['angle_mort_ferme'],
        },
    }


# --------------------------------------------------------------------------------------
# Autotests
# --------------------------------------------------------------------------------------
def autotests(rng) -> dict:
    t = {}
    # Bostrom : formule (*) et ses limites
    t['bostrom_moitie_pour_x_egal_1'] = abs(f_sim(0.5, 0.5, 4.0) - 0.5) < 1e-15
    t['bostrom_r1_redonne_formule'] = abs(f_sim(0.1, 0.01, 1e6) - 1e3 / (1 + 1e3)) < 1e-15
    t['logistique_egale_x_sur_1_plus_x'] = all(
        abs(float(logistique_log10(y)) - 10 ** y / (1 + 10 ** y)) < 1e-12 for y in (-3, -0.7, 0, 0.3, 2.5))
    t['logistique_stable_aux_extremes'] = (float(logistique_log10(-400)) == 0.0
                                           and float(logistique_log10(400)) == 1.0)
    n10 = bostrom_note10()
    t['bostrom_note10_produit_recalcule'] = (abs(n10['produit_min'] / 1.5e34 - 1) < 1e-12
                                             and abs(n10['produit_max'] / 1.5e37 - 1) < 1e-12)
    t['bostrom_note10_ecart_facteur_15'] = abs(n10['facteur_ecart'] - 15) < 1e-9
    # Convolution exacte contre forme fermée et Monte-Carlo
    for a, b in ((10, 9), (1, 9), (5, 3), (2, 30)):
        y, m = loi_log10_x({'f_P': (-a, 0), 'f_I': (-a, 0), 'N_I': (0, b)})
        p_conv = resume_loi(y, m, 1)['P_f_sim_sup_un_demi']
        t[f'convolution_forme_fermee_a{a}_b{b}'] = abs(p_conv - p_triangle_plus_uniforme(a, b)) < 2e-3
    y, m = loi_log10_x({'u': (-2, 0)})
    t['convolution_masse_unite'] = abs(m.sum() - 1) < 1e-12 and abs(np.sum(m * y) + 1) < 1e-9
    for s in SCENARIOS:
        y, m = loi_log10_x(s['log10'])
        exact = resume_loi(y, m, s['c'])
        mc = monte_carlo(s['log10'], s['c'], rng, 200_000)
        tol = 5 * math.sqrt(0.25 / 200_000) + 3e-3
        t['monte_carlo_' + s['cle']] = (abs(exact['P_f_sim_sup_un_demi'] - mc['P_f_sim_sup_un_demi']) < tol
                                        and abs(exact['esperance_f_sim'] - mc['esperance_f_sim']) < tol)
    # Kipping : équations (1), (3), (7), (8), (22), (27), (32)
    cas = [(0.5, 10, 6), (0.2, 100, 8), (0.9, 1000, 12), (0.3, 7, 4)]
    t['kipping_eq1_forme_fermee'] = all(
        abs(kipping_n_sim_ferme(*c) / kipping_n_sim_somme(*c) - 1) < 1e-12 for c in cas)
    t['kipping_eq7_contre_comptage'] = all(
        abs(kipping_p_null_HS_eq7(*c) - kipping_p_null_HS_compte(*c)) < 1e-12 for c in cas)
    t['kipping_eq8_limite'] = abs(kipping_p_null_HS_eq7(0.5, 10, 60) - 0.9) < 1e-12
    t['kipping_parentes_egal_N_sur_lambda'] = all(
        abs(kipping_parous(*c) / (kipping_n_sim_somme(*c) / c[1]) - 1) < 1e-12 for c in cas)
    t['kipping_eq3_neglige_plus_un'] = all(
        abs(kipping_p_gG_eq3(p, l, G) - kipping_n_g(p, l, G) / kipping_n_sim_somme(p, l, G)) < 1e-12
        for p, l, G in cas)
    t['kipping_eq22'] = all(abs(p_base_CES(N) - (0.5 + 1 / (2 * (N + 1)))) < 1e-15 for N in (0, 3, 1e3, 1e12))
    t['kipping_eq27'] = all(abs(p_base_nullipare(l) - 1 / (2 - 1 / l)) < 1e-15 for l in (1, 2, 10, 1e6))
    t['kipping_moyenne_de_modeles_directe'] = all(
        abs((1 - p_base_CES(N, pi)) - pi * N / (N + 1)) < 1e-15 for N in (1, 1e4) for pi in (0.5, 0.2))
    # Test de grille : cas limites
    t['test_w0_ne_change_rien'] = abs(posterieur_apres_test(0.5, 0.0) - 0.5) < 1e-15
    t['test_w1_exclut_tout'] = posterieur_apres_test(0.5, 1.0) == 0.0
    t['test_w_necessaire_inverse'] = abs(posterieur_apres_test(0.5, w_necessaire(0.5, 0.1)) - 0.1) < 1e-12
    return {k: bool(v) for k, v in t.items()}


# --------------------------------------------------------------------------------------
# Calcul principal
# --------------------------------------------------------------------------------------
def calculer() -> dict:
    rng = np.random.default_rng(GRAINE)
    tests_internes = autotests(rng)
    if not all(tests_internes.values()):
        echecs = [k for k, v in tests_internes.items() if not v]
        raise SystemExit(f'autotests en échec : {echecs}')

    # 1. Bostrom : la fraction ne dépend que du produit x
    transition = [{'log10_x': k, 'f_sim': float(logistique_log10(k))} for k in (-3, -2, -1, 0, 1, 2, 3)]
    x01, x99 = x_pour_fraction(0.01), x_pour_fraction(0.99)
    r_me = 1 / CITE['bostrom_facteur_me_simulations']

    # 2. Scénarios a priori
    scenarios = {}
    rng_mc = np.random.default_rng(GRAINE + 1)
    for s in SCENARIOS:
        y, m = loi_log10_x(s['log10'])
        scenarios[s['cle']] = {
            'libelle': s['libelle'], 'bornes_log10': {k: list(v) for k, v in s['log10'].items()}, 'c': s['c'],
            'exact': resume_loi(y, m, s['c']),
            'monte_carlo': monte_carlo(s['log10'], s['c'], rng_mc),
        }
    courbe = courbe_ignorance([0, 1, 2, 3, 4, 5, 7, 10, 15, 20, 30])
    D_star = largeur_critique()

    # 3. Kipping
    exemples = []
    for p, lam, G in [(0.5, 10, 6), (0.2, 100, 8), (0.9, 1000, 12)]:
        N = kipping_n_sim_somme(p, lam, G)
        exemples.append({
            'p': p, 'lambda': lam, 'G': G, 'N_sim': N,
            'P_simule_si_HS_vraie_eq2': N / (N + 1),
            'P_base_CES_eq22': p_base_CES(N), 'P_simule_CES': 1 - p_base_CES(N),
            'P_base_nullipare_eq27': p_base_nullipare(lam), 'P_simule_nullipare': 1 - p_base_nullipare(lam),
            'P_base_si_nous_simulions_eq32': p_base_parous(N, lam),
            'P_derniere_generation_eq3_exacte': kipping_n_g(p, lam, G) / (N + 1),
            'P_derniere_generation_eq3_publiee': kipping_p_gG_eq3(p, lam, G),
        })
    N_ref = 1e9
    prior = [{'pi_S': pi, 'P_simule_CES': 1 - p_base_CES(N_ref, pi),
              'P_simule_nullipare_lambda_10': 1 - p_base_nullipare(10, pi)}
             for pi in (0.5, 1 / 3, 0.1, 0.01)]
    partition = {
        'deux_hypotheses_egales_kipping': 1 - p_base_CES(N_ref, 0.5),
        'trois_propositions_egales_bostrom': (1 / 3) * float(logistique_log10(math.log10(N_ref))),
        'N_sim_ou_x_de_reference': N_ref,
    }

    # 4. Tests de grille
    mise_a_jour = [{'P_avant': p0, 'w': w, 'P_apres': posterieur_apres_test(p0, w)}
                   for p0 in (0.5, 1 / 3) for w in (0.01, 0.1, 0.5, 0.9)]

    # 5. Faisabilité (avec le produit recalculé de la note 10, le plus défavorable à la simulation)
    n10 = bostrom_note10()
    fais = {
        'bostrom_note10': n10,
        'decades_univers_sur_histoire_min': math.log10(CITE['lloyd_univers_ops'] / n10['produit_max']),
        'decades_univers_sur_histoire_max': math.log10(CITE['lloyd_univers_ops'] / n10['produit_min']),
        'duree_histoire_humaine_laptop_ultime_s_min': n10['produit_min'] / CITE['lloyd_laptop_ops_par_s'],
        'duree_histoire_humaine_laptop_ultime_s_max': n10['produit_max'] / CITE['lloyd_laptop_ops_par_s'],
    }

    return {
        'titre': 'Synthèse : de quoi dépend la probabilité d’être simulés ?',
        'date': '2026-09-28',
        'niveau': 'Scénarios a priori arbitraires ; aucune estimation empirique de la probabilité cosmique.',
        'probabilite_empirique_univers_simule': None,
        'note_conscience': 'c pondère ici deux modèles : tous les simulés conscients ou aucun. Une fraction c d’individus conscients donnerait c*x/(1+c*x), un autre modèle.',
        'graine': GRAINE,
        'valeurs_citees': CITE,
        'bostrom': {
            'formule': 'f_sim = f_P f_I N_I / (f_P f_I N_I + 1) (Bostrom 2003, formule (*))',
            'extension': 'x = f_P f_I N_I r ; confiance = c x / (1 + x) (extension aeternam)',
            'transition': transition,
            'x_pour_f_sim_1_pct': x01, 'x_pour_f_sim_99_pct': x99,
            'largeur_transition_decades': math.log10(x99 / x01),
            'r_me_simulation': r_me,
        },
        'scenarios': scenarios,
        'courbe_ignorance_N_I_1_a_1e9': courbe,
        'largeur_critique_decades_par_fraction': D_star,
        'kipping': {
            'source': 'arXiv:2008.12254v1 (= Universe 6, 109, 2020), équations (1)-(32)',
            'exemples': exemples,
            'prior_general_N_sim_1e9': prior,
            'remarque_eq3': 'la seconde forme de l’équation (3) vaut n_G/N_sim : écart relatif 1/(N_sim + 1)',
        },
        'partition': partition,
        'tests_de_grille': {
            'modele': 'Cas idéal illustratif : facteur de Bayes 1-w si détection certaine dans une part w. Ce n’est pas une conversion de p-values ou de bornes à 95 % en probabilité de simulation.',
            'mise_a_jour': mise_a_jour,
            'w_pour_passer_de_un_demi_a_un_dixieme': w_necessaire(0.5, 0.1),
            'w_pour_passer_de_un_demi_a_un_centieme': w_necessaire(0.5, 0.01),
        },
        'faisabilite': fais,
        'tests': resultats_des_tests(),
        'autotests': tests_internes,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--out', default='resultats.json', help='fichier de sortie')
    args = parser.parse_args()
    resultats = calculer()
    Path(args.out).write_text(json.dumps(resultats, ensure_ascii=False, indent=1) + '\n')
    n = len(resultats['autotests'])
    print(f'{n} autotests réussis ; résultats écrits dans {args.out}')


if __name__ == '__main__':
    main()
