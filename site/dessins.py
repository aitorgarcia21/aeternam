"""Dessins au trait d'ÆTERNAM : une plume, des hachures, un seul or.

Ce sont des illustrations, hors échelle : aucune n'est une mesure ni un enregistrement, et
aucune n'est présentée comme telle (les figures de données sont dans site/visuels.py). Les
formes sont calculées (lemniscate, positions d'électrodes, grille cubique), pas tracées à la
main. Bibliothèque standard uniquement.
"""
from __future__ import annotations

import html
import math
import random

# Ce que chaque dessin montre, dit dans la langue de la page : rempli par site/generer.py
# avec UI['dessins'] avant de construire une édition.
LIBELLES: dict = {}


def n(x: float) -> str:
    return f'{x:.1f}'.rstrip('0').rstrip('.')


def chemin(points, ferme: bool = False) -> str:
    return 'M' + ' L'.join(f'{n(x)} {n(y)}' for x, y in points) + (' Z' if ferme else '')


# Le trait « à la main » : un déplacement par bruit, dont la graine change quelques fois
# par seconde (site/base.js). Inclus une fois par page.
FILTRES = ('<svg class="filtres" width="0" height="0" aria-hidden="true" focusable="false"><defs>'
           '<filter id="trait" x="-8%" y="-8%" width="116%" height="116%">'
           '<feTurbulence type="fractalNoise" baseFrequency=".032" numOctaves="2" seed="4" result="b"/>'
           '<feDisplacementMap in="SourceGraphic" in2="b" scale="3.2" xChannelSelector="R" yChannelSelector="G"/></filter>'
           '<filter id="trait2" x="-8%" y="-8%" width="116%" height="116%">'
           '<feTurbulence type="fractalNoise" baseFrequency=".021" numOctaves="2" seed="19" result="b"/>'
           '<feDisplacementMap in="SourceGraphic" in2="b" scale="5" xChannelSelector="R" yChannelSelector="G"/></filter>'
           '</defs></svg>')


def hachures(p: str) -> str:
    """Deux hachures par dessin : dans la couleur du trait (.h) et dans celle du fond (.hi)."""
    return (f'<pattern id="{p}-h" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">'
            f'<line class="h" x1="0" y1="0" x2="0" y2="6"/></pattern>'
            f'<pattern id="{p}-hf" width="4.2" height="4.2" patternUnits="userSpaceOnUse" patternTransform="rotate(-50)">'
            f'<line class="h" x1="0" y1="0" x2="0" y2="4.2"/></pattern>'
            f'<pattern id="{p}-hi" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">'
            f'<line class="hi" x1="0" y1="0" x2="0" y2="5"/></pattern>')


def svg(classe: str, boite: str, label: str, contenu: str) -> str:
    return (f'<svg class="dessin d-{classe}" viewBox="{boite}" role="img" '
            f'aria-label="{html.escape(label, quote=True)}">{contenu}</svg>')


def t(d: str, classe: str = '', delai: float = 0.0) -> str:
    """Un trait qui se dessine à l'arrivée (pathLength = 1)."""
    style = f' style="--d:{n(delai)}s"' if delai else ''
    return f'<path class="t{" " + classe if classe else ""}" pathLength="1" d="{d}"{style}/>'


# ------------------------------------------------------------------ le sablier
LEMNISCATE_A, LEMNISCATE_GROS = 240.0, 1.15


def point_lemniscate(angle: float, a: float = LEMNISCATE_A, gros: float = LEMNISCATE_GROS) -> tuple[float, float]:
    """Lemniscate de Bernoulli dressée : deux lobes, un nœud au centre."""
    d = 1 + math.sin(angle) ** 2
    return gros * a * math.sin(angle) * math.cos(angle) / d, -a * math.cos(angle) / d


