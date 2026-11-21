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


# ------------------------------------------------------------------ la scène de l'accueil
# Le risque de mourir selon l'âge, hors échelle : y = (e^(k·u) − 1) / (e^K − 1), u de 0 à 1.
# K = 4,2 : la courbe d'aujourd'hui, qui monte de plus en plus vite. Retarder la décale de
# SCENE_DECALE vers la droite ; ralentir fait descendre k vers SCENE_K_FIN. site/accueil/accueil.js
# refait ces tracés au défilement, avec les mêmes nombres.
SCENE_X0, SCENE_X1, SCENE_BAS, SCENE_HAUT = 64, 530, 410, 70
SCENE_K, SCENE_K_FIN, SCENE_DECALE = 4.2, 2.6, 88


def risque(u: float, k: float = SCENE_K) -> float:
    return SCENE_BAS - (SCENE_BAS - SCENE_HAUT) * (math.exp(k * u) - 1) / (math.exp(SCENE_K) - 1)


def courbe_risque(k: float = SCENE_K, decale: float = 0.0, pas: int = 80) -> str:
    longueur = SCENE_X1 - SCENE_X0
    fin = (longueur - decale) / longueur
    return chemin([(SCENE_X0, SCENE_BAS)] + [(SCENE_X0 + decale + longueur * fin * i / pas, risque(fin * i / pas, k))
                                             for i in range(pas + 1)])


def _cellules(cx: float, cy: float, memoires: int, graine: int) -> str:
    """Quatorze lymphocytes dans une goutte : les premiers tirés sont « mémoire » (pleins)."""
    hasard = random.Random(graine)
    places: list[tuple[float, float]] = []
    while len(places) < 14:
        r, a = 92 * math.sqrt(hasard.random()), hasard.uniform(0, 2 * math.pi)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if all(math.hypot(x - u, y - v) > 38 for u, v in places):
            places.append((x, y))
    return ''.join(
        f'<g class="cellule a{" memoire" if i < memoires else ""}">'
        f'<circle class="corps" cx="{n(x)}" cy="{n(y)}" r="15"/><circle class="noyau" cx="{n(x + 2)}" cy="{n(y - 1)}" r="5.5"/></g>'
        for i, (x, y) in enumerate(places))


def _membrane(cx: float, cy: float, rx: float, ry: float, pas: int = 120) -> str:
    """Le contour d'une cellule : une ellipse un peu irrégulière, comme tracée à la main."""
    points = []
    for i in range(pas):
        a = 2 * math.pi * i / pas
        f = 1 + .035 * math.sin(3 * a + .4) + .025 * math.cos(5 * a + 1.3) + .015 * math.sin(7 * a)
        points.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
    return chemin(points, True)


def _helice(x0: float, x1: float, y: float, signe: int) -> str:
    """Un brin de la double hélice de l'ADN, entre x0 et x1."""
    return chemin([(x, y + signe * 9 * math.sin(2 * math.pi * (x - 252) / 30)) for x in range(int(x0), int(x1) + 1, 2)])


def _mito(cx: float, cy: float, angle: float) -> str:
    return (f'<g class="a k-mito" transform="translate({cx} {cy}) rotate({angle})"><ellipse rx="30" ry="13"/>'
            '<path class="fin" d="M-21 0 L-14 -7 L-7 7 L0 -7 L7 7 L14 -7 L21 0"/></g>')


def _amas(cx: float, cy: float) -> str:
    grains = ((0, 0, 6), (10, -4, 5), (-9, 5, 5.5), (4, 10, 4.5), (-6, -9, 4), (13, 7, 4))
    return '<g class="a k-amas">' + ''.join(f'<circle class="plein" cx="{cx + dx}" cy="{cy + dy}" r="{r}"/>'
                                            for dx, dy, r in grains) + '</g>'


def _bezier(p0, p1, p2, p3, x: float) -> float:
    """L'ordonnée d'une courbe de Bézier cubique à l'abscisse x (abscisses croissantes)."""
    bas, haut = 0.0, 1.0
    for _ in range(60):
        t = (bas + haut) / 2
        xt = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        bas, haut = (t, haut) if xt < x else (bas, t)
    return (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]


