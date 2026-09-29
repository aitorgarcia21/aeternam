#!/usr/bin/env python3
"""Aeternam : cinq axes étudiés sans nouvelles expériences humaines.

Données individuelles DREAM (archive vérifiée), statistiques publiées,
contre-exemples d'identification et simulations de puissance explicitement
hypothétiques. Aucune donnée simulée n'est présentée comme humaine.
Python >= 3.10 et numpy. --out resultats.json
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np

ICI = Path(__file__).resolve().parent
RECHERCHE = ICI.parent
GRAINE = 20260929


def module(dossier):
    spec = importlib.util.spec_from_file_location(dossier.replace('-', '_'), RECHERCHE / dossier / 'analyse.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


REVE = module('2026-09-29-temps-reve')
STIM = module('2026-09-29-temps-stimulation')
PROJET = module('2026-09-28-une-vie-en-une-nuit')


def bootstrap_sujets(valeurs, rng, tirages=20000):
    """Moyenne des proportions individuelles, poids égal par sujet éligible."""
    a = np.asarray(valeurs, dtype=float)
    if len(a) < 2:
        return {'moyenne': float(a.mean()) if len(a) else None, 'ic95_percentile': None}
    b = a[rng.integers(0, len(a), size=(tirages, len(a)))].mean(axis=1)
    return {'moyenne': float(a.mean()), 'ic95_percentile': np.quantile(b, [.025,.975]).tolist()}


def donnees_dream(rng):
    records, add = REVE.charger_tononi()
    par_id = {r['Filename']:r for r in records}
    assert len(par_id) == len(records) and len({a['Filename'] for a in add}) == len(add)
    assert {a['Filename'] for a in add} == set(par_id)
    cle = next(k for k in add[0] if k.startswith('Duration of continuous'))
    lignes = []
    for a in add:
        r = par_id[a['Filename']]
        d, p = a[cle].strip(), a['Perception (yes=1, no=0)'].strip()
        lignes.append({'sujet': r['Subject ID'], 'experience': r['Experience'],
                       'classe_duree': int(d) if d else None, 'perception': int(p) if p else None})
    ids = sorted({l['sujet'] for l in lignes}, key=int)
    sujets = []
    for i in ids:
        ls = [l for l in lignes if l['sujet']==i]
        ld = [l for l in ls if l['classe_duree'] is not None]
        sujets.append({'sujet': i, 'reveils':len(ls), 'avec_duree':len(ld),
                       'rappel_code2':sum(l['experience']=='2' for l in ls),
                       'proportion_duree_au_moins_1min': sum(l['classe_duree']>=4 for l in ld)/len(ld) if ld else None,
                       'proportion_perception':sum(l['perception']==1 for l in ld)/len(ld) if ld else None})
    avec = [l for l in lignes if l['classe_duree'] is not None]
    assert all((l['classe_duree'] is not None) == (l['experience']=='2') for l in lignes)
    assert all(l['perception'] in (0,1) for l in avec)
    # Association exploratoire : différence de proportions de durées >=1 min entre perception oui/non,
    # calculée dans chaque sujet présentant les deux réponses ; bootstrap par personne.
    differences = []
    for i in ids:
        oui=[l['classe_duree']>=4 for l in avec if l['sujet']==i and l['perception']==1]
        non=[l['classe_duree']>=4 for l in avec if l['sujet']==i and l['perception']==0]
        if oui and non:
            differences.append(float(np.mean(oui)-np.mean(non)))
    return {
        'statut':'réanalyse individuelle observationnelle',
        'source':REVE.URL_TONONI, 'sha256':REVE.SHA_TONONI,
        'n_reveils':len(lignes), 'n_sujets':len(ids), 'n_durees':len(avec),
        'n_sujets_avec_duree':sum(s['avec_duree']>0 for s in sujets),
        'effectifs_experience':{c:sum(l['experience']==c for l in lignes) for c in ('0','1','2')},
        'n_durees_manquantes':len(lignes)-len(avec),
        'effectifs_classes_duree':{str(c):sum(l['classe_duree']==c for l in avec) for c in range(1,7)},
        'n_duree_au_moins_1min':sum(l['classe_duree']>=4 for l in avec),
        'part_rapports_au_moins_1min':sum(l['classe_duree']>=4 for l in avec)/len(avec),
        'part_sujets_au_moins_1min':bootstrap_sujets([s['proportion_duree_au_moins_1min'] for s in sujets if s['avec_duree']],rng),
        'n_sujets_comparables_perception':len(differences),
        'difference_perception_oui_moins_non':bootstrap_sujets(differences,rng),
        'sujets':sujets,
        'portee':'N2 uniquement. Durées présentes pour les expériences rappelées ; sélection non aléatoire. '
                 'Les intervalles décrivent une variabilité entre sujets du corpus, pas une population générale. '
                 'Le seuil 1 min est choisi pour cette exploration. Association non causale, sans test confirmatoire.',
    }


def durees_taches():
    r={}
    for nom in ('comptage','marche','gymnastique'):
        d=REVE.VALEURS_PUBLIEES['erlacher_2014'][nom]
        delta=d['D']-d['W']; se=delta/d['t']; q=STIM.t_ppf(.975,d['n']-1)
        r[nom]={'n':d['n'],'difference_reve_moins_eveil_s':delta,
                'ic95_difference_s':[delta-q*se,delta+q*se],
                'p_bilateral_recalcule':2*(1-STIM.t_cdf(d['t'],d['n']-1)),
                'ratio_moyennes_eveil_sur_reve':d['W']/d['D']}
    return {'statut':'reconstruction à partir de moyennes et t appariés publiés arrondis',
            'taches':r,'portee':'Intervalles marginaux de différence en secondes, sans correction multiple. '
                    'Comptage et marche partagent des sujets ; aucun regroupement en vitesse de conscience.'}


def acces_contenu():
    k=PROJET.CITE['konkoly2021']; d=PROJET.CITE['dormio2020']
    avec=d['avec_arbre']/d['recits_avec_consigne']; sans=d['sans_consigne_avec_arbre']/d['recits_sans_consigne']
    return {
        'statut':'recalcul descriptif de tableaux publiés, pas de données individuelles pour ces études',
        'dialogue':{'essais':k['essais'],'corrects':k['corrects'],
                    'part_correcte_tous_essais':k['corrects']/k['essais'],
                    'part_correcte_reponses_interpretees':k['corrects']/(k['corrects']+k['incorrects']),
                    'part_sans_reponse_ou_ambigue':(k['sans_reponse']+k['ambigus'])/k['essais'],
                    'note':'Le changement de dénominateur change le taux. Essais répétés chez les mêmes personnes ; pas de CI binomial par essai.'},
        'incubation_2020':{'part_recits_avec_consigne':avec,'part_recits_sans_consigne':sans,
                           'difference_points_pct':100*(avec-sans), 'rapport_des_proportions':avec/sans,
                           'note':'Récits répétés, non personnes indépendantes. Un thème incorporé ne signifie pas contrôle narratif.'},
        'incubation_rem_2026':{'n_recrutes':11, 'n_avec_rem':8, 'n_incorporation_rem':7,
                               'part_parmi_rem':7/8,'part_tous_participants':7/11,
                               'recits_rem_avec_theme':10,'recits_rem':21,'part_recits_rem':10/21,
                               'note':'Pilote sans groupe contrôle. Taux différents selon l’unité ; aucun effet causal calculable.'},
    }


def puissance(rng, repetitions=6000):
    """Laboratoire numérique uniquement : log-ratios simulés, dépendance intra-sujet explicite.

    Effet cible choisi 20 %, écart-type marginal choisi 0,35, trois répétitions.
    Test t sur la moyenne de chaque sujet vs test naïf sur toutes les répétitions.
    Les paramètres ne sont pas des estimations de l'efficacité d'Aeternam.
    """
    resultats=[]; sd=.35; m=3
    for n in (20,40,80):
        for rho in (0.,.3,.6):
            z = sd*(math.sqrt(rho)*rng.normal(size=(repetitions,n,1))
                    +math.sqrt(1-rho)*rng.normal(size=(repetitions,n,m)))
            qs, qn = STIM.t_ppf(.975,n-1), STIM.t_ppf(.975,n*m-1)
            stats={}
            for nom,mu in (('nul',0.),('gain_20pct',math.log(1.2))):
                x=z+mu; a=x.mean(axis=2); b=x.reshape(repetitions,-1)
                ts=a.mean(axis=1)/(a.std(axis=1,ddof=1)/math.sqrt(n))
                tn=b.mean(axis=1)/(b.std(axis=1,ddof=1)/math.sqrt(n*m))
                stats[nom]={'taux_rejet_par_sujet':float(np.mean(ts>qs)),
                            'taux_rejet_naif_par_essai':float(np.mean(tn>qn))}
            resultats.append({'n_sujets':n,'repetitions_par_sujet':m,'correlation_intra_sujet':rho,**stats})
    return {'statut':'données entièrement synthétiques', 'simulations_par_scenario':repetitions,
            'gain_cible_choisi':1.2,'sd_log_ratio_choisi':sd, 'alpha_unilateral':.025,
            'erreur_monte_carlo_max_95_points_pct':100*1.96*math.sqrt(.25/repetitions),
            'scenarios':resultats}


def temps_memoire():
    annees=80; secondes=annees*365.25*24*3600; nuit=8*3600
    return {'statut':'hypothèses de conception, pas mesures cérébrales',
            'annees_cibles':annees,'nuit_heures':8,'facteur_continu_24h':secondes/nuit,
            'facteur_si_16h_vecues_par_jour':secondes*(16/24)/nuit,
            'scenes_choisies':100,'minutes_par_scene_choisies':3,
            'heures_total_scenes':100*3/60,
            'portee':'Cent scènes de trois minutes tiennent dans cinq heures par construction. '
                    'Elles ne constituent ni 80 années continues ni une preuve de continuité autobiographique. '
                    'Le modèle permet de spécifier deux objectifs distincts, sans substituer le récit à l’objectif central.'}


def calculer():
    rng=np.random.default_rng(GRAINE)
    d=donnees_dream(rng); t=durees_taches(); a=acces_contenu(); p=puissance(rng); m=temps_memoire()
    checks={
        'jointure_complete':d['n_durees']+d['n_durees_manquantes']==d['n_reveils'],
        'unite_sujet_conservee':sum(s['reveils'] for s in d['sujets'])==d['n_reveils'],
        'selection_explicite':d['n_durees']==d['effectifs_experience']['2'],
        'faux_positifs_calibres':all(.012<s['nul']['taux_rejet_par_sujet']<.04 for s in p['scenarios']),
        'dependance_revelee':all(s['nul']['taux_rejet_naif_par_essai']>s['nul']['taux_rejet_par_sujet']+.025 for s in p['scenarios'] if s['correlation_intra_sujet']==.6),
        'reconstruction_p':abs(t['taches']['comptage']['p_bilateral_recalcule']-.1)<.01,
        'objectif_litteral':m['facteur_continu_24h']==87660,
    }
    assert all(checks.values()), checks
    return {'date':'2026-09-29','graine':GRAINE,'version':1,
            'temps_dream':d,'taches_lucides':t,'acces_et_contenu':a,'laboratoire_numerique':p,
            'temps_et_memoire':m,'autotests':checks,
            'statut_general':'Réanalyses de données existantes et simulations ; aucun dispositif Aeternam testé sur une personne.'}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=ICI/'resultats.json')
    args=ap.parse_args();r=calculer();args.out.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    d=r['temps_dream']; print(json.dumps({k:v for k,v in d.items() if k not in ('sujets','portee')},ensure_ascii=False,indent=2))
    print('Autotests :',r['autotests'])