def sablier() -> str:
    """Le sablier de l'accueil : son sable tombe, ralentit, puis reste suspendu (site/accueil/accueil.js)."""
    a = LEMNISCATE_A
    k = 200
    tour = [point_lemniscate(2 * math.pi * i / k) for i in range(k + 1)]
    haut = [point_lemniscate(-math.pi / 2 + math.pi * i / 100) for i in range(101)]
    bas = [point_lemniscate(math.pi / 2 + math.pi * i / 100) for i in range(101)]
    hasard = random.Random(7)
    grains_surface = ''.join(
        f'<circle cx="{n(hasard.uniform(-70, 70))}" cy="{n(-118 + hasard.uniform(0, 26))}" r="{n(hasard.uniform(.7, 1.3))}"/>'
        for _ in range(26))
    # Le filet de sable. Chaque grain a sa place dans la chute (phase), son écart à l'axe (x) et la
    # dérive qu'il prend quand le temps s'arrête (dx, dy) ; le script le déplace à chaque image.
    nombre = 44
    chute = ''.join(
        f'<circle cx="{n(hasard.uniform(-1.7, 1.7))}" cy="{n(2 + 102 * (i + .5) / nombre)}" r="{n(hasard.uniform(.9, 1.9))}" '
        f'data-phase="{(i + hasard.uniform(0, .8)) / nombre:.3f}" data-dx="{n(hasard.uniform(-9, 9))}" '
        f'data-dy="{n(hasard.uniform(-5, 5))}" data-w="{n(hasard.uniform(.6, 1.4))}"/>'
        for i in range(nombre))
    poteaux = ''.join(
        f'<path d="M{x - 3} -246 L{x - 3} 246 M{x + 3} -246 L{x + 3} 246"/>'
        f'<ellipse cx="{x}" cy="0" rx="8" ry="5" class="plein"/>'
        f'<path d="M{x - 7} -226 L{x + 7} -226 M{x - 7} 226 L{x + 7} 226"/>' for x in (-118, 118))
    socles = ''.join(
        f'<rect class="plein" x="-132" y="{y}" width="264" height="22" rx="6"/>'
        f'<rect x="-20" y="{y}" width="152" height="22" fill="url(#sab-hi)" stroke="none"/>'
        f'<rect class="plein" x="-110" y="{y2}" width="220" height="6" rx="2"/>'
        for y, y2 in ((-270, -247), (248, 241)))
    return svg('sablier', '-300 -300 600 600', LIBELLES['sablier'], f'''
<defs>{hachures('sab')}
<clipPath id="sab-haut"><path d="{chemin(haut, True)}"/></clipPath>
<clipPath id="sab-bas"><path d="{chemin(bas, True)}"/></clipPath>
</defs>
<g id="sablier-tourne">
<g class="sablier-cadre" filter="url(#trait)">{socles}{poteaux}</g>
<g class="sablier-sable" filter="url(#trait)">
<g clip-path="url(#sab-haut)"><path class="or-plein" d="M-120 -124 Q0 -98 120 -124 L120 6 L-120 6 Z"/>
<path d="M18 -124 Q70 -110 120 -124 L120 6 L18 6 Z" fill="url(#sab-hi)" stroke="none" opacity=".55"/>
<g class="grains-surface">{grains_surface}</g></g>
<g clip-path="url(#sab-bas)"><path class="or-plein" d="M-120 174 C-56 172 -24 122 0 104 C24 122 56 172 120 174 L120 250 L-120 250 Z"/>
<path d="M8 110 C28 126 58 172 120 174 L120 250 L8 250 Z" fill="url(#sab-hi)" stroke="none" opacity=".55"/></g>
</g>
<g class="sablier-chute or-plein">{chute}</g>
<g class="sablier-reflets fin" filter="url(#trait2)"><path d="M-60 -200 C-80 -172 -84 -142 -72 -112"/><path d="M-44 -212 C-52 -200 -58 -190 -62 -178"/><path d="M62 200 C80 174 84 148 74 124"/></g>
<g class="sablier-verre" filter="url(#trait)"><path class="verre" d="{chemin(tour, True)}"/></g>
<g class="sablier-verre double" filter="url(#trait2)"><path class="verre fin" d="{chemin(tour, True)}"/></g>
</g>''')


