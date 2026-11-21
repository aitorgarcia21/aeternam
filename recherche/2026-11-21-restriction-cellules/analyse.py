#!/usr/bin/env python3
"""Ce que la restriction calorique change dans les cellules du sang, et ce qui annonce la survie.

Applique `plan.md`, enregistré dans Git avant tout calcul lié à la survie (commit bcf792f).
Données : les 937 souris femelles Diversity Outbred de Di Francesco et al. (Nature 2024),
fichier `phenotyping_data.csv` publié par Calico (licence MIT), inchangé.

Pour chaque mesure de la famille principale (numération sanguine vers 343 jours, cytométrie des
cellules immunitaires vers 490 jours) :
  - test 1 : l'effet de la dose de restriction (0 ; 0,2 ; 0,4) sur la mesure, chez les souris
    nourries à volonté ou restreintes, à âge et génération égaux ;
  - test 2 : le lien entre la mesure et la mort qui suit, à régime et génération égaux (modèle
    de Cox, troncature à gauche à l'âge de la mesure) ;
  - correction de Benjamini-Hochberg sur la famille, pour chaque test ;
  - candidate : q < 0,05 aux deux tests, et la restriction déplace la mesure du côté où le
    risque est plus bas.
Puis, pour les candidates : la part de l'effet de la restriction de 40 % qu'elles portent (Cox),
le temps de doublement du risque avant et après les avoir prises en compte (Gompertz), le test 2
refait avec le poids, et la variation de chaque souris entre deux mesures (le rythme).
Le même test 1 sur les mesures prises avant les régimes sert de témoin négatif.

Python >= 3.9 et numpy. Usage : python3 analyse.py --out resultats.json
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import NormalDist

import numpy as np

ICI = Path(__file__).resolve().parent
FICHIER = ICI / 'donnees' / 'phenotyping_data.csv'
EMPREINTE = '23c2089128ab6a514bd1bf12fa1898d3a38900c162a2eed599e08f1ad1d7bde1'
AN = 365.25
DEBUT_REGIME = 6 * 30.4375 / AN          # les régimes commencent à 6 mois
PLANCHER = 365.0 / AN                    # entrée dans le modèle de Gompertz : au plus tôt 365 jours
DOSES = {'AL': 0.0, '20': 0.2, '40': 0.4}
REGIMES = ('1D', '2D', '20', '40')       # indicatrices du modèle de Cox ; AL est la référence
PRINCIPALE = ('Y1_CBC_', 'Y2_FLOW_')
SUIVANTE = {'Y1_CBC_': 'Y2_CBC_', 'Y2_FLOW_': 'Y3_FLOW_'}
SECONDAIRE = ('Y1_Echo_', 'Y1_PIXI_', 'Y1_Rotarod_', 'Y1_Void_', 'Y1_Wheel_', 'Y1_AS_', 'Y1B_Frailty_',
              'Y1B_Grip_', 'Y1D_BW_', 'Y2_Glu.F_', 'Y2_Glu.NF_', 'Y2_MetCage_')
TEMOIN = ('Y1_FLOW_', 'Y1_Glu.F_', 'Y1_Glu.NF_', 'Y1_MetCage_', 'Y1A_Frailty_', 'Y1A_Grip_', 'Y1A_BW_')
MIN_SOURIS, MIN_VALEURS = 300, 10
Q = 0.05
NORMALE = NormalDist()


# ---------------------------------------------------------------- lecture

def nombre(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def lire():
    if hashlib.sha256(FICHIER.read_bytes()).hexdigest() != EMPREINTE:
        raise ValueError('donnees/phenotyping_data.csv a changé : empreinte différente.')
    with open(FICHIER, encoding='utf-8') as f:
        lignes = list(csv.DictReader(f))
    colonnes = list(lignes[0].keys())
    return lignes, colonnes


def mesures_de(prefixe, colonnes):
    return [c for c in colonnes if c.startswith(prefixe) and not c.endswith(('AgeInDays', 'BWTest'))]


# ---------------------------------------------------------------- outils statistiques

def p_normale(z):
    return math.erfc(abs(z) / math.sqrt(2))


def rangs_normaux(x):
    """Transformation inverse normale des rangs (Blom), rangs moyens pour les ex aequo."""
    x = np.asarray(x, float)
    n = len(x)
    valeurs, inverse, nombres = np.unique(x, return_inverse=True, return_counts=True)
    fin = np.cumsum(nombres)
    moyen = fin - (nombres - 1) / 2.0
    r = moyen[inverse]
    return np.array([NORMALE.inv_cdf((ri - 0.375) / (n + 0.25)) for ri in r])


def benjamini_hochberg(p):
    p = np.asarray(p, float)
    n = len(p)
    ordre = np.argsort(p)
    q = np.empty(n)
    mini = 1.0
    for rang in range(n - 1, -1, -1):
        i = ordre[rang]
        mini = min(mini, p[i] * n / (rang + 1))
        q[i] = mini
    return q


def moindres_carres(y, X):
    """Coefficients, erreurs-types et z de la régression linéaire y = Xb."""
    XtX = X.T @ X
    b = np.linalg.solve(XtX, X.T @ y)
    r = y - X @ b
    s2 = float(r @ r) / (len(y) - X.shape[1])
    se = np.sqrt(np.diag(np.linalg.inv(XtX)) * s2)
    return b, se, b / se


def cox(entree, sortie, mort, X, iterations=60):
    """Modèle de Cox avec troncature à gauche (à risque si entrée < t <= sortie), ex aequo de
    Breslow, Newton-Raphson avec demi-pas. Rend (coefficients, erreurs-types, log-vraisemblance)."""
    entree, sortie, mort = (np.asarray(v, float) for v in (entree, sortie, mort))
    X = np.asarray(X, float)
    n, p = X.shape
    temps = np.unique(sortie[mort > 0])
    R = ((entree[None, :] < temps[:, None]) & (sortie[None, :] >= temps[:, None])).astype(float)
    D = (sortie[None, :] == temps[:, None]) & (mort[None, :] > 0)
    d = D.sum(axis=1).astype(float)
    somme_morts = D.astype(float) @ X
    XX = (X[:, :, None] * X[:, None, :]).reshape(n, p * p)

    def evaluer(b):
        eta = X @ b
        c = eta.max()
        w = np.exp(eta - c)
        S0 = R @ w
        S1 = R @ (w[:, None] * X)
        ll = float((somme_morts @ b).sum() - (d * (np.log(S0) + c)).sum())
        g = (somme_morts - d[:, None] * S1 / S0[:, None]).sum(axis=0)
        S2 = (R @ (w[:, None] * XX)).reshape(-1, p, p)
        m = S1 / S0[:, None]
        H = -(d[:, None, None] * (S2 / S0[:, None, None] - m[:, :, None] * m[:, None, :])).sum(axis=0)
        return ll, g, H

    b = np.zeros(p)
    ll, g, H = evaluer(b)
    for _ in range(iterations):
        pas = np.linalg.solve(H, -g)
        t = 1.0
        while True:
            ll2, g2, H2 = evaluer(b + t * pas)
            if ll2 >= ll - 1e-12 or t < 1e-6:
                break
            t /= 2
        fini = abs(ll2 - ll) < 1e-10
        b, ll, g, H = b + t * pas, ll2, g2, H2
        if fini:
            break
    se = np.sqrt(np.diag(np.linalg.inv(-H)))
    return b, se, ll


def nelder_mead(f, x0, pas=0.3, iterations=8000, tol=1e-10):
    """Minimum d'une fonction de n variables (Nelder-Mead adaptatif, Gao et Han 2012)."""
    n = len(x0)
    al, ga, rh, si = 1.0, 1 + 2 / n, 0.75 - 1 / (2 * n), 1 - 1 / n
    P = [np.array(x0, float)] + [np.array(x0, float) + pas * np.eye(n)[i] for i in range(n)]
    F = [f(x) for x in P]
    for _ in range(iterations):
        ordre = np.argsort(F)
        P, F = [P[i] for i in ordre], [F[i] for i in ordre]
        if abs(F[-1] - F[0]) < tol and max(np.abs(x - P[0]).max() for x in P) < 1e-8:
            break
        c = sum(P[:-1]) / n
        r = c + al * (c - P[-1])
        fr = f(r)
        if F[0] <= fr < F[-2]:
            P[-1], F[-1] = r, fr
        elif fr < F[0]:
            x = c + ga * (r - c)
            fx = f(x)
            P[-1], F[-1] = (x, fx) if fx < fr else (r, fr)
        else:
            k = c + rh * ((r if fr < F[-1] else P[-1]) - c)
            fk = f(k)
            if fk < min(fr, F[-1]):
                P[-1], F[-1] = k, fk
            else:
                P = [P[0]] + [P[0] + si * (x - P[0]) for x in P[1:]]
                F = [F[0]] + [f(x) for x in P[1:]]
    i = int(np.argmin(F))
    return P[i], F[i]


