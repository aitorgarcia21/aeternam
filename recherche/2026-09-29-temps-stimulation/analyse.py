#!/usr/bin/env python3
"""aeternam : une intervention fait-elle vivre plus de temps que le temps écoulé ?

Question (projet « Une vie en une nuit ») : existe-t-il une preuve publiée
qu'une intervention (stimulation électrique, magnétique, sensorielle ou
acoustique, drogues, hypnose, réalité virtuelle, peur, rejeu ciblé pendant le
sommeil) fasse vivre subjectivement plus de temps que le temps réellement
écoulé, et de combien au maximum ?

Deux grandeurs, à ne pas confondre :
  (a) facteur de DURÉE ESTIMÉE : durée que la personne dit (ou reproduit) avoir
      vécue / durée réelle mesurée à l'horloge (ou / durée estimée par un groupe
      témoin). C'est un jugement, souvent rétrospectif (souvenir).
  (b) facteur de VÉCU PAR SECONDE : quantité d'expérience réellement traitée
      par seconde, vérifiée de l'extérieur (résolution temporelle, information
      extraite, apprentissage, calcul juste), sous intervention / sans. C'est ce
      qu'exige le projet : vivre plus, pas seulement croire après coup avoir
      vécu plus longtemps.

Toutes les valeurs viennent de VALEURS_PUBLIEES (source et passage exacts dans
sources.md) ; ce script ne fait que les recalculer, les classer et les borner.

RÈGLE DE DÉCISION (écrite avant la première exécution ; les ordres de grandeur
publiés étaient connus en l'écrivant, pas les bornes calculées) :
  OUI (accélération du vécu démontrée) si au moins une étude CONTRÔLÉE (groupe
      ou condition témoin, contenu vérifié de l'extérieur) donne un facteur (b)
      dont la borne inférieure à 95 % dépasse 2 (au moins un doublement) ;
  NON sinon ; on publie alors X_b, la plus grande borne supérieure à 95 %
      (à défaut, la plus grande valeur ponctuelle) des facteurs (b) contrôlés,
      et l'écart au facteur nécessaire 87 660 = 80 ans / 8 h.
Un facteur (a), même grand, ne suffit jamais pour OUI : il ne dit pas que plus
de choses ont été vécues, seulement qu'on juge la durée plus longue.

Python >= 3.10, bibliothèque standard. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

CONFIANCE = 0.95
SEUIL_OUI_FACTEUR_B = 2.0
FACTEUR_NECESSAIRE = 80 * 365.25 * 24 / 8  # une vie de 80 ans en une nuit de 8 h

# =========================================================================== valeurs publiées
VALEURS_PUBLIEES = {
    'stetson_2007': {
        'duree_imaginee_autrui_s': 2.17, 'pm_autrui_s': 0.24,
        'duree_rappelee_propre_chute_s': 2.96, 'pm_propre_s': 0.51,
        'duree_reelle_chute_s': 2.49, 'n_estimations': 7, 'p_unilateral_max': 0.03,
        'dilatation_publiee_pct': 36,
        'precision_predite_si_resolution_plus_36pct': 0.79,
        'p_vol_contre_prediction_max': 2e-6, 'p_vol_contre_temoin_texte': 0.98,
        'p_vol_contre_temoin_legende': 0.86,
        'source': 'Stetson, Fiesta & Eagleman, PLoS ONE 2(12), e1295 (2007), doi:10.1371/journal.pone.0001295, '
                  'PMC2110887 : « participants\' duration estimates increased by an average of 36% when they '
                  'recalled their own fall (from 2.17±0.24 s to 2.96±0.51 s, p<0.03, paired t-test, one-tailed) » ; '
                  '« The actual duration of the fall was 2.49 sec » ; « 7 participants made duration judgments » ; '
                  '« a 79% accuracy in digit identification during the fall would be predicted » ; « participants\' '
                  'accuracy in-flight was significantly less than expected [...] (p<2×10−6). In-flight performance '
                  'was no better than ground-based controls ». Le sens de « ± » n\'est pas précisé.'},
    'pariyadath_eagleman_2007': {
        'dilatation_oddball_mesuree_pct': 12, 'dilatation_oddball_max_publiee_pct': 50,
        'source': 'Pariyadath & Eagleman, PLoS ONE 2(11), e1264 (2007), doi:10.1371/journal.pone.0001264, '
                  'PMC2082074 : « The relative duration distortion averaged 12% » ; « the judged duration of the '
                  'oddball is overestimated by up to 50% [11], [12] » (réf. 11 : Tse et al. 2004) ; « neither the '
                  'pitch of the sound nor the frequency of the flicker is affected by the apparent duration dilation ».'},
    'jones_allely_wearden_2011': {
        'gain_lettres_300ms_pct': 3.25, 'gain_lettres_500ms_pct': 5.85,
        'F_effet_clics': 4.59, 'ddl_erreur': 19,
        'dilatation_subjective_clics_pct': 10,
        'source': 'Jones, Allely & Wearden, Q. J. Exp. Psychol. 64(2), 363-380 (2011), '
                  'doi:10.1080/17470218.2010.502580 (PDF de l\'université de Manchester, version publiée) : '
                  '« These increases were 3.25% in the 300-ms condition and of 5.85% in the 500-ms condition » ; '
                  '« There was a significant effect of clicks, F(1, 19) = 4.59, p < .05 » ; « Penton-Voak et al. '
                  '(1996) found that the click trains could increase the pacemaker speed by an average of 10% ».'},
    'cooper_erickson_1954': {
        # tableau 4, tâche 7 : durée suggérée 10 min, temps alloué 1 s, 402 pièces comptées, durée vécue 10 min
        'tab4_tache7': {'duree_vecue_s': 600.0, 'temps_alloue_s': 1.0, 'compte': 402, 'rythme_par_min': 66},
        # tableau 3, sujet F : temps alloué 10 s, durée vécue 60 min, compte 2 500, rythme 72/min
        'tab3_sujet_F': {'duree_vecue_s': 3600.0, 'temps_alloue_s': 10.0, 'compte': 2500, 'rythme_par_min': 72},
        # chapitre 8 : « seeming duration is 30 to 60 minutes, in an allotted time (A.T.) of three seconds »
        'ch8_affirmation': {'duree_vecue_s': 3600.0, 'temps_alloue_s': 3.0},
        # chapitre 9, expérience 1 : 3 s, 10 min vécues, 114 coups comptés, rythme démontré 60/min
        'ch9_exp1': {'duree_vecue_s': 600.0, 'temps_alloue_s': 3.0, 'compte': 114, 'rythme_par_min': 60},
        # chapitre 19 (un sujet, sans témoin) : temps d'étude par paire hors présentation, éveil / transe
        'ch19_temps_par_paire_eveil_s': 31.5, 'ch19_temps_par_paire_transe_s': 7.7,
        'ch19_retention_pct_eveil': 19, 'ch19_retention_pct_transe': 19,
        # chapitre 18 : amélioration des témoins
        'ch18_amelioration_temoins_pct': [11, 15, 114, 108, 84],
        'source': 'Cooper & Erickson, Time Distortion in Hypnosis, Baltimore, Williams & Wilkins (1954), texte '
                  'intégral (archive.org). Ch. 20 : « Where a short allotted time was used, the performance, in '
                  'terms of correct answers, was no better than chance would give, even though the suggested '
                  'personal time was usually accepted in full ». Ch. 18 : « There is no evidence, in the results of '
                  'these experiments, that the learning process itself is facilitated by such practice ».'},
    'krauss_1974_selon_johnson_1976': {
        'temps_etude_reel_min': 3, 'temps_etude_suggere_min': 10,
        'source': 'Johnson, Am. J. Clin. Hypn. 19(2), 98-102 (1976), doi:10.1080/00029157.1976.10403846, résumé : '
                  '« Krauss, Katzell, and Krauss (1974) reported that free-recall learning can be markedly enhanced '
                  'by suggestions given under hypnosis that three minutes of study time is equivalent to 10 minutes '
                  '[...]. The present investigation [...] did not yield similar results. Subjects learned a comparable '
                  'number of words for a comparable amount of study time ».'},
    'campagnoli_2020_ayahuasca': {
        'stimulus_s': 20.0, 'reproduit_sans_ayahuasca_s': [16.33, 16.52],
        'reproduit_ayahuasca_controle_s': 17.91, 'reproduit_ayahuasca_experimentale_s': 18.38, 'n': 9,
        'source': 'Campagnoli, Pereira & Bueno, Braz. J. Med. Biol. Res. 53(8), e9278 (2020), '
                  'doi:10.1590/1414-431X20209278, PMC7307892 : « means of 16.33 to 16.52 s [...] a mean of 17.91 s '
                  'for control ayahuasca and of 18.38 s for experimental ayahuasca » (stimuli de 20 s).'},
    'mullen_davidenko_2021_rv': {
        'secondes_de_plus_en_rv': 72.6, 'temps_reel_en_plus_pct': 28.5, 'intervalle_percu_s': 300.0,
        'source': 'Mullen & Davidenko, Timing & Time Perception 9(4), 377-392 (2021), '
                  'doi:10.1163/22134468-bja10034, résumé : « participants in the VR condition played for an average '
                  'of 72.6 more seconds than participants in the CM condition before feeling that five minutes had '
                  'passed. This amounts to perceived five-minute intervals in VR containing 28.5% more actual time ».'},
    'temps_reve_aeternam': {
        'F_global': 0.84, 'X_borne_sup_95': 0.92,
        'source': 'aeternam, recherche/2026-09-29-temps-reve/resultats.json, verdict.F_global et '
                  'verdict.X_borne_sup_95 (arrondis).'},
}

# études lues sans facteur chiffré dans le texte : sens seulement
SENS_SEULEMENT = {
    'wittmann_2007_psilocybine': {'mesure': 'a', 'sens': 'sous-reproduction des intervalles > 2,5 s',
                                  'statut': 'résumé lu'},
    'yanakieva_2019_lsd_microdose': {'mesure': 'a', 'sens': 'sur-reproduction des intervalles de 2 à 4 s, '
                                     'amplitude en figure seulement', 'statut': 'texte intégral lu'},
    'coull_2011_ketamine': {'mesure': 'a', 'sens': 'jugements de durée moins précis, surestimation plus '
                            'fréquente des sondes courtes ; aucun facteur', 'statut': 'texte intégral lu'},
    'cancer_2025_tdcs_ams': {'mesure': 'a', 'sens': 'interaction montage × style de montage ; aucun facteur '
                             'dans le texte', 'statut': 'texte intégral lu'},
    'martin_2016_hypnose': {'mesure': 'a', 'sens': 'distorsion hypnotique conforme à un effet de demande, '
                            'pas à une horloge ralentie', 'statut': 'texte intégral lu'},
    'rudoy_2009_tmr': {'mesure': 'aucune', 'sens': 'mémoire spatiale seulement', 'statut': 'résumé lu'},
    'antony_2012_tmr': {'mesure': 'aucune', 'sens': 'apprentissage moteur seulement', 'statut': 'résumé lu'},
    'ngo_2013_boucle_fermee': {'mesure': 'aucune', 'sens': 'oscillations lentes et mémoire seulement',
                               'statut': 'résumé lu'},
}


# =========================================================================== outils statistiques
def betacf(a: float, b: float, x: float) -> float:
    """Fraction continue de la bêta incomplète (Lentz)."""
    petit = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > petit else petit)
    h = d
    for m in range(1, 500):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > petit else petit)
        c = 1.0 + aa / c
        c = c if abs(c) > petit else petit
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > petit else petit)
        c = 1.0 + aa / c
        c = c if abs(c) > petit else petit
        de = d * c
        h *= de
        if abs(de - 1.0) < 1e-15:
            break
    return h


def betainc(a: float, b: float, x: float) -> float:
    """Bêta incomplète régularisée I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log1p(-x)
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbt) * betacf(a, b, x) / a
    return 1.0 - math.exp(lbt) * betacf(b, a, 1.0 - x) / b