# ------------------------------------------------------------------ relativité et trous noirs
def relativite() -> str:
    cx, cy, pente = 248, 262, math.radians(-12)

    def arc(rx: float, ry: float, a0: float, a1: float, pas: int = 48) -> str:
        pts = []
        for i in range(pas + 1):
            ang = math.radians(a0 + (a1 - a0) * i / pas)
            x, y = rx * math.cos(ang), ry * math.sin(ang)
            pts.append((cx + x * math.cos(pente) - y * math.sin(pente), cy + x * math.sin(pente) + y * math.cos(pente)))
        return chemin(pts)

    def cercle(r: float, a0: float, a1: float, pas: int = 40) -> list:
        return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / pas)),
                 cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / pas))) for i in range(pas + 1)]

    disque = ((198, 52), (168, 42), (140, 33))
    arriere = ''.join(t(arc(rx, ry, 180, 360), 'fin pale', .15 * i) for i, (rx, ry) in enumerate(disque))
    avant = ''.join(f'<path class="masque f" d="{arc(rx, ry, 0, 180)}"/>' + t(arc(rx, ry, 0, 180), '', .5 + .15 * i)
                    for i, (rx, ry) in enumerate(disque))
    halo = chemin(cercle(92, 196, 344) + cercle(79, 344, 196), True)

    def horloge(x: float, y: float, r: float, duree: float, classe: str) -> str:
        graduations = ''.join(
            f'<path class="fin" d="M{n(x + (r - (5 if i % 3 == 0 else 2.5)) * math.cos(i * math.pi / 6))} '
            f'{n(y + (r - (5 if i % 3 == 0 else 2.5)) * math.sin(i * math.pi / 6))} '
            f'L{n(x + (r - .5) * math.cos(i * math.pi / 6))} {n(y + (r - .5) * math.sin(i * math.pi / 6))}"/>'
            for i in range(12))
        return (f'<g class="horloge {classe}"><circle class="papier" cx="{x}" cy="{y}" r="{r}"/>{graduations}'
                f'<path class="aiguille or gras" d="M{x} {y} L{x} {n(y - r + 7)}" '
                f'style="transform-origin:{x}px {y}px;animation-duration:{duree}s"/>'
                f'<circle class="plein" cx="{x}" cy="{y}" r="2"/></g>')

    return svg('relativite', '0 0 480 480', LIBELLES['relativite'], f'''
<defs>{hachures('rel')}</defs>
<g filter="url(#trait)">
{arriere}
<path class="f" d="{halo}" fill="url(#rel-hf)" stroke="none"/>
{t(chemin(cercle(92, 196, 344)), 'fin', .3)}
<circle class="trou f" cx="{cx}" cy="{cy}" r="63"/>
{t(chemin(cercle(76, 0, 360)), 'fin', .2)}
{avant}
{t('M14 92 C150 92 262 104 466 162', 'or fin', .9)}{t('M14 436 C150 436 262 428 466 372', 'or fin', 1.05)}
<path class="or f" d="M456 152 L466 162 L452 166 M456 382 L466 372 L452 368" style="--d:1.6s"/>
</g>
{horloge(410, 74, 31, 5, 'lointaine')}{horloge(150, 372, 23, 17, 'proche')}''')


