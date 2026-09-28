#!/usr/bin/env python3
"""aeternam, test n° 3 : la lumière va-t-elle moins vite dans certaines directions ?

Hypothèse testée : l'espace est une grille cubique de maille a sur laquelle la
lumière obéit à Maxwell discrétisé (schéma de Yee). Un photon d'énergie E va
alors à la vitesse v/c ≃ 1 − (1/8)(Q − σ²/3)(aE/ħc)², avec Q(n) = Σ n_i⁴ dans
les axes de la grille et σ le nombre de Courant (test n° 1). Au pas de temps
maximal (σ = 1), les grandes diagonales (Q = 1/3) ne dispersent plus : une
source unique placée sur une diagonale ne borne rien (angle mort du test n° 1).

Ce test combine huit sources vues dans des directions différentes du ciel
(sursauts gamma, blazars, pulsar du Crabe), chacune avec une limite publiée à
95 % sur l'échelle quadratique E_QG,2 (sous-luminale), tirée d'articles de
temps de vol. Analyse secondaire : aucun photon n'est réanalysé.

Méthode (fixée avant le calcul) :
  1. chaque limite publiée est réécrite dans la convention de Jacob et Piran
     (facteur 3/2, distance K2 = ∫(1+z)²/H dz), puis ramenée à une même
     cosmologie (celle de LHAASO : H0 = 67,36, Ωm = 0,315) par
     E_commune = E_publiée × racine(K2_commune / K2_publiée) ;
  2. dans le modèle de grille, E_QG,2 = racine(12) ħc / (a racine(Q_eff)) :
     chaque source borne a·racine(Q_eff(R n_i)) ≤ B_i = racine(12) ħc / E_i ;
  3. pour une orientation R de la grille, a ≤ A(R) = min_i B_i / racine(Q_eff,i) ;
  4. pire orientation : max de A(R) sur 100 000 rotations tirées uniformément
     (quaternions gaussiens normalisés, graine fixe), plus des orientations
     construites (une source sur une diagonale, rotation autour de celle-ci),
     puis raffinement local ; 95 % des orientations : quantile 95 % de A(R).
Aucune vraisemblance n'est combinée (elles ne sont pas publiées) : la borne
retenue pour une orientation est la plus contraignante des limites individuelles.

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
DONNEES = ICI / 'donnees'

# Constantes SI exactes (CODATA 2022), comme au test n° 1.
C = 299_792_458.0
H = 6.62607015e-34
EV_J = 1.602176634e-19
HBAR_C_GEV_M = H / (2 * math.pi) * C / (EV_J * 1e9)
MPC_M = (648_000.0 / math.pi) * 149_597_870_700.0 * 1e6
KPC_M = MPC_M / 1000.0
LPL_M = 1.616255e-35                 # longueur de Planck, CODATA 2022
EPL_GEV = 1.22e19                     # énergie de Planck arrondie, convention LHAASO et MAGIC

# Cosmologie commune : celle de LHAASO (arXiv:2402.06009v3, p. 2), plate.
COSMO_COMMUNE = {'H0': 67.36, 'Om': 0.315, 'OL': 1 - 0.315}

BEANE_INV_B_GEV = 1e11                # arXiv:1210.1847v2, résumé et p. 11
TEST1_PIRE_SIGMA0_M = 2.4931583193889674e-27   # test n° 1, CCF, sigma = 0

SIGMAS = (0.0, 0.5, 0.9, 1.0)
N_ORIENTATIONS = 100_000
N_ORIENTATIONS_VARIANTES = 20_000
N_ANGLES_CONSTRUITS = 720
N_RAFFINES = 48
N_PAS_RAFFINEMENT = 1_500
GRAINE = 20260928
QE_NUL = 1e-12                        # Q_eff plus petit : compté comme diagonale exacte (aucune borne)

# ------------------------------------------------------------------ sources
# Chaque entrée : limite à 95 % sous-luminale sur E_QG,2 telle que publiée
# (méthode la moins contraignante quand l'article en donne plusieurs), la
# cosmologie et le décalage vers le rouge employés par l'article. Détail et
# citations : sources.md. Coordonnées : fichiers SIMBAD de donnees/.
SOURCES = [
    {'id': 'GRB221009A', 'nom': 'GRB 221009A', 'type': 'sursaut gamma',
     'instrument': 'LHAASO', 'arxiv': '2402.06009v3',
     'simbad': 'simbad_GRB_221009A.txt',
     'z': 0.151, 'cosmo': dict(COSMO_COMMUNE),
     # Tableau I : CCF, eta2 < 0,66 avec eta2 = 1e-15 E_Pl^2 / E_QG,2^2.
     'eta2_haut': 0.66, 'eta2_prefacteur': 1e-15,
     'EQG2_publie_GeV': None, 'EQG2_imprime_GeV': 4.7e11,
     'methode': 'CCF (la moins contraignante des trois ; ML : 6,9e11 GeV)'},
    {'id': 'GRB190114C', 'nom': 'GRB 190114C', 'type': 'sursaut gamma',
     'instrument': 'MAGIC', 'arxiv': '2001.09728v4',
     'simbad': 'simbad_GRB_190114C.txt',
     'z': 0.4245, 'cosmo': {'H0': 70.0, 'Om': 0.3, 'OL': 0.7},
     'eta2_haut': 3.7, 'eta2_prefacteur': 1e-16,
     'EQG2_publie_GeV': 6.3e10, 'EQG2_imprime_GeV': 6.3e10,
     'methode': 'courbe de lumière théorique (minimale : 7,3e10 GeV)'},
    {'id': 'GRB090510', 'nom': 'GRB 090510', 'type': 'sursaut gamma',
     'instrument': 'Fermi-LAT', 'arxiv': '1305.3463v1',
     'simbad': 'simbad_GRB_090510.txt',
     'z': 0.903, 'cosmo': {'H0': 73.8, 'Om': 0.272, 'OL': 0.728},
     'kappa2_imprime': 1.50,
     'EQG2_publie_GeV': 6.7e10, 'EQG2_imprime_GeV': 6.7e10,
     'methode': 'PairView, tableau IV (SMM : 13e10 ; vraisemblance : 8,6e10 GeV)'},
    {'id': 'Mrk501', 'nom': 'Mrk 501', 'type': 'blazar',
     'instrument': 'H.E.S.S.', 'arxiv': '1901.05209v1',
     'simbad': 'simbad_Mrk_501.txt',
     'z': 0.034, 'cosmo': {'H0': 67.74, 'Om': 0.31, 'OL': 0.69},
     'tau2': (-0.6, 1.8, 0.7),          # s/TeV^2 : meilleur, stat, syst
     'EQG2_publie_GeV': 8.5e10, 'EQG2_imprime_GeV': 8.5e10,
     'methode': 'temps de vol, vraisemblance (la limite spectrale EBL est une autre physique)'},
    {'id': 'Mrk421', 'nom': 'Mrk 421', 'type': 'blazar',
     'instrument': 'MAGIC', 'arxiv': '2406.07140v1',
     'simbad': 'simbad_Mrk_421.txt',
     'z': 0.03, 'cosmo': {'H0': 70.0, 'Om': 0.31, 'OL': 0.69},
     'kappa2_imprime_s': 1.35e16, 'eta2_s_TeV2': 16.0,
     'EQG2_publie_GeV': 2.5e10, 'EQG2_imprime_GeV': 2.5e10,
     'methode': 'tableau 2 avec systématiques ; plus faible des deux signes '
                '(le résumé et le tableau intervertissent 2,5 et 2,6e10)'},
    {'id': 'PKS2155', 'nom': 'PKS 2155-304', 'type': 'blazar',
     'instrument': 'H.E.S.S.', 'arxiv': '1101.3650v2',
     'simbad': 'simbad_PKS_2155-304.txt',
     'z': 0.116, 'cosmo': {'H0_s': 2.3e-18, 'Om': 0.3, 'OL': 0.7},
     'zeta_haut': 3.6e16,
     'EQG2_publie_GeV': 6.4e10, 'EQG2_imprime_GeV': 6.4e10,
     'methode': 'vraisemblance événement par événement, 95 %'},
    {'id': 'PG1553', 'nom': 'PG 1553+113', 'type': 'blazar',
     'instrument': 'H.E.S.S.', 'arxiv': '1501.05087v1',
     'simbad': 'simbad_PG_1553_113.txt',
     'z': 0.49, 'cosmo': {'H0': 70.4, 'Om': 0.27, 'OL': 0.73},
     'kappa2_imprime': 0.677, 'tau2_haut_s_TeV2': 1012.4,
     'EQG2_publie_GeV': 2.10e10, 'EQG2_imprime_GeV': 2.10e10,
     'methode': 'tableau 5, étalonné + systématiques'},
    {'id': 'Crabe', 'nom': 'pulsar du Crabe', 'type': 'pulsar',
     'instrument': 'MAGIC', 'arxiv': '1709.00346v1',
     'simbad': 'simbad_PSR_B0531_21.txt',
     'distance_kpc': 2.0, 'cosmo': None,
     'EQG2_publie_GeV': 5.9e10, 'EQG2_imprime_GeV': 5.9e10,
     'methode': 'vraisemblance profilée, tableau 6, avec systématiques'},
]
# Fiches SIMBAD relevées le 28/09/2026 (sim-id, format ASCII).
SHA256_SIMBAD = {
    'simbad_GRB_221009A.txt': 'f5dcadb02d85080ca4e8fa9d6bae7f1e49a1f93e2a6e5d803343ba4eebd60575',
    'simbad_GRB_190114C.txt': '53abc5578873123f35844fd42e8eb487481ef64127def402556b25c40695a958',
    'simbad_GRB_090510.txt': 'c7f372564ec7d8416eadba466e699b5c86f5d0faa733cfcfcf7fc51eb907d966',
    'simbad_Mrk_501.txt': 'eb17f59b8b387fa77f06986e7b41c77beba694e4618739783a32b10fb5dd8569',
    'simbad_Mrk_421.txt': 'd3275edd1ba6092d7b391d0b8c55bf2acab353ecc91dcbb3578e45face3bdfac',
    'simbad_PKS_2155-304.txt': '51699f4a9c1bfd1f36847166df81bdbe74a71b75dc77a32c8c6f2f8ca0ed2889',
    'simbad_PG_1553_113.txt': 'd0366949e8324919954aa26d2a5c1df9b249dbd2fad09c1abdec36528ddece50',
    'simbad_PSR_B0531_21.txt': 'f14480d2b9c1c476aab143c0ccdc1034e1f605a1743bbf995532ef320c5b5f3e',
}
# Variante : Fermi tableau V (effets intrinsèques au sursaut pris en compte).
FERMI_TABLEAU_V_GEV = 4.0e10


# ------------------------------------------------------------ cosmologie
def h0_si(cosmo: dict) -> float:
    if 'H0_s' in cosmo:
        return cosmo['H0_s']
    return cosmo['H0'] * 1000.0 / MPC_M


def kappa(n: int, z: float, om: float, ol: float, pas: int = 4096) -> float:
    """κ_n = ∫_0^z (1+z')^n / racine(Ωm (1+z')³ + ΩΛ) dz' (Simpson)."""
    x = np.linspace(0.0, z, pas + 1)
    f = (1 + x) ** n / np.sqrt(om * (1 + x) ** 3 + ol)
    poids = np.ones(pas + 1)
    poids[1:-1:2], poids[2:-1:2] = 4, 2
    return float(np.dot(poids, f) * (z / pas) / 3)


