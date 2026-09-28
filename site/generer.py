#!/usr/bin/env python3
"""Construit public/ : le site aeternam dans chaque langue.

Les textes sont dans site/langues/<code>.py (le français est la source) ; les
nombres viennent de recherche/2026-09-28-grille-lhaaso/resultats.json et sont
écrits selon les conventions de chaque langue. Une traduction n'est acceptée que
si elle garde exactement les mêmes nombres, formules et structure que la source.

Usage : python3 site/generer.py                  construit toutes les langues
        python3 site/generer.py --verifier de    vérifie seulement une traduction
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
import math
import re
import shutil
from collections import Counter
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
SITE = RACINE / 'site'
PUBLIC = RACINE / 'public'
ETUDE = RACINE / 'recherche' / '2026-09-28-grille-lhaaso'
DOMAINE = 'https://www.aeternam.org'
LANGUES = ('fr', 'en', 'es', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'ar')
SOURCE = 'fr'
DEFAUT = 'en'                  # pour les langues non traduites
ARTICLE = '/test-1/'
FICHIERS = '/fichiers/test-1/'
KATEX = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/'

MARQUEUR = re.compile(r'\[\[([a-z0-9_]+)\]\]')
FORMULE = re.compile(r'\$\$.+?\$\$|\\\(.+?\\\)', re.S)
BLOCS = ('h2', 'h3', 'p', 'ul', 'ol', 'li', 'table', 'tr', 'th', 'td', 'pre', 'section')
ATTRIBUTS = re.compile(r'\s(id|href|class)="([^"]*)"')
MOINS, FINE = '−', ' '
CLES_UI = ('devise', 'description_site', 'fichier_pdf')
CLES_ARTICLE = ('titre', 'description', 'date', 'corps')


def charger(code: str):
    chemin = SITE / 'langues' / f'{code}.py'
    spec = importlib.util.spec_from_file_location(f'langue_{code}', chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ecrire_nombre(valeur: float, genre: str, precision: int, decimale: str) -> str:
    if genre == 'sci':
        e = math.floor(math.log10(abs(valeur)))
        m = round(valeur / 10 ** e, precision - 1)
        if abs(m) >= 10:
            m, e = m / 10, e + 1
        mantisse = f'{m:.{precision - 1}f}'.replace('.', decimale)
        puissance = f'10<sup>{str(e).replace("-", MOINS)}</sup>'
        corps = puissance if mantisse == '1' else f'{mantisse}{FINE}×{FINE}{puissance}'
    elif genre == 'fix':
        corps = f'{valeur:.{precision}f}'.replace('.', decimale).replace('-', MOINS)
    elif genre == 'ent':
        corps = str(round(valeur))
    else:
        raise ValueError(genre)
    return f'<bdi>{corps}</bdi>'


def racine_sur_puissance(c: float) -> float:
    """Le nombre dont c serait la « racine » prise sur la seule puissance de dix (7,5e-8 -> 7,5e-16)."""
    e = math.floor(math.log10(c))
    return c / 10 ** e * 10.0 ** (2 * e)


def table_des_nombres(r: dict) -> dict[str, tuple[float, str, int]]:
    b = r['bornes_temps_continu']
    ccf, mi, ca = b['CCF'], b['ML_MINOS'], b['ML_calibre']
    t = r['temps_discret_methode_prudente']
    p26, p27, p28, ppl = r['predictions_non_mesurees']
    x = r['audit_xi_shu']
    beane = r['comparaison_beane_2012']['b_max_m']
    n = {
        'a_resume': (ccf['a_max_pire_orientation_m'], 'sci', 2),
        'a_ml_resume': (mi['a_max_pire_orientation_m'], 'sci', 2),
        'echelle_resume': (ccf['echelle_min_GeV'], 'sci', 2),
        'b_beane': (beane, 'sci', 2),
        'a95_sigma1': (t[4]['a_max_95pct_orientations_m'], 'sci', 2),
        'a_lineaire': (r['artefact_lineaire']['a_max_m_coefficient_1'], 'sci', 2),
        'facteur_planck': (r['maille_de_Planck']['facteur_sous_la_limite_prudente'], 'sci', 1),
        'facteur_planck_exact': (r['maille_de_Planck']['facteur_sous_la_limite_prudente'], 'sci', 2),
        'z': (r['constantes']['z'], 'fix', 3),
        'epl': (r['constantes']['E_Pl_GeV'], 'sci', 3),
        'h0': (r['constantes']['H0_km_s_Mpc'], 'fix', 2),
        'om': (r['constantes']['Omega_m'], 'fix', 3),
        'ol': (1 - r['constantes']['Omega_m'], 'fix', 3),
        'i2': (r['integrales_s']['I2'], 'sci', 3),
        'retard_limite': (r['retard_a_la_limite_1TeV_0p3TeV_s'], 'fix', 2),
        'e_bas': (0.3, 'fix', 1),
        'lpl': (r['constantes']['l_Pl_m'], 'sci', 2),
        'q_mediane': (r['orientation']['Q_mediane'], 'fix', 3),
        'q_5': (r['orientation']['Q_5pct'], 'fix', 3),
        'ccf_mediane': (t[0]['a_max_orientation_mediane_m'], 'sci', 3),
        'comobile_facteur': (r['maille_comobile']['facteur_sur_la_borne'], 'fix', 3),
        'comobile_a': (r['maille_comobile']['a_max_pire_orientation_m'], 'sci', 2),
        'validite': (r['validite_developpement']['a_E_sur_hbar_c'], 'sci', 2),
        'ak_test': (r['validite_developpement']['ak_test'], 'fix', 2),
        'ecart_dispersion': (r['validite_developpement']['ecart_relatif_max_developpement'], 'sci', 1),
        'beane_ratio': (ccf['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'beane_ml_min': (ca['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'beane_ml_max': (mi['a_max_pire_orientation_m'] / beane, 'fix', 2),
        'q_cal_axe': (ca['haut'] / p27['eta2_max'], 'fix', 2),
        'xs_facteur': (x['imprime_sur_coherent'], 'fix', 1),
        'xs_eqg_imprime': (x['EQG2_GeV_imprime_tableau_III'], 'sci', 2),
        'xs_rapport_lhaaso': (x['imprime_sur_LHAASO'], 'ent', 0),
        'xs_c1_imprime': (x['n1_constante_imprimee_eq6'], 'fix', 1),
        'xs_c1': (x['n1_constante_recalculee'], 'fix', 2),
        'xs_c2_imprime': (x['n2_constante_imprimee_eq7_sur_theta2'], 'sci', 2),
        'xs_theta': (x['theta2_limite_s_par_TeV2'], 'fix', 3),
        'xs_eq7': (x['EQG2_GeV_avec_eq7_imprimee'], 'sci', 3),
        'xs_c2': (x['n2_constante_coherente_sur_racine_theta2'], 'sci', 2),
        'xs_eqg': (x['EQG2_GeV_coherent_avec_eq3'], 'sci', 3),
        'xs_eps2': (x['n2_eps2_fois_theta2_recalcule'], 'sci', 3),
        'xs_eps2_imprime': (racine_sur_puissance(x['n2_constante_imprimee_eq7_sur_theta2']), 'sci', 2),
        'xs_vs_lhaaso': (x['coherent_sur_LHAASO'], 'fix', 1),
    }
    for nom, ligne in (('ccf', ccf), ('min', mi), ('cal', ca)):
        n[f'{nom}_bas'] = (ligne['bas'], 'fix', 2)
        n[f'{nom}_haut'] = (ligne['haut'], 'fix', 2)
        if ligne['meilleur'] is not None:
            n[f'{nom}_bf'] = (ligne['meilleur'], 'fix', 2)
        n[f'{nom}_arq'] = (ligne['a_racine_Q_max_m'], 'sci', 3)
        n[f'{nom}_pire'] = (ligne['a_max_pire_orientation_m'], 'sci', 3)
        n[f'{nom}_95'] = (ligne['a_max_95pct_orientations_m'], 'sci', 3)
        n[f'{nom}_ech'] = (ligne['echelle_min_GeV'], 'sci', 2)
    for i, ligne in enumerate(t):
        n[f's{i}_sigma'] = (ligne['sigma_courant'], 'fix', 2 if i == 3 else 1)
        n[f's{i}_cdt'] = (ligne['c_dt_sur_a'], 'fix', 3)
        if ligne['a_max_pire_orientation_m'] is not None:
            n[f's{i}_pire'] = (ligne['a_max_pire_orientation_m'], 'sci', 3)
        n[f's{i}_95'] = (ligne['a_max_95pct_orientations_m'], 'sci', 3)
        n[f's{i}_med'] = (ligne['a_max_orientation_mediane_m'], 'sci', 3)
    for nom, ligne, prec_eta, prec_ret, echelle_ret in (
            ('p26', p26, ('fix', 1), ('fix', 1), 1), ('p27', p27, ('fix', 2), ('fix', 2), 1),
            ('p28', p28, ('fix', 4), ('fix', 2), 1e3), ('pl', ppl, ('sci', 2), ('sci', 2), 1)):
        n[f'{nom}_eta_min'] = (ligne['eta2_min'], *prec_eta)
        n[f'{nom}_eta_max'] = (ligne['eta2_max'], *prec_eta)
        n[f'{nom}_ret_min'] = (ligne['retard_1TeV_0p3TeV_s_min'] * echelle_ret, *prec_ret)
        n[f'{nom}_ret_max'] = (ligne['retard_1TeV_0p3TeV_s_max'] * echelle_ret, *prec_ret)
    return n


def empreinte(texte: str) -> dict:
    """Ce qu'une traduction doit conserver à l'identique."""
    balises = Counter(re.findall(r'<(' + '|'.join(BLOCS) + r')[\s>]', texte))
    return {
        'marqueurs': Counter(MARQUEUR.findall(texte)),
        'formules': Counter(FORMULE.findall(texte)),
        'balises': balises,
        'attributs': Counter(ATTRIBUTS.findall(texte)),
    }


def verifier(code: str, source, module) -> list[str]:
    erreurs = []
    for nom in ('NOM', 'HTML_LANG', 'HREFLANG', 'DIR', 'LOCALE_OG', 'DECIMALE', 'UI', 'ARTICLE'):
        if not hasattr(module, nom):
            erreurs.append(f'{code} : {nom} manquant')
    if erreurs:
        return erreurs
    for cle in CLES_UI:
        if not module.UI.get(cle):
            erreurs.append(f'{code} : UI[{cle!r}] manquant')
    for cle in CLES_ARTICLE:
        if not module.ARTICLE.get(cle):
            erreurs.append(f'{code} : ARTICLE[{cle!r}] manquant')
    if erreurs:
        return erreurs
    ref, trad = empreinte(source.ARTICLE['corps']), empreinte(module.ARTICLE['corps'])
    for aspect in ref:
        if ref[aspect] != trad[aspect]:
            manque = ref[aspect] - trad[aspect]
            surplus = trad[aspect] - ref[aspect]
            erreurs.append(f'{code} : {aspect} différents ; manquants {dict(manque)} ; en trop {dict(surplus)}')
    for cle in CLES_UI + ('titre', 'description', 'date'):
        texte = module.UI.get(cle) or module.ARTICLE.get(cle)
        if MARQUEUR.search(texte or ''):
            erreurs.append(f'{code} : marqueur inattendu dans {cle}')
    return erreurs


def remplir(texte: str, nombres: dict, module, extras: dict) -> str:
    def un(m):
        nom = m.group(1)
        if nom in extras:
            return extras[nom]
        valeur, genre, precision = nombres[nom]
        return ecrire_nombre(valeur, genre, precision, module.DECIMALE)
    return MARQUEUR.sub(un, texte)


def alternatives(chemin: str) -> str:
    lignes = [f'<link rel="alternate" hreflang="{MODULES[c].HREFLANG}" href="{DOMAINE}/{c}{chemin}">'
              for c in LANGUES_ACTIVES]
    lignes.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAINE}{chemin}">')
    return '\n'.join(lignes)


def page(code: str, module, chemin: str, titre: str, description: str, contenu: str,
         classe: str, maths: bool) -> str:
    katex = ''
    if maths:
        katex = (f'<link rel="stylesheet" href="{KATEX}katex.min.css" crossorigin="anonymous">\n'
                 f'<script defer src="{KATEX}katex.min.js" crossorigin="anonymous"></script>\n'
                 f'<script defer src="{KATEX}contrib/auto-render.min.js" crossorigin="anonymous" '
                 "onload=\"renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},"
                 "{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false})\"></script>\n")
    barre = '' if classe == 'accueil' else f'<div class="barre"><a class="marque" href="/{code}/">aeternam</a></div>\n'
    return f'''<!doctype html>
<html lang="{module.HTML_LANG}" dir="{module.DIR}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{DOMAINE}/{code}{chemin}">
{alternatives(chemin)}
<meta property="og:title" content="{html.escape(titre)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{DOMAINE}/{code}{chemin}">
<meta property="og:locale" content="{module.LOCALE_OG}">
<meta name="theme-color" content="#0a0a0c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{katex}</head>
<body class="{classe}">
{barre}{contenu}
</body>
</html>
'''


def accueil(code: str, module) -> str:
    a = module.ARTICLE
    contenu = f'''<main>
<h1>aeternam</h1>
<p class="devise">{module.UI['devise']}</p>
<section class="travaux">
<a class="travail" href="/{code}{ARTICLE}"><span class="titre">{a['titre']}</span><span class="date">{a['date']}</span></a>
</section>
</main>'''
    return page(code, module, '/', 'aeternam', module.UI['description_site'], contenu, 'accueil', False)


def article(code: str, module, nombres: dict) -> str:
    a, ui = module.ARTICLE, module.UI
    extras = {'pdf': ui['fichier_pdf']}
    corps = remplir(a['corps'], nombres, module, extras)
    contenu = f'''<main>
<header>
<h1>{a['titre']}</h1>
<p class="sous-titre">{a['description']}</p>
<p class="meta">{a['date']}</p>
</header>
{corps}
</main>'''
    return page(code, module, ARTICLE, f"{a['titre']} — aeternam", a['description'], contenu, 'article', True)


def racine() -> str:
    """Repli statique si la fonction de langue ne répond pas : choix par le navigateur."""
    liens = ''.join(f'<li><a href="/{c}/" lang="{MODULES[c].HTML_LANG}">{MODULES[c].NOM}</a></li>'
                    for c in LANGUES_ACTIVES)
    codes = json.dumps(list(LANGUES_ACTIVES))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>aeternam</title>
{alternatives('/')}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
<script>(function(){{var codes={codes},prefs=(navigator.languages||[navigator.language||'']);
for(var i=0;i<prefs.length;i++){{var c=(prefs[i]||'').toLowerCase().split('-')[0];
if(codes.indexOf(c)>=0){{location.replace('/'+c+'/');return;}}}}location.replace('/{DEFAUT}/');}})();</script>
</head>
<body class="accueil"><main><h1>aeternam</h1><ul class="choix">{liens}</ul></main></body>
</html>
'''


def plan_du_site() -> str:
    urls = []
    for chemin in ('/', ARTICLE):
        alt = ''.join(f'<xhtml:link rel="alternate" hreflang="{MODULES[c].HREFLANG}" href="{DOMAINE}/{c}{chemin}"/>'
                      for c in LANGUES_ACTIVES)
        for c in LANGUES_ACTIVES:
            urls.append(f'<url><loc>{DOMAINE}/{c}{chemin}</loc>{alt}</url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n')


def construire() -> None:
    nombres = table_des_nombres(json.loads((ETUDE / 'resultats.json').read_text(encoding='utf-8')))
    source = MODULES[SOURCE]
    inconnus = set(empreinte(source.ARTICLE['corps'])['marqueurs']) - set(nombres) - {'pdf'}
    if inconnus:
        raise SystemExit(f'marqueurs sans valeur : {sorted(inconnus)}')
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    (PUBLIC / FICHIERS.strip('/')).mkdir(parents=True)
    for nom in ('style.css', 'favicon.svg'):
        shutil.copy(SITE / nom, PUBLIC / nom)
    for nom in ('analyse.py', 'resultats.json'):
        shutil.copy(ETUDE / nom, PUBLIC / FICHIERS.strip('/') / nom)
    for code in LANGUES_ACTIVES:
        module = MODULES[code]
        dossier = PUBLIC / code
        (dossier / ARTICLE.strip('/')).mkdir(parents=True)
        (dossier / 'index.html').write_text(accueil(code, module), encoding='utf-8')
        (dossier / ARTICLE.strip('/') / 'index.html').write_text(article(code, module, nombres), encoding='utf-8')
    (PUBLIC / 'index.html').write_text(racine(), encoding='utf-8')
    (PUBLIC / 'sitemap.xml').write_text(plan_du_site(), encoding='utf-8')
    (PUBLIC / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {DOMAINE}/sitemap.xml\n', encoding='utf-8')
    routes = {'version': 1, 'include': ['/', ARTICLE.rstrip('/'), ARTICLE + '*'], 'exclude': []}
    (PUBLIC / '_routes.json').write_text(json.dumps(routes, indent=2) + '\n', encoding='utf-8')
    print(f'public/ construit : {", ".join(LANGUES_ACTIVES)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--verifier', metavar='CODE', help='vérifie une traduction sans construire')
    args = parser.parse_args()
    disponibles = [c for c in LANGUES if (SITE / 'langues' / f'{c}.py').exists()]
    MODULES = {c: charger(c) for c in disponibles}
    if args.verifier:
        problemes = verifier(args.verifier, MODULES[SOURCE], MODULES[args.verifier])
        print('\n'.join(problemes) or f'{args.verifier} : conforme à la source')
        raise SystemExit(1 if problemes else 0)
    problemes = [e for c in disponibles if c != SOURCE for e in verifier(c, MODULES[SOURCE], MODULES[c])]
    if problemes:
        raise SystemExit('\n'.join(problemes))
    LANGUES_ACTIVES = tuple(disponibles)
    construire()
