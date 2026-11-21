#!/usr/bin/env python3
"""La restriction calorique ralentit-elle le vieillissement, et que vaudrait-elle chez l'humain ?

Trois calculs, sur des données publiques :

A. Souris (mesure). 937 souris femelles Diversity Outbred, une par génome, nourries à volonté
   (AL), à jeun un jour (1D) ou deux jours (2D) par semaine, ou restreintes de 20 % ou 40 % dès
   6 mois (Di Francesco et al., Nature 2024 ; durées de vie individuelles publiées par Calico
   sous licence MIT, donnees/drido-survie.csv). Chaque régime est comparé aux souris nourries
   à volonté avec le modèle de l'étude « Retarder ou ralentir » :
     - retarder : le risque est divisé par un même facteur à tout âge, h1(t) = θ·h0(t) ;
     - ralentir : à partir du début du régime (âge s), le temps s'écoule λ fois plus lentement,
       h1(t) = (1/λ)·h0(s + (t − s)/λ) ; le temps de doublement du risque est multiplié par λ.
   Le modèle général h1(t) = θ·a·exp(b·s)·exp((b/λ)(t − s)) contient les deux. Une souris entre
   dans le calcul à 365 jours (troncature à gauche), une souris retirée est censurée.

B. Le contrôle demandé par la relecture du 21 novembre 2026 : les souris ne sont pas toutes
   aussi fragiles. Un traitement qui sauve d'abord les plus fragiles peut raidir la courbe sans
   rien changer au vieillissement. On refait donc chaque ajustement avec une fragilité
   individuelle de loi gamma (modèle gamma-Gompertz), pour la restriction et pour les 27
   traitements de l'Interventions Testing Program (ITP) retenus par l'étude du 20 novembre.

C. Humain (conversion, pas mesure). La table de mortalité 2023 de la Social Security
   Administration est ralentie à partir de 40 ans d'un facteur λ, sur la seule part du risque
   qui augmente avec l'âge (le risque de fond, celui de 10 ans, reste tel quel). On en tire
   l'âge médian au décès pour : le ralentissement mesuré chez l'humain sous restriction par
   l'horloge DunedinPACE dans l'essai CALERIE (2 à 3 %, Waziry et al. 2023), celui qu'elle
   donnerait pour 20 % de restriction, et ceux mesurés chez la souris en A. Aucune de ces
   valeurs n'est une prévision : DunedinPACE n'est pas la mortalité, et rien ne montre qu'un
   ralentissement mesuré sur deux ans dure toute une vie.

Limites : analyse faite après avoir vu les données, sans plan déposé ; une seule expérience de
souris, femelles seulement, un seul laboratoire ; modèle de Gompertz.

Python >= 3.9 et numpy. Usage : python3 analyse.py --out resultats.json
"""
import argparse
import collections
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
DRIDO = ICI / 'donnees' / 'drido-survie.csv'
ITP = RACINE / '2026-11-20-retarder-ou-ralentir' / 'donnees' / 'itp-survie.csv'
ITP_RESULTATS = RACINE / '2026-11-20-retarder-ou-ralentir' / 'resultats.json'
SSA = RACINE / '2026-11-20-immortalite' / 'donnees' / 'table-mortalite-ssa-2023.csv'
EMPREINTE_DRIDO = '981f1bf476280f4e84643afcda48cb3ab20ddf9d10200083e6f8285cfd190f3d'

AN = 365.25
MOIS = 30.4375
PLANCHER_JOURS = 365.0
DEBUT_DRIDO_MOIS = 6.0
REGIMES = (('20', 'restriction de 20 %'), ('40', 'restriction de 40 %'),
           ('1D', 'un jour de jeûne par semaine'), ('2D', 'deux jours de jeûne par semaine'))
SITES_ITP = ('TJL', 'UM', 'UT')
SEUIL_1DDL = 3.841
SEUIL_ETALONNE = 6.99444   # seuil corrigé par l'étalonnage de l'étude du 20 novembre (resultats.json)
T975 = {k: v for k, v in zip(range(1, 31), (12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228,
                                             2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086,
                                             2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042))}