def scene() -> str:
    """Le schéma de la scène de l'accueil, en quatre tableaux qui se succèdent au défilement
    (site/accueil/accueil.js) : la courbe du risque (humain, sans montée, hydre, retarder,
    ralentir) ; une cellule et ce qui s'y abîme ; l'âge biologique qui redescend dans l'embryon ;
    deux gouttes de sang. Rien n'est à l'échelle, rien n'est une mesure."""
    x0, x1, bas, haut = SCENE_X0, SCENE_X1, SCENE_BAS, SCENE_HAUT
    longueur = x1 - x0
    y_retarde = risque((longueur - SCENE_DECALE) / longueur)
    y_ralenti = risque(1, SCENE_K_FIN)

    def droite(ident: str, y: float, cle: str, classe: str = '') -> str:
        return f'<text id="{ident}" class="a nom {classe}" x="{x1 + 12}" y="{n(y + 4.5)}">{LIBELLES[cle]}</text>'

    def dessus(ident: str, cle: str, classe: str = '') -> str:
        return f'<text id="{ident}" class="a nom {classe}" x="{x1}" y="{bas - 12}" text-anchor="end">{LIBELLES[cle]}</text>'

    def axes(gauche: str, droite_: str) -> str:
        return (f'<g filter="url(#trait)"><path class="fin pale" d="M{x0 - 8} {haut - 10} L{x0 - 8} {bas + 10} L{x1 + 4} {bas + 10}"/></g>'
                f'<text class="nom" x="{x0 - 8}" y="{haut - 24}">{gauche}</text>'
                f'<text class="nom" x="{x1 + 4}" y="{bas + 36}" text-anchor="end">{droite_}</text>')

    courbe = f'''<g id="scene-courbe">
{axes(LIBELLES['pente_risque'], LIBELLES['pente_age'])}
<g filter="url(#trait2)">
<path id="c-plat" class="a or fin tirets-longs" clip-path="url(#plat-clip)" d="M{x0} {bas} L{x1} {bas}"/>
<path id="c-hydre" class="trace or gras" pathLength="1" d="M{x0} {bas} L{x1} {bas}"/>
<path id="c-fantome" class="a fin pale tirets-longs" d="{courbe_risque()}"/>
<path id="c-ralentir" class="a or gras" d="{courbe_risque()}"/>
<path id="c-humain" class="trace gras" pathLength="1" d="{courbe_risque()}"/>
</g>
<circle id="p-dix" class="a or-plein" cx="{x0}" cy="{bas}" r="5.5"/>
<text id="n-dix" class="a nom or" x="{x0}" y="{bas + 36}" text-anchor="middle">{LIBELLES['scene_dix']}</text>
{droite('n-humain', haut, 'scene_humain', 'clair')}
{dessus('n-plat', 'scene_plat', 'or')}
{dessus('n-hydre', 'scene_hydre', 'or')}
{droite('n-retarder', y_retarde, 'scene_retarder', 'clair')}
{droite('n-ralentir', y_ralenti, 'scene_ralentir', 'or')}
</g>'''

    # La cellule ; ses noms au-dessus d'elle, chacun relié à ce qu'il nomme par un trait fin.
    adn = ''.join(f'<path d="{_helice(a, b, 250, s)}"/>' for a, b in ((252, 290), (302, 340)) for s in (1, -1))
    noms_cellule = ''.join(
        f'<g class="a k-nom"><path class="fin pale" d="M{x} 88 L{cible[0]} {cible[1]}"/>'
        f'<text class="nom clair" x="{x}" y="76" text-anchor="middle">{LIBELLES[cle]}</text></g>'
        for x, cible, cle in ((150, (188, 186), 'cellule_proteines'), (300, (298, 236), 'cellule_adn'), (470, (448, 200), 'cellule_mito')))
    cellule = f'''<g id="scene-cellule">
<g filter="url(#trait)"><path id="k-membrane" class="trace gras" pathLength="1" d="{_membrane(320, 262, 190, 150)}"/>
<circle id="k-noyau" class="trace" pathLength="1" cx="296" cy="250" r="62"/>
<g id="k-adn" class="a">{adn}</g>
<path id="k-casse" class="a or" d="M291 236 L285 226 M301 264 L307 274"/>
{_mito(448, 214, -24)}{_mito(430, 334, 18)}{_mito(192, 334, 32)}
{_amas(196, 194)}{_amas(366, 380)}</g>
{noms_cellule}
</g>'''

    v = ((x0 + 6, 236), (108, 300), (136, 386), (172, 386)), ((172, 386), (236, 386), (392, 262), (x1, 124))
    y_saut = _bezier(*v[1], 440)
    embryon = f'''<g id="scene-embryon">
{axes(LIBELLES['embryon_age'], LIBELLES['embryon_temps'])}
<g filter="url(#trait2)">
<path id="e-courbe" class="trace gras" pathLength="1" d="M{v[0][0][0]} {v[0][0][1]} C{v[0][1][0]} {v[0][1][1]} {v[0][2][0]} {v[0][2][1]} {v[0][3][0]} {v[0][3][1]} C{v[1][1][0]} {v[1][1][1]} {v[1][2][0]} {v[1][2][1]} {v[1][3][0]} {v[1][3][1]}"/>
<path id="e-saut" class="trace or" pathLength="1" d="M440 {n(y_saut + 10)} L440 374 M432 362 L440 375 L448 362"/>
</g>
<path id="e-zero-ligne" class="a fin or tirets" d="M172 394 L172 {bas + 10}"/>
<circle id="e-zero" class="a or-plein" cx="172" cy="386" r="6"/>
<circle id="e-adulte" class="a plein" cx="440" cy="{n(y_saut)}" r="5"/>
<text id="n-zero" class="a nom or" x="172" y="{bas + 36}" text-anchor="middle">{LIBELLES['embryon_zero']}</text>
<text id="n-facteurs" class="a nom or" x="452" y="{n((y_saut + 374) / 2 + 4)}">{LIBELLES['embryon_facteurs']}</text>
</g>'''

    gouttes = ((176, LIBELLES['sang_volonte'], 9, 11), (464, LIBELLES['sang_restriction'], 5, 23))
    sang_ = ''.join(f'<circle class="trace goutte" pathLength="1" cx="{cx}" cy="230" r="116"/>'
                    f'<text class="nom clair" x="{cx}" y="388" text-anchor="middle">{nom}</text>'
                    f'{_cellules(cx, 230, memoires, graine)}' for cx, nom, memoires, graine in gouttes)
    legende = (f'<g class="cellule"><circle class="corps" cx="214" cy="62" r="9"/></g>'
               f'<text class="nom" x="230" y="66.5">{LIBELLES["sang_naif"]}</text>'
               f'<g class="cellule memoire"><circle class="corps" cx="372" cy="62" r="9"/></g>'
               f'<text class="nom" x="388" y="66.5">{LIBELLES["sang_memoire"]}</text>')
    sang = f'<g id="scene-sang"><g filter="url(#trait)">{sang_}</g><g class="sang-legende">{legende}</g></g>'

    return svg('scene', '0 0 640 480', LIBELLES['scene'],
               f'<defs><clipPath id="plat-clip"><rect id="plat-rect" x="{x0 - 8}" y="{bas - 30}" width="0" height="60"/></clipPath></defs>'
               f'{courbe}{cellule}{embryon}{sang}')