# ------------------------------------------------------------------ vision et perception
def vision() -> str:
    haut = ((52, 244), (140, 120), (340, 120), (428, 244))
    bas = ((52, 244), (140, 352), (340, 352), (428, 244))

    def bezier(p, u: float) -> tuple[float, float]:
        v = 1 - u
        return (v ** 3 * p[0][0] + 3 * v * v * u * p[1][0] + 3 * v * u * u * p[2][0] + u ** 3 * p[3][0],
                v ** 3 * p[0][1] + 3 * v * v * u * p[1][1] + 3 * v * u * u * p[2][1] + u ** 3 * p[3][1])

    amande = (f'M{haut[0][0]} {haut[0][1]} C{haut[1][0]} {haut[1][1]} {haut[2][0]} {haut[2][1]} {haut[3][0]} {haut[3][1]} '
              f'C{bas[2][0]} {bas[2][1]} {bas[1][0]} {bas[1][1]} {bas[0][0]} {bas[0][1]} Z')
    cils = []
    for i in range(13):
        u = .12 + .76 * i / 12
        x, y = bezier(haut, u)
        x2, y2 = bezier(haut, u + .01)
        nx, ny = (y2 - y), -(x2 - x)
        norme = math.hypot(nx, ny)
        longueur = 13 + 9 * math.sin(math.pi * (u - .12) / .76)
        penche = (u - .5) * 16
        cils.append(f'<path class="fin" d="M{n(x)} {n(y)} L{n(x + nx / norme * longueur + penche)} {n(y + ny / norme * longueur)}"/>')
    stries = ''.join(
        f'<path class="fin pale" d="M{n(240 + 65 * math.cos(i * math.pi / 22))} {n(240 + 65 * math.sin(i * math.pi / 22))} '
        f'L{n(240 + (74 + 4 * (i % 3)) * math.cos(i * math.pi / 22))} {n(240 + (74 + 4 * (i % 3)) * math.sin(i * math.pi / 22))}"/>'
        for i in range(44))
    points, ordre = [], 0
    for ligne in range(9):
        for col in range(9):
            x, y = 240 + (col - 4) * 12.5, 240 + (ligne - 4) * 12.5
            if math.hypot(x - 240, y - 240) > 58:
                continue
            allume = (col == 2 and 1 <= ligne <= 7) or (ligne in (1, 7) and 2 <= col <= 6) or (ligne == 4 and 2 <= col <= 5)
            if allume:
                points.append(f'<circle class="phosphene or-plein" cx="{n(x)}" cy="{n(y)}" r="4.3" style="--d:{n(.9 + .07 * ordre)}s"/>')
                ordre += 1
            else:
                points.append(f'<circle class="plein" cx="{n(x)}" cy="{n(y)}" r="1.25"/>')
    return svg('vision', '0 0 480 480', LIBELLES['vision'], f'''
<defs>{hachures('vis')}<clipPath id="vis-amande"><path d="{amande}"/></clipPath></defs>
<g filter="url(#trait)">
<g clip-path="url(#vis-amande)">
<path class="f" d="M40 250 C140 108 340 108 440 250 L440 214 C340 150 140 150 40 214 Z" fill="url(#vis-hf)" stroke="none"/>
{t('M320 240 A80 80 0 1 1 319.9 239.6', '', .35)}{stries}
<circle class="fin f" cx="240" cy="240" r="63"/>
</g>
{t(f'M{haut[0][0]} {haut[0][1]} C{haut[1][0]} {haut[1][1]} {haut[2][0]} {haut[2][1]} {haut[3][0]} {haut[3][1]}', 'gras')}
{t(f'M{bas[0][0]} {bas[0][1]} C{bas[1][0]} {bas[1][1]} {bas[2][0]} {bas[2][1]} {bas[3][0]} {bas[3][1]}', '', .15)}
{t('M74 212 C152 92 328 92 406 212', 'fin pale', .3)}
<path class="fin f" d="M52 244 C44 250 40 258 42 266"/>
<g class="f" style="--d:.6s">{''.join(cils)}</g>
</g>
<g class="grille">{''.join(points)}</g>''')