def minimiser(f, x0):
    x, fx = nelder_mead(f, x0)
    for pas in (0.1, 0.03, 0.01):
        x2, f2 = nelder_mead(f, x, pas=pas)
        if f2 < fx - 1e-9:
            x, fx = x2, f2
    return x, fx


def gompertz_lambda(entree, sortie, mort, traite, Z):
    """Modèle général de la piste restriction (retard θ et ralentissement λ à partir de 6 mois),
    entrées individuelles, risque multiplié par exp(Z·β). Rend λ, θ et β."""
    entree, sortie, mort, traite = (np.asarray(v, float) for v in (entree, sortie, mort, traite))
    Z = np.asarray(Z, float).reshape(len(sortie), -1)
    k = Z.shape[1]
    s = DEBUT_REGIME

    def moins_ll(x):
        ln_a, ln_b, ln_t, ln_l = x[:4]
        beta = x[4:]
        if not (-15 < ln_a < 2 and -3 < ln_b < 3 and abs(ln_t) < 6 and abs(ln_l) < 2.5):
            return 1e12
        a, b = math.exp(ln_a), math.exp(ln_b)
        bt = b / math.exp(ln_l)
        kk = math.exp(ln_t) * a * math.exp(b * s)
        H0 = lambda t: (a / b) * np.expm1(b * t)
        H1 = lambda t: (a / b) * math.expm1(b * s) + kk * np.expm1(bt * (t - s)) / bt
        log_h = np.where(traite > 0, ln_t + ln_a + b * s + bt * (sortie - s), ln_a + b * sortie)
        Hs = np.where(traite > 0, H1(sortie), H0(sortie))
        He = np.where(traite > 0, H1(entree), H0(entree))
        eta = Z @ beta if k else np.zeros(len(sortie))
        ll = float((mort * (log_h + eta)).sum() - (np.exp(eta) * (Hs - He)).sum())
        return -ll if math.isfinite(ll) else 1e12

    x, _ = minimiser(moins_ll, [-5.0, 0.5, 0.0, 0.0] + [0.0] * k)
    return {'lambda': math.exp(x[3]), 'theta': math.exp(x[2]), 'beta': [float(v) for v in x[4:]]}


