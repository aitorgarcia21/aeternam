#!/usr/bin/env python3
"""aeternam : un rêve fait-il vivre plus de temps qu'il n'en dure réellement ?

Question (projet « Une vie en une nuit ») : le temps vécu en rêve dépasse-t-il,
même partiellement ou par moments, le temps réellement dormi ? On mesure le
facteur F = durée vécue / durée dormie ; F > 1 serait une compression du temps.

Trois sources de mesure, toutes recalculées ici :

1. Données ouvertes (base DREAM, Wong et al., Nat. Commun. 16, 7495, 2025 ;
   jeu n° 13 « Tononi Serial Awakenings », Siclari, Baird, Perogamvros, Boly,
   LaRocque, Tononi, doi:10.26180/23306054.v3, CC BY 4.0). Réveils en sommeil
   lent N2 ; au réveil, le dormeur estime « For how long were you having
   continuous experiences before the alarm sound? » en six classes
   (0-5 s, 5-10 s, 10 s-1 min, 1-10 min, 10 min-1 h, > 1 h). La durée réelle
   de l'expérience n'est pas connue ; elle est bornée par le temps écoulé
   depuis le réveil précédent (même nuit). Si la borne basse de la classe
   déclarée dépasse ce temps, le vécu dépasse CERTAINEMENT le dormi.
2. Dement et Kleitman (1957) : réveils 5 ou 15 min après le début du sommeil
   paradoxal, choix forcé « 5 ou 15 min ? ». Effectifs publiés (sources
   secondaires concordantes, original non lu). Modèle de détection du signal
   log-normal : durée vécue = F × durée réelle × bruit, frontière de décision
   à la moyenne géométrique de 5 et 15 min (sensibilités : 10 min ; toute
   frontière entre 5 et 15 min pour la borne robuste).
3. Rêves lucides chronométrés par signaux oculaires (Erlacher, Schädlich,
   Stumbrys et Schredl, Front. Psychol. 4, 1013, 2014, tableau 2) : la même
   tâche (compter jusqu'à 10, 20, 30 ; gymnastique ; marche) dure W à l'éveil
   et D en rêve ; le temps vécu en rêve, exprimé en temps d'éveil, est W, le
   temps dormi D, donc F = W / D. Incertitude par la méthode delta à partir
   du t apparié publié, bornée de façon prudente (Cauchy-Schwarz), puis gonflée
   du rapport des quantiles t (n - 1 ddl) et normal pour la méta-synthèse.

Méta-synthèse : moyenne pondérée par l'inverse des variances de ln F sur les
échantillons INDÉPENDANTS (Erlacher comptage, Erlacher gymnastique, Dement et
Kleitman), effets fixes et effets aléatoires (DerSimonian-Laird).

RÈGLE DE DÉCISION (écrite avant d'exécuter les calculs ; les ordres de
grandeur publiés étaient connus en l'écrivant, pas les résultats combinés) :
  OUI (compression démontrée) si la borne inférieure unilatérale à 95 % du
      facteur global F (effets aléatoires) dépasse 1, OU si, dans les données
      ouvertes, la borne inférieure unilatérale à 95 % (Clopper-Pearson) de la
      proportion d'expériences dont le vécu dépasse certainement le dormi
      dépasse 5 % (compression « par moments » fréquente) ;
  NON (compression exclue au-delà de X) si ce n'est pas OUI et que la borne
      supérieure unilatérale à 95 % X du facteur global (effets aléatoires)
      est inférieure à 2 (même un doublement du temps vécu est exclu) ;
  INDÉTERMINÉ sinon.

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
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
N_BOOT = 20000
N = NormalDist()

SEUIL_OUI_PROPORTION = 0.05
SEUIL_NON_FACTEUR = 2.0
CONFIANCE = 0.95

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


def inverse(f, cible: float, lo: float, hi: float, n: int = 200) -> float:
    """Bissection pour f croissante."""
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if f(mid) < cible:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def t_cdf(t: float, nu: float) -> float:
    x = nu / (nu + t * t)
    queue = 0.5 * betainc(nu / 2.0, 0.5, x)
    return 1.0 - queue if t >= 0 else queue


def t_ppf(p: float, nu: float) -> float:
    return inverse(lambda t: t_cdf(t, nu), p, -1e3, 1e3)


def clopper_pearson(k: int, n: int, conf: float = CONFIANCE) -> tuple[float, float]:
    """Bornes UNILATÉRALES au niveau conf : (inférieure, supérieure)."""
    alpha = 1.0 - conf
    bas = 0.0 if k == 0 else inverse(lambda p: betainc(k, n - k + 1, p), alpha, 0.0, 1.0)
    haut = 1.0 if k == n else inverse(lambda p: betainc(k + 1, n - k, p), 1.0 - alpha, 0.0, 1.0)
    return bas, haut


# =========================================================================== 1. données ouvertes
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


def resume_tononi(lignes: list[dict]) -> dict:
    classes = {str(c): sum(1 for l in lignes if l['classe'] == c) for c in CLASSES_TONONI}
    bornees = [l for l in lignes if l['dormi_max_s'] is not None]
    certain = [l for l in bornees if CLASSES_TONONI[l['classe']][0] > l['dormi_max_s']]
    possible = [l for l in bornees if CLASSES_TONONI[l['classe']][1] > l['dormi_max_s']]
    n, k = len(bornees), len(certain)
    bas, haut = clopper_pearson(k, n)
    rapports_min = [CLASSES_TONONI[l['classe']][0] / l['dormi_max_s'] for l in bornees]
    dormis = sorted(l['dormi_max_s'] / 60.0 for l in bornees)
    return {
        'n_estimations': len(lignes),
        'effectifs_par_classe': classes,
        'n_avec_experience_rappelee': sum(1 for l in lignes if l['experience'] == '2'),
        'n_bornees': n,
        'n_vecu_depasse_certainement_dormi': k,
        'proportion_certaine': k / n if n else None,
        'proportion_certaine_borne_inf_95': bas,
        'proportion_certaine_borne_sup_95': haut,
        'n_depassement_possible': len(possible),
        'rapport_vecu_min_sur_dormi_max_le_plus_grand': max(rapports_min) if rapports_min else None,
        'dormi_max_min_minutes': dormis[0] if dormis else None,
        'dormi_max_mediane_minutes': float(np.median(dormis)) if dormis else None,
        'dormi_max_max_minutes': dormis[-1] if dormis else None,
        'n_classe_plus_de_10_min': classes['5'] + classes['6'],
        'n_classe_plus_d_une_heure': classes['6'],
    }


# =========================================================================== 2. Dement et Kleitman
def sdt_ln_F(p_faux_5: float, p_faux_15: float, frontiere_min: float) -> tuple[float, float]:
    """Modèle log-normal : ln S = ln F + ln T + σ ε. Retourne (ln F, σ)."""
    za = N.inv_cdf(1.0 - p_faux_5)   # P(S > c | T = 5) = p_faux_5
    zb = N.inv_cdf(p_faux_15)        # P(S < c | T = 15) = p_faux_15
    sigma = math.log(3.0) / (za - zb)
    lnF = math.log(frontiere_min / 5.0) - za * sigma
    return lnF, sigma


def analyse_dement_kleitman() -> dict:
    v = VALEURS_PUBLIEES['dement_kleitman_1957']
    n5, n15 = v['reveils_5min'], v['reveils_15min']
    f5, f15 = n5 - v['corrects_5min'], n15 - v['corrects_15min']
    rng = np.random.default_rng(GRAINE)
    res = {'reveils': n5 + n15, 'corrects': v['corrects_5min'] + v['corrects_15min'],
           'taux_correct': (v['corrects_5min'] + v['corrects_15min']) / (n5 + n15),
           'faux_apres_5min': f5, 'faux_apres_15min': f15}
    for nom, c in (('geometrique', math.sqrt(5.0 * 15.0)), ('arithmetique', 10.0)):
        lnF, sigma = sdt_ln_F(f5 / n5, f15 / n15, c)
        b5 = rng.binomial(n5, f5 / n5, N_BOOT)
        b15 = rng.binomial(n15, f15 / n15, N_BOOT)
        ok = (b5 > 0) & (b5 < n5) & (b15 > 0) & (b15 < n15)
        tirages = np.array([sdt_ln_F(a / n5, b / n15, c)[0] for a, b in zip(b5[ok], b15[ok])])
        se = float(np.std(tirages, ddof=1))
        res[f'frontiere_{nom}'] = {
            'frontiere_min': c, 'F': math.exp(lnF), 'sigma_ln': sigma, 'ln_F': lnF, 'se_ln_F': se,
            'F_borne_sup_95': math.exp(float(np.quantile(tirages, CONFIANCE))),
            'F_borne_inf_95': math.exp(float(np.quantile(tirages, 1 - CONFIANCE))),
            'part_tirages_valides': float(ok.mean()),
            'proba_vecu_superieur_au_dormi_modele': N.cdf(lnF / sigma),
        }
    # borne robuste : si F >= c/5, la durée vécue médiane d'un rêve de 5 min dépasse la frontière c
    # et au moins la moitié des réveils à 5 min seraient jugés « 15 min ».
    _, haut = clopper_pearson(f5, n5)
    res['part_jugee_15_apres_5min'] = f5 / n5
    res['part_jugee_15_apres_5min_borne_sup_95'] = haut
    res['borne_robuste'] = {
        'condition': 'P(dire 15 | 5 min) < 1/2 exclut F_médian >= c/5',
        'exclue': haut < 0.5,
        'F_median_max_frontiere_geometrique': math.sqrt(5.0 * 15.0) / 5.0,
        'F_median_max_frontiere_15min': 15.0 / 5.0,
    }
    return res


def analyse_koulack() -> dict:
    v = VALEURS_PUBLIEES['koulack_1968']
    bas, haut = clopper_pearson(v['jugements'] - v['corrects'], v['jugements'])
    return {'jugements': v['jugements'], 'corrects': v['corrects'], 'taux_correct': v['corrects'] / v['jugements'],
            'taux_erreur_borne_sup_95': haut, 'rapport_des_durees_a_distinguer': 180.0 / 30.0}


# =========================================================================== 3. rêves lucides
def facteur_erlacher(d: dict) -> dict:
    W, D, n, t = d['W'], d['D'], d['n'], d['t']
    delta = D - W
    se_delta = delta / t
    se_W = d['W_sd'] / math.sqrt(n)
    lnF = math.log(W / D)
    se = se_delta / D + abs(delta) / (W * D) * se_W  # borne prudente (Cauchy-Schwarz)
    q = t_ppf(CONFIANCE, n - 1)
    # pour la méta-synthèse (quantiles normaux), l'erreur est gonflée du rapport t/z : petit effectif
    se_meta = se * q / N.inv_cdf(CONFIANCE)
    return {'F': W / D, 'ln_F': lnF, 'se_ln_F': se, 'se_ln_F_meta': se_meta, 'n': n,
            'F_borne_sup_95_t': math.exp(lnF + q * se), 'F_borne_inf_95_t': math.exp(lnF - q * se),
            'allongement_en_reve_pct': 100.0 * (D / W - 1.0),
            'participants_plus_rapides_ou_egaux_en_reve': n - d['plus_long_en_reve'] if 'plus_long_en_reve' in d else None}


# =========================================================================== 4. méta-synthèse
def meta(estimations: dict[str, tuple[float, float]]) -> dict:
    noms = list(estimations)
    y = np.array([estimations[k][0] for k in noms])
    s = np.array([estimations[k][1] for k in noms])
    w = 1.0 / s**2
    mu_f = float(np.sum(w * y) / np.sum(w))
    se_f = float(1.0 / math.sqrt(np.sum(w)))
    Q = float(np.sum(w * (y - mu_f) ** 2))
    ddl = len(y) - 1
    tau2 = max(0.0, (Q - ddl) / (np.sum(w) - np.sum(w**2) / np.sum(w))) if ddl > 0 else 0.0
    wr = 1.0 / (s**2 + tau2)
    mu_r = float(np.sum(wr * y) / np.sum(wr))
    se_r = float(1.0 / math.sqrt(np.sum(wr)))
    z = N.inv_cdf(CONFIANCE)
    p_Q = chi2_sf(Q, ddl) if ddl > 0 else None
    return {
        'echantillons': noms,
        'poids_effets_aleatoires': {k: float(x) for k, x in zip(noms, wr / wr.sum())},
        'F_effets_fixes': math.exp(mu_f),
        'F_effets_fixes_borne_sup_95': math.exp(mu_f + z * se_f),
        'F_effets_fixes_borne_inf_95': math.exp(mu_f - z * se_f),
        'Q': Q, 'ddl': ddl, 'p_heterogeneite': p_Q,
        'I2': max(0.0, (Q - ddl) / Q) if Q > 0 else 0.0,
        'tau2': float(tau2),
        'F_effets_aleatoires': math.exp(mu_r),
        'F_effets_aleatoires_borne_sup_95': math.exp(mu_r + z * se_r),
        'F_effets_aleatoires_borne_inf_95': math.exp(mu_r - z * se_r),
        'F_effets_aleatoires_ic95_bilateral': [math.exp(mu_r - 1.959963984540054 * se_r),
                                               math.exp(mu_r + 1.959963984540054 * se_r)],
        'p_unilateral_F_superieur_a_1': 1.0 - N.cdf(-mu_r / se_r) if se_r > 0 else None,
    }


def chi2_sf(x: float, k: int) -> float:
    """P(χ²_k > x) = 1 - P(k/2, x/2), par la série de la gamma incomplète."""
    a, xx = k / 2.0, x / 2.0
    if xx <= 0:
        return 1.0
    terme = somme = 1.0 / a
    n = 1
    while n < 1000:
        terme *= xx / (a + n)
        somme += terme
        if terme < somme * 1e-15:
            break
        n += 1
    P = somme * math.exp(-xx + a * math.log(xx) - math.lgamma(a))
    return max(0.0, 1.0 - P)


# =========================================================================== autotests
def autotests() -> dict:
    r = {}
    # 1. bêta incomplète et Student : valeurs de contrôle calculées autrement
    r['betainc_symetrie'] = abs(betainc(2.5, 3.5, 0.3) + betainc(3.5, 2.5, 0.7) - 1.0) < 1e-12
    r['t_grand_nu_normal'] = abs(t_ppf(0.95, 1e6) - N.inv_cdf(0.95)) < 1e-4
    # t à 1 ddl = Cauchy : quantile 0,95 = tan(0,45 π)
    r['t_cauchy'] = abs(t_ppf(0.95, 1) - math.tan(0.45 * math.pi)) < 1e-6
    # χ² à 2 ddl : P(X > x) = exp(-x/2)
    r['chi2_2ddl'] = abs(chi2_sf(3.0, 2) - math.exp(-1.5)) < 1e-12
    # Clopper-Pearson : 0 sur n donne borne sup unilatérale 1 - 0,05^(1/n)
    r['clopper_pearson_zero'] = abs(clopper_pearson(0, 50)[1] - (1 - 0.05 ** (1 / 50))) < 1e-9
    # 2. le modèle de détection du signal retrouve F et σ injectés
    F0, s0, c = 2.5, 0.4, math.sqrt(75.0)
    p5 = 1 - N.cdf((math.log(c) - math.log(F0 * 5)) / s0)
    p15 = N.cdf((math.log(c) - math.log(F0 * 15)) / s0)
    lnF, s = sdt_ln_F(p5, p15, c)
    r['sdt_retrouve_F'] = abs(math.exp(lnF) - F0) < 1e-9 and abs(s - s0) < 1e-9
    # 3. une compression injectée dans des données synthétiques est détectée
    rng = np.random.default_rng(1)
    lignes = []
    for i in range(200):
        dormi = float(rng.uniform(11, 60)) * 60.0
        vecu = dormi * 10.0  # facteur 10
        classe = next(k for k, (lo, hi) in CLASSES_TONONI.items() if lo <= vecu < hi)
        lignes.append({'classe': classe, 'dormi_max_s': dormi, 'experience': '2'})
    syn = resume_tononi(lignes)
    r['compression_injectee_detectee'] = syn['proportion_certaine_borne_inf_95'] > SEUIL_OUI_PROPORTION
    lignes_nulles = [dict(l, classe=4) for l in lignes]
    r['absence_de_compression_non_detectee'] = resume_tononi(lignes_nulles)['n_vecu_depasse_certainement_dormi'] == 0
    # 4. Erlacher : les pourcentages publiés (27,2 ; 52,5 ; 23,2) sont retrouvés à l'arrondi des moyennes près
    e = VALEURS_PUBLIEES['erlacher_2014']
    r['erlacher_pourcentages'] = (abs(100 * (e['comptage']['D'] / e['comptage']['W'] - 1) - 27.2) < 0.1
                                 and abs(100 * (e['marche']['D'] / e['marche']['W'] - 1) - 52.5) < 0.1
                                 and abs(100 * (e['gymnastique']['D'] / e['gymnastique']['W'] - 1) - 23.2) < 1.0)
    # 5. méta : deux estimations identiques donnent la même valeur, τ² nul
    m = meta({'a': (0.1, 0.2), 'b': (0.1, 0.2)})
    r['meta_identiques'] = abs(math.log(m['F_effets_fixes']) - 0.1) < 1e-12 and m['tau2'] == 0.0
    # 6. Dement-Kleitman : effectifs cohérents avec 92/111
    v = VALEURS_PUBLIEES['dement_kleitman_1957']
    r['dk_92_sur_111'] = (v['corrects_5min'] + v['corrects_15min'] == 92
                          and v['reveils_5min'] + v['reveils_15min'] == 111)
    r['tous_passes'] = all(r.values())
    if not r['tous_passes']:
        raise SystemExit(f'autotests en échec : {r}')
    return r


# =========================================================================== principal
def principal() -> dict:
    res = {'question': 'Un rêve fait-il vivre plus de temps qu’il n’en dure ? F = vécu / dormi',
           'regle': {'oui': 'borne inf. unilat. 95 % de F (effets aléatoires) > 1, ou borne inf. 95 % '
                            'de la proportion de vécu certainement supérieur au dormi > 5 %',
                     'non': f'borne sup. unilat. 95 % de F (effets aléatoires) < {SEUIL_NON_FACTEUR}',
                     'sinon': 'indéterminé'},
           'autotests': autotests()}
    records, add = charger_tononi()
    res['donnees_ouvertes_tononi'] = analyse_tononi(records, add)
    res['donnees_ouvertes_tononi']['sha256_archive'] = SHA_TONONI
    res['dement_kleitman'] = analyse_dement_kleitman()
    res['koulack'] = analyse_koulack()
    e = VALEURS_PUBLIEES['erlacher_2014']
    res['erlacher'] = {k: facteur_erlacher(e[k]) for k in ('comptage', 'marche', 'gymnastique')}
    res['erlacher_schredl_2004_F_squats'] = 1.0 / (1.0 + VALEURS_PUBLIEES['erlacher_schredl_2004']['squats_ecart_pct'] / 100.0)
    c = VALEURS_PUBLIEES['carlson_1978']
    res['carlson_rapport_estimation_sur_reel'] = c['estimation_moyenne_min'] / c['intervalle_reel_moyen_min']

    dk = res['dement_kleitman']
    er = res['erlacher']
    principal_set = {
        'erlacher_comptage': (er['comptage']['ln_F'], er['comptage']['se_ln_F_meta']),
        'erlacher_gymnastique': (er['gymnastique']['ln_F'], er['gymnastique']['se_ln_F_meta']),
        'dement_kleitman': (dk['frontiere_geometrique']['ln_F'], dk['frontiere_geometrique']['se_ln_F']),
    }
    res['meta'] = meta(principal_set)
    res['meta_sensibilite'] = {
        'marche_au_lieu_du_comptage': meta({**{k: v for k, v in principal_set.items() if k != 'erlacher_comptage'},
                                           'erlacher_marche': (er['marche']['ln_F'], er['marche']['se_ln_F_meta'])}),
        'frontiere_arithmetique': meta({**{k: v for k, v in principal_set.items() if k != 'dement_kleitman'},
                                       'dement_kleitman_10min': (dk['frontiere_arithmetique']['ln_F'],
                                                                 dk['frontiere_arithmetique']['se_ln_F'])}),
        'reves_lucides_seuls': meta({k: v for k, v in principal_set.items() if k != 'dement_kleitman'}),
        'dement_kleitman_seul_borne_sup_95': dk['frontiere_geometrique']['F_borne_sup_95'],
    }
    pires = [res['meta']['F_effets_aleatoires_borne_sup_95']] + [
        m['F_effets_aleatoires_borne_sup_95'] for k, m in res['meta_sensibilite'].items() if isinstance(m, dict)]
    res['meta_sensibilite']['borne_sup_95_la_plus_haute'] = max(pires)

    # verdict selon la règle
    m = res['meta']
    t = res['donnees_ouvertes_tononi']
    oui = (m['F_effets_aleatoires_borne_inf_95'] > 1.0
           or t['proportion_certaine_borne_inf_95'] > SEUIL_OUI_PROPORTION)
    X = m['F_effets_aleatoires_borne_sup_95']
    if oui:
        verdict = 'oui'
    elif X < SEUIL_NON_FACTEUR:
        verdict = 'non'
    else:
        verdict = 'indetermine'
    facteur_projet = 80 * 365.25 * 24 / 8
    res['verdict'] = {
        'reponse': verdict,
        'F_global': m['F_effets_aleatoires'],
        'X_borne_sup_95': X,
        'F_borne_inf_95': m['F_effets_aleatoires_borne_inf_95'],
        'facteur_necessaire_une_vie_en_une_nuit': facteur_projet,
        'ecart_au_facteur_necessaire': facteur_projet / X,
        'proportion_certaine_borne_sup_95_donnees_ouvertes': t['proportion_certaine_borne_sup_95'],
    }
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ICI / 'resultats.json'))
    args = ap.parse_args()
    res = principal()
    Path(args.out).write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    v = res['verdict']
    print(f"verdict : {v['reponse']} ; F = {v['F_global']:.3f} ; borne sup. 95 % = {v['X_borne_sup_95']:.3f}")


if __name__ == '__main__':
    main()
