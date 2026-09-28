#!/usr/bin/env python3
"""aeternam, test n° 4 : le hasard quantique trahit-il un générateur pseudo-aléatoire ?

Idée testée : une simulation « bon marché » tirerait les résultats des mesures
quantiques d'un générateur pseudo-aléatoire (PRNG), c'est-à-dire d'un algorithme
déterministe. Les PRNG rapides et simples laissent des traces mesurables ; un
PRNG cryptographique n'en laisse aucune que l'on sache détecter.

Données (toutes dans donnees/, refaites par telecharger.py, empreintes SHA-256
vérifiées ci-dessous) :
  parity  bits BRUTS (aucun post-traitement) d'un QRNG à photons intriqués :
          parité des comptages de quatre détecteurs (Kavulich, Van Deren,
          Schlosshauer, Phys. Lett. A 388, 127032, 2021 ; Zenodo 4440318).
  ibm     bits BRUTS de l'algorithme « Basic QRNG » (porte de Hadamard puis
          mesure d'un qubit) sur neuf ordinateurs quantiques IBM (Root et
          Becker, arXiv:2401.12250 ; Zenodo 10542216).
  anu     QRNG de l'ANU (fluctuations du vide) ; sortie HACHÉE par AES-128
          (Haw et al., Phys. Rev. Applied 3, 054004, 2015, annexe E).
  beacon  NIST Randomness Beacon 2.0 : localRandomValue = SHA-512 de deux
          générateurs physiques ou plus (NISTIR 8213, champ F9) ; HACHÉE.
Sur des données hachées, aucun test statistique ne peut voir la source : un
succès n'y mesure que la qualité du hachage. Seuls parity et ibm testent la
nature du hasard quantique lui-même.

Méthode (règle de décision fixée avant de lire les résultats) :
  Niveau 1, défauts génériques : batterie NIST SP 800-22 rév. 1a complète
    (15 tests, 188 p-valeurs par séquence de 10^6 bits), réimplémentée ici et
    vérifiée sur les valeurs publiées de l'annexe B du document (π, e, √2, √3).
    Un échec y signale un écart au hasard idéal, physique ou algorithmique,
    sans dire lequel.
  Niveau 2, signatures de pseudo-hasard :
    a. complexité linéaire (Berlekamp-Massey) de segments de 50 000 bits, lus
       en continu et décimés par 48 et 64 (un bit sur 48 ou 64). Tout
       générateur linéaire sur GF(2) (LFSR, Mersenne Twister, etc.) dont
       l'état fait moins de 25 000 bits et dont la taille de mot divise 48 ou
       64 donne L < n/2 ; p-valeur exacte (énumération vérifiée) ;
    b. répétitions : toute fenêtre de 64 bits répétée, à tout décalage (période
       ou graine réutilisée) ; p-valeur de Poisson avec le biais mesuré ;
    c. corrélations à longue portée : autocorrélation aux décalages 17 à 65 536.
  Correction pour tests multiples : Holm, risque global 1 %, séparément pour
  chaque niveau. Verdict « trace de pseudo-hasard » = OUI si le niveau 2
  rejette sur une source quantique brute (parity ou ibm).
  Analyse secondaire (décidée après lecture des données, famille de Holm à
  part) : IBM sans la machine Belem, dont la sortie reste bloquée à 0 ou à 1
  pendant des essais entiers de 8 192 tirs ; le verdict retient ce cas, la
  règle initiale appliquée aux données publiées est aussi rapportée.
  Contrôles : la même chaîne est appliquée à des générateurs connus : LFSR de
  degré 20 et 31, LCG 32 bits, Mersenne Twister (doivent être détectés),
  PCG64, SHA-256 en mode compteur, décimales binaires de √2 (déterministes,
  mais ne doivent pas l'être : c'est la limite de toute la démarche).

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
DONNEES = ICI / 'donnees'

MACHINES_IBM = ('Belem', 'Jakarta', 'Lagos', 'Lima', 'Manila', 'Nairobi', 'Oslo', 'Perth', 'Quito')
BITS_IBM = (1048576, 1048576, 1048576, 2613248, 2662400, 1687552, 2097152, 1048576, 1048576)
OCTETS_ANU = 2_097_152
BEACON_PREMIERE = 1_950_000
BEACON_NOMBRE = 8192
TIRS_PAR_ESSAI = 8192
MACHINE_EXCLUE = 'Belem'      # analyse secondaire : sortie bloquée observée (voir essais_constants)

FICHIERS = {
    'parity_qrng.bin': {'sha256': 'f824345474637cb10745c414f96f179d2a976e6ca3aacc5ef615b148e98dbab9', 'octets': 800_000},
    'ibm_basic_qrng.bin': {'sha256': 'c3d5885c48206b3d4f00e9d33ed864c74b230a50197633e8935fdca984ad41d9', 'octets': sum(BITS_IBM) // 8},
    'anu_qrng.bin': {'sha256': '1e24b1a67e896e6c3287a23feb8e8f2fc9baed8ee1a202bc93b9423e49c1e5f8', 'octets': OCTETS_ANU},
    'nist_beacon.bin': {'sha256': '8672e66af9925a846a2e3c70ae894151e3a774c70b9a69e78d9c2d7094f4f325', 'octets': 128 * BEACON_NOMBRE},
}

GRAINE = 20260928
ALPHA = 0.01                  # risque global (Holm) de chaque famille de tests
N_SEQ = 1_000_000             # longueur d'une séquence NIST
N_BM = 50_000                 # longueur des segments de Berlekamp-Massey
DECIMATIONS = (1, 48, 64)
SEGMENTS_BM = {1: 8, 48: 2, 64: 2}
LAGS_COURTS = 16
LAG_MAX = 65_536
N_CONTROLE = 4_194_304        # bits par générateur de contrôle


# =================================================================== fonctions spéciales
def igamc(a: float, x: float) -> float:
    """Q(a, x), gamma incomplète supérieure régularisée (série et fraction continue)."""
    if x <= 0:
        return 1.0
    if x < a + 1:
        s = terme = 1.0 / a
        ap = a
        for _ in range(1_000_000):
            ap += 1
            terme *= x / ap
            s += terme
            if abs(terme) < abs(s) * 1e-16:
                break
        return max(0.0, 1.0 - s * math.exp(-x + a * math.log(x) - math.lgamma(a)))
    petit = 1e-300
    b = x + 1 - a
    c = 1 / petit
    d = 1 / b
    h = d
    for i in range(1, 1_000_000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = petit if abs(d) < petit else d
        c = b + an / c
        c = petit if abs(c) < petit else c
        d = 1 / d
        h *= d * c
        if abs(d * c - 1) < 1e-16:
            break
    return math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def phi(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2))


# =================================================================== NIST SP 800-22 rév. 1a
# Deux constantes diffèrent entre le texte du document et le code de référence
# qui a produit l'annexe B : on utilise le texte (valeurs exactes) pour
# l'analyse, et reference=True reproduit l'annexe B pour l'autotest.
PI_CHEV = (0.364091, 0.185659, 0.139381, 0.100571, 0.070432, 0.139865)          # § 2.8.4 et 3.8
PI_CHEV_REF = (0.367879, 0.183940, 0.137955, 0.099634, 0.069935, 0.140657)      # code de référence
PI_LC = (0.010417, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833)                 # § 2.10.4
PI_LC_REF = (0.01047, 0.03125, 0.125, 0.5, 0.25, 0.0625, 0.020833)              # code de référence


def t_frequence(e):
    n = len(e)
    return math.erfc(abs(2 * int(e.sum()) - n) / math.sqrt(2 * n))


def t_frequence_blocs(e, M=128):
    N = len(e) // M
    pi = e[:N * M].reshape(N, M).mean(axis=1)
    return igamc(N / 2, 2 * M * float(np.sum((pi - 0.5) ** 2)))


def t_sommes_cumulees(e, arriere=False):
    n = len(e)
    x = 2 * e.astype(np.int64) - 1
    z = int(np.max(np.abs(np.cumsum(x[::-1] if arriere else x))))
    r = math.sqrt(n)
    s1 = s2 = 0.0
    k = int((-n / z + 1) / 4)
    while k <= (n / z - 1) / 4:
        s1 += phi((4 * k + 1) * z / r) - phi((4 * k - 1) * z / r)
        k += 1
    k = int((-n / z - 3) / 4)
    while k <= (n / z - 1) / 4:
        s2 += phi((4 * k + 3) * z / r) - phi((4 * k + 1) * z / r)
        k += 1
    return 1.0 - s1 + s2


def t_suites(e):
    n = len(e)
    p = float(e.mean())
    if abs(p - 0.5) >= 2 / math.sqrt(n):          # prérequis non rempli : échec (§ 2.3.4)
        return 0.0
    V = 1 + int(np.count_nonzero(e[1:] != e[:-1]))
    return math.erfc(abs(V - 2 * n * p * (1 - p)) / (2 * math.sqrt(2 * n) * p * (1 - p)))


def t_plus_longue_suite(e):
    n = len(e)
    if n >= 750_000:
        M, lo, hi, pi = 10_000, 10, 16, (0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727)
    else:
        M, lo, hi, pi = 128, 4, 9, (0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124)
    N = n // M
    pad = np.zeros((N, M + 2), np.int8)
    pad[:, 1:-1] = e[:N * M].reshape(N, M)
    d = np.diff(pad, axis=1)
    r0, c0 = np.nonzero(d == 1)
    _, c1 = np.nonzero(d == -1)
    lmax = np.zeros(N, np.int64)
    np.maximum.at(lmax, r0, c1 - c0)
    nu = np.bincount(np.clip(lmax, lo, hi) - lo, minlength=hi - lo + 1)
    pi = np.array(pi)
    return igamc((len(pi) - 1) / 2, float(np.sum((nu - N * pi) ** 2 / (N * pi))) / 2)


def rangs_gf2(lignes: np.ndarray, ncol: int) -> np.ndarray:
    """Rang sur GF(2) de chaque matrice d'un lot ; lignes : (lot, nlignes) en uint64."""
    m = lignes.copy()
    lot, nl = m.shape
    rang = np.zeros(lot, np.int64)
    tous = np.arange(lot)
    for col in range(ncol - 1, -1, -1):
        bit = np.uint64(1) << np.uint64(col)
        cand = ((m & bit) != 0) & (np.arange(nl)[None, :] >= rang[:, None])
        s = tous[cand.any(axis=1)]
        if len(s) == 0:
            continue
        piv = np.argmax(cand[s], axis=1)
        pl = m[s, piv].copy()
        m[s, piv] = m[s, rang[s]]
        m[s, rang[s]] = pl
        a = (m[s] & bit) != 0
        a[np.arange(len(s)), rang[s]] = False
        m[s] = np.where(a, m[s] ^ pl[:, None], m[s])
        rang[s] += 1
    return rang