# ---------------------------------------------------------------- l'analyse

def preparer_serie(lignes, prefixe, mesure):
    """Les souris qui ont la mesure : valeur, âge (années), poids, régime, génération, survie."""
    out = []
    for r in lignes:
        v, age = nombre(r[mesure]), nombre(r.get(prefixe + 'AgeInDays'))
        t = nombre(r['SurvDays'])
        if v is None or age is None or t is None or t <= age:
            continue
        out.append({'v': v, 'age': age / AN, 'poids': nombre(r.get(prefixe + 'BWTest')), 'regime': r['Diet'],
                    'generation': r['Generation'], 'sortie': t / AN, 'mort': 1.0 if r['Died'] == 'TRUE' else 0.0,
                    'id': r['MouseID']})
    return out


def generations(lignes):
    return sorted({r['Generation'] for r in lignes})


def indicatrices(valeurs, niveaux):
    return np.array([[1.0 if v == n else 0.0 for n in niveaux] for v in valeurs]).reshape(len(valeurs), len(niveaux))


def strates(valeurs):
    """Indicatrices des générations présentes, la première servant de référence : une génération
    sans souris mesurée n'a pas de coefficient (certaines mesures manquent dans des générations)."""
    presentes = sorted(set(valeurs))
    return indicatrices(valeurs, presentes[1:])