def distance_k2(source: dict, cosmo: dict | None) -> float:
    """K2 en secondes : ∫(1+z)²/H dz pour une source cosmologique, d/c pour le Crabe."""
    if source.get('distance_kpc') is not None:
        return source['distance_kpc'] * KPC_M / C
    return kappa(2, source['z'], cosmo['Om'], cosmo['OL']) / h0_si(cosmo)


def eqg2_publie(source: dict) -> float:
    if source.get('eta2_haut') is not None and source['EQG2_publie_GeV'] is None:
        return EPL_GEV * math.sqrt(source['eta2_prefacteur'] / source['eta2_haut'])
    return source['EQG2_publie_GeV']


def eqg2_commune(source: dict, e_pub: float | None = None) -> float:
    """Limite ramenée à la cosmologie commune (même contrainte sur Δt/ΔE²)."""
    e = eqg2_publie(source) if e_pub is None else e_pub
    if source['cosmo'] is None:
        return e
    rapport = distance_k2(source, COSMO_COMMUNE) / distance_k2(source, source['cosmo'])
    return e * math.sqrt(rapport)


def borne_a_racine_qe(eqg2_gev: float) -> float:
    """B = racine(12) ħc / E_QG,2 : borne sur a·racine(Q_eff) en mètres."""
    return math.sqrt(12.0) * HBAR_C_GEV_M / eqg2_gev


