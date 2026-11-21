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

LANGUE = 'fr'


def T(fr: str, en: str) -> str:
    return en if LANGUE == 'en' else fr


def _mois() -> tuple[str, ...]:
    return T(('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août',
              'septembre', 'octobre', 'novembre', 'décembre'),
             ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'))


def _dec(texte: str) -> str:
    """Écrit un nombre déjà formaté avec un point décimal selon la langue (virgule en français)."""
    return texte.replace('.', ',') if LANGUE != 'en' else texte


def _pct(texte: str) -> str:
    """Pourcentage en HTML : « 12,3&nbsp;% » en français, « 12.3% » en anglais."""
    return _dec(texte) + T('&nbsp;%', '%')


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
        titre = T(f"{l['energy']} EeV, {d.day} {_mois()[d.month - 1]} {d.year}",
                  f"{l['energy']} EeV, {_mois()[d.month - 1]} {d.day}, {d.year}")
        points.append(f'<g class="evt"><title>{html.escape(titre)}</title>'
                      f'<circle class="cible" cx="{_f(x)}" cy="{_f(y)}" r="12"/>'
                      f'<circle class="point" cx="{_f(x)}" cy="{_f(y)}" r="4.5"/></g>')
    morceaux.extend(points)
    label = T(f'Carte du ciel en coordonnées équatoriales des {len(lignes)} rayons cosmiques les plus '
              f'énergétiques enregistrés par l’observatoire Pierre Auger.',
              f'Sky map in equatorial coordinates of the {len(lignes)} most energetic cosmic rays '
              f'recorded by the Pierre Auger Observatory.')
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
    return (grille_bits(reels, colonnes, T(f'{n} bits tirés de photons intriqués', f'{n} bits drawn from entangled photons')),
            grille_bits(simple, colonnes, T(f'{n} bits d’un registre à décalage de degré 7',
                                            f'{n} bits from a degree-7 shift register')), n)


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
    etiquettes = (f'<text class="lib" x="{_f((a1[0] + a2[0]) / 2)}" y="{_f(a2[1] + 34)}" text-anchor="middle">{T("arête", "edge")}</text>'
                  f'<text class="lib" x="{_f(d2[0] - 18)}" y="{_f(d2[1] - 14)}" text-anchor="end">{T("grande diagonale", "main diagonal")}</text>')
    # Cadre : tous les points, plus la place des étiquettes.
    xs = [p(i, j, k)[0] for i in (0, N - 1) for j in (0, N - 1) for k in (0, N - 1)]
    ys = [p(i, j, k)[1] for i in (0, N - 1) for j in (0, N - 1) for k in (0, N - 1)]
    x0, x1 = min(xs) - 20, max(xs) + 30
    y0, y1 = min(ys) - 56, max(ys) + 50
    return (f'<svg class="reseau" viewBox="{_f(x0)} {_f(y0)} {_f(x1 - x0)} {_f(y1 - y0)}" role="img" '
            f'aria-label="{T("Réseau cubique : une arête et une grande diagonale", "Cubic lattice: one edge and one main diagonal")}">'
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
        txt = {0: '1', 1: '10', -1: _dec('0.1')}.get(e, f'10{sup}')
        morceaux.append(f'<text class="axe" x="{_f(xe)}" y="{_f(H - 8)}" text-anchor="middle">{txt}</text>')
    x1 = x(1.0)
    morceaux.append(f'<line class="unite" x1="{_f(x1)}" y1="24" x2="{_f(x1)}" y2="{_f(H - 30)}"/>')
    for i, (lib, v, cls) in enumerate(lignes):
        y = 40 + pas * i
        xa, xb = sorted((x1, x(v)))
        valeur = (f'{v:,.0f}'.replace(',', T('\u202f', ',')) if v >= 10
                  else _dec(f'{v:.2f}'.rstrip('0').rstrip('.')))
        morceaux.append(f'<g class="{cls}"><title>{html.escape(lib)} : × {valeur}</title>'
                        f'<text class="lib" x="{_f(g - 14)}" y="{_f(y + h / 2 + 5)}" text-anchor="end">{html.escape(lib)}</text>'
                        f'<rect x="{_f(xa)}" y="{_f(y + 6)}" width="{_f(max(xb - xa, 2))}" height="{_f(h - 12)}" rx="3"/>'
                        f'<text class="val" x="{_f(max(xb, x1) + 8)}" y="{_f(y + h / 2 + 5)}">× {valeur}</text></g>')
    label = T('Facteur d’accélération du temps vécu : nécessaire contre mesuré, échelle logarithmique',
              'Speed-up factor of experienced time: needed versus measured, logarithmic scale')
    return (f'<svg class="facteurs" viewBox="0 0 {int(L)} {int(H)}" role="img" aria-label="{label}">'
            + ''.join(morceaux) + '</svg>')


# ------------------------------------------------------------------ programme onirique
def _axes() -> tuple[tuple[str, str, str], ...]:
    return (
        ('acces', T('Accéder', 'Access'), T('Entrer en relation avec le rêve.', 'Establish contact with the dream.')),
        ('contenu', T('Orienter', 'Steer'), T('Retrouver un thème, un lieu, une histoire.', 'Find a theme, a place, a story.')),
        ('temps', T('Étendre', 'Extend'), T('Mesurer le temps de l’expérience.', 'Measure the time of the experience.')),
        ('memoire', T('Se souvenir', 'Remember'), T('Relier les épisodes après le réveil.', 'Link the episodes after waking.')),
    )


def parcours_recherche() -> str:
    liens = ''.join(f'<li><a href="/programme/#{cle}"><span class="noeud-axe" aria-hidden="true">{i}</span>'
                    f'<span class="nom-axe">{nom}</span><span class="detail-axe">{detail}</span></a></li>'
                    for i, (cle, nom, detail) in enumerate(_axes(), 1))
    return (f'<nav class="parcours" aria-label="{T("Les cinq axes de recherche", "The five research axes")}">'
            f'<ol class="axes">{liens}</ol>'
            '<a class="axe-calcul" href="/programme/#calcul"><span aria-hidden="true">5</span>'
            f'<span>{T("Calculer et vérifier", "Compute and verify")}<small>'
            f'{T("La méthode commune aux quatre capacités.", "The method shared by the four capabilities.")}</small></span></a></nav>')


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
        titre=T(f'{total} réveils : {present} durées renseignées, {total-present} manquantes. Un point par réveil.',
                f'{total} awakenings: {present} durations reported, {total-present} missing. One dot per awakening.')
        images.append(_svg_stats(w,h,titre,''.join(points),compact))
    bins=d['effectifs_classes_duree']
    categories=[T('0–5 secondes', '0–5 seconds'), T('Plus de 5–10 secondes', 'Over 5–10 seconds'),
                T('Plus de 10 secondes–1 minute', 'Over 10 seconds–1 minute'),
                T('Plus de 1–10 minutes', 'Over 1–10 minutes'), T('Plus de 10 minutes–1 heure', 'Over 10 minutes–1 hour'),
                T('Plus d’une heure', 'Over one hour')]
    lignes=''.join(f'<tr><td>{lib}</td><td>{bins[str(i)]}</td></tr>' for i,lib in enumerate(categories,1))
    return (f'<figure class="figure-recherche" id="figure-dream"><h4>{T("287 réveils. 124 durées déclarées.", "287 awakenings. 124 reported durations.")}</h4>'
            f'<div class="legende-points"><span><i class="plein" aria-hidden="true"></i>{T(f"{present} renseignées", f"{present} reported")}</span>'
            f'<span><i class="creux" aria-hidden="true"></i>{T(f"{total-present} manquantes", f"{total-present} missing")}</span></div>'
            +''.join(images)+
            '<figcaption>'
            + T('Un point = un réveil. Les points sont regroupés par disponibilité, sans ordre chronologique. '
                'Les durées manquantes restent manquantes ; elles ne valent pas zéro. ',
                'One dot = one awakening. Dots are grouped by availability, not in chronological order. '
                'Missing durations stay missing; they do not count as zero. ')
            + '<a href="https://doi.org/10.26180/23306054.v3">' + T('Données DREAM, série Tononi', 'DREAM data, Tononi series')
            + '</a>.</figcaption></figure>'
            + f'<details class="detail-donnees"><summary>{T("Voir les classes des 124 durées déclarées", "View the classes of the 124 reported durations")}</summary>'
            f'<div class="tableau"><table><thead><tr><th>{T("Classe déclarée", "Reported class")}</th><th>{T("Réveils", "Awakenings")}</th></tr></thead>'
            f'<tbody>{lignes}</tbody></table></div></details>')


def monte_carlo_tableaux(r: dict) -> dict:
    conditions = r['scenarios']['empirique']['conditions']
    noms = {'niveau_initial': T('Sans bruit ajouté', 'No added noise'),
            'bruit_ajoute': T('Bruit ajouté, sans correction', 'Added noise, uncorrected'),
            'reference': T('Correction par référence', 'Correction using a reference'),
            'attenuation': T('Atténuation supposée', 'Assumed attenuation'),
            'reference_contaminee': T('Référence contaminée', 'Contaminated reference')}
    lignes = []
    for cle, libelle in noms.items():
        n = conditions[cle]['minimum_budget_gain']
        valeur = str(n) if n is not None else T('Non atteint sur la grille', 'Not reached on the grid')
        reference = r['protocole']['observations_reference_non_etiquetees'] if cle.startswith('reference') else 0
        lignes.append(f'<tr><th scope="row">{libelle}</th><td>{valeur}</td><td>{reference}</td></tr>')
    seuils = (f'<div class="tableau"><table class="phrases"><caption>{T("Scénario empirique : premier budget testé satisfaisant le critère de gain moyen", "Empirical scenario: first tested budget meeting the mean-gain criterion")}</caption>'
              f'<thead><tr><th scope="col">{T("Condition simulée", "Simulated condition")}</th><th scope="col">{T("Essais étiquetés", "Labelled trials")}</th>'
              f'<th scope="col">{T("Observations de référence supplémentaires", "Additional reference observations")}</th></tr></thead><tbody>'
              + ''.join(lignes) + '</tbody></table></div>')
    lignes = []
    for i, n in enumerate(r['protocole']['budgets_etiquetes']):
        cellules = ''.join('<td>'+_pct(f'{100*conditions[k]["scores"]["moyenne"][i]:.1f}')+'</td>'
                           for k in ('niveau_initial', 'bruit_ajoute', 'reference'))
        lignes.append(f'<tr><th scope="row">{n}</th>{cellules}</tr>')
    scores = (f'<details class="detail-donnees"><summary>{T("Lire les scores moyens à chaque budget", "Read the mean scores at each budget")}</summary>'
              f'<div class="tableau"><table class="phrases"><caption>{T("Exactitude simulée, classes équilibrées", "Simulated accuracy, balanced classes")}</caption>'
              f'<thead><tr><th scope="col">{T("Essais étiquetés", "Labelled trials")}</th><th scope="col">{T("Sans bruit ajouté", "No added noise")}</th>'
              f'<th scope="col">{T("Bruit non corrigé", "Uncorrected noise")}</th><th scope="col">{T("Référence", "Reference")}</th></tr></thead><tbody>'
              + ''.join(lignes) + '</tbody></table></div></details>')
    return {'figure_mc_seuils': seuils, 'figure_mc_scores': scores}


def bci_tableau(r: dict) -> str:
    """Équivalent textuel des points du graphique, issu des mêmes résultats."""
    inconnus = r['evaluations']['personne_reservee']['par_personne']
    connus = {v['sujet']: v for v in r['evaluations']['run_reserve']['par_personne']}
    lignes = []
    for v in inconnus:
        def pourcent(score):
            return _pct(f'{100 * score:.1f}')
        lignes.append(f'<tr><th scope="row">S{v["sujet"]:03d}</th>'
                      f'<td>{pourcent(v["exactitude_equilibree"])}</td>'
                      f'<td>{pourcent(connus[v["sujet"]]["exactitude_equilibree"])}</td></tr>')
    return (f'<details class="detail-donnees"><summary>{T("Lire les scores de chaque personne", "Read each person’s scores")}</summary>'
            f'<div class="tableau"><table class="phrases"><caption>{T("Exactitude équilibrée (%)", "Balanced accuracy (%)")}</caption>'
            f'<thead><tr><th scope="col">{T("Personne", "Person")}</th><th scope="col">{T("Personne entière réservée", "Whole person held out")}</th>'
            f'<th scope="col">{T("Run réservé, même personne", "Run held out, same person")}</th></tr></thead>'
            '<tbody>' + ''.join(lignes) + '</tbody></table></div></details>')


def figure_faux_positifs(r: dict) -> str:
    lab=r['laboratoire_numerique']
    c=next(s for s in lab['scenarios'] if s['n_sujets']==40 and s['correlation_intra_sujet']==.6)
    valeurs=[(T('Chaque essai pris comme indépendant', 'Each trial treated as independent'),c['nul']['taux_rejet_naif_par_essai'],'comparaison'),
             (T('Une analyse par personne', 'One analysis per person'),c['nul']['taux_rejet_par_sujet'],'principal')]
    images=[]
    for compact,w in ((False,640),(True,360)):
        gauche,droite=12,w-38; echelle=(droite-gauche)/.12
        elements=[]
        for i,(lib,p,cls) in enumerate(valeurs):
            y=46+i*104; x=gauche+p*echelle
            err=1.96*math.sqrt(p*(1-p)/lab['simulations_par_scenario'])
            valeur=_dec(f'{100*p:.1f}')+T(' %', '%')
            elements += [f'<text class="label" x="12" y="{y-20}">{lib}</text>',
                         f'<rect class="{cls}" x="{gauche}" y="{y}" width="{p*echelle:.2f}" height="14"/>',
                         f'<path class="incertitude" d="M{x-err*echelle:.2f},{y+7} H{x+err*echelle:.2f} M{x-err*echelle:.2f},{y+2} v10 M{x+err*echelle:.2f},{y+2} v10"/>',
                         f'<text class="valeur" x="{x+err*echelle+7:.2f}" y="{y+34}">{valeur}</text>']
        ref=gauche*1+lab['alpha_unilateral']*echelle
        elements += [f'<line class="seuil" x1="{ref:.2f}" x2="{ref:.2f}" y1="35" y2="205"/>',
                     f'<text class="repere" x="{ref:.2f}" y="225" text-anchor="middle">{T("seuil 2,5 %", "threshold 2.5%")}</text>']
        for v in (0,.04,.08,.12):
            x=gauche+v*echelle
            elements.append(f'<text class="repere" x="{x:.2f}" y="253" text-anchor="middle">{100*v:.0f}{T(" %", "%")}</text>')
        images.append(_svg_stats(w,270,T('Simulation sans gain réel : 9,7 % de faux positifs par essai, 2,7 % par personne.', 'Simulation with no real gain: 9.7% false positives per trial, 2.7% per person.'), ''.join(elements),compact))
    return (f'<figure class="figure-recherche" id="figure-erreurs"><h4>{T("Un faux progrès peut venir de la méthode.", "False progress can come from the method.")}</h4>'
            f'<p class="contexte-figure">{T("Simulation numérique · Aucun gain réel dans le modèle.", "Numerical simulation · No real gain in the model.")}</p>'
            + ''.join(images) +
            '<figcaption>'
            + T('40 personnes simulées, trois mesures chacune, corrélation 0,6. '
                'Barres : taux de faux positifs sur 6 000 jeux ; traits : incertitude Monte-Carlo approximative à 95 %. '
                'Paramètres choisis pour éprouver la méthode, sans données humaines dans cette figure.',
                '40 simulated people, three measurements each, correlation 0.6. '
                'Bars: false-positive rate over 6,000 datasets; lines: approximate 95% Monte Carlo uncertainty. '
                'Parameters chosen to stress-test the method, with no human data in this figure.')
            + '</figcaption></figure>')


# ------------------------------------------------------------------ retarder ou ralentir
def points_doublement(r: dict, label: str, marques: list[tuple[float, str]] = ()) -> str:
    """Les traitements qui allongent la vie (recherche/2026-11-20-retarder-ou-ralentir) : pour
    chacun, le rapport λ des temps de doublement du risque, traitées sur témoins. Un point par
    traitement ; en couleur, la moyenne par cohorte et sexe et son intervalle à 95 % ; hachurée,
    la plage de λ qu'il faudrait si ces traitements ralentissaient le vieillissement.
    À l'arrivée de la figure, chaque point part de la valeur qu'il aurait s'il ralentissait
    (--dx, en unités du dessin) et rejoint sa valeur mesurée (site/accueil/accueil.css).
    `marques` : d'autres mesures du même rapport, chacune un losange et son libellé court, au-dessus
    des points (la restriction calorique, recherche/2026-11-21-piste-restriction) ; elles arrivent
    après la moyenne."""
    e = r['efficaces']
    x = lambda v: 40 + (v - 0.6) / 0.8 * 520
    rayon, ecart, places, points = 6.5, 15.0, [], []
    for i, c in enumerate(sorted(r['liste_efficaces'], key=lambda c: c['lambda_general'])):
        cx, k = x(c['lambda_general']), 0
        while True:                     # le premier étage libre autour de la ligne médiane
            cy = 104 + (k + 1) // 2 * ecart * (-1 if k % 2 else 1)
            if all((cx - px) ** 2 + (cy - py) ** 2 >= ecart ** 2 for px, py in places):
                break
            k += 1
        places.append((cx, cy))
        points.append(f'<circle class="pt" cx="{cx:.1f}" cy="{cy:.1f}" r="{rayon}" '
                      f'style="--dx: {x(c["lambda_ralentissement"]) - cx:.1f}; --d: {i * 0.03:.2f}s"/>')
    bas, haut = e['lambda_moyen_ic95']
    graduations = ''.join(
        f'<path class="fin" d="M{x(v):.1f} 220 L{x(v):.1f} 227"/>'
        f'<text class="grad" x="{x(v):.1f}" y="250" text-anchor="middle">{_dec(f"{v:.1f}")}</text>'
        for v in (0.6, 0.8, 1.0, 1.2, 1.4))
    return f'''<svg class="dessin d-doublement" viewBox="0 0 600 258" role="img" aria-label="{html.escape(label, quote=True)}">
<defs><pattern id="dbl-h" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line class="hach" x1="0" y1="0" x2="0" y2="7"/></pattern></defs>
<rect class="bande" x="{x(e['lambda_si_ralentissement_min']):.1f}" y="20" width="{x(e['lambda_si_ralentissement_max']) - x(e['lambda_si_ralentissement_min']):.1f}" height="200" fill="url(#dbl-h)" stroke="none"/>
<path class="fin" d="M40 220 L560 220"/>{graduations}
<path class="un" d="M{x(1):.1f} 20 L{x(1):.1f} 220"/>
{''.join(points)}
<path class="moy" d="M{x(bas):.1f} 198 L{x(haut):.1f} 198"/><circle class="moy-pt" cx="{x(e['lambda_moyen']):.1f}" cy="198" r="7.5"/>
{''.join(f'<path class="pt-r" d="M{x(v):.1f} 49 L{x(v) + 9:.1f} 58 L{x(v):.1f} 67 L{x(v) - 9:.1f} 58 Z"/>'
         f'<text class="lab-r" x="{x(v):.1f}" y="40" text-anchor="middle">{libelle}</text>' for v, libelle in marques)}
</svg>'''
