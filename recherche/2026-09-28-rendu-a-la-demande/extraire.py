#!/usr/bin/env python3
"""aeternam, test n° 5 : relevé des mesures publiées dans les figures vectorielles.

Les figures utilisées sont des dessins vectoriels dans les PDF arXiv : chaque
point de mesure y est un objet (cercle, losange, croix…) dont les coordonnées
sont lisibles exactement, à la précision du tracé (0,1 à 0,25 pt). Ce script
télécharge les PDF (versions arXiv figées), vérifie leur SHA-256, repère les
graduations des axes, les étalonne sur les valeurs imprimées, puis convertit
chaque marqueur (et ses barres d'erreur) en valeurs physiques. Il écrit
donnees/figures.json, que lit analyse.py.

Figures relevées :
  walborn2002   quant-ph/0106078v1, fig. 2 à 9 (p. 8 à 15) : coïncidences en
                fonction de la position du détecteur Ds, avec barres d'erreur.
  kim2000       quant-ph/9903047v1, fig. 3 à 5 (p. 4) : coïncidences R01, R02, R03.
  schwindt1999  quant-ph/9908072v1, fig. 2 (p. 3) : visibilité V, connaissance K
                (base optimisée et base H/V) et V² + K², avec barres d'erreur.
  hornberger2003 quant-ph/0303093v1, fig. 2 (p. 3) : visibilité en fonction de la
                pression de méthane (échelle log) et droite théorique ; fig. 3 : pression de
                décohérence p0 mesurée et calculée pour dix gaz.
  hackermuller2004 quant-ph/0402146v1, fig. 4 (p. 4) : visibilité normalisée en
                fonction de la puissance de chauffage, panneaux a et b, et les deux
                courbes théoriques (trait plein).

Contrôles faits ici (le script s'arrête s'ils échouent) : régularité des
graduations (écart à la droite d'étalonnage), nombre de points attendu, centre
des barres d'erreur confondu avec le marqueur, et pour les comptages de Walborn
et al. : valeurs proches d'entiers et barres d'erreur égales à √N (loi de
Poisson), ce qui valide l'étalonnage.

Nécessite PyMuPDF (pip install pymupdf) et un accès à arxiv.org ; analyse.py
n'en a pas besoin. Usage : python3 extraire.py [--cache DOSSIER]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import tempfile
import time
import urllib.request
from pathlib import Path

import pymupdf

ICI = Path(__file__).resolve().parent
SORTIE = ICI / 'donnees' / 'figures.json'

PDF = {
    'walborn2002': ('quant-ph/0106078v1', '33bb3bd7f17d8ad7fdb24c5ad2ad6e34e3dd8fd4a7bdb01468696061ee554ce5'),
    'kim2000': ('quant-ph/9903047v1', '164a96a6c4cc49310748ad26a969ac5fae398c47cab254fbbbff444c38bee1d5'),
    'schwindt1999': ('quant-ph/9908072v1', '9e6d5453ca61705d5484dc6b441ee9dc8a64e501029c61335b19e4d09ebf3d90'),
    'hornberger2003': ('quant-ph/0303093v1', '06d3ae4ad0af56fc114d65e532eb453be9dc59eb19c127d6643471e4466c6de5'),
    'hackermuller2004': ('quant-ph/0402146v1', 'f1f38ac71b1a03102e1b09937eab5f855e0cd5b6a02ace2f5bb83d2a8c217a24'),
}


# =================================================================== outils
def telecharger(cle: str, cache: Path) -> pymupdf.Document:
    ident, sha = PDF[cle]
    f = cache / (ident.replace('/', '_') + '.pdf')
    if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest() != sha:
        req = urllib.request.Request(f'https://arxiv.org/pdf/{ident}',
                                     headers={'User-Agent': 'aeternam-recherche/1.0'})
        f.write_bytes(urllib.request.urlopen(req, timeout=180).read())
        time.sleep(3)
    got = hashlib.sha256(f.read_bytes()).hexdigest()
    if got != sha:
        raise SystemExit(f'{ident} : SHA-256 inattendu {got}')
    return pymupdf.open(f)


def lignes(page, pleins: bool = True) -> list[tuple[int, float, float, float, float]]:
    """Segments droits de la page : traits ('l') et, si pleins, rectangles pleins très
    minces (certaines figures dessinent ainsi graduations et barres d'erreur)."""
    out = []
    for i, d in enumerate(page.get_drawings()):
        r = d['rect']
        if pleins and d['type'] == 'f' and min(r.width, r.height) < 0.4 and max(r.width, r.height) > 0.5 \
                and ''.join(it[0] for it in d['items']) == 'llll':
            if r.width < r.height:
                xc = 0.5 * (r.x0 + r.x1)
                out.append((i, xc, r.y0, xc, r.y1))
            else:
                yc = 0.5 * (r.y0 + r.y1)
                out.append((i, r.x0, yc, r.x1, yc))
            continue
        if d['type'] in ('s', 'fs'):
            for it in d['items']:
                if it[0] == 'l':
                    out.append((i, it[1].x, it[1].y, it[2].x, it[2].y))
    return out


def verticales(segs, xmin=-1e9, xmax=1e9, ymin=-1e9, ymax=1e9):
    return [(i, 0.5 * (x0 + x1), min(y0, y1), max(y0, y1)) for i, x0, y0, x1, y1 in segs
            if abs(x0 - x1) < 0.06 and xmin <= x0 <= xmax and ymin <= min(y0, y1) and max(y0, y1) <= ymax]


def horizontales(segs, xmin=-1e9, xmax=1e9, ymin=-1e9, ymax=1e9):
    return [(i, 0.5 * (y0 + y1), min(x0, x1), max(x0, x1)) for i, x0, y0, x1, y1 in segs
            if abs(y0 - y1) < 0.06 and ymin <= y0 <= ymax and xmin <= min(x0, x1) and max(x0, x1) <= xmax]


def textes(page, xmin=-1e9, xmax=1e9, ymin=-1e9, ymax=1e9):
    out = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                x0, y0, x1, y1 = s['bbox']
                xc, yc = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
                if xmin <= xc <= xmax and ymin <= yc <= ymax and s['text'].strip():
                    out.append((s['text'].strip(), xc, yc))
    return out


def nombre(t: str):
    t = t.replace('˚', '').replace('°', '').replace('−', '-').replace(',', '')
    try:
        return float(t)
    except ValueError:
        return None


def etalonner(pos, val, log=False, tol=0.25):
    """val = a + b pos (ou log10 val = a + b pos). Renvoie (a, b, résidu max en pt)."""
    n = len(pos)
    assert n >= 3, 'moins de trois graduations'
    v = [math.log10(x) for x in val] if log else list(val)
    mp, mv = sum(pos) / n, sum(v) / n
    b = sum((p - mp) * (w - mv) for p, w in zip(pos, v)) / sum((p - mp) ** 2 for p in pos)
    a = mv - b * mp
    res = max(abs((w - a) / b - p) for p, w in zip(pos, v))
    assert res < tol, f'graduations irrégulières (résidu {res:.3f} pt)'
    return a, b, res


def convertir(p, et, log=False):
    a, b, _ = et
    return 10 ** (a + b * p) if log else a + b * p


def associer(graduations, etiquettes, axe, tol):
    """Associe chaque graduation (position) à l'étiquette numérique la plus proche."""
    pos, val = [], []
    for g in graduations:
        meilleur = None
        for t, xc, yc in etiquettes:
            v = nombre(t)
            if v is None:
                continue
            d = abs((xc if axe == 'x' else yc) - g)
            if d < tol and (meilleur is None or d < meilleur[0]):
                meilleur = (d, v)
        if meilleur is not None:
            pos.append(g)
            val.append(meilleur[1])
    return pos, val


def centre(r):
    return 0.5 * (r.x0 + r.x1), 0.5 * (r.y0 + r.y1)


def uniques(vals, tol=0.3):
    out = []
    for v in sorted(vals):
        if not out or v - out[-1] > tol:
            out.append(v)
    return out


# =================================================================== Walborn et al. 2002
def walborn(doc) -> dict:
    """Fig. 2 à 9, une par page (p. 8 à 15) : cercles pleins, barres d'erreur, axes gradués."""
    figures = {}
    for page_no, fig in zip(range(8, 16), range(2, 10)):
        page = doc[page_no - 1]
        segs = lignes(page, pleins=False)          # la courbe théorique est faite de polygones pleins
        # cadre : longues verticales et horizontales
        cadre_v = [x for _, x, y0, y1 in verticales(segs) if y1 - y0 > 150]
        cadre_h = [y for _, y, x0, x1 in horizontales(segs) if x1 - x0 > 150]
        gauche, droite, haut, bas = min(cadre_v), max(cadre_v), min(cadre_h), max(cadre_h)
        # graduations principales : traits de 3,0 à 3,5 pt collés au bord
        gy = uniques([y for _, y, x0, x1 in horizontales(segs) if abs(x0 - gauche) < 0.3 and 2.9 < x1 - x0 < 3.5])
        gx = uniques([x for _, x, y0, y1 in verticales(segs) if abs(y1 - bas) < 0.4 and 3.1 < y1 - y0 < 3.7])
        lab_y = textes(page, xmax=gauche - 1, ymin=haut - 8, ymax=bas + 8)
        lab_x = textes(page, xmin=gauche - 8, xmax=droite + 8, ymin=bas + 1, ymax=bas + 14)
        py, vy = associer(gy, lab_y, 'y', 4.0)
        px, vx = associer(gx, lab_x, 'x', 4.0)
        ety, etx = etalonner(py, vy), etalonner(px, vx)
        # marqueurs : cercles pleins d'environ 3,1 pt
        pts = []
        for d in page.get_drawings():
            r = d['rect']
            k = ''.join(it[0] for it in d['items'])
            if d['type'] == 'f' and k == 'cccc' and 2.9 < r.width < 3.4 and gauche < r.x0 < droite:
                pts.append(centre(r))
        pts.sort()
        # barres d'erreur : chapeaux horizontaux de 2,0 à 2,5 pt centrés sur le marqueur,
        # reliés à un trait vertical qui s'arrête à leur hauteur (ce qui écarte les
        # morceaux plats de la courbe théorique)
        vert = verticales(segs, xmin=gauche, xmax=droite)
        chapeaux = [(0.5 * (x0 + x1), y) for _, y, x0, x1 in horizontales(segs, xmin=gauche, xmax=droite)
                    if 1.9 < x1 - x0 < 2.6 and any(abs(xv - 0.5 * (x0 + x1)) < 0.2 and
                                                   min(abs(y0v - y), abs(y1v - y)) < 0.25
                                                   for _, xv, y0v, y1v in vert)]
        donnees = []
        for xm, ym in pts:
            ys = sorted(y for xc, y in chapeaux if abs(xc - xm) < 0.6)
            n = convertir(ym, ety)
            e = None
            if len(ys) == 2:
                haut_c, bas_c = ys
                assert haut_c <= ym + 0.35 and bas_c >= ym - 0.35, (fig, xm, ym, ys)
                e = 0.5 * (convertir(haut_c, ety) - convertir(bas_c, ety))
                milieu = convertir(0.5 * (haut_c + bas_c), ety)
                assert abs(milieu - n) < 0.6, (fig, n, milieu)
            elif len(ys) == 1:            # barre coupée par l'axe : demi-longueur visible
                e = abs(convertir(ys[0], ety) - n)
            else:
                assert not ys, (fig, xm, ym, ys)
            donnees.append({'x_mm': round(convertir(xm, etx), 4), 'coups': round(n, 3),
                            'erreur': None if e is None else round(e, 3)})
        # contrôles : nombres entiers et barres d'erreur de Poisson
        ecart_entier = max(abs(p['coups'] - round(p['coups'])) for p in donnees)
        rap = [p['erreur'] / math.sqrt(round(p['coups'])) for p in donnees
               if p['erreur'] is not None and round(p['coups']) >= 16]
        figures[f'fig{fig}'] = {
            'page_pdf': page_no, 'n_points': len(donnees), 'points': donnees,
            'etalonnage': {'graduations_y': list(zip(py, vy)), 'graduations_x': list(zip(px, vx)),
                           'residu_max_pt': max(ety[2], etx[2])},
            'controle': {'ecart_max_a_un_entier': round(ecart_entier, 3),
                         'erreur_sur_racine_N_moyenne': round(sum(rap) / len(rap), 4),
                         'erreur_sur_racine_N_min_max': [round(min(rap), 4), round(max(rap), 4)]},
        }
        assert 0.9 < sum(rap) / len(rap) < 1.1, (fig, rap)
    return figures


# =================================================================== Kim et al. 2000
def kim(doc) -> dict:
    """Fig. 3, 4, 5 (p. 4). Les étiquettes des axes sont des tracés, pas du texte : les
    graduations principales (0 à 140 par 20 ; 0,0 à 3,0 mm par 0,5) sont identifiées
    par leur nombre et leur régularité."""
    page = doc[3]
    dessins = page.get_drawings()
    cadres = []
    for d in dessins:
        r = d['rect']
        if d['type'] == 'f' and r.width < 0.3 and r.height > 100 and 360 < r.x0 < 366:
            cadres.append((r.y0, r.y1, 0.5 * (r.x0 + r.x1)))      # bord gauche de chaque figure
    cadres = sorted(set((round(a, 2), round(b, 2), round(g, 2)) for a, b, g in cadres))
    assert len(cadres) == 3, cadres
    noms = ('R01', 'R02', 'R03')
    out = {}
    for nom, (haut, bas, gauche) in zip(noms, cadres):
        gy, gx = [], []
        for d in dessins:
            r = d['rect']
            if d['type'] != 'f' or not (haut - 1 <= r.y0 and r.y1 <= bas + 1):
                continue
            if 1.40 < r.width < 1.55 and r.height < 0.15 and abs(r.x0 - gauche) < 0.3:
                gy.append(0.5 * (r.y0 + r.y1))
            if 1.40 < r.height < 1.55 and r.width < 0.15 and abs(r.y1 - bas) < 0.2:
                gx.append(0.5 * (r.x0 + r.x1))
        gy, gx = uniques(gy), uniques(gx)
        assert len(gy) == 8 and len(gx) == 7, (nom, gy, gx)
        ety = etalonner(sorted(gy, reverse=True), [20 * k for k in range(8)], tol=0.15)
        etx = etalonner(sorted(gx), [0.5 * k for k in range(7)], tol=0.15)
        pts = []
        for d in dessins:
            r = d['rect']
            if d['type'] == 'fs' and 1.7 < r.width < 2.0 and haut < r.y0 < bas and d.get('fill') == (0.0, 0.0, 0.5):
                pts.append(centre(r))
        # la légende (coin supérieur droit) contient un marqueur : on l'écarte
        legende = [t for t in textes(page, ymin=haut, ymax=bas) if t[0] == 'R' and t[1] > 500]
        assert len(legende) == 1, legende
        _, lx, ly = legende[0]
        pts = sorted(p for p in pts if math.hypot(p[0] - lx, p[1] - ly) > 25)
        out[nom] = {'points': [{'x_mm': round(convertir(x, etx), 4), 'coups': round(convertir(y, ety), 3)}
                               for x, y in pts],
                    'n_points': len(pts),
                    'etalonnage': {'residu_max_pt': max(ety[2], etx[2]),
                                   'graduations': 'y : 0 à 140 par 20 ; x : 0,0 à 3,0 mm par 0,5 (lues sur la figure)'}}
        ecart = max(abs(p['coups'] - round(p['coups'])) for p in out[nom]['points'])
        out[nom]['controle'] = {'ecart_max_a_un_entier': round(ecart, 3)}
    assert [out[n]['n_points'] for n in noms] == [28, 28, 15], [out[n]['n_points'] for n in noms]
    return out


# =================================================================== Schwindt et al. 1999
def schwindt(doc) -> dict:
    """Fig. 2 (p. 3, colonne de gauche). Marqueurs : croix (V), losanges blancs (K, base
    optimisée), triangles noirs (K, base H/V), disques noirs (V² + K²)."""
    page = doc[2]
    zone = dict(xmin=60, xmax=300, ymin=55, ymax=165)
    segs = lignes(page)
    gy = uniques([y for _, y, x0, x1 in horizontales(segs, **zone) if abs(x0 - 66.51) < 0.2 and 3.0 < x1 - x0 < 3.3])
    gx = uniques([x for _, x, y0, y1 in verticales(segs, **zone) if abs(y0 - 156.65) < 0.2 and 3.0 < y1 - y0 < 3.3])
    py, vy = associer(gy, textes(page, xmax=66, ymin=55, ymax=162), 'y', 3.0)
    px, vx = associer(gx, textes(page, xmin=60, xmax=300, ymin=161, ymax=170), 'x', 4.0)
    assert vy == [1.0, 0.8, 0.6, 0.4, 0.2, 0.0] and vx == [0, 7.5, 15, 22.5, 30, 37.5, 45], (vy, vx)
    ety, etx = etalonner(py, vy, tol=0.2), etalonner(px, vx, tol=0.2)
    dessins = page.get_drawings()
    los, tri, dis = [], [], []
    for d in dessins:
        r = d['rect']
        if not (zone['xmin'] < r.x0 < zone['xmax'] and zone['ymin'] < r.y0 < zone['ymax']):
            continue
        k = ''.join(it[0] for it in d['items'])
        if d['type'] == 'f' and k == 'llll' and 2.4 < r.width < 2.8 and d.get('fill') == (1.0, 1.0, 1.0):
            los.append(centre(r))
        elif d['type'] == 'f' and k == 'lll' and 2.4 < r.width < 2.8:
            tri.append(centre(r))           # le logiciel centre le triangle sur sa boîte
        elif d['type'] == 'f' and k == 'cccc' and 2.2 < r.width < 2.6:
            dis.append(centre(r))
    # croix : quatre petits traits pleins consécutifs dont l'axe passe par leur centre
    # commun (les contours des losanges sont aussi faits de quatre traits, mais leurs
    # axes sont perpendiculaires à la direction du centre)
    traits = []
    for i, d in enumerate(dessins):
        r = d['rect']
        k = ''.join(it[0] for it in d['items'])
        if d['type'] == 'f' and k == 'lllll' and 1.0 < r.width < 1.8 and 1.0 < r.height < 1.8 \
                and zone['xmin'] < r.x0 < zone['xmax'] and zone['ymin'] < r.y0 < zone['ymax']:
            it = max((t for t in d['items'] if t[0] == 'l'),
                     key=lambda t: math.hypot(t[2].x - t[1].x, t[2].y - t[1].y))   # grand côté
            traits.append((i, centre(r), (it[2].x - it[1].x, it[2].y - it[1].y)))
    croix = []
    j = 0
    while j + 3 < len(traits):
        groupe = traits[j:j + 4]
        if [g[0] for g in groupe] == list(range(groupe[0][0], groupe[0][0] + 4)):
            cx = sum(g[1][0] for g in groupe) / 4
            cy = sum(g[1][1] for g in groupe) / 4
            ok = True
            for _, (tx, ty), (ux, uy) in groupe:
                dx, dy = cx - tx, cy - ty
                sinus = abs(ux * dy - uy * dx) / (math.hypot(ux, uy) * math.hypot(dx, dy) + 1e-12)
                ok = ok and sinus < 0.35
            if ok:
                croix.append((cx, cy))
                j += 4
                continue
        j += 1
    for serie in (los, tri, dis, croix):
        serie.sort()
    assert [len(los), len(tri), len(dis), len(croix)] == [7, 7, 7, 7], [len(los), len(tri), len(dis), len(croix)]
    # barres d'erreur : blocs successifs (trait vertical, chapeau) pour chaque angle ;
    # ordre des blocs vérifié ci-dessous par l'encadrement des marqueurs
    chap = []
    for i, d in enumerate(dessins):
        r = d['rect']
        k = ''.join(it[0] for it in d['items'])
        # chapeaux : 2,99 pt, centrés sur une graduation d'angle (les tirets de la droite
        # V² + K² = 1 mesurent 3,09 pt et tombent entre les graduations)
        if d['type'] == 's' and k == 'l' and 2.95 < r.width < 3.05 and r.height < 0.01 \
                and zone['xmin'] < r.x0 < zone['xmax'] and zone['ymin'] < r.y0 < zone['ymax'] and r.x0 > 66.55 \
                and min(abs(0.5 * (r.x0 + r.x1) - g) for g in px) < 0.5:
            chap.append((i, 0.5 * (r.x0 + r.x1), r.y0))
    assert len(chap) == 56, len(chap)
    blocs = [chap[7 * b: 7 * (b + 1)] for b in range(8)]
    series = {'V': croix, 'K_optimise': los, 'K_base_HV': tri, 'V2_plus_K2': dis}
    out = {}
    for s, (nom, marq) in enumerate(series.items()):
        haut_b, bas_b = blocs[2 * s], blocs[2 * s + 1]
        pts = []
        for j, (xm, ym) in enumerate(marq):
            (_, xh, yh), (_, xb, yb) = haut_b[j], bas_b[j]
            assert abs(xh - xm) < 0.5 and abs(xb - xm) < 0.5, (nom, j)
            y_haut, y_bas = min(yh, yb), max(yh, yb)
            assert y_haut - 0.35 <= ym <= y_bas + 0.35, (nom, j, ym, y_haut, y_bas)
            v = convertir(ym, ety)
            v_haut, v_bas = convertir(y_haut, ety), convertir(y_bas, ety)
            pts.append({'angle_deg': round(convertir(xm, etx), 3), 'valeur': round(v, 4),
                        'barre_basse': round(v_bas, 4), 'barre_haute': round(v_haut, 4),
                        'erreur': round(0.5 * (v_haut - v_bas), 4)})
        out[nom] = pts
    out['etalonnage'] = {'graduations_y': list(zip(py, vy)), 'graduations_x': list(zip(px, vx)),
                         'residu_max_pt': max(ety[2], etx[2])}
    return out


# =================================================================== Hornberger et al. 2003
def hornberger(doc) -> dict:
    page = doc[2]
    dessins = page.get_drawings()
    segs = lignes(page)
    # ---- fig. 2 : échelle log en ordonnée (1, 2, 5, 10, 20, 50 %), 0 à 2,5e-6 mbar
    gauche, bas = 73.94, 238.78
    gy = uniques([y for _, y, x0, x1 in horizontales(segs, ymin=55, ymax=241) if abs(x0 - gauche) < 0.2 and 2.0 < x1 - x0 < 2.3])
    gx = uniques([x for _, x, y0, y1 in verticales(segs, xmin=70, xmax=295) if abs(y1 - bas) < 0.3 and 2.0 < y1 - y0 < 2.3])
    assert len(gy) == 6 and len(gx) == 6, (gy, gx)
    ety = etalonner(sorted(gy, reverse=True), [1, 2, 5, 10, 20, 50], log=True, tol=0.2)
    etx = etalonner(sorted(gx), [0, 0.5, 1, 1.5, 2, 2.5], tol=0.2)
    los = []
    for d in dessins:
        r = d['rect']
        k = ''.join(it[0] for it in d['items'])
        if d['type'] == 'f' and k == 'llll' and 4.2 < r.width < 4.5 and 5.5 < r.height < 5.8:
            los.append(centre(r))
    legende = [l for l in los if l[1] < 75 and l[0] > 230]   # losange de la légende, en haut à droite
    assert len(legende) == 1, legende
    los = sorted(l for l in los if l not in legende)
    assert len(los) == 17, len(los)
    chap = [(0.5 * (x0 + x1), y) for _, y, x0, x1 in horizontales(segs, xmin=70, xmax=295, ymin=58, ymax=241)
            if 3.9 < x1 - x0 < 4.3]
    fig2 = []
    for xm, ym in los:
        ys = sorted(y for xc, y in chap if abs(xc - xm) < 0.6)
        v = convertir(ym, ety, log=True)
        haut_c = ys[0] if ys and ys[0] < ym else None
        bas_c = ys[-1] if ys and ys[-1] > ym else None
        v_h = None if haut_c is None else convertir(haut_c, ety, log=True)
        v_b = None if bas_c is None else convertir(bas_c, ety, log=True)
        fig2.append({'p_1e-6_mbar': round(convertir(xm, etx), 4), 'visibilite_pct': round(v, 3),
                     'barre_haute_pct': None if v_h is None else round(v_h, 3),
                     'barre_basse_pct': None if v_b is None else round(v_b, 3)})
    # la dernière barre descend sous le bas du cadre (1 %) : pas de chapeau bas
    assert all(p['barre_haute_pct'] is not None for p in fig2)
    assert sum(p['barre_basse_pct'] is None for p in fig2) == 1 and fig2[-1]['barre_basse_pct'] is None
    sym = [(p['barre_haute_pct'] - p['visibilite_pct']) / (p['visibilite_pct'] - p['barre_basse_pct'])
           for p in fig2[:-1]]
    # ---- fig. 3 : p0 (1e-6 mbar) en fonction de sigma_eff (nm²), étiquettes en texte
    zone = dict(xmin=340, xmax=560, ymin=500, ymax=675)
    gy3 = uniques([y for _, y, x0, x1 in horizontales(segs, **zone) if abs(x0 - 351.65) < 0.2 and 1.8 < x1 - x0 < 2.0])
    gx3 = uniques([x for _, x, y0, y1 in verticales(segs, **zone) if abs(y1 - 665.36) < 0.2 and 1.8 < y1 - y0 < 2.0])
    py, vy = associer(gy3, textes(page, xmin=340, xmax=351, ymin=500, ymax=670), 'y', 2.5)
    px, vx = associer(gx3, textes(page, xmin=345, xmax=550, ymin=666, ymax=674), 'x', 3.0)
    ety3, etx3 = etalonner(py, vy, tol=0.2), etalonner(px, vx, tol=0.2)
    cercles, carres = [], []
    for d in dessins:
        r = d['rect']
        k = ''.join(it[0] for it in d['items'])
        if not (352 < r.x0 < 542 and 507 < r.y0 < 664):
            continue
        if d['type'] == 's' and k == 'cccc' and 3.7 < r.width < 3.9:
            cercles.append(centre(r))
        elif d['type'] == 's' and k == 'qu' and 2.9 < r.width < 3.1:
            carres.append(centre(r))
    # légende : cadre (482-541, 509-527)
    cercles = sorted(c for c in cercles if not (482 < c[0] < 541 and 509 < c[1] < 527))
    carres = sorted(c for c in carres if not (482 < c[0] < 541 and 509 < c[1] < 527))
    assert len(cercles) == 10 and len(carres) == 9, (len(cercles), len(carres))
    # barres d'erreur : un trait vertical d'un chapeau à l'autre ; on prend celui dont le
    # milieu coïncide avec le cercle (deux barres se chevauchent pour N2 et l'air)
    barres3 = [(x, y0, y1) for _, x, y0, y1 in verticales(segs, **zone) if y1 - y0 > 2.0]
    # abscisses des étiquettes de gaz (texte de la figure) ; N2 et air partagent
    # sigma_eff = 69 nm² et un seul carré théorique
    etiquettes = {t: xc for t, xc, _ in textes(page, xmin=370, xmax=530, ymin=595, ymax=645)
                  if t in ('Ne', 'He', 'Kr', 'Ar', 'Xe', 'D', 'CH', 'H')}
    etiquettes = {{'D': 'D2', 'CH': 'CH4', 'H': 'H2'}.get(k, k): v for k, v in etiquettes.items()}
    assert len(etiquettes) == 8, etiquettes
    fig3 = []
    for xm, ym in cercles:
        cand = [(abs(0.5 * (y0 + y1) - ym), y0, y1) for x, y0, y1 in barres3 if abs(x - xm) < 0.6]
        ecart, a, b = min(cand)
        assert ecart < 0.3, (xm, ym, cand)
        th = [c for c in carres if abs(c[0] - xm) < 0.6]
        meme_x = sum(abs(c[0] - xm) < 0.3 for c in cercles)
        gaz = min(etiquettes, key=lambda g: abs(etiquettes[g] - xm))
        fig3.append({'gaz': 'N2 ou air' if meme_x == 2 else gaz,
                     'sigma_eff_nm2': round(convertir(xm, etx3), 3),
                     'p0_mesure': round(convertir(ym, ety3), 4),
                     'p0_erreur': round(0.5 * (convertir(a, ety3) - convertir(b, ety3)), 4),
                     'p0_theorie': round(convertir(th[0][1], ety3), 4) if th else None})
    # droite théorique de la fig. 2 (« solid line », prédiction sans paramètre ajustable) :
    # polygone plein très mince ; on prend l'axe médian entre ses deux longs côtés
    droites = [d for d in dessins if d['type'] == 'f' and len(d['items']) == 5
               and all(it[0] == 'l' for it in d['items']) and d['rect'].width > 150
               and 55 < d['rect'].y0 and d['rect'].y1 < 241]
    assert len(droites) == 1, len(droites)
    longs = sorted((it for it in droites[0]['items'] if abs(it[2].x - it[1].x) > 150),
                   key=lambda it: it[1].y + it[2].y)
    assert len(longs) == 2
    ext = []
    for bout in ('gauche', 'droite'):
        pts = []
        for it in longs:
            a, b = sorted((it[1], it[2]), key=lambda q: q.x)
            pts.append(a if bout == 'gauche' else b)
        ext.append((0.5 * (pts[0].x + pts[1].x), 0.5 * (pts[0].y + pts[1].y)))
    theorie2 = [{'p_1e-6_mbar': round(convertir(x, etx), 4), 'visibilite_pct': round(convertir(y, ety, log=True), 3)}
                for x, y in ext]
    return {'fig2': {'points': fig2, 'n_points': len(fig2), 'theorie_extremites': theorie2,
                     'etalonnage': {'residu_max_pt': max(ety[2], etx[2]),
                                    'graduations': 'y log : 1, 2, 5, 10, 20, 50 % ; x : 0 à 2,5e-6 mbar par 0,5 (lues sur la figure)'},
                     'controle': {'symetrie_barres_haut_sur_bas_min_max': [round(min(sym), 3), round(max(sym), 3)]}},
            'fig3': {'points': fig3, 'n_points': len(fig3),
                     'etalonnage': {'graduations_y': list(zip(py, vy)), 'graduations_x': list(zip(px, vx)),
                                    'residu_max_pt': max(ety3[2], etx3[2])}}}


# =================================================================== Hackermüller et al. 2004
def hackermuller(doc) -> dict:
    page = doc[3]
    dessins = page.get_drawings()
    segs = lignes(page)
    out = {}
    lab_x = textes(page, xmin=105, xmax=300, ymin=315, ymax=328)
    for panneau, (ymin, ymax) in (('a', (60, 185)), ('b', (190, 314))):
        lab_y = [t for t in textes(page, xmin=90, xmax=112, ymin=ymin, ymax=ymax)]
        # graduations de l'ordonnée : traits horizontaux courts collés à l'axe gauche
        gy = uniques([y for _, y, x0, x1 in horizontales(segs, xmin=110, xmax=120, ymin=ymin, ymax=ymax)
                      if 2.2 < x1 - x0 < 2.6])
        py, vy = associer(gy, lab_y, 'y', 3.0)
        assert vy == [1.0, 0.8, 0.6, 0.4, 0.2, 0.0], (panneau, vy)
        ety = etalonner(py, vy, tol=0.3)
        out[panneau] = {'ety': ety, 'bornes': (ymin, ymax)}
    gx = uniques([x for _, x, y0, y1 in verticales(segs, xmin=110, xmax=295, ymin=300, ymax=315) if 2.0 < y1 - y0 < 2.6])
    px, vx = associer(gx, lab_x, 'x', 3.0)
    assert len(vx) >= 5 and all(v == int(v) and 0 <= v <= 10 for v in vx), vx   # graduations tous les 2 W
    etx = etalonner(px, vx, tol=0.3)
    points = []
    for d in dessins:
        r = d['rect']
        k = ''.join(it[0] for it in d['items'])
        if d['type'] == 'f' and k == 'cccc' and 3.6 < r.width < 4.0 and 110 < r.x0 < 300:
            points.append(centre(r))
    assert len(points) == 32, len(points)
    # barres d'erreur : deux chapeaux horizontaux (2,5 pt en b, 3,6 pt en a), souvent
    # cachés derrière le marqueur ; on prend le plus proche au-dessus et au-dessous
    chapeaux = [(0.5 * (x0 + x1), y) for _, y, x0, x1 in horizontales(segs, xmin=110, xmax=300, ymin=55, ymax=315)
                if 2.3 < x1 - x0 < 3.7]
    res = {}
    for panneau in ('a', 'b'):
        ety = out[panneau]['ety']
        ymin, ymax = out[panneau]['bornes']
        pts = sorted(p for p in points if ymin < p[1] < ymax)
        liste = []
        for xm, ym in pts:
            dessus = [y for xc, y in chapeaux if abs(xc - xm) < 0.5 and ym - 12 < y < ym]
            dessous = [y for xc, y in chapeaux if abs(xc - xm) < 0.5 and ym < y < ym + 12]
            e = None
            if dessus and dessous:
                haut_c, bas_c = max(dessus), min(dessous)
                assert abs(0.5 * (haut_c + bas_c) - ym) < 0.4, (panneau, xm, ym, haut_c, bas_c)
                e = 0.5 * (convertir(haut_c, ety) - convertir(bas_c, ety))
            liste.append({'puissance_W': round(convertir(xm, etx), 3), 'visibilite_normalisee': round(convertir(ym, ety), 4),
                          'erreur': None if e is None else round(e, 4)})
        res[panneau] = liste
    assert len(res['a']) == 21 and len(res['b']) == 11, (len(res['a']), len(res['b']))
    # courbes théoriques (trait plein) : une ligne brisée de 40 segments par panneau
    theorie = {}
    for panneau in ('a', 'b'):
        ety = out[panneau]['ety']
        ymin, ymax = out[panneau]['bornes']
        courbes = [d for d in dessins if d['type'] == 's' and len(d['items']) == 40
                   and all(it[0] == 'l' for it in d['items']) and d['rect'].width > 150
                   and ymin < d['rect'].y0 and d['rect'].y1 < ymax]
        assert len(courbes) == 1, (panneau, len(courbes))
        its = courbes[0]['items']
        sommets = [it[1] for it in its] + [its[-1][2]]
        for u, v in zip(its[:-1], its[1:]):
            assert abs(u[2].x - v[1].x) < 1e-3 and abs(u[2].y - v[1].y) < 1e-3   # ligne continue
        theorie[panneau] = [{'puissance_W': round(convertir(p.x, etx), 4),
                             'visibilite_normalisee': round(convertir(p.y, ety), 4)} for p in sommets]
    return {'a': res['a'], 'b': res['b'], 'theorie_a': theorie['a'], 'theorie_b': theorie['b'],
            'etalonnage': {'residu_max_pt': max(etx[2], out['a']['ety'][2], out['b']['ety'][2])}}


# =================================================================== principal
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cache', type=Path, default=None, help='dossier des PDF téléchargés')
    args = ap.parse_args()
    cache = args.cache or Path(tempfile.gettempdir()) / 'aeternam-test5-pdf'
    cache.mkdir(parents=True, exist_ok=True)
    res = {
        'note': 'Valeurs relevées par extraire.py dans les dessins vectoriels des PDF arXiv '
                '(coordonnées des marqueurs, étalonnées sur les graduations). Voir sources.md.',
        'pymupdf': pymupdf.VersionBind,
        'pdf': {k: {'arxiv': v[0], 'url': f'https://arxiv.org/pdf/{v[0]}', 'sha256': v[1]} for k, v in PDF.items()},
        'walborn2002': walborn(telecharger('walborn2002', cache)),
        'kim2000': kim(telecharger('kim2000', cache)),
        'schwindt1999': schwindt(telecharger('schwindt1999', cache)),
        'hornberger2003': hornberger(telecharger('hornberger2003', cache)),
        'hackermuller2004': hackermuller(telecharger('hackermuller2004', cache)),
    }
    SORTIE.parent.mkdir(exist_ok=True)
    SORTIE.write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('écrit', SORTIE, hashlib.sha256(SORTIE.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