def test_regime(souris, gens, ajout=None):
    """Test 1 : effet de la dose de restriction (souris AL, 20, 40). `ajout` : une covariable de
    plus par souris (dictionnaire identifiant -> valeur), pour les contrôles de robustesse."""
    s = [x for x in souris if x['regime'] in DOSES and (ajout is None or ajout.get(x['id']) is not None)]
    if len(s) < MIN_SOURIS // 2:
        return None
    y = rangs_normaux([x['v'] for x in s])
    age = np.array([x['age'] for x in s])
    colonnes = [np.ones(len(s)), [DOSES[x['regime']] for x in s], age - age.mean()]
    if ajout is not None:
        colonnes.append(rangs_normaux([ajout[x['id']] for x in s]))
    X = np.column_stack(colonnes + [strates([x['generation'] for x in s])])
    b, se, z = moindres_carres(y, X)
    return {'n': len(s), 'dose_coef': float(b[1]), 'dose_z': float(z[1]), 'p': p_normale(z[1])}


def colonne_par_souris(lignes, colonne):
    return {r['MouseID']: nombre(r.get(colonne)) for r in lignes}


def matrice_cox(s, gens, avec_mesure=True, poids=False):
    colonnes = []
    if avec_mesure:
        colonnes.append(rangs_normaux([x['v'] for x in s]))
    if poids:
        pw = np.array([x['poids'] for x in s], float)
        colonnes.append((pw - pw.mean()) / pw.std())
    colonnes.append(indicatrices([x['regime'] for x in s], REGIMES))
    colonnes.append(strates([x['generation'] for x in s]))
    return np.column_stack(colonnes)


def test_survie(souris, gens, poids=False):
    """Test 2 : lien entre la mesure et la mort qui suit, à régime et génération égaux."""
    s = [x for x in souris if (x['poids'] is not None or not poids)]
    X = matrice_cox(s, gens, True, poids)
    b, se, _ = cox([x['age'] for x in s], [x['sortie'] for x in s], [x['mort'] for x in s], X)
    z = b[0] / se[0]
    return {'n': len(s), 'morts': int(sum(x['mort'] for x in s)), 'log_hr': float(b[0]), 'hr_par_ecart_type': math.exp(b[0]),
            'z': float(z), 'p': p_normale(z)}


def famille(lignes, colonnes, prefixes, gens, survie=True):
    sortie = []
    for prefixe in prefixes:
        for m in mesures_de(prefixe, colonnes):
            souris = preparer_serie(lignes, prefixe, m)
            if len(souris) < MIN_SOURIS or len({x['v'] for x in souris}) < MIN_VALEURS:
                continue
            t1 = test_regime(souris, gens)
            if t1 is None:
                continue
            entree = {'serie': prefixe, 'mesure': m, 'n': len(souris),
                      'age_median_jours': float(np.median([x['age'] for x in souris]) * AN), 'test1': t1}
            if survie:
                entree['test2'] = test_survie(souris, gens)
            sortie.append(entree)
    q1 = benjamini_hochberg([e['test1']['p'] for e in sortie])
    for e, q in zip(sortie, q1):
        e['test1']['q'] = float(q)
    if survie:
        q2 = benjamini_hochberg([e['test2']['p'] for e in sortie])
        for e, q in zip(sortie, q2):
            e['test2']['q'] = float(q)
            e['candidate'] = bool(e['test1']['q'] < Q and q < Q
                                  and e['test1']['dose_coef'] * e['test2']['log_hr'] < 0)
    return sortie