def t_cdf(t: float, nu: float) -> float:
    x = nu / (nu + t * t)
    queue = 0.5 * betainc(nu / 2.0, 0.5, x)
    return 1.0 - queue if t >= 0 else queue


def t_ppf(p: float, nu: float) -> float:
    lo, hi = -1e3, 1e3
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, nu) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# =========================================================================== (a) durée estimée
def analyse_stetson() -> dict:
    v = VALEURS_PUBLIEES['stetson_2007']
    n = v['n_estimations']
    t95 = t_ppf(CONFIANCE, n - 1)
    propre, autrui, reel = v['duree_rappelee_propre_chute_s'], v['duree_imaginee_autrui_s'], v['duree_reelle_chute_s']
    # contre la durée réelle : « ± » lu comme erreur type (lecture prudente, intervalle le plus large)
    sup_reel_se = (propre + t95 * v['pm_propre_s']) / reel
    # lecture « écart type » : erreur type = ± / √n
    sup_reel_sd = (propre + t95 * v['pm_propre_s'] / math.sqrt(n)) / reel
    # contre autrui : erreur type de la différence appariée bornée par p < 0,03 unilatéral (t > t_0,97)
    diff = propre - autrui
    se_diff_max = diff / t_ppf(1.0 - v['p_unilateral_max'], n - 1)
    sup_autrui = (autrui + diff + t95 * se_diff_max) / autrui
    return {
        'mesure': 'a (rétrospective, souvenir d\'une chute de 31 m)',
        'facteur_contre_reel': propre / reel,
        'facteur_contre_reel_borne_sup_95_prudente': sup_reel_se,
        'facteur_contre_reel_borne_sup_95_si_ecart_type': sup_reel_sd,
        'facteur_contre_autrui': propre / autrui,
        'facteur_contre_autrui_borne_sup_95': sup_autrui,
        'facteur_imagine_autrui_contre_reel': autrui / reel,
        'dilatation_contre_autrui_pct': 100.0 * (propre / autrui - 1.0),
    }


