"""L'accueil d'ÆTERNAM : le nom, la question (peut-on vivre pour toujours ?), le sablier
dont le sable s'arrête, puis le récit : ce que la recherche sait de l'immortalité, chapitre
après chapitre, écrit par le sable ; enfin le blog de recherche et l'invitation à écrire.

Aucun texte ni aucun nombre n'est saisi ici : les textes viennent de ACCUEIL et SUJETS
(site/langues/), les nombres des études, par site/generer.py. Aucun sur-titre : un titre
se suffit, ce qui le précise vient après lui.
"""
from __future__ import annotations

import html

import dessins


def _mots(texte: str) -> str:
    """Chaque mot dans son <span> : la phrase s'éclaire au défilement (site/accueil/accueil.js)."""
    return ' '.join(f'<span class="m">{html.escape(mot)}</span>' for mot in texte.split())


def heros(a: dict) -> str:
    """Le nom et la question, seuls ; le sablier n'apparaît qu'au défilement, dans la scène animée."""
    return f'''<section class="heros nuit" id="heros" aria-label="ÆTERNAM" style="--chapitres: {len(a['chapitres'])}">
<div class="heros-plan">
<canvas class="ciel" aria-hidden="true"></canvas>
<div class="heros-tete">
<h1 class="mot">ÆTERNAM</h1>
<p class="heros-question">{a['question']}</p>
</div>
<div class="heros-dessin">{dessins.sablier()}</div>
<p class="heros-defiler" aria-hidden="true">{a['defiler']} <span></span></p>
</div>
</section>'''


def recit(a: dict) -> str:
    """Les chapitres : un nombre, la question qu'il pose, ce que l'on sait, et la source dans la phrase.

    Dans la scène animée, le sable du sablier vient écrire chaque nombre (site/accueil/accueil.js) ;
    le nombre reste dans la page, pour qui ne voit pas la scène. <i class="base"> marque la ligne
    de base sur laquelle le sable se pose."""
    chapitres = ''.join(f'''<li class="chapitre">
<p class="chapitre-nombre" style="--car: {len(html.unescape(c['nombre']))}"><span class="n">{c['nombre']}</span><i class="base"></i> <span class="u">{c['unite']}</span></p>
<h2>{c['question']}</h2>
<p class="chapitre-texte">{c['texte']}</p>
</li>''' for c in a['chapitres'])
    return f'''<section class="recit nuit" id="recit" aria-label="{a['recit_label']}">
<canvas class="grains" aria-hidden="true"></canvas>
<ol class="chapitres">{chapitres}</ol>
</section>'''


def manifeste(a: dict, chiffres: list[tuple[int, str]]) -> str:
    """Trois phrases, une par ligne, puis ce qu'est le site et ses trois nombres."""
    phrases = ''.join(f'<span class="phrase">{_mots(phrase)}</span> ' for phrase in a['manifeste'])
    compteurs = ''.join(f'<li><strong data-compte="{valeur}">{valeur}</strong><span>{libelle}</span></li>'
                        for valeur, libelle in chiffres)
    return f'''<section class="manifeste" aria-labelledby="manifeste-titre">
<h2 class="manifeste-phrase" id="manifeste-titre">{phrases.strip()}</h2>
<div class="manifeste-suite" data-vu>
<p>{a['manifeste_suite']}</p>
<ul class="chiffres">{compteurs}</ul>
</div>
</section>'''


def blog(a: dict, themes: list[dict], fleche: str) -> str:
    """Six thèmes : la question, pourquoi elle compte, ce que l'on sait, les derniers articles, puis le thème entier."""
    blocs = []
    for th in themes:
        articles = ''.join(f'<li><a href="{art["chemin"]}"><span>{art["titre"]}</span>{fleche}</a></li>' for art in th['articles'])
        blocs.append(f'''<article class="univers" id="univers-{th['cle']}" data-vu>
<figure class="univers-figure">{th['dessin']}</figure>
<div class="univers-texte">
<h3>{th['question']}</h3>
<p class="univers-enjeu">{th['enjeu']}</p>
<p class="univers-reponse">{th['reponse']} <a href="{th['lien']}">{a['blog_etude']}</a></p>
<ul class="univers-articles">{articles}</ul>
<p class="univers-suite"><a class="lien-suite" href="{th['chemin']}">{th['suite']} {fleche}</a></p>
</div>
</article>''')
    return f'''<section class="univers-tous" id="blog" aria-labelledby="blog-titre">
<header class="section-tete" data-vu><h2 id="blog-titre">{a['blog_titre']}</h2>
<p>{a['blog_texte']}</p></header>
{''.join(blocs)}
</section>'''


def ecrire(a: dict, derniers: list[dict], fleche: str) -> str:
    """L'invitation à écrire, et les derniers articles de la communauté quand il y en a."""
    liste = ''.join(f'<li><a href="{d["chemin"]}"><span>{d["titre"]}<small>{d["signature"]}</small></span>{fleche}</a></li>'
                    for d in derniers)
    liste = f'<ul class="univers-articles signes-accueil">{liste}</ul>' if liste else ''
    return f'''<section class="ouvert" aria-labelledby="ouvert-titre" data-vu>
<h2 id="ouvert-titre">{a['ecrire_titre']}</h2>
<p>{a['ecrire_texte']}</p>
<p class="actions"><a class="bouton" href="/ecrire/">{a['ecrire_bouton']} {fleche}</a><a class="bouton contour" href="/recherches/">{a['blog_tous']}</a></p>
{liste}
</section>'''


def corps(a: dict, themes: list[dict], chiffres: list[tuple[int, str]], derniers: list[dict], fleche: str) -> str:
    # Tout ce qui suit la nuit est une seule feuille de papier, qui monte par-dessus le ciel.
    return (f'<main class="accueil">{heros(a)}{recit(a)}<div class="feuille">{manifeste(a, chiffres)}'
            f'{blog(a, themes, fleche)}{ecrire(a, derniers, fleche)}</div></main>')
