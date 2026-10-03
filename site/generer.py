#!/usr/bin/env python3
"""Construit public/ : le site aeternam, en français, servi à la racine (www.aeternam.org/).

Les textes sont dans site/langues/fr.py ; les nombres viennent du resultats.json de
chaque étude (recherche/). Les anciennes adresses à préfixe de langue (/fr/, /en/…)
redirigent durablement vers la racine (public/_redirects).

Usage : python3 site/generer.py
"""
from __future__ import annotations

import html
import importlib.util
import json
import math
import re
import shutil
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import visuels  # noqa: E402  (site/visuels.py)
SITE = RACINE / 'site'
PUBLIC = RACINE / 'public'
DOMAINE = 'https://www.aeternam.org'
# Préfixes des anciennes adresses (site multilingue jusqu'au 28 septembre 2026) : redirigés vers la racine.
ANCIENS_PREFIXES = ('fr', 'en', 'es', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'ar')
KATEX = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/'

MARQUEUR = re.compile(r'\[\[([a-z0-9_]+)\]\]')
FORMULE = re.compile(r'\$\$.+?\$\$|\\\(.+?\\\)', re.S)
MOINS, FINE = '−', ' '


def charger(code: str):
    chemin = SITE / 'langues' / f'{code}.py'
    spec = importlib.util.spec_from_file_location(f'langue_{code}', chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ecrire_nombre(valeur: float, genre: str, precision: int, decimale: str) -> str:
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
        corps = f'{int(entier):,}'.replace(',', FINE).replace('-', MOINS)
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


def formules_dangereuses(texte: str) -> list[str]:
    """Formules où « < » suivi d'une lettre serait lu comme une balise HTML (écrire \\lt)."""
    return [f for f in FORMULE.findall(texte) if re.search(r'<[A-Za-z/!?]', f)]


def remplir(texte: str, nombres: dict, module, extras: dict) -> str:
    def un(m):
        nom = m.group(1)
        if nom in extras:
            return extras[nom]
        valeur, genre, precision = nombres[nom]
        return ecrire_nombre(valeur, genre, precision, module.DECIMALE)
    return MARQUEUR.sub(un, texte)


def pluie() -> str:
    """Fond de chaque page : une pluie des vrais bits quantiques du test n° 4."""
    bits = ''.join(str(b) for b in visuels._bits_fichier(visuels.HASARD / 'donnees' / 'parity_qrng.bin', 4096))
    return f'<canvas class="pluie" aria-hidden="true" data-bits="{bits}"></canvas>\n'


def page(module, chemin: str, titre: str, description: str, contenu: str,
         classe: str, maths: bool) -> str:
    katex = ''
    if maths:
        katex = (f'<link rel="stylesheet" href="{KATEX}katex.min.css" crossorigin="anonymous">\n'
                 f'<script defer src="{KATEX}katex.min.js" crossorigin="anonymous"></script>\n'
                 f'<script defer src="{KATEX}contrib/auto-render.min.js" crossorigin="anonymous" '
                 "onload=\"renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},"
                 "{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false})\"></script>\n")
    navigation = []
    for cible, libelle in (('/sujets/', 'Thèmes'), ('/recherches/', 'Articles'), ('/a-propos/', 'À propos')):
        courant = ' aria-current="page"' if chemin == cible else ''
        navigation.append(f'<a href="{cible}"{courant}>{libelle}</a>')
    barre = ('<div class="barre"><a class="marque" href="/">aeternam</a>'
             '<nav aria-label="Navigation principale">' + ''.join(navigation) + '</nav></div>\n')
    return f'''<!doctype html>
<html lang="{module.HTML_LANG}" dir="{module.DIR}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{DOMAINE}{chemin}">
<meta property="og:title" content="{html.escape(titre)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{DOMAINE}{chemin}">
<meta property="og:locale" content="{module.LOCALE_OG}">
<meta name="theme-color" content="#0a0a0c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{katex}</head>
<body class="{classe}">
{pluie()}{barre}{contenu}
{PLUIE_JS}
</body>
</html>
'''


PLUIE_JS = """<script>
(function () {
  var c = document.querySelector('.pluie');
  if (!c || !c.getContext) return;
  var bits = c.getAttribute('data-bits') || '01', ctx = c.getContext('2d'), curseur = 0, colonnes = [];
  var flou = document.createElement('canvas'), fctx = flou.getContext('2d'), R = 4;
  var st = getComputedStyle(document.documentElement);
  var tete = st.getPropertyValue('--accent').trim() || '#d2c29a', traine = st.getPropertyValue('--muted').trim() || '#9a9486';
  var calme = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var blocs = document.querySelectorAll('.hero h1, .hero p, main h2, main h3, main p, main li, main figure, main .travail, main table, main .katex-display, main header h1, .barre');
  var FORCE = 0.3;  // visibilité d'ensemble : on doit à peine deviner la pluie
  var d = 1, pas = 18, dernier = 0, zones = [];
  function bit() { var b = bits.charAt(curseur); curseur = (curseur + 1) % bits.length; return b; }
  function taille() {
    d = Math.min(window.devicePixelRatio || 1, 2);
    c.width = Math.round(window.innerWidth * d); c.height = Math.round(window.innerHeight * d);
    flou.width = Math.ceil(c.width / R); flou.height = Math.ceil(c.height / R);
    pas = Math.max(14, Math.min(20, Math.round(window.innerWidth / 70))) * d;
    var n = Math.ceil(c.width / pas); colonnes = [];
    for (var i = 0; i < n; i++) {
      var col = { y: Math.random() * c.height * 1.3, v: (0.5 + Math.random() * 0.8) * pas * 0.3,
        long: 12 + Math.floor(Math.random() * 20), glyphes: [] };
      col.rang = Math.floor(col.y / pas);
      for (var k = 0; k < col.long; k++) col.glyphes.push(bit());
      colonnes.push(col);
    }
  }
  function mesurer() {
    zones = [];
    for (var i = 0; i < blocs.length; i++) {
      var r = blocs[i].getBoundingClientRect();
      if (r.bottom < -40 || r.top > window.innerHeight + 40 || r.width === 0) continue;
      zones.push([(r.left - 18) * d, (r.top - 14) * d, (r.right + 18) * d, (r.bottom + 14) * d]);
    }
  }
  function dansTexte(x, y) {
    for (var i = 0; i < zones.length; i++) { var z = zones[i]; if (x > z[0] && x < z[2] && y > z[1] && y < z[3]) return true; }
    return false;
  }
  function dessin() {
    mesurer();
    ctx.clearRect(0, 0, c.width, c.height); fctx.clearRect(0, 0, flou.width, flou.height);
    ctx.font = Math.round(pas * 0.8) + 'px ui-monospace, Menlo, monospace'; ctx.textAlign = 'center';
    fctx.font = Math.round(pas * 0.8 / R) + 'px ui-monospace, Menlo, monospace'; fctx.textAlign = 'center';
    colonnes.forEach(function (col, i) {
      var x = (i + 0.5) * pas;
      col.y += col.v;
      var rang = Math.floor(col.y / pas);
      if (rang !== col.rang) { col.rang = rang; col.glyphes.unshift(bit()); if (col.glyphes.length > col.long) col.glyphes.pop(); }
      if ((rang - col.long) * pas > c.height) { col.y = -Math.random() * c.height * 0.4; col.glyphes = []; col.rang = null; }
      col.glyphes.forEach(function (g, k) {
        var y = (rang - k) * pas; if (y < 0 || y > c.height + pas) return;
        var a = FORCE * (k === 0 ? 0.6 : 0.38 * (1 - k / col.long)), couleur = k === 0 ? tete : traine;
        if (dansTexte(x, y)) { fctx.globalAlpha = a * 0.55; fctx.fillStyle = couleur; fctx.fillText(g, x / R, y / R); }
        else { ctx.globalAlpha = a; ctx.fillStyle = couleur; ctx.fillText(g, x, y); }
      });
    });
    ctx.globalAlpha = 1; ctx.imageSmoothingEnabled = true; ctx.drawImage(flou, 0, 0, c.width, c.height);
  }
  function boucle(t) {
    if (document.hidden) { requestAnimationFrame(boucle); return; }
    if (t - dernier > 45) { dernier = t; dessin(); }
    requestAnimationFrame(boucle);
  }
  taille();
  window.addEventListener('resize', function () { taille(); if (calme) dessin(); });
  if (calme) { for (var k = 0; k < 60; k++) dessin(); window.addEventListener('scroll', dessin, { passive: true }); return; }
  requestAnimationFrame(boucle);
})();
</script>"""


def etudes_par_date():
    return sorted(ETUDES, key=lambda e: e.get('publication', e['dossier'][:10]), reverse=True)


def liens_sujets(module, cles):
    return ' · '.join(f'<a href="{module.SUJETS[cle]["chemin"]}">{html.escape(module.SUJETS[cle]["titre"])}</a>'
                      for cle in cles)


def liste_etudes(module, etudes, niveau=3, compact=False, afficher_sujets=True):
    elements = []
    for etude in etudes:
        a = getattr(module, etude['attribut'])
        description = '' if compact else f'<p>{html.escape(a["description"])}</p>'
        rubriques = (f'<p class="sujets-article">{liens_sujets(module, etude["sujets"])}</p>'
                     if afficher_sujets else '')
        elements.append(f'''<li class="entree-article">
<h{niveau}><a href="{etude['chemin']}">{html.escape(a['titre'])}</a></h{niveau}>
{description}{rubriques}
</li>''')
    classe = 'liste-articles articles-compacts' if compact else 'liste-articles'
    return f'<ul class="{classe}">\n' + '\n'.join(elements) + '\n</ul>'


def liste_sujets(module, niveau=3):
    return '<ul class="liste-sujets">' + '\n'.join(
        f'<li><h{niveau}><a href="{s["chemin"]}">{html.escape(s["titre"])}</a></h{niveau}>'
        f'<p>{html.escape(s["description"])}</p></li>' for s in module.SUJETS.values()) + '</ul>'


def sommaire_themes(module):
    liens = ' · '.join(f'<a href="#{cle}">{html.escape(s["titre"])}</a>'
                       for cle, s in module.SUJETS.items())
    return f'<nav id="sujets" class="index-sujets" aria-label="Aller à un thème">{liens}</nav>'


def articles_par_theme(module, compact=False):
    sections = []
    for cle, s in module.SUJETS.items():
        etudes = [e for e in etudes_par_date() if cle in e['sujets']]
        sections.append(f'''<section id="{cle}" class="theme-recherche">
<h2><a href="{s['chemin']}">{html.escape(s['titre'])}</a></h2>
<p class="description-theme">{html.escape(s['description'])}</p>
{liste_etudes(module, etudes, compact=compact, afficher_sujets=False)}
</section>''')
    return '\n'.join(sections)


def recherches(module):
    contenu = f'''<main><header><h1>Les articles par thème</h1></header>
<p>Lectures critiques, réanalyses et questions ouvertes, regroupées par thème. Les articles qui relient plusieurs thèmes apparaissent dans chacune des rubriques concernées.</p>
{sommaire_themes(module)}
{articles_par_theme(module)}
<p id="aeternam">Pour approfondir les questions de chaque rubrique, explorez les <a href="/sujets/">thèmes du blog</a>.</p>
</main>'''
    return page(module, '/recherches/', 'Les articles par thème — aeternam',
                'Les articles d’Aeternam classés par thème : BCI, vision, mémoire, rêve, temps vécu et théorie de la simulation.', contenu, 'article index-blog', False)


def sujets(module):
    contenu = f'''<main><header><h1>Les thèmes de recherche</h1></header>
<p>Cinq thèmes pour explorer le cerveau, l’expérience vécue et la nature du réel. Un article peut relier plusieurs thèmes.</p>
{liste_sujets(module, niveau=2)}
</main>'''
    return page(module, '/sujets/', 'Les thèmes de recherche — aeternam', module.UI['description_site'], contenu, 'article index-blog', False)


def sujet(module, cle):
    s = module.SUJETS[cle]
    questions = ''.join(f'<li>{html.escape(q)}</li>' for q in s['questions'])
    lectures = ''.join(f'<li><a href="{lien}">{html.escape(titre)}</a></li>' for lien, titre in s['lectures'])
    etudes = [e for e in etudes_par_date() if cle in e['sujets']]
    contenu = f'''<main><header><h1>{html.escape(s['titre'])}</h1></header>
{s['intro']}
<section><h2>Les questions</h2><ul>{questions}</ul></section>
<section><h2>Par où commencer</h2><ul class="lectures">{lectures}</ul></section>
<section><h2>Les articles de ce thème</h2>{liste_etudes(module, etudes)}</section>
<p class="retour-sujets"><a href="/sujets/">Tous les thèmes</a> · <a href="/recherches/">Tous les articles</a></p>
</main>'''
    return page(module, s['chemin'], f"{s['titre']} — aeternam", s['description'], contenu, 'article index-blog', False)


def a_propos(module):
    a = module.A_PROPOS
    contenu = f'<main><header><h1>{a["titre"]}</h1></header>{a["corps"]}</main>'
    return page(module, '/a-propos/', f'{a["titre"]} — aeternam', a['description'], contenu, 'article', False)


def accueil(module) -> str:
    a = module.ACCUEIL
    contenu = f'''<main>
<header class="hero-blog"><h1>aeternam</h1></header>
<p class="intro-blog">{a['intro']}</p>
{sommaire_themes(module)}
<div id="travaux">{articles_par_theme(module, compact=True)}</div>
<p><a href="/recherches/">Les articles par thème, en détail</a></p>
<p class="methode-blog">{a['methode']} <a href="/a-propos/">À propos du blog</a>.</p>
</main>'''
    return page(module, '/', a['titre'], module.UI['description_site'], contenu, 'article blog', False)


def article(module, etude: dict, nombres: dict) -> str:
    a, ui = getattr(module, etude['attribut']), module.UI
    extras = {'pdf': ui['fichier_pdf']}
    if 'figures' in etude:
        extras.update(etude['figures'](etude['resultats'], lambda s: remplir(s, nombres, module, {})))
    corps = remplir(a['corps'], nombres, module, extras)
    contenu = f'''<main>
<header>
<h1>{a['titre']}</h1>
</header>
{corps}
<nav class="suite-article" aria-label="Poursuivre la lecture">
<h2>Explorer ces thèmes</h2>
<p>{liens_sujets(module, etude['sujets'])}</p>
<p><a href="/recherches/">Tous les articles</a></p>
</nav>
</main>'''
    return page(module, etude['chemin'], f"{a['titre']} — aeternam", a['description'], contenu,
                'article', True)


def introuvable(module) -> str:
    contenu = f'''<main>
<h1>aeternam</h1>
<p class="devise">{module.UI['introuvable']}</p>
<p class="verdict"><a href="/">aeternam.org</a></p>
</main>'''
    return page(module, '/', 'aeternam', module.UI['introuvable'], contenu, 'accueil', False)


def plan_du_site(module) -> str:
    chemins = ('/', '/recherches/', '/sujets/', '/a-propos/')
    chemins += tuple(s['chemin'] for s in module.SUJETS.values()) + tuple(e['chemin'] for e in ETUDES)
    urls = ''.join(f'<url><loc>{DOMAINE}{chemin}</loc></url>\n' for chemin in chemins)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')


def redirections() -> str:
    """public/_redirects (Cloudflare Pages) : /fr/test-2/ -> /test-2/, /en/ -> /, etc., en 301."""
    statiques = [f'/{c} / 301' for c in ANCIENS_PREFIXES]
    dynamiques = [f'/{c}/* /:splat 301' for c in ANCIENS_PREFIXES]
    return '\n'.join(statiques + dynamiques) + '\n'


def construire(module) -> None:
    dangereuses = [f for e in ETUDES for f in formules_dangereuses(getattr(module, e['attribut'])['corps'])]
    if dangereuses:
        raise SystemExit('formules à écrire avec \\lt :\n' + '\n'.join(dangereuses))
    for etude in ETUDES:
        if not etude['sujets'] or set(etude['sujets']) - module.SUJETS.keys():
            raise SystemExit(f"{etude['chemin']} : classement par sujet absent ou inconnu")
        dossier = RACINE / 'recherche' / etude['dossier']
        etude['resultats'] = json.loads((dossier / 'resultats.json').read_text(encoding='utf-8'))
        etude['nombres'] = etude['table'](etude['resultats'])
        inconnus = set(MARQUEUR.findall(getattr(module, etude['attribut'])['corps'])) - set(etude['nombres']) - {'pdf'}
        inconnus = {m for m in inconnus if not m.startswith('figure_')}
        if inconnus:
            raise SystemExit(f"{etude['chemin']} : marqueurs sans valeur : {sorted(inconnus)}")
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    for nom in ('style.css', 'favicon.svg'):
        shutil.copy(SITE / nom, PUBLIC / nom)
    for etude in ETUDES:
        cible = PUBLIC / 'fichiers' / etude['chemin'].strip('/')
        for nom in etude['fichiers']:
            (cible / nom).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RACINE / 'recherche' / etude['dossier'] / nom, cible / nom)
    (PUBLIC / 'index.html').write_text(accueil(module), encoding='utf-8')
    for chemin, contenu in (('/recherches/', recherches(module)), ('/sujets/', sujets(module)),
                            ('/a-propos/', a_propos(module))):
        dossier = PUBLIC / chemin.strip('/')
        dossier.mkdir(parents=True)
        (dossier / 'index.html').write_text(contenu, encoding='utf-8')
    for cle, s in module.SUJETS.items():
        dossier = PUBLIC / s['chemin'].strip('/')
        dossier.mkdir(parents=True)
        (dossier / 'index.html').write_text(sujet(module, cle), encoding='utf-8')
    (PUBLIC / '404.html').write_text(introuvable(module), encoding='utf-8')
    for etude in ETUDES:
        dossier = PUBLIC / etude['chemin'].strip('/')
        dossier.mkdir()
        (dossier / 'index.html').write_text(article(module, etude, etude['nombres']), encoding='utf-8')
    (PUBLIC / 'sitemap.xml').write_text(plan_du_site(module), encoding='utf-8')
    (PUBLIC / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {DOMAINE}/sitemap.xml\n', encoding='utf-8')
    (PUBLIC / '_redirects').write_text(redirections(), encoding='utf-8')
    print(f'public/ construit : blog, {len(module.SUJETS)} sujets et {len(ETUDES)} articles')


if __name__ == '__main__':
    construire(charger('fr'))