# ------------------------------------------------------------------ mémoire
def memoire() -> str:
    noeuds = [(96, 122), (192, 82), (302, 108), (398, 152), (138, 218), (250, 196), (354, 252),
              (82, 322), (198, 318), (306, 354), (412, 364), (148, 414), (262, 432)]
    aretes = [(0, 1), (1, 2), (2, 3), (0, 4), (1, 5), (2, 5), (3, 6), (4, 5), (5, 6), (4, 7), (4, 8), (5, 8),
              (6, 9), (6, 10), (7, 8), (8, 9), (9, 10), (7, 11), (8, 11), (8, 12), (9, 12), (11, 12)]
    souvenir = [1, 5, 8, 9, 6, 5]
    hasard = random.Random(11)

    def courbe(i: int, j: int, signe: float = 0) -> str:
        (x1, y1), (x2, y2) = noeuds[i], noeuds[j]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        norme = math.hypot(dx, dy)
        f = signe or hasard.choice((-1, 1)) * hasard.uniform(6, 15)
        return f'Q{n(mx - dy / norme * f)} {n(my + dx / norme * f)} {n(x2)} {n(y2)}'

    fleches = {a: hasard.choice((-1, 1)) * hasard.uniform(6, 15) for a in aretes}
    liens = ''.join(t(f'M{noeuds[i][0]} {noeuds[i][1]} ' + courbe(i, j, fleches[(i, j)]), 'fin pale', .04 * k)
                    for k, (i, j) in enumerate(aretes))
    trajet = f'M{noeuds[souvenir[0]][0]} {noeuds[souvenir[0]][1]} '
    for i, j in zip(souvenir, souvenir[1:]):
        cle = (i, j) if (i, j) in fleches else (j, i)
        trajet += courbe(i, j, fleches[cle] * (1 if (i, j) in fleches else -1)) + ' '
    dendrites = []
    for x, y in noeuds:
        for _ in range(3):
            ang = hasard.uniform(0, 2 * math.pi)
            l1, l2 = hasard.uniform(13, 21), hasard.uniform(7, 11)
            bx, by = x + l1 * math.cos(ang), y + l1 * math.sin(ang)
            dendrites.append(f'<path class="fin" d="M{n(x)} {n(y)} L{n(bx)} {n(by)} L{n(bx + l2 * math.cos(ang + .6))} {n(by + l2 * math.sin(ang + .6))} '
                             f'M{n(bx)} {n(by)} L{n(bx + l2 * math.cos(ang - .7))} {n(by + l2 * math.sin(ang - .7))}"/>')
    corps = ''.join(
        (f'<circle class="or-plein neurone" cx="{x}" cy="{y}" r="11" style="--d:{n(1 + .25 * souvenir.index(i))}s"/>'
         if i in souvenir else f'<circle class="papier" cx="{x}" cy="{y}" r="8"/>')
        for i, (x, y) in enumerate(noeuds))
    return svg('memoire', '0 0 480 480', LIBELLES['memoire'], f'''
<g filter="url(#trait)">{liens}<g class="f" style="--d:.5s">{''.join(dendrites)}</g>
{t(trajet, 'or', .9)}
{corps}</g>
<path class="or gras signal" pathLength="1" d="{trajet}"/>''')


# ------------------------------------------------------------------ rêve et temps vécu
def reve() -> str:
    niveaux = {'E': 190, 'P': 224, 'N1': 258, 'N2': 292, 'N3': 326}
    noms = {'E': LIBELLES['eveil'], 'P': LIBELLES['paradoxal'], 'N1': 'N1', 'N2': 'N2', 'N3': 'N3'}
    nuit = [('E', 1), ('N1', 1), ('N2', 2), ('N3', 4), ('N2', 1.5), ('P', 1.2), ('N2', 2), ('N3', 3), ('N2', 1.5),
            ('P', 2.2), ('N2', 2.5), ('N3', 1.2), ('N2', 1.5), ('P', 3.2), ('N2', 2), ('P', 3.8), ('E', 1)]
    x0, x1 = 112, 440
    echelle = (x1 - x0) / sum(d for _, d in nuit)
    x, pts, paradoxal = x0, [], []
    for stade, duree in nuit:
        y, xf = niveaux[stade], x + duree * echelle
        pts += [(x, y), (xf, y)]
        if stade == 'P':
            paradoxal.append(f'M{n(x)} {y} L{n(xf)} {y}')
        x = xf
    etiquettes = ''.join(f'<text class="nom" x="{x0 - 14}" y="{y + 3.5}" text-anchor="end">{noms[s]}</text>' for s, y in niveaux.items())
    graduations = ''.join(f'<path class="fin" d="M{n(x0 + i * (x1 - x0) / 8)} 356 L{n(x0 + i * (x1 - x0) / 8)} 362"/>' for i in range(9))
    # Croissant : intersection de deux cercles.
    (ax, ay, ar), (bx, by, br) = (368, 96, 46), (390, 82, 40)
    d = math.hypot(bx - ax, by - ay)
    k = (ar * ar - br * br + d * d) / (2 * d)
    h = math.sqrt(ar * ar - k * k)
    mx, my = ax + k * (bx - ax) / d, ay + k * (by - ay) / d
    p1 = (mx + h * (by - ay) / d, my - h * (bx - ax) / d)
    p2 = (mx - h * (by - ay) / d, my + h * (bx - ax) / d)
    croissant = (f'M{n(p1[0])} {n(p1[1])} A{ar} {ar} 0 1 0 {n(p2[0])} {n(p2[1])} '
                 f'A{br} {br} 0 0 1 {n(p1[0])} {n(p1[1])} Z')
    etoiles = ''.join(f'<path class="or fin etoile" style="--d:{n(i * .7)}s" d="M{x - r} {y} L{x + r} {y} M{x} {y - r} L{x} {y + r}"/>'
                      for i, (x, y, r) in enumerate(((150, 70, 6), (226, 118, 4), (286, 56, 5), (96, 132, 4), (444, 150, 4))))
    trace = chemin(pts)
    return svg('reve', '0 0 480 480', LIBELLES['reve'], f'''
<defs>{hachures('rev')}</defs>
<g filter="url(#trait)">
<path class="f" d="{croissant}" fill="url(#rev-hf)" stroke="none"/>{t(croissant, '', .2)}
<circle class="fin pale tirets f" cx="{ax}" cy="{ay}" r="{ar}"/>
{t(trace, '', .5)}
{''.join(t(p, 'or gras', 1.3 + .2 * i) for i, p in enumerate(paradoxal))}
<path class="fin f" d="M{x0} 356 L{x1} 356"/><g class="f">{graduations}</g>
</g>
{etoiles}
<g class="f">{etiquettes}<text class="nom" x="{x0}" y="378">0 h</text><text class="nom" x="{x1}" y="378" text-anchor="end">8 h</text></g>
<circle class="or-plein voyageur" r="4.5"><animateMotion dur="14s" repeatCount="indefinite" path="{trace}"/></circle>''')


