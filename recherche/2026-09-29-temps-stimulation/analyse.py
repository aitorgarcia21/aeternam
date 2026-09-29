#!/usr/bin/env python3
"""Interventions : distinguer durée jugée, performance et expérience consciente.

Correction du 29 septembre 2026. Les valeurs 1,09 et 0,92 ne sont pas des
bornes du temps vécu. Une absence de différence significative n'est pas une
preuve d'équivalence. Les données manquantes restent nulles. Aucune intervention
n'est appliquée par ce script : il réanalyse des valeurs publiées.
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
    propre, autrui, reel = v['duree_rappelee_propre_chute_s'], v['duree_imaginee_autrui_s'], v['duree_reelle_chute_s']
    return {'mesure': 'Durée rétrospective déclarée',
            'facteur_contre_reel': propre/reel, 'facteur_contre_autrui': propre/autrui,
            'dilatation_contre_autrui_pct': 100*(propre/autrui-1),
            'borne_sup_95': None,
            'note': 'Rapports descriptifs. Incertitude du dénominateur et nature des ± insuffisamment établies.'}


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
    return {'mesure': 'Lettres correctement rapportées dans cette tâche',
            'facteur_300ms': 1+g300/100, 'facteur_500ms': 1+g500/100,
            'moyenne_arithmetique_gains_pct': (g300+g500)/2,
            'facteur_borne_inf_95_approx': None, 'facteur_borne_sup_95_approx': None,
            'note': 'Le F de l’effet principal sur les scores ne donne pas l’erreur type de la moyenne '
                    'des gains relatifs. Intervalle 1,09 retiré. Performance différente de temps vécu.'}


def analyse_hypnose_controles() -> dict:
    v = VALEURS_PUBLIEES['cooper_erickson_1954']
    k = VALEURS_PUBLIEES['krauss_1974_selon_johnson_1976']
    return {
        'cooper_ch19_un_sujet_sans_temoin_rapport_temps_etude': v['ch19_temps_par_paire_eveil_s'] / v['ch19_temps_par_paire_transe_s'],
        'cooper_ch19_retention_identique': v['ch19_retention_pct_eveil'] == v['ch19_retention_pct_transe'],
        'cooper_ch20_calcul_temps_court': 'pas de supériorité au hasard rapportée ; équivalence non établie',
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
def decider(facteurs_b: list[dict]) -> dict:
    # Même des intervalles complets sur des tâches hétérogènes ne bornent pas le temps vécu.
    return {'verdict': 'acceleration_generale_non_etablie', 'X_b': None,
            'n_sans_intervalle': sum(f.get('sup') is None or f.get('inf') is None for f in facteurs_b)}


def autotests() -> dict:
    r = {'incertitude_absente_preservee': decider([{'valeur': 1, 'sup': None, 'inf': None}])['X_b'] is None,
         'performance_non_convertie_en_vecu': decider([{'valeur': 3.5, 'inf': 3, 'sup': 4}])['X_b'] is None,
         'jones_intervalle_non_identifie': analyse_jones()['facteur_borne_sup_95_approx'] is None,
         'facteur_projet': FACTEUR_NECESSAIRE == 87660}
    assert all(r.values()), r
    return {**r, 'tous_passes': True}


def principal() -> dict:
    return {'question': 'Quelles dimensions du temps les interventions modifient-elles ?',
            'version_analyse': 2, 'valeurs_publiees': VALEURS_PUBLIEES,
            'stetson': analyse_stetson(), 'jones': analyse_jones(),
            'hypnose_recits': analyse_hypnose_recits(), 'hypnose_controles': analyse_hypnose_controles(),
            'autres_a': autres_a(), 'sens_seulement': SENS_SEULEMENT,
            'verdict': {'verdict': 'acceleration_generale_non_etablie',
                        'X_b_borne_sup_95_vecu_par_seconde': None,
                        'facteur_necessaire_une_vie_en_une_nuit': FACTEUR_NECESSAIRE,
                        'portee': 'Des changements de jugement et de performance sont publiés ; '
                                  'ils ne quantifient pas une accélération générale de la vie consciente.'},
            'corrections': ['Borne universelle 1,09 retirée.', 'Valeurs 1 imputées aux résultats non significatifs retirées.',
                           'Comparaisons entre récits, scores et vie entière retirées.'],
            'autotests': autotests()}


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
    print(v['verdict'])