# ------------------------------------------------------------- directions
def lire_simbad(fichier: str) -> tuple[float, float, str, str]:
    brut = (DONNEES / fichier).read_bytes()
    texte = brut.decode('utf-8')
    for ligne in texte.splitlines():
        if ligne.startswith('Coordinates(ICRS,ep=J2000,eq=2000):'):
            morceaux = ligne.split(':', 1)[1].split()
            h, m, s, d, dm, ds = morceaux[:6]
            ra = 15.0 * (float(h) + float(m) / 60 + float(s) / 3600)
            signe = -1.0 if d.startswith('-') else 1.0
            dec = signe * (abs(float(d)) + float(dm) / 60 + float(ds) / 3600)
            return ra, dec, ligne.split(':', 1)[1].strip(), hashlib.sha256(brut).hexdigest()
    raise SystemExit(f'coordonnées absentes de {fichier}')


def vecteur(ra_deg: float, dec_deg: float) -> np.ndarray:
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return np.array([math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d)])


# ------------------------------------------------------------ orientations
def quaternions_uniformes(n: int, rng: np.random.Generator) -> np.ndarray:
    q = rng.standard_normal((n, 4))
    return q / np.linalg.norm(q, axis=1, keepdims=True)


def matrices(q: np.ndarray) -> np.ndarray:
    w, x, y, z = q[:, 0], q[:, 1], q[:, 2], q[:, 3]
    return np.stack([
        np.stack([1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)], -1),
        np.stack([2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)], -1),
        np.stack([2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)], -1),
    ], -2)


