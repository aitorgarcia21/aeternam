#!/usr/bin/env python3
"""Construit public/ : le site ÆTERNAM en deux langues, le français à la racine
(æternam.com/) et l'anglais sous /en/, avec les mêmes adresses de pages.

Les textes sont dans site/langues/fr.py (la source) et site/langues/en.py (la traduction,
dont la structure est vérifiée à chaque construction) ; les nombres viennent du
resultats.json de chaque étude (recherche/). Les anciennes adresses à préfixe de langue
(/fr/, /es/…) redirigent durablement vers la racine (public/_redirects).

Usage : python3 site/generer.py
"""
from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import math
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / 'langues'))
import visuels  # noqa: E402  (site/visuels.py)
import dessins  # noqa: E402  (site/dessins.py : les dessins au trait)
import accueil as page_accueil  # noqa: E402  (site/accueil.py : la page d'accueil)
import contributions  # noqa: E402  (site/contributions.py : les articles de la communauté)
import verifier_traduction  # noqa: E402  (site/langues/verifier_traduction.py)
SITE = RACINE / 'site'
PUBLIC = RACINE / 'public'
DOMAINE = 'https://xn--ternam-oua.com'  # æternam.com (adresse principale depuis le 17/11/2026), écrite en punycode pour le plan du site
# Préfixes des anciennes adresses (site multilingue jusqu'au 28 septembre 2026) : redirigés vers la racine.
# /en/ n'en fait plus partie : c'est l'édition anglaise depuis le 20 novembre 2026.
ANCIENS_PREFIXES = ('fr', 'es', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'ar')
KATEX = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/'
FLECHE = ('<svg class="fleche" viewBox="0 0 24 24" fill="none" aria-hidden="true" '
          'focusable="false"><path d="M5 19 19 5M5 5h14v14" '
          'stroke="currentColor" stroke-width="1.25" stroke-linecap="round" '
          'stroke-linejoin="round"/></svg>')

MARQUEUR = re.compile(r'\[\[([a-z0-9_]+)\]\]')
FORMULE = re.compile(r'\$\$.+?\$\$|\\\(.+?\\\)', re.S)
MOINS, FINE = '−', ' '