def analyse_hypnose_recits() -> dict:
    v = VALEURS_PUBLIEES['cooper_erickson_1954']
    out = {}
    for k in ('tab4_tache7', 'tab3_sujet_F', 'ch8_affirmation', 'ch9_exp1'):
        d = v[k]
        e = {'facteur_duree_declaree': d['duree_vecue_s'] / d['temps_alloue_s']}
        if 'compte' in d:
            # durée qu'aurait prise le compte déclaré au rythme démontré à l'éveil
            duree_compte_s = 60.0 * d['compte'] / d['rythme_par_min']
            e['facteur_contenu_declare'] = duree_compte_s / d['temps_alloue_s']
            e['contenu_declare_sur_duree_declaree'] = duree_compte_s / d['duree_vecue_s']
        out[k] = e
    out['facteur_duree_declaree_max'] = max(out[k]['facteur_duree_declaree']
                                            for k in ('tab4_tache7', 'tab3_sujet_F', 'ch8_affirmation', 'ch9_exp1'))
    out['mesure'] = 'a (récit après coup, invérifiable : compte hallucinatoire déclaré)'
    return out


# =========================================================================== (b) vécu par seconde
def analyse_jones() -> dict:
    v = VALEURS_PUBLIEES['jones_allely_wearden_2011']
    g300, g500 = v['gain_lettres_300ms_pct'], v['gain_lettres_500ms_pct']
    # effet principal ≈ moyenne des deux gains relatifs (pas d'interaction : F = 0,51)
    g = 0.5 * (g300 + g500)
    t = math.sqrt(v['F_effet_clics'])
    se = g / t
    t_bi = t_ppf(0.975, v['ddl_erreur'])
    return {
        'mesure': 'b (lettres correctement rapportées, mémoire iconique de Sperling)',
        'facteur_300ms': 1.0 + g300 / 100.0,
        'facteur_500ms': 1.0 + g500 / 100.0,
        'facteur_moyen_approx': 1.0 + g / 100.0,
        'facteur_borne_inf_95_approx': 1.0 + (g - t_bi * se) / 100.0,
        'facteur_borne_sup_95_approx': 1.0 + (g + t_bi * se) / 100.0,
        'dilatation_subjective_associee': 1.0 + v['dilatation_subjective_clics_pct'] / 100.0,
        'note': 'intervalle approché : effet principal pris comme moyenne des deux gains relatifs publiés, '
                'erreur type tirée de F(1, 19) = 4,59 ; ddl 19',
    }


