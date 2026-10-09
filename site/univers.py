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
        reperes.append(f'<a href="#{e["id"]}" aria-label="{escape(e["repere"])}" title="{escape(e["date"])}"{courant}><span></span><span class="univ-repere-nom">{e["repere"]}</span></a>')
    sources = ''.join(f'<li><a href="{url}">{nom}</a></li>' for nom, url in SOURCES.values())
    options = ''.join(f'<option value="{i}">{escape(e["repere"])}</option>' for i, e in enumerate(ETAPES))
    return f'''<main>
<nav class="univ-sommaire" aria-label="Chapitres">
<a href="#histoire" aria-current="location">Histoire de l’Univers</a>
<a href="#espace-temps">Espace et temps</a><a href="#avant-apres">Avant et après</a><a href="#sources-univers">Sources</a>
<button id="univ-motion" type="button" aria-pressed="false" hidden><span class="univ-motion-icon" aria-hidden="true"></span><span id="univ-motion-label">Figer les animations</span></button>
</nav>
<section id="histoire" class="univ-histoire" aria-label="Histoire de l’Univers">
<div class="univ-scenes" aria-hidden="true"><div class="univ-scene-fixe">
<canvas id="cosmos-canvas"></canvas><canvas id="cosmos-overlay"></canvas>
<span id="cosmos-numero"></span><p id="cosmos-legende">Galaxie · représentation schématique</p>
</div></div>
<div class="univ-etapes">
<article class="univ-ouverture" id="apercu"><div class="univ-texte">
<h2>13,8 milliards<br><span>d’années d’évolution.</span></h2>
<p>L’Univers observable a évolué depuis un état extrêmement chaud et dense. En se dilatant, il s’est refroidi : les particules, les atomes, puis les étoiles ont pu se former.</p>
<nav class="univ-raccourcis" aria-label="Repères de l’histoire"><a href="#debut">Big Bang</a><a href="#atomes">Première lumière</a><a href="#aujourdhui">Aujourd’hui</a></nav>
</div></article>
{''.join(etapes)}</div>
<nav class="univ-chronologie" aria-label="Étapes de l’histoire cosmique">{''.join(reperes)}
<div class="univ-navigation-mobile"><button type="button" id="epoque-precedente" aria-label="Étape précédente">←</button><label class="univ-choix-mobile" for="univ-choix"><span class="univ-sr">Étape cosmologique</span><select id="univ-choix">{options}</select></label><button type="button" id="epoque-suivante" aria-label="Étape suivante">→</button></div></nav>
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
