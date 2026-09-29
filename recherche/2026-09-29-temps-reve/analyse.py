#!/usr/bin/env python3
"""Temps du rêve : mesures distinctes, sans facteur global de temps vécu.

Correction du 29 septembre 2026 : les durées déclarées, la discrimination de
5/15 minutes et les durées de tâches n'estiment pas un paramètre commun.
Les anciennes valeurs globales 0,84 et 0,92 sont retirées. Les réveils répétés
ne sont pas traités comme des sujets indépendants. Python 3.10+, numpy.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import urllib.request
import zipfile
from pathlib import Path
from statistics import NormalDist

import numpy as np

ICI = Path(__file__).resolve().parent
ZIP_TONONI = ICI / 'donnees' / 'tononi_part1.zip'
URL_TONONI = 'https://ndownloader.figshare.com/files/59168237'
SHA_TONONI = 'e4d7932ed96e65fe6ff1e25df9fea0229b2e7e3d3cca1730f9dd637531ff62b0'
GRAINE = 20260929
N = NormalDist()


# =========================================================================== valeurs publiées
VALEURS_PUBLIEES = {
    'dement_kleitman_1957': {
        'reveils_5min': 51, 'corrects_5min': 45,
        'reveils_15min': 60, 'corrects_15min': 47,
        'source': 'Dement & Kleitman, J. Exp. Psychol. 53, 339-346 (1957), doi:10.1037/h0048189 ; '
                  'original non lu. Erlacher et al. 2014 : « In 92 out of 111 awakenings (83%) the '
                  'participants judged correctly » ; guide Simply Psychology : « On 88% of trials (45/51) '
                  'the participants estimated 5 mins correctly », « On 78% of trials (47/60) [...] 15 mins '
                  'correctly ». 45 + 47 = 92 et 51 + 60 = 111 : concordant.'},
    'koulack_1968': {
        'jugements': 12, 'corrects': 11, 'sujets': 5,
        'source': 'Koulack, Psychon. Sci. 11(6), 202 (1968), doi:10.3758/BF03327656 : « There were 12 '
                  'instances obtained from five of the Ss [...]; 92% of S-judgments (11 of 12) placed those '
                  'incidents at a time corresponding to the time of stimulation » (30 s contre 3 min).'},
    'erlacher_2014': {
        # tableau 2 : moyenne (s), écart type (s), effectif, t apparié
        'comptage': {'W': 50.3, 'W_sd': 11.5, 'D': 64.0, 'D_sd': 17.1, 'n': 5, 't': 2.10, 'p': 0.10,
                     'plus_long_en_reve': 3},
        'marche': {'W': 37.7, 'W_sd': 1.7, 'D': 57.5, 'D_sd': 19.2, 'n': 7, 't': 2.82, 'p': 0.03,
                   'plus_long_en_reve': 5},
        'gymnastique': {'W': 6.6, 'W_sd': 0.1, 'D': 8.1, 'D_sd': 1.5, 'n': 8, 't': 2.81, 'p': 0.03,
                        'plus_long_en_reve': 6},
        'source': 'Erlacher, Schädlich, Stumbrys & Schredl, Front. Psychol. 4, 1013 (2014), '
                  'doi:10.3389/fpsyg.2013.01013, tableau 2 et § Results. Les participants du comptage ont '
                  'aussi fait la marche (non indépendants) ; la gymnastique est un autre groupe.'},
    'erlacher_schredl_2004': {
        'squats_ecart_pct': 39.9,
        'source': 'Erlacher & Schredl, Percept. Mot. Skills 99, 1239-1242 (2004), cité par Erlacher 2014 : '
                  '« squats: 39.9% » ; pas d\'écart type publié pour le rêve : hors méta-synthèse.'},
    'carlson_1978': {
        'intervalle_reel_moyen_min': 38.7, 'estimation_moyenne_min': 61.6,
        'source': 'Carlson, Feinberg & Goodenough, Physiol. Psychol. 6(4), 497-500 (1978) : « The actual time '
                  'intervals varied from 10 min to 2 h (mean = 38.7 min [...]). The subjects\' time estimates '
                  'ranged from 5 min to 3 h (mean = 61.6 min [...]) ». Temps écoulé (éveil compris), pas vécu '
                  'd\'un rêve : hors méta-synthèse.'},
}

# classes de durée du jeu Tononi (secondes) : borne basse, borne haute
CLASSES_TONONI = {1: (0.0, 5.0), 2: (5.0, 10.0), 3: (10.0, 60.0), 4: (60.0, 600.0),
                  5: (600.0, 3600.0), 6: (3600.0, math.inf)}
NOUVELLE_NUIT_MIN = 360.0  # écart de plus de 6 h entre deux réveils : autre nuit


def charger_tononi() -> tuple[list[dict], list[dict]]:
    if not ZIP_TONONI.exists():
        ZIP_TONONI.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(URL_TONONI, timeout=120) as r:
            ZIP_TONONI.write_bytes(r.read())
    brut = ZIP_TONONI.read_bytes()
    empreinte = hashlib.sha256(brut).hexdigest()
    if empreinte != SHA_TONONI:
        raise SystemExit(f'empreinte SHA-256 inattendue pour {ZIP_TONONI.name} : {empreinte}')
    z = zipfile.ZipFile(io.BytesIO(brut))
    lire = lambda nom: list(csv.DictReader(io.StringIO(z.read(nom).decode('utf-8-sig'))))
    records = lire('Tononi Serial Awakenings/Records.csv')
    add = lire('Tononi Serial Awakenings/Data/AdditionalData.csv')
    return records, add


def minutes(h: str) -> float:
    hh, mm, ss = (int(x) for x in h.split(':'))
    return hh * 60 + mm + ss / 60.0


def bornes_dormi(records: list[dict]) -> dict[str, float | None]:
    """Temps écoulé (s) depuis le réveil précédent du même sujet la même nuit ; None sinon."""
    par_sujet: dict[str, list[tuple[int, str, float]]] = {}
    for r in records:
        ep = int(r['Filename'].split('_ep')[1].split('.')[0])
        par_sujet.setdefault(r['Subject ID'], []).append((ep, r['Filename'], minutes(r['Time of awakening'])))
    borne: dict[str, float | None] = {}
    for liste in par_sujet.values():
        liste.sort()
        borne[liste[0][1]] = None
        for (_, _, t1), (_, f2, t2) in zip(liste, liste[1:]):
            ecart = (t2 - t1) % 1440.0
            borne[f2] = ecart * 60.0 if 0.0 < ecart <= NOUVELLE_NUIT_MIN else None
    return borne


def analyse_tononi(records: list[dict], add: list[dict]) -> dict:
    borne = bornes_dormi(records)
    exp = {r['Filename']: r['Experience'] for r in records}
    cle_duree = [k for k in add[0] if k.startswith('Duration of continuous')][0]
    lignes = []
    for a in add:
        c = a[cle_duree].strip()
        if not c:
            continue
        c = int(c)
        lignes.append({'fichier': a['Filename'], 'classe': c, 'experience': exp[a['Filename']],
                       'dormi_max_s': borne[a['Filename']]})
    return resume_tononi(lignes)


def sdt_ln_F(p_faux_5: float, p_faux_15: float, frontiere_min: float) -> tuple[float, float]:
    """Modèle log-normal : ln S = ln F + ln T + σ ε. Retourne (ln F, σ)."""
    za = N.inv_cdf(1.0 - p_faux_5)   # P(S > c | T = 5) = p_faux_5
    zb = N.inv_cdf(p_faux_15)        # P(S < c | T = 15) = p_faux_15
    sigma = math.log(3.0) / (za - zb)
    lnF = math.log(frontiere_min / 5.0) - za * sigma
    return lnF, sigma


def resume_tononi(lignes: list[dict]) -> dict:
    classes = {str(c): sum(l['classe'] == c for l in lignes) for c in CLASSES_TONONI}
    bornees = [l for l in lignes if l['dormi_max_s'] is not None]
    depasse = [l for l in bornees if CLASSES_TONONI[l['classe']][0] > l['dormi_max_s']]
    return {
        'n_estimations': len(lignes), 'effectifs_par_classe': classes,
        'n_avec_intervalle_reconstruit': len(bornees),
        'n_borne_declaree_depasse_intervalle': len(depasse),
        'proportion_des_rapports_depassement': len(depasse) / len(bornees) if bornees else None,
        'borne_frequence_acceleration': None,
        'methode': 'Intervalle entre réveils du même sujet, nuits séparées par un seuil heuristique de 6 h.',
        'portee': 'Description des rapports. Début réel du rêve inconnu ; intervalle reconstruit et durée '
                  'déclarée ne mesurent pas directement le temps vécu. Une absence de dépassement ne borne '
                  'pas la fréquence des accélérations. Réveils répétés, non indépendants.',
    }


def analyse_dement_kleitman() -> dict:
    v = VALEURS_PUBLIEES['dement_kleitman_1957']
    n5, n15 = v['reveils_5min'], v['reveils_15min']
    p5, p15 = 1-v['corrects_5min']/n5, 1-v['corrects_15min']/n15
    exemples = []
    for c in (math.sqrt(75), 10, 10*math.sqrt(75)):
        lnF, sigma = sdt_ln_F(p5, p15, c)
        exemples.append({'critere_choisi_minutes': c, 'F_conditionnel': math.exp(lnF), 'sigma_ln': sigma})
    return {
        'reveils': n5+n15, 'corrects': v['corrects_5min']+v['corrects_15min'],
        'taux_correct': (v['corrects_5min']+v['corrects_15min'])/(n5+n15),
        'facteur_identifie': None,
        'illustration_non_identifiabilite': exemples,
        'portee': 'Les réponses binaires ne séparent pas F du critère de décision c. '
                  'Multiplier F et c par le même nombre laisse les probabilités de réponse inchangées. '
                  'Effectifs secondaires ; original non relu. Aucune borne de F déduite.',
    }


def facteur_erlacher(d: dict) -> dict:
    return {'n': d['n'], 'duree_eveil_s': d['W'], 'duree_reve_s': d['D'],
            'rapport_moyennes_eveil_sur_reve': d['W']/d['D'],
            'allongement_en_reve_pct': 100*(d['D']/d['W']-1),
            'p_apparie_publie': d['p'],
            'portee': 'Durée chronométrée de cette tâche ; ni durée phénoménale ni ratio individuel moyen.'}


def autotests() -> dict:
    # Régression : un choix forcé ne distingue pas un facteur et un critère multipliés ensemble.
    a, sa = sdt_ln_F(6/51, 13/60, 10)
    b, sb = sdt_ln_F(6/51, 13/60, 100)
    # Contre-exemple : 120 s ressenties dans 60 s, à l'intérieur d'un intervalle de 30 min.
    # Le détecteur ne signale rien malgré cette accélération hypothétique d'un facteur deux.
    exemple = resume_tononi([{'classe': 4, 'dormi_max_s': 1800, 'experience': '2'}])
    r = {'critere_et_facteur_non_identifiables': abs(b-a-math.log(10)) < 1e-12 and abs(sa-sb) < 1e-12,
         'non_detection_ne_prouve_pas_absence': exemple['n_borne_declaree_depasse_intervalle'] == 0
                    and exemple['borne_frequence_acceleration'] is None,
         'depassement_detectable': resume_tononi([{'classe': 5, 'dormi_max_s': 60}])['n_borne_declaree_depasse_intervalle'] == 1,
         'durations_distinctes': facteur_erlacher(VALEURS_PUBLIEES['erlacher_2014']['marche'])['duree_reve_s'] == 57.5}
    assert all(r.values()), r
    return {**r, 'tous_passes': True}


def principal() -> dict:
    records, add = charger_tononi()
    e = VALEURS_PUBLIEES['erlacher_2014']
    t = analyse_tononi(records, add)
    t['sha256_archive'] = SHA_TONONI
    k = VALEURS_PUBLIEES['koulack_1968']
    return {
        'question': 'Que mesurent les expériences sur la durée du rêve ?',
        'version_analyse': 2,
        'donnees_ouvertes_tononi': t, 'dement_kleitman': analyse_dement_kleitman(),
        'koulack': {'jugements': k['jugements'], 'corrects': k['corrects'], 'participants': k['sujets'],
                    'portee': 'Localisation temporelle déclarée ; observations répétées.'},
        'erlacher': {k: facteur_erlacher(e[k]) for k in ('comptage', 'marche', 'gymnastique')},
        'valeurs_publiees': VALEURS_PUBLIEES,
        'verdict': {'reponse': 'acceleration_generale_non_etablie', 'F_global': None,
                    'X_borne_sup_95': None, 'facteur_necessaire_une_vie_en_une_nuit': 87660,
                    'portee': 'Pas de démonstration de vie accélérée dans ce corpus ; aucune borne universelle déduite.'},
        'corrections': ['Méta-analyse retirée : construits distincts.',
                       'Borne de fréquence retirée : non-détection non informative et réveils dépendants.',
                       'Borne de F par choix forcé retirée : critère non identifié.'],
        'autotests': autotests(),
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ICI / 'resultats.json'))
    args = ap.parse_args()
    res = principal()
    Path(args.out).write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(res['verdict']['reponse'])