# ---------------------------------------------------------------- le modèle

class Strate:
    """Témoins et traités d'un même lieu ; âges en années, entrée e et début du traitement s."""

    def __init__(self, tc, dc, tt, dt, entree, debut):
        self.tc, self.dc = np.asarray(tc, float), np.asarray(dc, float)
        self.tt, self.dt = np.asarray(tt, float), np.asarray(dt, float)
        self.entree, self.debut = float(entree), float(debut)

    def log_vraisemblance(self, ln_a, ln_b, ln_theta, ln_lambda, v):
        a, b = math.exp(ln_a), math.exp(ln_b)
        bt = b / math.exp(ln_lambda)
        e, s = self.entree, self.debut
        # témoins
        hc = ln_a + b * self.tc
        Hc = (a / b) * np.expm1(b * self.tc)
        Hce = (a / b) * math.expm1(b * e)
        # traités (âges ≥ e ≥ s)
        k = math.exp(ln_theta) * a * math.exp(b * s)
        H0s = (a / b) * math.expm1(b * s)
        ht = ln_theta + ln_a + b * s + bt * (self.tt - s)
        Ht = H0s + k * np.expm1(bt * (self.tt - s)) / bt
        Hte = H0s + k * math.expm1(bt * (e - s)) / bt
        if v <= 0:
            return (float((self.dc * hc).sum() + (self.dt * ht).sum())
                    - float((Hc - Hce).sum() + (Ht - Hte).sum()))
        lc, lt = np.log1p(v * Hc), np.log1p(v * Ht)
        return (float((self.dc * (hc - lc)).sum() + (self.dt * (ht - lt)).sum())
                - float((lc - math.log1p(v * Hce)).sum() + (lt - math.log1p(v * Hte)).sum()) / v)


def nelder_mead(f, x0, pas=0.3, iterations=6000, tol=1e-9):
    """Minimum d'une fonction de n variables (Nelder-Mead adaptatif, Gao et Han 2012)."""
    n = len(x0)
    al, ga, rh, si = 1.0, 1 + 2 / n, 0.75 - 1 / (2 * n), 1 - 1 / n
    P = [np.array(x0, float)] + [np.array(x0, float) + pas * np.eye(n)[i] for i in range(n)]
    F = [f(p) for p in P]
    for _ in range(iterations):
        ordre = np.argsort(F)
        P, F = [P[i] for i in ordre], [F[i] for i in ordre]
        if abs(F[-1] - F[0]) < tol and max(np.abs(p - P[0]).max() for p in P) < 1e-7:
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
            if fr < F[-1]:
                k = c + rh * (r - c)
                fk = f(k)
                ok = fk <= fr
            else:
                k = c + rh * (P[-1] - c)
                fk = f(k)
                ok = fk < F[-1]
            if ok:
                P[-1], F[-1] = k, fk
            else:
                P = [P[0]] + [P[0] + si * (p - P[0]) for p in P[1:]]
                F = [F[0]] + [f(p) for p in P[1:]]
    i = int(np.argmin(F))
    return P[i], F[i]


def minimiser(f, x0):
    """Nelder-Mead relancé depuis son meilleur point jusqu'à ce qu'il ne progresse plus."""
    x, fx = nelder_mead(f, x0)
    for pas in (0.1, 0.03, 0.01):
        x2, f2 = nelder_mead(f, x, pas=pas)
        if f2 < fx - 1e-7:
            x, fx = x2, f2
    return x, fx