def part_expliquee(lignes, gens, e):
    """Le coefficient de Cox de la restriction de 40 % sans puis avec la mesure (mêmes souris)."""
    s = preparer_serie(lignes, e['serie'], e['mesure'])
    args = ([x['age'] for x in s], [x['sortie'] for x in s], [x['mort'] for x in s])
    i40 = 1 + REGIMES.index('40')
    sans, _, _ = cox(*args, matrice_cox(s, gens, False))
    avec, _, _ = cox(*args, matrice_cox(s, gens, True))
    b_sans, b_avec = float(sans[i40 - 1]), float(avec[i40])
    return {'log_hr_40_sans': b_sans, 'log_hr_40_avec': b_avec, 'part_expliquee': 1 - b_avec / b_sans}


def pente(lignes, serie, candidates):
    """λ (restriction de 40 % contre volonté) sans puis avec les candidates d'une série."""
    souris = []
    for r in lignes:
        if r['Diet'] not in ('AL', '40'):
            continue
        age = nombre(r.get(serie + 'AgeInDays'))
        valeurs = [nombre(r[m]) for m in candidates]
        t = nombre(r['SurvDays'])
        if age is None or t is None or any(v is None for v in valeurs):
            continue
        e = max(PLANCHER, age / AN)
        if t / AN <= e:
            continue
        souris.append((e, t / AN, 1.0 if r['Died'] == 'TRUE' else 0.0, 1.0 if r['Diet'] == '40' else 0.0, valeurs))
    entree, sortie_, mort, traite = (np.array([x[i] for x in souris]) for i in range(4))
    Z = np.column_stack([rangs_normaux([x[4][j] for x in souris]) for j in range(len(candidates))])
    sans = gompertz_lambda(entree, sortie_, mort, traite, np.zeros((len(souris), 0)))
    avec = gompertz_lambda(entree, sortie_, mort, traite, Z)
    return {'serie': serie, 'mesures': list(candidates), 'souris': len(souris),
            'lambda_sans': sans['lambda'], 'lambda_avec': avec['lambda'], 'theta_sans': sans['theta'],
            'theta_avec': avec['theta'], 'beta': avec['beta']}


def pente_score(lignes, gens, serie, candidates):
    """Robustesse : les candidates résumées en un seul score (prédicteur linéaire d'un modèle de Cox
    à régime et génération égaux), puis λ sans et avec ce score."""
    souris = []
    for r in lignes:
        age = nombre(r.get(serie + 'AgeInDays'))
        valeurs = [nombre(r[m]) for m in candidates]
        t = nombre(r['SurvDays'])
        if age is None or t is None or t <= age or any(v is None for v in valeurs):
            continue
        souris.append({'age': age / AN, 'sortie': t / AN, 'mort': 1.0 if r['Died'] == 'TRUE' else 0.0,
                       'regime': r['Diet'], 'generation': r['Generation'], 'valeurs': valeurs})
    Z = np.column_stack([rangs_normaux([x['valeurs'][j] for x in souris]) for j in range(len(candidates))])
    X = np.column_stack([Z, indicatrices([x['regime'] for x in souris], REGIMES), strates([x['generation'] for x in souris])])
    b, _, _ = cox([x['age'] for x in souris], [x['sortie'] for x in souris], [x['mort'] for x in souris], X)
    score = Z @ b[:len(candidates)]
    garde = [i for i, x in enumerate(souris) if x['regime'] in ('AL', '40') and x['sortie'] > max(PLANCHER, x['age'])]
    entree = np.array([max(PLANCHER, souris[i]['age']) for i in garde])
    sortie_ = np.array([souris[i]['sortie'] for i in garde])
    mort = np.array([souris[i]['mort'] for i in garde])
    traite = np.array([1.0 if souris[i]['regime'] == '40' else 0.0 for i in garde])
    sc = score[garde]
    sc = (sc - sc.mean()) / sc.std()
    sans = gompertz_lambda(entree, sortie_, mort, traite, np.zeros((len(garde), 0)))
    avec = gompertz_lambda(entree, sortie_, mort, traite, sc[:, None])
    return {'serie': serie, 'souris': len(garde), 'lambda_sans': sans['lambda'], 'lambda_avec': avec['lambda'],
            'theta_sans': sans['theta'], 'theta_avec': avec['theta'], 'beta_score': avec['beta'][0]}


