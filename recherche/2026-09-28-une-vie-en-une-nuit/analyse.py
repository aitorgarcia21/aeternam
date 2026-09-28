#!/usr/bin/env python3
"""Projet « une vie en une nuit » : ce qu'il faudrait, ce qu'on mesure aujourd'hui.

Calcule le facteur d'accélération du temps vécu nécessaire pour vivre une vie
entière pendant une nuit de sommeil, et le compare aux mesures publiées du temps
dans les rêves lucides. Toutes les valeurs d'entrée sont citées dans CITE, avec
leur source (détail et passages dans sources.md). Bibliothèque standard.

Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

# Hypothèses du projet (choisies, non mesurées) : une vie de 80 ans, une nuit de 8 heures.
VIE_ANS, NUIT_H, JOURS_PAR_AN = 80, 8, 365.25

CITE = {
    # Erlacher, Schädlich, Stumbrys, Schredl (2014), Front. Psychol. 4:1013, tableau 2 (moyennes, s).
    'erlacher2014': {'compter': (50.3, 64.0), 'marcher': (37.7, 57.5), 'gymnastique': (6.6, 8.1),
                     'p': {'compter': 0.10, 'marcher': 0.03, 'gymnastique': 0.03}},
    # Mitterling et al. (2015), Sleep 38(6):867, résumé : médianes.
    'mitterling2015': {'moins_de_30_ans': {'sommeil_total_min': 413.5, 'part_paradoxal_pct': 15.5},
                       'plus_de_60_ans': {'sommeil_total_min': 378.3, 'part_paradoxal_pct': 10.3}},
    # Konkoly et al. (2021), Current Biology 31(7):1417, tableau 2.
    'konkoly2021': {'participants': 36, 'essais': 158, 'corrects': 29, 'incorrects': 5, 'ambigus': 28,
                    'sans_reponse': 96},
    # Haar Horowitz et al. (2020), Consciousness and Cognition 83:102938.
    'dormio2020': {'participants': 49, 'recits_avec_consigne': 67, 'avec_arbre': 45,
                   'recits_sans_consigne': 69, 'sans_consigne_avec_arbre': 2},
    # Vitesses de rejeu mesurées (facteur = durée vécue / durée du rejeu ; détail dans sources.md).
    'rejeu': {
        'humain_eveil_meg_kurth_nelson_2016': 100,      # « ∼25–100 », borne haute retenue (le plus favorable)
        'rat_sommeil_lent_lee_wilson_2002': 20,          # « approximately 20-fold » (résumé)
        'rat_prefrontal_sommeil_euston_2007': 6.5,       # « a factor of 6 to 7 » (résumé), milieu
        'rat_sommeil_paradoxal_louie_wilson_2001': 1 / 1.4,  # échelle moyenne « 1.4 ± 0.6 » : plus lent
    },
    # Rosenblum et al. (2025), eLife : 205 adultes, 961 cycles.
    'rosenblum2025': {'cycles': 4.7, 'duree_cycle_min': 90.1, 'part_paradoxal_pct': 18.6, 'sommeil_min': 438},
    # Fenêtres d'intégration perceptive de 290 à 450 ms (Drissi-Daoudi et al. 2019) ; ordre de grandeur retenu
    # pour le nombre d'« instants » vécus : de 2 à 10 par seconde (voir sources.md).
    'instants_par_seconde': (2, 10),
    # Pew Research Center (2013), Living to 120 and Beyond, chapitre 1 et méthode.
    'pew2013': {'voudraient_pct': 38, 'ne_voudraient_pas_pct': 56, 'duree_ideale_mediane_ans': 90,
                'plus_de_100_ans_pct': 9, 'echantillon': 2012},
}


def calculer() -> dict:
    heures_vie = VIE_ANS * JOURS_PAR_AN * 24
    facteur_nuit = heures_vie / NUIT_H
    m = CITE['mitterling2015']
    paradoxal = {k: v['sommeil_total_min'] * v['part_paradoxal_pct'] / 100 for k, v in m.items()}
    facteur_paradoxal = {k: heures_vie * 60 / minutes for k, minutes in paradoxal.items()}
    e = CITE['erlacher2014']
    rapports = {t: e[t][1] / e[t][0] for t in ('compter', 'marcher', 'gymnastique')}
    rejeu = CITE['rejeu']
    meilleur = max(rejeu.values())
    lo, hi = CITE['instants_par_seconde']
    secondes_vie = heures_vie * 3600
    modele = {
        'meilleure_compression_mesuree': meilleur,
        'ecart_restant_avec_la_meilleure': facteur_nuit / meilleur,
        'ecart_restant_sommeil_lent': facteur_nuit / rejeu['rat_sommeil_lent_lee_wilson_2002'],
        'instants_vie': {'bas': secondes_vie * lo, 'haut': secondes_vie * hi},
        'instants_par_seconde_de_nuit_necessaires': {'bas': secondes_vie * lo / (NUIT_H * 3600),
                                                     'haut': secondes_vie * hi / (NUIT_H * 3600)},
        'minutes_paradoxal_rosenblum': CITE['rosenblum2025']['sommeil_min'] * CITE['rosenblum2025']['part_paradoxal_pct'] / 100,
    }
    k, d = CITE['konkoly2021'], CITE['dormio2020']
    r = {
        'hypotheses': {'vie_ans': VIE_ANS, 'nuit_heures': NUIT_H, 'jours_par_an': JOURS_PAR_AN},
        'heures_de_vie': heures_vie,
        'facteur_nuit_entiere': facteur_nuit,
        'heures_vecues_par_seconde_de_nuit': facteur_nuit / 3600,
        'minutes_paradoxal_par_nuit': paradoxal,
        'facteur_sommeil_paradoxal_seul': facteur_paradoxal,
        'reve_lucide_duree_reve_sur_eveil': rapports,
        'reve_lucide_allongement_pct': {t: 100 * (x - 1) for t, x in rapports.items()},
        'facteur_de_compression_mesure_max': max(1 / x for x in rapports.values()),
        'konkoly_pct': {c: 100 * k[c] / k['essais'] for c in ('corrects', 'incorrects', 'ambigus', 'sans_reponse')},
        'dormio_pct': {'avec_consigne': 100 * d['avec_arbre'] / d['recits_avec_consigne'],
                       'sans_consigne': 100 * d['sans_consigne_avec_arbre'] / d['recits_sans_consigne']},
        'modele': modele,
        'valeurs_citees': CITE,
    }
    # Autotests
    assert heures_vie == 701_280
    assert abs(facteur_nuit - 87_660) < 1e-9
    assert all(x > 1 for x in rapports.values()), 'le rêve lucide mesuré ne va pas plus vite que l’éveil'
    assert abs(r['konkoly_pct']['corrects'] - 18.35) < 0.01 and abs(r['konkoly_pct']['sans_reponse'] - 60.76) < 0.01
    assert k['corrects'] + k['incorrects'] + k['ambigus'] + k['sans_reponse'] == k['essais']
    assert round(r['dormio_pct']['avec_consigne']) == 67 and round(r['dormio_pct']['sans_consigne']) == 3
    assert abs(modele['ecart_restant_avec_la_meilleure'] - 876.6) < 1e-6
    assert all(x < facteur_nuit / 100 for x in rejeu.values()), 'aucune voie mesurée n’approche le facteur'
    r['autotests'] = 'OK'
    return r


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--out', type=Path, default=Path(__file__).with_name('resultats.json'))
    args = parser.parse_args()
    resultats = calculer()
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"facteur {resultats['facteur_nuit_entiere']:.0f} ; paradoxal seul "
          f"{resultats['facteur_sommeil_paradoxal_seul']} ; rêve/éveil {resultats['reve_lucide_duree_reve_sur_eveil']}")