def analyse_hypnose_controles() -> dict:
    v = VALEURS_PUBLIEES['cooper_erickson_1954']
    k = VALEURS_PUBLIEES['krauss_1974_selon_johnson_1976']
    return {
        'cooper_ch19_un_sujet_sans_temoin_rapport_temps_etude': v['ch19_temps_par_paire_eveil_s'] / v['ch19_temps_par_paire_transe_s'],
        'cooper_ch19_retention_identique': v['ch19_retention_pct_eveil'] == v['ch19_retention_pct_transe'],
        'cooper_ch20_calcul_temps_court': 'pas mieux que le hasard (facteur b vérifié : aucun gain)',
        'cooper_ch18_amelioration_temoins_min_pct': min(v['ch18_amelioration_temoins_pct']),
        'cooper_ch18_amelioration_temoins_max_pct': max(v['ch18_amelioration_temoins_pct']),
        'krauss_1974_rapport_suggere': k['temps_etude_suggere_min'] / k['temps_etude_reel_min'],
        'krauss_1974_reproduit': False,
    }


# =========================================================================== autres (a)
def autres_a() -> dict:
    a = VALEURS_PUBLIEES['campagnoli_2020_ayahuasca']
    m = VALEURS_PUBLIEES['mullen_davidenko_2021_rv']
    p = VALEURS_PUBLIEES['pariyadath_eagleman_2007']
    cm = m['secondes_de_plus_en_rv'] / (m['temps_reel_en_plus_pct'] / 100.0)  # temps réel produit sur écran
    return {
        'ayahuasca_experimentale_reproduit_sur_reel': a['reproduit_ayahuasca_experimentale_s'] / a['stimulus_s'],
        'ayahuasca_controle_reproduit_sur_reel': a['reproduit_ayahuasca_controle_s'] / a['stimulus_s'],
        'sans_ayahuasca_reproduit_sur_reel_max': max(a['reproduit_sans_ayahuasca_s']) / a['stimulus_s'],
        'rv_temps_reel_ecran_s': cm,
        'rv_temps_reel_casque_s': cm + m['secondes_de_plus_en_rv'],
        'rv_facteur_percu_casque_sur_ecran': cm / (cm + m['secondes_de_plus_en_rv']),
        'oddball_facteur_mesure_pariyadath': 1.0 + p['dilatation_oddball_mesuree_pct'] / 100.0,
        'oddball_facteur_max_publie': 1.0 + p['dilatation_oddball_max_publiee_pct'] / 100.0,
        'clics_facteur_duree': 1.0 + VALEURS_PUBLIEES['jones_allely_wearden_2011']['dilatation_subjective_clics_pct'] / 100.0,
    }