def rythme(lignes, gens, e):
    """Variation de chaque souris entre la première et la seconde série de mesures."""
    serie2 = SUIVANTE[e['serie']]
    m2 = serie2 + e['mesure'][len(e['serie']):]
    s = []
    for r in lignes:
        v1, v2 = nombre(r[e['mesure']]), nombre(r.get(m2))
        if v1 is None or v2 is None or r['Diet'] not in DOSES:
            continue
        s.append((v2 - v1, r['Diet'], r['Generation']))
    if len(s) < 60:
        return None
    delta = np.array([x[0] for x in s])
    al = delta[[x[1] == 'AL' for x in s]]
    z_al = float(al.mean() / (al.std(ddof=1) / math.sqrt(len(al))))
    X = np.column_stack([np.ones(len(s)), [DOSES[x[1]] for x in s], strates([x[2] for x in s])])
    b, se, z = moindres_carres(rangs_normaux(delta), X)
    return {'souris': len(s), 'variation_moyenne_volonte': float(al.mean()), 'z_variation_volonte': z_al,
            'dose_coef_variation': float(b[1]), 'dose_z_variation': float(z[1]), 'p_dose_variation': p_normale(z[1])}


def temoin(lignes, colonnes, gens):
    resultats = famille(lignes, colonnes, TEMOIN, gens, survie=False)
    p = np.array([e['test1']['p'] for e in resultats])
    z = np.array([e['test1']['dose_z'] for e in resultats])
    poids3 = [e for e in resultats if e['mesure'] == 'Y1A_BW_BW']
    return {'mesures': len(resultats), 'part_p_inferieur_0_05': float((p < 0.05).mean()),
            'decouvertes_q_0_05': int(sum(e['test1']['q'] < Q for e in resultats)),
            'inflation': float(np.median(z ** 2) / 0.454936),
            'quantile_95_abs_z': float(np.quantile(np.abs(z), 0.95)),
            'poids_3_mois_z': poids3[0]['test1']['dose_z'] if poids3 else None,
            'liste': resultats}


def etalonner(entrees, inflation):
    """Écart au plan, déclaré : le témoin négatif montre que le test 1 rejette trop souvent. Ses z
    sont divisés par la racine du facteur d'inflation mesuré sur ce témoin (médiane de z² rapportée
    à celle d'une loi du khi-deux à 1 degré, 0,4549), puis corrigés par Benjamini-Hochberg."""
    for e in entrees:
        z = e['test1']['dose_z'] / math.sqrt(inflation)
        e['test1']['z_etalonne'] = z
        e['test1']['p_etalonne'] = p_normale(z)
    q = benjamini_hochberg([e['test1']['p_etalonne'] for e in entrees])
    for e, qi in zip(entrees, q):
        e['test1']['q_etalonne'] = float(qi)
        e['candidate_etalonnee'] = bool(qi < Q and e['test2']['q'] < Q and e['test1']['dose_coef'] * e['test2']['log_hr'] < 0)


