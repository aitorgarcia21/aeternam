#!/usr/bin/env python3
"""aeternam, test n° 6 : le ciel entier a-t-il la symétrie d'un cube ?

Suite du test n° 2 (recherche/2026-09-28-rayons-cosmiques/) : même prédiction
(Beane, Davoudi et Savage, arXiv:1210.1847), même statistique, même calibration
par ciels simulés, même maximisation sur l'orientation, mais sur tout le ciel
(Auger au sud, Telescope Array au nord) et avec dix fois plus d'événements.

Données
  Sud. Observatoire Pierre Auger : liste publique complète des 2 635 événements
    au-dessus de 32 EeV (1er janvier 2004 - 31 décembre 2020, zénith <= 80°),
    ApJ 935, 170 (2022), arXiv:2206.13492, DOI 10.5281/zenodo.6504276
    (CC BY-SA 4.0). Fichier d'origine copié dans donnees/.
  Nord. Telescope Array : les 72 événements au-dessus de 57 EeV (11 mai 2008 -
    4 mai 2013, zénith < 55°), ApJL 790, L21 (2014), tableau 1, arXiv:1404.5890.
    Table sous droits (© AAS, tous droits réservés) : elle n'est pas versionnée ;
    le script la télécharge à la première exécution (table lisible par machine
    de l'éditeur, ou source LaTeX de la version arXiv en secours) et vérifie
    les empreintes SHA-256 du fichier et de la liste lue.
  Échelle d'énergie. Conversion publiée par le groupe de travail Auger-TA pour
    cette sélection TA (coupures lâches, E_TA >= 57 EeV), arXiv:2507.10441 :
    E_Auger / 10 EeV = exp(-0,159) (E_TA / 10 EeV)^0,954, d'où 57 EeV (TA) =
    44,88 EeV (Auger). L'échantillon principal réunit donc les événements Auger
    d'au moins 44,88 EeV et les 72 événements TA.

Méthode (fixée avant de calculer la statistique sur ces données)
  0. Trois lots, chacun avec son exposition géométrique (Sommers 2001, efficacité
     de détection totale à ces énergies) : Auger vertical (latitude -35,2°,
     zénith < 60°), Auger incliné (60° à 80°), TA (latitude +39,30°, zénith < 55°).
     Le nombre d'événements de chaque lot est tenu fixe (on conditionne sur lui),
     comme Auger le fait pour ses lots vertical et incliné : le test ne dépend
     alors ni des expositions absolues ni de l'écart d'échelle d'énergie.
  1. Statistique du test n° 2, étendue aux lots :
       T(R) = [somme_i f(R n_i) - somme_d N_d <f>_d] / racine(somme_d N_d Var_d f),
     f(R n) = somme_k (e_k . n)^4 = Q, harmonique cubique l = 4.
  2. Z4 = max de |T(R)| sur les 20 000 orientations du test n° 2 (même graine).
  3. p-valeur : 20 000 ciels isotropes simulés lot par lot, même maximisation
     (le coût du choix de l'orientation est inclus). Test principal : l = 4 ;
     tests secondaires : l = 6 et l = 4 + 6.
  4. Limite supérieure à 95 % sur l'amplitude eps du motif 1 + eps (5Q - 3)/2 :
     (a) orientation tirée au hasard pour chaque ciel (comme au test n° 2) ;
     (b) 16 orientations fixes, dont la moins visible et les deux pires de (c),
         par Monte-Carlo ;
     (c) chacune des 20 000 orientations, par une borne analytique
         conservatrice : Z4 >= |T(R0)| et T(R0) suit une loi normale dont la
         moyenne et la variance sous le signal se calculent exactement ;
         la même borne est calculée pour la configuration du test n° 2.
  5. Contrôles prévus d'avance : variantes (Auger seul ; plus hautes énergies ;
     N maximal ; deux autres étalonnages ; sans correction d'échelle ; exposition
     Auger d'un seul bloc ; avec l'événement Amaterasu ; excès connus de
     Centaurus A et du point chaud TA masqués) ; excès observé autour des six
     axes et des huit diagonales de la meilleure orientation.
  6. Ajouté après coup, parce que la variante « N maximal » donnait p < 0,01, et
     signalé comme tel : variantes N maximal (Auger seul, excès masqués) et Auger
     32-44,88 EeV ; reproduction (orientation choisie sur les événements Auger de
     32 à 44,88 EeV, absents de l'échantillon principal, puis T évalué sur celui-ci) ;
     p-valeurs sous un ciel portant le dipôle ajusté aux données.

Python >= 3.10 et numpy. Usage : python3 analyse.py --out resultats.json
"""
from __future__ import annotations

import argparse
import hashlib
import io
import itertools
import json
import math
import re
import tarfile
import time
import urllib.request
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
DONNEES = ICI / 'donnees'
TEST2 = ICI.parent / '2026-09-28-rayons-cosmiques' / 'resultats.json'

AUGER = DONNEES / 'AugerApJS2022_Yr_JD_UTC_Th_Ph_RA_Dec_E_Expo.dat'
SHA_AUGER = 'b03b91b5b4bf98b373cde2a9f41044704a32af77029cf9c07044e6860ffabb35'
AMATERASU = DONNEES / 'tasd_highest_event_244EeV_backtrack_JF_PT_eq.dat'
SHA_AMATERASU = '980b0cb04f78edbed022a5d059d72b5ebc27467c664694a7b81cd96aa44ed0ee'
TA_MRT = DONNEES / 'apjl498370t1_mrt.txt'          # non versionné (© AAS)
TA_MRT_URL = ('https://content.cld.iop.org/journals/2041-8205/790/2/L21/'
              'revision1/apjl498370t1_mrt.txt')
SHA_TA_MRT = '0c8dcc83e95e7b2bc30c787ffcce7330783aa2c488d4b44a1d7b82c990134525'
TA_TEX_URL = 'https://arxiv.org/e-print/1404.5890v3'
SHA_TA_TEX = 'f93ba17024acb77cbf83b2c7c5896ccf0f7a96dcc396e249a38e1f086653c878'
SHA_TA_LISTE = 'e5c47447625d53dc6955c70a96d921e1db64f71c2735e543718eb127fbcfaee8'

LAT_AUGER = -35.2          # arXiv:1411.6111 p. 9 ; code Auger (Zenodo 6504276, Data/exposure.cc)
LAT_TA = 39.30             # arXiv:1404.5890 p. 4 ; code TA (Zenodo 8427755, utility4anisotropy.py)
ZEN_VERTICAL = 60.0        # Auger : verticaux < 60°, inclinés 60° à 80° (arXiv:2206.13492 p. 2)
ZEN_INCLINE = 80.0
ZEN_TA = 55.0              # TA : zénith < 55° (arXiv:1404.5890 p. 4)
SEUIL_TA = 57.0            # EeV, échelle TA

# Étalonnage croisé du groupe de travail Auger-TA : E_Auger / 10 EeV = exp(alpha) (E_TA / 10 EeV)^beta
ETALONNAGES = {
    'principal': {'alpha': -0.159, 'beta': 0.954,
                  'source': 'arXiv:2507.10441 (ICRC 2025), p. 3 : étalonnage de PoS(UHECR2024)009, '
                            'appliqué aux données TA à coupures lâches, E_TA >= 57 EeV'},
    'icrc2025_strict': {'alpha': -0.150, 'beta': 0.962,
                        'source': 'arXiv:2507.10441 (ICRC 2025), p. 3 : données TA à coupures strictes'},
    'uhecr2022': {'alpha': -0.159, 'beta': 0.945, 'source': 'arXiv:2302.04502 (UHECR 2022), p. 3'},
    'icrc2021': {'alpha': math.log(0.857), 'beta': 0.937,
                 'source': 'arXiv:2111.12366 (ICRC 2021), éq. (1) : E_Auger = 8,57 (E_TA / 10 EeV)^0,937 EeV'},
}

# Excès connus (variante « excès masqués ») : (ascension droite, déclinaison, rayon), degrés
CENTAURUS_A = (201.4, -43.0, 27.0)     # arXiv:2206.13492 § 5 : E >= 38 EeV, 215 observés / 152,0 attendus
POINT_CHAUD_TA = (146.7, 43.2, 20.0)   # arXiv:1404.5890 § 4 : 19 observés / 4,49 attendus

