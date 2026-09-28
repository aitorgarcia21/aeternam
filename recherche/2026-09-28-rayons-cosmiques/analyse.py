#!/usr/bin/env python3
"""aeternam, test n° 2 : les rayons cosmiques les plus énergétiques ont-ils la symétrie d'un cube ?

Prédiction testée (Beane, Davoudi et Savage, arXiv:1210.1847) : si l'Univers est
calculé sur une grille cubique, les directions d'arrivée des rayons cosmiques les
plus énergétiques portent la symétrie de cette grille. Sur un réseau cubique, la
première brisure de l'isotropie est proportionnelle à Q(n) = n_x^4 + n_y^4 + n_z^4
(le même Q que le test n° 1) : c'est l'harmonique cubique l = 4. La suivante est
l'harmonique cubique l = 6.

Données : catalogue des 100 rayons cosmiques les plus énergétiques (78 à 166 EeV,
1er janvier 2004 - 31 décembre 2020) de l'observatoire Pierre Auger, ApJS 264, 50
(2023), arXiv:2211.16020, diffusé dans Auger Open Data release 3,
DOI 10.5281/zenodo.10488964 (licence CC BY-SA 4.0). Le fichier contient aussi les
9 événements hybrides d'étalonnage, écartés ici.

Méthode (fixée avant de regarder le résultat) :
  1. statistique T(R) = écart, en écarts-types, entre la moyenne observée de la
     fonction cubique f(R n) et celle qu'aurait un ciel isotrope vu avec
     l'exposition d'Auger (Sommers 2001, latitude -35,2°, zénith <= 80°) ;
  2. l'orientation R de la grille est inconnue : Z = max sur R de |T(R)|,
     sur 20 000 orientations tirées uniformément ;
  3. p-valeur : fraction de 20 000 ciels isotropes simulés (même exposition,
     même nombre d'événements, même maximisation) dont le Z dépasse celui des
     données. Le coût de l'orientation choisie a posteriori est donc inclus.
Test principal : l = 4. Tests secondaires : l = 6 et l = 4 + 6 combinés.
Enfin, limite supérieure à 95 % sur l'amplitude d'un motif cubique.

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
CATALOGUE = ICI / 'donnees' / 'auger_catalogSD.csv'
SHA256_CATALOGUE = 'dc94ee0da5a20dc6d3897b8dde23d28d4f283a4fd94d2264e4dbe5cc02911b6b'

# Événements hybrides d'étalonnage (auger_catalogHybrid.csv), hors des 100 du
# catalogue : les 10 identifiants hybrides moins PAO100815 (82 EeV, dans les 100).
ETALONNAGE = {'PAO060329', 'PAO071111', 'PAO080703a', 'PAO080703b', 'PAO090322',
              'PAO110527', 'PAO110627', 'PAO140131', 'PAO150912'}

LATITUDE_DEG = -35.2      # Observatoire Pierre Auger (Malargüe)
ZENITH_MAX_DEG = 80.0     # catalogue : gerbes verticales et inclinées jusqu'à 80°

N_ORIENTATIONS = 20_000
N_CIELS = 20_000
N_CIELS_SIGNAL = 1_000
AMPLITUDES = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5)
N_ORIENT_FIXES = 16
N_CIELS_FIXES = 400
AMPLITUDES_FIXES = (0.4, 0.6, 0.8, 1.0, 1.25, 1.5)
GRAINE = 20260928


# ---------------------------------------------------------------- données
def lire_catalogue() -> dict:
    brut = CATALOGUE.read_bytes()
    empreinte = hashlib.sha256(brut).hexdigest()
    if empreinte != SHA256_CATALOGUE:
        raise SystemExit(f'catalogue modifié : sha256 {empreinte}')
    lignes = list(csv.DictReader(brut.decode('utf-8').splitlines()))
    garde = [l for l in lignes if l['id'] not in ETALONNAGE]
    ra = np.radians([float(l['ra']) for l in garde])
    dec = np.radians([float(l['dec']) for l in garde])
    return {
        'ids': [l['id'] for l in garde],
        'energie_EeV': np.array([float(l['energy']) for l in garde]),
        'theta_deg': np.array([float(l['theta']) for l in garde]),
        'n': vecteurs(ra, dec),
        'n_lignes': len(lignes),
    }


def vecteurs(ra: np.ndarray, dec: np.ndarray) -> np.ndarray:
    c = np.cos(dec)
    return np.stack([c * np.cos(ra), c * np.sin(ra), np.sin(dec)], axis=-1)


# ---------------------------------------------------------------- exposition
def exposition(dec: np.ndarray) -> np.ndarray:
    """Exposition relative en fonction de la déclinaison (Sommers 2001), maximum 1."""
    with np.errstate(divide='ignore', invalid='ignore'):
        return _exposition(dec)


def _exposition(dec: np.ndarray) -> np.ndarray:
    a0 = math.radians(LATITUDE_DEG)
    tm = math.radians(ZENITH_MAX_DEG)
    xi = (math.cos(tm) - math.sin(a0) * np.sin(dec)) / (math.cos(a0) * np.cos(dec))
    am = np.arccos(np.clip(xi, -1.0, 1.0))
    w = math.cos(a0) * np.cos(dec) * np.sin(am) + am * math.sin(a0) * np.sin(dec)
    grille = np.linspace(-math.pi / 2, math.pi / 2, 20001)
    xg = (math.cos(tm) - math.sin(a0) * np.sin(grille)) / (math.cos(a0) * np.cos(grille) + 1e-300)
    amg = np.arccos(np.clip(xg, -1.0, 1.0))
    wmax = np.max(math.cos(a0) * np.cos(grille) * np.sin(amg) + amg * math.sin(a0) * np.sin(grille))
    return np.clip(w, 0.0, None) / wmax


def tirer_ciel(rng: np.random.Generator, n: int, poids=None) -> np.ndarray:
    """n directions isotropes vues par Auger ; poids(n) <= 1 optionnel (signal injecté)."""
    sortie = []
    reste = n
    while reste > 0:
        m = 4 * reste + 64
        sind = rng.uniform(-1.0, 1.0, m)
        ra = rng.uniform(0.0, 2 * math.pi, m)
        dec = np.arcsin(sind)
        acc = exposition(dec)
        v = vecteurs(ra, dec)
        if poids is not None:
            acc = acc * poids(v)
        v = v[rng.uniform(0.0, 1.0, m) < acc]
        sortie.append(v[:reste])
        reste -= len(sortie[-1])
    return np.concatenate(sortie)


def quadrature(n_dec: int = 400, n_ra: int = 64):
    """Points et poids pour <g>_expo = intégrale(g w dOmega) / intégrale(w dOmega)."""
    x, wx = np.polynomial.legendre.leggauss(n_dec)          # x = sin(dec)
    ra = (np.arange(n_ra) + 0.5) * 2 * math.pi / n_ra
    dec = np.arcsin(x)
    D, A = np.meshgrid(dec, ra, indexing='ij')
    poids = (wx * exposition(dec))[:, None] * np.ones_like(A)
    poids = poids / poids.sum()
    return vecteurs(A.ravel(), D.ravel()), poids.ravel()


def quadrature_uniforme(n_dec: int = 60, n_ra: int = 64):
    x, wx = np.polynomial.legendre.leggauss(n_dec)
    ra = (np.arange(n_ra) + 0.5) * 2 * math.pi / n_ra
    D, A = np.meshgrid(np.arcsin(x), ra, indexing='ij')
    p = (wx[:, None] * np.ones_like(A)).ravel()
    return vecteurs(A.ravel(), D.ravel()), p / p.sum()


# ---------------------------------------------------------------- polynômes
def multi_indices(d: int) -> list[tuple[int, int, int]]:
    return [(a, b, d - a - b) for a in range(d, -1, -1) for b in range(d - a, -1, -1)]


def multinomial(al: tuple[int, int, int]) -> int:
    return math.factorial(sum(al)) // math.prod(math.factorial(k) for k in al)


def monomes(n: np.ndarray, indices) -> np.ndarray:
    """Matrice (événements x monômes) de n^alpha."""
    return np.stack([n[:, 0] ** a * n[:, 1] ** b * n[:, 2] ** c for a, b, c in indices], axis=1)


def coefficients_puissance(E: np.ndarray, d: int, indices_cible) -> np.ndarray:
    """Coefficients, dans les monômes de degré D = indices_cible, de
    somme_k (e_k . n)^d (n . n)^((D - d) / 2), pour chaque orientation.
    E : (orientations, 3, 3), lignes e_k = axes de la grille."""
    D = sum(indices_cible[0])
    k = (D - d) // 2
    col = {al: i for i, al in enumerate(indices_cible)}
    out = np.zeros((E.shape[0], len(indices_cible)))
    for al in multi_indices(d):
        c = multinomial(al) * np.sum(E[:, :, 0] ** al[0] * E[:, :, 1] ** al[1] * E[:, :, 2] ** al[2], axis=1)
        for be in multi_indices(k):                        # (x^2+y^2+z^2)^k
            cb = multinomial(be)
            tgt = (al[0] + 2 * be[0], al[1] + 2 * be[1], al[2] + 2 * be[2])
            out[:, col[tgt]] += c * cb
    return out


def rotations(rng: np.random.Generator, n: int) -> np.ndarray:
    q = rng.normal(size=(n, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    w, x, y, z = q.T
    return np.stack([
        np.stack([1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)], -1),
        np.stack([2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)], -1),
        np.stack([2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)], -1),
    ], axis=1)


def coefficient_l6() -> float:
    """alpha tel que f6 = somme n^6 + alpha somme n^4 (+ constante) soit l = 6 pur."""
    v, p = quadrature_uniforme()
    i4 = np.sum(v ** 4, axis=1)
    i6 = np.sum(v ** 6, axis=1)
    m = lambda g: float(np.sum(p * g))
    c4 = i4 - m(i4)
    return -(m(i6 * c4)) / m(c4 * c4)


class Statistique:
    """T(R) = c(R).(P - N mu) / sqrt(N c(R)^T S c(R)) pour une fonction cubique."""

    def __init__(self, E: np.ndarray, degre: int, alpha: float = 0.0):
        self.idx = multi_indices(degre)
        self.C = coefficients_puissance(E, degre, self.idx)
        if alpha:
            self.C += alpha * coefficients_puissance(E, degre - 2, self.idx)
        v, w = quadrature()
        M = monomes(v, self.idx)
        self.mu = w @ M
        self.S = (M * w[:, None]).T @ M - np.outer(self.mu, self.mu)
        self.sd1 = np.sqrt(np.einsum('ri,ij,rj->r', self.C, self.S, self.C))

    def T(self, n: np.ndarray) -> np.ndarray:
        P = monomes(n, self.idx).sum(axis=0) - len(n) * self.mu
        return (self.C @ P) / (math.sqrt(len(n)) * self.sd1)

    def T_lots(self, P: np.ndarray, N: int) -> np.ndarray:
        """P : (ciels, monômes) déjà centrés ; renvoie (orientations, ciels)."""
        return (self.C @ P.T) / (math.sqrt(N) * self.sd1[:, None])

    def P_centre(self, ciels: np.ndarray) -> np.ndarray:
        m = monomes(ciels.reshape(-1, 3), self.idx).reshape(ciels.shape[0], ciels.shape[1], -1)
        return m.sum(axis=1) - ciels.shape[1] * self.mu


# ---------------------------------------------------------------- calcul
def Q(v: np.ndarray) -> np.ndarray:
    return np.sum(v ** 4, axis=-1)


def maxima(stats, P_list, N):
    """Z4, Z6, Z46 pour un lot de ciels."""
    T4 = stats[0].T_lots(P_list[0], N)
    T6 = stats[1].T_lots(P_list[1], N)
    return (np.max(np.abs(T4), axis=0), np.max(np.abs(T6), axis=0),
            np.max(T4 ** 2 + T6 ** 2, axis=0))


def simuler(rng, stats, N, n_ciels, poids_fn=None, lot=250):
    z = [[], [], []]
    for debut in range(0, n_ciels, lot):
        k = min(lot, n_ciels - debut)
        if poids_fn is None:
            ciels = tirer_ciel(rng, N * k).reshape(k, N, 3)
        else:
            ciels = np.stack([tirer_ciel(rng, N, poids_fn(rng)) for _ in range(k)])
        P = [s.P_centre(ciels) for s in stats]
        for i, a in enumerate(maxima(stats, P, N)):
            z[i].append(a)
    return [np.concatenate(a) for a in z]


def p_valeur(nuls: np.ndarray, obs: float) -> float:
    return float((1 + np.sum(nuls >= obs)) / (1 + len(nuls)))


def angle_modulo_cube(R1: np.ndarray, R2: np.ndarray) -> float:
    """Plus petit angle (degrés) entre deux orientations de grille, au groupe du cube près."""
    meilleur = 180.0
    for perm in itertools.permutations(range(3)):
        for signes in itertools.product((1, -1), repeat=3):
            G = np.zeros((3, 3))
            for i, j in enumerate(perm):
                G[i, j] = signes[i]
            M = (G @ R1) @ R2.T
            c = (np.trace(M) - 1) / 2
            meilleur = min(meilleur, math.degrees(math.acos(max(-1.0, min(1.0, c)))))
    return meilleur


def poids_signal(eps: float, R0: np.ndarray):
    """Densité relative 1 + eps (5 Q(R0 n) - 3) / 2, ramenée à un maximum de 1.
    eps > 0 : excès vers les 6 axes du cube ; eps < 0 : vers les 8 diagonales."""
    haut = 1 + max(eps, -2 * eps / 3)
    return lambda v: (1 + eps * (5 * Q(v @ R0.T) - 3) / 2) / haut


def autotests(rng, stats, E) -> dict:
    s4, s6 = stats
    # 1. f est invariante sous le groupe du cube (permutations et signes des axes).
    v = rng.normal(size=(50, 3))
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    for perm in itertools.permutations(range(3)):
        assert np.allclose(Q(v[:, perm] * np.array([1, -1, 1])), Q(v))
    # 2. Le développement en monômes reproduit l'évaluation directe.
    R = E[:3]
    M4 = monomes(v, s4.idx)
    for r in range(3):
        direct = Q(v @ R[r].T)
        assert np.allclose(M4 @ s4.C[r], direct, atol=1e-12)
    alpha = coefficient_l6()
    M6 = monomes(v, s6.idx)
    direct6 = np.sum((v @ R[0].T) ** 6, axis=1) + alpha * Q(v @ R[0].T)
    assert np.allclose(M6 @ s6.C[0], direct6, atol=1e-12)
    # 3. Exposition : nulle au-delà de dec = latitude + zénith max, pleine au pôle sud.
    assert exposition(np.radians(np.array([45.0])))[0] == 0.0
    assert abs(exposition(np.radians(np.array([-90.0])))[0] - 1.0) < 1e-3
    # 4. La quadrature et un grand tirage donnent la même moyenne de Q.
    grand = tirer_ciel(rng, 400_000)
    mu_q = float(np.sum(quadrature()[1] * Q(quadrature()[0])))
    assert abs(float(np.mean(Q(grand))) - mu_q) < 5 * float(np.std(Q(grand))) / math.sqrt(4e5)
    # 5. Sous isotropie, T(R) à orientation fixée est centré réduit.
    ciels = tirer_ciel(rng, 100 * 2000).reshape(2000, 100, 3)
    t = s4.T_lots(s4.P_centre(ciels), 100)[:5]
    assert np.all(np.abs(t.mean(axis=1)) < 0.12) and np.all(np.abs(t.std(axis=1) - 1) < 0.08)
    # 6. l = 6 pur : orthogonal à l = 4 sur la sphère uniforme.
    vu, pu = quadrature_uniforme()
    f6 = np.sum(vu ** 6, axis=1) + alpha * Q(vu)
    c4 = Q(vu) - np.sum(pu * Q(vu))
    assert abs(np.sum(pu * (f6 - np.sum(pu * f6)) * c4)) < 1e-12
    # 7. Un motif cubique franc est détecté et son orientation retrouvée.
    R0 = rotations(rng, 1)[0]
    ciel = tirer_ciel(rng, 2000, poids_signal(1.0, R0))
    T4 = s4.T(ciel)
    ecart = angle_modulo_cube(E[int(np.argmax(np.abs(T4)))], R0)
    assert np.max(np.abs(T4)) > 8 and ecart < 10, (np.max(np.abs(T4)), ecart)
    return {'alpha_l6': alpha, 'orientation_retrouvee_ecart_deg': ecart, 'mu_Q_expo': mu_q}


def calculer() -> dict:
    rng = np.random.default_rng(GRAINE)
    cat = lire_catalogue()
    n = cat['n']
    N = len(n)
    assert cat['n_lignes'] == 109 and N == 100
    assert cat['energie_EeV'].min() >= 78 and cat['theta_deg'].max() <= ZENITH_MAX_DEG

    E = rotations(rng, N_ORIENTATIONS)
    alpha = coefficient_l6()
    stats = (Statistique(E, 4), Statistique(E, 6, alpha))
    tests = autotests(rng, stats, E)

    T4 = stats[0].T(n)
    T6 = stats[1].T(n)
    obs = (float(np.max(np.abs(T4))), float(np.max(np.abs(T6))), float(np.max(T4 ** 2 + T6 ** 2)))
    ib = int(np.argmax(np.abs(T4)))
    Rb = E[ib]

    nuls = simuler(rng, stats, N, N_CIELS)
    p = [p_valeur(nuls[i], obs[i]) for i in range(3)]

    # Écart observé à la meilleure orientation, en fraction de l'isotropie.
    q_obs = float(np.mean(Q(n @ Rb.T)))
    v, w = quadrature()
    q_iso = float(np.sum(w * Q(v @ Rb.T)))

    # Limite supérieure : amplitude eps pour laquelle 95 % des ciels simulés
    # (grille d'orientation aléatoire) donnent un Z4 plus grand que celui observé.
    courbe = []
    for signe in (1, -1):
        for a in AMPLITUDES[1:]:
            eps = signe * a
            if eps < -1:
                continue
            fn = lambda r, e=eps: poids_signal(e, rotations(r, 1)[0])
            z4 = simuler(rng, stats, N, N_CIELS_SIGNAL, fn, lot=100)[0]
            courbe.append({'epsilon': eps, 'fraction_Z4_superieur_obs': float(np.mean(z4 > obs[0])),
                           'Z4_median': float(np.median(z4))})

    def limite(signe):
        pts = sorted((abs(c['epsilon']), c['fraction_Z4_superieur_obs']) for c in courbe
                     if math.copysign(1, c['epsilon']) == signe)
        for (a0, f0), (a1, f1) in zip(pts, pts[1:]):
            if f0 < 0.95 <= f1:
                return a0 + (0.95 - f0) * (a1 - a0) / (f1 - f0)
        return None

    # Limite garantie pour chaque orientation, pas seulement en moyenne : même calcul
    # à orientation fixée, pour l'orientation la moins visible par Auger (écart-type
    # minimal de Q sous l'exposition) et pour des orientations tirées au hasard.
    fixes = [int(np.argmin(stats[0].sd1))] + list(rng.choice(len(E), N_ORIENT_FIXES - 1, replace=False))
    par_orientation = []
    for k in fixes:
        lim = {}
        for signe, grille in ((1, AMPLITUDES_FIXES), (-1, tuple(a for a in AMPLITUDES_FIXES if a <= 1))):
            pts = [(0.0, 0.0)]
            for a in grille:
                fn = lambda r, e=signe * a, R0=E[k]: poids_signal(e, R0)
                z4 = simuler(rng, stats, N, N_CIELS_FIXES, fn, lot=100)[0]
                pts.append((a, float(np.mean(z4 > obs[0]))))
            lim[signe] = next((a0 + (0.95 - f0) * (a1 - a0) / (f1 - f0)
                               for (a0, f0), (a1, f1) in zip(pts, pts[1:]) if f0 < 0.95 <= f1), None)
        par_orientation.append({'indice': int(k), 'ecart_type_Q_expo': float(stats[0].sd1[k]),
                                'epsilon_axes_max': lim[1], 'epsilon_diagonales_max': lim[-1]})

    def pire(cle, borne):
        vals = [p[cle] for p in par_orientation]
        return None if any(v is None for v in vals) else max(vals), sum(v is None for v in vals)

    seuils = {q: float(np.quantile(nuls[0], q)) for q in (0.5, 0.95, 0.99, 0.999)}
    return {
        'titre': 'Test n° 2 : symétrie cubique des rayons cosmiques les plus énergétiques (Auger)',
        'date': '2026-09-28',
        'prediction': 'Beane, Davoudi, Savage, arXiv:1210.1847 : brisure de la symétrie de rotation '
                      'reflétant la grille, dans les directions des rayons cosmiques les plus énergétiques',
        'donnees': {
            'source': 'Pierre Auger Collaboration, ApJS 264, 50 (2023), arXiv:2211.16020 ; '
                      'Auger Open Data release 3, DOI 10.5281/zenodo.10488964, CC BY-SA 4.0',
            'fichier': 'donnees/auger_catalogSD.csv',
            'sha256': SHA256_CATALOGUE,
            'n_evenements': N,
            'energie_min_EeV': float(cat['energie_EeV'].min()),
            'energie_max_EeV': float(cat['energie_EeV'].max()),
            'periode': '2004-01-01 / 2020-12-31',
            'ecartes_etalonnage': sorted(ETALONNAGE),
        },
        'methode': {
            'exposition': f'Sommers 2001, latitude {LATITUDE_DEG}°, zénith <= {ZENITH_MAX_DEG}°',
            'latitude_deg': LATITUDE_DEG,
            'zenith_max_deg': ZENITH_MAX_DEG,
            'declinaison_max_visible_deg': LATITUDE_DEG + ZENITH_MAX_DEG,
            'fraction_du_ciel_visible': (1 + math.sin(math.radians(LATITUDE_DEG + ZENITH_MAX_DEG))) / 2,
            'angle_axe_diagonale_deg': math.degrees(math.acos(1 / math.sqrt(3))),
            'fonction_l4': 'Q(Rn) = somme (R n)_k^4',
            'fonction_l6': f'somme (R n)_k^6 + {alpha:.6f} somme (R n)_k^4',
            'fonction_l6_alpha': alpha,
            'orientations': N_ORIENTATIONS,
            'ciels_isotropes': N_CIELS,
            'ciels_par_amplitude': N_CIELS_SIGNAL,
            'graine': GRAINE,
            'test_principal': 'l = 4, Z4 = max_R |T4(R)|',
        },
        'resultats': {
            'Z4_observe': obs[0], 'p_valeur_l4': p[0],
            'Z6_observe': obs[1], 'p_valeur_l6': p[1],
            'Z46_observe': obs[2], 'p_valeur_l4_l6': p[2],
            'seuils_Z4_isotrope': seuils,
            'meilleure_orientation_T4': float(T4[ib]),
            'meilleure_orientation_matrice': Rb.round(6).tolist(),
            'Q_moyen_observe': q_obs,
            'Q_moyen_attendu_isotrope': q_iso,
            'ecart_relatif_Q': (q_obs - q_iso) / q_iso,
        },
        'limite_superieure_95': {
            'definition': 'densité relative 1 + eps (5 Q - 3) / 2 ; eps = excès relatif le long des axes '
                          'de la grille (eps < 0 : le long des diagonales)',
            'epsilon_axes_max': limite(1),
            'epsilon_diagonales_max': limite(-1),
            'exces_axes_max': limite(1),
            'exces_diagonales_max': None if limite(-1) is None else 2 / 3 * limite(-1),
            'convention': 'orientation de la grille tirée au hasard pour chaque ciel simulé : '
                          'limite moyenne sur les orientations',
            'par_orientation_fixe': par_orientation,
            'pire_orientation_epsilon_axes_max': pire('epsilon_axes_max', 1.5)[0],
            'pire_orientation_epsilon_diagonales_max': pire('epsilon_diagonales_max', 1.0)[0],
            'orientations_sans_limite_axes': pire('epsilon_axes_max', 1.5)[1],
            'orientations_sans_limite_diagonales': pire('epsilon_diagonales_max', 1.0)[1],
            'n_orientations_fixes': len(par_orientation),
            'courbe': courbe,
        },
        'autotests': {'etat': 'OK', **tests},
    }


def resume(r: dict) -> str:
    x = r['resultats']
    l = r['limite_superieure_95']
    return (f"{r['donnees']['n_evenements']} événements de {r['donnees']['energie_min_EeV']:.0f} à "
            f"{r['donnees']['energie_max_EeV']:.0f} EeV\n"
            f"l=4 : Z = {x['Z4_observe']:.2f}, p = {x['p_valeur_l4']:.3f}\n"
            f"l=6 : Z = {x['Z6_observe']:.2f}, p = {x['p_valeur_l6']:.3f}\n"
            f"l=4+6 : Z² = {x['Z46_observe']:.2f}, p = {x['p_valeur_l4_l6']:.3f}\n"
            f"limite 95 % : eps(axes) < {l['epsilon_axes_max']}, eps(diagonales) > -{l['epsilon_diagonales_max']}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ICI / 'resultats.json')
    args = parser.parse_args()
    resultat = calculer()
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2), encoding='utf-8')
    print(resume(resultat))