# ------------------------------------------------------------------ l'expérience à financer
def experience() -> str:
    """L'expérience des cellules T (recherche/2026-11-21-restriction-cellules/protocole.md) :
    trois régimes à partir de 6 mois, deux prises de sang à 16 et 28 mois. Les pentes entre les
    deux prises sont l'hypothèse, pas un résultat ; les niveaux sont hors échelle."""
    x0, bas, haut = 70, 320, 70
    mois = lambda m: 110 + (m - 6) * 450 / 22
    depart = 292
    groupes = ((248, 118, '', ''), (257, 170, 'pale', ''), (267, 214, 'or', 'or'))
    traits, points, noms = '', '', ''
    for i, ((y16, y28, classe, couleur), nom) in enumerate(zip(groupes, LIBELLES['exp_groupes'])):
        traits += f'<path class="f fin tirets {classe}" style="--d:{n(.5 + .15 * i)}s" d="M{n(mois(6))} {depart} L{n(mois(16))} {y16}"/>'
        traits += t(f'M{n(mois(16))} {y16} L{n(mois(28))} {y28}', f'gras {classe}', 1.1 + .25 * i)
        plein = 'or-plein' if couleur else 'plein'
        points += ''.join(f'<circle class="f {plein}{" pale" if classe == "pale" else ""}" style="--d:{n(1 + .25 * i)}s" cx="{n(x)}" cy="{y}" r="4.5"/>'
                          for x, y in ((mois(16), y16), (mois(28), y28)))
        noms += f'<text class="f nom {couleur}" style="--d:{n(1.9 + .25 * i)}s" x="{n(mois(28) + 16)}" y="{y28 + 4.5}">{nom}</text>'
    graduations = ''.join(f'<path class="fin" d="M{n(mois(m))} {bas} L{n(mois(m))} {bas + 7}"/>'
                          f'<text class="nom" x="{n(mois(m))}" y="{bas + 30}" text-anchor="middle">{LIBELLES["exp_mois"].format(m)}</text>'
                          for m in (6, 16, 28))
    goutte = lambda x: (f'<path class="f or-plein" style="--d:.8s" d="M{n(x)} {bas + 44} C{n(x + 8)} {bas + 55} {n(x + 8)} {bas + 63} '
                        f'{n(x)} {bas + 63} C{n(x - 8)} {bas + 63} {n(x - 8)} {bas + 55} {n(x)} {bas + 44} Z"/>')
    return svg('experience', '0 0 720 400', LIBELLES['experience'], f'''
<g filter="url(#trait)">{t(f'M{x0} {haut - 18} L{x0} {bas} L{n(mois(28) + 34)} {bas}', 'fin')}{graduations}
{traits}</g>
{points}{goutte(mois(16))}{goutte(mois(28))}
<text class="f nom" style="--d:.8s" x="{n((mois(16) + mois(28)) / 2)}" y="{bas + 60}" text-anchor="middle">{LIBELLES['exp_sang']}</text>
<text class="nom" x="{x0}" y="{haut - 32}">{LIBELLES['exp_part']}</text>
{noms}''')