def ajuster(strates, modele, fragilite, depart=None):
    """Ajuste un modèle : 'nul' (θ = λ = 1), 'retard' (λ = 1), 'ralentissement' (θ = 1/λ),
    'general' ; avec ou sans fragilité gamma (variance v). Une courbe de base (a, b) par strate.
    Rend (log-vraisemblance, paramètres)."""
    n = len(strates)
    libres = {'nul': 0, 'retard': 1, 'ralentissement': 1, 'general': 2}[modele] + (1 if fragilite else 0)

    def deplier(x):
        base = x[:2 * n]
        p = x[2 * n:]
        if modele == 'nul':
            lt, ll = 0.0, 0.0
        elif modele == 'retard':
            lt, ll = p[0], 0.0
        elif modele == 'ralentissement':
            lt, ll = -p[0], p[0]
        else:
            lt, ll = p[0], p[1]
        v = math.exp(p[-1]) if fragilite else 0.0
        return base, lt, ll, v

    def moins_ll(x):
        base, lt, ll, v = deplier(x)
        if abs(ll) > 2.5 or abs(lt) > 6 or v > 50:
            return 1e12
        tot = 0.0
        for i, st in enumerate(strates):
            if not (-15 < base[2 * i] < 2 and -3 < base[2 * i + 1] < 3):
                return 1e12
            tot += st.log_vraisemblance(base[2 * i], base[2 * i + 1], lt, ll, v)
        return -tot if math.isfinite(tot) else 1e12

    if depart is None:
        depart = []
        for st in strates:
            seul = Strate(st.tc, st.dc, [], [], st.entree, st.debut)
            xa, _ = minimiser(lambda z: -seul.log_vraisemblance(z[0], z[1], 0.0, 0.0, 0.0)
                              if -15 < z[0] < 2 and -3 < z[1] < 3 else 1e12, [-5.0, 0.8])
            depart += list(xa)
        depart += [0.0] * (libres - (1 if fragilite else 0)) + ([math.log(0.1)] if fragilite else [])
    x, fx = minimiser(moins_ll, depart)
    base, lt, ll, v = deplier(x)
    return -fx, {'theta': math.exp(lt), 'lambda': math.exp(ll), 'v': v, 'x': [float(z) for z in x],
                 'doublement_temoins_jours': [math.log(2) / math.exp(base[2 * i + 1]) * AN for i in range(n)]}


def comparer(strates, fragilite):
    """Les quatre modèles et les tests du rapport de vraisemblance."""
    l0, p0 = ajuster(strates, 'nul', fragilite)
    lr, pr = ajuster(strates, 'retard', fragilite)
    ls, ps = ajuster(strates, 'ralentissement', fragilite)
    lg, pg = ajuster(strates, 'general', fragilite)
    # le modèle général contient les trois autres : on part aussi de leurs optimums
    for p, extra in ((pr, [math.log(pr['theta']), 0.0]), (ps, [-math.log(ps['lambda']), math.log(ps['lambda'])])):
        n = 2 * len(strates)
        depart = p['x'][:n] + extra + (p['x'][-1:] if fragilite else [])
        l2, p2 = ajuster(strates, 'general', fragilite, depart)
        if l2 > lg:
            lg, pg = l2, p2
    lg = max(lg, lr, ls, l0)
    return {
        'theta_general': pg['theta'], 'lambda_general': pg['lambda'], 'fragilite_v': pg['v'],
        'theta_retard': pr['theta'], 'lambda_ralentissement': ps['lambda'],
        'x2_effet': 2 * (lg - l0), 'x2_retard_insuffisant': 2 * (lg - lr),
        'x2_ralentissement_insuffisant': 2 * (lg - ls),
        'doublement_temoins_jours': float(np.mean(pg['doublement_temoins_jours'])),
        'log_vraisemblance': lg, '_general': pg,
    }