# ------------------------------------------------------------------ interfaces cerveau-machine
# Positions schématiques (système 10-10, vue de dessus, le nez en haut), en rayons de tête.
MONTAGE = {'FC3': (-.46, -.21), 'FC4': (.46, -.21), 'C3': (-.5, 0), 'Cz': (0, 0), 'C4': (.5, 0),
               'CP3': (-.46, .21), 'CPz': (0, .2), 'CP4': (.46, .21)}
REPERES = ((0, -.4), (0, .4), (-.42, -.44), (.42, -.44), (-.42, .44), (.42, .44), (-.25, -.76), (.25, -.76),
           (-.25, .76), (.25, .76), (-.75, 0), (.75, 0), (0, -.8), (0, .8), (-.25, 0), (.25, 0), (0, -.2))


def onde(largeur: float, amplitude: float, graine: int) -> str:
    """Un tracé périodique sur `largeur`, dessiné deux fois de suite pour défiler sans raccord."""
    hasard = random.Random(graine)
    phases = [hasard.uniform(0, 2 * math.pi) for _ in range(4)]
    pts = []
    for i in range(int(2 * largeur / 2) + 1):
        x = i * 2
        u = 2 * math.pi * x / largeur
        enveloppe = 1 + .55 * math.sin(2 * u + phases[0])
        y = amplitude * (enveloppe * .62 * math.sin(13 * u + phases[1]) + .26 * math.sin(29 * u + phases[2])
                         + .3 * math.sin(5 * u + phases[3]))
        pts.append((x, y))
    return chemin(pts)