# ------------------------------------------------------------------ vieillir
def vieillir() -> str:
    """Le risque de mourir selon l'âge : la courbe qui monte de plus en plus vite, et la droite
    de qui ne vieillit pas. Un schéma, sans échelle : les mesures sont dans les articles."""
    x0, x1, bas, haut, k = 96, 412, 384, 96, 4.2
    courbe = [(x0 + (x1 - x0) * i / 60, bas - 12 - (bas - haut - 12) * (math.exp(k * i / 60) - 1) / (math.exp(k) - 1))
              for i in range(61)]
    graduations = ''.join(f'<path class="fin" d="M{n(x0 + i * (x1 - x0) / 6)} {bas + 4} L{n(x0 + i * (x1 - x0) / 6)} {bas + 10}"/>'
                          for i in range(7))
    return svg('vieillir', '0 0 480 480', LIBELLES['vieillir'], f'''
<g filter="url(#trait)">{t(f'M{x0 - 4} {haut - 12} L{x0 - 4} {bas + 4} L{x1 + 12} {bas + 4}', 'fin')}{graduations}
{t(chemin(courbe), 'gras', .3)}
{t(f'M{x0} {bas - 12} L{x1} {bas - 12}', 'or gras', .9)}</g>
<text class="nom" x="{x1 - 22}" y="{haut + 4}" text-anchor="end">{LIBELLES['vieillir_risque']}</text>
<text class="nom" x="{x1}" y="{bas - 24}" text-anchor="end">{LIBELLES['vieillir_sans']}</text>''')


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