def intervalle_lambda(strates, fragilite, lg, centre, seuil=SEUIL_1DDL):
    """Intervalle de vraisemblance profilée à 95 % pour λ (modèle général)."""
    def profil(ln_l):
        def f(x):
            n = 2 * len(strates)
            base, lt = x[:n], x[n]
            v = math.exp(x[n + 1]) if fragilite else 0.0
            if abs(lt) > 6 or v > 50:
                return 1e12
            tot = sum(st.log_vraisemblance(base[2 * i], base[2 * i + 1], lt, ln_l, v) for i, st in enumerate(strates))
            return -tot if math.isfinite(tot) else 1e12
        x0 = centre['x'][:2 * len(strates)] + [math.log(centre['theta']) + 0.0] + (centre['x'][-1:] if fragilite else [])
        _, fx = minimiser(f, x0)
        return 2 * (lg + fx)

    def borne(sens):
        lo, hi = math.log(centre['lambda']), math.log(centre['lambda']) + sens * 0.05
        while profil(hi) < seuil:
            lo, hi = hi, hi + sens * 0.05
            if abs(hi) > 2:
                return None
        for _ in range(18):
            mi = (lo + hi) / 2
            lo, hi = (mi, hi) if profil(mi) < seuil else (lo, mi)
        return math.exp((lo + hi) / 2)
    return [borne(-1), borne(+1)]


# ---------------------------------------------------------------- A. la restriction chez la souris

def lire_drido():
    if hashlib.sha256(DRIDO.read_bytes()).hexdigest() != EMPREINTE_DRIDO:
        raise ValueError('donnees/drido-survie.csv a changé : empreinte différente.')
    with open(DRIDO, encoding='utf-8') as f:
        return [(r['generation'], r['regime'], int(r['mort']), float(r['age_jours'])) for r in csv.DictReader(f)]


def mediane_km(ages, morts, entree=0.0):
    paires = sorted((t, d) for t, d in zip(ages, morts) if t > entree)
    n, survie, i = len(paires), 1.0, 0
    restant = n
    while i < n:
        t = paires[i][0]
        j, d = i, 0
        while j < n and paires[j][0] == t:
            d += paires[j][1]
            j += 1
        if d:
            survie *= 1 - d / restant
            if survie <= 0.5:
                return t
        restant -= j - i
        i = j
    return None


def strates_drido(souris, regime, plancher=PLANCHER_JOURS, coupure=None):
    debut = DEBUT_DRIDO_MOIS * MOIS / AN
    entree = max(DEBUT_DRIDO_MOIS * MOIS, plancher) / AN

    def prendre(r):
        out = []
        for (_, reg, mort, age) in souris:
            if reg != r or age / AN <= entree:
                continue
            t, d = age / AN, mort
            if coupure is not None and t > coupure:
                t, d = coupure, 0
            out.append((t, d))
        return out
    c, x = prendre('AL'), prendre(regime)
    return [Strate([t for t, _ in c], [d for _, d in c], [t for t, _ in x], [d for _, d in x], entree, debut)]


def analyser_restriction(souris):
    medianes = {}
    for reg in ('AL',) + tuple(r for r, _ in REGIMES):
        ages = [s[3] for s in souris if s[1] == reg]
        morts = [s[2] for s in souris if s[1] == reg]
        medianes[reg] = {'souris': len(ages), 'mortes': sum(morts), 'mediane_jours': mediane_km(ages, morts)}
    for reg in medianes:
        medianes[reg]['gain_pourcent'] = 100 * (medianes[reg]['mediane_jours'] / medianes['AL']['mediane_jours'] - 1)
    regimes = {}
    tous = sorted(s[3] for s in souris)
    coupure_90 = tous[int(0.9 * len(tous))] / AN
    for reg, nom in REGIMES:
        st = strates_drido(souris, reg)
        sans = comparer(st, False)
        avec = comparer(st, True)
        sortie = {'nom': nom, 'n_regime': int(len(st[0].tt)), 'n_temoins': int(len(st[0].tc))}
        for cle, r, frag in (('gompertz', sans, False), ('gamma_gompertz', avec, True)):
            r = dict(r)
            g = r.pop('_general')
            r['lambda_ic95'] = intervalle_lambda(st, frag, r['log_vraisemblance'], g)
            r['p_retard_suffit'] = math.erfc(math.sqrt(max(r['x2_retard_insuffisant'], 0) / 2))
            r['p_ralentissement_suffit'] = math.erfc(math.sqrt(max(r['x2_ralentissement_insuffisant'], 0) / 2))
            r['p_effet'] = math.exp(-max(r['x2_effet'], 0) / 2)
            sortie[cle] = r
        # sensibilité : entrée à 6 mois au lieu de 365 jours ; âges coupés au 90e centile
        for cle, kw in (('entree_6_mois', {'plancher': 0.0}), ('coupure_90e_centile', {'coupure': coupure_90})):
            r = comparer(strates_drido(souris, reg, **kw), False)
            sortie[cle] = {'lambda_general': r['lambda_general'], 'x2_retard_insuffisant': r['x2_retard_insuffisant']}
        regimes[reg] = sortie
    return {'souris': len(souris), 'censurees': sum(1 - s[2] for s in souris), 'medianes': medianes,
            'regimes': regimes, 'coupure_90e_centile_jours': coupure_90 * AN}


