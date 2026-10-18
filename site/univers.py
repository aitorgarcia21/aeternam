"""Composition de l'accueil : l'Univers, l'espace-temps, le cerveau, les frontières, puis les articles.
Le texte complet reste présent sans JavaScript."""
from html import escape
from langues.univers_fr import (ELECTRODES, ETAPES, ETAPES_CERVEAU, EXPERIENCES, OUVERTURE_CERVEAU,
                                SOURCES, SOURCES_CERVEAU)
from univers_schemas import schema
from univers_illustrations import illustration

CHAPITRES = (('histoire', 'Univers'), ('espace-temps', 'Relativité'), ('cerveau', 'Cerveau'),
             ('frontieres', 'Frontières'), ('articles', 'Articles'))
FLECHE = ('<svg class="fleche" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">'
          '<path d="M5 19 19 5M5 5h14v14" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" '
          'stroke-linejoin="round"/></svg>')


def source(cle):
    nom, url = {**SOURCES, **SOURCES_CERVEAU}[cle]
    return f'<a href="{url}">{nom}</a>'


def etape_univers(i, e):
    paragraphes = ''.join(f'<p>{p}</p>' for p in e['texte'])
    return f'''<article class="univ-etape" id="{e['id']}" data-scene="{i}" data-legende="{escape(e['legende'])}">
<div class="univ-texte"><h2>{e['titre']}</h2><p class="univ-date">{e['date']}</p>
<p class="univ-resume">{e['resume']}</p>
<details><summary>Analyse détaillée</summary>{paragraphes}<p>{e['detail']}</p>
{schema(e['id'])}<p class="univ-source">{source(e['source'])}</p></details></div>{illustration(e['id'])}</article>'''


def nombre(n: int) -> str:
    return f'{n:,}'.replace(',', ' ')


def controles_electrodes():
    """Le curseur règle le côté de la grille ; l'affichage donne le nombre d'électrodes."""
    e = ELECTRODES
    reperes = ''.join(f'<button type="button" data-field="electrodes" data-value="{cote}" aria-pressed="false">'
                      f'{nombre(cote * cote)}</button>' for cote in e['reperes'])
    return (f'<div class="univ-controles univ-controles-etape"><label for="electrodes">Électrodes '
            f'<output id="val-electrodes">{nombre(e["depart"] ** 2)}</output>'
            f'<input id="electrodes" type="range" min="{e["min"]}" max="{e["max"]}" step="1" value="{e["depart"]}"></label>'
            f'<div class="univ-presets" role="group" aria-label="Nombre d’électrodes à comparer">{reperes}</div>'
            f'<p class="univ-precision">{e["precision"]}</p></div>')


def etape_cerveau(e, sujets):
    paragraphes = ''.join(f'<p>{p}</p>' for p in e['texte'])
    sources = ' · '.join(source(cle) for cle in e['sources'])
    question = e.get('question', False)
    resume = f'<p class="{"univ-reponse" if question else "univ-resume"}">{e["resume"]}</p>'
    suite = ''.join(f'<p class="univ-suite"><a href="{sujets[cle]["chemin"]}"><span>{escape(sujets[cle]["titre"])}</span>{FLECHE}</a></p>'
                    for cle in e.get('sujets', ()))
    return f'''<article class="univ-etape{' univ-etape-question' if question else ''}" id="{e['id']}" data-scene="{e['scene']}" data-legende="{escape(e['legende'])}">
<div class="univ-texte"><h2>{e['titre']}</h2>
{resume}{controles_electrodes() if e['id'] == 'vision' else ''}
<details><summary>Analyse détaillée</summary>{paragraphes}{e.get('complement', '')}
<p class="univ-source">{sources}</p></details>{suite}</div></article>'''