# =========================================================================== autotests
def autotests() -> dict:
    r = {}
    r['t_cauchy'] = abs(t_ppf(0.95, 1) - math.tan(0.45 * math.pi)) < 1e-6
    r['t_6ddl'] = abs(t_ppf(0.95, 6) - 1.943180) < 1e-5  # table de Student
    r['t_19ddl'] = abs(t_ppf(0.975, 19) - 2.093024) < 1e-5
    s = VALEURS_PUBLIEES['stetson_2007']
    # le « 36 % » publié se retrouve à partir des moyennes
    r['stetson_36pct'] = round(100 * (s['duree_rappelee_propre_chute_s'] / s['duree_imaginee_autrui_s'] - 1)) == 36
    # Cooper : 10 min en 1 s = 600 ; 60 min en 3 s = 1 200
    r['cooper_600'] = VALEURS_PUBLIEES['cooper_erickson_1954']['tab4_tache7']['duree_vecue_s'] == 600.0
    r['cooper_1200'] = abs(3600.0 / 3.0 - 1200.0) < 1e-12
    # Mullen : 72,6 s = 28,5 % du temps écran, à l'arrondi près
    m = VALEURS_PUBLIEES['mullen_davidenko_2021_rv']
    cm = m['secondes_de_plus_en_rv'] / (m['temps_reel_en_plus_pct'] / 100.0)
    r['mullen_coherent'] = 200.0 < cm < 300.0
    # facteur nécessaire identique à l'étude précédente
    r['facteur_necessaire'] = FACTEUR_NECESSAIRE == 87660.0
    # la règle de décision répond OUI à un facteur (b) contrôlé fictif de borne inf. 3
    r['regle_detecte_oui'] = decider([{'nom': 'fictif', 'controle': True, 'inf': 3.0, 'sup': 4.0, 'valeur': 3.5}])['verdict'] == 'oui'
    r['regle_ignore_non_controle'] = decider([{'nom': 'fictif', 'controle': False, 'inf': 3.0, 'sup': 4.0, 'valeur': 3.5}])['verdict'] == 'non'
    r['tous_passes'] = all(r.values())
    if not r['tous_passes']:
        raise SystemExit(f'autotests en échec : {r}')
    return r