def resumer(entrees):
    return {'mesures': len(entrees),
            'changees_par_la_restriction': int(sum(e['test1']['q'] < Q for e in entrees)),
            'changees_apres_etalonnage': int(sum(e['test1']['q_etalonne'] < Q for e in entrees)),
            'liees_a_la_survie': int(sum(e['test2']['q'] < Q for e in entrees)),
            'candidates': [e['mesure'] for e in entrees if e['candidate']],
            'candidates_etalonnees': [e['mesure'] for e in entrees if e['candidate_etalonnee']],
            'n_candidates': int(sum(e['candidate'] for e in entrees)),
            'n_candidates_etalonnees': int(sum(e['candidate_etalonnee'] for e in entrees))}


def analyser(lignes, colonnes):
    gens = generations(lignes)
    negatif = temoin(lignes, colonnes, gens)
    principale = famille(lignes, colonnes, PRINCIPALE, gens)
    secondaire = famille(lignes, colonnes, SECONDAIRE, gens)
    for f in (principale, secondaire):
        etalonner(f, negatif['inflation'])
    poids3 = colonne_par_souris(lignes, 'Y1A_BW_BW')
    candidates = [e for e in principale if e['candidate']]
    for e in candidates:
        e['part_expliquee'] = part_expliquee(lignes, gens, e)
        s = preparer_serie(lignes, e['serie'], e['mesure'])
        e['test2_avec_poids'] = test_survie(s, gens, poids=True)
        e['rythme'] = rythme(lignes, gens, e)
        # Robustesse (après le plan) : le test 1 avec le poids à 3 mois, mesuré avant les régimes ;
        # pour la cytométrie, avec la même mesure prise à 155 jours, avant les régimes.
        e['test1_avec_poids_3_mois'] = test_regime(s, gens, poids3)
        if e['serie'] == 'Y2_FLOW_':
            base = colonne_par_souris(lignes, 'Y1_FLOW_' + e['mesure'][len('Y2_FLOW_'):])
            e['test1_avec_mesure_avant_regime'] = test_regime(s, gens, base)
    pentes, pentes_etalonnees, scores = [], [], []
    for serie in PRINCIPALE:
        noms = [e['mesure'] for e in candidates if e['serie'] == serie]
        if noms:
            pentes.append(pente(lignes, serie, noms))
            scores.append(pente_score(lignes, gens, serie, noms))
        noms_e = [e['mesure'] for e in principale if e['serie'] == serie and e['candidate_etalonnee']]
        if noms_e and noms_e != noms:
            pentes_etalonnees.append(pente(lignes, serie, noms_e))
    parts = [e['part_expliquee']['part_expliquee'] for e in candidates]
    rapports = [e['test2']['hr_par_ecart_type'] for e in candidates]
    avec_rythme = [e for e in candidates if e.get('rythme')]
    vieillit = [e for e in avec_rythme if abs(e['rythme']['z_variation_volonte']) > 1.96]
    return {
        'donnees': {'souris': len(lignes), 'generations': gens},
        'temoin_negatif': negatif,
        'principale': {'resume': resumer(principale), 'liste': principale,
                       'part_expliquee_min': min(parts), 'part_expliquee_max': max(parts),
                       'risque_par_ecart_type_min': min(rapports), 'risque_par_ecart_type_max': max(rapports)},
        'pentes': pentes,
        'pentes_candidates_etalonnees': pentes_etalonnees,
        'pentes_score': scores,
        'rythme': {
            'candidates_suivies': len(avec_rythme),
            'n_qui_changent': len(vieillit),
            'n_sens_frein': sum(e['rythme']['dose_z_variation'] * e['rythme']['z_variation_volonte'] < 0 for e in vieillit),
            'qui_changent_avec_l_age_chez_les_souris_a_volonte': [e['mesure'] for e in vieillit],
            'dont_la_restriction_freine_le_changement_nominal': [
                e['mesure'] for e in vieillit
                if e['rythme']['dose_z_variation'] * e['rythme']['z_variation_volonte'] < 0
                and abs(e['rythme']['dose_z_variation']) > 1.96],
            'dont_le_sens_est_celui_d_un_frein': [
                e['mesure'] for e in vieillit if e['rythme']['dose_z_variation'] * e['rythme']['z_variation_volonte'] < 0],
            # Souris à mesurer deux fois pour voir, avec 90 % de chances (test bilatéral à 5 %), un
            # effet de la dose sur la variation de la taille de celui observé : n·((1,96 + 1,28)/z)².
            'souris_pour_90_pourcent': {
                e['mesure']: math.ceil(e['rythme']['souris'] * ((1.959964 + 1.281552) / e['rythme']['dose_z_variation']) ** 2)
                for e in vieillit},
        },
        'secondaire': {'resume': resumer(secondaire), 'liste': secondaire},
    }


