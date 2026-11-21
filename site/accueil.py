"""L'accueil d'ÆTERNAM, une seule histoire et une seule direction à financer.

Sur la nuit, de bout en bout : le nom et la question, puis des temps, un par écran, chacun avec
son schéma. D'abord décortiquer le vieillissement (un risque de mourir qui monte, sans loi qui
l'impose, et qui se joue dans les cellules) ; puis le principe (une cellule peut rajeunir) ; puis
copier ce qui marche, jusqu'à l'expérience à financer, celle des cellules (décision d'Aitor du
21/11/2026). Le dernier temps est l'appel.

Aucun texte ni aucun nombre n'est saisi ici : les textes viennent de ACCUEIL (site/langues/),
les nombres des études, par site/generer.py. Aucun sur-titre : un titre se suffit, ce qui le
précise vient après lui.
"""
from __future__ import annotations

import dessins


def heros(a: dict) -> str:
    """Le nom et la question, seuls ; le schéma n'apparaît qu'au défilement, dans la scène animée.
    Un cran par temps, appel compris : le défilement s'arrête là où ce temps est entièrement
    montré (accueil.css)."""
    nombre = len(a['temps']) + 1
    crans = ''.join(f'<span class="cran" style="--k: {k}" aria-hidden="true"></span>' for k in range(nombre))
    return f'''<section class="heros nuit" id="heros" aria-label="ÆTERNAM" style="--temps: {nombre}">
<div class="heros-plan">
<div class="heros-tete">
<h1 class="mot">ÆTERNAM</h1>
<p class="heros-question">{a['question']}</p>
</div>
<div class="scene" aria-hidden="true">{dessins.scene()}</div>
<p class="heros-defiler" aria-hidden="true">{a['defiler']} <span></span></p>
</div>
{crans}
</section>'''


def recit(a: dict, contact: dict | None) -> str:
    """Les temps : une phrase, puis ce qui la prouve, sources dans la phrase. Le dernier est
    l'appel : le cri, ce que l'on demande, et l'adresse, seule action de la page (sans adresse,
    le cri et la phrase restent seuls).

    Dans la scène animée, les temps se succèdent, un par écran, à côté du schéma qu'ils
    commentent (site/accueil/accueil.js) ; sans elle, ils se lisent l'un sous l'autre."""
    temps = ''.join(f'''<li class="temps">
<h2>{t['phrase']}</h2>
<p>{t['texte']}</p>
</li>''' for t in a['temps'])
    adresse = (f'\n<p class="appel-adresse"><a href="{contact["ecrire"]}">{contact["affiche"]}</a></p>'
               if contact else '')
    appel = f'''<li class="temps final" id="contact">
<h2>{a['cri']}</h2>
<p>{a['appel_texte']}</p>{adresse}
</li>'''
    return f'''<section class="recit nuit" id="recit" aria-label="{a['recit_label']}">
<ol class="temps-liste">{temps}{appel}</ol>
</section>'''


def corps(a: dict, contact: dict | None) -> str:
    return f'<main class="accueil">{heros(a)}{recit(a, contact)}</main>'