def decider(facteurs_b: list[dict]) -> dict:
    controles = [f for f in facteurs_b if f['controle']]
    oui = [f['nom'] for f in controles if f['inf'] is not None and f['inf'] > SEUIL_OUI_FACTEUR_B]
    bornes = [f['sup'] if f['sup'] is not None else f['valeur'] for f in controles]
    X = max(bornes) if bornes else None
    return {'verdict': 'oui' if oui else 'non', 'etudes_oui': oui, 'X_b': X}


# =========================================================================== principal
def principal() -> dict:
    res = {'question': 'Une intervention fait-elle vivre plus de temps que le temps écoulé ? '
                       '(a) durée estimée / réelle ; (b) vécu vérifié par seconde, sous intervention / sans',
           'regle': {'oui': f'un facteur (b) contrôlé de borne inf. 95 % > {SEUIL_OUI_FACTEUR_B}',
                     'non': 'sinon ; X_b = plus grande borne sup. 95 % des facteurs (b) contrôlés'},
           'autotests': autotests()}
    res['stetson'] = analyse_stetson()
    res['hypnose_recits'] = analyse_hypnose_recits()
    res['jones'] = analyse_jones()
    res['hypnose_controles'] = analyse_hypnose_controles()
    res['autres_a'] = autres_a()
    res['sens_seulement'] = SENS_SEULEMENT

    st, jo, hc = res['stetson'], res['jones'], res['hypnose_controles']
    facteurs_b = [
        # Stetson : +36 % de résolution rejeté, performance en vol = témoin au sol : aucun gain mesuré
        {'nom': 'stetson_resolution_chute', 'controle': True, 'inf': None, 'sup': None, 'valeur': 1.0},
        # Pariyadath : scintillement et hauteur inchangés pendant la dilatation
        {'nom': 'pariyadath_scintillement', 'controle': True, 'inf': None, 'sup': None, 'valeur': 1.0},
        {'nom': 'jones_clics_lettres', 'controle': True, 'inf': jo['facteur_borne_inf_95_approx'],
         'sup': jo['facteur_borne_sup_95_approx'], 'valeur': jo['facteur_moyen_approx']},
        # Cooper ch. 20 : calcul en temps distordu au niveau du hasard (contrôle : mêmes tâches éveillé)
        {'nom': 'cooper_calcul_temps_distordu', 'controle': True, 'inf': None, 'sup': None, 'valeur': 1.0},
        # Johnson 1976 : quantités apprises comparables
        {'nom': 'johnson_1976_apprentissage', 'controle': True, 'inf': None, 'sup': None, 'valeur': 1.0},
        # non contrôlés : exclus de la règle, rapportés
        {'nom': 'cooper_ch19_un_sujet', 'controle': False, 'inf': None, 'sup': None,
         'valeur': hc['cooper_ch19_un_sujet_sans_temoin_rapport_temps_etude']},
        # rapport SUGGÉRÉ (10 min pour 3 min), pas un gain mesuré (texte inaccessible) ; non reproduit
        {'nom': 'krauss_1974_rapport_suggere_non_reproduit', 'controle': False, 'inf': None, 'sup': None,
         'valeur': hc['krauss_1974_rapport_suggere']},
    ]
    res['facteurs_b'] = facteurs_b
    dec = decider(facteurs_b)
    Xb = dec['X_b']
    a_controle_max = max(st['facteur_contre_reel_borne_sup_95_prudente'], res['autres_a']['oddball_facteur_max_publie'])
    a_recit_max = res['hypnose_recits']['facteur_duree_declaree_max']
    b_non_controle_max = max(f['valeur'] for f in facteurs_b if not f['controle'])
    res['verdict'] = {
        'verdict': dec['verdict'],
        'X_b_borne_sup_95_vecu_par_seconde': Xb,
        'b_meilleur_gain_controle': jo['facteur_moyen_approx'],
        'b_meilleur_gain_controle_pct': 100.0 * (jo['facteur_moyen_approx'] - 1.0),
        'b_X_pct': 100.0 * (Xb - 1.0),
        'b_max_non_controle_non_reproduit': b_non_controle_max,
        'a_max_mesure_controlee': a_controle_max,
        'a_max_publie_psychophysique': res['autres_a']['oddball_facteur_max_publie'],
        'a_stetson_contre_reel': st['facteur_contre_reel'],
        'a_stetson_contre_autrui': st['facteur_contre_autrui'],
        'a_max_recit_hypnotique': a_recit_max,
        'facteur_necessaire_une_vie_en_une_nuit': FACTEUR_NECESSAIRE,
        'ecart_b': FACTEUR_NECESSAIRE / Xb,
        'ecart_b_ordres_de_grandeur': math.log10(FACTEUR_NECESSAIRE / Xb),
        'ecart_b_non_controle': FACTEUR_NECESSAIRE / b_non_controle_max,
        'ecart_a_controle': FACTEUR_NECESSAIRE / a_controle_max,
        'ecart_a_recit_hypnotique': FACTEUR_NECESSAIRE / a_recit_max,
    }
    return res


def arrondir(o):
    if isinstance(o, float):
        return float(f'{o:.6g}')
    if isinstance(o, dict):
        return {k: arrondir(v) for k, v in o.items()}
    if isinstance(o, list):
        return [arrondir(v) for v in o]
    return o


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='resultats.json')
    args = ap.parse_args()
    res = arrondir(principal())
    Path(args.out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    v = res['verdict']
    print(f"verdict : {v['verdict']} ; X_b = {v['X_b_borne_sup_95_vecu_par_seconde']} ; "
          f"a contrôlé max = {v['a_max_mesure_controlee']} ; récit hypnotique max = {v['a_max_recit_hypnotique']} ; "
          f"écart b = {v['ecart_b']:.0f}")