# ---------------------------------------------------------------- contrôles

def controle_cox(graine=20261121):
    """Simulation numérique (pas une mesure) : le moteur de Cox retrouve un effet fabriqué, avec
    troncature à gauche et ex aequo, à 0,1 près."""
    rng = np.random.default_rng(graine)
    n = 900
    x = rng.normal(size=n)
    g = (rng.random(n) < 0.5).astype(float)
    entree = rng.uniform(0.5, 1.5, n)
    # risque de Gompertz, multiplié par exp(0,4 x − 0,7 g), conditionné à la vie à l'entrée
    a, b = 0.01, 1.5
    m = np.exp(0.4 * x - 0.7 * g)
    u = -np.log(rng.random(n))
    t = np.log(np.exp(b * entree) + b * u / (a * m)) / b
    t = np.round(t * 365.25) / 365.25            # des ex aequo, comme des jours entiers
    mort = (rng.random(n) < 0.95).astype(float)  # quelques censures
    coef, se, _ = cox(entree, t, mort, np.column_stack([x, g]))
    return {'vrai': [0.4, -0.7], 'estime': [float(c) for c in coef], 'erreur_type': [float(s) for s in se]}


def autotests(r):
    assert r['donnees']['souris'] == 937
    c = r['controle_cox']
    assert all(abs(e - v) < 0.1 for e, v in zip(c['estime'], c['vrai'])), c
    # Les décomptes écrits dans l'article (site/langues) : s'ils changent, le texte doit changer.
    p, t, s = r['principale']['resume'], r['temoin_negatif'], r['secondaire']['resume']
    assert (p['mesures'], p['changees_par_la_restriction'], p['changees_apres_etalonnage'], p['liees_a_la_survie'],
            len(p['candidates']), len(p['candidates_etalonnees'])) == (75, 51, 42, 43, 27, 25), p
    assert (t['mesures'], t['decouvertes_q_0_05']) == (109, 10), t
    assert (s['mesures'], s['liees_a_la_survie'], len(s['candidates_etalonnees'])) == (104, 15, 5), s
    ry = r['rythme']
    assert len(ry['qui_changent_avec_l_age_chez_les_souris_a_volonte']) == 4 and not ry['dont_la_restriction_freine_le_changement_nominal']
    assert len(ry['dont_le_sens_est_celui_d_un_frein']) == 4
    assert all(abs(x['lambda_avec']) >= 0.98 * x['lambda_sans'] for x in r['pentes']), r['pentes']


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
    options = arguments.parse_args()
    lignes, colonnes = lire()
    resultats = analyser(lignes, colonnes)
    resultats['controle_cox'] = controle_cox()
    autotests(resultats)
    Path(options.out).write_text(json.dumps(arrondir(resultats), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    p = resultats['principale']['resume']
    print(f"{p['mesures']} mesures du sang ; changées par la restriction : {p['changees_par_la_restriction']} ; "
          f"liées à la survie : {p['liees_a_la_survie']} ; candidates : {len(p['candidates'])}")
    print(f"témoin négatif : {resultats['temoin_negatif']['part_p_inferieur_0_05']:.3f} de p < 0,05, "
          f"{resultats['temoin_negatif']['decouvertes_q_0_05']} découverte(s) ; autotests réussis")
