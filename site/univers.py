"""Composition du parcours de l'accueil ; texte complet présent sans JavaScript."""
from html import escape
from langues.univers_fr import ETAPES, EXPERIENCES, SOURCES
from univers_schemas import schema
from univers_illustrations import illustration


def contenu():
    etapes = []
    for i, e in enumerate(ETAPES):
        nom, url = SOURCES[e['source']]
        paragraphes = ''.join(f'<p>{p}</p>' for p in e['texte'])
        etapes.append(f'''<article class="univ-etape" id="{e['id']}" data-etape="{i}" data-legende="{escape(e['legende'])}">
<div class="univ-texte"><h2>{e['titre']}</h2><p class="univ-date">{e['date']}</p>
<p class="univ-resume">{e['resume']}</p>
<details><summary>Analyse détaillée</summary>{paragraphes}<p>{e['detail']}</p>
{schema(e['id'])}<p class="univ-source"><a href="{url}">{nom}</a></p></details></div>{illustration(e['id'])}</article>''')
    sources = ''.join(f'<li><a href="{url}">{nom}</a></li>' for nom, url in SOURCES.values())
    return f'''<main>
<nav class="univ-sommaire" aria-label="Chapitres">
<a href="#histoire" aria-current="location">Univers</a>
<a href="#espace-temps">Relativité</a><a href="#avant-apres">Origines</a><a href="#sources-univers">Sources</a>
<button id="univ-motion" type="button" aria-pressed="false" aria-label="Figer les animations" title="Figer les animations" hidden><span class="univ-motion-icon" aria-hidden="true"></span></button>
</nav>
<section id="histoire" class="univ-histoire" aria-label="Histoire de l’Univers">
<div class="univ-scenes"><div class="univ-scene-fixe">
<canvas id="cosmos-canvas" aria-hidden="true"></canvas><canvas id="cosmos-overlay" aria-hidden="true"></canvas>
<div class="univ-art-layer"></div><p id="cosmos-legende">Illustration · hors échelle</p>
</div></div>
<div class="univ-etapes">
<article class="univ-ouverture" id="apercu"><div class="univ-texte">
<h2>13,8 milliards<br><span>d’années d’évolution.</span></h2>
<p>En se dilatant, l’Univers se refroidit et la matière s’organise.</p>
</div>{illustration('apercu')}</article>
{''.join(etapes)}</div>
</section>
{EXPERIENCES}
<section id="sources-univers" class="univ-sources" aria-labelledby="titre-sources">
<h2 id="titre-sources">Sources et modèles.</h2>
<div><p>Scènes illustratives. Dates approximatives.</p>
<details><summary>Références scientifiques</summary>
<p>Les scènes de l’histoire cosmique associent des vues d’artiste générées avec ImageGen, des animations procédurales et des schémas. Elles ne sont ni des photographies ni une simulation de l’Univers. Les couleurs, lumières et textures servent à expliquer ; elles ne montrent pas l’apparence mesurée des particules. L’espacement des chapitres n’est pas proportionnel aux durées. Les dates sont approximatives.</p>
<p>Les expériences de relativité calculent les rapports de durée et une géodésique dans les modèles indiqués. Les repères qui ressemblent à une grille n’impliquent pas que l’espace soit réellement un quadrillage.</p>
<ul>{sources}</ul></details>
<p><a href="/sujets/relativite-trous-noirs/">Relativité et trous noirs</a> · <a href="/recherches/">Tous les articles d’Aeternam</a></p></div>
</section>
</main>'''