N_ORIENTATIONS = 20_000
N_CIELS = 20_000
N_CIELS_VARIANTE = 10_000
N_CIELS_SIGNAL = 1_000
AMPLITUDES = (0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5, 0.6)
N_ORIENT_FIXES = 16
N_CIELS_FIXES = 400
FACTEURS_FIXES = (0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1)
RAYON_CONES = 30.0
GRAINE = 20260928
MOIS = {m: i + 1 for i, m in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split())}


# ================================================================ données
def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def vecteurs(ra: np.ndarray, dec: np.ndarray) -> np.ndarray:
    c = np.cos(dec)
    return np.stack([c * np.cos(ra), c * np.sin(ra), np.sin(dec)], axis=-1)


def vecteur_deg(ra: float, dec: float) -> np.ndarray:
    return vecteurs(np.radians(np.array([ra])), np.radians(np.array([dec])))[0]


def lire_auger() -> dict:
    brut = AUGER.read_bytes()
    if sha256(brut) != SHA_AUGER:
        raise SystemExit(f'{AUGER.name} modifié : sha256 {sha256(brut)}')
    lignes = [l.split() for l in brut.decode('ascii').splitlines() if l.strip() and not l.startswith('#')]
    a = np.array([[float(x) for x in l] for l in lignes])
    return {'annee': a[:, 0], 'utc': a[:, 2], 'theta': a[:, 3], 'ra': a[:, 5], 'dec': a[:, 6], 'E': a[:, 7]}


