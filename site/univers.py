"""Composition du parcours de l'accueil ; texte complet présent sans JavaScript."""
from html import escape
from langues.univers_fr import ETAPES, EXPERIENCES, SOURCES


def contenu():
    etapes = []
    reperes = []
    for i, e in enumerate(ETAPES):
        nom, url = SOURCES[e['source']]
        paragraphes = ''.join(f'<p>{p}</p>' for p in e['texte'])
        etapes.append(f'''<article class="univ-etape" id="{e['id']}" data-etape="{i}" data-legende="{escape(e['legende'])}">
<div class="univ-texte"><h2>{e['titre']}</h2><p class="univ-date">{e['date']}</p>
{paragraphes}<p class="univ-source"><a href="{url}">{nom}</a></p>
<details><summary>Analyse détaillée</summary><p>{e['detail']}</p></details></div></article>''')
        courant = ' aria-current="step"' if i == 0 else ''
        reperes.append(f'<a href="#{e["id"]}" aria-label="{escape(e["repere"])}"{courant}><span></span><span class="univ-repere-nom">{e["repere"]}</span></a>')
    sources = ''.join(f'<li><a href="{url}">{nom}</a></li>' for nom, url in SOURCES.values())
    options = ''.join(f'<option value="{i}">{escape(e["repere"])}</option>' for i, e in enumerate(ETAPES))
    return f'''<main>
<nav class="univ-sommaire" aria-label="Chapitres">
<a href="#histoire" aria-current="location">Histoire de l’Univers</a>
<a href="#espace-temps">Espace et temps</a><a href="#avant-apres">Avant et après</a><a href="#sources-univers">Sources</a>
<button id="univ-motion" type="button" aria-pressed="false" hidden>Figer les animations</button>
</nav>
<section id="histoire" class="univ-histoire" aria-label="Histoire de l’Univers">
<div class="univ-scenes" aria-hidden="true"><div class="univ-scene-fixe">
<canvas id="cosmos-canvas"></canvas><p id="cosmos-legende">{ETAPES[0]['legende']}</p>
</div></div>
<div class="univ-etapes">{''.join(etapes)}</div>
<nav class="univ-chronologie" aria-label="Étapes de l’histoire cosmique">{''.join(reperes)}
<label class="univ-choix-mobile" for="univ-choix"><span class="univ-sr">Étape cosmologique</span><select id="univ-choix">{options}</select></label></nav>
</section>
{EXPERIENCES}
<section id="sources-univers" class="univ-sources" aria-labelledby="titre-sources">
<h2 id="titre-sources">Sources et modèles.</h2>
<div><p>Les scènes de l’histoire cosmique sont des illustrations calculées pour expliquer les étapes ; elles ne sont ni des photographies ni une simulation de l’Univers. L’espacement des chapitres n’est pas proportionnel aux durées. Les dates sont approximatives.</p>
<p>Les expériences de relativité calculent les rapports de durée et une géodésique dans les modèles indiqués. Les repères qui ressemblent à une grille n’impliquent pas que l’espace soit réellement un quadrillage.</p>
<ul>{sources}</ul>
<p><a href="/sujets/relativite-trous-noirs/">Relativité et trous noirs</a> · <a href="/recherches/">Tous les articles d’Aeternam</a></p></div>
</section>
</main>'''