def charger(code: str):
    chemin = SITE / 'langues' / f'{code}.py'
    spec = importlib.util.spec_from_file_location(f'langue_{code}', chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def titre_html(texte: str) -> str:
    """La ponctuation française reste attachée au mot qui la précède."""
    return re.sub(r' (?=[:;!?])', '\u202f', html.escape(texte))


def ecrire_nombre(valeur: float, genre: str, precision: int, decimale: str, milliers: str = FINE) -> str:
    if genre == 'sci':
        e = math.floor(math.log10(abs(valeur)))
        m = round(valeur / 10 ** e, precision - 1)
        if abs(m) >= 10:
            m, e = m / 10, e + 1
        mantisse = f'{m:.{precision - 1}f}'.replace('.', decimale).replace('-', MOINS)
        puissance = f'10<sup>{str(e).replace("-", MOINS)}</sup>'
        corps = puissance if mantisse == '1' else f'{mantisse}{FINE}×{FINE}{puissance}'
    elif genre == 'fix':
        corps = f'{valeur:.{precision}f}'.replace('.', decimale).replace('-', MOINS)
    elif genre == 'ent':
        entier = round(valeur, precision) if precision < 0 else round(valeur)  # précision < 0 : arrondi à 10^-p
        corps = f'{int(entier):,}'.replace(',', milliers).replace('-', MOINS)
    else:
        raise ValueError(genre)
    return f'<bdi>{corps}</bdi>'


def racine_sur_puissance(c: float) -> float:
    """Le nombre dont c serait la « racine » prise sur la seule puissance de dix (7,5e-8 -> 7,5e-16)."""
    e = math.floor(math.log10(c))
    return c / 10 ** e * 10.0 ** (2 * e)


def table_des_nombres(r: dict) -> dict[str, tuple[float, str, int]]:
    b = r['bornes_temps_continu']
    ccf, mi, ca = b['CCF'], b['ML_MINOS'], b['ML_calibre']
    t = r['temps_discret_methode_prudente']
    p26, p27, p28, ppl = r['predictions_non_mesurees']
    x = r['audit_xi_shu']
    beane = r['comparaison_beane_2012']['b_max_m']
    n = {
        'a_resume': (ccf['a_max_pire_orientation_m'], 'sci', 2),
        'a_ml_resume': (mi['a_max_pire_orientation_m'], 'sci', 2),
        'echelle_resume': (ccf['echelle_min_GeV'], 'sci', 2),
        'b_beane': (beane, 'sci', 2),
        'a95_sigma1': (t[4]['a_max_95pct_orientations_m'], 'sci', 2),
        'a_lineaire': (r['artefact_lineaire']['a_max_m_coefficient_1'], 'sci', 2),
        'facteur_planck': (r['maille_de_Planck']['facteur_sous_la_limite_prudente'], 'sci', 1),
        'facteur_planck_exact': (r['maille_de_Planck']['facteur_sous_la_limite_prudente'], 'sci', 2),
        'z': (r['constantes']['z'], 'fix', 3),
        'epl': (r['constantes']['E_Pl_GeV'], 'sci', 3),
        'h0': (r['constantes']['H0_km_s_Mpc'], 'fix', 2),
        'om': (r['constantes']['Omega_m'], 'fix', 3),
        'ol': (1 - r['constantes']['Omega_m'], 'fix', 3),
        'i2': (r['integrales_s']['I2'], 'sci', 3),
        'retard_limite': (r['retard_a_la_limite_1TeV_0p3TeV_s'], 'fix', 2),
        'e_bas': (0.3, 'fix', 1),
        'lpl': (r['constantes']['l_Pl_m'], 'sci', 2),
        'q_mediane': (r['orientation']['Q_mediane'], 'fix', 3),
        'q_5': (r['orientation']['Q_5pct'], 'fix', 3),
        'ccf_mediane': (t[0]['a_max_orientation_mediane_m'], 'sci', 3),
        'comobile_facteur': (r['maille_comobile']['facteur_sur_la_borne'], 'fix', 3),
        'comobile_a': (r['maille_comobile']['a_max_pire_orientation_m'], 'sci', 2),
        'validite': (r['validite_developpement']['a_E_sur_hbar_c'], 'sci', 2),
        'ak_test': (r['validite_developpement']['ak_test'], 'fix', 2),
        'ecart_dispersion': (r['validite_developpement']['ecart_relatif_max_developpement'], 'sci', 1),
        'beane_ratio': (ccf['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'beane_ml_min': (ca['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'beane_ml_max': (mi['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'q_cal_axe': (ca['haut'] / p27['eta2_max'], 'fix', 2),
        'xs_facteur': (x['imprime_sur_coherent'], 'fix', 1),
        'xs_eqg_imprime': (x['EQG2_GeV_imprime_tableau_III'], 'sci', 2),
        'xs_rapport_lhaaso': (x['imprime_sur_LHAASO'], 'ent', 0),
        'xs_c1_imprime': (x['n1_constante_imprimee_eq6'], 'fix', 1),
        'xs_c1': (x['n1_constante_recalculee'], 'fix', 2),
        'xs_c2_imprime': (x['n2_constante_imprimee_eq7_sur_theta2'], 'sci', 2),
        'xs_theta': (x['theta2_limite_s_par_TeV2'], 'fix', 3),
        'xs_eq7': (x['EQG2_GeV_avec_eq7_imprimee'], 'sci', 3),
        'xs_c2': (x['n2_constante_coherente_sur_racine_theta2'], 'sci', 2),
        'xs_eqg': (x['EQG2_GeV_coherent_avec_eq3'], 'sci', 3),
        'xs_eps2': (x['n2_eps2_fois_theta2_recalcule'], 'sci', 3),
        'xs_eps2_imprime': (racine_sur_puissance(x['n2_constante_imprimee_eq7_sur_theta2']), 'sci', 2),
        'xs_vs_lhaaso': (x['coherent_sur_LHAASO'], 'fix', 1),
    }
    for nom, ligne in (('ccf', ccf), ('min', mi), ('cal', ca)):
        n[f'{nom}_bas'] = (ligne['bas'], 'fix', 2)
        n[f'{nom}_haut'] = (ligne['haut'], 'fix', 2)
        if ligne['meilleur'] is not None:
            n[f'{nom}_bf'] = (ligne['meilleur'], 'fix', 2)
        n[f'{nom}_arq'] = (ligne['a_racine_Q_max_m'], 'sci', 3)
        n[f'{nom}_pire'] = (ligne['a_max_pire_orientation_m'], 'sci', 3)
        n[f'{nom}_95'] = (ligne['a_max_95pct_orientations_m'], 'sci', 3)
        n[f'{nom}_ech'] = (ligne['echelle_min_GeV'], 'sci', 2)
    for i, ligne in enumerate(t):
        n[f's{i}_sigma'] = (ligne['sigma_courant'], 'fix', 2 if i == 3 else 1)
        n[f's{i}_cdt'] = (ligne['c_dt_sur_a'], 'fix', 3)
        if ligne['a_max_pire_orientation_m'] is not None:
            n[f's{i}_pire'] = (ligne['a_max_pire_orientation_m'], 'sci', 3)
        n[f's{i}_95'] = (ligne['a_max_95pct_orientations_m'], 'sci', 3)
        n[f's{i}_med'] = (ligne['a_max_orientation_mediane_m'], 'sci', 3)
    for nom, ligne, prec_eta, prec_ret, echelle_ret in (
            ('p26', p26, ('fix', 1), ('fix', 1), 1), ('p27', p27, ('fix', 2), ('fix', 2), 1),
            ('p28', p28, ('fix', 4), ('fix', 2), 1e3), ('pl', ppl, ('sci', 2), ('sci', 2), 1)):
        n[f'{nom}_eta_min'] = (ligne['eta2_min'], *prec_eta)
        n[f'{nom}_eta_max'] = (ligne['eta2_max'], *prec_eta)
        n[f'{nom}_ret_min'] = (ligne['retard_1TeV_0p3TeV_s_min'] * echelle_ret, *prec_ret)
        n[f'{nom}_ret_max'] = (ligne['retard_1TeV_0p3TeV_s_max'] * echelle_ret, *prec_ret)
    return n


def table_test_2(r: dict) -> dict[str, tuple[float, str, int]]:
    d, m, x, l = r['donnees'], r['methode'], r['resultats'], r['limite_superieure_95']
    return {
        'n_evt': (d['n_evenements'], 'ent', 0),
        'n_calib': (len(d['ecartes_etalonnage']), 'ent', 0),
        'e_min': (d['energie_min_EeV'], 'ent', 0),
        'e_max': (d['energie_max_EeV'], 'ent', 0),
        'lat': (m['latitude_deg'], 'fix', 1),
        'zmax': (m['zenith_max_deg'], 'ent', 0),
        'dec_max': (m['declinaison_max_visible_deg'], 'fix', 1),
        'ciel_pct': (100 * m['fraction_du_ciel_visible'], 'ent', 0),
        'angle_diag': (m['angle_axe_diagonale_deg'], 'fix', 1),
        'n_orient': (m['orientations'], 'ent', 0),
        'n_ciels': (m['ciels_isotropes'], 'ent', 0),
        'n_ciels_signal': (m['ciels_par_amplitude'], 'ent', 0),
        'alpha6': (m['fonction_l6_alpha'], 'fix', 4),
        'z4': (x['Z4_observe'], 'fix', 2),
        'p4': (x['p_valeur_l4'], 'fix', 2),
        'p4_pct': (100 * x['p_valeur_l4'], 'ent', 0),
        'z6': (x['Z6_observe'], 'fix', 2),
        'p6': (x['p_valeur_l6'], 'fix', 2),
        'z46': (x['Z46_observe'], 'fix', 1),
        'p46': (x['p_valeur_l4_l6'], 'fix', 2),
        'z4_50': (x['seuils_Z4_isotrope']['0.5'], 'fix', 2),
        'z4_95': (x['seuils_Z4_isotrope']['0.95'], 'fix', 2),
        'z4_99': (x['seuils_Z4_isotrope']['0.99'], 'fix', 2),
        'z4_999': (x['seuils_Z4_isotrope']['0.999'], 'fix', 2),
        'q_obs': (x['Q_moyen_observe'], 'fix', 4),
        'q_iso': (x['Q_moyen_attendu_isotrope'], 'fix', 4),
        'q_ecart_pct': (100 * x['ecart_relatif_Q'], 'fix', 1),
        'eps_axes': (l['epsilon_axes_max'], 'fix', 2),
        'eps_diag': (l['epsilon_diagonales_max'], 'fix', 2),
        'n_orient_fixes': (l['n_orientations_fixes'], 'ent', 0),
        'n_ciels_fixes': (l['ciels_par_amplitude_orientation_fixe'], 'ent', 0),
        'eps_axes_fix': (l['pire_orientation_epsilon_axes_max'], 'fix', 2),
        'eps_diag_fix': (l['pire_orientation_epsilon_diagonales_max'], 'fix', 2),
        'eps_axes_fix_min': (min(o['epsilon_axes_max'] for o in l['par_orientation_fixe']), 'fix', 2),
        'eps_diag_fix_min': (min(o['epsilon_diagonales_max'] for o in l['par_orientation_fixe']), 'fix', 2),
        'exces_axes_pct': (100 * l['pire_orientation_epsilon_axes_max'], 'ent', 0),
        'exces_diag_pct': (100 * l['exces_diagonales_max_pire_orientation'], 'ent', 0),
        'ecart_orient': (r['autotests']['orientation_retrouvee_ecart_deg'], 'fix', 1),
    }


def table_test_3(r: dict) -> dict[str, tuple[float, str, int]]:
    s, v = r['resume'], r['variantes']
    n = {
        'n_src': (r['n_sources'], 'ent', 0),
        'n_orient': (r['constantes']['n_orientations'], 'ent', 0),
        'a_exclue': (s['maille_exclue_toutes_orientations_m'], 'sci', 2),
        'echelle': (s['echelle_min_toutes_orientations_GeV'], 'sci', 2),
        'planck_x': (s['rapport_sur_longueur_Planck'], 'sci', 1),
        'x_test1': (s['rapport_sur_test1_sigma0'], 'fix', 1),
        'x_beane': (s['rapport_sur_beane'], 'fix', 1),
        'x_beane0': (s['rapport_sigma0_sur_beane'], 'fix', 2),
        'b_beane': (s['beane_b_max_m'], 'sci', 2),
        'ae': (s['aE_sur_hbar_c_20TeV_a_la_borne'], 'sci', 1),
        'fc_max': (s['facteur_cosmologie_max'], 'fix', 3),
        'ecart_graines': (s['ecart_relatif_deux_graines_sigma1'], 'sci', 1),
        'x_min': (s['rapport_B_autres_sur_LHAASO_min'], 'fix', 1),
        'x_max': (s['rapport_B_autres_sur_LHAASO_max'], 'ent', 0),
        'ang_grb': (s['angle_diag_GRB221009A_pire_sigma1_deg'], 'fix', 1),
        'qeff_grb': (s['Qeff_GRB221009A_pire_sigma1'], 'fix', 4),
        'n_actives': (s['n_sources_actives_sigma1'], 'ent', 0),
        'ang_diag': (s['angle_entre_diagonales_deg'], 'fix', 2),
        'ang_190_090': (s['angle_GRB190114C_GRB090510_deg'], 'fix', 2),
        'ang_090_pks': (s['angle_GRB090510_PKS2155_deg'], 'fix', 2),
        'couverture': (100 * s['couverture_min_bonferroni_sigma1'], 'ent', 0),
        'med1': (s['mediane_sigma1_m'], 'sci', 2),
        'v_sans_lhaaso': (v['sans_LHAASO']['sigma_1']['pire_m'], 'sci', 2),
        'v_sans_cosmo': (v['sans_cosmologie_commune']['sigma_1']['pire_m'], 'sci', 2),
        'v_fermi': (v['Fermi_tableau_V']['sigma_1']['pire_m'], 'sci', 2),
        'v_sursauts': (v['sursauts_seuls']['sigma_1']['pire_m'], 'sci', 2),
        'v_blazars': (v['blazars_et_pulsar_seuls']['sigma_1']['pire_m'], 'sci', 2),
    }
    for cle, nom in (('0', 'sigma0'), ('05', 'sigma05'), ('09', 'sigma09'), ('1', 'sigma1')):
        n[f'pire{cle}'] = (s[f'pire_{nom}_m'], 'sci', 2)
        n[f'q95_{cle}'] = (s[f'q95_{nom}_m'], 'sci', 2)
    for i, src in enumerate(r['sources']):
        d = src['z'] if src['z'] is not None else src['distance_kpc']
        n[f's{i}_z'] = (d, 'fix', len(repr(d).split('.')[1]))
        n[f's{i}_pub'] = (src['EQG2_imprime_GeV'], 'sci', 2)
        n[f's{i}_com'] = (src['EQG2_commun_GeV'], 'sci', 3)
        n[f's{i}_b'] = (src['a_racine_Qeff_max_m'], 'sci', 3)
    return n


def table_test_4(r: dict) -> dict[str, tuple[float, str, int]]:
    def v(chemin: str):
        d = r
        for cle in chemin.split('.'):
            d = d[cle]
        return d
    n = {}
    for nom, chemin, genre, prec in (
            ('bits_total', 'volume.bits_total', 'ent', 0),
            ('bits_bruts', 'volume.bits_bruts_non_haches', 'ent', 0),
            ('n_parity', 'donnees.parity.n_bits', 'ent', 0),
            ('n_ibm', 'donnees.ibm.n_bits', 'ent', 0),
            ('n_anu', 'donnees.anu.n_bits', 'ent', 0),
            ('n_beacon', 'donnees.beacon.n_bits', 'ent', 0),
            ('engagements', 'donnees.beacon.engagements_verifies', 'ent', 0),
            ('annexe_n', 'autotests.annexe_b_valeurs_verifiees', 'ent', 0),
            ('annexe_ecart', 'autotests.annexe_b_ecart_max', 'sci', 2),
            ('annexe_ecart_chev', 'autotests.annexe_b_ecart_max_chevauchant', 'sci', 2),
            ('n_seq', 'volume.sequences_nist_total', 'ent', 0),
            ('np1', 'familles.principale_niveau1_nist.n_p', 'ent', 0),
            ('par_np1', 'donnees.parity.niveau1.n_p', 'ent', 0),
            ('par_p1', 'donnees.parity.niveau1.p_holm_min', 'fix', 2),
            ('par_frac', 'donnees.parity.fraction_de_1', 'fix', 5),
            ('anu_p1', 'donnees.anu.niveau1.p_holm_min', 'fix', 2),
            ('ibm_rej1', 'donnees.ibm.niveau1.rejets', 'ent', 0),
            ('ibm_np1', 'donnees.ibm.niveau1.n_p', 'ent', 0),
            ('ibm_frac', 'donnees.ibm.fraction_de_1', 'fix', 4),
            ('ibm_z', 'donnees.ibm.z_biais', 'fix', 1),
            ('vn_bits', 'diagnostic_von_neumann.ibm_sans_belem.bits_apres_extraction', 'ent', 0),
            ('vn_np', 'diagnostic_von_neumann.ibm_sans_belem.n_p', 'ent', 0),
            ('vn_p', 'diagnostic_von_neumann.ibm_sans_belem.p_holm_min', 'fix', 2),
            ('seg_bm', 'methode.segment_bm', 'ent', 0),
            ('etat_max', 'methode.etat_max_detecte_bits', 'ent', 0),
            ('rep_attendu', 'donnees.parity.niveau2.repetitions.attendu_poisson', 'sci', 2),
            ('lag_max', 'methode.lag_max', 'ent', 0),
            ('np2', 'familles.principale_niveau2_cible.n_p', 'ent', 0),
            ('par_p2', 'donnees.parity.niveau2.p_holm_min', 'fix', 2),
            ('par_ecart_l', 'donnees.parity.niveau2.complexite_ecart_max_a_n_sur_2', 'ent', 0),
            ('par_auto', 'donnees.parity.niveau2.autocorrelation.longue_portee_17_65536.p_bonferroni', 'fix', 2),
            ('ibm_rej2', 'donnees.ibm.niveau2.rejets', 'ent', 0),
            ('ibm_essais', 'donnees.ibm.n_essais', 'ent', 0),
            ('ibm_const', 'donnees.ibm.n_essais_tous_egaux', 'ent', 0),
            ('ibm_const0', 'donnees.ibm.n_essais_tous_a_0', 'ent', 0),
            ('ibm_const1', 'donnees.ibm.n_essais_tous_a_1', 'ent', 0),
            ('ibm_quasi', 'donnees.ibm.n_essais_quasi_constants', 'ent', 0),
            ('ibm_paires', 'donnees.ibm.niveau2.repetitions.paires_identiques', 'sci', 3),
            ('ibm_paires_typ', 'donnees.ibm.niveau2.repetitions.paires_identiques_fenetres_typiques', 'ent', 0),
            ('sb_bits', 'donnees.ibm_sans_belem.n_bits', 'ent', 0),
            ('sb_np2', 'donnees.ibm_sans_belem.niveau2.n_p', 'ent', 0),
            ('sb_p2', 'donnees.ibm_sans_belem.niveau2.p_holm_min', 'fix', 2),
            ('sb_ecart_l', 'donnees.ibm_sans_belem.niveau2.complexite_ecart_max_a_n_sur_2', 'ent', 0),
            ('sb_r1', 'donnees.ibm_sans_belem.niveau2.autocorrelation.r_lag1', 'fix', 4),
            ('sb_z1', 'donnees.ibm_sans_belem.niveau2.autocorrelation.courte_portee_1_16.z_max', 'fix', 1),
            ('sb_rej1', 'donnees.ibm_sans_belem.niveau1.rejets', 'ent', 0),
            ('sb_np1', 'donnees.ibm_sans_belem.niveau1.n_p', 'ent', 0),
            ('bits_ctrl', 'methode.bits_par_controle', 'ent', 0),
            ('mt_p1', 'controles.mersenne_twister.niveau1_p_holm_min', 'fix', 2),
            ('pcg_p1', 'controles.pcg64.niveau1_p_holm_min', 'fix', 2),
            ('pcg_p2', 'controles.pcg64.niveau2_p_holm_min', 'fix', 2),
            ('sha_p1', 'controles.sha256_compteur.niveau1_p_holm_min', 'fix', 2),
            ('sha_p2', 'controles.sha256_compteur.niveau2_p_holm_min', 'fix', 2),
            ('r2_p1', 'controles.racine_de_2.niveau1_p_holm_min', 'fix', 2),
            ('r2_p2', 'controles.racine_de_2.niveau2_p_holm_min', 'fix', 2)):
        n[nom] = (v(chemin), genre, prec)
    for nom, gen in (('l20', 'lfsr_degre_20'), ('l31', 'lfsr_degre_31'), ('mt', 'mersenne_twister')):
        c = r['controles'][gen]
        n[f'{nom}_lmin'] = (min(c['complexite_min_par_decimation'].values()), 'ent', 0)
        n[f'{nom}_log10p'] = (c['complexite_log10_p_min'], 'ent', 0)
    return n


def table_synthese(r: dict) -> dict[str, tuple[float, str, int]]:
    """Synthèse : ses calculs, les valeurs citées qu'elle enregistre et les tests n° 1 à 3 qu'elle
    recopie ; la limite retenue par le test n° 2 et le volume du test n° 4 viennent de leurs fichiers."""
    def v(d, chemin: str):
        for cle in chemin.split('.'):
            d = d[int(cle)] if isinstance(d, list) else d[cle]
        return d

    def lire(dossier: str) -> dict:
        return json.loads((RACINE / 'recherche' / dossier / 'resultats.json').read_text(encoding='utf-8'))
    n = {}
    for nom, chemin, genre, prec in (
            ('conf_genereux', 'scenarios.genereux.exact.confiance_c_fois_esperance', 'fix', 3),
            ('conf_genereux_c', 'scenarios.genereux_conscience.exact.confiance_c_fois_esperance', 'fix', 2),
            ('conf_ignorance', 'scenarios.ignorance.exact.confiance_c_fois_esperance', 'fix', 2),
            ('conf_n_astro', 'scenarios.ignorance_N_astronomique.exact.confiance_c_fois_esperance', 'fix', 2),
            ('conf_observateurs', 'scenarios.ignorance_observateurs.exact.confiance_c_fois_esperance', 'fix', 3),
            ('conf_aeternam', 'scenarios.aeternam.exact.confiance_c_fois_esperance', 'fix', 3),
            ('x_1pct', 'bostrom.x_pour_f_sim_1_pct', 'fix', 3),
            ('x_99pct', 'bostrom.x_pour_f_sim_99_pct', 'ent', 0),
            ('largeur_transition', 'bostrom.largeur_transition_decades', 'fix', 1),
            ('b_facteur_moi', 'valeurs_citees.bostrom_facteur_me_simulations', 'sci', 1),
            ('r_moi', 'bostrom.r_me_simulation', 'sci', 1),
            ('largeur_critique', 'largeur_critique_decades_par_fraction', 'fix', 1),
            ('k_p', 'kipping.exemples.0.p', 'fix', 1),
            ('k_lambda', 'kipping.exemples.0.lambda', 'ent', 0),
            ('k_g', 'kipping.exemples.0.G', 'ent', 0),
            ('k_nsim', 'kipping.exemples.0.N_sim', 'ent', 0),
            ('k_p_simule', 'kipping.exemples.0.P_simule_CES', 'fix', 5),
            ('k_p_nullipare', 'kipping.exemples.0.P_simule_nullipare', 'fix', 3),
            ('k_p_base_parous', 'kipping.exemples.0.P_base_si_nous_simulions_eq32', 'fix', 4),
            ('k_nsim_ref', 'partition.N_sim_ou_x_de_reference', 'sci', 1),
            ('k_pi_tiers', 'kipping.prior_general_N_sim_1e9.1.P_simule_CES', 'fix', 3),
            ('k_pi_dixieme', 'kipping.prior_general_N_sim_1e9.2.P_simule_CES', 'fix', 3),
            ('part_deux', 'partition.deux_hypotheses_egales_kipping', 'fix', 2),
            ('part_trois', 'partition.trois_propositions_egales_bostrom', 'fix', 2),
            ('w_ex', 'tests_de_grille.mise_a_jour.1.w', 'fix', 1),
            ('w_apres', 'tests_de_grille.mise_a_jour.1.P_apres', 'fix', 2),
            ('w_dixieme', 'tests_de_grille.w_pour_passer_de_un_demi_a_un_dixieme', 'fix', 2),
            ('b_humains', 'valeurs_citees.bostrom_H_humains', 'sci', 1),
            ('b_annees', 'valeurs_citees.bostrom_annees_par_humain', 'ent', 0),
            ('b_secondes', 'valeurs_citees.bostrom_secondes_par_an', 'sci', 1),
            ('b_cerveau_min', 'valeurs_citees.bostrom_ops_cerveau_min', 'sci', 1),
            ('b_cerveau_max', 'valeurs_citees.bostrom_ops_cerveau_max', 'sci', 1),
            ('b_imprime_min', 'faisabilite.bostrom_note10.imprime_min', 'sci', 1),
            ('b_imprime_max', 'faisabilite.bostrom_note10.imprime_max', 'sci', 1),
            ('b_produit_min', 'faisabilite.bostrom_note10.produit_min', 'sci', 2),
            ('b_produit_max', 'faisabilite.bostrom_note10.produit_max', 'sci', 2),
            ('b_facteur', 'faisabilite.bostrom_note10.facteur_ecart', 'ent', 0),
            ('decades_min', 'faisabilite.decades_univers_sur_histoire_min', 'fix', 1),
            ('decades_max', 'faisabilite.decades_univers_sur_histoire_max', 'fix', 1),
            ('lloyd_ops_s', 'valeurs_citees.lloyd_laptop_ops_par_s', 'sci', 5),
            ('lloyd_bits', 'valeurs_citees.lloyd_laptop_bits', 'sci', 3),
            ('lloyd_univers_ops', 'valeurs_citees.lloyd_univers_ops', 'sci', 1),
            ('lloyd_univers_bits', 'valeurs_citees.lloyd_univers_bits_matiere', 'sci', 1),
            ('lloyd_univers_bits_grav', 'valeurs_citees.lloyd_univers_bits_gravitation', 'sci', 1),
            ('t1_maille', 'tests.test1.maille_max_pire_orientation_temps_continu_m', 'sci', 2),
            ('t2_n', 'tests.test2.n_evenements', 'ent', 0),
            ('t2_p', 'tests.test2.p_valeur_l4', 'fix', 2),
            ('t3_n', 'tests.test3.n_sources', 'ent', 0),
            ('t3_maille', 'tests.test3.maille_exclue_toutes_orientations_m', 'sci', 2),
            ('t3_planck', 'tests.test3.rapport_sur_longueur_planck', 'sci', 2)):
        n[nom] = (v(r, chemin), genre, prec)
    # Les mêmes résultats, dits en mots dans l'explication (« une chance sur 7 », « 3 chances sur cent »).
    n['un_sur_ignorance'] = (1 / n['conf_ignorance'][0], 'ent', 0)
    n['pct_observateurs'] = (100 * n['conf_observateurs'][0], 'ent', 0)
    # Notre choix central, repris sur l'accueil : « environ 7 % », « une chance sur 14 ».
    n['pct_aeternam'] = (100 * n['conf_aeternam'][0], 'ent', 0)
    n['un_sur_aeternam'] = (1 / n['conf_aeternam'][0], 'ent', 0)
    n['n_autotests'] = (len(r['autotests']), 'ent', 0)
    # Test n° 2 : la limite que retient son article (pire des orientations fixées), comme table_test_2.
    t2 = lire('2026-09-28-rayons-cosmiques')
    n['t2_exces_pct'] = (100 * t2['limite_superieure_95']['pire_orientation_epsilon_axes_max'], 'ent', 0)
    t4 = lire('2026-09-28-hasard-quantique')
    n['t4_bits_bruts'] = (t4['volume']['bits_bruts_non_haches'], 'ent', 0)
    return n


def table_audit(r: dict) -> dict[str, tuple[float, str, int]]:
    """Audit des démonstrations du « oui » (Vopson 2023, 2025, 2026)."""
    def v(chemin: str):
        d = r
        for cle in chemin.split('.'):
            d = d[int(cle)] if isinstance(d, list) else d[cle]
        return d
    m, c = 'multiplicites.', 'codage.'
    n = {}
    for nom, chemin, genre, prec in (
            ('i33', m + 'contre_exemple_N6.egal_3_3_bits', 'ent', 0),
            ('i42', m + 'contre_exemple_N6.g_4_2_bits', 'fix', 9),
            ('i51', m + 'contre_exemple_N6.g_5_1_bits', 'fix', 9),
            ('nb_cas', m + 'enumeration.nb_cas', 'ent', 0),
            ('nb_compo', m + 'enumeration.nb_compositions_examinees', 'ent', 0),
            ('nb_non_triv', m + 'enumeration.nb_cas_non_triviaux', 'ent', 0),
            ('nb_max', m + 'enumeration.nb_cas_ou_repartition_la_plus_egale_est_le_maximum', 'ent', 0),
            ('nb_min', m + 'enumeration.nb_cas_ou_repartition_la_plus_egale_est_le_minimum', 'ent', 0),
            ('nb_points', m + 'concavite.nb_points', 'ent', 0),
            ('d2_max', m + 'concavite.derivee_seconde_max_observee', 'sci', 2),
            ('ecart_hess', m + 'concavite.ecart_relatif_max_numerique_vs_hessienne', 'sci', 2),
            ('p_tri', 'polygones.formes.triangle_quelconque.I_bits', 'fix', 3),
            ('p_quad', 'polygones.formes.quadrilatere_quelconque.I_bits', 'ent', 0),
            ('p_penta', 'polygones.formes.pentagone_quelconque.I_bits', 'fix', 3),
            ('p_carre', 'polygones.formes.carre.I_bits', 'ent', 0),
            ('p_iso', 'polygones.formes.triangle_isocele.I_bits', 'fix', 9),
            ('p_rect', 'polygones.formes.rectangle.I_bits', 'fix', 1),
            ('ds', 'thermodynamique.detente_libre.Delta_S_J_par_K_arrondi', 'fix', 9),
            ('r_gaz', 'thermodynamique.detente_libre.R_J_par_mol_K', 'fix', 14),
            ('ds_info', 'thermodynamique.reponse_2025_signe.cas.3.dS_info', 'ent', 0),
            ('h_src', c + 'H_source_bits', 'fix', 2),
            ('h_code', c + 'H_mots_de_code_bits', 'fix', 2),
            ('nb_msg', c + 'messages_de_3_symboles.nb', 'ent', 0),
            ('h_msg', c + 'messages_de_3_symboles.H_codes_bits', 'fix', 2),
            ('l_pref', c + 'longueur_moyenne_prefixe_bits', 'fix', 2),
            ('l_fixe', c + 'longueur_moyenne_fixe_bits', 'ent', 0),
            ('hb_fixe', c + 'entropie_par_bit_code_fixe', 'fix', 3),
            ('hb_pref', c + 'entropie_par_bit_code_prefixe', 'ent', 0),
            ('h_perte', c + 'avec_perte.H_apres_bits', 'fix', 1),
            ('info_perdue', c + 'avec_perte.information_perdue_bits', 'fix', 2)):
        n[nom] = (float(v(chemin)), genre, prec)
    return n


def table_projet(r: dict) -> dict[str, tuple[float, str, int]]:
    return {'vie_ans': (r['hypotheses']['vie_ans'], 'ent', 0),
            'nuit_h': (r['hypotheses']['nuit_heures'], 'ent', 0),
            'facteur': (r['facteur_nuit_entiere'], 'ent', 0)}


def table_par_marqueurs(nom: str):
    """Table lue dans site/nombres/<nom>.json : [marqueur, clé de resultats.json, échelle, genre, précision]."""
    spec = json.loads((SITE / 'nombres' / f'{nom}.json').read_text(encoding='utf-8'))

    def table(r: dict) -> dict[str, tuple[float, str, int]]:
        n = {}
        for marqueur, cle, echelle, genre, precision in spec:
            d = r
            for morceau in (cle if isinstance(cle, list) else cle.split('.')):
                d = d[int(morceau)] if isinstance(d, list) else d[morceau]
            n[marqueur] = (float(d) * echelle, genre, precision)
        return n
    return table


# Une étude = une page. attribut : nom du dictionnaire dans site/langues/fr.py.
# Les listes sont triées par publication ; l'ordre ci-dessous départage les dates égales.
# 'sujets' référence les rubriques de SUJETS ; un article peut en relier plusieurs.
ETUDES = (
    {'chemin': '/lecture-cerveau/', 'attribut': 'LECTURE_CERVEAU', 'sujets': ('memoire',),
     'dossier': '2026-11-20-piste-lecture-cerveau', 'table': table_par_marqueurs('lecture-cerveau'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md', 'protocole.md')},
    {'chemin': '/combinaisons/', 'attribut': 'COMBINAISONS', 'sujets': ('vieillissement',),
     'dossier': '2026-11-20-piste-combinaisons', 'table': table_par_marqueurs('combinaisons'),
     'fichiers': ('analyse.py', 'resultats.json', 'releves.json', 'sources.md', 'protocole.md')},
    {'chemin': '/reve-recit/', 'attribut': 'REVE_RECIT',
     'dossier': '2026-10-08-reve-recit', 'sujets': ('reve-temps', 'memoire'),
     'table': table_par_marqueurs('reve-recit'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md', 'protocole.json',
                  'disponibilite.json', 'tableau-signaux.csv', 'provenance-tableau.json',
                  'schema-paires.csv', 'verifier.py', 'verification.json', 'README.md',
                  'figures.py', 'requirements-figures.txt', 'contrat-figure.md',
                  'signaux-par-personne.svg', 'signaux-par-personne.png')},
    {'chemin': '/einstein-relativite-restreinte/', 'attribut': 'EINSTEIN_RESTREINTE',
     'dossier': '2026-10-08-einstein-hawking', 'sujets': ('relativite',),
     'table': table_par_marqueurs('einstein-hawking'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/gravitation-horloges/', 'attribut': 'GRAVITATION_HORLOGES',
     'dossier': '2026-10-08-einstein-hawking', 'sujets': ('relativite',),
     'table': table_par_marqueurs('einstein-hawking'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md', 'figures.py',
                  'requirements-figures.txt', 'contrat-figures.md',
                  'terre-horloges.svg', 'terre-horloges.png',
                  'trou-noir-horloges.svg', 'trou-noir-horloges.png')},
    {'chemin': '/hawking-trous-noirs-limites/', 'attribut': 'HAWKING_LIMITES',
     'dossier': '2026-10-08-einstein-hawking', 'sujets': ('relativite',),
     'table': table_par_marqueurs('einstein-hawking'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/bci-monte-carlo/', 'attribut': 'BCI_MONTE_CARLO', 'dossier': '2026-10-03-bci-monte-carlo',
     'sujets': ('bci',), 'table': table_par_marqueurs('bci-monte-carlo'),
     'figures': lambda r, rem: visuels.monte_carlo_tableaux(r),
     'fichiers': ('analyse.py', 'protocole.json', 'resultats.json', 'sources.md', 'validation.md',
                  'verifier.py', 'verification.json', 'figures.py', 'requirements-verification.txt',
                  'contrat-figures.md', 'calibration-bruit.svg', 'calibration-bruit.png',
                  'sensibilite-modele.svg', 'sensibilite-modele.png')},
    {'chemin': '/bci-generalisation/', 'attribut': 'BCI_GENERALISATION', 'dossier': '2026-10-03-bci-generalisation',
     'sujets': ('bci',), 'table': table_par_marqueurs('bci-generalisation'),
     'figures': lambda r, rem: {'figure_bci_tableau': visuels.bci_tableau(r)},
     'fichiers': ('analyse.py', 'extraire.py', 'verifier.py', 'figure.py', 'resultats.json',
                  'protocole.json', 'releves.json', 'verification.json', 'sources.md',
                  'requirements-extraction.txt', 'donnees/caracteristiques.csv', 'donnees/manifest.json',
                  'resultats-individuels.svg', 'resultats-individuels.png')},
    {'chemin': '/interfaces-cerveau/', 'attribut': 'INTERFACES_CERVEAU', 'dossier': '2026-10-03-interfaces-cerveau',
     'sujets': ('bci', 'vision', 'memoire'), 'table': table_par_marqueurs('interfaces-cerveau'),
     'fichiers': ('analyse.py', 'resultats.json', 'releves.json', 'sources.md')},
    {'chemin': '/meg-eeg-reves/', 'attribut': 'MEG_EEG_REVES', 'dossier': '2026-10-03-meg-eeg-reves',
     'sujets': ('bci', 'reve-temps'), 'table': table_par_marqueurs('meg-eeg-reves'),
     'fichiers': ('analyse.py', 'resultats.json', 'releves.json', 'disponibilite.json', 'sources.md')},
    {'chemin': '/programme/', 'attribut': 'PROGRAMME', 'dossier': '2026-09-29-programme-calcul',
     'sujets': ('reve-temps', 'memoire'), 'table': table_par_marqueurs('programme'),
     'figures': lambda r, rem: {'figure_parcours': visuels.parcours_recherche(),
                                 'figure_dream': visuels.figure_dream(r),
                                 'figure_erreurs': visuels.figure_faux_positifs(r)},
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/synthese/', 'attribut': 'SYNTHESE', 'dossier': '2026-09-28-synthese', 'publication': '2026-09-29',
     'sujets': ('simulation',), 'table': table_synthese, 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/temps-stimulation/', 'attribut': 'TEMPS_STIMULATION', 'sujets': ('reve-temps',), 'dossier': '2026-09-29-temps-stimulation',
     'table': table_par_marqueurs('temps-stimulation'), 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/temps-reve/', 'attribut': 'TEMPS_REVE', 'sujets': ('reve-temps', 'memoire'), 'dossier': '2026-09-29-temps-reve',
     'table': table_par_marqueurs('temps-reve'), 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/test-6/', 'attribut': 'ARTICLE_6', 'dossier': '2026-09-28-ciel-complet',
     'sujets': ('simulation',), 'table': table_par_marqueurs('test-6'),
     'fichiers': ('analyse.py', 'resultats.json', 'sources.md', 'donnees/AugerApJS2022_Yr_JD_UTC_Th_Ph_RA_Dec_E_Expo.dat',
                  'donnees/tasd_highest_event_244EeV_backtrack_JF_PT_eq.dat')},
    {'chemin': '/test-5/', 'attribut': 'ARTICLE_5', 'dossier': '2026-09-28-rendu-a-la-demande',
     'sujets': ('simulation',), 'table': table_par_marqueurs('test-5'),
     'fichiers': ('analyse.py', 'extraire.py', 'donnees/figures.json', 'resultats.json', 'sources.md')},
    {'chemin': '/audit-infodynamique/', 'attribut': 'AUDIT_1', 'dossier': '2026-09-28-audit-infodynamique',
     'sujets': ('simulation',), 'table': table_audit, 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/test-4/', 'attribut': 'ARTICLE_4', 'dossier': '2026-09-28-hasard-quantique',
     'sujets': ('simulation',), 'table': table_test_4, 'fichiers': ('analyse.py', 'telecharger.py', 'resultats.json', 'sources.md')},
    {'chemin': '/test-3/', 'attribut': 'ARTICLE_3', 'dossier': '2026-09-28-dispersion-directionnelle',
     'sujets': ('simulation',), 'table': table_test_3, 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
    {'chemin': '/test-2/', 'attribut': 'ARTICLE_2', 'dossier': '2026-09-28-rayons-cosmiques',
     'sujets': ('simulation',), 'table': table_test_2, 'fichiers': ('analyse.py', 'resultats.json', 'donnees/auger_catalogSD.csv')},
    {'chemin': '/test-1/', 'attribut': 'ARTICLE', 'dossier': '2026-09-28-grille-lhaaso',
     'sujets': ('simulation',), 'table': table_des_nombres, 'fichiers': ('analyse.py', 'resultats.json')},
    {'chemin': '/projet/', 'attribut': 'PROJET', 'dossier': '2026-09-28-une-vie-en-une-nuit', 'publication': '2026-09-29', 'sujets': ('reve-temps', 'memoire'),
     'table': table_projet, 'fichiers': ('analyse.py', 'resultats.json', 'sources.md')},
)


ETUDES_PAR_CHEMIN = {e['chemin']: e for e in ETUDES}


def formules_dangereuses(texte: str) -> list[str]:
    """Formules où « < » suivi d'une lettre serait lu comme une balise HTML (écrire \\lt)."""
    return [f for f in FORMULE.findall(texte) if re.search(r'<[A-Za-z/!?]', f)]


def remplir(texte: str, nombres: dict, module, extras: dict) -> str:
    def un(m):
        nom = m.group(1)
        if nom in extras:
            return extras[nom]
        valeur, genre, precision = nombres[nom]
        return ecrire_nombre(valeur, genre, precision, module.DECIMALE, module.MILLIERS)
    return MARQUEUR.sub(un, texte)


def typo(texte: str, module) -> str:
    """Textes courts des pages : en français, la ponctuation haute et le signe % restent attachés au mot qui précède."""
    if module.HTML_LANG != 'fr':
        return texte
    return re.sub(r' (?=[:;!?%»])', FINE, texte).replace('« ', '«' + FINE)


def formules_de_la_langue(corps: str, module) -> str:
    """Les formules sont les mêmes dans toutes les langues ; seule la virgule décimale {,} devient un point en anglais."""
    if module.DECIMALE == ',':
        return corps
    return FORMULE.sub(lambda m: re.sub(r'(?<=\d)\{,\}(?=\d)', '.', m.group(0)), corps)


def date_longue(jour, module) -> str:
    mois = module.MOIS[jour.month - 1]
    if module.HTML_LANG == 'en':
        return f'{mois} {jour.day}, {jour.year}'
    return f'{jour.day}{"er" if jour.day == 1 else ""} {mois} {jour.year}'


def bits_quantiques(nombre: int = 46) -> str:
    """Les vrais bits quantiques du test n° 4, repris dans le dessin de la simulation."""
    return ''.join(str(b) for b in visuels._bits_fichier(visuels.HASARD / 'donnees' / 'parity_qrng.bin', nombre))


def version(*fichiers: Path) -> str:
    """Empreinte courte du contenu, ajoutée aux adresses des fichiers pour vider les caches."""
    return hashlib.sha256(b''.join(f.read_bytes() for f in fichiers)).hexdigest()[:12]


PAPIER, NUIT = '#f2efe7', '#131211'
# Les éditions : le français à la racine, l'anglais sous /en/, mêmes adresses de pages.
EDITIONS = ('fr', 'en')
MODULES: dict = {}          # code de langue -> module de site/langues/, rempli par construire()
RACINES = ('/fichiers/', '/contributions/', '/polices/')   # jamais préfixés : communs aux deux éditions


def prefixer(texte: str, prefixe: str) -> str:
    """Édition anglaise : les liens internes vers une page reçoivent /en. Les fichiers (une
    extension), les polices et les articles de la communauté restent à la racine."""
    if not prefixe:
        return texte

    def un(m):
        chemin = m.group(1)
        nu = re.split(r'[?#]', chemin, maxsplit=1)[0]
        if not nu.endswith('/') or nu.startswith(RACINES):
            return m.group(0)
        return f'href="{prefixe}{chemin}"'
    return re.sub(r'href="(/[^"]*)"', un, texte)


def page(module, chemin: str, titre: str, description: str, contenu: str,
         classe: str, maths: bool, tete: str = '', autre_chemin: str | None = None) -> str:
    """Une page complète. `chemin` est l'adresse sans préfixe de langue ; `autre_chemin` est
    donné quand la page n'existe que dans une langue (article de la communauté, 404) :
    c'est alors la page de l'autre édition vers laquelle pointe le lien de langue."""
    ui = module.UI
    contenu = re.sub(r'<main(?=[ >])', '<main id="aeternam-contenu"', contenu, count=1)
    classes = classe.split()
    version_style = version(SITE / 'style.css')
    lecture_js = f'<script defer src="/base.js?v={version(SITE / "base.js")}"></script>'
    if 'lecture' in classes:
        lecture_js += f'<script defer src="/lecture.js?v={version(SITE / "lecture.js")}"></script>'
    katex = ''
    if maths:
        katex = (f'<link rel="stylesheet" href="{KATEX}katex.min.css" crossorigin="anonymous">\n'
                 f'<script defer src="{KATEX}katex.min.js" crossorigin="anonymous"></script>\n'
                 f'<script defer src="{KATEX}contrib/auto-render.min.js" crossorigin="anonymous" '
                 "onload=\"renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},"
                 "{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false})\"></script>\n")
    navigation = []
    for cible, libelle in ui['nav']:
        courant = ' aria-current="page"' if chemin == cible else ''
        if not courant and ((cible == '/sujets/' and chemin.startswith('/sujets/'))
                            or (cible == '/recherches/' and 'lecture' in classes)):
            courant = ' aria-current="true"'
        navigation.append(f'<a href="{cible}"{courant}>{libelle}</a>')
    # Le lien vers l'autre édition : écrit après le préfixage, il garde son adresse telle quelle.
    autres = [m for m in MODULES.values() if m is not module]
    langue_barre = langue_pied = alternatives = ''
    for autre in autres:
        cible = autre.PREFIXE + (autre_chemin or chemin)
        attributs = f'href="{cible}" lang="{autre.HTML_LANG}" hreflang="{autre.HREFLANG}"'
        langue_barre += f'<a class="langue" {attributs} aria-label="{autre.UI["version"]}">{autre.HTML_LANG.upper()}</a>'
        langue_pied += f'<a {attributs}>{autre.NOM}</a>'
    if autres and autre_chemin is None:
        alternatives = ''.join(f'<link rel="alternate" hreflang="{m.HREFLANG}" href="{DOMAINE}{m.PREFIXE}{chemin}">\n'
                               for m in MODULES.values())
        alternatives += f'<link rel="alternate" hreflang="x-default" href="{DOMAINE}{chemin}">\n'
    # Une pilule flottante, la même sur toutes les pages : le signe Æ, les rubriques, l'autre langue.
    barre = (f'<header class="barre" id="haut"><nav aria-label="{ui["nav_principale"]}">'
             f'<a class="marque" href="/" aria-label="{ui["accueil_label"]}">Æ</a>'
             + ''.join(navigation) + '\x00</nav></header>\n')
    pied = ('<footer class="pied-site nuit"><div class="pied-dedans">'
            f'<nav aria-label="{ui["nav_fin"]}">'
            + ''.join(f'<a href="{cible}">{libelle}</a>' for cible, libelle in ui['nav']) +
            f'\x01</nav><p class="pied-licence">{ui["licence_pied"]}</p>'
            f'<a class="haut-page" href="#haut">{ui["en_haut"]} ' + FLECHE + '</a>'
            f'<a class="pied-mot" href="/" aria-label="{ui["accueil_label"]}">ÆTERNAM</a></div></footer>')
    filtres = dessins.FILTRES if 'class="dessin' in contenu else ''
    corps = prefixer(barre + contenu + pied, module.PREFIXE).replace('\x00', langue_barre).replace('\x01', langue_pied)
    if module.HTML_LANG != 'fr':  # la licence s'ouvre dans la langue du lecteur, pas en français
        corps = corps.replace('/licenses/by/4.0/deed.fr', '/licenses/by/4.0/')
    # Les pages qui s'ouvrent sur une planche sombre (accueil, thèmes) teintent la barre du navigateur.
    teinte = NUIT if {'arrivee', 'page-sujet'} & set(classes) else PAPIER
    adresse = f'{DOMAINE}{module.PREFIXE}{chemin}'
    return f'''<!doctype html>
<html lang="{module.HTML_LANG}" dir="{module.DIR}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{adresse}">
{alternatives}<meta property="og:title" content="{html.escape(titre)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{adresse}">
<meta property="og:locale" content="{module.LOCALE_OG}">
<meta name="theme-color" content="{teinte}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/polices/newsreader-latin.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add('js')</script>
<link rel="stylesheet" href="/style.css?v={version_style}">
{tete}{lecture_js}
{katex}</head>
<body class="{classe}">
<a class="lien-evitement" href="#aeternam-contenu">{ui['aller_contenu']}</a>
{filtres}{corps}
</body>
</html>
'''


# ------------------------------------------------------------------ le blog : listes d'articles
def date_etude(etude: dict) -> str:
    return etude.get('publication', etude['dossier'][:10])


def etudes_par_date():
    return sorted(ETUDES, key=date_etude, reverse=True)


def liens_sujets(module, cles):
    return ' · '.join(f'<a href="{module.SUJETS[cle]["chemin"]}">{html.escape(module.SUJETS[cle]["titre"])}</a>'
                      for cle in cles)


def entree_etude(module, etude, niveau: int, afficher_sujets: bool) -> str:
    a = getattr(module, etude['attribut'])
    rubriques = (f'<p class="sujets-article">{liens_sujets(module, etude["sujets"])}</p>' if afficher_sujets else '')
    return f'''<li class="entree-article">
<h{niveau}><a class="lien-article" href="{etude['chemin']}"><span>{titre_html(a['titre'])}</span>{FLECHE}</a></h{niveau}>
<p>{html.escape(a["description"])}</p>{rubriques}
</li>'''


def signe_par(module, a: dict) -> str:
    """« Signé Prénom Nom, le 3 décembre 2026 », et la langue de l'article si ce n'est pas celle de la page."""
    ligne = module.UI['signe_par'].format(auteur=html.escape(a['auteur']), date=date_longue(a['jour'], module))
    if a['langue'] != module.HTML_LANG:
        ligne += f' ({module.UI["ecrit_en"][a["langue"]]})'
    return ligne


def entree_signe(module, a: dict, niveau: int, afficher_sujets: bool) -> str:
    """Un article de la communauté : titre, résumé, signature et date."""
    resume = f'<p>{html.escape(a["resume"])}</p>' if a['resume'] else ''
    theme = (f' · <a href="{module.SUJETS[a["theme"]]["chemin"]}">{html.escape(module.SUJETS[a["theme"]]["titre"])}</a>'
             if a['theme'] and afficher_sujets else '')
    return f'''<li class="entree-article entree-signee">
<h{niveau}><a class="lien-article" href="{a['chemin']}" hreflang="{a['langue']}"><span>{titre_html(a['titre'])}</span>{FLECHE}</a></h{niveau}>
{resume}<p class="sujets-article">{signe_par(module, a)}{theme}</p>
</li>'''


def liste_articles(module, etudes=(), signes=(), niveau: int = 3, afficher_sujets: bool = True) -> str:
    """Les articles d'ÆTERNAM et ceux de la communauté dans une seule liste, du plus récent au plus ancien."""
    entrees = [(date_etude(e), entree_etude(module, e, niveau, afficher_sujets)) for e in etudes]
    entrees += [(a['jour'].isoformat(), entree_signe(module, a, niveau, afficher_sujets)) for a in signes]
    entrees.sort(key=lambda e: e[0], reverse=True)   # tri stable : l'ordre d'ETUDES départage les dates égales
    return '<ul class="liste-articles">\n' + '\n'.join(e for _, e in entrees) + '\n</ul>'


def liste_signes(module, signes, niveau: int = 3) -> str:
    """Tous les articles de la communauté, ou l'invitation à écrire le premier."""
    if not signes:
        return (f'<p class="aucun-signe">{module.UI["signes_aucun"]} '
                f'<a href="/ecrire/">{module.UI["signes_premier"]}</a></p>')
    return liste_articles(module, signes=signes, niveau=niveau)


def reponse_theme(module, cle: str) -> str:
    """La réponse en mots simples d'un thème ; ses nombres viennent des articles cités dans 'sources'."""
    s = module.SUJETS[cle]
    nombres = {}
    for source in s['sources']:
        nombres.update(ETUDES_PAR_CHEMIN[source]['nombres'])
    manquants = set(MARQUEUR.findall(s['reponse'])) - set(nombres)
    if manquants:
        raise SystemExit(f'thème {cle} ({module.HTML_LANG}) : marqueurs sans valeur dans la réponse : {sorted(manquants)}')
    return remplir(typo(html.escape(s['reponse'], quote=False), module), nombres, module, {})


def sommaire_themes(module):
    liens = ''.join(f'<li><a href="#{cle}"><span>{titre_html(s["titre"])}</span>{FLECHE}</a></li>'
                    for cle, s in module.SUJETS.items())
    liens += f'<li><a href="#signes"><span>{module.UI["signes_titre"]}</span>{FLECHE}</a></li>'
    return f'<nav id="sujets" class="index-sujets" aria-label="{module.UI["aller_theme"]}"><ul>{liens}</ul></nav>'


def articles_par_theme(module, signes) -> str:
    """Chaque thème : sa question, ce qu'il couvre, puis ses articles, ceux de la communauté compris."""
    sections = []
    for cle, s in module.SUJETS.items():
        etudes = [e for e in ETUDES if cle in e['sujets']]
        du_theme = [a for a in signes if a['theme'] == cle]
        sections.append(f'''<section id="{cle}" class="theme-recherche">
<div class="entete-theme"><h2><a href="{s['chemin']}">{titre_html(s['titre'])}</a></h2>
<p class="question-theme">{titre_html(s['question'])}</p>
<p class="description-theme">{html.escape(s['description'])}</p>
</div>
{liste_articles(module, etudes, du_theme, afficher_sujets=False)}
</section>''')
    return '\n'.join(sections)


def recherches(module, signes):
    ui = module.UI
    contenu = f'''<main><header><h1>{ui['recherches_h1']}</h1></header>
<p>{typo(ui['recherches_intro'], module)}</p>
{sommaire_themes(module)}
{articles_par_theme(module, signes)}
<section id="signes" class="theme-recherche">
<div class="entete-theme"><h2><a href="/ecrire/">{ui['signes_titre']}</a></h2>
<p class="description-theme">{ui['signes_description']}</p>
<p class="actions"><a class="bouton" href="/ecrire/">{ui['ecrire_article']} {FLECHE}</a></p>
</div>
{liste_signes(module, signes)}
</section>
</main>'''
    return page(module, '/recherches/', ui['recherches_titre'], ui['recherches_description'], contenu, 'article index-blog', False)


def sujets(module):
    ui = module.UI
    themes = '\n'.join(
        f'<li><div><h2><a class="lien-article" href="{s["chemin"]}">{titre_html(s["titre"])}</a></h2></div>'
        f'<div><p class="question-theme">{titre_html(s["question"])}</p><p>{html.escape(s["description"])}</p></div>{FLECHE}</li>'
        for s in module.SUJETS.values())
    contenu = f'''<main><header><h1>{ui['sujets_h1']}</h1></header>
<p>{typo(ui['sujets_intro'], module)}</p>
<ul class="liste-sujets">{themes}</ul>
</main>'''
    return page(module, '/sujets/', ui['sujets_titre'], ui['description_site'], contenu, 'article index-blog', False)


# Le dessin au trait de chaque thème (site/dessins.py), le même sur l'accueil et en tête de sa page.
DESSINS_SUJETS = {'vieillissement': dessins.vieillir, 'relativite': dessins.relativite, 'vision': dessins.vision, 'memoire': dessins.memoire,
                  'reve-temps': dessins.reve, 'bci': dessins.montage,
                  'simulation': lambda: dessins.simulation(bits_quantiques())}


def sujet(module, cle, signes):
    s, ui = module.SUJETS[cle], module.UI
    questions = ''.join(f'<li>{titre_html(q)}</li>' for q in s['questions'])
    lectures = ''.join(f'<li><a href="{lien}">{titre_html(titre)}</a></li>' for lien, titre in s['lectures'])
    etudes = [e for e in ETUDES if cle in e['sujets']]
    du_theme = [a for a in signes if a['theme'] == cle]
    contenu = f'''<main><header class="entete-sujet nuit"><div><h1>{titre_html(s['titre'])}</h1>
<p class="question">{titre_html(s['question'])}</p></div>
<figure class="dessin-sujet" data-vu>{DESSINS_SUJETS[cle]()}</figure></header>
<section class="reponse-theme"><p class="enjeu">{typo(html.escape(s['enjeu'], quote=False), module)}</p>
<p>{reponse_theme(module, cle)} <a class="lien-suite" href="{s['lien']}">{ui['sujet_source']} {FLECHE}</a></p></section>
{s['intro']}
<section><h2>{ui['sujet_questions']}</h2><ul>{questions}</ul></section>
<section><h2>{ui['sujet_commencer']}</h2><ul class="lectures">{lectures}</ul></section>
<section><h2>{ui['sujet_articles']}</h2>{liste_articles(module, etudes, du_theme)}</section>
<p class="retour-sujets"><a href="/sujets/">{ui['tous_themes']}</a> · <a href="/recherches/">{ui['tous_articles']}</a></p>
</main>'''
    return page(module, s['chemin'], f"{s['titre']} — ÆTERNAM", s['description'], contenu, 'article index-blog page-sujet', False)


def a_propos(module):
    a = module.A_PROPOS
    contenu = f'<main><header><h1>{titre_html(a["titre"])}</h1></header>{a["corps"]}</main>'
    return page(module, '/a-propos/', f'{a["titre"]} — ÆTERNAM', a['description'], contenu, 'article page-propos', False)


# ------------------------------------------------------------------ l'accueil
def themes_accueil(module, signes, par_theme: int = 3) -> list[dict]:
    """Les six thèmes du blog : la question, l'enjeu, la réponse chiffrée et les derniers articles."""
    a, themes = module.ACCUEIL, []
    for cle, s in module.SUJETS.items():
        articles = [(date_etude(e), e['chemin'], titre_html(getattr(module, e['attribut'])['titre']))
                    for e in ETUDES if cle in e['sujets']]
        articles += [(a['jour'].isoformat(), a['chemin'], f'{titre_html(a["titre"])} · {html.escape(a["auteur"])}')
                     for a in signes if a['theme'] == cle]
        articles.sort(key=lambda a: a[0], reverse=True)
        themes.append({
            'cle': cle, 'chemin': s['chemin'], 'question': titre_html(s['question']),
            'suite': typo(a['blog_theme'], module).format(titre=titre_html(s['titre']), n=len(articles)),
            'enjeu': typo(html.escape(s['enjeu'], quote=False), module), 'reponse': reponse_theme(module, cle),
            'lien': s['lien'], 'dessin': DESSINS_SUJETS[cle](),
            'articles': [{'chemin': chemin, 'titre': titre} for _, chemin, titre in articles[:par_theme]]})
    return themes


def accueil(module, signes) -> str:
    """Le nom et la question, le sablier dont le sable s'arrête, puis le blog : six questions et leurs articles."""
    a = module.ACCUEIL
    chiffres = list(zip((len(ETUDES), len({e['dossier'] for e in ETUDES}), len(module.SUJETS)), a['chiffres']))
    derniers = [{'chemin': s['chemin'], 'titre': titre_html(s['titre']), 'signature': signe_par(module, s)} for s in signes[:4]]
    textes = {cle: typo(valeur, module) if isinstance(valeur, str) else valeur for cle, valeur in a.items()}
    textes['manifeste'] = tuple(typo(phrase, module) for phrase in a['manifeste'])
    # Les chapitres du récit : leurs marqueurs viennent des études des deux pistes.
    nombres = ETUDES_PAR_CHEMIN['/combinaisons/']['nombres'] | ETUDES_PAR_CHEMIN['/lecture-cerveau/']['nombres']
    textes['chapitres'] = [{cle: remplir(typo(valeur, module), nombres, module, {}) for cle, valeur in c.items()}
                           for c in a['chapitres']]
    for c in textes['chapitres']:
        c['nombre'] = re.sub(r'</?bdi>', '', c['nombre'])     # le nombre que le sable écrit : sans balise
    contenu = page_accueil.corps(textes, themes_accueil(module, signes), chiffres, derniers, FLECHE)
    v = version(SITE / 'accueil' / 'accueil.css', SITE / 'accueil' / 'accueil.js')
    return page(module, '/', a['titre_page'], a['description'],
                contenu + f'\n<script defer src="/accueil/accueil.js?v={v}"></script>', 'arrivee', False,
                f'<link rel="stylesheet" href="/accueil/accueil.css?v={v}">\n')


# ------------------------------------------------------------------ les articles
def sommaire_article(corps: str, module) -> tuple[str, str]:
    """Repères de lecture ; les ancres déjà publiées restent inchangées."""
    ids = set(re.findall(r'\bid=[\"\']([^\"\']+)[\"\']', corps))
    entrees = []

    def reperer(m):
        attributs, titre = m.group(1), m.group(2)
        texte = html.unescape(re.sub(r'<[^>]+>', '', titre)).strip()
        existant = re.search(r'\bid=[\"\']([^\"\']+)[\"\']', attributs)
        if existant:
            identifiant = existant.group(1)
        else:
            simple = unicodedata.normalize('NFKD', texte).encode('ascii', 'ignore').decode().lower()
            base = 'section-' + re.sub(r'[^a-z0-9]+', '-', simple).strip('-')
            identifiant, i = base, 2
            while identifiant in ids:
                identifiant, i = f'{base}-{i}', i + 1
            ids.add(identifiant)
            attributs += f' id="{identifiant}"'
        entrees.append(f'<li><a href="#{html.escape(identifiant, quote=True)}">{html.escape(texte)}</a></li>')
        return f'<h2{attributs}>{titre}</h2>'

    corps = re.sub(r'<h2([^>]*)>(.*?)</h2>', reperer, corps, flags=re.S)
    liste = '<ol>' + ''.join(entrees) + '</ol>'
    libelle = module.UI['dans_article']
    sommaire = ('<aside class="reperes-lecture">'
                f'<nav class="sommaire-bureau" aria-label="{libelle}">' + liste + '</nav>'
                f'<details class="sommaire-mobile"><summary>{libelle}</summary>'
                f'<nav aria-label="{libelle}">' + liste + '</nav></details></aside>') if entrees else ''
    return corps, sommaire


def article(module, etude: dict) -> str:
    a, ui = getattr(module, etude['attribut']), module.UI
    nombres = etude['nombres']
    extras = {}
    if 'figures' in etude:
        extras.update(etude['figures'](etude['resultats'], lambda s: remplir(s, nombres, module, {})))
    corps = remplir(formules_de_la_langue(a['corps'], module), nombres, module, extras)
    corps, sommaire = sommaire_article(corps, module)
    # L'article suivant dans le premier thème, dans l'ordre de l'index ; le dernier renvoie au premier.
    voisins = [e for e in etudes_par_date() if etude['sujets'][0] in e['sujets']]
    suivant = ''
    if len(voisins) > 1:
        autre = voisins[(voisins.index(etude) + 1) % len(voisins)]
        suivant = (f'<p class="article-suivant"><a class="lien-article" href="{autre["chemin"]}">'
                   f'<span>{titre_html(getattr(module, autre["attribut"])["titre"])}</span>{FLECHE}</a></p>')
    contenu = f'''<main>
<header>
<h1>{titre_html(a['titre'])}</h1>
</header>
<div class="mise-en-lecture">{sommaire}<div class="corps-article">{corps}
<nav class="suite-article" aria-label="{ui['poursuivre']}">
<h2>{ui['lire_ensuite']}</h2>
{suivant}
<p>{liens_sujets(module, etude['sujets'])} · <a href="/recherches/">{ui['tous_articles']}</a></p>
</nav>
</div></div>
</main>'''
    return page(module, etude['chemin'], f"{a['titre']} — ÆTERNAM", a['description'], contenu,
                'article lecture', True)


def ecrire(module, signes) -> str:
    """Écrire sur ÆTERNAM : le formulaire prépare le fichier et l'ouvre sur GitHub (site/ecrire.js)."""
    e = module.ECRIRE
    licence, _ = contributions.LICENCE
    extras = {
        'options': ''.join(f'<option value="{cle}">{html.escape(s["titre"])}</option>' for cle, s in module.SUJETS.items()),
        'modele': html.escape(e['modele'], quote=True), 'depot': contributions.DEPOT, 'fleche': FLECHE,
        'licence': licence, 'adresse_licence': module.UI['adresse_licence'],
        'liste_signes': liste_signes(module, signes),
    }
    contenu = f'''<main><header><h1>{titre_html(e['titre'])}</h1></header>
{remplir(e['corps'], {}, module, extras)}
</main>
<script defer src="/ecrire.js?v={version(SITE / 'ecrire.js')}"></script>'''
    return page(module, '/ecrire/', e['titre'], e['description'], contenu, 'article page-propos page-ecrire', False)


def signature(module, a: dict) -> str:
    """La signature qui clôt un article de la communauté, comme une lettre."""
    ui = module.UI
    licence, _ = contributions.LICENCE
    orcid = (f' (<a href="https://orcid.org/{a["orcid"]}" rel="noopener">ORCID {a["orcid"]}</a>)' if a['orcid'] else '')
    historique, correction = ui['signature_liens']
    return ('<footer class="signature">'
            + typo(ui['signature'], module).format(auteur=html.escape(a['auteur']), orcid=orcid, date=date_longue(a['jour'], module),
                                                   licence=licence, adresse_licence=ui['adresse_licence'])
            + f'<p><a href="{contributions.DEPOT}/commits/main/contributions/{a["fichier"]}" rel="noopener">{historique}</a> · '
              f'<a href="{contributions.DEPOT}/edit/main/contributions/{a["fichier"]}" rel="noopener">{correction}</a> · '
              f'<a href="/ecrire/">{ui["ecrire_article"]}</a></p></footer>')


def contribution(a: dict) -> str:
    """Un article de la communauté, mis en page comme les autres, dans la langue où il est écrit.
    Il n'existe qu'à une adresse, à la racine ; le lien de langue mène au blog de l'autre édition."""
    module = MODULES[a['langue']]
    ui = module.UI
    corps, sommaire = sommaire_article(a['corps'], module)
    sommaire = sommaire or '<aside class="reperes-lecture"></aside>'
    rubrique = (f'<a href="{module.SUJETS[a["theme"]]["chemin"]}">{html.escape(module.SUJETS[a["theme"]]["titre"])}</a> · '
                if a['theme'] else '')
    contenu = f'''<main>
<header>
<h1>{titre_html(a['titre'])}</h1>
<p class="signe">{signe_par(module, a)}</p>
</header>
<div class="mise-en-lecture">{sommaire}<div class="corps-article">{corps}
{signature(module, a)}
<nav class="suite-article" aria-label="{ui['poursuivre']}">
<h2>{ui['lire_ensuite']}</h2>
<p>{rubrique}<a href="/recherches/#signes">{ui['signes_titre']}</a> · <a href="/ecrire/">{ui['ecrire_article']}</a> · <a href="/recherches/">{ui['tous_articles']}</a></p>
</nav>
</div></div>
</main>'''
    description = a['resume'] or ui['signe_defaut'].format(auteur=a['auteur'])
    # Page servie à la racine dans les deux cas : ses liens internes reçoivent le préfixe de sa langue, pas son adresse.
    html_page = page(module, a['chemin'], f'{a["titre"]} — ÆTERNAM', description, contenu, 'article lecture',
                     bool(contributions.FORMULE.search(a['corps'])),
                     f'<meta name="author" content="{html.escape(a["auteur"], quote=True)}">\n', autre_chemin='/recherches/')
    return html_page.replace(f'{DOMAINE}{module.PREFIXE}{a["chemin"]}', f'{DOMAINE}{a["chemin"]}')


def introuvable(module) -> str:
    ui = module.UI
    contenu = f'''<main>
<h1>ÆTERNAM</h1>
<p class="devise">{ui['introuvable']}</p>
<p class="actions"><a class="bouton" href="/">{ui['retour_accueil']} {FLECHE}</a></p>
</main>'''
    return page(module, '/', 'ÆTERNAM', ui['introuvable'], contenu, 'article introuvable', False, autre_chemin='/')


# ------------------------------------------------------------------ plan du site et anciennes adresses
def chemins_edition(module) -> tuple[str, ...]:
    return (('/', '/recherches/', '/sujets/', '/a-propos/', '/ecrire/')
            + tuple(s['chemin'] for s in module.SUJETS.values()) + tuple(e['chemin'] for e in ETUDES))


def plan_du_site(signes) -> str:
    adresses = [f'{DOMAINE}{module.PREFIXE}{chemin}' for module in MODULES.values() for chemin in chemins_edition(module)]
    adresses += [f'{DOMAINE}{a["chemin"]}' for a in signes]
    urls = ''.join(f'<url><loc>{adresse}</loc></url>\n' for adresse in adresses)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')


def redirections() -> str:
    """public/_redirects (Cloudflare Pages) : les anciens préfixes de langue (/fr/test-2/ -> /test-2/) en 301 ;
    la section CAP, retirée du site le 20/11/2026, renvoie à l'accueil."""
    statiques = [f'/{c} / 301' for c in ANCIENS_PREFIXES]
    dynamiques = [f'/{c}/* /:splat 301' for c in ANCIENS_PREFIXES]
    retirees = ['/cap / 302', '/cap/* / 302']
    return '\n'.join(statiques + dynamiques + retirees) + '\n'


# ------------------------------------------------------------------ la construction
def preparer(modules: dict) -> None:
    """Charge les résultats de chaque étude, une fois, et vérifie les textes de chaque langue :
    formules sûres, thème connu, chaque marqueur a sa valeur, la traduction garde la structure du français."""
    fr = modules['fr']
    for etude in ETUDES:
        if not etude['sujets'] or set(etude['sujets']) - fr.SUJETS.keys():
            raise SystemExit(f"{etude['chemin']} : classement par sujet absent ou inconnu")
        dossier = RACINE / 'recherche' / etude['dossier']
        etude['resultats'] = json.loads((dossier / 'resultats.json').read_text(encoding='utf-8'))
        etude['nombres'] = etude['table'](etude['resultats'])
    for code, module in modules.items():
        dangereuses = [f for e in ETUDES for f in formules_dangereuses(getattr(module, e['attribut'])['corps'])]
        if dangereuses:
            raise SystemExit(f'{code} : formules à écrire avec \\lt :\n' + '\n'.join(dangereuses))
        for etude in ETUDES:
            inconnus = set(MARQUEUR.findall(getattr(module, etude['attribut'])['corps'])) - set(etude['nombres'])
            inconnus = {m for m in inconnus if not m.startswith('figure_')}
            if inconnus:
                raise SystemExit(f"{code} {etude['chemin']} : marqueurs sans valeur : {sorted(inconnus)}")
        if module is fr:
            continue
        # Une traduction ne change ni les marqueurs, ni les balises, ni les formules (site/langues/verifier_traduction.py).
        if list(module.SUJETS) != list(fr.SUJETS):
            raise SystemExit(f'{code} : SUJETS doit avoir les mêmes thèmes que le français, dans le même ordre')
        erreurs = []
        for nom, valeur in vars(fr).items():
            if isinstance(valeur, dict) and 'corps' in valeur:
                if not hasattr(module, nom):
                    erreurs.append(f'{nom} : absent de {code}.py')
                else:
                    erreurs += verifier_traduction.comparer(nom, valeur, getattr(module, nom))
        for cle, s in fr.SUJETS.items():
            t = module.SUJETS[cle]
            if (s['chemin'], s['sources'], s['lien'], [l for l, _ in s['lectures']]) != (t['chemin'], t['sources'], t['lien'], [l for l, _ in t['lectures']]):
                erreurs.append(f'SUJETS[{cle}] : chemin, sources, lien et adresses des lectures doivent être ceux du français')
        if erreurs:
            raise SystemExit(f'Traduction {code} à corriger :\n' + '\n'.join(erreurs))


def ecrire_page(racine: Path, chemin: str, contenu: str) -> None:
    dossier = racine / chemin.strip('/')
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / 'index.html').write_text(contenu, encoding='utf-8')


def construire_edition(module, signes) -> None:
    """Toutes les pages d'une langue, sous public/ (français) ou public/en/ (anglais)."""
    visuels.LANGUE = module.HTML_LANG
    dessins.LIBELLES = module.UI['dessins']
    racine = PUBLIC / module.PREFIXE.strip('/')
    racine.mkdir(parents=True, exist_ok=True)
    ecrire_page(racine, '/', accueil(module, signes))
    for chemin, contenu in (('/recherches/', recherches(module, signes)), ('/sujets/', sujets(module)),
                            ('/a-propos/', a_propos(module)), ('/ecrire/', ecrire(module, signes))):
        ecrire_page(racine, chemin, contenu)
    for cle, s in module.SUJETS.items():
        ecrire_page(racine, s['chemin'], sujet(module, cle, signes))
    for etude in ETUDES:
        ecrire_page(racine, etude['chemin'], article(module, etude))
    (racine / '404.html').write_text(introuvable(module), encoding='utf-8')


def construire() -> None:
    MODULES.update({code: charger(code) for code in EDITIONS})
    preparer(MODULES)
    # Articles de la communauté (contributions/) : une erreur arrête tout, avec ce qu'il faut corriger.
    try:
        signes = contributions.lire(RACINE, MODULES['fr'].SUJETS, tuple(MODULES))
    except contributions.ErreurContribution as erreur:
        raise SystemExit(f'Article signé à corriger : {erreur}')
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    for nom in ('style.css', 'favicon.svg', 'base.js', 'lecture.js', 'ecrire.js'):
        shutil.copy(SITE / nom, PUBLIC / nom)
    shutil.copytree(SITE / 'polices', PUBLIC / 'polices')
    (PUBLIC / 'accueil').mkdir()
    for nom in ('accueil.css', 'accueil.js'):
        shutil.copy(SITE / 'accueil' / nom, PUBLIC / 'accueil' / nom)
    medias = RACINE / 'contributions' / 'medias'
    if medias.is_dir():  # seules les images autorisées sont publiées, jamais de SVG
        (PUBLIC / 'contributions' / 'medias').mkdir(parents=True)
        for fichier in medias.iterdir():
            if fichier.is_file() and fichier.suffix.lower() in contributions.IMAGES:
                shutil.copy(fichier, PUBLIC / 'contributions' / 'medias' / fichier.name)
    for etude in ETUDES:  # les fichiers de chaque étude, communs aux deux éditions
        cible = PUBLIC / 'fichiers' / etude['chemin'].strip('/')
        for nom in etude['fichiers']:
            (cible / nom).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RACINE / 'recherche' / etude['dossier'] / nom, cible / nom)
    for module in MODULES.values():
        construire_edition(module, signes)
    for a in signes:
        dessins.LIBELLES = MODULES[a['langue']].UI['dessins']
        ecrire_page(PUBLIC, a['chemin'], contribution(a))
    (PUBLIC / 'sitemap.xml').write_text(plan_du_site(signes), encoding='utf-8')
    (PUBLIC / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {DOMAINE}/sitemap.xml\n', encoding='utf-8')
    (PUBLIC / '_redirects').write_text(redirections(), encoding='utf-8')
    print(f'public/ construit : {len(MODULES)} langues ({", ".join(MODULES)}), {len(MODULES["fr"].SUJETS)} thèmes, '
          f'{len(ETUDES)} articles, {len(signes)} article(s) de la communauté')


if __name__ == '__main__':
    construire()
