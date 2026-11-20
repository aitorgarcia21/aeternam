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
    """Les chapitres : une question, sa réponse en une phrase, puis ce que l'on sait, nombres et
    sources dans la phrase. Aucun nombre n'est affiché seul.

    Dans la scène animée, les chapitres se succèdent, un par écran (site/accueil/accueil.js) ;
    sans elle, ils se lisent l'un sous l'autre."""
    chapitres = ''.join(f'''<li class="chapitre">
<h2>{c['question']}</h2>
<p class="chapitre-reponse">{c['reponse']}</p>
<p class="chapitre-texte">{c['texte']}</p>
</li>''' for c in a['chapitres'])
    return f'''<section class="recit nuit" id="recit" aria-label="{a['recit_label']}">
<ol class="chapitres">{chapitres}</ol>
</section>'''


def etude(a: dict, chiffres: list[tuple[int, str, str]]) -> str:
    """Le résultat, en une phrase, et ses trois nombres (chacun avec ce qu'il compte)."""
    compteurs = ''.join(f'<li><strong data-compte="{valeur}">{affiche}</strong><span>{libelle}</span></li>'
                        for valeur, affiche, libelle in chiffres)
    return f'''<section class="etude" id="etude" aria-labelledby="etude-titre">
<div class="etude-tete" data-vu><h2 id="etude-titre">{a['etude_titre']}</h2>
<p>{a['etude_texte']}</p></div>
<ul class="chiffres" data-vu>{compteurs}</ul>
</section>'''


def difference(a: dict) -> str:
    """Retarder ou ralentir : les deux schémas, côte à côte."""
    pentes = ''.join(f'''<figure class="pente" data-vu>{dessins.pente(mode)}
<figcaption><h3>{titre}</h3><p>{texte}</p></figcaption></figure>''' for mode, titre, texte in a['pentes'])
    return f'''<section class="difference" aria-labelledby="difference-titre">
<header class="section-tete" data-vu><h2 id="difference-titre">{a['difference_titre']}</h2>
<p>{a['difference_texte']}</p></header>
<div class="pentes">{pentes}</div>
</section>'''


def mesure(a: dict, figure: str) -> str:
    """La mesure : la figure tirée des données, son axe et sa légende."""
    legende = ''.join(f'<li class="cle-{i}">{ligne}</li>' for i, ligne in enumerate(a['mesure_legende']))
    return f'''<section class="mesure" aria-labelledby="mesure-titre">
<header class="section-tete" data-vu><h2 id="mesure-titre">{a['mesure_titre']}</h2>
<p>{a['mesure_texte']}</p></header>
<figure class="mesure-figure" data-vu>{figure}
<figcaption><p class="mesure-axe">{a['mesure_axe']}</p><ul class="mesure-legende">{legende}</ul></figcaption></figure>
</section>'''


def verifier(a: dict) -> str:
    """Pourquoi on peut s'y fier : données, lecture contrôlée, test étalonné, limites."""
    preuves = ''.join(f'<li><h3>{titre}</h3><p>{texte}</p></li>' for titre, texte in a['preuves'])
    return f'''<section class="verifier" aria-labelledby="verifier-titre">
<header class="section-tete" data-vu><h2 id="verifier-titre">{a['verifier_titre']}</h2>
<p>{a['verifier_texte']}</p></header>
<ul class="preuves" data-vu>{preuves}</ul>
</section>'''


def suite(a: dict, fleche: str) -> str:
    """Les expériences prêtes : ce qu'elles mesurent, leur taille, leur protocole."""
    experiences = ''.join(f'''<li><h3>{titre}</h3><p>{texte}</p>
<p><a class="lien-suite" href="{lien}">{libelle} {fleche}</a></p></li>''' for titre, texte, lien, libelle in a['experiences'])
    return f'''<section class="suite" id="experiences" aria-labelledby="suite-titre">
<header class="section-tete" data-vu><h2 id="suite-titre">{a['suite_titre']}</h2>
<p>{a['suite_texte']}</p></header>
<ul class="experiences" data-vu>{experiences}</ul>
</section>'''


def appel(a: dict, contact: dict | None) -> str:
    """Le dernier écran : les trois phrases, puis ce que l'on demande et l'adresse, seule action
    de la page. Sans adresse, les trois phrases restent seules."""
    phrases = ''.join(f'<span class="phrase">{_mots(phrase)}</span> ' for phrase in a['manifeste'])
    suite = ''
    if contact:
        suite = (f'<div class="appel-suite" data-vu><p class="appel-texte">{a["appel_texte"]} {a["appel_ecrivez"]}</p>'
                 f'<p class="appel-adresse"><a href="{contact["ecrire"]}">{contact["affiche"]}</a></p></div>')
    return f'''<section class="manifeste appel" id="contact" aria-labelledby="manifeste-titre">
<h2 class="manifeste-phrase" id="manifeste-titre">{phrases.strip()}</h2>
{suite}
</section>'''


def corps(a: dict, chiffres: list[tuple[int, str, str]], figure: str, contact: dict | None, fleche: str) -> str:
    # Après la nuit, quatre volets qui glissent l'un sur l'autre : le résultat et la différence
    # (papier), la mesure et ses contrôles (nuit), les expériences (papier), l'appel (nuit).
    return (f'<main class="accueil">{heros(a)}{recit(a)}<div class="feuille">'
            f'<div class="volet">{etude(a, chiffres)}{difference(a)}</div>'
            f'<div class="volet nuit">{mesure(a, figure)}{verifier(a)}</div>'
            f'<div class="volet">{suite(a, fleche)}</div>'
            f'<div class="volet nuit">{appel(a, contact)}</div>'
            '</div></main>')