def _telecharger(url: str) -> bytes:
    req = urllib.request.Request(url, headers={'User-Agent': 'aeternam-analyse/1.0 (recherche reproductible)'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _ta_depuis_mrt(texte: str) -> list[tuple]:
    out = []
    for l in texte.splitlines():
        if re.match(r'^\d{4} [A-Z][a-z]{2} ', l):
            date = (int(l[0:4]), MOIS[l[5:8]], int(l[9:11]), int(l[12:14]), int(l[15:17]), int(l[18:20]))
            out.append((date, float(l[21:26]), float(l[27:32]), float(l[33:39]), float(l[40:46])))
    return out


def _ta_depuis_tex(texte: str) -> list[tuple]:
    i = texte.find(r'\startdata', texte.find('List of Telescope Array events'))
    j = texte.find(r'\enddata', i)
    out = []
    motif = (r'\s*(\d{4}) ([A-Z][a-z]{2}) (\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s*&\s*([\d.]+)\s*&\s*([\d.]+)'
             r'\s*&\s*([\d.]+)\s*&\s*(\$-\$)?([\d.]+)')
    for l in texte[i:j].splitlines():
        m = re.match(motif, l)
        if m:
            g = m.groups()
            date = (int(g[0]), MOIS[g[1]], int(g[2]), int(g[3]), int(g[4]), int(g[5]))
            out.append((date, float(g[6]), float(g[7]), float(g[8]), float(g[10]) * (-1 if g[9] else 1)))
    return out


def empreinte_liste_ta(ev: list[tuple]) -> str:
    texte = ''.join('%04d-%02d-%02dT%02d:%02d:%02d %.2f %.1f %.2f %.2f\n' % (*d, t, e, a, b)
                    for d, t, e, a, b in ev)
    return sha256(texte.encode())


def lire_ta() -> tuple[list[tuple], str]:
    """Les 72 événements TA : copie locale, sinon table de l'éditeur, sinon source LaTeX arXiv."""
    brut, source = None, None
    if TA_MRT.exists():
        brut, source = TA_MRT.read_bytes(), 'table de l’éditeur (copie locale)'
    else:
        try:
            brut, source = _telecharger(TA_MRT_URL), 'table de l’éditeur (téléchargée)'
        except Exception as err:                                  # noqa: BLE001
            print(f'table TA de l’éditeur indisponible ({err}) ; essai de la source LaTeX arXiv')
    if brut is not None:
        if sha256(brut) != SHA_TA_MRT:
            raise SystemExit(f'table TA modifiée : sha256 {sha256(brut)}')
        if not TA_MRT.exists():
            DONNEES.mkdir(exist_ok=True)
            TA_MRT.write_bytes(brut)
        ev = _ta_depuis_mrt(brut.decode('ascii'))
    else:
        try:
            tgz = _telecharger(TA_TEX_URL)
            tex = tarfile.open(fileobj=io.BytesIO(tgz)).extractfile('ms.tex').read()
        except Exception as err:                                  # noqa: BLE001
            raise SystemExit(f'table TA introuvable ({err}). Télécharger {TA_MRT_URL} '
                             f'dans {TA_MRT} (sha256 {SHA_TA_MRT}).')
        if sha256(tex) != SHA_TA_TEX:
            raise SystemExit(f'source arXiv modifiée : sha256 {sha256(tex)}')
        ev, source = _ta_depuis_tex(tex.decode('latin-1')), 'source LaTeX arXiv:1404.5890v3'
    if empreinte_liste_ta(ev) != SHA_TA_LISTE:
        raise SystemExit(f'liste TA inattendue : {empreinte_liste_ta(ev)}')
    return ev, source


def lire_amaterasu() -> dict:
    brut = AMATERASU.read_bytes()
    if sha256(brut) != SHA_AMATERASU:
        raise SystemExit(f'{AMATERASU.name} modifié : sha256 {sha256(brut)}')
    c = brut.decode('ascii').splitlines()[0].split()          # 1re ligne : direction mesurée
    return {'ra': float(c[0]), 'dec': float(c[1]), 'E_EeV': float(c[3]), 'date': c[4], 'heure_utc': c[5]}


def e_auger(e_ta_eev: float, etal: dict) -> float:
    return 10.0 * math.exp(etal['alpha']) * (e_ta_eev / 10.0) ** etal['beta']


def e_ta(e_auger_eev: float, etal: dict) -> float:
    return 10.0 * math.exp(-etal['alpha'] / etal['beta']) * (e_auger_eev / 10.0) ** (1.0 / etal['beta'])


# ================================================================ exposition
def _sommers(dec: np.ndarray, a0: float, tm: float) -> np.ndarray:
    """Exposition relative (Sommers 2001) d'un détecteur à la latitude a0 pour zénith <= tm."""
    if tm <= 0.0:
        return np.zeros_like(dec)
    with np.errstate(divide='ignore', invalid='ignore'):
        xi = (math.cos(tm) - math.sin(a0) * np.sin(dec)) / (math.cos(a0) * np.cos(dec))
    am = np.arccos(np.clip(np.nan_to_num(xi, nan=1.0), -1.0, 1.0))
    return math.cos(a0) * np.cos(dec) * np.sin(am) + am * math.sin(a0) * np.sin(dec)


class Lot:
    """Un lot d'événements (directions unitaires) et son exposition géométrique."""

    def __init__(self, nom: str, latitude: float, zen_min: float, zen_max: float, n: np.ndarray,
                 masques=()):
        self.nom, self.latitude, self.zen = nom, latitude, (zen_min, zen_max)
        self.a0, self.t1, self.t2 = math.radians(latitude), math.radians(zen_min), math.radians(zen_max)
        self.masques = [(vecteur_deg(ra, dec), math.cos(math.radians(r))) for ra, dec, r in masques]
        self.n = n[self.hors_masques(n)] if self.masques else n
        g = np.linspace(-math.pi / 2, math.pi / 2, 400_001)
        self.w_max = float(np.max(self.omega(g))) * (1 + 1e-9)
        self._quad = {}
        _, p = self._brute(*self._defaut())
        self.acceptance = float(np.sum(p) / (2.0 * self.w_max))   # moyenne de omega sur la sphère / max

    def omega(self, dec: np.ndarray) -> np.ndarray:
        return np.clip(_sommers(dec, self.a0, self.t2) - _sommers(dec, self.a0, self.t1), 0.0, None)

    def hors_masques(self, v: np.ndarray) -> np.ndarray:
        garde = np.ones(v.shape[:-1], dtype=bool)
        for u, c in self.masques:
            garde &= v @ u < c
        return garde

    def _defaut(self):
        return (600, 1080) if self.masques else (400, 64)

    def _brute(self, n_dec: int, n_ra: int):
        x, wx = np.polynomial.legendre.leggauss(n_dec)            # x = sin(dec)
        ra = (np.arange(n_ra) + 0.5) * 2 * math.pi / n_ra
        dec = np.arcsin(x)
        D, A = np.meshgrid(dec, ra, indexing='ij')
        v = vecteurs(A.ravel(), D.ravel())
        p = ((wx * self.omega(dec))[:, None] * np.ones_like(A)).ravel() / n_ra
        if self.masques:
            p = p * self.hors_masques(v)
        return v, p

    def quadrature(self, n_dec: int | None = None, n_ra: int | None = None):
        """Points et poids : <g>_lot = somme(p g) (Gauss-Legendre en sin(dec), uniforme en ascension droite)."""
        cle = (n_dec, n_ra) if n_dec else self._defaut()
        if cle not in self._quad:
            v, p = self._brute(*cle)
            self._quad[cle] = (v, p / p.sum())
        return self._quad[cle]

    def tirer(self, rng: np.random.Generator, n: int, poids=None) -> np.ndarray:
        """n directions d'un ciel isotrope vu par ce lot ; poids(v) <= 1 optionnel (signal injecté)."""
        sortie, reste = [], n
        while reste > 0:
            m = int(1.3 * reste / self.acceptance) + 256
            dec = np.arcsin(rng.uniform(-1.0, 1.0, m))
            v = vecteurs(rng.uniform(0.0, 2 * math.pi, m), dec)
            acc = self.omega(dec) / self.w_max
            if self.masques:
                acc = acc * self.hors_masques(v)
            if poids is not None:
                acc = acc * poids(v)
            v = v[rng.uniform(0.0, 1.0, m) < acc]
            sortie.append(v[:reste])
            reste -= len(sortie[-1])
        return np.concatenate(sortie)


# ================================================================ polynômes
def multi_indices(d: int) -> list[tuple[int, int, int]]:
    return [(a, b, d - a - b) for a in range(d, -1, -1) for b in range(d - a, -1, -1)]


def multinomial(al) -> int:
    return math.factorial(sum(al)) // math.prod(math.factorial(k) for k in al)


def _puissances(n: np.ndarray, dmax: int):
    x, y, z = n[..., 0], n[..., 1], n[..., 2]
    px, py, pz = [np.ones_like(x), x], [np.ones_like(y), y], [np.ones_like(z), z]
    for _ in range(2, dmax + 1):
        px.append(px[-1] * x)
        py.append(py[-1] * y)
        pz.append(pz[-1] * z)
    return px, py, pz


def monomes(n: np.ndarray, indices) -> np.ndarray:
    px, py, pz = _puissances(n, max(sum(i) for i in indices))
    return np.stack([px[a] * py[b] * pz[c] for a, b, c in indices], axis=-1)


def sommes_monomes(ciels: np.ndarray, listes) -> list[np.ndarray]:
    """Pour des ciels (k, N, 3) : sommes sur les N événements de chaque monôme."""
    px, py, pz = _puissances(ciels, max(sum(i) for idx in listes for i in idx))
    return [np.stack([(px[a] * py[b] * pz[c]).sum(axis=-1) for a, b, c in idx], axis=-1) for idx in listes]


def coefficients_puissance(E: np.ndarray, d: int, indices_cible) -> np.ndarray:
    """Coefficients, dans les monômes de degré D, de somme_k (e_k . n)^d (n . n)^((D-d)/2),
    pour chaque orientation (lignes e_k de E = axes de la grille)."""
    D = sum(indices_cible[0])
    k = (D - d) // 2
    col = {al: i for i, al in enumerate(indices_cible)}
    out = np.zeros((E.shape[0], len(indices_cible)))
    for al in multi_indices(d):
        c = multinomial(al) * np.sum(E[:, :, 0] ** al[0] * E[:, :, 1] ** al[1] * E[:, :, 2] ** al[2], axis=1)
        for be in multi_indices(k):
            out[:, col[(al[0] + 2 * be[0], al[1] + 2 * be[1], al[2] + 2 * be[2])]] += c * multinomial(be)
    return out


def coefficients_unite(indices) -> np.ndarray:
    """Coefficients de (n . n)^(D/2), égal à 1 sur la sphère."""
    D = sum(indices[0])
    col = {al: i for i, al in enumerate(indices)}
    u = np.zeros(len(indices))
    for be in multi_indices(D // 2):
        u[col[(2 * be[0], 2 * be[1], 2 * be[2])]] += multinomial(be)
    return u


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
    """alpha tel que somme n^6 + alpha somme n^4 (+ constante) soit l = 6 pur (vaut -15/11)."""
    x, wx = np.polynomial.legendre.leggauss(60)
    ra = (np.arange(64) + 0.5) * 2 * math.pi / 64
    D, A = np.meshgrid(np.arcsin(x), ra, indexing='ij')
    v = vecteurs(A.ravel(), D.ravel())
    p = (wx[:, None] * np.ones_like(A)).ravel()
    p /= p.sum()
    i4, i6 = np.sum(v ** 4, axis=1), np.sum(v ** 6, axis=1)
    c4 = i4 - np.sum(p * i4)
    return -float(np.sum(p * i6 * c4) / np.sum(p * c4 * c4))


def Q(v: np.ndarray) -> np.ndarray:
    return np.sum(v ** 4, axis=-1)


class Statistique:
    """T(R) = c(R).(P - somme_d N_d mu_d) / racine(c(R)^T (somme_d N_d S_d) c(R))."""

    def __init__(self, E: np.ndarray, degre: int, lots: list[Lot], alpha: float = 0.0):
        self.idx = multi_indices(degre)
        self.C = coefficients_puissance(E, degre, self.idx)
        if alpha:
            self.C += alpha * coefficients_puissance(E, degre - 2, self.idx)
        m = len(self.idx)
        self.mu, self.S = np.zeros(m), np.zeros((m, m))
        for lot in lots:
            v, w = lot.quadrature()
            M = monomes(v, self.idx)
            mu = w @ M
            self.mu += len(lot.n) * mu
            self.S += len(lot.n) * ((M * w[:, None]).T @ M - np.outer(mu, mu))
        self.sd = np.sqrt(np.einsum('ri,ij,rj->r', self.C, self.S, self.C))

    def T(self, P: np.ndarray, sel=slice(None)) -> np.ndarray:
        """P : (ciels, monômes) sommes brutes ; renvoie (orientations, ciels)."""
        return (self.C[sel] @ (np.atleast_2d(P) - self.mu).T) / self.sd[sel, None]


def statistiques(E, lots, alpha6):
    return Statistique(E, 4, lots), Statistique(E, 6, lots, alpha6)


def observer(stats, lots) -> dict:
    n = np.concatenate([l.n for l in lots])
    P4, P6 = sommes_monomes(n[None], [stats[0].idx, stats[1].idx])
    T4, T6 = stats[0].T(P4)[:, 0], stats[1].T(P6)[:, 0]
    return {'T4': T4, 'T6': T6, 'Z4': float(np.max(np.abs(T4))), 'Z6': float(np.max(np.abs(T6))),
            'Z46': float(np.max(T4 ** 2 + T6 ** 2)), 'n': n}


# ================================================================ simulations
def _ciels(rng, lots, k, poids=None):
    return np.concatenate([l.tirer(rng, len(l.n) * k, poids).reshape(k, len(l.n), 3) for l in lots], axis=1)


def _taille_lot(N: int) -> int:
    return max(20, min(500, 300_000 // N))


def simuler_nul(rng, lots, stats, n_ciels) -> list[np.ndarray]:
    """Z4, Z6, Z46 de n_ciels ciels isotropes (nombre d'événements de chaque lot fixé)."""
    N = sum(len(l.n) for l in lots)
    z = [[], [], []]
    for debut in range(0, n_ciels, _taille_lot(N)):
        k = min(_taille_lot(N), n_ciels - debut)
        P4, P6 = sommes_monomes(_ciels(rng, lots, k), [stats[0].idx, stats[1].idx])
        T4, T6 = stats[0].T(P4), stats[1].T(P6)
        z[0].append(np.max(np.abs(T4), axis=0))
        z[1].append(np.max(np.abs(T6), axis=0))
        z[2].append(np.max(T4 ** 2 + T6 ** 2, axis=0))
    return [np.concatenate(a) for a in z]


def T_simules(rng, lots, stat, k, sel, poids=None) -> np.ndarray:
    """T(R) pour les orientations sel, sur k ciels simulés (par paquets, mémoire bornée)."""
    out = []
    for debut in range(0, k, 300):
        m = min(300, k - debut)
        out.append(stat.T(sommes_monomes(_ciels(rng, lots, m, poids), [stat.idx])[0], sel))
    return np.concatenate(out, axis=1)


def poids_signal(eps: float, R0: np.ndarray):
    """Densité relative 1 + eps (5 Q(R0 n) - 3) / 2, ramenée à un maximum de 1.
    eps > 0 : excès vers les 6 axes de la grille ; eps < 0 : vers les 8 diagonales."""
    haut = 1 + max(eps, -2 * eps / 3)
    return lambda v: (1 + eps * (5 * Q(v @ R0.T) - 3) / 2) / haut


def z4_signal_fixe(rng, lots, stat4, eps, R0, n_ciels) -> np.ndarray:
    """Z4 de ciels portant un motif d'amplitude eps et d'orientation R0 fixée."""
    N = sum(len(l.n) for l in lots)
    out = []
    for debut in range(0, n_ciels, _taille_lot(N)):
        k = min(_taille_lot(N), n_ciels - debut)
        P4 = sommes_monomes(_ciels(rng, lots, k, poids_signal(eps, R0)), [stat4.idx])[0]
        out.append(np.max(np.abs(stat4.T(P4)), axis=0))
    return np.concatenate(out)


def z4_signal_aleatoire(rng, lots, stat4, eps, n_ciels) -> np.ndarray:
    """Z4 de ciels portant un motif d'amplitude eps ; orientation tirée au hasard pour chaque ciel,
    la même pour tous les lots d'un ciel."""
    out = []
    for debut in range(0, n_ciels, 100):
        k = min(100, n_ciels - debut)
        ciels = []
        for _ in range(k):
            w = poids_signal(eps, rotations(rng, 1)[0])
            ciels.append(np.concatenate([l.tirer(rng, len(l.n), w) for l in lots]))
        P4 = sommes_monomes(np.stack(ciels), [stat4.idx])[0]
        out.append(np.max(np.abs(stat4.T(P4)), axis=0))
    return np.concatenate(out)


def p_valeur(nuls: np.ndarray, obs: float) -> float:
    return float((1 + np.sum(nuls >= obs)) / (1 + len(nuls)))


def croisement_95(points) -> float | None:
    """Amplitude où la fraction de ciels dépassant Z4 observé franchit 0,95 (interpolation linéaire)."""
    pts = sorted(points)
    for (a0, f0), (a1, f1) in zip(pts, pts[1:]):
        if f0 < 0.95 <= f1:
            return a0 + (0.95 - f0) * (a1 - a0) / (f1 - f0)
    return None


# ================================================================ borne analytique
def _phi(x: np.ndarray) -> np.ndarray:
    """Fonction de répartition normale (erfc de Numerical Recipes, erreur relative < 1,2e-7)."""
    z = np.abs(x) / math.sqrt(2)
    t = 1.0 / (1.0 + 0.5 * z)
    r = t * np.exp(-z * z - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * (0.09678418 + t * (
        -0.18628806 + t * (0.27886187 + t * (-1.13520398 + t * (1.48851587 + t * (-0.82215223 + t * 0.17087277)))))))))
    return np.where(x >= 0, 1 - 0.5 * r, 0.5 * r)


class BorneAnalytique:
    """Moyenne et variance exactes de T(R0) quand le ciel porte le motif eps à l'orientation R0."""

    def __init__(self, stat4: Statistique, lots: list[Lot]):
        C = stat4.C
        G = (5 * C - 3 * coefficients_unite(stat4.idx)) / 2          # g(R0 n) = (5 Q - 3)/2
        self.lots = []
        for lot in lots:
            v, w = lot.quadrature()
            M = monomes(v, stat4.idx)
            mu = w @ M
            K = (M * w[:, None]).T @ M
            L = np.stack([(M * (w * M[:, a])[:, None]).T @ M for a in range(M.shape[1])])
            LG = np.einsum('abc,rc->rab', L, G)
            self.lots.append({
                'N': len(lot.n), 'a': C @ mu, 's': G @ mu,
                'b': np.einsum('ra,ab,rb->r', C, K, G), 'q': np.einsum('ra,ab,rb->r', C, K, C),
                't': np.einsum('rab,ra,rb->r', LG, C, C)})
        self.sd2 = sum(d['N'] * (d['q'] - d['a'] ** 2) for d in self.lots)

    def moments(self, eps, sel=slice(None)):
        m = v = 0.0
        for d in self.lots:
            den = 1 + eps * d['s'][sel]
            e1 = (d['a'][sel] + eps * d['b'][sel]) / den
            e2 = (d['q'][sel] + eps * d['t'][sel]) / den
            m = m + d['N'] * (e1 - d['a'][sel])
            v = v + d['N'] * (e2 - e1 ** 2)
        return m / np.sqrt(self.sd2[sel]), v / self.sd2[sel]

    def puissance(self, eps, z, sel=slice(None)):
        m, v = self.moments(eps, sel)
        s = np.sqrt(v)
        return _phi((m - z) / s) + _phi((-m - z) / s)

    def bornes(self, z: float, signe: int) -> np.ndarray:
        """Pour chaque orientation, plus petite |eps| telle que P(|T(R0)| > z) >= 0,95 (nan : aucune)."""
        grille = np.linspace(0.0, 1.5 if signe > 0 else 1.0, 301)
        res = np.full(len(self.sd2), np.nan)
        prec = self.puissance(0.0, z) * np.ones(len(self.sd2))
        for a0, a1 in zip(grille[:-1], grille[1:]):
            p = self.puissance(signe * a1, z)
            neuf = np.isnan(res) & (p >= 0.95)
            res[neuf] = a0 + (0.95 - prec[neuf]) * (a1 - a0) / (p[neuf] - prec[neuf])
            prec = p
        return res


def resume_bornes(b: np.ndarray) -> dict:
    ok = b[~np.isnan(b)]
    return {'pire': None if len(ok) < len(b) else float(np.max(b)),
            'orientations_sans_borne': int(np.sum(np.isnan(b))),
            'mediane': float(np.median(ok)), 'quantile_95': float(np.quantile(ok, 0.95)),
            'meilleure': float(np.min(ok)), 'indice_pire': int(np.nanargmax(b))}


# ================================================================ diagnostics
def angle_modulo_cube(R1: np.ndarray, R2: np.ndarray) -> float:
    """Plus petit angle (degrés) entre deux orientations de grille, au groupe du cube près."""
    meilleur = 180.0
    for perm in itertools.permutations(range(3)):
        for signes in itertools.product((1, -1), repeat=3):
            G = np.zeros((3, 3))
            for i, j in enumerate(perm):
                G[i, j] = signes[i]
            c = (np.trace((G @ R1) @ R2.T) - 1) / 2
            meilleur = min(meilleur, math.degrees(math.acos(max(-1.0, min(1.0, c)))))
    return meilleur


def cones(lots: list[Lot], R: np.ndarray, rayon: float) -> dict:
    """Observé et attendu (isotropie) dans des cônes autour des 6 axes et des 8 diagonales de R."""
    axes = [s * R[k] for k in range(3) for s in (1, -1)]
    diags = [np.array(s) @ R / math.sqrt(3) for s in itertools.product((1, -1), repeat=3)]
    c = math.cos(math.radians(rayon))
    n = np.concatenate([l.n for l in lots])
    quads = [(len(l.n), *l.quadrature(600, 1080)) for l in lots]
    out = {}
    for nom, dirs in (('axes', axes), ('diagonales', diags)):
        rows = []
        for u in dirs:
            obs = int(np.sum(n @ u >= c))
            att = float(sum(N * np.sum(w[v @ u >= c]) for N, v, w in quads))
            rows.append({'ra_deg': math.degrees(math.atan2(u[1], u[0])) % 360,
                         'dec_deg': math.degrees(math.asin(max(-1.0, min(1.0, u[2])))),
                         'observe': obs, 'attendu': att, 'rapport': obs / att if att > 0 else None,
                         'distance_centaurus_a_deg': math.degrees(math.acos(float(np.clip(
                             u @ vecteur_deg(*CENTAURUS_A[:2]), -1, 1)))),
                         'distance_point_chaud_ta_deg': math.degrees(math.acos(float(np.clip(
                             u @ vecteur_deg(*POINT_CHAUD_TA[:2]), -1, 1))))})
        o = sum(r['observe'] for r in rows)
        a = sum(r['attendu'] for r in rows)
        out[nom] = {'cones': rows, 'observe_total': o, 'attendu_total': a, 'rapport_total': o / a,
                    'n_cones_en_exces': sum(r['observe'] > r['attendu'] for r in rows),
                    'chi2_isotropie': sum((r['observe'] - r['attendu']) ** 2 / r['attendu']
                                          for r in rows if r['attendu'] > 0),
                    'ddl': sum(r['attendu'] > 0 for r in rows)}
    return out


# ================================================================ lots
def lots_auger(aug, seuil, masques=(), un_bloc=False) -> list[Lot]:
    s = aug['E'] >= seuil
    n = vecteurs(np.radians(aug['ra'][s]), np.radians(aug['dec'][s]))
    th = aug['theta'][s]
    if un_bloc:
        return [Lot('Auger (zénith <= 80°)', LAT_AUGER, 0.0, ZEN_INCLINE, n, masques)]
    return [Lot('Auger vertical', LAT_AUGER, 0.0, ZEN_VERTICAL, n[th < ZEN_VERTICAL], masques),
            Lot('Auger incliné', LAT_AUGER, ZEN_VERTICAL, ZEN_INCLINE, n[th >= ZEN_VERTICAL], masques)]


def lot_ta(ta, seuil=SEUIL_TA, amaterasu=None, masques=()) -> Lot:
    ev = [e for e in ta if e[2] >= seuil]
    ra = np.radians([e[3] for e in ev])
    dec = np.radians([e[4] for e in ev])
    if amaterasu is not None:
        ra = np.append(ra, math.radians(amaterasu['ra']))
        dec = np.append(dec, math.radians(amaterasu['dec']))
    return Lot('Telescope Array', LAT_TA, 0.0, ZEN_TA, vecteurs(ra, dec), masques)


def description_lots(lots) -> list[dict]:
    return [{'nom': l.nom, 'latitude_deg': l.latitude, 'zenith_deg': list(l.zen), 'n': int(len(l.n))}
            for l in lots]


# ================================================================ autotests
def autotests(rng, E, alpha6, aug, ta, amat, lots, stats, borne) -> dict:
    s4, s6 = stats
    # 1. Données : effectifs et bornes publiés.
    assert len(aug['E']) == 2635 and int(np.sum(aug['theta'] < 60)) == 2040        # arXiv:2206.13492 p. 3
    assert aug['E'].min() >= 32.0 and aug['theta'].max() <= 80.0 and aug['dec'].max() <= 44.8
    assert len(ta) == 72 and min(e[2] for e in ta) > 57.0 and max(e[1] for e in ta) < 55.0
    assert ta[0][0][:3] == (2008, 6, 10) and ta[-1][0][:3] == (2013, 4, 28)
    assert min(e[4] for e in ta) >= LAT_TA - ZEN_TA
    assert abs(amat['E_EeV'] - 243.611) < 1e-9 and amat['date'] == '20210527'
    # 2. Étalonnages : correspondances imprimées dans les sources.
    et = ETALONNAGES
    # (alpha et beta sont publiés arrondis : on tolère 0,01 EeV sur les valeurs à deux décimales)
    assert round(e_ta(32, et['principal']), 1) == 40.0                              # arXiv:2507.10441 p. 3
    assert abs(e_auger(10, et['icrc2025_strict']) - 8.60) < 0.01
    assert round(e_ta(16, et['icrc2025_strict']), 1) == 19.1 and round(e_ta(32, et['icrc2025_strict']), 1) == 39.2
    assert round(e_ta(32, et['uhecr2022']), 1) == 40.5 and abs(e_auger(10, et['uhecr2022']) - 8.53) < 0.01
    for a, t in ((32, 40.8), (38, 49.0), (41, 53.1), (59, 78.4)):                   # arXiv:2111.12366
        assert abs(e_ta(a, et['icrc2021']) - t) < 0.06
    assert abs(e_ta(80, et['icrc2021']) - 108.6) < 0.15
    # 3. Q invariante sous le groupe du cube ; monômes exacts ; l = 6 orthogonal à l = 4.
    v = rng.normal(size=(50, 3))
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    for perm in itertools.permutations(range(3)):
        assert np.allclose(Q(v[:, perm] * np.array([1, -1, 1])), Q(v))
    M4, M6 = monomes(v, s4.idx), monomes(v, s6.idx)
    for r in range(3):
        assert np.allclose(M4 @ s4.C[r], Q(v @ E[r].T), atol=1e-12)
    assert np.allclose(M6 @ s6.C[0], np.sum((v @ E[0].T) ** 6, axis=1) + alpha6 * Q(v @ E[0].T), atol=1e-12)
    assert np.allclose(M4 @ coefficients_unite(s4.idx), 1.0)
    assert abs(alpha6 + 15 / 11) < 1e-9
    # 4. Expositions : bornes du ciel visible, bande inclinée, pôles, somme des bandes.
    aug_v, aug_i, lta = lots
    d = np.radians(np.array([-90.0, 24.7, 24.9, 44.7, 44.9, 90.0]))
    assert aug_v.omega(d)[2] == 0.0 and aug_v.omega(d)[1] > 0                      # -35,2 + 60 = 24,8°
    assert aug_i.omega(d)[4] == 0.0 and aug_i.omega(d)[3] > 0                      # -35,2 + 80 = 44,8°
    assert abs(aug_i.omega(d)[0]) < 1e-12                          # pôle sud : zénith 54,8°, toujours vertical
    assert lta.omega(np.radians(np.array([-15.8])))[0] == 0.0 and lta.omega(d)[5] > 0   # 39,3 - 55 = -15,7°
    tot = Lot('t', LAT_AUGER, 0.0, 80.0, aug_v.n)
    g = np.radians(np.linspace(-89, 44, 300))
    assert np.allclose(aug_v.omega(g) + aug_i.omega(g), tot.omega(g), atol=1e-12)
    # 5. Quadrature et grands tirages concordent, lot par lot (et avec les masques).
    masque = Lot('m', LAT_AUGER, 0.0, 80.0, aug_v.n, (CENTAURUS_A, POINT_CHAUD_TA))
    for lot in [*lots, masque]:
        grand = lot.tirer(rng, 300_000)
        vq, wq = lot.quadrature()
        for f in (Q, lambda u: u[..., 2], lambda u: u[..., 0] * u[..., 1]):
            assert abs(np.mean(f(grand)) - float(np.sum(wq * f(vq)))) < 5 * np.std(f(grand)) / math.sqrt(3e5), lot.nom
    assert not np.any(~masque.hors_masques(masque.tirer(rng, 10_000)))
    # 6. Sous isotropie, T(R) à orientation fixée est centré réduit.
    t = T_simules(rng, lots, s4, 3000, slice(0, 5))
    assert np.all(np.abs(t.mean(axis=1)) < 0.08) and np.all(np.abs(t.std(axis=1) - 1) < 0.06)
    # 7. Moyenne et variance analytiques de T(R0) sous un signal = Monte-Carlo.
    k0 = 123
    ecarts = {}
    for eps0 in (0.3, -0.3):
        t0 = T_simules(rng, lots, s4, 3000, slice(k0, k0 + 1), poids_signal(eps0, E[k0]))[0]
        m_an, v_an = borne.moments(eps0, slice(k0, k0 + 1))
        assert abs(t0.mean() - m_an[0]) < 4 * t0.std() / math.sqrt(3000), (eps0, t0.mean(), m_an)
        assert abs(t0.var() / v_an[0] - 1) < 0.1, (eps0, t0.var(), v_an)
        ecarts[str(eps0)] = {'moyenne_MC': float(t0.mean()), 'moyenne_analytique': float(m_an[0]),
                             'variance_MC': float(t0.var()), 'variance_analytique': float(v_an[0])}
    # 8. Un motif cubique franc est détecté et son orientation retrouvée, sur tout le ciel.
    R0 = rotations(rng, 1)[0]
    grands = [Lot(l.nom, l.latitude, *l.zen, l.n[:1]) for l in lots]
    for l, m in zip(grands, (1200, 400, 400)):
        l.n = l.tirer(rng, m, poids_signal(1.0, R0))
    s4g = Statistique(E, 4, grands)
    T4 = s4g.T(sommes_monomes(np.concatenate([l.n for l in grands])[None], [s4g.idx])[0])[:, 0]
    ecart = angle_modulo_cube(E[int(np.argmax(np.abs(T4)))], R0)
    assert np.max(np.abs(T4)) > 8 and ecart < 10, (np.max(np.abs(T4)), ecart)
    return {'orientation_retrouvee_ecart_deg': ecart, 'alpha_l6': alpha6, 'borne_contre_MC': ecarts}


# ================================================================ calcul
def analyser(rng, E, alpha6, lots, n_ciels) -> dict:
    stats = statistiques(E, lots, alpha6)
    obs = observer(stats, lots)
    nuls = simuler_nul(rng, lots, stats, n_ciels)
    b = BorneAnalytique(stats[0], lots)
    return {'lots': description_lots(lots), 'n_evenements': int(sum(len(l.n) for l in lots)),
            'Z4_observe': obs['Z4'], 'p_valeur_l4': p_valeur(nuls[0], obs['Z4']),
            'Z6_observe': obs['Z6'], 'p_valeur_l6': p_valeur(nuls[1], obs['Z6']),
            'Z46_observe': obs['Z46'], 'p_valeur_l4_l6': p_valeur(nuls[2], obs['Z46']),
            'ciels_isotropes': n_ciels,
            'borne_toutes_orientations': {'axes': resume_bornes(b.bornes(obs['Z4'], 1)),
                                          'diagonales': resume_bornes(b.bornes(obs['Z4'], -1))}}


def calculer() -> dict:
    t_debut = time.time()
    rng = np.random.default_rng(GRAINE)
    E = rotations(rng, N_ORIENTATIONS)                  # mêmes orientations qu'au test n° 2
    alpha6 = coefficient_l6()
    aug = lire_auger()
    ta, source_ta = lire_ta()
    amat = lire_amaterasu()
    print(f'Telescope Array : {source_ta}')

    etal = ETALONNAGES['principal']
    seuil = e_auger(SEUIL_TA, etal)
    lots = lots_auger(aug, seuil) + [lot_ta(ta)]
    stats = statistiques(E, lots, alpha6)
    borne = BorneAnalytique(stats[0], lots)
    tests = autotests(rng, E, alpha6, aug, ta, amat, lots, stats, borne)
    print(f'autotests OK ({time.time() - t_debut:.0f} s)')

    # ---------------------------------------------------------------- test principal
    obs = observer(stats, lots)
    n = obs['n']
    N = len(n)
    nuls = simuler_nul(rng, lots, stats, N_CIELS)
    p = [p_valeur(nuls[i], obs[k]) for i, k in enumerate(('Z4', 'Z6', 'Z46'))]
    ib = int(np.argmax(np.abs(obs['T4'])))
    Rb = E[ib]
    q_obs = float(np.mean(Q(n @ Rb.T)))
    q_iso = float(sum(len(l.n) * np.sum(l.quadrature()[1] * Q(l.quadrature()[0] @ Rb.T)) for l in lots) / N)
    T4_lots = {}
    for l in lots:
        s = Statistique(E[ib:ib + 1], 4, [l])
        T4_lots[l.nom] = float(s.T(sommes_monomes(l.n[None], [s.idx])[0])[0, 0])
    print(f'test principal : N = {N}, Z4 = {obs["Z4"]:.3f}, p = {p[0]:.4f} ({time.time() - t_debut:.0f} s)')

    # ---------------------------------------------------------------- limites
    b_axes = borne.bornes(obs['Z4'], 1)
    b_diag = borne.bornes(obs['Z4'], -1)
    courbe = []
    for signe in (1, -1):
        for a in AMPLITUDES:
            z4 = z4_signal_aleatoire(rng, lots, stats[0], signe * a, N_CIELS_SIGNAL)
            courbe.append({'epsilon': signe * a, 'fraction_Z4_superieur_obs': float(np.mean(z4 > obs['Z4'])),
                           'Z4_median': float(np.median(z4))})
    moy = {s: croisement_95([(abs(c['epsilon']), c['fraction_Z4_superieur_obs']) for c in courbe
                             if math.copysign(1, c['epsilon']) == s] + [(0.0, p[0])]) for s in (1, -1)}
    print(f'limite moyenne : {moy} ({time.time() - t_debut:.0f} s)')

    speciales = list(dict.fromkeys([int(np.argmin(stats[0].sd)), int(np.nanargmax(b_axes)),
                                    int(np.nanargmax(b_diag))]))
    autres = [int(k) for k in rng.choice(len(E), N_ORIENT_FIXES + 3, replace=False) if int(k) not in speciales]
    fixes = speciales + autres[:N_ORIENT_FIXES - len(speciales)]
    roles = {speciales[0]: 'la moins visible'}
    roles.setdefault(int(np.nanargmax(b_axes)), 'pire borne analytique (axes)')
    roles.setdefault(int(np.nanargmax(b_diag)), 'pire borne analytique (diagonales)')
    par_orientation = []
    for k in fixes:
        lim = {}
        for signe, b in ((1, b_axes[k]), (-1, b_diag[k])):
            pts = []
            for f in FACTEURS_FIXES:
                a = min(1.5 if signe > 0 else 1.0, f * b)
                z4 = z4_signal_fixe(rng, lots, stats[0], signe * a, E[k], N_CIELS_FIXES)
                pts.append((float(a), float(np.mean(z4 > obs['Z4']))))
            lim[signe] = (croisement_95(pts), pts)
        par_orientation.append({
            'indice': k, 'role': roles.get(k, 'tirée au hasard'),
            'ecart_type_Q_par_evenement': float(stats[0].sd[k] / math.sqrt(N)),
            'epsilon_axes_max': lim[1][0], 'borne_analytique_axes': float(b_axes[k]),
            'epsilon_diagonales_max': lim[-1][0], 'borne_analytique_diagonales': float(b_diag[k]),
            'points_axes': lim[1][1], 'points_diagonales': lim[-1][1]})
    print(f'orientations fixes ({time.time() - t_debut:.0f} s)')

    def pire(cle):
        vals = [x[cle] for x in par_orientation]
        return None if any(v is None for v in vals) else max(vals)

    # Même borne analytique pour la configuration du test n° 2 (100 événements Auger, un bloc).
    t2 = json.loads(TEST2.read_text(encoding='utf-8'))
    lot2 = Lot('Auger, test n° 2', LAT_AUGER, 0.0, ZEN_INCLINE, np.zeros((t2['donnees']['n_evenements'], 3)))
    b2 = BorneAnalytique(Statistique(E, 4, [lot2]), [lot2])
    z2 = t2['resultats']['Z4_observe']
    l2 = t2['limite_superieure_95']
    test2 = {'Z4_observe': z2, 'p_valeur_l4': t2['resultats']['p_valeur_l4'],
             'n_evenements': t2['donnees']['n_evenements'],
             'fraction_du_ciel_visible': t2['methode']['fraction_du_ciel_visible'],
             'limite_moyenne_axes': l2['epsilon_axes_max'], 'limite_moyenne_diagonales': l2['epsilon_diagonales_max'],
             'pire_16_orientations_axes': l2['pire_orientation_epsilon_axes_max'],
             'pire_16_orientations_diagonales': l2['pire_orientation_epsilon_diagonales_max'],
             'borne_toutes_orientations': {'axes': resume_bornes(b2.bornes(z2, 1)),
                                           'diagonales': resume_bornes(b2.bornes(z2, -1))}}
    print(f'comparaison au test n° 2 ({time.time() - t_debut:.0f} s)')

    # ---------------------------------------------------------------- variantes
    variantes = {}

    def variante(cle, desc, lv):
        variantes[cle] = {'description': desc, **analyser(rng, E, alpha6, lv, N_CIELS_VARIANTE)}
        v = variantes[cle]
        print(f'variante {cle} : N = {v["n_evenements"]}, Z4 = {v["Z4_observe"]:.3f}, p = {v["p_valeur_l4"]:.4f} '
              f'({time.time() - t_debut:.0f} s)')

    variante('auger_seul', 'Auger seul, même seuil (44,9 EeV) : ce que TA ajoute', lots_auger(aug, seuil))
    s78 = 78.0
    variante('hautes_energies', f'plus hautes énergies : Auger >= 78 EeV (seuil du test n° 2) et TA >= '
             f'{e_ta(s78, etal):.1f} EeV', lots_auger(aug, s78) + [lot_ta(ta, e_ta(s78, etal))])
    variante('n_maximal', 'N maximal : tous les événements Auger (>= 32 EeV) et TA (> 57 EeV), seuils non équivalents',
             lots_auger(aug, 32.0) + [lot_ta(ta)])
    for cle in ('icrc2021', 'icrc2025_strict'):
        s = e_auger(SEUIL_TA, ETALONNAGES[cle])
        variante(f'etalonnage_{cle}', f'étalonnage {cle} : seuil Auger {s:.2f} EeV', lots_auger(aug, s) + [lot_ta(ta)])
    variante('sans_correction', 'aucune correction d’échelle : Auger >= 57 EeV', lots_auger(aug, 57.0) + [lot_ta(ta)])
    variante('auger_un_bloc', 'exposition Auger d’un seul bloc (zénith <= 80°), comme au test n° 2',
             lots_auger(aug, seuil, un_bloc=True) + [lot_ta(ta)])
    variante('avec_amaterasu', 'TA + événement Amaterasu (27 mai 2021, 244 EeV)',
             lots_auger(aug, seuil) + [lot_ta(ta, amaterasu=amat)])
    masques = (CENTAURUS_A, POINT_CHAUD_TA)
    variante('exces_masques', 'Centaurus A (27°) et point chaud TA (20°) retirés du ciel et des données',
             lots_auger(aug, seuil, masques) + [lot_ta(ta, masques=masques)])
    # Ajoutées après coup (la variante « N maximal » donnait p < 0,01) : d'où vient ce signal ?
    # Placées en dernier, elles ne changent aucun des tirages précédents.
    variante('n_maximal_auger_seul', 'N maximal, Auger seul (>= 32 EeV) : le signal vient-il du sud ?',
             lots_auger(aug, 32.0))
    variante('n_maximal_exces_masques', 'N maximal, Centaurus A (27°) et point chaud TA (20°) retirés',
             lots_auger(aug, 32.0, masques) + [lot_ta(ta, masques=masques)])
    bas = {k: v[aug['E'] < seuil] for k, v in aug.items()}
    variante('auger_32_a_seuil', f'Auger seul, 32 à {seuil:.2f} EeV : événements absents de l’échantillon principal',
             lots_auger(bas, 32.0))
    variante('auger_32_a_seuil_exces_masques', 'Auger seul, 32 à 44,88 EeV, Centaurus A et point chaud TA retirés',
             lots_auger(bas, 32.0, masques))

    # ---------------------------------------------------------------- après coup : reproduction et dipôle
    reproduction = {'note': 'analyses ajoutées après avoir vu la variante « N maximal » ; elles ne changent '
                            'ni le test principal ni son verdict'}
    for cle, lb, lh in (('sans_masque', lots_auger(bas, 32.0), lots),
                        ('exces_masques', lots_auger(bas, 32.0, masques),
                         lots_auger(aug, seuil, masques) + [lot_ta(ta, masques=masques)])):
        sb, sh = Statistique(E, 4, lb), Statistique(E, 4, lh)
        tb = sb.T(sommes_monomes(np.concatenate([l.n for l in lb])[None], [sb.idx])[0])[:, 0]
        th = sh.T(sommes_monomes(np.concatenate([l.n for l in lh])[None], [sh.idx])[0])[:, 0]
        k = int(np.argmax(np.abs(tb)))
        reproduction[cle] = {
            'orientation_choisie_sur': 'Auger 32 à 44,88 EeV', 'indice': k, 'T4_choix': float(tb[k]),
            'T4_echantillon_principal_meme_orientation': float(th[k]),
            'p_bilaterale_normale': float(2 * (1 - _phi(np.array([abs(th[k])]))[0])),
            'ecart_a_la_meilleure_orientation_principale_deg': angle_modulo_cube(E[k], E[int(np.argmax(np.abs(th)))])}

    def dipole(lv):
        """Dipôle d ajusté par les moments : moyenne de n sous omega_d (1 + d.n) = moyenne observée."""
        S, d = sum(l.n.sum(axis=0) for l in lv), np.zeros(3)
        for _ in range(100):
            F, J = np.zeros(3), np.zeros((3, 3))
            for l in lv:
                v, w = l.quadrature()
                W = w * (1 + v @ d)
                m = W @ v / W.sum()
                F += len(l.n) * m
                J += len(l.n) * (((v * w[:, None]).T @ v) - np.outer(m, w @ v)) / W.sum()
            d = d + np.linalg.solve(J, S - F)
        return d

    nul_dipolaire = {'note': 'ciels simulés avec le dipôle ajusté sur les données (et non isotropes) : '
                             'une anisotropie à grande échelle explique-t-elle Z4 ?'}
    for cle, lv in (('principal', lots), ('n_maximal', lots_auger(aug, 32.0) + [lot_ta(ta)])):
        d = dipole(lv)
        a = float(np.linalg.norm(d))
        s4 = Statistique(E, 4, lv)
        z_obs = float(np.max(np.abs(s4.T(sommes_monomes(np.concatenate([l.n for l in lv])[None], [s4.idx])[0]))))
        w = (lambda v, d=d, a=a: (1 + v @ d) / (1 + a))
        z = np.concatenate([np.max(np.abs(s4.T(sommes_monomes(_ciels(rng, lv, 100, w), [s4.idx])[0])), axis=0)
                            for _ in range(N_CIELS_VARIANTE // 100)])
        nul_dipolaire[cle] = {'amplitude': a, 'ra_deg': math.degrees(math.atan2(d[1], d[0])) % 360,
                              'dec_deg': math.degrees(math.asin(d[2] / a)), 'Z4_observe': z_obs,
                              'p_valeur_l4_sous_dipole': p_valeur(z, z_obs), 'ciels': len(z)}
    print(f'reproduction et dipôle ({time.time() - t_debut:.0f} s)')

    pire_axes, pire_diag = float(np.nanmax(b_axes)), float(np.nanmax(b_diag))
    t2b = test2['borne_toutes_orientations']
    return {
        'titre': 'Test n° 6 : symétrie cubique des rayons cosmiques sur tout le ciel (Auger + Telescope Array)',
        'date': '2026-09-28',
        'prediction': 'Beane, Davoudi, Savage, arXiv:1210.1847 : brisure de la symétrie de rotation '
                      'reflétant la grille, dans les directions des rayons cosmiques les plus énergétiques',
        'donnees': {
            'auger': {'source': 'Pierre Auger Collaboration, ApJ 935, 170 (2022), arXiv:2206.13492 ; '
                                'DOI 10.5281/zenodo.6504276 (version 10.5281/zenodo.6759610), CC BY-SA 4.0',
                      'fichier': f'donnees/{AUGER.name}', 'sha256': SHA_AUGER,
                      'n_liste': int(len(aug['E'])), 'n_verticaux_liste': int(np.sum(aug['theta'] < 60)),
                      'energie_min_liste_EeV': float(aug['E'].min()), 'energie_max_EeV': float(aug['E'].max()),
                      'periode': '2004-01-01 / 2020-12-31', 'declinaison_max_deg': float(aug['dec'].max())},
            'telescope_array': {'source': 'Telescope Array Collaboration, ApJL 790, L21 (2014), tableau 1, '
                                          'arXiv:1404.5890v3 ; © AAS, non redistribué',
                                'url_table': TA_MRT_URL, 'sha256_table': SHA_TA_MRT,
                                'url_secours': TA_TEX_URL, 'sha256_ms_tex': SHA_TA_TEX,
                                'sha256_liste': SHA_TA_LISTE, 'n': len(ta),
                                'energie_min_EeV': min(e[2] for e in ta), 'energie_max_EeV': max(e[2] for e in ta),
                                'declinaison_min_deg': min(e[4] for e in ta),
                                'periode': '2008-05-11 / 2013-05-04'},
            'amaterasu': {'source': 'Telescope Array Collaboration, Science 382, 903 (2023), arXiv:2311.14231 ; '
                                    'DOI 10.5281/zenodo.8427755, CC BY 4.0', 'fichier': f'donnees/{AMATERASU.name}',
                          'sha256': SHA_AMATERASU, **amat},
        },
        'etalonnage': {'formule': 'E_Auger / 10 EeV = exp(alpha) (E_TA / 10 EeV)^beta', **ETALONNAGES,
                       'seuil_TA_EeV': SEUIL_TA, 'seuil_Auger_equivalent_EeV': seuil,
                       'seuils_Auger_selon_etalonnage_EeV': {k: e_auger(SEUIL_TA, v) for k, v in ETALONNAGES.items()},
                       'seuil_TA_equivalent_a_78_EeV_Auger': e_ta(78.0, etal)},
        'methode': {
            'lots': description_lots(lots),
            'exposition': 'Sommers 2001, efficacité totale : Auger latitude -35,2°, verticaux zénith < 60°, '
                          'inclinés 60°-80° ; TA latitude 39,30°, zénith < 55°',
            'declinaison_max_Auger_deg': LAT_AUGER + ZEN_INCLINE,
            'declinaison_min_TA_deg': LAT_TA - ZEN_TA,
            'fraction_du_ciel_visible': 1.0,
            'fraction_du_ciel_vue_par_les_deux': (math.sin(math.radians(LAT_AUGER + ZEN_INCLINE))
                                                  - math.sin(math.radians(LAT_TA - ZEN_TA))) / 2,
            'fraction_du_ciel_vue_par_TA_seul': (1 - math.sin(math.radians(LAT_AUGER + ZEN_INCLINE))) / 2,
            'fonction_l4': 'Q(Rn) = somme (R n)_k^4',
            'fonction_l6_alpha': alpha6,
            'orientations': N_ORIENTATIONS, 'ciels_isotropes': N_CIELS, 'ciels_par_variante': N_CIELS_VARIANTE,
            'ciels_par_amplitude': N_CIELS_SIGNAL, 'ciels_par_amplitude_orientation_fixe': N_CIELS_FIXES,
            'graine': GRAINE, 'test_principal': 'l = 4, Z4 = max_R |T4(R)|', 'rayon_cones_deg': RAYON_CONES,
        },
        'resultats': {
            'n_evenements': N, 'n_auger': int(sum(len(l.n) for l in lots[:2])), 'n_ta': int(len(lots[2].n)),
            'n_auger_verticaux': int(len(lots[0].n)), 'n_auger_inclines': int(len(lots[1].n)),
            'Z4_observe': obs['Z4'], 'p_valeur_l4': p[0],
            'Z6_observe': obs['Z6'], 'p_valeur_l6': p[1],
            'Z46_observe': obs['Z46'], 'p_valeur_l4_l6': p[2],
            'seuils_Z4_isotrope': {q: float(np.quantile(nuls[0], q)) for q in (0.5, 0.95, 0.99, 0.999)},
            'meilleure_orientation_indice': ib,
            'meilleure_orientation_T4': float(obs['T4'][ib]),
            'meilleure_orientation_matrice': Rb.round(6).tolist(),
            'meilleure_orientation_ecart_au_test2_deg': angle_modulo_cube(
                Rb, np.array(t2['resultats']['meilleure_orientation_matrice'])),
            'T4_par_lot_meilleure_orientation': T4_lots,
            'Q_moyen_observe': q_obs, 'Q_moyen_attendu_isotrope': q_iso,
            'ecart_relatif_Q': (q_obs - q_iso) / q_iso,
            'cones_meilleure_orientation': cones(lots, Rb, RAYON_CONES),
        },
        'limite_superieure_95': {
            'definition': 'densité relative 1 + eps (5 Q - 3) / 2 ; eps = excès relatif le long des axes '
                          '(eps < 0 : excès 2|eps|/3 le long des diagonales)',
            'moyenne_orientations': {'epsilon_axes_max': moy[1], 'epsilon_diagonales_max': moy[-1],
                                     'exces_diagonales_max': None if moy[-1] is None else 2 / 3 * moy[-1],
                                     'courbe': courbe},
            'par_orientation_fixe': par_orientation,
            'pire_orientation_fixe_epsilon_axes_max': pire('epsilon_axes_max'),
            'pire_orientation_fixe_epsilon_diagonales_max': pire('epsilon_diagonales_max'),
            'toutes_orientations_borne_analytique': {
                'axes': resume_bornes(b_axes), 'diagonales': resume_bornes(b_diag),
                'exces_axes_max': pire_axes, 'exces_diagonales_max': 2 / 3 * pire_diag,
                'note': 'Z4 >= |T(R0)| ; approximation normale et balayage fini des orientations/amplitudes. Moments calculés par quadrature ; couverture uniforme non certifiée.'},
        },
        'test2_meme_methode': test2,
        'comparaison': {
            'rapport_N': N / test2['n_evenements'],
            'gain_limite_moyenne_axes': test2['limite_moyenne_axes'] / moy[1] if moy[1] else None,
            'gain_limite_moyenne_diagonales': test2['limite_moyenne_diagonales'] / moy[-1] if moy[-1] else None,
            'gain_pire_orientation_axes': t2b['axes']['pire'] / pire_axes if t2b['axes']['pire'] else None,
            'gain_pire_orientation_diagonales': (t2b['diagonales']['pire'] / pire_diag
                                                 if t2b['diagonales']['pire'] else None),
        },
        'variantes': variantes,
        'apres_coup': {'reproduction_par_energie': reproduction, 'nul_dipolaire': nul_dipolaire},
        'autotests': {'etat': 'OK', **tests},
    }


def resume(r: dict) -> str:
    x = r['resultats']
    l = r['limite_superieure_95']
    b = l['toutes_orientations_borne_analytique']
    m = l['moyenne_orientations']
    f = lambda v: 'aucune' if v is None else f'{v:.3f}'          # noqa: E731
    return (f"{x['n_evenements']} événements ({x['n_auger']} Auger, {x['n_ta']} TA)\n"
            f"l=4 : Z = {x['Z4_observe']:.2f}, p = {x['p_valeur_l4']:.4f}\n"
            f"l=6 : Z = {x['Z6_observe']:.2f}, p = {x['p_valeur_l6']:.4f}\n"
            f"l=4+6 : Z² = {x['Z46_observe']:.2f}, p = {x['p_valeur_l4_l6']:.4f}\n"
            f"limite 95 % (moyenne) : eps(axes) < {f(m['epsilon_axes_max'])}, "
            f"|eps(diag)| < {f(m['epsilon_diagonales_max'])}\n"
            f"limite 95 % (16 orientations fixes, pire) : eps(axes) < {f(l['pire_orientation_fixe_epsilon_axes_max'])}, "
            f"|eps(diag)| < {f(l['pire_orientation_fixe_epsilon_diagonales_max'])}\n"
            f"limite 95 % (toutes orientations, borne) : eps(axes) < {f(b['axes']['pire'])}, "
            f"|eps(diag)| < {f(b['diagonales']['pire'])}\n"
            + ''.join(f"variante {k} : N = {v['n_evenements']}, Z4 = {v['Z4_observe']:.2f}, p = {v['p_valeur_l4']:.4f}\n"
                      for k, v in r['variantes'].items()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, default=ICI / 'resultats.json')
    args = parser.parse_args()
    t0 = time.time()
    resultat = calculer()
    args.out.write_text(json.dumps(resultat, ensure_ascii=False, indent=2), encoding='utf-8')
    print(resume(resultat))
    print(f'durée : {time.time() - t0:.0f} s')
