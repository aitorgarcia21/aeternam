#!/usr/bin/env python3
"""Les molécules qui allongent la vie de la souris retardent-elles le vieillissement, ou le ralentissent-elles ?

Entrée : donnees/itp-survie.csv, les durées de vie individuelles des souris de l'Interventions
Testing Program (ITP) du National Institute on Aging, cohortes 2004 à 2021, telles que la Mouse
Phenome Database les publie (projet ITP1). Une ligne = une souris : cohorte, site (TJL, UM, UT),
sexe, groupe, dose, âge de début du traitement, mort (1) ou retirée de l'étude (0), âge en jours.

La question. Le risque de mourir d'une souris adulte croît à peu près comme une exponentielle de
l'âge (Gompertz) : h(t) = a·exp(b·t). Le temps de doublement du risque est ln 2 / b. Un traitement
peut allonger la vie de deux façons :

  - retarder : le risque est divisé par un même facteur à tout âge, h1(t) = θ·h0(t). La courbe du
    risque est la même, décalée vers la droite ; le temps de doublement ne change pas ;
  - ralentir : à partir du début du traitement (âge s), le temps s'écoule λ fois plus lentement,
    h1(t) = (1/λ)·h0(s + (t − s)/λ). Le temps de doublement est multiplié par λ.

Le modèle général contient les deux : h1(t) = θ·a·exp(b·s)·exp((b/λ)(t − s)). « Retarder » est le
cas λ = 1, « ralentir » le cas θ = 1/λ. Pour chaque groupe traité, comparé aux témoins de la même
cohorte et du même sexe, quatre modèles sont ajustés par maximum de vraisemblance (sans effet,
retard, ralentissement, général), avec une courbe de base (a, b) propre à chaque site. Chaque
souris entre dans le calcul à l'âge le plus tardif entre le début du traitement et 365 jours
(troncature à gauche) ; une souris retirée de l'étude est censurée à son âge de retrait.

Ce que le calcul donne :
  1. les traitements qui allongent la vie (test du modèle général contre « sans effet », 2 degrés
     de liberté, seuil de Bonferroni sur toutes les comparaisons, risque diminué) ;
  2. pour chacun, le rapport λ des temps de doublement, et les tests « λ = 1 » (le retard suffit)
     et « θ = 1/λ » (le ralentissement suffit), 1 degré de liberté chacun ;
  3. l'étalonnage : parmi les comparaisons sans effet, la part de rejets de « λ = 1 » devrait être
     5 % ; le quantile 95 % observé sert de seuil corrigé ;
  4. un contrôle sans modèle : le gain en jours à la médiane et au 90e centile des âges de mort ;
  5. des simulations numériques (pas des mesures) : le calcul retrouve-t-il un retard et un
     ralentissement fabriqués, avec des effectifs comme ceux de l'ITP ?
  6. la reproduction d'un résultat publié (Harrison et al. 2009), pour vérifier la lecture des
     données.

Limites : analyse exploratoire, faite après avoir vu les données, sans plan déposé ; le modèle de
Gompertz est une approximation ; les groupes d'une même cohorte partagent leurs témoins.

Python >= 3.9 et numpy. Usage : python3 analyse.py --out resultats.json
"""
import argparse
import collections
import csv
import json
import math
import re
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
AN = 365.25
MOIS = 30.4375
PLANCHER_JOURS = 365.0
SITES = ('TJL', 'UM', 'UT')
OR = (math.sqrt(5) - 1) / 2
T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
        11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093,
        20: 2.086, 21: 2.080, 22: 2.074, 23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048,
        29: 2.045, 30: 2.042}