# ---------------------------------------------------------------- B. la fragilité sur les traitements de l'ITP

def lire_itp():
    import re
    par = collections.defaultdict(list)
    with open(ITP, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            m = re.match(r'\s*(\d+(?:\.\d+)?)', r['age_debut_mois'])
            par[(r['cohorte'], r['sexe'], r['groupe'])].append(
                (r['site'], int(r['mort']), float(r['age_jours']), float(m.group(1)) if m else None))
    return par


def strates_itp(par, cohorte, sexe, groupe):
    v = par[(cohorte, sexe, groupe)]
    debut_j = v[0][3] * MOIS
    entree, debut = max(debut_j, PLANCHER_JOURS) / AN, debut_j / AN
    out = []
    for site in SITES_ITP:
        c = [(t / AN, d) for (st, d, t, _) in par[(cohorte, sexe, 'Control')] if st == site and t / AN > entree]
        x = [(t / AN, d) for (st, d, t, _) in v if st == site and t / AN > entree]
        if len(c) < 20 or len(x) < 10:
            continue
        out.append(Strate([t for t, _ in c], [d for _, d in c], [t for t, _ in x], [d for _, d in x], entree, debut))
    return out


def molecule(groupe):
    """La molécule d'un groupe, d'après les abréviations de la Mouse Phenome Database (comme l'étude
    du 20 novembre)."""
    g = groupe.lower()
    for debut, nom in (('metrapa', 'rapamycine et metformine'), ('raac', 'rapamycine et acarbose'), ('rapa', 'rapamycine'),
                       ('aca', 'acarbose'), ('17ae2', '17-alpha-estradiol'), ('cana', 'canagliflozine'),
                       ('ndga', 'acide nordihydroguaïarétique'), ('nd_', 'acide nordihydroguaïarétique'),
                       ('oh-est', '16-alpha-hydroxyestriol')):
        if g.startswith(debut):
            return nom
    return groupe


def moyenne_grappes(liste, cle):
    grappes = collections.defaultdict(list)
    for r in liste:
        grappes[(r['cohorte'], r['sexe'])].append(math.log(r[cle]))
    m = np.array([np.mean(v) for v in grappes.values()])
    k = len(m)
    demi = T975[min(k - 1, 30)] * float(m.std(ddof=1)) / math.sqrt(k)
    return math.exp(m.mean()), [math.exp(m.mean() - demi), math.exp(m.mean() + demi)], k


def analyser_itp():
    publies = json.loads(ITP_RESULTATS.read_text(encoding='utf-8'))['liste_efficaces']
    par = lire_itp()
    liste = []
    for p in publies:
        st = strates_itp(par, p['cohorte'], p['sexe'], p['groupe'])
        sans = comparer(st, False)
        avec = comparer(st, True)
        liste.append({
            'cohorte': p['cohorte'], 'sexe': p['sexe'], 'groupe': p['groupe'],
            'lambda_publie': p['lambda_general'], 'lambda_gompertz': sans['lambda_general'],
            'lambda_gamma_gompertz': avec['lambda_general'], 'fragilite_v': avec['fragilite_v'],
            'x2_fragilite': 2 * (avec['log_vraisemblance'] - sans['log_vraisemblance']),
            'x2_retard_insuffisant_gamma': avec['x2_retard_insuffisant'],
            'x2_ralentissement_insuffisant_gamma': avec['x2_ralentissement_insuffisant'],
        })
    par_molecule = collections.defaultdict(list)
    for r in liste:
        par_molecule[molecule(r['groupe'])].append(r)
    resume_molecules = {
        nom: {'comparaisons': len(v),
              'lambda_median_gompertz': float(np.median([r['lambda_gompertz'] for r in v])),
              'lambda_median_gamma_gompertz': float(np.median([r['lambda_gamma_gompertz'] for r in v])),
              'lambda_max_gamma_gompertz': max(r['lambda_gamma_gompertz'] for r in v)}
        for nom, v in sorted(par_molecule.items())}
    m_g, ic_g, k = moyenne_grappes(liste, 'lambda_gompertz')
    m_f, ic_f, _ = moyenne_grappes(liste, 'lambda_gamma_gompertz')
    return {
        'n': len(liste), 'n_cohortes_sexes': k,
        'ecart_max_au_publie': max(abs(r['lambda_gompertz'] / r['lambda_publie'] - 1) for r in liste),
        'lambda_moyen_gompertz': m_g, 'lambda_moyen_gompertz_ic95': ic_g,
        'lambda_moyen_gamma_gompertz': m_f, 'lambda_moyen_gamma_gompertz_ic95': ic_f,
        'doublement_raccourci_pourcent_gamma': 100 * (1 - m_f),
        'n_fragilite_retenue': sum(r['x2_fragilite'] > SEUIL_1DDL for r in liste),
        'n_lambda_superieur_a_1_gamma': sum(r['lambda_gamma_gompertz'] > 1 for r in liste),
        'n_ralentissement_etabli_gamma': sum(r['lambda_gamma_gompertz'] > 1 and r['x2_retard_insuffisant_gamma'] > SEUIL_ETALONNE
                                            for r in liste),
        'n_ralentissement_rejete_gamma': sum(r['x2_ralentissement_insuffisant_gamma'] > SEUIL_ETALONNE for r in liste),
        'par_molecule': resume_molecules,
        'liste': liste,
    }


# ---------------------------------------------------------------- C. la conversion chez l'humain

def lire_ssa():
    lignes = [l for l in SSA.read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
    t = list(csv.DictReader(lignes))
    return {'hommes': [float(r['male_q']) for r in t], 'femmes': [float(r['female_q']) for r in t]}


def age_median_ralenti(q, lam, depart=40, fond_age=10, pas=0.01):
    """Âge médian au décès d'une personne en vie à `depart`, si la part du risque qui croît avec
    l'âge (au-dessus du risque de fond, celui de `fond_age` ans) avance λ fois moins vite après
    `depart`. Risque annuel constant par année d'âge, prolongé au-delà de la table."""
    mu = [-math.log(1 - x) for x in q]
    fond = mu[fond_age]

    def mu_age(x):
        i = min(int(x), len(mu) - 1)
        return mu[i]
    cumul, x = 0.0, float(depart)
    cible = math.log(2)
    while x < 1e6:
        u = depart + (x - depart) / lam
        h = fond + max(mu_age(u) - fond, 0.0) / lam
        if cumul + h * pas >= cible:
            return x + (cible - cumul) / h
        cumul += h * pas
        x += pas
    return None


def analyser_humain(restriction):
    q = lire_ssa()
    # CALERIE (Waziry et al. 2023) : « a reduction in the pace of aging of 2–3% » en intention de
    # traiter ; pour 20 % de restriction, d = −0,43 au lieu de −0,25 à −0,29 en intention de traiter,
    # soit environ 1,6 fois plus : de 3,2 % à 4,7 % en gardant le même rapport.
    rapport_20 = 0.43 / 0.27
    scenarios = [
        ('aucun', 1.0),
        ('calerie_2_pourcent', 1 / 0.98),
        ('calerie_3_pourcent', 1 / 0.97),
        ('calerie_20_pourcent_de_restriction', 1 / (1 - 0.025 * rapport_20)),
        ('souris_restriction_20', restriction['regimes']['20']['gompertz']['lambda_general']),
        ('souris_restriction_40', restriction['regimes']['40']['gompertz']['lambda_general']),
        ('double', 2.0), ('dix_fois', 10.0), ('cent_fois', 100.0),
    ]
    sortie = {'hypotheses': {'depart_ans': 40, 'risque_de_fond': 'risque à 10 ans, laissé tel quel',
                             'rapport_effet_20_pourcent_sur_intention_de_traiter': rapport_20}}
    for nom, lam in scenarios:
        sortie[nom] = {'lambda': lam}
        for sexe in ('hommes', 'femmes'):
            m0 = age_median_ralenti(q[sexe], 1.0)
            m = age_median_ralenti(q[sexe], lam)
            sortie[nom][sexe] = {'age_median_au_deces': m, 'annees_gagnees': m - m0}
    # Essai humain dont le critère est le rythme du vieillissement (DunedinPACE) : personnes par
    # groupe pour 90 % de chances de voir l'effet, test bilatéral à 5 %, deux groupes égaux.
    z = 1.959964 + 1.281552
    sortie['essai_humain'] = {
        'effet_intention_de_traiter_d': 0.27, 'effet_20_pourcent_d': 0.43,
        'personnes_par_groupe_intention_de_traiter': math.ceil(2 * z * z / 0.27 ** 2),
        'personnes_par_groupe_20_pourcent': math.ceil(2 * z * z / 0.43 ** 2),
        'abandons_prevus': 0.2,
        'personnes_a_recruter_par_groupe_intention_de_traiter': math.ceil(math.ceil(2 * z * z / 0.27 ** 2) / 0.8),
    }
    return sortie


# ---------------------------------------------------------------- contrôles

def tirer(rng, n, a, b, entree, debut=None, theta=1.0, lam=1.0, v=0.0):
    """Âges de mort simulés sous le modèle (fragilité gamma de variance v si v > 0)."""
    z = rng.gamma(1 / v, v, n) if v > 0 else np.ones(n)
    u = -np.log(rng.random(n)) / z
    if debut is None:
        return np.log(np.exp(b * entree) + (b / a) * u) / b
    bt = b / lam
    return debut + np.log(np.exp(bt * (entree - debut)) + bt * u / (theta * a * math.exp(b * debut))) / bt


def simuler(graine, tours=12):
    """Simulations numériques (pas des mesures) : effectifs voisins de la restriction de 40 %.
    Un retard pur, un ralentissement pur, et un retard pur dans une population hétérogène."""
    rng = np.random.default_rng(graine)
    a, b, entree, debut = 0.01, 1.6, 1.0, 0.5
    sortie = {}
    for nom, theta, lam, v in (('retard', 0.45, 1.0, 0.0), ('ralentissement', 1 / 1.3, 1.3, 0.0),
                               ('retard_heterogene', 0.45, 1.0, 0.6)):
        sans, avec = [], []
        for _ in range(tours):
            tc = tirer(rng, 185, a, b, entree, v=v)
            tt = tirer(rng, 180, a, b, entree, debut, theta, lam, v=v)
            st = [Strate(tc, np.ones(185), tt, np.ones(180), entree, debut)]
            sans.append(ajuster(st, 'general', False)[1]['lambda'])
            if v > 0:
                avec.append(ajuster(st, 'general', True)[1]['lambda'])
        sortie[nom] = {'lambda_vrai': lam, 'fragilite_vraie': v, 'tours': tours,
                       'lambda_median_gompertz': float(np.median(sans))}
        if avec:
            sortie[nom]['lambda_median_gamma_gompertz'] = float(np.median(avec))
    return sortie


def puissance_pente(graine, tours=200, effectifs=(150, 300, 450, 600), lam=1.25):
    """Simulations numériques (pas des mesures) : chances de détecter un ralentissement pur de
    facteur λ (souris témoins et traitées en nombre égal, suivies jusqu'à la mort, courbe de base
    voisine des souris nourries à volonté). Sert à dimensionner une expérience dont le critère
    principal est la pente, pas la durée de vie."""
    rng = np.random.default_rng(graine)
    a, b, entree, debut = 0.01, 1.55, 1.0, 0.5
    sortie = {}
    for n in effectifs:
        x2 = []
        for _ in range(tours):
            tc = tirer(rng, n, a, b, entree)
            tt = tirer(rng, n, a, b, entree, debut, 1 / lam, lam)
            st = [Strate(tc, np.ones(n), tt, np.ones(n), entree, debut)]
            lr = ajuster(st, 'retard', False)[0]
            lg = ajuster(st, 'general', False)[0]
            x2.append(2 * max(lg - lr, 0.0))
        x2 = np.array(x2)
        sortie[str(n)] = {'souris_par_groupe': n, 'tours': tours, 'lambda_vrai': lam,
                          'puissance_seuil_theorique': float((x2 > SEUIL_1DDL).mean()),
                          'puissance_seuil_etalonne': float((x2 > SEUIL_ETALONNE).mean())}
    return sortie


def autotests(r):
    # le moteur refait l'étude du 20 novembre
    assert r['itp']['ecart_max_au_publie'] < 0.03, r['itp']['ecart_max_au_publie']
    # les simulations retrouvent ce qui a été fabriqué
    s = r['simulations']
    assert abs(s['retard']['lambda_median_gompertz'] - 1.0) < 0.08, s
    assert abs(s['ralentissement']['lambda_median_gompertz'] - 1.3) < 0.1, s
    assert abs(s['retard_heterogene']['lambda_median_gamma_gompertz'] - 1.0) < 0.1, s
    # la médiane des souris nourries à volonté et le gain de la restriction de 40 %
    m = r['restriction']['medianes']
    assert m['AL']['souris'] == 188 and m['40']['souris'] == 182
    assert r['restriction']['souris'] == 937 and r['restriction']['censurees'] == 13
    # Di Francesco et al. 2024 : médiane de la restriction de 40 % allongée de 36,3 %
    assert abs(m['40']['gain_pourcent'] - 36.3) < 0.1, m['40']
    # conversion humaine : sans ralentissement, rien ne change ; elle croît avec λ
    h = r['humain']
    assert abs(h['aucun']['hommes']['annees_gagnees']) < 1e-9
    assert h['dix_fois']['femmes']['annees_gagnees'] > h['double']['femmes']['annees_gagnees'] > 0


def arrondir(x):
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return float(f'{float(x):.6g}')
    if isinstance(x, dict):
        return {k: arrondir(v) for k, v in x.items() if not k.startswith('_')}
    if isinstance(x, (list, tuple)):
        return [arrondir(v) for v in x]
    return x


if __name__ == '__main__':
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--out', default=str(ICI / 'resultats.json'))
    arguments.add_argument('--tours', type=int, default=12)
    options = arguments.parse_args()
    restriction = analyser_restriction(lire_drido())
    resultats = {
        'restriction': restriction,
        'itp': analyser_itp(),
        'humain': analyser_humain(restriction),
        'simulations': simuler(20261121, options.tours),
        'puissance_pente': puissance_pente(20261122),
    }
    autotests(resultats)
    Path(options.out).write_text(json.dumps(arrondir(resultats), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for reg, v in restriction['regimes'].items():
        g, f = v['gompertz'], v['gamma_gompertz']
        print(f"{reg} : λ = {g['lambda_general']:.3f} {g['lambda_ic95']} ; avec fragilité {f['lambda_general']:.3f} {f['lambda_ic95']}")
    i = resultats['itp']
    print(f"ITP : λ moyen {i['lambda_moyen_gompertz']:.3f} ; avec fragilité {i['lambda_moyen_gamma_gompertz']:.3f} "
          f"{i['lambda_moyen_gamma_gompertz_ic95']} ; autotests réussis")