def montage(prefixe: str = 'bci', toutes_etiquettes: bool = False, voies: tuple = ('C3', 'Cz', 'C4')) -> str:
    """Une tête vue de dessus, huit électrodes au-dessus du cortex moteur et des tracés dessinés (pas des enregistrements)."""
    cx, cy, r = 240, 178, 128
    haut_traces = 360
    pas = 30 if len(voies) <= 3 else 17
    boite_h = haut_traces + pas * len(voies) + 14
    reperes = ''.join(f'<circle class="fin pale" cx="{n(cx + x * r)}" cy="{n(cy + y * r)}" r="2.6"/>' for x, y in REPERES)
    electrodes, noms = [], []
    for nom, (x, y) in MONTAGE.items():
        ex, ey = cx + x * r, cy + y * r
        classe = 'or-plein' if nom in ('C3', 'C4') else 'papier'
        electrodes.append(f'<circle class="{classe} electrode" cx="{n(ex)}" cy="{n(ey)}" r="7.5" '
                          f'style="--d:{n(.6 + .08 * len(electrodes))}s"/>')
        if toutes_etiquettes or nom in ('C3', 'Cz', 'C4'):
            dessous = y >= 0
            noms.append(f'<text class="nom" x="{n(ex)}" y="{n(ey + (21 if dessous else -13))}" text-anchor="middle">{nom}</text>')
    largeur = 340
    traces = []
    for i, nom in enumerate(voies):
        y = haut_traces + i * pas
        traces.append(f'<text class="nom" x="80" y="{n(y + 3.5)}" text-anchor="end">{nom}</text>'
                      f'<g transform="translate(92 {n(y)})"><path class="defile {"or" if nom in ("C3", "C4") else ""}" '
                      f'style="animation-duration:{n(11 + 1.7 * (i % 3))}s" d="{onde(largeur, 8.5 if len(voies) <= 3 else 5.5, 31 + i)}"/></g>')
    return svg(f'montage {prefixe}', f'0 0 480 {n(boite_h)}', LIBELLES['bci'], f'''
<defs><clipPath id="{prefixe}-fenetre"><rect x="92" y="{haut_traces - 20}" width="{largeur}" height="{n(pas * len(voies) + 24)}"/></clipPath></defs>
<g filter="url(#trait)">
{t(f'M{cx + r} {cy} A{r} {r} 0 1 1 {cx + r} {n(cy - .4)}', 'gras')}
{t(f'M{cx - 15} {cy - r + 4} L{cx} {cy - r - 17} L{cx + 15} {cy - r + 4}', '', .2)}
{t(f'M{cx - r + 1} {cy - 17} q-13 17 0 34', '', .3)}{t(f'M{cx + r - 1} {cy - 17} q13 17 0 34', '', .3)}
<path class="fin pale tirets f" d="M{cx} {cy - r} L{cx} {cy + r} M{cx - r} {cy} L{cx + r} {cy}"/>
<circle class="fin pale tirets f" cx="{cx}" cy="{cy}" r="{r / 2}"/>
<g class="f">{reperes}</g>
{''.join(electrodes)}
</g>
<g class="f" style="--d:.9s">{''.join(noms)}</g>
<g class="traces f" style="--d:1.1s" clip-path="url(#{prefixe}-fenetre)">{''.join(traces)}</g>''')


# ------------------------------------------------------------------ théorie de la simulation
def simulation(bits: str = '') -> str:
    def point(i: float, j: float, k: float) -> tuple[float, float]:
        return 240 + (i - j) * 72, 218 + (i + j - 2) * 36 - (k - 1) * 84

    aretes = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for di, dj, dk in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                    if i + di < 3 and j + dj < 3 and k + dk < 3:
                        (x1, y1), (x2, y2) = point(i, j, k), point(i + di, j + dj, k + dk)
                        aretes.append(t(f'M{n(x1)} {n(y1)} L{n(x2)} {n(y2)}', 'fin pale', .012 * len(aretes)))
    noeuds = ''.join(f'<circle class="plein" cx="{n(x)}" cy="{n(y)}" r="2.7"/>'
                     for x, y in (point(i, j, k) for i in range(3) for j in range(3) for k in range(3)))
    source, bout_arete, bout_diagonale = point(0, 2, 0), point(2, 2, 0), point(2, 0, 2)
    arete = f'M{n(source[0])} {n(source[1])} L{n(bout_arete[0])} {n(bout_arete[1])}'
    diagonale = f'M{n(source[0])} {n(source[1])} L{n(bout_diagonale[0])} {n(bout_diagonale[1])}'
    ruban = (f'<text class="ruban-bits f" x="240" y="446" text-anchor="middle" textLength="372" lengthAdjust="spacing">'
             f'{html.escape(bits[:46])}</text>') if bits else ''
    return svg('simulation', '0 0 480 480', LIBELLES['simulation'], f'''
<g filter="url(#trait)">{''.join(aretes)}<g class="f" style="--d:.5s">{noeuds}</g>
{t(arete, 'gras', .9)}{t(diagonale, 'or gras', 1.1)}
<circle class="papier" cx="{n(source[0])}" cy="{n(source[1])}" r="6.5"/></g>
<circle class="plein voyageur" r="4"><animateMotion dur="5s" repeatCount="indefinite" path="{arete}"/></circle>
<circle class="or-plein voyageur" r="4"><animateMotion dur="5s" repeatCount="indefinite" path="{diagonale}"/></circle>
{ruban}''')