def lire(chemin):
    """Les souris : (cohorte, site, sexe, groupe, âge de début en mois ou None, mort 0/1, âge en jours)."""
    souris = []
    with open(chemin, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            m = re.match(r'\s*(\d+(?:\.\d+)?)', r['age_debut_mois'])
            souris.append((r['cohorte'], r['site'], r['sexe'], r['groupe'], float(m.group(1)) if m else None,
                           int(r['mort']), float(r['age_jours'])))
    return souris


def maximum(f, a, b, tol=1e-4):
    """Maximum d'une fonction à un seul sommet sur [a, b] (section dorée)."""
    c, d = b - OR * (b - a), a + OR * (b - a)
    fc, fd = f(c), f(d)
    while b - a > tol:
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - OR * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + OR * (b - a)
            fd = f(d)
    x = (a + b) / 2
    return x, f(x)


def simplexe(f, x0, pas=0.15, tours=160, tol=1e-6):
    """Maximum d'une fonction de deux variables (Nelder-Mead)."""
    P = [np.array(x0, float)] + [np.array(x0, float) + pas * np.eye(len(x0))[i] for i in range(len(x0))]
    F = [f(p) for p in P]
    for _ in range(tours):
        ordre = np.argsort(F)[::-1]
        P, F = [P[i] for i in ordre], [F[i] for i in ordre]
        if F[0] - F[-1] < tol:
            break
        c = sum(P[:-1]) / (len(P) - 1)
        r = c + (c - P[-1])
        fr = f(r)
        if fr > F[0]:
            x = c + 2 * (c - P[-1])
            fx = f(x)
            P[-1], F[-1] = (x, fx) if fx > fr else (r, fr)
        elif fr > F[-2]:
            P[-1], F[-1] = r, fr
        else:
            k = c + 0.5 * (P[-1] - c)
            fk = f(k)
            if fk > F[-1]:
                P[-1], F[-1] = k, fk
            else:
                P = [P[0]] + [P[0] + 0.5 * (p - P[0]) for p in P[1:]]
                F = [F[0]] + [f(p) for p in P[1:]]
    i = int(np.argmax(F))
    return P[i], F[i]


class Site:
    """Témoins et traités d'un site, âges en années. La vraisemblance est profilée sur a :
    pour b, θ et λ fixés, le meilleur a vaut (nombre de morts) / (exposition cumulée)."""

    def __init__(self, tc, dc, tt, dt, entree, debut):
        self.tc, self.tt, self.entree, self.debut = tc, tt, entree, debut
        self.n_c, self.n_t = len(tc), len(tt)
        self.morts = float(dc.sum() + dt.sum())
        self.morts_t = float(dt.sum())
        self.somme_c = float((dc * tc).sum())
        self.somme_t = float((dt * (tt - debut)).sum())

    def profil(self, b, ln_theta, ln_lambda):
        bt = b / math.exp(ln_lambda)
        kc = (np.exp(b * self.tc) - math.exp(b * self.entree)).sum() / b
        kt = math.exp(ln_theta + b * self.debut) * (
            np.exp(bt * (self.tt - self.debut)) - math.exp(bt * (self.entree - self.debut))).sum() / bt
        return (self.morts * math.log(self.morts / (kc + kt)) - self.morts + b * self.somme_c
                + self.morts_t * (ln_theta + b * self.debut) + bt * self.somme_t)

    def meilleur(self, ln_theta, ln_lambda):
        return maximum(lambda b: self.profil(b, ln_theta, ln_lambda), 0.3, 9.0)


def vraisemblance(sites, ln_theta, ln_lambda):
    return sum(s.meilleur(ln_theta, ln_lambda)[1] for s in sites)


def preparer(temoins, traites, debut_jours):
    """temoins, traites : listes de (site, mort, âge en jours). Rend les sites utilisables."""
    entree, debut = max(debut_jours, PLANCHER_JOURS) / AN, debut_jours / AN
    sites = []
    for site in SITES:
        c = [(t / AN, d) for (st, d, t) in temoins if st == site and t / AN > entree]
        x = [(t / AN, d) for (st, d, t) in traites if st == site and t / AN > entree]
        if len(c) < 20 or len(x) < 10:
            continue
        sites.append(Site(np.array([a for a, _ in c]), np.array([d for _, d in c], float),
                          np.array([a for a, _ in x]), np.array([d for _, d in x], float), entree, debut))
    return sites


def ajuster(sites):
    """Les quatre modèles. Rend les vraisemblances et les paramètres."""
    l0 = vraisemblance(sites, 0.0, 0.0)
    ln_theta_d, l_d = maximum(lambda v: vraisemblance(sites, v, 0.0), -3.0, 2.0, 1e-3)
    ln_lambda_r, l_r = maximum(lambda v: vraisemblance(sites, -v, v), -0.6, 1.2, 1e-3)
    x, l_g = simplexe(lambda v: vraisemblance(sites, v[0], v[1]), [ln_theta_d, 0.0])
    x2, l_g2 = simplexe(lambda v: vraisemblance(sites, v[0], v[1]), [-ln_lambda_r, ln_lambda_r])
    if l_g2 > l_g:
        x, l_g = x2, l_g2
    l_g = max(l_g, l_d, l_r)
    doublements = [math.log(2) / s.meilleur(0.0, 0.0)[0] * AN for s in sites]
    return {
        'n_traites': int(sum(s.n_t for s in sites)), 'n_temoins': int(sum(s.n_c for s in sites)),
        'morts_traites': int(sum(s.morts_t for s in sites)), 'sites': len(sites),
        'theta_retard': math.exp(ln_theta_d), 'lambda_ralentissement': math.exp(ln_lambda_r),
        'theta_general': math.exp(float(x[0])), 'lambda_general': math.exp(float(x[1])),
        'x2_effet': 2 * (l_g - l0), 'x2_retard_seul': 2 * (l_d - l0),
        'x2_retard_insuffisant': 2 * (l_g - l_d), 'x2_ralentissement_insuffisant': 2 * (l_g - l_r),
        'avantage_retard': l_d - l_r,
        'doublement_temoins_jours': float(np.mean(doublements)),
    }


def molecule(groupe):
    """La molécule d'un groupe, d'après les abréviations de la Mouse Phenome Database."""
    g = groupe.lower()
    for debut, nom in (('metrapa', 'rapamycine et metformine'), ('raac', 'rapamycine et acarbose'), ('rapa', 'rapamycine'),
                       ('aca', 'acarbose'), ('17ae2', '17-alpha-estradiol'), ('cana', 'canagliflozine'),
                       ('ndga', 'acide nordihydroguaïarétique'), ('nd_', 'acide nordihydroguaïarétique'),
                       ('oh-est', '16-alpha-hydroxyestriol')):
        if g.startswith(debut):
            return nom
    return groupe


def p_chi2_1(x):
    return math.erfc(math.sqrt(max(x, 0.0) / 2))


def p_chi2_2(x):
    return math.exp(-max(x, 0.0) / 2)


def quantile_km(ages, morts, entree, parts):
    """Âges auxquels une part donnée des souris présentes à l'entrée sont mortes (Kaplan-Meier)."""
    paires = sorted((t, d) for t, d in zip(ages, morts) if t > entree)
    n, survie, sortie, i = len(paires), 1.0, {}, 0
    restant = n
    while i < n:
        t = paires[i][0]
        j, d = i, 0
        while j < n and paires[j][0] == t:
            d += paires[j][1]
            j += 1
        if d:
            survie *= 1 - d / restant
            for p in parts:
                if p not in sortie and survie <= 1 - p + 1e-12:
                    sortie[p] = t
        restant -= j - i
        i = j
    return [sortie.get(p) for p in parts]


def tirer(rng, n, a, b, entree, debut=None, theta=1.0, lam=1.0):
    """Âges de mort simulés (années) sous le modèle, conditionnés à être en vie à l'entrée."""
    u = -np.log(rng.random(n))
    if debut is None:
        return np.log(np.exp(b * entree) + (b / a) * u) / b
    bt = b / lam
    return debut + np.log(np.exp(bt * (entree - debut)) + bt * u / (theta * a * math.exp(b * debut))) / bt


def simuler(graine, tours):
    """Simulations numériques : un retard pur, puis un ralentissement pur, d'ampleur voisine de la
    rapamycine, avec les effectifs d'une comparaison de l'ITP (3 sites, 97 témoins et 48 traités
    par site, suivis jusqu'à la mort). Ce ne sont pas des mesures."""
    rng = np.random.default_rng(graine)
    a, b, entree, debut = 0.004, 2.2, 1.0, 0.75
    sortie = {}
    for nom, theta, lam in (('retard', 0.45, 1.0), ('ralentissement', 1 / 1.22, 1.22)):
        lambdas, rejets_retard, rejets_ralent = [], 0, 0
        for _ in range(tours):
            sites = []
            for _site in range(3):
                tc = tirer(rng, 97, a, b, entree)
                tt = tirer(rng, 48, a, b, entree, debut, theta, lam)
                sites.append(Site(tc, np.ones(97), tt, np.ones(48), entree, debut))
            r = ajuster(sites)
            lambdas.append(r['lambda_general'])
            rejets_retard += r['x2_retard_insuffisant'] > 3.841
            rejets_ralent += r['x2_ralentissement_insuffisant'] > 3.841
        sortie[nom] = {
            'theta_vrai': theta, 'lambda_vrai': lam, 'tours': tours,
            'lambda_estime_median': float(np.median(lambdas)),
            'lambda_estime_centiles_2_5_97_5': [float(np.percentile(lambdas, 2.5)), float(np.percentile(lambdas, 97.5))],
            'part_rejets_du_retard': rejets_retard / tours,
            'part_rejets_du_ralentissement': rejets_ralent / tours,
        }
    return sortie


def analyser(souris, tours=150):
    par = collections.defaultdict(list)
    for (cohorte, site, sexe, groupe, debut, mort, age) in souris:
        par[(cohorte, sexe, groupe)].append((site, mort, age, debut))

    # 6. Lecture des données : Harrison et al. 2009, rapamycine à 600 jours (cohorte 2005).
    controle = {}
    for sexe, publie in (('f', 14), ('m', 9)):
        t = par[('C2005', sexe, 'Rapa')]
        c = par[('C2005', sexe, 'Control')]
        qt = quantile_km([x[2] for x in t], [x[1] for x in t], 0.0, [0.9])[0]
        qc = quantile_km([x[2] for x in c], [x[1] for x in c], 0.0, [0.9])[0]
        controle[sexe] = {'age_90_temoins_jours': qc, 'age_90_traites_jours': qt,
                          'gain_pourcent': 100 * (qt / qc - 1), 'publie_pourcent': publie}

    # 1 et 2. Toutes les comparaisons.
    comparaisons = []
    for (cohorte, sexe, groupe), v in sorted(par.items()):
        if groupe == 'Control':
            continue
        debut_mois = v[0][3]
        temoins = [(s, d, t) for (s, d, t, _) in par[(cohorte, sexe, 'Control')]]
        traites = [(s, d, t) for (s, d, t, _) in v]
        sites = preparer(temoins, traites, debut_mois * MOIS)
        if not sites:
            continue
        r = ajuster(sites)
        entree = max(debut_mois * MOIS, PLANCHER_JOURS)
        qc = quantile_km([t for _, _, t in temoins], [d for _, d, _ in temoins], entree, [0.5, 0.9])
        qt = quantile_km([t for _, _, t in traites], [d for _, d, _ in traites], entree, [0.5, 0.9])
        r.update(cohorte=cohorte, sexe=sexe, groupe=groupe, debut_mois=debut_mois,
                 p_effet=p_chi2_2(r['x2_effet']), p_retard_seul=p_chi2_1(r['x2_retard_seul']),
                 mediane_temoins_jours=qc[0], mediane_traites_jours=qt[0],
                 age_90_temoins_jours=qc[1], age_90_traites_jours=qt[1])
        comparaisons.append(r)
    n = len(comparaisons)

    # 3. Étalonnage sur les comparaisons sans effet (test du retard seul : p > 0,2).
    nuls = [r for r in comparaisons if r['p_retard_seul'] > 0.2]
    stat_nuls = sorted(r['x2_retard_insuffisant'] for r in nuls)
    seuil = float(np.percentile(stat_nuls, 95))
    etalonnage = {
        'n_sans_effet': len(nuls),
        'part_rejets_au_seuil_theorique': sum(x > 3.841 for x in stat_nuls) / len(nuls),
        'seuil_theorique': 3.841, 'seuil_corrige': seuil,
        'lambda_median': float(np.median([r['lambda_general'] for r in nuls])),
        'part_lambda_inferieur_a_1': sum(r['lambda_general'] < 1 for r in nuls) / len(nuls),
    }

    # Les traitements qui allongent la vie.
    efficaces = [r for r in comparaisons if r['p_effet'] < 0.05 / n and r['theta_retard'] < 1]
    for r in efficaces:
        r['gain_mediane_jours'] = r['mediane_traites_jours'] - r['mediane_temoins_jours']
        r['gain_90_jours'] = r['age_90_traites_jours'] - r['age_90_temoins_jours']
    # Moyenne de ln λ par cohorte et sexe (les groupes d'une cohorte partagent leurs témoins).
    grappes = collections.defaultdict(list)
    for r in efficaces:
        grappes[(r['cohorte'], r['sexe'])].append(math.log(r['lambda_general']))
    moyennes = np.array([np.mean(v) for v in grappes.values()])
    m, k = float(moyennes.mean()), len(moyennes)
    demi = T975[min(k - 1, 30)] * float(moyennes.std(ddof=1)) / math.sqrt(k)
    gains_med = [r['gain_mediane_jours'] for r in efficaces]
    gains_90 = [r['gain_90_jours'] for r in efficaces]
    resume = {
        'n': len(efficaces), 'n_cohortes_sexes': k,
        'n_ralentissement_rejete_theorique': sum(r['x2_ralentissement_insuffisant'] > 3.841 for r in efficaces),
        'n_ralentissement_rejete_corrige': sum(r['x2_ralentissement_insuffisant'] > seuil for r in efficaces),
        'n_retard_rejete_theorique': sum(r['x2_retard_insuffisant'] > 3.841 for r in efficaces),
        'n_retard_rejete_corrige': sum(r['x2_retard_insuffisant'] > seuil for r in efficaces),
        'n_lambda_superieur_a_1': sum(r['lambda_general'] > 1 for r in efficaces),
        'n_doublement_allonge_etabli': sum(r['lambda_general'] > 1 and r['x2_retard_insuffisant'] > seuil for r in efficaces),
        'n_doublement_raccourci_etabli': sum(r['lambda_general'] < 1 and r['x2_retard_insuffisant'] > seuil for r in efficaces),
        'n_retard_mieux_ajuste': sum(r['avantage_retard'] > 0 for r in efficaces),
        'lambda_median': float(np.median([r['lambda_general'] for r in efficaces])),
        'lambda_moyen': math.exp(m), 'lambda_moyen_ic95': [math.exp(m - demi), math.exp(m + demi)],
        'doublement_raccourci_pourcent': 100 * (1 - math.exp(m)),
        'doublement_raccourci_pourcent_ic95': [100 * (1 - math.exp(m + demi)), 100 * (1 - math.exp(m - demi))],
        'par_molecule': dict(collections.Counter(molecule(r['groupe']) for r in efficaces)),
        'lambda_si_ralentissement_median': float(np.median([r['lambda_ralentissement'] for r in efficaces])),
        'lambda_si_ralentissement_min': min(r['lambda_ralentissement'] for r in efficaces),
        'lambda_si_ralentissement_max': max(r['lambda_ralentissement'] for r in efficaces),
        'gain_mediane_jours_median': float(np.median(gains_med)),
        'gain_90_jours_median': float(np.median(gains_90)),
        'n_gain_90_inferieur_au_gain_mediane': sum(b < a for a, b in zip(gains_med, gains_90)),
        'doublement_temoins_jours_median': float(np.median([r['doublement_temoins_jours'] for r in efficaces])),
    }
    morts = sum(s[5] for s in souris)
    return {
        'donnees': {
            'souris': len(souris), 'mortes': morts, 'retirees': len(souris) - morts,
            'cohortes': len({s[0] for s in souris}), 'groupes_traites': len({(s[0], s[3]) for s in souris if s[3] != 'Control'}),
            'comparaisons': n, 'seuil_bonferroni': 0.05 / n, 'plancher_jours': PLANCHER_JOURS,
        },
        'controle_publication': controle,
        'etalonnage': etalonnage,
        'efficaces': resume,
        'liste_efficaces': sorted(efficaces, key=lambda r: r['p_effet']),
        'simulations': simuler(20261120, tours),
        'comparaisons': comparaisons,
    }


def autotests(r):
    c = r['controle_publication']
    assert abs(c['f']['gain_pourcent'] - 14) < 2 and abs(c['m']['gain_pourcent'] - 9) < 2, c
    s = r['simulations']
    assert abs(s['retard']['lambda_estime_median'] - 1.0) < 0.06, s['retard']
    assert abs(s['ralentissement']['lambda_estime_median'] - 1.22) < 0.08, s['ralentissement']
    assert s['retard']['part_rejets_du_retard'] < 0.12, s['retard']
    assert s['ralentissement']['part_rejets_du_ralentissement'] < 0.12, s['ralentissement']
    d = r['donnees']
    assert d['souris'] == d['mortes'] + d['retirees'] and d['comparaisons'] > 150
    e = r['efficaces']
    # Les décomptes écrits dans l'article (site/langues) : s'ils changent, le texte doit changer.
    assert e['par_molecule'] == {'rapamycine': 11, 'rapamycine et acarbose': 4, 'rapamycine et metformine': 2, 'acarbose': 5,
                                 '17-alpha-estradiol': 2, 'canagliflozine': 1, 'acide nordihydroguaïarétique': 1,
                                 '16-alpha-hydroxyestriol': 1}, e['par_molecule']
    assert e['n_doublement_allonge_etabli'] == 0 and e['n_doublement_raccourci_etabli'] == e['n_retard_rejete_corrige']
    assert e['n'] == len(r['liste_efficaces']) and e['lambda_moyen_ic95'][0] < e['lambda_moyen'] < e['lambda_moyen_ic95'][1]


def arrondir(x):
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return float(f'{float(x):.6g}')
    if isinstance(x, dict):
        return {k: arrondir(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [arrondir(v) for v in x]
    return x


if __name__ == '__main__':
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--out', default=str(ICI / 'resultats.json'))
    arguments.add_argument('--tours', type=int, default=150)
    options = arguments.parse_args()
    resultats = analyser(lire(ICI / 'donnees' / 'itp-survie.csv'), options.tours)
    autotests(resultats)
    Path(options.out).write_text(json.dumps(arrondir(resultats), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    e, t = resultats['efficaces'], resultats['etalonnage']
    print(f"{resultats['donnees']['souris']} souris, {resultats['donnees']['comparaisons']} comparaisons, {e['n']} traitements efficaces")
    print(f"ralentissement rejeté : {e['n_ralentissement_rejete_corrige']} ; retard rejeté : {e['n_retard_rejete_corrige']} (seuil corrigé {t['seuil_corrige']:.2f})")
    print(f"λ moyen {e['lambda_moyen']:.3f} [{e['lambda_moyen_ic95'][0]:.3f} ; {e['lambda_moyen_ic95'][1]:.3f}] ; autotests réussis")