def proba_rang(r, M=32, Q=32):
    p = 2.0 ** (r * (Q + M - r) - M * Q)
    for i in range(r):
        p *= (1 - 2.0 ** (i - Q)) * (1 - 2.0 ** (i - M)) / (1 - 2.0 ** (i - r))
    return p


def t_rang(e, M=32, Q=32):
    N = len(e) // (M * Q)
    b = e[:N * M * Q].reshape(N, M, Q).astype(np.uint64)
    lignes = (b << np.arange(Q - 1, -1, -1, dtype=np.uint64)).sum(axis=2, dtype=np.uint64)
    r = rangs_gf2(lignes, Q)
    p32, p31 = proba_rang(32), proba_rang(31)
    F = (int(np.sum(r == 32)), int(np.sum(r == 31)))
    F = F + (N - F[0] - F[1],)
    P = (p32, p31, 1 - p32 - p31)
    return math.exp(-sum((f - p * N) ** 2 / (p * N) for f, p in zip(F, P)) / 2)


def t_spectrale(e):
    n = len(e)
    m = np.abs(np.fft.rfft(2.0 * e - 1.0))[: n // 2]
    N1 = int(np.sum(m < math.sqrt(math.log(1 / 0.05) * n)))
    d = (N1 - 0.95 * n / 2) / math.sqrt(n * 0.95 * 0.05 / 4)
    return math.erfc(abs(d) / math.sqrt(2))


def fenetres(e, m, circulaire=False):
    """Valeur de chaque fenêtre de m bits (bit de tête = poids fort)."""
    x = e.astype(np.int64)
    if circulaire:
        x = np.concatenate([x, x[: m - 1]])
    n = len(x) - m + 1
    v = np.zeros(n, np.int64)
    for i in range(m):
        v = (v << 1) | x[i:i + n]
    return v


def gabarits_aperiodiques(m=9):
    """Gabarits sans auto-recouvrement (148 pour m = 9, comme le fichier template9 du NIST)."""
    out = []
    for t in range(2 ** m):
        b = [(t >> (m - 1 - i)) & 1 for i in range(m)]
        if all(b[k:] != b[:m - k] for k in range(1, m)):
            out.append(t)
    return out


GABARITS_9 = gabarits_aperiodiques(9)


def t_gabarits_non_chevauchants(e, m=9, N=8):
    """Un gabarit apériodique ne peut pas chevaucher sa propre occurrence :
    le comptage non chevauchant du NIST est donc le comptage de toutes les fenêtres."""
    M = len(e) // N
    mu = (M - m + 1) / 2 ** m
    var = M * (1 / 2 ** m - (2 * m - 1) / 2 ** (2 * m))
    W = np.stack([np.bincount(fenetres(e[j * M:(j + 1) * M], m), minlength=2 ** m) for j in range(N)])
    chi2 = np.sum((W[:, GABARITS_9] - mu) ** 2, axis=0) / var
    return [igamc(N / 2, float(c) / 2) for c in chi2]


def t_gabarit_chevauchant(e, m=9, M=1032, reference=False):
    N = len(e) // M
    b = e[:N * M].reshape(N, M)
    v = np.ones((N, M - m + 1), bool)
    for i in range(m):
        v &= b[:, i:i + M - m + 1] == 1
    nu = np.bincount(np.minimum(v.sum(axis=1), 5), minlength=6)
    pi = np.array(PI_CHEV_REF if reference else PI_CHEV)
    return igamc(2.5, float(np.sum((nu - N * pi) ** 2 / (N * pi))) / 2)


def t_universel(e, L=7, Q=1280):
    K = len(e) // L - Q
    b = e[: (Q + K) * L].reshape(-1, L).astype(np.int64)
    v = (b << np.arange(L - 1, -1, -1)).sum(axis=1)
    num = np.arange(1, Q + K + 1)
    ordre = np.argsort(v, kind='stable')
    meme = np.concatenate([[False], v[ordre][1:] == v[ordre][:-1]])
    prec = np.zeros(Q + K, np.int64)
    prec[ordre] = np.where(meme, np.concatenate([[0], num[ordre][:-1]]), 0)
    fn = float(np.sum(np.log2(num[Q:] - prec[Q:]))) / K
    attendu, variance = 6.1962507, 3.125
    c = 0.7 - 0.8 / L + (4 + 32 / L) * K ** (-3 / L) / 15
    return math.erfc(abs(fn - attendu) / (math.sqrt(2) * c * math.sqrt(variance / K)))


def _phi_m(e, m):
    c = np.bincount(fenetres(e, m, circulaire=True), minlength=2 ** m) / len(e)
    c = c[c > 0]
    return float(np.sum(c * np.log(c)))


def t_entropie_approchee(e, m=10):
    n = len(e)
    apen = _phi_m(e, m) - _phi_m(e, m + 1)
    return igamc(2 ** (m - 1), n * (math.log(2) - apen))


def _psi2(e, m):
    if m <= 0:
        return 0.0
    n = len(e)
    c = np.bincount(fenetres(e, m, circulaire=True), minlength=2 ** m).astype(np.float64)
    return 2 ** m / n * float(np.sum(c * c)) - n


def t_serie(e, m=16):
    p0, p1, p2 = _psi2(e, m), _psi2(e, m - 1), _psi2(e, m - 2)
    return [igamc(2 ** (m - 2), (p0 - p1) / 2), igamc(2 ** (m - 3), (p0 - 2 * p1 + p2) / 2)]


def bm_lot(b: np.ndarray) -> np.ndarray:
    """Berlekamp-Massey sur GF(2), vectorisé sur les lignes de b (lot, M)."""
    lot, M = b.shape
    b = b.astype(np.uint8)
    C = np.zeros((lot, M + 1), np.uint8)
    B = np.zeros((lot, M + 1), np.uint8)
    C[:, 0] = B[:, 0] = 1
    L = np.zeros(lot, np.int64)
    mm = -np.ones(lot, np.int64)
    lignes = np.arange(lot)
    for N in range(M):
        d = (np.sum(C[:, :N + 1] & b[:, N::-1], axis=1) & 1).astype(bool)
        if not d.any():
            continue
        s = lignes[d]
        T = C[s].copy()
        dec = N - mm[s]
        for k in np.unique(dec):
            sk = s[dec == k]
            C[sk, k:] ^= B[sk, :M + 1 - k]
        maj = 2 * L[s] <= N
        sm = s[maj]
        L[sm] = N + 1 - L[sm]
        mm[sm] = N
        B[sm] = T[maj]
    return L


def t_complexite_lineaire(e, M=500, reference=False):
    N = len(e) // M
    L = bm_lot(e[:N * M].reshape(N, M))
    mu = M / 2 + (9 + (-1) ** (M + 1)) / 36 - (M / 3 + 2 / 9) / 2 ** M
    T = (-1) ** M * (L - mu) + 2 / 9
    nu = np.bincount(np.searchsorted([-2.5, -1.5, -0.5, 0.5, 1.5, 2.5], T, side='left'), minlength=7)
    pi = np.array(PI_LC_REF if reference else PI_LC)
    return igamc(3, float(np.sum((nu - N * pi) ** 2 / (N * pi))) / 2)


def _cycles(e):
    S = np.concatenate([[0], np.cumsum(2 * e.astype(np.int64) - 1), [0]])
    zeros = np.nonzero(S == 0)[0]
    J = len(zeros) - 1
    cyc = np.searchsorted(zeros, np.arange(len(S)), side='right') - 1
    return S, J, cyc


def t_excursions(e):
    S, J, cyc = _cycles(e)
    if J < max(0.005 * math.sqrt(len(e)), 500):
        return {}           # trop peu de cycles : test interrompu (§ 2.14.4, étape 4)
    ps = {}
    for x in (-4, -3, -2, -1, 1, 2, 3, 4):
        a = 1 / (2 * abs(x))
        pi = np.array([1 - a] + [a * a * (1 - a) ** (k - 1) for k in range(1, 5)] + [a * (1 - a) ** 4])
        nu = np.bincount(np.minimum(np.bincount(cyc[S == x], minlength=J + 1)[:J], 5), minlength=6)
        ps[x] = igamc(2.5, float(np.sum((nu - J * pi) ** 2 / (J * pi))) / 2)
    return ps


def t_excursions_variante(e):
    S, J, _ = _cycles(e)
    if J < max(0.005 * math.sqrt(len(e)), 500):
        return {}
    return {x: math.erfc(abs(int(np.sum(S == x)) - J) / math.sqrt(2 * J * (4 * abs(x) - 2)))
            for x in list(range(-9, 0)) + list(range(1, 10))}


def batterie(e: np.ndarray, reference: bool = False) -> dict[str, list[float]]:
    """Les 15 tests ; chaque entrée est la liste de ses p-valeurs (188 au total si tout s'applique)."""
    exc = t_excursions(e)
    excv = t_excursions_variante(e)
    return {
        'frequence': [t_frequence(e)],
        'frequence_blocs_M128': [t_frequence_blocs(e)],
        'sommes_cumulees': [t_sommes_cumulees(e), t_sommes_cumulees(e, True)],
        'suites': [t_suites(e)],
        'plus_longue_suite': [t_plus_longue_suite(e)],
        'rang_32x32': [t_rang(e)],
        'spectrale_dft': [t_spectrale(e)],
        'gabarits_non_chevauchants_m9': t_gabarits_non_chevauchants(e),
        'gabarit_chevauchant_m9': [t_gabarit_chevauchant(e, reference=reference)],
        'universel_maurer': [t_universel(e)],
        'entropie_approchee_m10': [t_entropie_approchee(e)],
        'excursions': [exc[x] for x in sorted(exc)],
        'excursions_variante': [excv[x] for x in sorted(excv)],
        'complexite_lineaire_M500': [t_complexite_lineaire(e, reference=reference)],
        'serie_m16': t_serie(e),
    }


# Annexe B de SP 800-22 rév. 1a : p-valeurs publiées pour 10^6 bits de chaque constante.
ORDRE_ANNEXE_B = ('frequence', 'blocs', 'cusum_avant', 'cusum_arriere', 'suites', 'plus_longue', 'rang',
                  'dft', 'gabarit_000000001', 'chevauchant', 'universel', 'entropie', 'excursion_x+1',
                  'variante_x-1', 'complexite_lineaire', 'serie_delta1')
ANNEXE_B = {
    'pi': (0.578211, 0.380615, 0.628308, 0.663369, 0.419268, 0.024390, 0.083553, 0.010186, 0.165757,
           0.296897, 0.669012, 0.361595, 0.844143, 0.760966, 0.255475, 0.143005),
    'e': (0.953749, 0.211072, 0.669887, 0.724266, 0.561917, 0.718945, 0.306156, 0.847187, 0.078790,
          0.110434, 0.282568, 0.700073, 0.786868, 0.826009, 0.826335, 0.766182),
    'sqrt2': (0.811881, 0.833222, 0.879009, 0.957206, 0.313427, 0.012117, 0.823810, 0.581909, 0.569461,
              0.791982, 0.130805, 0.884740, 0.216235, 0.566118, 0.317127, 0.861925),
    'sqrt3': (0.610051, 0.473961, 0.917121, 0.689519, 0.261123, 0.446726, 0.314498, 0.776046, 0.532235,
              0.082716, 0.165981, 0.180481, 0.783283, 0.155066, 0.346469, 0.157500),
}


def extraire_annexe_b(r: dict) -> tuple:
    return (r['frequence'][0], r['frequence_blocs_M128'][0], r['sommes_cumulees'][0], r['sommes_cumulees'][1],
            r['suites'][0], r['plus_longue_suite'][0], r['rang_32x32'][0], r['spectrale_dft'][0],
            r['gabarits_non_chevauchants_m9'][GABARITS_9.index(1)], r['gabarit_chevauchant_m9'][0],
            r['universel_maurer'][0], r['entropie_approchee_m10'][0], r['excursions'][4],
            r['excursions_variante'][8], r['complexite_lineaire_M500'][0], r['serie_m16'][0])


# =================================================================== niveau 2 : tests ciblés
def berlekamp_massey(bits: np.ndarray) -> int:
    """Complexité linéaire d'une longue suite (entiers Python comme vecteurs de bits)."""
    s = bits.tolist()
    C = B = 1
    L, m, W = 0, -1, 0
    for N, b in enumerate(s):
        W = (W << 1) | b                       # bit j de W = s[N - j]
        if (C & W).bit_count() & 1:
            T = C
            C ^= B << (N - m)
            if 2 * L <= N:
                L, B, m = N + 1 - L, T, N
    return L


def p_complexite_basse(n: int, L: int) -> float:
    """P(L(s) <= L) pour s uniforme de n bits (Rueppel) : il y a une suite de complexité 0 et
    2^min(2n-2l, 2l-1) suites de complexité l pour 1 <= l <= n."""
    if 2 * L <= n:                       # tous les termes valent 2^(2l-1)
        tot = 1 + 2 * ((1 << (2 * L)) - 1) // 3
    else:                                # complément : termes 2^(2n-2l) pour l > L
        tot = (1 << n) - ((1 << (2 * (n - L))) - 1) // 3
    return float(Fraction(tot, 1 << n))


def log10_p_complexite_basse(n: int, L: int) -> float:
    p = p_complexite_basse(n, L)
    if p > 0:
        return math.log10(p)
    return (2 * L - 1 - n) * math.log10(2) + math.log10(4 / 3)


def segments_bm(bits: np.ndarray, d: int, nmax: int) -> list[np.ndarray]:
    """Segments disjoints répartis régulièrement sur tout le jeu de données."""
    long = d * N_BM
    k = min(nmax, len(bits) // long)
    debuts = [0] if k == 1 else [i * ((len(bits) - long) // (k - 1)) for i in range(k)]
    return [bits[a:a + long:d] for a in debuts]


def test_complexite(bits: np.ndarray) -> list[dict]:
    out = []
    for d in DECIMATIONS:
        for k, seg in enumerate(segments_bm(bits, d, SEGMENTS_BM[d])):
            L = berlekamp_massey(seg)
            out.append({'decimation': d, 'segment': k, 'n': len(seg), 'L': L,
                        'p': p_complexite_basse(len(seg), L), 'log10_p': log10_p_complexite_basse(len(seg), L)})
    return out


def mots64(bits: np.ndarray) -> np.ndarray:
    """Fenêtre de 64 bits commençant à chaque position multiple de 1 (tous les décalages)."""
    o = np.packbits(bits).astype(np.uint64)
    n = len(o) - 8
    base = np.zeros(n, np.uint64)
    for k in range(8):
        base |= o[k:k + n] << np.uint64(56 - 8 * k)
    suiv = o[8:8 + n]
    parts = [base]
    for s in range(1, 8):
        parts.append((base << np.uint64(s)) | (suiv >> np.uint64(8 - s)))
    return np.concatenate(parts)


def test_repetitions(bits: np.ndarray) -> dict:
    w = np.sort(mots64(bits))
    egal = w[1:] == w[:-1]
    # nombre de paires de fenêtres identiques
    bords = np.flatnonzero(np.diff(np.concatenate([[0], egal.astype(np.int8), [0]])))
    tailles = (bords[1::2] - bords[::2]) + 1
    paires = int(np.sum(tailles * (tailles - 1) // 2))
    # Fenêtres « typiques » (entre 16 et 48 bits à 1) : une répétition de ces fenêtres ne peut
    # pas venir d'une longue suite de bits identiques (P < 3e-5 par fenêtre sous le hasard).
    valeurs = w[bords[::2]]
    poids = np.zeros(len(valeurs), np.int64)
    for k in range(64):
        poids += ((valeurs >> np.uint64(k)) & np.uint64(1)).astype(np.int64)
    typ = (poids >= 16) & (poids <= 48)
    paires_typiques = int(np.sum((tailles * (tailles - 1) // 2)[typ]))
    p1 = float(bits.mean())
    c = p1 * p1 + (1 - p1) ** 2
    nw = len(w)
    lam = nw * (nw - 1) / 2 * c ** 64
    return {'fenetres_64_bits': nw, 'paires_identiques': paires, 'attendu_poisson': lam,
            'p': poisson_queue(paires, lam), 'paires_identiques_fenetres_typiques': paires_typiques,
            'valeurs_repetees_distinctes': int(len(valeurs))}


def poisson_queue(k: int, lam: float) -> float:
    """P(X >= k) pour X de Poisson(lam) = gamma incomplète inférieure régularisée P(k, lam)."""
    if k == 0:
        return 1.0
    if lam >= k:
        return 1.0 - igamc(k, lam)
    s = terme = 1.0 / k
    a = k
    while terme > s * 1e-17:
        a += 1
        terme *= lam / a
        s += terme
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k) + math.log(s))


def autocorrelation(seqs: list[np.ndarray]) -> dict:
    S = np.zeros(LAG_MAX + 1)
    V = np.zeros(LAG_MAX + 1)
    for e in seqs:
        x = e.astype(np.float64)
        x -= x.mean()
        n = len(x)
        f = np.fft.rfft(x, 1 << (2 * n - 1).bit_length())
        ac = np.fft.irfft(f * np.conj(f))[: LAG_MAX + 1]
        S += ac
        s2 = float(np.mean(x * x))
        V += (n - np.arange(LAG_MAX + 1)) * s2 * s2
    z = S[1:] / np.sqrt(V[1:])
    lags = np.arange(1, LAG_MAX + 1)

    def groupe(masque):
        zz = np.abs(z[masque])
        i = int(np.argmax(zz))
        pmin = math.erfc(zz[i] / math.sqrt(2))
        return {'lag_max_z': int(lags[masque][i]), 'z_max': float(z[masque][i]),
                'p_min': pmin, 'p_bonferroni': min(1.0, pmin * int(masque.sum())), 'n_lags': int(masque.sum())}

    return {'r_lag1': float(S[1] / S[0]),
            'courte_portee_1_16': groupe(lags <= LAGS_COURTS),
            'longue_portee_17_65536': groupe(lags > LAGS_COURTS),
            'z_lags_1_8': [float(v) for v in z[:8]]}


# =================================================================== générateurs de contrôle
def lfsr(n: int, deg: int, prise: int, rng) -> np.ndarray:
    """s[t] = s[t-deg] xor s[t-prise] (trinôme x^deg + x^(deg-prise) + 1)."""
    s = np.zeros(n + deg, np.uint8)
    s[:deg] = rng.integers(0, 2, deg)
    s[0] = 1
    pas = prise
    t = deg
    while t < n + deg:
        k = min(pas, n + deg - t)
        s[t:t + k] = s[t - deg:t - deg + k] ^ s[t - prise:t - prise + k]
        t += k
    return s[deg:]


def lcg32(n: int, graine: int) -> np.ndarray:
    x = graine & 0xFFFFFFFF
    mots = np.empty(n // 32, np.uint32)
    for i in range(len(mots)):
        x = (1664525 * x + 1013904223) & 0xFFFFFFFF
        mots[i] = x
    return np.unpackbits(mots.astype('>u4').view(np.uint8))


def mt19937(n: int, graine: int) -> np.ndarray:
    return np.unpackbits(np.frombuffer(np.random.RandomState(graine).bytes(n // 8), np.uint8))


def pcg64(n: int, graine: int) -> np.ndarray:
    return np.unpackbits(np.frombuffer(np.random.default_rng(graine).bytes(n // 8), np.uint8))


def sha256_compteur(n: int, graine: int) -> np.ndarray:
    cle = graine.to_bytes(8, 'big')
    b = b''.join(hashlib.sha256(cle + i.to_bytes(8, 'big')).digest() for i in range(n // 256))
    return np.unpackbits(np.frombuffer(b, np.uint8))


def bits_entier(v: int, n: int) -> np.ndarray:
    s = bin(v)[2:2 + n]
    assert len(s) == n
    return np.frombuffer(s.encode(), np.uint8) - 48


def racine_bits(k: int, n: int) -> np.ndarray:
    """Développement binaire de √k (bit de la partie entière compris), comme data.sqrt2 du NIST."""
    return bits_entier(math.isqrt(k << (2 * n + 8)), n)


def e_bits(n: int) -> np.ndarray:
    def bs(a, b):
        if b - a == 1:
            return 1, b
        m = (a + b) // 2
        p1, q1 = bs(a, m)
        p2, q2 = bs(m, b)
        return p1 * q2 + p2, q1 * q2
    k = 16
    while math.lgamma(k + 1) / math.log(2) < n + 64:
        k *= 2
    p, q = bs(0, k)
    return bits_entier(((p + q) << (n + 8)) // q, n)


def pi_bits(n: int) -> np.ndarray:
    """Chudnovsky, séparation binaire."""
    C3 = 640320 ** 3 // 24

    def bs(a, b):
        if b - a == 1:
            P = Q = 1 if a == 0 else None
            if a:
                P = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Q = a * a * a * C3
            T = P * (13591409 + 545140134 * a)
            return P, Q, -T if a & 1 else T
        m = (a + b) // 2
        P1, Q1, T1 = bs(a, m)
        P2, Q2, T2 = bs(m, b)
        return P1 * P2, Q1 * Q2, T1 * Q2 + P1 * T2
    _, Q, T = bs(0, int(n / 47.11) + 2)
    prec = n + 64
    return bits_entier((Q * 426880 * math.isqrt(10005 << (2 * prec))) // T, n)


def von_neumann(bits: np.ndarray) -> np.ndarray:
    a, b = bits[0:len(bits) - 1:2], bits[1::2]
    return a[a != b]


# =================================================================== données
def lire(nom: str) -> bytes:
    brut = (DONNEES / nom).read_bytes()
    emp = hashlib.sha256(brut).hexdigest()
    if emp != FICHIERS[nom]['sha256'] or len(brut) != FICHIERS[nom]['octets']:
        raise SystemExit(f'{nom} modifié : sha256 {emp}, {len(brut)} octets')
    return brut


def charger() -> dict:
    bits = lambda b: np.unpackbits(np.frombuffer(b, np.uint8))
    ibm = bits(lire('ibm_basic_qrng.bin'))
    bornes = np.cumsum((0,) + BITS_IBM)
    beacon = np.frombuffer(lire('nist_beacon.bin'), np.uint8).reshape(BEACON_NOMBRE, 2, 64)
    # Chaîne d'engagements : precommitmentValue(i) = SHA-512(localRandomValue(i+1)) (NISTIR 8213, F18).
    chaine = sum(hashlib.sha512(beacon[i + 1, 0].tobytes()).digest() == beacon[i, 1].tobytes()
                 for i in range(BEACON_NOMBRE - 1))
    par_machine = {m: ibm[bornes[i]:bornes[i + 1]] for i, m in enumerate(MACHINES_IBM)}
    # Essais IBM (8 192 tirs chacun, Root et Becker § II.D) « bloqués » : sortie constante
    # (tous les bits égaux) ou quasi constante (moins de 1 % de l'autre valeur).
    constants = {}
    for m, b in par_machine.items():
        moy = b.reshape(-1, TIRS_PAR_ESSAI).mean(axis=1)
        constants[m] = {'n_essais': int(len(moy)),
                        'tous_a_0': np.flatnonzero(moy == 0).tolist(), 'tous_a_1': np.flatnonzero(moy == 1).tolist(),
                        'quasi_constants': np.flatnonzero((moy > 0) & (moy < 1) & (np.abs(moy - 0.5) > 0.49)).tolist()}
    sans = [m for m in MACHINES_IBM if m != MACHINE_EXCLUE]
    return {
        'parity': {'bits': bits(lire('parity_qrng.bin')), 'hache': False, 'par_machine': None},
        'ibm': {'bits': ibm, 'hache': False, 'par_machine': par_machine, 'essais_constants': constants},
        'anu': {'bits': bits(lire('anu_qrng.bin')), 'hache': True, 'par_machine': None},
        'beacon': {'bits': np.unpackbits(np.ascontiguousarray(beacon[:, 0]).reshape(-1)), 'hache': True,
                   'par_machine': None, 'chaine_verifiee': int(chaine)},
        'ibm_sans_belem': {'bits': np.concatenate([par_machine[m] for m in sans]), 'hache': False,
                           'par_machine': {m: par_machine[m] for m in sans}},
    }


def sequences_nist(jeu: dict) -> list[tuple[str, np.ndarray]]:
    parts = jeu['par_machine'] or {'': jeu['bits']}
    out = []
    for nom, b in parts.items():
        for k in range(len(b) // N_SEQ):
            out.append((f'{nom}{"#" if nom else ""}{k}', b[k * N_SEQ:(k + 1) * N_SEQ]))
    return out


# =================================================================== statistiques
def holm(ps: list[float]) -> np.ndarray:
    p = np.asarray(ps, float)
    m = len(p)
    o = np.argsort(p, kind='stable')
    adj = np.minimum(1.0, np.maximum.accumulate((m - np.arange(m)) * p[o]))
    out = np.empty(m)
    out[o] = adj
    return out


def analyser(bits: np.ndarray, seqs: list[tuple[str, np.ndarray]]) -> dict:
    nist = []
    for nom, e in seqs:
        for test, ps in batterie(e).items():
            for j, p in enumerate(ps):
                nist.append({'sequence': nom, 'test': test, 'indice': j, 'p': p})
    cible = []
    for c in test_complexite(bits):
        cible.append({'test': f'complexite_lineaire_d{c["decimation"]}', **c})
    rep = test_repetitions(bits)
    cible.append({'test': 'repetitions_64_bits', **rep})
    ac = autocorrelation([e for _, e in seqs] or [bits])
    cible.append({'test': 'autocorrelation_17_65536', 'p': ac['longue_portee_17_65536']['p_bonferroni']})
    p1 = float(bits.mean())
    return {
        'n_bits': int(len(bits)),
        'fraction_de_1': p1,
        'z_biais': (p1 - 0.5) * 2 * math.sqrt(len(bits)),
        'min_entropie_par_bit': -math.log2(max(p1, 1 - p1)),
        'n_sequences_nist': len(seqs),
        'nist': nist,
        'cible': cible,
        'autocorrelation': ac,
        'complexite': [c for c in cible if c['test'].startswith('complexite')],
        'repetitions': rep,
    }


def resume_nist(nist: list[dict], adj: np.ndarray) -> dict:
    out = {}
    for i, r in enumerate(nist):
        t = out.setdefault(r['test'], {'n_p': 0, 'n_p_inf_0_01': 0, 'p_min': 1.0, 'p_holm_min': 1.0})
        t['n_p'] += 1
        t['n_p_inf_0_01'] += r['p'] < 0.01
        t['p_min'] = min(t['p_min'], r['p'])
        t['p_holm_min'] = min(t['p_holm_min'], float(adj[i]))
    return out


def famille(jeux: dict, cle: str) -> dict:
    """Holm sur toutes les p-valeurs d'une famille, tous jeux confondus."""
    etiquettes, ps = [], []
    for nom, r in jeux.items():
        for x in r[cle]:
            etiquettes.append(nom)
            ps.append(x['p'])
    adj = holm(ps)
    par = {}
    for nom in jeux:
        a = adj[[i for i, e in enumerate(etiquettes) if e == nom]]
        par[nom] = {'n_p': int(len(a)), 'p_holm_min': float(a.min()), 'rejets': int(np.sum(a < ALPHA))}
    return {'n_p': len(ps), 'rejets': int(np.sum(adj < ALPHA)), 'par_jeu': par, 'adj': adj, 'etiquettes': etiquettes}


def detecte(r: dict) -> dict:
    a1 = holm([x['p'] for x in r['nist']])
    a2 = holm([x['p'] for x in r['cible']])
    return {'niveau1_p_holm_min': float(a1.min()), 'niveau1_rejets': int(np.sum(a1 < ALPHA)),
            'niveau2_p_holm_min': float(a2.min()), 'niveau2_rejets': int(np.sum(a2 < ALPHA)),
            'detecte_niveau1': bool(a1.min() < ALPHA), 'detecte_niveau2': bool(a2.min() < ALPHA)}


# =================================================================== autotests
def autotests(rng) -> dict:
    t0 = time.time()
    out = {}
    # 1. Fonctions spéciales.
    assert abs(igamc(1, 2) - math.exp(-2)) < 1e-14
    assert abs(igamc(0.5, 2) - math.erfc(math.sqrt(2))) < 1e-13
    assert abs(igamc(3, 30) - math.exp(-30) * (1 + 30 + 450)) < 1e-20
    # 2. 148 gabarits apériodiques de 9 bits, comme le fichier template9 du NIST.
    assert len(GABARITS_9) == 148 and GABARITS_9[0] == 1
    # 3. Rang sur GF(2) : contre une élimination naïve.
    lots = rng.integers(0, 2, (50, 32, 32)).astype(np.uint64)
    lots[:5, 31] = lots[:5, 0] ^ lots[:5, 1]
    lignes = (lots << np.arange(31, -1, -1, dtype=np.uint64)).sum(axis=2, dtype=np.uint64)
    for k in range(50):
        a = [int(v) for v in lignes[k]]
        r = 0
        for col in range(31, -1, -1):
            piv = next((i for i in range(r, 32) if a[i] >> col & 1), None)
            if piv is None:
                continue
            a[r], a[piv] = a[piv], a[r]
            a = [a[i] ^ a[r] if i != r and a[i] >> col & 1 else a[i] for i in range(32)]
            r += 1
        assert rangs_gf2(lignes[k:k + 1], 32)[0] == r
    assert abs(proba_rang(32) - 0.2888) < 1e-4 and abs(proba_rang(31) - 0.5776) < 1e-4
    # 4. Berlekamp-Massey : distribution exacte vérifiée par énumération (n = 12),
    #    accord des deux implémentations, LFSR de degré connu.
    n = 12
    toutes = ((np.arange(2 ** n)[:, None] >> np.arange(n - 1, -1, -1)) & 1).astype(np.uint8)
    Ls = bm_lot(toutes)
    compte = np.bincount(Ls, minlength=n + 1)
    theorie = [1] + [2 ** min(2 * n - 2 * l, 2 * l - 1) for l in range(1, n + 1)]
    assert compte.tolist() == theorie
    for l in range(n + 1):
        assert abs(p_complexite_basse(n, l) - compte[:l + 1].sum() / 2 ** n) < 1e-15
    assert abs(p_complexite_basse(50_000, 24_990) / (2 / 3 * 2.0 ** (2 * 24_990 - 50_000)) - 1) < 1e-12
    assert p_complexite_basse(50_000, 25_010) > 0.99
    for k in range(20):
        s = rng.integers(0, 2, 300).astype(np.uint8)
        assert berlekamp_massey(s) == bm_lot(s[None, :])[0]
    assert berlekamp_massey(lfsr(2000, 31, 28, rng)) == 31
    assert berlekamp_massey(lfsr(2000, 20, 17, rng)) == 20
    #    Une source physique biaisée et corrélée (Markov, p(répétition) = 0,6, 47 % de 1)
    #    garde une complexité voisine de n/2 : le test ne confond pas défaut et algorithme.
    x = np.empty(20_000, np.uint8)
    u = rng.random(20_000)
    x[0] = 0
    for i in range(1, 20_000):
        x[i] = x[i - 1] if u[i] < 0.6 else 1 - x[i - 1]
    x[(x == 1) & (rng.random(20_000) < 0.06)] = 0
    L_markov = berlekamp_massey(x)
    assert abs(L_markov - 10_000) <= 12, L_markov
    out['bm_markov_biaise_L_sur_n'] = L_markov / 20_000
    # 5. LFSR de degré 20 : période exacte 2^20 - 1 (trinôme primitif).
    s = lfsr(2_200_000, 20, 17, rng)
    P = 2 ** 20 - 1
    assert np.array_equal(s[P:], s[:-P])
    # 6. Fenêtres de 64 bits à tous les décalages.
    b = rng.integers(0, 2, 4096).astype(np.uint8)
    w = mots64(b)
    for i in (0, 1, 7, 8, 13, 1000):
        s_ = int(''.join(map(str, b[i:i + 64])), 2)
        assert s_ in set(w.tolist())
    assert test_repetitions(np.concatenate([b, b[:200]]))['paires_identiques'] >= 1
    # 7. Autocorrélation : un signal injecté au décalage 1000 est retrouvé.
    e = rng.integers(0, 2, 200_000).astype(np.uint8)
    copie = rng.random(199_000) < 0.05
    e[1000:][copie] = e[:-1000][copie]
    ac = autocorrelation([e])
    assert ac['longue_portee_17_65536']['lag_max_z'] == 1000
    # 8. Batterie NIST : reproduction de l'annexe B de SP 800-22 (10^6 bits de π, e, √2, √3).
    consts = {'sqrt2': racine_bits(2, N_SEQ), 'sqrt3': racine_bits(3, N_SEQ), 'e': e_bits(N_SEQ), 'pi': pi_bits(N_SEQ)}
    assert ''.join(map(str, consts['pi'][:16])) == '1100100100001111'
    ecart_max = 0.0
    ecart_max_chev = 0.0
    for nom, bits in consts.items():
        obtenu = extraire_annexe_b(batterie(bits, reference=True))
        for cle, p, ref in zip(ORDRE_ANNEXE_B, obtenu, ANNEXE_B[nom]):
            ec = abs(p - ref)
            if cle == 'chevauchant':
                ecart_max_chev = max(ecart_max_chev, ec)
                assert ec < 3e-5, (nom, cle, p, ref)
            else:
                ecart_max = max(ecart_max, ec)
                assert ec < 1.5e-6, (nom, cle, p, ref)
    out.update({'annexe_b_valeurs_verifiees': 4 * len(ORDRE_ANNEXE_B), 'annexe_b_ecart_max': ecart_max,
                'annexe_b_ecart_max_chevauchant': ecart_max_chev, 'duree_s': time.time() - t0})
    return out


# =================================================================== calcul principal
def controles(rng) -> dict:
    gens = {
        'lfsr_degre_20': ('LFSR, trinôme x^20 + x^3 + 1 (période 1 048 575 bits)', True,
                          lambda: lfsr(N_CONTROLE, 20, 17, rng)),
        'lfsr_degre_31': ('LFSR, trinôme x^31 + x^3 + 1', True, lambda: lfsr(N_CONTROLE, 31, 28, rng)),
        'lcg_32_bits': ('LCG x <- 1664525 x + 1013904223 mod 2^32, mots de 32 bits', True,
                        lambda: lcg32(N_CONTROLE, GRAINE)),
        'mersenne_twister': ('MT19937 (numpy RandomState)', True, lambda: mt19937(N_CONTROLE, GRAINE)),
        'pcg64': ('PCG64 (numpy default_rng), non cryptographique', False, lambda: pcg64(N_CONTROLE, GRAINE)),
        'sha256_compteur': ('SHA-256 en mode compteur (cryptographique)', False,
                            lambda: sha256_compteur(N_CONTROLE, GRAINE)),
        'racine_de_2': ('décimales binaires de √2 (entièrement déterministes)', False,
                        lambda: racine_bits(2, N_CONTROLE)),
    }
    out = {}
    for nom, (desc, faible, fab) in gens.items():
        bits = fab()
        seqs = [(str(k), bits[k * N_SEQ:(k + 1) * N_SEQ]) for k in range(2)]
        r = analyser(bits, seqs)
        d = detecte(r)
        cx = {f'd{c["decimation"]}': min(x['L'] for x in r['complexite'] if x['decimation'] == c['decimation'])
              for c in r['complexite']}
        tests_rejetes = sorted({x['test'] for x, a in zip(r['nist'], holm([x['p'] for x in r['nist']])) if a < ALPHA})
        cibles_rejetes = sorted({x['test'] for x, a in zip(r['cible'], holm([x['p'] for x in r['cible']])) if a < ALPHA})
        out[nom] = {'description': desc, 'attendu_detecte': faible, **d,
                    'detecte': d['detecte_niveau1'] or d['detecte_niveau2'],
                    'tests_nist_rejetes': tests_rejetes, 'tests_cibles_rejetes': cibles_rejetes,
                    'complexite_min_par_decimation': cx, 'n_segment_bm': N_BM,
                    'complexite_log10_p_min': min(x['log10_p'] for x in r['complexite']),
                    'repetitions_paires': r['repetitions']['paires_identiques']}
    return out


def calculer() -> dict:
    t0 = time.time()
    rng = np.random.default_rng(GRAINE)
    tests = autotests(rng)
    jeux = charger()
    assert jeux['beacon']['chaine_verifiee'] == BEACON_NOMBRE - 1

    res = {}
    for nom, j in jeux.items():
        res[nom] = analyser(j['bits'], sequences_nist(j))

    # Familles de Holm : l'analyse principale porte sur les quatre jeux tels que publiés ;
    # l'analyse secondaire (IBM sans les essais constants, choix fait après lecture des
    # données) forme sa propre famille.
    principaux = ('parity', 'ibm', 'anu', 'beacon')
    secondaires = ('ibm_sans_belem',)
    f1, f2, detail, idx2 = {}, {}, {}, {}
    for groupe in (principaux, secondaires):
        g = {n: res[n] for n in groupe}
        a, b = famille(g, 'nist'), famille(g, 'cible')
        for nom in groupe:
            f1[nom], f2[nom] = a, b
            idx = [i for i, e in enumerate(a['etiquettes']) if e == nom]
            detail[nom] = resume_nist(res[nom]['nist'], a['adj'][idx])
            idx2[nom] = [i for i, e in enumerate(b['etiquettes']) if e == nom]
    fam_p1, fam_p2 = f1['parity'], f2['parity']

    # Diagnostic : les échecs du niveau 1 sur les sources brutes disparaissent-ils
    # après extraction de von Neumann (qui retire un biais constant) ?
    diag = {}
    for nom in ('parity', 'ibm', 'ibm_sans_belem'):
        vn = von_neumann(jeux[nom]['bits'])
        seqs = [(str(k), vn[k * N_SEQ:(k + 1) * N_SEQ]) for k in range(len(vn) // N_SEQ)]
        ps = [p for _, e in seqs for v in batterie(e).values() for p in v]
        a = holm(ps)
        diag[nom] = {'bits_apres_extraction': int(len(vn)), 'fraction_de_1': float(vn.mean()),
                     'n_sequences': len(seqs), 'n_p': len(ps), 'p_holm_min': float(a.min()) if len(a) else None,
                     'rejets': int(np.sum(a < ALPHA))}
    # Par machine IBM : biais et niveau 1 (Holm interne à chaque machine).
    machines = {}
    for m, b in jeux['ibm']['par_machine'].items():
        ps = [x['p'] for x in res['ibm']['nist'] if x['sequence'].startswith(m + '#')]
        p1 = float(b.mean())
        machines[m] = {'n_bits': int(len(b)), 'fraction_de_1': p1, 'z_biais': (p1 - 0.5) * 2 * math.sqrt(len(b)),
                       'repetition_bit_suivant': float(np.mean(b[1:] == b[:-1])),
                       'niveau1_p_holm_min': float(holm(ps).min()) if ps else None,
                       'niveau1_rejets': int(np.sum(holm(ps) < ALPHA)) if ps else 0}

    ctrl = controles(rng)
    for nom, c in ctrl.items():
        assert c['detecte'] == c['attendu_detecte'], (nom, c)

    donnees = {}
    for nom, j in jeux.items():
        r = res[nom]
        donnees[nom] = {
            'hache': j['hache'],
            'n_bits': r['n_bits'],
            'fraction_de_1': r['fraction_de_1'],
            'z_biais': r['z_biais'],
            'min_entropie_par_bit': r['min_entropie_par_bit'],
            'n_sequences_nist': r['n_sequences_nist'],
            'niveau1': {**f1[nom]['par_jeu'][nom],
                        'tests_rejetes': sorted(t for t, v in detail[nom].items() if v['p_holm_min'] < ALPHA),
                        'par_test': detail[nom]},
            'niveau2': {**f2[nom]['par_jeu'][nom],
                        'complexite': [{k: v for k, v in c.items() if k != 'test'} for c in r['complexite']],
                        'complexite_log10_p_min': min(c['log10_p'] for c in r['complexite']),
                        'complexite_ecart_max_a_n_sur_2': max(abs(c['L'] - c['n'] / 2) for c in r['complexite']),
                        'repetitions': r['repetitions'],
                        'autocorrelation': r['autocorrelation'],
                        'p_holm': {x['test'] + (f"_d{x['decimation']}_s{x['segment']}" if 'segment' in x else ''):
                                   float(f2[nom]['adj'][i]) for x, i in zip(r['cible'], idx2[nom])}},
        }
    donnees['beacon']['impulsions'] = f'chaîne 2, {BEACON_PREMIERE} à {BEACON_PREMIERE + BEACON_NOMBRE - 1}'
    donnees['beacon']['engagements_verifies'] = jeux['beacon']['chaine_verifiee']
    donnees['ibm']['par_machine'] = machines
    ec = jeux['ibm']['essais_constants']
    for m, v in ec.items():
        machines[m].update({'essais': v['n_essais'], 'essais_tous_a_0': v['tous_a_0'], 'essais_tous_a_1': v['tous_a_1'],
                            'essais_quasi_constants': v['quasi_constants']})
    bloques = {m: len(v['tous_a_0']) + len(v['tous_a_1']) + len(v['quasi_constants']) for m, v in ec.items()}
    donnees['ibm']['essais_bloques_par_machine'] = bloques
    donnees['ibm']['n_essais'] = int(sum(BITS_IBM) // TIRS_PAR_ESSAI)
    donnees['ibm']['n_essais_tous_egaux'] = sum(len(v['tous_a_0']) + len(v['tous_a_1']) for v in ec.values())
    donnees['ibm']['n_essais_tous_a_0'] = sum(len(v['tous_a_0']) for v in ec.values())
    donnees['ibm']['n_essais_tous_a_1'] = sum(len(v['tous_a_1']) for v in ec.values())
    donnees['ibm']['n_essais_quasi_constants'] = sum(len(v['quasi_constants']) for v in ec.values())
    assert all(bloques[m] == 0 for m in MACHINES_IBM if m != MACHINE_EXCLUE) and bloques[MACHINE_EXCLUE] > 0

    rejets_bruts = {n: f2[n]['par_jeu'][n]['rejets'] for n in ('parity', 'ibm')}
    rejets_nettoyes = {n: f2[n]['par_jeu'][n]['rejets'] for n in ('parity', 'ibm_sans_belem')}
    trace = any(v > 0 for v in rejets_nettoyes.values())
    # Aucune répétition de fenêtre typique nulle part : toutes les répétitions IBM sont des suites de bits égaux.
    rep_typ = {n: res[n]['repetitions']['paires_identiques_fenetres_typiques'] for n in principaux}
    return {
        'titre': 'Test n° 4 : le hasard quantique trahit-il un générateur pseudo-aléatoire ?',
        'date': '2026-09-28',
        'verdict': {
            'trace_de_pseudo_hasard': trace,
            'regle': 'OUI si un test ciblé (niveau 2 : complexité linéaire, répétitions, corrélations '
                     'à longue portée) rejette après correction de Holm (risque global 1 %) sur une source '
                     'quantique brute non hachée (parity ou ibm)',
            'rejets_niveau2_donnees_publiees': rejets_bruts,
            'rejets_niveau2_sans_belem': rejets_nettoyes,
            'repetitions_de_fenetres_typiques': rep_typ,
            'note': 'Sur les données IBM telles que publiées, le niveau 2 rejette ; la cause est '
                    'identifiée : la machine Belem reste bloquée à 0 ou à 1 pendant des essais entiers. '
                    'Une sortie bloquée est un défaut de mesure, pas une sortie pseudo-aléatoire ; le '
                    'verdict porte sur les huit autres machines (exclusion décidée après lecture des '
                    'données, analysée comme famille séparée).',
        },
        'volume': {
            'bits_total': int(sum(res[n]['n_bits'] for n in principaux)),
            'bits_bruts_non_haches': int(res['parity']['n_bits'] + res['ibm']['n_bits']),
            'bits_haches': int(res['anu']['n_bits'] + res['beacon']['n_bits']),
            'sequences_nist_total': int(sum(res[n]['n_sequences_nist'] for n in principaux)),
        },
        'donnees': donnees,
        'familles': {
            'principale_niveau1_nist': {'jeux': list(principaux), 'n_p': fam_p1['n_p'], 'rejets': fam_p1['rejets']},
            'principale_niveau2_cible': {'jeux': list(principaux), 'n_p': fam_p2['n_p'], 'rejets': fam_p2['rejets']},
            'secondaire_niveau1_nist': {'jeux': list(secondaires), 'n_p': f1[secondaires[0]]['n_p'],
                                        'rejets': f1[secondaires[0]]['rejets']},
            'secondaire_niveau2_cible': {'jeux': list(secondaires), 'n_p': f2[secondaires[0]]['n_p'],
                                         'rejets': f2[secondaires[0]]['rejets']},
        },
        'diagnostic_von_neumann': diag,
        'controles': ctrl,
        'methode': {
            'batterie': 'NIST SP 800-22 rév. 1a, 15 tests, paramètres de l\'annexe B (M = 128, m = 9, '
                        'M = 1032, L = 7, Q = 1280, m = 10, M = 500, m = 16), 188 p-valeurs par séquence',
            'longueur_sequence_nist': N_SEQ,
            'segment_bm': N_BM,
            'decimations': list(DECIMATIONS),
            'segments_bm_par_decimation': {str(k): v for k, v in SEGMENTS_BM.items()},
            'etat_max_detecte_bits': N_BM // 2,
            'lags_courts': LAGS_COURTS,
            'lag_max': LAG_MAX,
            'alpha_holm': ALPHA,
            'bits_par_controle': N_CONTROLE,
            'graine': GRAINE,
        },
        'autotests': {'etat': 'OK', **tests},
        'duree_totale_s': time.time() - t0,
    }


def resume(r: dict) -> str:
    lignes = [f"{r['volume']['bits_total']:,} bits ({r['volume']['bits_bruts_non_haches']:,} bruts)".replace(',', ' ')]
    for nom, d in r['donnees'].items():
        lignes.append(f"{nom:7s} {'haché' if d['hache'] else 'brut '} {d['n_bits']:>9} bits  1 : {d['fraction_de_1']:.4f}  "
                      f"N1 rejets {d['niveau1']['rejets']:>4} (p_holm {d['niveau1']['p_holm_min']:.2g})  "
                      f"N2 rejets {d['niveau2']['rejets']} (p_holm {d['niveau2']['p_holm_min']:.2g})")
    for nom, c in r['controles'].items():
        lignes.append(f"contrôle {nom:18s} détecté {c['detecte']} (N1 {c['detecte_niveau1']}, N2 {c['detecte_niveau2']}) "
                      f"L min {c['complexite_min_par_decimation']}")
    lignes.append(f"verdict : trace de pseudo-hasard = {'OUI' if r['verdict']['trace_de_pseudo_hasard'] else 'NON'}"
                  f"  ({r['duree_totale_s']:.0f} s)")
    return '\n'.join(lignes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ICI / 'resultats.json')
    args = parser.parse_args()
    resultat = calculer()
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2), encoding='utf-8')
    print(resume(resultat))
