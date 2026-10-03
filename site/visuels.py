"""Visuels de l'accueil, dessinés en SVG au moment de la construction.

Chaque figure de données est tirée des fichiers publiés avec les études (aucune
valeur saisie à la main) : catalogue Auger pour la carte du ciel, bits bruts de
photons intriqués pour le hasard quantique. Bibliothèque standard uniquement.
"""
from __future__ import annotations

import csv
import datetime as dt
import html
import json
import math
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
AUGER = RACINE / 'recherche' / '2026-09-28-rayons-cosmiques'
HASARD = RACINE / 'recherche' / '2026-09-28-hasard-quantique'

MOIS = ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août',
        'septembre', 'octobre', 'novembre', 'décembre')


def _f(x: float) -> str:
    return f'{x:.1f}'.rstrip('0').rstrip('.')


# ------------------------------------------------------------------ carte du ciel
def _hammer(ra_deg: float, dec_deg: float) -> tuple[float, float]:
    """Projection de Hammer-Aitoff centrée sur 0 h, ascension droite croissante vers la gauche."""
    lon = math.radians(((ra_deg + 180.0) % 360.0) - 180.0)
    lat = math.radians(dec_deg)
    z = math.sqrt(1.0 + math.cos(lat) * math.cos(lon / 2.0))
    x = 2.0 * math.sqrt(2.0) * math.cos(lat) * math.sin(lon / 2.0) / z
    y = math.sqrt(2.0) * math.sin(lat) / z
    return -x, y


def evenements_auger() -> tuple[list[dict], dict]:
    r = json.loads((AUGER / 'resultats.json').read_text(encoding='utf-8'))
    ecartes = set(r['donnees']['ecartes_etalonnage'])
    with (AUGER / 'donnees' / 'auger_catalogSD.csv').open(encoding='utf-8') as f:
        lignes = [l for l in csv.DictReader(f) if l['id'] not in ecartes]
    assert len(lignes) == r['donnees']['n_evenements']
    return lignes, r


def carte_ciel() -> str:
    lignes, r = evenements_auger()
    dec_max = r['methode']['declinaison_max_visible_deg']
    L, H, M = 760.0, 400.0, 30.0                       # largeur, hauteur, marge
    ex = (L - 2 * M) / (4 * math.sqrt(2))              # échelle : x de -2√2 à 2√2
    ey = (H - 2 * M) / (2 * math.sqrt(2))

    def pt(ra, dec):
        x, y = _hammer(ra, dec)
        return L / 2 + ex * x, H / 2 - ey * y

    def trace(points):
        return 'M' + ' L'.join(f'{_f(x)},{_f(y)}' for x, y in points)

    morceaux = []
    # Ciel hors de vue d'Auger (déclinaison supérieure à la limite) : voile léger.
    bord = [pt(-179.999 + i * 359.998 / 180, dec_max) for i in range(181)]
    bord_d = [pt(180.001, dec_max + i * (90 - dec_max) / 30) for i in range(31)]
    bord_g = [pt(179.999, 90 - i * (90 - dec_max) / 30) for i in range(31)]
    morceaux.append(f'<path class="hors-vue" d="{trace(bord + bord_d + bord_g)} Z"/>')
    # Graticule : parallèles tous les 30°, méridiens toutes les 4 h, contour.
    for dec in (-60, -30, 0, 30, 60):
        morceaux.append(f'<path class="grille" d="{trace([pt(-179.999 + i * 2, dec) for i in range(180)])}"/>')
    for ra in (60, 120, 240, 300, 0):
        morceaux.append(f'<path class="grille" d="{trace([pt(ra, -90 + i) for i in range(181)])}"/>')
    contour = [pt(180.001, -90 + i) for i in range(181)] + [pt(179.999, 90 - i) for i in range(181)]
    morceaux.append(f'<path class="contour" d="{trace(contour)} Z"/>')
    # Repères de déclinaison, à gauche, et limite du ciel visible.
    for dec in (60, 30, 0, -30, -60):
        x, y = pt(179.999, dec)
        signe = '+' if dec > 0 else ('−' if dec < 0 else '')
        morceaux.append(f'<text class="repere" x="{_f(x - 8)}" y="{_f(y + 5)}" text-anchor="end">{signe}{abs(dec)}°</text>')
    xg, yg = pt(0, dec_max)
    morceaux.append(f'<path class="limite" d="{trace(bord)}"/>')
    # Les événements : un point par rayon cosmique, zone de survol élargie.
    points = []
    for l in sorted(lignes, key=lambda l: float(l['energy'])):
        x, y = pt(float(l['ra']), float(l['dec']))
        d = dt.datetime.fromtimestamp(int(l['utctime']), dt.timezone.utc)
        titre = f"{l['energy']} EeV, {d.day} {MOIS[d.month - 1]} {d.year}"
        points.append(f'<g class="evt"><title>{html.escape(titre)}</title>'
                      f'<circle class="cible" cx="{_f(x)}" cy="{_f(y)}" r="12"/>'
                      f'<circle class="point" cx="{_f(x)}" cy="{_f(y)}" r="4.5"/></g>')
    morceaux.extend(points)
    label = (f'Carte du ciel en coordonnées équatoriales des {len(lignes)} rayons cosmiques les plus '
             f'énergétiques enregistrés par l’observatoire Pierre Auger.')
    return (f'<svg class="carte" viewBox="0 0 {int(L)} {int(H)}" role="img" aria-label="{html.escape(label)}">'
            + ''.join(morceaux) + '</svg>')


