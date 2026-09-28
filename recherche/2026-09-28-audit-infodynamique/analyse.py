#!/usr/bin/env python3
"""Audit infodynamique : les démonstrations publiées du « oui » tiennent-elles ?

Vérifications exactes (bibliothèque standard seulement) de quatre étapes
mathématiques des articles de Melvin Vopson et d'une confusion fréquente sur la
compression. Aucune observation nouvelle, aucune probabilité cosmique.

1. Vopson (Entropy 28, 564, 2026), section 2, équations (5) à (14) : la
   répartition égale g_i = N/n est présentée comme le MINIMUM de
   I = log2 N - (1/N) sum g_i log2 g_i. Contre-exemple N = 6, n = 2 ; énumération
   exhaustive (N de 2 à 15, n de 2 à min(5, N)) ; concavité vérifiée
   numériquement le long de directions admissibles (somme des g_i fixée) et
   comparée à la hessienne analytique -delta_ij / (N ln 2 g_i).
2. Section 3 du même article (polygones) : la conclusion « polygone régulier =
   entropie minimale » est recalculée par la règle de chaîne
   I = 1 + (H_côtés + H_angles)/2 >= 1 bit, indépendante de l'équation (14).
3. Vopson (AIP Advances 13, 105308, 2023), telle que résumée par l'auteur dans
   sa réponse (IPI Letters 3(1), N6-N9, 2025) : Q = 0 => dS = 0. Contre-exemple :
   détente libre d'une mole de gaz parfait vers un volume double,
   Q = W = dU = 0 et Delta S = R ln 2 (calcul en Decimal, constantes SI exactes).
   Réponse de 2025, équation (11) : signe de dS_info indéterminé.
4. Codage : un code sans perte (injectif) conserve l'entropie des messages ;
   l'entropie est ici recalculée sur la loi des mots de code réellement émis
   (le script d'un tiers recopiait l'entropie d'entrée). Un codage avec perte
   (non injectif) la réduit, en détruisant de l'information.

Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import json
import math
import random
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterator, Sequence

if not __debug__:
    raise SystemExit('Les autotests reposent sur assert : ne pas lancer avec python -O.')

ICI = Path(__file__).resolve().parent
GRAINE = 20260928
TOL = 1e-12

# --------------------------------------------------------------------------------------
# Valeurs citées (source primaire lue le 28/09/2026 ; détail dans sources.md)
# --------------------------------------------------------------------------------------
CITE = {
    # Vopson, « The Role of Information Entropy in Symmetry of Euclidean Polygons »,
    # Entropy 28(5), 564, publié le 18/05/2026, DOI 10.3390/e28050564, PMC13205927
    # (texte intégral JATS via NCBI E-utilities).
    'vopson2026_eq14': {'valeur': 'g_i = N/n', 'source': 'Entropy 28, 564 (2026), éq. (14)'},
    'vopson2026_triangle_quelconque_bits': {'valeur': 2.585, 'source': 'Entropy 28, 564 (2026), section 3'},
    'vopson2026_triangle_equilateral_bits': {'valeur': 1.0, 'source': 'id., section 3'},
    'vopson2026_quadrilatere_quelconque_bits': {'valeur': 3.0, 'source': 'id., section 3'},
    'vopson2026_carre_bits': {'valeur': 1.0, 'source': 'id., section 3'},
    'vopson2026_pentagone_quelconque_bits': {'valeur': 3.321, 'source': 'id., section 3'},
    'vopson2026_pentagone_regulier_bits': {'valeur': 1.0, 'source': 'id., section 3'},
    # Vopson, « On the Second Law of Infodynamics from Cosmological Thermodynamics »,
    # IPI Letters 3(1), N6-N9, publié le 10/01/2025, DOI 10.59973/ipil.137 (PDF de l'éditeur).
    'vopson2025_equations': {'valeur': '(2)-(13)', 'source': 'IPI Letters 3(1), N6-N9 (2025)'},
    # CODATA 2022 (NIST, physics.nist.gov/cuu) : valeurs exactes dans le SI depuis 2019.
    'k_B_J_par_K': {'valeur': '1.380649e-23', 'source': 'NIST CODATA 2022, « exact »'},
    'N_A_par_mol': {'valeur': '6.02214076e23', 'source': 'NIST CODATA 2022, « exact »'},
    'R_affiche_NIST': {'valeur': '8.314462618', 'source': 'NIST CODATA 2022, « 8.314 462 618... », exact'},
    # MIT 16 Unified, Thermodynamics and Propulsion, section 5.5 (node41).
    'mit_detente_libre': {'valeur': 'Delta S_system = N R ln(V2/V1) ; Delta S_surroundings = 0',
                          'source': 'web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html'},
}


# --------------------------------------------------------------------------------------
# 1. Entropie de multiplicités
# --------------------------------------------------------------------------------------
def entropie_bits(g: Sequence[float]) -> float:
    """I = log2 N - (1/N) sum g_i log2 g_i, avec N = sum g_i (éq. (5) de Vopson 2026)."""
    if not g or any(x <= 0 for x in g):
        raise ValueError('multiplicités strictement positives requises')
    n_tot = sum(g)
    return math.log2(n_tot) - sum(x * math.log2(x) for x in g) / n_tot


def entropie_shannon(p: Sequence[float]) -> float:
    """-sum p_i log2 p_i (éq. (1)/(2) de Vopson 2026)."""
    return -sum(x * math.log2(x) for x in p if x > 0)


def compositions(total: int, n: int) -> Iterator[tuple[int, ...]]:
    """Suites ordonnées de n entiers >= 1 de somme total."""
    if n < 1 or total < n:
        raise ValueError('1 <= n <= total requis')
    if n == 1:
        yield (total,)
        return
    for premier in range(1, total - n + 2):
        for reste in compositions(total - premier, n - 1):
            yield (premier, *reste)


def partition_equilibree(total: int, n: int) -> tuple[int, ...]:
    q, r = divmod(total, n)
    return tuple([q + 1] * r + [q] * (n - r))


def partition_extreme(total: int, n: int) -> tuple[int, ...]:
    return tuple([total - n + 1] + [1] * (n - 1))


def contre_exemple_N6() -> dict:
    lignes = []
    for k in (3, 4, 5):
        g = (k, 6 - k)
        lignes.append({'g': list(g), 'I_bits': round(entropie_bits(g), 9),
                       'I_shannon_bits': round(entropie_shannon([x / 6 for x in g]), 9)})
    return {
        'N': 6, 'n': 2, 'lignes': lignes,
        'egal_3_3_bits': lignes[0]['I_bits'],
        'g_4_2_bits': lignes[1]['I_bits'],
        'g_5_1_bits': lignes[2]['I_bits'],
        'conclusion': "à N et n fixés, la répartition égale (3,3) donne l'entropie la plus GRANDE",
    }


def enumeration() -> dict:
    cas, cas_non_triviaux, egal_est_max, egal_est_min = 0, 0, 0, 0
    detail = []
    for N in range(2, 16):
        for n in range(2, min(5, N) + 1):
            valeurs = {c: entropie_bits(c) for c in compositions(N, n)}
            vmax, vmin = max(valeurs.values()), min(valeurs.values())
            e = entropie_bits(partition_equilibree(N, n))
            x = entropie_bits(partition_extreme(N, n))
            assert math.isclose(vmax, e, abs_tol=TOL), (N, n, 'max')
            assert math.isclose(vmin, x, abs_tol=TOL), (N, n, 'min')
            cas += 1
            if vmax - vmin > TOL:
                cas_non_triviaux += 1
                egal_est_max += 1
                if math.isclose(e, vmin, abs_tol=TOL):
                    egal_est_min += 1
            detail.append({'N': N, 'n': n, 'nb_compositions': len(valeurs),
                           'I_min_bits': round(vmin, 9), 'I_max_bits': round(vmax, 9),
                           'argmin': list(partition_extreme(N, n)),
                           'argmax': list(partition_equilibree(N, n))})
    return {
        'domaine': 'N de 2 à 15, n de 2 à min(5, N) ; toutes les compositions ordonnées',
        'nb_cas': cas,
        'nb_cas_non_triviaux': cas_non_triviaux,
        'nb_cas_ou_repartition_la_plus_egale_est_le_maximum': egal_est_max,
        'nb_cas_ou_repartition_la_plus_egale_est_le_minimum': egal_est_min,
        'nb_compositions_examinees': sum(d['nb_compositions'] for d in detail),
        'detail': detail,
    }


def concavite(rng: random.Random, nb_points: int = 2000) -> dict:
    """Dérivée seconde de I le long de directions d (somme d_i = 0, N fixé)."""
    pire_ecart_relatif, max_derivee_seconde = 0.0, -math.inf
    h = 1e-4
    for _ in range(nb_points):
        n = rng.randint(2, 6)
        N = rng.uniform(n + 1.0, 40.0)
        w = [rng.random() + 0.05 for _ in range(n)]
        g = [N * x / sum(w) for x in w]
        d = [rng.gauss(0, 1) for _ in range(n)]
        m = sum(d) / n
        d = [x - m for x in d]
        norme = math.sqrt(sum(x * x for x in d))
        d = [x / norme for x in d]
        if min(g) - h * max(abs(x) for x in d) <= 0:
            continue
        plus = entropie_bits([a + h * b for a, b in zip(g, d)])
        moins = entropie_bits([a - h * b for a, b in zip(g, d)])
        num = (plus + moins - 2 * entropie_bits(g)) / h ** 2
        ana = -sum(b * b / (N * math.log(2) * a) for a, b in zip(g, d))
        assert abs(sum(a + h * b for a, b in zip(g, d)) - N) < 1e-9
        pire_ecart_relatif = max(pire_ecart_relatif, abs(num - ana) / abs(ana))
        max_derivee_seconde = max(max_derivee_seconde, num)
    # Point stationnaire de Lagrange : gradient de I en g_i = N/n parallèle à (1,...,1).
    N, n = 12.0, 3
    g = [N / n] * n
    grad = [-(math.log2(x) + 1 / math.log(2)) / N for x in g]
    return {
        'nb_points': nb_points,
        'pas_differences_finies': h,
        'derivee_seconde_max_observee': max_derivee_seconde,
        'toutes_negatives': max_derivee_seconde < 0,
        'ecart_relatif_max_numerique_vs_hessienne': pire_ecart_relatif,
        'hessienne': '-delta_ij / (N ln 2 g_i), définie négative : I strictement concave sur {sum g_i = N}',
        'gradient_au_point_egal_N12_n3': grad,
        'gradient_projete_nul': max(grad) - min(grad) < TOL,
    }


# --------------------------------------------------------------------------------------
# 2. Polygones : règle de chaîne
# --------------------------------------------------------------------------------------
def entropie_polygone(cotes: Sequence[int], angles: Sequence[int]) -> float:
    """Multiplicités des longueurs et des angles (deux espèces distinctes, comme chez Vopson)."""
    return entropie_bits(list(cotes) + list(angles))


def chaine_polygone(cotes: Sequence[int], angles: Sequence[int]) -> float:
    m = sum(cotes)
    assert m == sum(angles)
    return 1 + 0.5 * entropie_bits(cotes) + 0.5 * entropie_bits(angles)


def polygones() -> dict:
    formes = {
        # nom : (multiplicités des longueurs, multiplicités des angles)
        'triangle_quelconque': ((1, 1, 1), (1, 1, 1)),
        'triangle_isocele': ((2, 1), (2, 1)),
        'triangle_equilateral': ((3,), (3,)),
        'quadrilatere_quelconque': ((1, 1, 1, 1), (1, 1, 1, 1)),
        'rectangle': ((2, 2), (4,)),
        'losange': ((4,), (2, 2)),
        'carre': ((4,), (4,)),
        'pentagone_quelconque': ((1,) * 5, (1,) * 5),
        'pentagone_regulier': ((5,), (5,)),
    }
    res = {}
    for nom, (c, a) in formes.items():
        direct = entropie_polygone(c, a)
        chaine = chaine_polygone(c, a)
        assert math.isclose(direct, chaine, abs_tol=TOL), nom
        res[nom] = {'cotes': list(c), 'angles': list(a), 'n': len(c) + len(a),
                    'N': 2 * sum(c), 'I_bits': round(direct, 9)}
    return {
        'formes': res,
        'regle_de_chaine': 'I = 1 + (H_côtés + H_angles)/2 >= 1 bit ; égalité ssi côtés tous égaux et angles tous égaux',
        'n2_impose_repartition_egale': "n = 2 exige une seule longueur et un seul angle : g = (m, m), seule composition réalisable",
    }


# --------------------------------------------------------------------------------------
# 3. Thermodynamique : détente libre
# --------------------------------------------------------------------------------------
def detente_libre() -> dict:
    with localcontext() as ctx:
        ctx.prec = 50
        k_b = Decimal(CITE['k_B_J_par_K']['valeur'])
        n_a = Decimal(CITE['N_A_par_mol']['valeur'])
        R = k_b * n_a
        dS = R * Decimal(2).ln()
    return {
        'modele': "1 mol de gaz parfait, enceinte isolée et rigide, V -> 2V dans le vide",
        'Q_J': 0, 'W_J': 0, 'Delta_U_J': 0,
        'integrale_dQ_sur_T_J_par_K': 0,
        'R_J_par_mol_K': str(R),
        'Delta_S_J_par_K': str(dS),
        'Delta_S_J_par_K_arrondi': f'{dS:.9f}',
        'conclusion': 'Q = 0 et pourtant Delta S > 0 : dS = dQ/T ne vaut que pour une transformation réversible',
    }


def signe_reponse_2025() -> dict:
    """Éq. (11) de Vopson 2025 : dS_info = -dS_phys + dU_loss/T, avec dS_phys >= 0 et dU_loss >= 0."""
    cas = []
    for dS_phys, perte_sur_T in ((Fraction(1), Fraction(0)), (Fraction(1), Fraction(1, 2)),
                                 (Fraction(1), Fraction(1)), (Fraction(1), Fraction(2))):
        ds_info = -dS_phys + perte_sur_T
        cas.append({'dS_phys': str(dS_phys), 'dU_loss_sur_T': str(perte_sur_T),
                    'dS_info': str(ds_info),
                    'signe': 'négatif' if ds_info < 0 else ('nul' if ds_info == 0 else 'positif')})
    return {
        'equation': 'dS_info = -dS_phys + dU_loss/T (éq. 11), dS_phys >= 0, dU_loss >= 0',
        'cas': cas,
        'conclusion': "le signe de dS_info dépend de dU_loss/T face à dS_phys : l'équation seule ne l'impose pas",
    }


# --------------------------------------------------------------------------------------
# 4. Codage sans perte et avec perte
# --------------------------------------------------------------------------------------
def entropie_loi(loi: dict) -> Fraction | float:
    return -sum(float(p) * math.log2(float(p)) for p in loi.values() if p > 0)


def codage() -> dict:
    source = {'a': Fraction(1, 2), 'b': Fraction(1, 4), 'c': Fraction(1, 8), 'd': Fraction(1, 8)}
    code = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}
    fixe = {'a': '00', 'b': '01', 'c': '10', 'd': '11'}

    def loi_image(application: dict) -> dict:
        loi: dict = {}
        for s, p in source.items():
            loi[application[s]] = loi.get(application[s], Fraction(0)) + p
        return loi

    def prefixe_libre(c: dict) -> bool:
        mots = list(c.values())
        return all(not b.startswith(a) for a in mots for b in mots if a != b)

    def decoder(flux: str, c: dict) -> list:
        inverse, sortie, tampon = {v: k for k, v in c.items()}, [], ''
        for bit in flux:
            tampon += bit
            if tampon in inverse:
                sortie.append(inverse[tampon])
                tampon = ''
        assert tampon == ''
        return sortie

    H_source = entropie_loi(source)
    loi_mots = loi_image(code)                       # loi des mots de code réellement émis
    H_mots = entropie_loi(loi_mots)
    L = sum(p * len(code[s]) for s, p in source.items())
    L_fixe = sum(p * len(fixe[s]) for s, p in source.items())
    uns = sum(p * code[s].count('1') for s, p in source.items())
    p1 = uns / L                                     # fréquence des 1 dans le flux binaire codé
    uns_fixe = sum(p * fixe[s].count('1') for s, p in source.items())

    # Tous les messages de longueur 3 : l'encodage est injectif, les probabilités sont conservées.
    msgs = {}
    for m in product(source, repeat=3):
        p = source[m[0]] * source[m[1]] * source[m[2]]
        mot = ''.join(code[s] for s in m)
        assert decoder(mot, code) == list(m)
        msgs[mot] = msgs.get(mot, Fraction(0)) + p
    assert len(msgs) == 4 ** 3
    H_msg3_source = 3 * H_source
    H_msg3_code = entropie_loi(msgs)

    # Codage avec perte : c et d confondus (application non injective).
    perte = {'a': '0', 'b': '10', 'c': '11', 'd': '11'}
    loi_perte = loi_image(perte)
    H_perte = entropie_loi(loi_perte)
    return {
        'source': {k: str(v) for k, v in source.items()},
        'code_prefixe': code,
        'code_prefixe_libre': prefixe_libre(code),
        'H_source_bits': H_source,
        'loi_des_mots_de_code': {k: str(v) for k, v in loi_mots.items()},
        'H_mots_de_code_bits': H_mots,
        'longueur_moyenne_prefixe_bits': float(L),
        'longueur_moyenne_fixe_bits': float(L_fixe),
        'entropie_par_bit_code_prefixe': H_source / float(L),
        'entropie_par_bit_code_fixe': H_source / float(L_fixe),
        'frequence_des_1_code_prefixe': str(p1),
        'frequence_des_1_code_fixe': str(uns_fixe / L_fixe),
        'messages_de_3_symboles': {'nb': len(msgs), 'H_source_bits': H_msg3_source,
                                   'H_codes_bits': H_msg3_code},
        'avec_perte': {
            'application': perte,
            'loi_image': {k: str(v) for k, v in loi_perte.items()},
            'H_apres_bits': H_perte,
            'information_perdue_bits': H_source - H_perte,
        },
    }


# --------------------------------------------------------------------------------------
# Autotests (échouent bruyamment)
# --------------------------------------------------------------------------------------
def autotests() -> dict:
    ok = {}
    # entropie : cas connus
    assert entropie_bits([1, 1]) == 1.0
    assert entropie_bits([7]) == 0.0
    assert math.isclose(entropie_bits([1] * 8), 3.0, abs_tol=TOL)
    assert math.isclose(entropie_bits([2, 1, 1]), entropie_shannon([0.5, 0.25, 0.25]), abs_tol=TOL)
    ok['entropie'] = True
    # compositions : nombre = C(N-1, n-1)
    for N in range(2, 12):
        for n in range(1, N + 1):
            assert sum(1 for _ in compositions(N, n)) == math.comb(N - 1, n - 1)
    ok['compositions'] = True
    # contre-exemple
    assert entropie_bits([5, 1]) < entropie_bits([4, 2]) < entropie_bits([3, 3])
    assert f'{entropie_bits([4, 2]):.9f}' == '0.918295834'
    assert f'{entropie_bits([5, 1]):.9f}' == '0.650022422'
    ok['contre_exemple'] = True
    # valeurs publiées par Vopson (section 3) retrouvées
    assert f"{entropie_bits([1] * 6):.3f}" == f"{CITE['vopson2026_triangle_quelconque_bits']['valeur']:.3f}"
    # log2 10 = 3,32193 : Vopson imprime 3.321 (troncature, pas arrondi) ; écart < 0,001 bit
    assert abs(entropie_bits([1] * 10) - CITE['vopson2026_pentagone_quelconque_bits']['valeur']) < 1e-3
    assert entropie_bits([1] * 8) == CITE['vopson2026_quadrilatere_quelconque_bits']['valeur']
    assert entropie_bits([3, 3]) == CITE['vopson2026_carre_bits']['valeur']
    ok['valeurs_vopson_retrouvees'] = True
    # R = k_B N_A cohérent avec l'affichage NIST
    with localcontext() as ctx:
        ctx.prec = 50
        R = Decimal(CITE['k_B_J_par_K']['valeur']) * Decimal(CITE['N_A_par_mol']['valeur'])
    assert str(R).replace('.', '').startswith(CITE['R_affiche_NIST']['valeur'].replace('.', ''))
    ok['constante_R'] = True
    # le défaut du script tiers : recopier l'entropie d'entrée masquerait une perte
    c = codage()
    assert math.isclose(c['H_mots_de_code_bits'], c['H_source_bits'], abs_tol=TOL)
    assert c['avec_perte']['H_apres_bits'] < c['H_source_bits'] - 0.1
    ok['codage'] = True
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--out', default='resultats.json', help='fichier de sortie')
    args = parser.parse_args()

    tests = autotests()
    rng = random.Random(GRAINE)
    resultats = {
        'titre': 'Audit infodynamique : les démonstrations publiées du « oui » tiennent-elles ?',
        'date': '2026-09-28',
        'niveau': 'vérifications mathématiques exactes ; aucune observation nouvelle, aucune probabilité cosmique',
        'graine': GRAINE,
        'valeurs_citees': CITE,
        'autotests': tests,
        'multiplicites': {
            'contre_exemple_N6': contre_exemple_N6(),
            'enumeration': enumeration(),
            'concavite': concavite(rng),
        },
        'polygones': polygones(),
        'thermodynamique': {
            'detente_libre': detente_libre(),
            'reponse_2025_signe': signe_reponse_2025(),
        },
        'codage': codage(),
    }
    e = resultats['multiplicites']['enumeration']
    assert e['nb_cas_ou_repartition_la_plus_egale_est_le_minimum'] == 0
    assert e['nb_cas_ou_repartition_la_plus_egale_est_le_maximum'] == e['nb_cas_non_triviaux']
    assert resultats['multiplicites']['concavite']['toutes_negatives']
    assert resultats['multiplicites']['concavite']['ecart_relatif_max_numerique_vs_hessienne'] < 1e-3

    sortie = Path(args.out)
    if not sortie.is_absolute():
        sortie = Path.cwd() / sortie
    sortie.write_text(json.dumps(resultats, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f"autotests : {', '.join(tests)} — OK")
    print(f"N = 6, n = 2 : (3,3) {resultats['multiplicites']['contre_exemple_N6']['egal_3_3_bits']} bit ; "
          f"(4,2) {resultats['multiplicites']['contre_exemple_N6']['g_4_2_bits']} ; "
          f"(5,1) {resultats['multiplicites']['contre_exemple_N6']['g_5_1_bits']}")
    print(f"énumération : {e['nb_cas']} cas, {e['nb_cas_non_triviaux']} non triviaux, "
          f"répartition égale = maximum dans {e['nb_cas_ou_repartition_la_plus_egale_est_le_maximum']}, "
          f"= minimum dans {e['nb_cas_ou_repartition_la_plus_egale_est_le_minimum']}")
    print(f"détente libre : Delta S = {resultats['thermodynamique']['detente_libre']['Delta_S_J_par_K_arrondi']} J/K")
    print(f"écrit : {sortie}")


if __name__ == '__main__':
    main()
