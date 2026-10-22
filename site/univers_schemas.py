"""Schémas explicatifs : compositions exactes, géométrie illustrative hors échelle.

Les couleurs distinguent les objets nommés, jamais la charge de couleur des quarks.
Les tracés ne sont ni des observations ni des simulations microscopiques.
"""
from html import escape
from math import cos, sin, pi
from random import Random


def texte(x, y, valeur, classe='schema-label', ancre='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{ancre}" class="{classe}">{escape(valeur)}</text>'


def cercle(x, y, rayon, classe, lettre=''):
    return (f'<circle cx="{x}" cy="{y}" r="{rayon}" class="{classe}"/>'
            + (texte(x, y + 1, lettre, 'schema-symbole') if lettre else ''))


def trajet(points, classe='schema-trait', fleche=False):
    return f'<polyline points="{points}" class="{classe}"' + (' marker-end="url(#fleche-schema)"' if fleche else '') + '/>'


def inflation():
    pieces = []
    for cx, taille in ((145, 45), (435, 105)):
        for i in (-1, 0, 1):
            pieces.append(trajet(f'{cx-taille},{190+i*taille} {cx+taille},{190+i*taille}', 'schema-grille'))
            pieces.append(trajet(f'{cx+i*taille},{190-taille} {cx+i*taille},{190+taille}', 'schema-grille'))
            for j in (-1, 0, 1):
                pieces.append(cercle(cx+i*taille, 190+j*taille, 5, 'schema-point'))
    pieces += [trajet('232,190 283,190', fleche=True),
               texte(145, 330, 'Avant'), texte(435, 330, 'Après'),
               texte(300, 385, 'Les distances s’étirent.', 'schema-note')]
    return ''.join(pieces)


def particules():
    points = [(90,145,'u'),(215,110,'d'),(355,170,'u'),(495,115,'d'),
              (135,285,'d'),(275,240,'u'),(460,280,'u')]
    pieces = []
    for x,y,lettre in points:
        pieces.append(cercle(x,y,23,'schema-up' if lettre == 'u' else 'schema-down',lettre))
    for x,y,angle in [(170,180,.4),(340,290,-.5),(430,57,.05),(55,230,.15)]:
        pts = []
        for n in range(65):
            t=n/64*68; onde=sin(t*.55)*7
            pts.append(f'{x+t*cos(angle)-onde*sin(angle):.1f},{y+t*sin(angle)+onde*cos(angle):.1f}')
        pieces.append(trajet(' '.join(pts),'schema-gluon'))
    pieces += [texte(165,50,'Quarks'),trajet('165,65 165,85 201,97'),
               texte(475,355,'Gluons'),trajet('465,330 420,330 405,275'),
               texte(170,385,'u : up · d : down','schema-note')]
    return ''.join(pieces)


def protons():
    pieces = []
    for cx, lettres, titre in ((165,('u','u','d'),'Proton'),(435,('u','d','d'),'Neutron')):
        pieces.append(cercle(cx,175,92,'schema-enveloppe'))
        for (dx,dy),lettre in zip(((-35,-24),(35,-24),(0,42)),lettres):
            pieces.append(cercle(cx+dx,175+dy,29,'schema-up' if lettre == 'u' else 'schema-down',lettre))
        pieces.append(texte(cx,312,titre))
    pieces.append(texte(300,373,'u : quark up · d : quark down','schema-note'))
    return ''.join(pieces)


def noyaux():
    pieces = [cercle(155,177,36,'schema-up','p⁺')]
    for dx,dy,proton in ((-28,-28,True),(28,-28,False),(-28,28,False),(28,28,True)):
        pieces.append(cercle(435+dx,177+dy,35,'schema-up' if proton else 'schema-down','p⁺' if proton else 'n'))
    pieces += [texte(155,302,'Hydrogène'),texte(435,302,'Hélium 4'),
               texte(300,373,'p⁺ : proton · n : neutron','schema-note')]
    return ''.join(pieces)


def plasma():
    pieces = [trajet('40,195 130,155 220,260 320,125 435,240 563,183','schema-lumiere',True)]
    for x,y in ((130,155),(220,260),(320,125),(435,240)):
        pieces.append(cercle(x,y,16,'schema-down','−'))
    pieces += [cercle(480,80,24,'schema-up','p⁺'),cercle(130,300,24,'schema-up','p⁺'),
               texte(170,55,'Électrons libres'),trajet('175,73 175,105 143,142'),
               texte(342,360,'Lumière diffusée','schema-label schema-or')]
    return ''.join(pieces)


def atomes():
    return f'''<defs><radialGradient id="nuage-hydrogene">
<stop offset="0" stop-color="#a9c2ff" stop-opacity=".32"/>
<stop offset=".45" stop-color="#a9c2ff" stop-opacity=".17"/>
<stop offset="1" stop-color="#a9c2ff" stop-opacity="0"/></radialGradient></defs>
<circle cx="265" cy="188" r="132" fill="url(#nuage-hydrogene)"/>
{cercle(265,188,23,'schema-up','p⁺')}
{texte(160,48,'Nuage électronique')}{trajet('150,68 150,114 186,150')}
{texte(478,115,'Noyau')}{trajet('480,133 377,133 284,176')}
{trajet('45,321 554,321','schema-lumiere',True)}
{texte(300,374,'Lumière libre','schema-label schema-or')}'''


def soleil():
    random = Random(4627)
    pieces = []
    for r in (108,164,226):
        pieces.append(f'<ellipse cx="300" cy="195" rx="{r}" ry="{r*.32}" class="schema-grille"/>')
    for _ in range(340):
        r=random.uniform(68,230); a=random.random()*2*pi
        x=300+cos(a)*r; y=195+sin(a)*r*.32+random.uniform(-5,5)
        pieces.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{random.uniform(.8,2):.1f}" class="schema-poussiere"/>')
    pieces += [cercle(300,195,33,'schema-soleil'),cercle(457,223,9,'schema-planete'),cercle(184,165,6,'schema-planete'),
               texte(135,67,'Jeune Soleil'),trajet('135,85 215,85 280,166'),
               texte(452,115,'Planètes en formation'),trajet('455,135 491,161 462,213'),
               texte(393,342,'Gaz et poussières'),trajet('421,320 478,286 488,232')]
    return ''.join(pieces)


SCHEMAS = {
    'inflation': (inflation, 'Une même portion d’espace avant et après une expansion.', 'Les mêmes repères sont plus éloignés. Illustration de l’hypothèse inflationnaire, sans durée ni facteur mesuré.'),
    'particules': (particules, 'Quarks et gluons dans le plasma primordial.', 'Des quarks up et down sont représentés séparément, accompagnés de gluons. Ce sont des exemples, sans proportion ni trajectoire mesurées.'),
    'protons': (protons, 'Composition en quarks de valence du proton et du neutron.', 'Proton : deux quarks up et un down. Neutron : un up et deux down. Les gluons et les paires quark-antiquark ne sont pas dessinés.'),
    'noyaux': (noyaux, 'Les noyaux de l’hydrogène et de l’hélium 4.', 'Hydrogène ordinaire : un proton. Hélium 4 : deux protons et deux neutrons. Les abondances ne sont pas représentées.'),
    'plasma': (plasma, 'La lumière est diffusée par les électrons libres.', 'Les changements de direction du trajet lumineux coïncident avec les électrons. Les distances entre rencontres sont schématiques.'),
    'atomes': (atomes, 'Un atome neutre et la propagation libre de la lumière.', 'L’atome d’hydrogène est figuré par un proton et un nuage électronique, sans orbite d’électron. Le trait indique une lumière qui traverse le milieu.'),
    'systeme-solaire': (soleil, 'La formation du Soleil et des planètes dans un disque.', 'Un jeune Soleil est entouré d’un disque de gaz et de poussières, avec des planètes en formation. Les dimensions ne sont pas proportionnelles.'),
}


def schema(identifiant):
    if identifiant not in SCHEMAS:
        return ''
    dessiner, titre, description = SCHEMAS[identifiant]
    # Le marqueur possède un identifiant propre à la figure, y compris sans JS.
    dessin = dessiner().replace('url(#fleche-schema)', f'url(#fleche-{identifiant})')
    return f'''<figure class="univ-schema" data-schema="{identifiant}">
<svg viewBox="0 0 600 410" role="img" aria-labelledby="titre-schema-{identifiant} desc-schema-{identifiant}">
<title id="titre-schema-{identifiant}">{escape(titre)}</title><desc id="desc-schema-{identifiant}">{escape(description)}</desc>
<defs><marker id="fleche-{identifiant}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 1 1 L 8 5 L 1 9" fill="none" stroke="#dfc58f" stroke-width="1.3"/></marker></defs>
{dessin}</svg><figcaption>Schéma · hors échelle</figcaption></figure>'''