def contenu(articles: str, sujets: dict) -> str:
    courant = ' aria-current="location"'
    chapitres = ''.join(f'<a href="#{cle}"{courant if i == 0 else ""}>{nom}</a>' for i, (cle, nom) in enumerate(CHAPITRES))
    univers = ''.join(etape_univers(i, e) for i, e in enumerate(ETAPES))
    cerveau = ''.join(etape_cerveau(e, sujets) for e in ETAPES_CERVEAU)
    references = ''.join(f'<li><a href="{url}">{nom}</a></li>' for nom, url in {**SOURCES, **SOURCES_CERVEAU}.values())
    o = OUVERTURE_CERVEAU
    return f'''<main>
<nav class="univ-sommaire" aria-label="Chapitres">
<div class="univ-chapitres">{chapitres}</div>
<button id="univ-motion" type="button" aria-pressed="false" aria-label="Figer les animations" title="Figer les animations" hidden><span class="univ-motion-icon" aria-hidden="true"></span></button>
</nav>
<section id="histoire" class="univ-histoire" data-scene-intro="12" aria-label="Histoire de l’Univers">
<div class="univ-scenes"><div class="univ-scene-fixe">
<canvas class="cosmos-canvas" aria-hidden="true"></canvas><canvas id="cosmos-overlay" class="cosmos-overlay" aria-hidden="true"></canvas>
<div class="univ-art-layer"></div><p class="cosmos-legende" data-defaut="Illustration · hors échelle">Illustration · hors échelle</p>
</div></div>
<div class="univ-etapes">
<article class="univ-ouverture" id="apercu"><div class="univ-texte">
<h2>13,8 milliards<br><span>d’années d’évolution.</span></h2>
<p>En se dilatant, l’Univers se refroidit et la matière s’organise.</p>
</div>{illustration('apercu')}</article>
{univers}</div>
</section>
{EXPERIENCES}
<section id="cerveau" class="univ-histoire univ-histoire-cerveau" data-scene-intro="{o['scene']}" aria-label="Le cerveau et les frontières">
<div class="univ-scenes"><div class="univ-scene-fixe">
<canvas class="cosmos-canvas" aria-hidden="true"></canvas><canvas id="cerveau-overlay" class="cosmos-overlay" aria-hidden="true"></canvas>
<div class="univ-art-layer"></div><p class="cosmos-legende" data-defaut="Schéma · hors échelle">{escape(o['legende'])}</p>
</div></div>
<div class="univ-etapes">
<article class="univ-ouverture" id="du-cosmos-au-cerveau" data-legende="{escape(o['legende'])}"><div class="univ-texte">
<h2>{o['titre']}</h2>
<p>{o['texte']}</p>
</div></article>
{cerveau}</div>
</section>
<section id="articles" class="univ-articles" aria-labelledby="titre-articles">
<h2 id="titre-articles">Les articles.</h2>
<div class="univ-articles-themes">{articles}</div>
</section>
<section id="sources-univers" class="univ-sources" aria-labelledby="titre-sources">
<h2 id="titre-sources">Sources et modèles.</h2>
<div><p>Scènes illustratives et schémas hors échelle. Dates approximatives.</p>
<details><summary>Références scientifiques</summary>
<p>Les scènes de l’histoire cosmique associent des vues d’artiste générées avec ImageGen, des animations procédurales et des schémas. Elles ne sont ni des photographies ni une simulation de l’Univers. Les couleurs, lumières et textures servent à expliquer ; elles ne montrent pas l’apparence mesurée des particules. L’espacement des chapitres n’est pas proportionnel aux durées. Les dates sont approximatives.</p>
<p>Les scènes du cerveau sont des schémas procéduraux. Elles ne montrent ni des neurones observés, ni des enregistrements, ni le fonctionnement d’une interface réelle ; le passage de la toile cosmique au réseau de neurones est une transition de mise en scène.</p>
<p>Les expériences de relativité calculent les rapports de durée et une géodésique dans les modèles indiqués. Les repères qui ressemblent à une grille n’impliquent pas que l’espace soit réellement un quadrillage.</p>
<ul>{references}</ul></details>
<p><a href="/sujets/">Tous les thèmes</a> · <a href="/recherches/">Tous les articles</a> · <a href="/a-propos/">La démarche</a></p></div>
</section>
</main>'''
