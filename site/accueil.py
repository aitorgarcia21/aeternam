"""L'accueil d'ÆTERNAM, une seule histoire et une seule direction à financer.

La nuit : le nom et la question, puis cinq temps, un par écran, chacun avec son schéma (la
courbe du risque de mourir, l'hydre, retarder, ralentir, le sang). La feuille qui monte :
l'expérience à financer, celle des cellules (décision d'Aitor du 21/11/2026). Puis l'appel.

Aucun texte ni aucun nombre n'est saisi ici : les textes viennent de ACCUEIL (site/langues/),
les nombres des études, par site/generer.py. Aucun sur-titre : un titre se suffit, ce qui le
précise vient après lui.
"""
from __future__ import annotations

import html

import dessins


def _mots(texte: str) -> str:
    """Chaque mot dans son <span> : la phrase s'éclaire au défilement (site/accueil/accueil.js)."""
    return ' '.join(f'<span class="m">{html.escape(mot)}</span>' for mot in texte.split())


def heros(a: dict) -> str:
    """Le nom et la question, seuls ; le schéma n'apparaît qu'au défilement, dans la scène animée."""
    return f'''<section class="heros nuit" id="heros" aria-label="ÆTERNAM" style="--temps: {len(a['temps'])}">
<div class="heros-plan">
<div class="heros-tete">
<h1 class="mot">ÆTERNAM</h1>
<p class="heros-question">{a['question']}</p>
</div>
<div class="scene" aria-hidden="true">{dessins.scene()}</div>
<p class="heros-defiler" aria-hidden="true">{a['defiler']} <span></span></p>
</div>
</section>'''


def recit(a: dict) -> str:
    """Les cinq temps : une phrase, puis ce qui la prouve, sources dans la phrase.

    Dans la scène animée, les temps se succèdent, un par écran, à côté du schéma qu'ils
    commentent (site/accueil/accueil.js) ; sans elle, ils se lisent l'un sous l'autre."""
    temps = ''.join(f'''<li class="temps">
<h2>{t['phrase']}</h2>
<p>{t['texte']}</p>
</li>''' for t in a['temps'])
    return f'''<section class="recit nuit" id="recit" aria-label="{a['recit_label']}">
<ol class="temps-liste">{temps}</ol>
</section>'''


def experience(a: dict, fleche: str) -> str:
    """L'expérience à financer : le but, ce qu'elle mesure (schéma), comment, et son protocole."""
    faits = ''.join(f'<li>{f}</li>' for f in a['experience_faits'])
    lien, libelle = a['experience_lien']
    return f'''<section class="experience" id="experience" aria-labelledby="experience-titre">
<header class="experience-tete" data-vu><h2 id="experience-titre">{a['experience_titre']}</h2>
<p>{a['experience_texte']}</p></header>
<figure class="experience-figure" data-vu>{dessins.experience()}
<figcaption>{a['experience_legende']}</figcaption></figure>
<div class="experience-bas" data-vu><ul class="experience-faits">{faits}</ul>
<p class="experience-lien"><a class="lien-suite" href="{lien}">{libelle} {fleche}</a></p></div>
</section>'''


def appel(a: dict, contact: dict | None) -> str:
    """Le dernier écran : les trois temps de la thèse, le cri sur toute la largeur, puis ce que
    l'on demande et l'adresse, seule action de la page. Sans adresse, les phrases restent seules."""
    phrases = ''.join(f'<span class="phrase">{_mots(phrase)}</span> ' for phrase in a['manifeste'])
    suite = ''
    if contact:
        suite = (f'<div class="appel-suite" data-vu><p class="appel-texte">{a["appel_texte"]} {a["appel_ecrivez"]}</p>'
                 f'<p class="appel-adresse"><a href="{contact["ecrire"]}">{contact["affiche"]}</a></p></div>')
    return f'''<section class="manifeste appel" id="contact" aria-labelledby="manifeste-titre">
<div class="manifeste-haut">
<h2 class="manifeste-phrase" id="manifeste-titre">{phrases.strip()}</h2>
<p class="manifeste-cri" style="--r-cri: {a['cri_encre'][0]}; --g-cri: {a['cri_encre'][1]}"><span>{a['cri']}</span></p>
</div>
{suite}
</section>'''


def corps(a: dict, contact: dict | None, fleche: str) -> str:
    # Après la nuit, deux volets : l'expérience à financer (papier), l'appel (nuit).
    return (f'<main class="accueil">{heros(a)}{recit(a)}<div class="feuille">'
            f'<div class="volet">{experience(a, fleche)}</div>'
            f'<div class="volet nuit">{appel(a, contact)}</div>'
            '</div></main>')