def q_facteurs(rot: np.ndarray, dirs: np.ndarray) -> np.ndarray:
    """Q(R n_i) pour chaque orientation (lignes) et chaque source (colonnes)."""
    m = np.einsum('rij,sj->rsi', rot, dirs)
    return np.sum(m ** 4, axis=-1)


def borne_orientation(q: np.ndarray, b: np.ndarray, sigma: float) -> np.ndarray:
    """A(R) = min_i B_i / racine(Q_eff,i) ; une source à Q_eff = 0 ne borne rien."""
    qe = q - sigma ** 2 / 3
    par_source = np.where(qe > QE_NUL, b / np.sqrt(np.clip(qe, QE_NUL, None)), np.inf)
    return par_source.min(axis=1)


def rotation_vers(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Quaternion (w, x, y, z) de la rotation minimale qui envoie u sur v (unitaires)."""
    axe = np.cross(u, v)
    c = float(np.dot(u, v))
    q = np.array([1 + c, *axe])
    if np.linalg.norm(q) < 1e-12:                   # u = -v
        perp = np.cross(u, [1.0, 0.0, 0.0])
        if np.linalg.norm(perp) < 1e-6:
            perp = np.cross(u, [0.0, 1.0, 0.0])
        q = np.array([0.0, *perp])
    return q / np.linalg.norm(q)


def produit(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    w1, x1, y1, z1 = np.moveaxis(q1, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(q2, -1, 0)
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], -1)


def orientations_construites(dirs: np.ndarray, n_angles: int) -> np.ndarray:
    """Pour chaque source : la placer sur la diagonale (1,1,1)/racine 3, puis tourner autour.

    Ce sont les candidates naturelles au pire cas quand σ = 1."""
    diag = np.ones(3) / math.sqrt(3)
    angles = np.linspace(0, 2 * math.pi, n_angles, endpoint=False)
    tours = np.stack([np.cos(angles / 2), *(np.sin(angles / 2)[None, :] * diag[:, None])], -1)
    blocs = []
    for n in dirs:
        q0 = rotation_vers(n, diag)
        blocs.append(produit(tours, np.broadcast_to(q0, tours.shape)))
    return np.concatenate(blocs)


def raffiner(q0: np.ndarray, dirs: np.ndarray, b: np.ndarray, sigma: float,
             rng: np.random.Generator, pas: int = N_PAS_RAFFINEMENT) -> tuple[np.ndarray, np.ndarray]:
    """Montée aléatoire (acceptation si A augmente), pas décroissant de 0,1 à 1e-7 rad."""
    q = q0.copy()
    val = borne_orientation(q_facteurs(matrices(q), dirs), b, sigma)
    for echelle in np.geomspace(0.1, 1e-7, pas):
        essai = q + echelle * rng.standard_normal(q.shape)
        essai /= np.linalg.norm(essai, axis=1, keepdims=True)
        v = borne_orientation(q_facteurs(matrices(essai), dirs), b, sigma)
        mieux = v > val
        q[mieux], val[mieux] = essai[mieux], v[mieux]
    return q, val


def pire_orientation(dirs: np.ndarray, b: np.ndarray, sigma: float, q_tirees: np.ndarray,
                     rng: np.random.Generator) -> dict:
    tirees = borne_orientation(q_facteurs(matrices(q_tirees), dirs), b, sigma)
    construites_q = orientations_construites(dirs, N_ANGLES_CONSTRUITS)
    construites = borne_orientation(q_facteurs(matrices(construites_q), dirs), b, sigma)
    tous_q = np.concatenate([q_tirees, construites_q])
    toutes = np.concatenate([tirees, construites])
    finies = np.isfinite(toutes)
    if not finies.all():
        return {'borne_m': math.inf, 'fini': False, 'quantile95_m': float(np.quantile(tirees, 0.95)),
                'mediane_m': float(np.median(tirees)), 'max_tirage_m': math.inf}
    depart = tous_q[np.argsort(toutes)[-N_RAFFINES:]]
    q_fin, v_fin = raffiner(depart, dirs, b, sigma, rng)
    k = int(np.argmax(v_fin))
    rot = matrices(q_fin[k:k + 1])
    q_src = q_facteurs(rot, dirs)[0]
    diagonales = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1]]) / math.sqrt(3)
    cos_diag = np.abs(np.einsum('ij,sj->si', rot[0], dirs) @ diagonales.T).max(axis=1)
    angle_diag = np.degrees(np.arccos(np.clip(cos_diag, -1, 1)))
    qe = q_src - sigma ** 2 / 3
    par_source = np.where(qe > QE_NUL, b / np.sqrt(np.clip(qe, QE_NUL, None)), np.inf)
    return {
        'borne_m': float(v_fin[k]),
        'fini': True,
        'max_tirage_m': float(tirees.max()),
        'max_construites_m': float(construites.max()),
        'quantile95_m': float(np.quantile(tirees, 0.95)),
        'mediane_m': float(np.median(tirees)),
        'quaternion': [float(x) for x in q_fin[k]],
        'Q_eff_par_source': [float(x) for x in qe],
        'borne_par_source_m': [float(x) for x in par_source],
        'sources_actives': [int(i) for i in np.flatnonzero(par_source <= v_fin[k] * (1 + 1e-3))],
        'angle_a_la_diagonale_la_plus_proche_deg': [float(x) for x in angle_diag],
    }


# ------------------------------------------------------------ autotests
def vitesse_groupe(n: np.ndarray, ak: float, sigma: float) -> float:
    """v/c radiale exacte sur le réseau de Yee (repris du test n° 1)."""
    k = ak * n
    s2 = float(np.sum(np.sin(k / 2) ** 2))
    if sigma == 0:
        w = 2 * math.sqrt(s2)
        grad = np.sin(k) / w
    else:
        tau = sigma / math.sqrt(3)
        w = 2 / tau * math.asin(tau * math.sqrt(s2))
        grad = tau * np.sin(k) / math.sin(w * tau)
    return float(np.dot(grad, n))


def autotests(sources: list[dict], dirs: np.ndarray) -> dict:
    rng = np.random.default_rng(GRAINE + 1)
    # Q : 1 sur un axe, 1/3 sur une diagonale, moyenne 3/5 sur la sphère.
    assert math.isclose(float(np.sum(np.array([1.0, 0, 0]) ** 4)), 1.0)
    assert math.isclose(float(np.sum((np.ones(3) / math.sqrt(3)) ** 4)), 1 / 3)
    rot = matrices(quaternions_uniformes(200_000, rng))
    assert np.allclose(np.einsum('rij,rkj->rik', rot[:50], rot[:50]), np.eye(3), atol=1e-12)
    assert np.allclose(np.linalg.det(rot[:50]), 1.0)
    moy = float(q_facteurs(rot, np.array([[0.3, -0.5, 0.81]]) / np.linalg.norm([0.3, -0.5, 0.81])).mean())
    assert abs(moy - 0.6) < 2e-3, moy
    # Développement v/c = 1 − (ak)²(Q − σ²/3)/8 contre la dispersion exacte.
    for d in ([1, 0, 0], [1, 1, 0], [1, 1, 1], [0.3, 0.5, 0.8]):
        n = np.array(d, float) / np.linalg.norm(d)
        for s in SIGMAS:
            attendu = 1e-4 / 8 * (float(np.sum(n ** 4)) - s * s / 3)
            exact = 1 - vitesse_groupe(n, 1e-2, s)
            if attendu > 1e-12:
                assert math.isclose(exact, attendu, rel_tol=1e-3), (d, s)
            else:
                assert abs(exact) < 1e-12
    # Conventions : recalcul des limites imprimées à partir des paramètres publiés.
    s = {x['id']: x for x in sources}
    verifs = {}
    e = eqg2_publie(s['GRB221009A'])
    verifs['LHAASO_EQG2_depuis_eta2'] = e
    assert math.isclose(e, 4.7e11, rel_tol=0.012)      # imprimé à deux chiffres
    e = EPL_GEV * math.sqrt(1e-16 / s['GRB190114C']['eta2_haut'])
    verifs['MAGIC_GRB_EQG2_depuis_eta2'] = e
    assert math.isclose(e, 6.3e10, rel_tol=0.01)
    k2 = kappa(2, 0.903, 0.272, 0.728)
    verifs['Fermi_kappa2'] = k2
    assert math.isclose(k2, s['GRB090510']['kappa2_imprime'], rel_tol=0.01)
    k2 = kappa(2, 0.49, 0.27, 0.73)
    verifs['PG1553_kappa2'] = k2
    assert math.isclose(k2, s['PG1553']['kappa2_imprime'], rel_tol=0.002)
    assert math.isclose(kappa(1, 0.49, 0.27, 0.73), 0.541, rel_tol=0.002)
    e = math.sqrt(1.5 * distance_k2(s['PG1553'], s['PG1553']['cosmo'])
                  / s['PG1553']['tau2_haut_s_TeV2']) * 1e3
    verifs['PG1553_EQG2_depuis_tau2'] = e
    assert math.isclose(e, 2.10e10, rel_tol=0.01)
    k2 = distance_k2(s['Mrk421'], s['Mrk421']['cosmo'])
    verifs['Mrk421_kappa2_s'] = k2
    assert math.isclose(k2, s['Mrk421']['kappa2_imprime_s'], rel_tol=0.01)
    e = math.sqrt(1.5 * k2 / s['Mrk421']['eta2_s_TeV2']) * 1e3
    verifs['Mrk421_EQG2_sans_syst_depuis_eta2'] = e
    assert math.isclose(e, 3.5e10, rel_tol=0.03)
    meilleur, stat, syst = s['Mrk501']['tau2']
    haut = meilleur + 1.96 * math.hypot(stat, syst)
    e = math.sqrt(1.5 * distance_k2(s['Mrk501'], s['Mrk501']['cosmo']) / haut) * 1e3
    verifs['Mrk501_EQG2_depuis_tau2_1p96sigma'] = e
    assert math.isclose(e, 8.5e10, rel_tol=0.02)
    e = EPL_GEV / math.sqrt(s['PKS2155']['zeta_haut'])
    verifs['PKS2155_EQG2_depuis_zeta'] = e
    assert math.isclose(e, 6.4e10, rel_tol=0.01)
    # Continuité avec le test n° 1 : LHAASO seul, pire orientation, σ = 0.
    b = borne_a_racine_qe(eqg2_publie(s['GRB221009A']))
    assert math.isclose(b * math.sqrt(3), TEST1_PIRE_SIGMA0_M, rel_tol=1e-12)
    # L'optimiseur retrouve la pire orientation connue d'une source seule.
    un = dirs[:1]
    qt = quaternions_uniformes(5_000, rng)
    r0 = pire_orientation(un, np.array([b]), 0.0, qt, rng)
    assert math.isclose(r0['borne_m'], b * math.sqrt(3), rel_tol=1e-6), r0['borne_m']
    r1 = pire_orientation(un, np.array([b]), 1.0, qt, rng)
    assert not r1['fini']                                   # angle mort d'une source seule
    # Deux sources séparées de arccos(1/3) peuvent être mises toutes deux sur des diagonales.
    d1, d2 = np.ones(3) / math.sqrt(3), np.array([1.0, 1.0, -1.0]) / math.sqrt(3)
    r2 = pire_orientation(np.stack([d1, d2]), np.array([b, b]), 1.0, qt, rng)
    assert not r2['fini']
    return verifs


# ------------------------------------------------------------ calcul
def preparer() -> tuple[list[dict], np.ndarray]:
    lignes, dirs = [], []
    for src in SOURCES:
        ra, dec, brut, empreinte = lire_simbad(src['simbad'])
        if SHA256_SIMBAD[src['simbad']] != empreinte:
            raise SystemExit(f"{src['simbad']} modifié : sha256 {empreinte}")
        e_pub = eqg2_publie(src)
        e_com = eqg2_commune(src)
        k_pub = distance_k2(src, src['cosmo'])
        k_com = distance_k2(src, COSMO_COMMUNE if src['cosmo'] else None)
        lignes.append({
            'id': src['id'], 'nom': src['nom'], 'type': src['type'], 'instrument': src['instrument'],
            'arxiv': f"https://arxiv.org/abs/{src['arxiv']}", 'methode': src['methode'],
            'ra_deg': ra, 'dec_deg': dec, 'simbad': brut, 'simbad_sha256': empreinte,
            'z': src.get('z'), 'distance_kpc': src.get('distance_kpc'),
            'cosmologie_publiee': src['cosmo'],
            'EQG2_publie_GeV': e_pub, 'EQG2_imprime_GeV': src['EQG2_imprime_GeV'],
            'K2_publie_s': k_pub, 'K2_commun_s': k_com,
            'facteur_cosmologie': e_com / e_pub,
            'EQG2_commun_GeV': e_com,
            'a_racine_Qeff_max_m': borne_a_racine_qe(e_com),
        })
        dirs.append(vecteur(ra, dec))
    return lignes, np.array(dirs)


def seule_pire(b: float, sigma: float) -> float | None:
    qe = 1 / 3 - sigma ** 2 / 3
    return b / math.sqrt(qe) if qe > 1e-12 else None


def angles_entre(dirs: np.ndarray) -> list[list[float]]:
    c = np.clip(dirs @ dirs.T, -1, 1)
    return np.degrees(np.arccos(c)).round(3).tolist()


def calculer() -> dict:
    lignes, dirs = preparer()
    verifs = autotests(SOURCES, dirs)
    b = np.array([l['a_racine_Qeff_max_m'] for l in lignes])
    rng = np.random.default_rng(GRAINE)
    q_tirees = quaternions_uniformes(N_ORIENTATIONS, rng)

    par_sigma = []
    for s in SIGMAS:
        r = pire_orientation(dirs, b, s, q_tirees, rng)
        r['sigma_courant'] = s
        r['sources_actives_noms'] = [lignes[i]['nom'] for i in r.get('sources_actives', [])]
        r['LHAASO_seul_pire_m'] = seule_pire(b[0], s)
        r['echelle_min_GeV'] = HBAR_C_GEV_M / r['borne_m'] if r['fini'] else None
        par_sigma.append(r)
    # Reproductibilité de l'optimum : autre graine, autre tirage.
    rng2 = np.random.default_rng(GRAINE + 7)
    controle = pire_orientation(dirs, b, 1.0, quaternions_uniformes(N_ORIENTATIONS, rng2), rng2)
    ecart_graines = abs(controle['borne_m'] / par_sigma[-1]['borne_m'] - 1)
    assert ecart_graines < 1e-3, ecart_graines
    # Monotonie : la borne ne fait que croître avec σ ; σ = 1 couvre tout σ ≤ 1.
    valeurs = [r['borne_m'] for r in par_sigma]
    assert all(x <= y * (1 + 1e-9) for x, y in zip(valeurs, valeurs[1:]))

    # Variantes (σ = 0 et σ = 1).
    def variante(indices: list[int], b_var: np.ndarray) -> dict:
        rv = np.random.default_rng(GRAINE + 3)
        qv = quaternions_uniformes(N_ORIENTATIONS_VARIANTES, rv)
        sortie = {}
        for s in (0.0, 1.0):
            r = pire_orientation(dirs[indices], b_var[indices], s, qv, rv)
            sortie[f'sigma_{s:g}'] = {'pire_m': r['borne_m'] if r['fini'] else None,
                                      'quantile95_m': r['quantile95_m']}
        return sortie

    tous = list(range(len(lignes)))
    b_brut = np.array([borne_a_racine_qe(l['EQG2_publie_GeV']) for l in lignes])
    b_fermi_v = b.copy()
    src_fermi = next(x for x in SOURCES if x['id'] == 'GRB090510')
    b_fermi_v[2] = borne_a_racine_qe(eqg2_commune(src_fermi, FERMI_TABLEAU_V_GEV))
    variantes = {
        'sans_LHAASO': variante(tous[1:], b),
        'sans_cosmologie_commune': variante(tous, b_brut),
        'Fermi_tableau_V': variante(tous, b_fermi_v),
        'sursauts_seuls': variante([0, 1, 2], b),
        'blazars_et_pulsar_seuls': variante([3, 4, 5, 6, 7], b),
    }

    x_m = par_sigma[-1]['borne_m']
    b_beane = HBAR_C_GEV_M / BEANE_INV_B_GEV
    return {
        'titre': 'Test n° 3 : dispersion directionnelle de la lumière, huit sources combinées',
        'date': '2026-09-28',
        'niveau': "Analyse secondaire de limites publiées ; aucun photon réanalysé",
        'hypotheses': [
            'Réseau cubique de maille physique a, au repos dans le référentiel cosmologique, orientation R inconnue',
            'Photon régi par Maxwell discrétisé (schéma de Yee), sans terme compensateur',
            'v/c = 1 − (Q − σ²/3)(aE/ħc)²/8, Q = Σ n_i⁴ dans les axes du réseau, 0 ≤ σ ≤ 1',
            'Retard de Jacob et Piran : Δt = (3/2)(ΔE²/E_QG,2²) K2, K2 = ∫(1+z)²/H dz (d/c pour le Crabe)',
            "Aucun effet intrinsèque aux sources (hypothèse de chaque article)",
        ],
        'constantes': {'hbar_c_GeV_m': HBAR_C_GEV_M, 'E_Pl_GeV': EPL_GEV,
                       'cosmologie_commune': COSMO_COMMUNE, 'graine': GRAINE,
                       'n_orientations': N_ORIENTATIONS},
        'sources': lignes,
        'n_sources': len(lignes),
        'angles_entre_sources_deg': angles_entre(dirs),
        'verifications_conventions': verifs,
        'par_sigma': par_sigma,
        'resume': {
            'pire_sigma0_m': par_sigma[0]['borne_m'],
            'pire_sigma05_m': par_sigma[1]['borne_m'],
            'pire_sigma09_m': par_sigma[2]['borne_m'],
            'pire_sigma1_m': x_m,
            'q95_sigma0_m': par_sigma[0]['quantile95_m'],
            'q95_sigma05_m': par_sigma[1]['quantile95_m'],
            'q95_sigma09_m': par_sigma[2]['quantile95_m'],
            'q95_sigma1_m': par_sigma[-1]['quantile95_m'],
            'mediane_sigma1_m': par_sigma[-1]['mediane_m'],
            'angle_mort_ferme': bool(par_sigma[-1]['fini']),
            'maille_exclue_toutes_orientations_m': x_m,
            'echelle_min_toutes_orientations_GeV': HBAR_C_GEV_M / x_m,
            'rapport_sur_test1_sigma0': x_m / TEST1_PIRE_SIGMA0_M,
            'test1_pire_sigma0_m': TEST1_PIRE_SIGMA0_M,
            'beane_b_max_m': b_beane,
            'rapport_sur_beane': x_m / b_beane,
            'rapport_sigma0_sur_beane': par_sigma[0]['borne_m'] / b_beane,
            'ecart_relatif_deux_graines_sigma1': ecart_graines,
            'aE_sur_hbar_c_20TeV_a_la_borne': x_m * 2e4 / HBAR_C_GEV_M,
            'angle_entre_diagonales_deg': math.degrees(math.acos(1 / 3)),
            'angle_GRB190114C_GRB090510_deg': angles_entre(dirs)[1][2],
            'angle_GRB090510_PKS2155_deg': angles_entre(dirs)[2][5],
            'angle_diag_GRB221009A_pire_sigma1_deg': par_sigma[-1]['angle_a_la_diagonale_la_plus_proche_deg'][0],
            'Qeff_GRB221009A_pire_sigma1': par_sigma[-1]['Q_eff_par_source'][0],
            'n_sources_actives_sigma1': len(par_sigma[-1]['sources_actives']),
            'couverture_min_bonferroni_sigma1': 1 - 0.05 * len(par_sigma[-1]['sources_actives']),
            'facteur_cosmologie_max': max(l['facteur_cosmologie'] for l in lignes),
            'facteur_cosmologie_min': min(l['facteur_cosmologie'] for l in lignes),
            'rapport_sur_longueur_Planck': x_m / LPL_M,
            'rapport_B_autres_sur_LHAASO_min': float(b[1:].min() / b[0]),
            'rapport_B_autres_sur_LHAASO_max': float(b[1:].max() / b[0]),
        },
        'variantes': variantes,
        'autotests': 'OK',
        'references': {
            'Beane_Davoudi_Savage': 'https://arxiv.org/abs/1210.1847v2',
            'SIMBAD': 'https://simbad.cds.unistra.fr/simbad/',
            'CODATA': 'https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
        },
        'limites': [
            'Limites publiées à 95 % prises une à une : la borne combinée, minimum de plusieurs limites, '
            'a une couverture inférieure à 95 % (au pire 1 − 5 % × nombre de sources actives)',
            'Chaque article suppose l’absence de décalage intrinsèque à la source',
            'Les fractions d’orientations sont géométriques, pas des probabilités sur l’Univers',
            'Un schéma amélioré (erreur en a⁴) ou des termes compensateurs échappent à cette borne',
        ],
    }


def resume_texte(r: dict) -> str:
    lignes = []
    for s in r['sources']:
        lignes.append(f"{s['nom']:16s} RA {s['ra_deg']:8.3f} Dec {s['dec_deg']:+8.3f} "
                      f"E_QG,2 publiée {s['EQG2_publie_GeV']:.3g} -> commune {s['EQG2_commun_GeV']:.3g} GeV "
                      f"(x{s['facteur_cosmologie']:.4f}) | a·racine(Qe) <= {s['a_racine_Qeff_max_m']:.3e} m")
    for p in r['par_sigma']:
        pire = f"{p['borne_m']:.3e} m" if p['fini'] else 'aucune borne'
        lignes.append(f"sigma = {p['sigma_courant']:<4} pire orientation : {pire:>12} | 95 % : "
                      f"{p['quantile95_m']:.3e} m | médiane : {p['mediane_m']:.3e} m | actives : "
                      f"{', '.join(p['sources_actives_noms'])}")
    z = r['resume']
    lignes.append(f"Angle mort fermé : {z['angle_mort_ferme']} ; maille exclue >= {z['maille_exclue_toutes_orientations_m']:.3e} m "
                  f"(échelle >= {z['echelle_min_toutes_orientations_GeV']:.3e} GeV) ; "
                  f"x{z['rapport_sur_test1_sigma0']:.2f} test 1 (sigma 0) ; x{z['rapport_sur_beane']:.2f} Beane")
    for nom, v in r['variantes'].items():
        lignes.append(f"variante {nom:24s} " + ' | '.join(
            f"{k} : pire {('%.3e' % x['pire_m']) if x['pire_m'] else 'aucune'} m, 95 % {x['quantile95_m']:.3e} m"
            for k, x in v.items()))
    return '\n'.join(lignes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('resultats.json'))
    args = parser.parse_args()
    resultat = calculer()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2), encoding='utf-8')
    print(resume_texte(resultat))