# ------------------------------------------------------------------ hasard
def _bits_fichier(chemin: Path, n: int) -> list[int]:
    donnees = chemin.read_bytes()[: (n + 7) // 8]
    return [(octet >> (7 - k)) & 1 for octet in donnees for k in range(8)][:n]


def _lfsr(degre: int, taps: tuple[int, ...], n: int, graine: int = 1) -> list[int]:
    etat, sortie = graine, []
    for _ in range(n):
        sortie.append(etat & 1)
        bit = 0
        for t in taps:
            bit ^= (etat >> (degre - t)) & 1
        etat = (etat >> 1) | (bit << (degre - 1))
    return sortie


def grille_bits(bits: list[int], colonnes: int, etiquette: str) -> str:
    c, g = 6, 1                                          # côté d'une case, espace
    lignes = len(bits) // colonnes
    rects = ''.join(f'<rect x="{(i % colonnes) * (c + g)}" y="{(i // colonnes) * (c + g)}" width="{c}" height="{c}"/>'
                    for i, b in enumerate(bits) if b)
    return (f'<svg class="bits" viewBox="0 0 {colonnes * (c + g) - g} {lignes * (c + g) - g}" role="img" '
            f'aria-label="{html.escape(etiquette)}">{rects}</svg>')


def figures_hasard(colonnes: int = 64, lignes: int = 24) -> tuple[str, str, int]:
    n = colonnes * lignes
    reels = _bits_fichier(HASARD / 'donnees' / 'parity_qrng.bin', n)
    # Registre à décalage de degré 7 (x^7 + x^6 + 1), période 127 : un générateur simple.
    simple = _lfsr(7, (7, 6), n)
    return (grille_bits(reels, colonnes, f'{n} bits tirés de photons intriqués'),
            grille_bits(simple, colonnes, f'{n} bits d’un registre à décalage de degré 7'), n)


# ------------------------------------------------------------------ grille
def reseau() -> str:
    """Réseau cubique 4 × 4 × 4 en perspective cavalière, une arête et une grande diagonale."""
    N, pas = 4, 92.0
    kx, ky = 0.5 * pas * math.cos(math.radians(32)), 0.5 * pas * math.sin(math.radians(32))

    def p(i, j, k):                                      # i : x, j : profondeur, k : hauteur
        return i * pas + j * kx, -k * pas - j * ky

    traits, points = [], []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x, y = p(i, j, k)
                for di, dj, dk in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                    if i + di < N and j + dj < N and k + dk < N:
                        x2, y2 = p(i + di, j + dj, k + dk)
                        traits.append(f'<line class="maille" x1="{_f(x)}" y1="{_f(y)}" x2="{_f(x2)}" y2="{_f(y2)}"/>')
                points.append(f'<circle class="noeud" cx="{_f(x)}" cy="{_f(y)}" r="3"/>')
    a1, a2 = p(0, 0, 0), p(N - 1, 0, 0)
    d1, d2 = p(0, 0, 0), p(N - 1, N - 1, N - 1)

    def fleche(cls, depart, arrivee):
        (x1, y1), (x2, y2) = depart, arrivee
        return (f'<line class="{cls}" x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}" '
                f'marker-end="url(#pointe-{cls})"/>')

    defs = ''.join(f'<marker id="pointe-{c}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
                   f'orient="auto-start-reverse"><path class="{c}-pointe" d="M0,0 L10,5 L0,10 z"/></marker>'
                   for c in ('axe', 'diagonale'))
    etiquettes = (f'<text class="lib" x="{_f((a1[0] + a2[0]) / 2)}" y="{_f(a2[1] + 34)}" text-anchor="middle">arête</text>'
                  f'<text class="lib" x="{_f(d2[0] - 18)}" y="{_f(d2[1] - 14)}" text-anchor="end">grande diagonale</text>')
    # Cadre : tous les points, plus la place des étiquettes.
    xs = [p(i, j, k)[0] for i in (0, N - 1) for j in (0, N - 1) for k in (0, N - 1)]
    ys = [p(i, j, k)[1] for i in (0, N - 1) for j in (0, N - 1) for k in (0, N - 1)]
    x0, x1 = min(xs) - 20, max(xs) + 30
    y0, y1 = min(ys) - 56, max(ys) + 50
    return (f'<svg class="reseau" viewBox="{_f(x0)} {_f(y0)} {_f(x1 - x0)} {_f(y1 - y0)}" role="img" '
            f'aria-label="Réseau cubique : une arête et une grande diagonale">'
            f'<defs>{defs}</defs>{"".join(traits)}{"".join(points)}'
            f'{fleche("axe", a1, a2)}{fleche("diagonale", d1, d2)}{etiquettes}</svg>')


# ------------------------------------------------------------------ projet
def echelle_facteurs(lignes: list[tuple[str, float, str]], mini: float = 0.1, maxi: float = 1e7) -> str:
    """Barres horizontales sur une échelle logarithmique partant de 1 (même vitesse que l'horloge).

    lignes : (libellé, facteur, classe) ; classe « besoin » (ce qu'il faudrait) ou « mesure » (ce qu'on mesure).
    Une barre part de 1 vers la droite si le facteur accélère, vers la gauche s'il ralentit.
    """
    L, g, d, h, pas = 760.0, 300.0, 24.0, 34.0, 44.0
    H = 40 + pas * len(lignes) + 36
    a, b = math.log10(mini), math.log10(maxi)

    def x(v):
        return g + (L - g - d) * (math.log10(v) - a) / (b - a)

    morceaux = []
    for e in range(int(a), int(b) + 1):
        xe = x(10.0 ** e)
        morceaux.append(f'<line class="grille" x1="{_f(xe)}" y1="30" x2="{_f(xe)}" y2="{_f(H - 30)}"/>')
        sup = str(e).translate(str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹'))
        txt = {0: '1', 1: '10', -1: '0,1'}.get(e, f'10{sup}')
        morceaux.append(f'<text class="axe" x="{_f(xe)}" y="{_f(H - 8)}" text-anchor="middle">{txt}</text>')
    x1 = x(1.0)
    morceaux.append(f'<line class="unite" x1="{_f(x1)}" y1="24" x2="{_f(x1)}" y2="{_f(H - 30)}"/>')
    for i, (lib, v, cls) in enumerate(lignes):
        y = 40 + pas * i
        xa, xb = sorted((x1, x(v)))
        valeur = (f'{v:,.0f}'.replace(',', '\u202f') if v >= 10
                  else f'{v:.2f}'.rstrip('0').rstrip('.').replace('.', ','))
        morceaux.append(f'<g class="{cls}"><title>{html.escape(lib)} : × {valeur}</title>'
                        f'<text class="lib" x="{_f(g - 14)}" y="{_f(y + h / 2 + 5)}" text-anchor="end">{html.escape(lib)}</text>'
                        f'<rect x="{_f(xa)}" y="{_f(y + 6)}" width="{_f(max(xb - xa, 2))}" height="{_f(h - 12)}" rx="3"/>'
                        f'<text class="val" x="{_f(max(xb, x1) + 8)}" y="{_f(y + h / 2 + 5)}">× {valeur}</text></g>')
    label = 'Facteur d’accélération du temps vécu : nécessaire contre mesuré, échelle logarithmique'
    return (f'<svg class="facteurs" viewBox="0 0 {int(L)} {int(H)}" role="img" aria-label="{label}">'
            + ''.join(morceaux) + '</svg>')


# ------------------------------------------------------------------ programme onirique
AXES = (
    ('acces', 'Accéder', 'Entrer en relation avec le rêve.'),
    ('contenu', 'Orienter', 'Retrouver un thème, un lieu, une histoire.'),
    ('temps', 'Étendre', 'Mesurer le temps de l’expérience.'),
    ('memoire', 'Se souvenir', 'Relier les épisodes après le réveil.'),
)


def parcours_recherche() -> str:
    liens = ''.join(f'<li><a href="/programme/#{cle}"><span class="noeud-axe" aria-hidden="true">{i}</span>'
                    f'<span class="nom-axe">{nom}</span><span class="detail-axe">{detail}</span></a></li>'
                    for i, (cle, nom, detail) in enumerate(AXES, 1))
    return ('<nav class="parcours" aria-label="Les cinq axes de recherche">'
            f'<ol class="axes">{liens}</ol>'
            '<a class="axe-calcul" href="/programme/#calcul"><span aria-hidden="true">5</span>'
            '<span>Calculer et vérifier<small>La méthode commune aux quatre capacités.</small></span></a></nav>')


def _svg_stats(w, h, titre, contenu, compact=False):
    cls = 'compact' if compact else 'large'
    return (f'<svg class="viz {cls}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(titre)}">'
            f'<title>{html.escape(titre)}</title>{contenu}</svg>')


def figure_dream(r: dict) -> str:
    d = r['temps_dream']
    total, present = d['n_reveils'], d['n_durees']
    images = []
    for compact, w, cols, gap in ((False, 640, 41, 15), (True, 360, 21, 16)):
        rows = math.ceil(total/cols); top=30; h=top+rows*gap+16
        left=(w-(cols-1)*gap)/2
        points=[]
        for i in range(total):
            x=left+(i%cols)*gap; y=top+(i//cols)*gap
            cls='renseigne' if i<present else 'manquant'
            points.append(f'<circle class="{cls}" cx="{_f(x)}" cy="{_f(y)}" r="4.2"/>')
        titre=f'{total} réveils : {present} durées renseignées, {total-present} manquantes. Un point par réveil.'
        images.append(_svg_stats(w,h,titre,''.join(points),compact))
    bins=d['effectifs_classes_duree']
    categories=['0–5 secondes','Plus de 5–10 secondes','Plus de 10 secondes–1 minute',
                'Plus de 1–10 minutes','Plus de 10 minutes–1 heure','Plus d’une heure']
    lignes=''.join(f'<tr><td>{lib}</td><td>{bins[str(i)]}</td></tr>' for i,lib in enumerate(categories,1))
    return ('<figure class="figure-recherche" id="figure-dream"><h4>287 réveils. 124 durées déclarées.</h4>'
            f'<div class="legende-points"><span><i class="plein" aria-hidden="true"></i>{present} renseignées</span>'
            f'<span><i class="creux" aria-hidden="true"></i>{total-present} manquantes</span></div>'
            +''.join(images)+
            '<figcaption>Un point = un réveil. Les points sont regroupés par disponibilité, sans ordre chronologique. '
            'Les durées manquantes restent manquantes ; elles ne valent pas zéro. '
            '<a href="https://doi.org/10.26180/23306054.v3">Données DREAM, série Tononi</a>.</figcaption></figure>'
            '<details class="detail-donnees"><summary>Voir les classes des 124 durées déclarées</summary>'
            '<div class="tableau"><table><thead><tr><th>Classe déclarée</th><th>Réveils</th></tr></thead>'
            f'<tbody>{lignes}</tbody></table></div></details>')


def monte_carlo_tableaux(r: dict) -> dict:
    conditions = r['scenarios']['empirique']['conditions']
    noms = {'niveau_initial': 'Sans bruit ajouté', 'bruit_ajoute': 'Bruit ajouté, sans correction',
            'reference': 'Correction par référence', 'attenuation': 'Atténuation supposée',
            'reference_contaminee': 'Référence contaminée'}
    lignes = []
    for cle, libelle in noms.items():
        n = conditions[cle]['minimum_budget_gain']
        valeur = str(n) if n is not None else 'Non atteint sur la grille'
        reference = r['protocole']['observations_reference_non_etiquetees'] if cle.startswith('reference') else 0
        lignes.append(f'<tr><th scope="row">{libelle}</th><td>{valeur}</td><td>{reference}</td></tr>')
    seuils = ('<div class="tableau"><table class="phrases"><caption>Scénario empirique : premier budget testé satisfaisant le critère de gain moyen</caption>'
              '<thead><tr><th scope="col">Condition simulée</th><th scope="col">Essais étiquetés</th>'
              '<th scope="col">Observations de référence supplémentaires</th></tr></thead><tbody>'
              + ''.join(lignes) + '</tbody></table></div>')
    lignes = []
    for i, n in enumerate(r['protocole']['budgets_etiquetes']):
        cellules = ''.join('<td>'+f'{100*conditions[k]["scores"]["moyenne"][i]:.1f}'.replace('.', ',')+'&nbsp;%</td>'
                           for k in ('niveau_initial', 'bruit_ajoute', 'reference'))
        lignes.append(f'<tr><th scope="row">{n}</th>{cellules}</tr>')
    scores = ('<details class="detail-donnees"><summary>Lire les scores moyens à chaque budget</summary>'
              '<div class="tableau"><table class="phrases"><caption>Exactitude simulée, classes équilibrées</caption>'
              '<thead><tr><th scope="col">Essais étiquetés</th><th scope="col">Sans bruit ajouté</th>'
              '<th scope="col">Bruit non corrigé</th><th scope="col">Référence</th></tr></thead><tbody>'
              + ''.join(lignes) + '</tbody></table></div></details>')
    return {'figure_mc_seuils': seuils, 'figure_mc_scores': scores}


def bci_tableau(r: dict) -> str:
    """Équivalent textuel des points du graphique, issu des mêmes résultats."""
    inconnus = r['evaluations']['personne_reservee']['par_personne']
    connus = {v['sujet']: v for v in r['evaluations']['run_reserve']['par_personne']}
    lignes = []
    for v in inconnus:
        def pourcent(score):
            return f'{100 * score:.1f}'.replace('.', ',') + '&nbsp;%'
        lignes.append(f'<tr><th scope="row">S{v["sujet"]:03d}</th>'
                      f'<td>{pourcent(v["exactitude_equilibree"])}</td>'
                      f'<td>{pourcent(connus[v["sujet"]]["exactitude_equilibree"])}</td></tr>')
    return ('<details class="detail-donnees"><summary>Lire les scores de chaque personne</summary>'
            '<div class="tableau"><table class="phrases"><caption>Exactitude équilibrée (%)</caption>'
            '<thead><tr><th scope="col">Personne</th><th scope="col">Personne entière réservée</th>'
            '<th scope="col">Run réservé, même personne</th></tr></thead>'
            '<tbody>' + ''.join(lignes) + '</tbody></table></div></details>')


def figure_faux_positifs(r: dict) -> str:
    lab=r['laboratoire_numerique']
    c=next(s for s in lab['scenarios'] if s['n_sujets']==40 and s['correlation_intra_sujet']==.6)
    valeurs=[('Chaque essai pris comme indépendant',c['nul']['taux_rejet_naif_par_essai'],'comparaison'),
             ('Une analyse par personne',c['nul']['taux_rejet_par_sujet'],'principal')]
    images=[]
    for compact,w in ((False,640),(True,360)):
        gauche,droite=12,w-38; echelle=(droite-gauche)/.12
        elements=[]
        for i,(lib,p,cls) in enumerate(valeurs):
            y=46+i*104; x=gauche+p*echelle
            err=1.96*math.sqrt(p*(1-p)/lab['simulations_par_scenario'])
            valeur=f'{100*p:.1f}'.replace('.',',')+' %'
            elements += [f'<text class="label" x="12" y="{y-20}">{lib}</text>',
                         f'<rect class="{cls}" x="{gauche}" y="{y}" width="{p*echelle:.2f}" height="14"/>',
                         f'<path class="incertitude" d="M{x-err*echelle:.2f},{y+7} H{x+err*echelle:.2f} M{x-err*echelle:.2f},{y+2} v10 M{x+err*echelle:.2f},{y+2} v10"/>',
                         f'<text class="valeur" x="{x+err*echelle+7:.2f}" y="{y+34}">{valeur}</text>']
        ref=gauche*1+lab['alpha_unilateral']*echelle
        elements += [f'<line class="seuil" x1="{ref:.2f}" x2="{ref:.2f}" y1="35" y2="205"/>',
                     f'<text class="repere" x="{ref:.2f}" y="225" text-anchor="middle">seuil 2,5 %</text>']
        for v in (0,.04,.08,.12):
            x=gauche+v*echelle
            elements.append(f'<text class="repere" x="{x:.2f}" y="253" text-anchor="middle">{100*v:.0f} %</text>')
        images.append(_svg_stats(w,270,'Simulation sans gain réel : 9,7 % de faux positifs par essai, 2,7 % par personne.', ''.join(elements),compact))
    return ('<figure class="figure-recherche" id="figure-erreurs"><h4>Un faux progrès peut venir de la méthode.</h4>'
            '<p class="contexte-figure">Simulation numérique · Aucun gain réel dans le modèle.</p>'
            + ''.join(images) +
            '<figcaption>40 personnes simulées, trois mesures chacune, corrélation 0,6. '
            'Barres : taux de faux positifs sur 6 000 jeux ; traits : incertitude Monte-Carlo approximative à 95 %. '
            'Paramètres choisis pour éprouver la méthode, sans données humaines dans cette figure.</figcaption></figure>')
