"""Section CAP : la casquette noire au Æ, ses figures et son texte.

Les deux figures de données sont tirées des fichiers publiés avec les études BCI
(aucune valeur saisie à la main) : les 540 essais EEG réels de PhysioNet pour les
signatures par personne, le Monte-Carlo pour la courbe de calibration. La casquette
est une maquette dessinée. Bibliothèque standard uniquement.
"""
from __future__ import annotations

import csv
import html
import json
import math
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
GENERALISATION = RACINE / 'recherche' / '2026-10-03-bci-generalisation'
MONTE_CARLO = RACINE / 'recherche' / '2026-10-03-bci-monte-carlo'
ELECTRODES = ('C3', 'Cz', 'C4')


def _f(x: float) -> str:
    return f'{x:.1f}'.rstrip('0').rstrip('.')


def pct(x: float) -> str:
    return f'{100 * x:.1f}'.replace('.', ',') + ' %'


# ------------------------------------------------------------------ données
def signatures() -> list[dict]:
    """Par personne et par électrode : écart standardisé du rythme mu (8-13 Hz),
    consigne « main gauche » moins consigne « main droite », et son erreur type."""
    with (GENERALISATION / 'donnees' / 'caracteristiques.csv').open(encoding='utf-8') as f:
        lignes = list(csv.DictReader(f))
    personnes = []
    for sujet in sorted({int(l['sujet']) for l in lignes}):
        essais = [l for l in lignes if int(l['sujet']) == sujet]
        gauche = [l for l in essais if l['label'] == '0']
        droite = [l for l in essais if l['label'] == '1']
        ecarts = {}
        for e in ELECTRODES:
            a = [float(l[f'{e}_8_13']) for l in gauche]
            b = [float(l[f'{e}_8_13']) for l in droite]
            ma, mb = sum(a) / len(a), sum(b) / len(b)
            va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
            vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
            sp = math.sqrt(((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2))
            d = (ma - mb) / sp
            se = math.sqrt(1 / len(a) + 1 / len(b) + d * d / (2 * (len(a) + len(b))))
            ecarts[e] = {'d': d, 'net': abs(d) > 1.96 * se}
        personnes.append({'sujet': sujet, 'essais': len(essais), 'ecarts': ecarts})
    return personnes


def courbe() -> tuple[list[int], list[float], list[list[float]]]:
    r = json.loads((MONTE_CARLO / 'resultats.json').read_text(encoding='utf-8'))
    s = r['scenarios']['empirique']['conditions']['niveau_initial']['scores']
    return r['protocole']['budgets_etiquetes'], s['moyenne'], s['quantiles_campagnes_10_90']


def nombres(personnes: list[dict]) -> dict:
    g = json.loads((GENERALISATION / 'resultats.json').read_text(encoding='utf-8'))
    budgets, moyenne, _ = courbe()
    attendu = [p for p in personnes if (p['ecarts']['C4']['net'] and p['ecarts']['C4']['d'] < 0)
               or (p['ecarts']['C3']['net'] and p['ecarts']['C3']['d'] > 0)]
    nets = [p for p in personnes if any(v['net'] for v in p['ecarts'].values())]
    return {
        'personnes': len(personnes),
        'essais': sum(p['essais'] for p in personnes),
        'par_personne': round(sum(p['essais'] for p in personnes) / len(personnes)),
        'attendu': len(attendu),
        'dans_le_bruit': len(personnes) - len(nets),
        'inconnue': pct(g['evaluations']['personne_reservee']['moyenne_personnes'] if 'evaluations' in g
                        else g['personne_reservee']['moyenne_personnes']),
        'meme': pct(g['evaluations']['run_reserve']['moyenne_personnes'] if 'evaluations' in g
                    else g['run_reserve']['moyenne_personnes']),
        'mc_debut': pct(moyenne[0]), 'mc_fin': pct(moyenne[-1]), 'mc_budget_fin': budgets[-1],
        'mc_45': pct(moyenne[budgets.index(32)] + (moyenne[budgets.index(64)] - moyenne[budgets.index(32)])
                     * math.log2(45 / 32)),
    }


# ------------------------------------------------------------------ casquette
def casquette() -> str:
    """Maquette : casquette noire vue de profil, le Æ brodé sur le panneau latéral."""
    calotte = ('M116 262 C106 210 128 146 188 113 C230 90 284 81 332 86 C400 93 447 138 462 203 '
               'C469 234 469 265 462 291 C384 300 226 292 116 262 Z')
    return f'''<svg class="casquette" viewBox="0 0 640 360" role="img" aria-label="Casquette noire vue de profil, un Æ brodé sur le côté">
<defs>
<linearGradient id="cap-tissu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c2f37"/><stop offset=".55" stop-color="#15171c"/><stop offset="1" stop-color="#08090b"/></linearGradient>
<radialGradient id="cap-volume" cx="0.56" cy="0.42" r="0.62"><stop offset="0" stop-color="#ffffff" stop-opacity=".075"/><stop offset=".7" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#000000" stop-opacity=".35"/></radialGradient>
<linearGradient id="cap-visiere" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0d0e11"/><stop offset=".35" stop-color="#23262c"/><stop offset="1" stop-color="#16181c"/></linearGradient>
<filter id="cap-flou" x="-30%" y="-300%" width="160%" height="700%"><feGaussianBlur stdDeviation="10"/></filter>
<filter id="cap-relief" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="1.2" stdDeviation=".7" flood-color="#000" flood-opacity=".9"/></filter>
<clipPath id="cap-forme"><path d="{calotte}"/></clipPath>
</defs>
<ellipse cx="372" cy="318" rx="240" ry="9" fill="#000" opacity=".85" filter="url(#cap-flou)"/>
<path d="M440 283 C506 277 576 287 622 309 C631 313 631 321 620 322 C560 318 496 306 446 302 Z" fill="url(#cap-visiere)"/>
<path d="M446 302 C496 306 560 318 620 322" fill="none" stroke="#040506" stroke-width="2.4"/>
<path d="M452 283.5 C510 279 574 289 618 309" fill="none" stroke="#ffffff" stroke-opacity=".1" stroke-width="1"/>
<g fill="none" stroke="#454953" stroke-width=".8" stroke-dasharray="2 2.4">
<path d="M466 290 C520 288 570 297 606 313"/><path d="M468 295 C520 294 566 302 600 316"/>
</g>
<path d="{calotte}" fill="url(#cap-tissu)"/>
<g clip-path="url(#cap-forme)">
<path d="{calotte}" fill="url(#cap-volume)"/>
<path d="M300 86 C362 104 414 180 431 296 L470 296 L470 80 Z" fill="#ffffff" opacity=".028"/>
<path d="M292 86 C238 108 202 186 194 296 L100 296 L100 80 Z" fill="#000000" opacity=".22"/>
<path d="M110 280 C232 292 384 297 470 289" fill="none" stroke="#050607" stroke-width="16" opacity=".55"/>
</g>
<path d="M120 250 C112 204 134 147 190 116 C232 93 284 84 332 89 C396 96 442 138 457 200" fill="none" stroke="#ffffff" stroke-opacity=".16" stroke-width="1.1"/>
<g clip-path="url(#cap-forme)">
<g fill="none" stroke="#050607" stroke-width="1.5">
<path d="M300 87 C362 105 414 181 431 293"/><path d="M291 87 C238 108 202 186 194 289"/>
</g>
<g fill="none" stroke="#43464f" stroke-width=".75" stroke-dasharray="2 2.4">
<path d="M306 90 C366 110 417 184 436 293"/><path d="M296 90 C246 112 211 188 203 289"/>
<path d="M120 255 C232 284 388 293 458 287"/>
</g>
</g>
<g fill="#07080a" stroke="#4a4e57" stroke-width="1"><ellipse cx="316" cy="124" rx="3.6" ry="3.2"/><ellipse cx="228" cy="136" rx="3" ry="3.4"/></g>
<ellipse cx="296" cy="86" rx="12" ry="4.2" fill="#1e2026" stroke="#4a4e57" stroke-width=".8"/>
<g filter="url(#cap-relief)"><text class="cap-ae" x="314" y="228" text-anchor="middle" transform="rotate(-5 314 210) skewX(-2)">Æ</text></g>
</svg>'''


# ------------------------------------------------------------------ figures de données
def figure_signatures(personnes: list[dict]) -> str:
    colonnes, L, H = 4, 132, 132
    lignes = math.ceil(len(personnes) / colonnes)
    largeur, hauteur = colonnes * L, lignes * H + 14
    morceaux = []
    for i, p in enumerate(personnes):
        cx, cy = (i % colonnes) * L + L / 2, (i // colonnes) * H + 60
        r = 42
        morceaux.append(f'<g class="tete"><path d="M{_f(cx - 6)} {_f(cy - r + 1)} L{_f(cx)} {_f(cy - r - 8)} L{_f(cx + 6)} {_f(cy - r + 1)}"/>'
                        f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{r}"/>'
                        f'<path d="M{_f(cx - r)} {_f(cy - 7)} q-6 7 0 14 M{_f(cx + r)} {_f(cy - 7)} q6 7 0 14"/></g>')
        for j, e in enumerate(ELECTRODES):
            ex = cx + (j - 1) * 25
            v = p['ecarts'][e]
            rayon = 2.5 + 11 * min(abs(v['d']), 1.0)
            classe = ('baisse' if v['d'] < 0 else 'hausse') + ('' if v['net'] else ' bruit')
            titre = (f"S{p['sujet']:03d}, {e} : écart {v['d']:+.2f}".replace('.', ',')
                     + ('' if v['net'] else ', dans le bruit'))
            morceaux.append(f'<g class="ecart {classe}"><title>{html.escape(titre)}</title>'
                            f'<circle cx="{_f(ex)}" cy="{_f(cy)}" r="{_f(rayon)}"/></g>'
                            f'<circle class="site" cx="{_f(ex)}" cy="{_f(cy)}" r="1.2"/>')
            if i == 0:
                morceaux.append(f'<text class="electrode" x="{_f(ex)}" y="{_f(cy + 26)}" text-anchor="middle">{e}</text>')
        morceaux.append(f'<text class="personne" x="{_f(cx)}" y="{_f(cy + r + 20)}" text-anchor="middle">S{p["sujet"]:03d}</text>')
    label = ('Douze têtes vues de dessus, une par personne. Sur chacune, trois marques à la place des électrodes C3, Cz et C4 : '
             'disque plein quand le rythme mu baisse en imaginant la main gauche plutôt que la droite, anneau quand il monte.')
    return (f'<svg class="signatures" viewBox="0 0 {largeur} {hauteur}" role="img" aria-label="{html.escape(label)}">'
            + ''.join(morceaux) + '</svg>')


def figure_courbe() -> str:
    budgets, moyenne, quantiles = courbe()
    L, H, g, d, h, b = 560, 300, 54, 18, 18, 46
    ymin, ymax = 0.45, 0.70

    def x(i):
        return g + i * (L - g - d) / (len(budgets) - 1)

    def y(v):
        return h + (ymax - v) * (H - h - b) / (ymax - ymin)

    m = []
    for v in (0.45, 0.50, 0.55, 0.60, 0.65, 0.70):
        m.append(f'<line class="grille{" hasard" if v == 0.5 else ""}" x1="{g}" x2="{L - d}" y1="{_f(y(v))}" y2="{_f(y(v))}"/>'
                 f'<text class="axe" x="{g - 10}" y="{_f(y(v) + 4)}" text-anchor="end">{int(round(v * 100))} %</text>')
    m.append(f'<text class="axe hasard-txt" x="{L - d}" y="{_f(y(0.5) - 7)}" text-anchor="end">hasard</text>')
    bande = ([f'{_f(x(i))},{_f(y(q[1]))}' for i, q in enumerate(quantiles)]
             + [f'{_f(x(i))},{_f(y(q[0]))}' for i, q in reversed(list(enumerate(quantiles)))])
    m.append(f'<polygon class="bande" points="{" ".join(bande)}"/>')
    m.append(f'<polyline class="moyenne" points="{" ".join(f"{_f(x(i))},{_f(y(v))}" for i, v in enumerate(moyenne))}"/>')
    for i, (n, v) in enumerate(zip(budgets, moyenne)):
        m.append(f'<g class="point"><title>{n} essais : {pct(v)}</title><circle cx="{_f(x(i))}" cy="{_f(y(v))}" r="3.2"/></g>'
                 f'<text class="axe" x="{_f(x(i))}" y="{H - b + 22}" text-anchor="middle">{n}</text>')
    m.append(f'<text class="axe titre-axe" x="{_f((g + L - d) / 2)}" y="{H - 6}" text-anchor="middle">essais étiquetés de la personne</text>')
    m.append(f'<text class="valeur" x="{_f(x(0) + 8)}" y="{_f(y(moyenne[0]) + 20)}">{pct(moyenne[0])}</text>')
    m.append(f'<text class="valeur" x="{_f(x(len(budgets) - 1))}" y="{_f(y(moyenne[-1]) - 12)}" text-anchor="end">{pct(moyenne[-1])}</text>')
    i45 = budgets.index(32) + math.log2(45 / 32)
    m.append(f'<line class="limite" x1="{_f(x(i45))}" x2="{_f(x(i45))}" y1="{h}" y2="{H - b}"/>'
             f'<text class="axe" x="{_f(x(i45) + 6)}" y="{h + 10}">45 essais réels par personne</text>')
    label = (f'Courbe : exactitude moyenne de {pct(moyenne[0])} sans essai personnel à {pct(moyenne[-1])} '
             f'avec {budgets[-1]} essais, bande des campagnes simulées autour.')
    return (f'<svg class="courbe" viewBox="0 0 {L} {H}" role="img" aria-label="{html.escape(label)}">' + ''.join(m) + '</svg>')


# ------------------------------------------------------------------ démonstration
def demonstration() -> str:
    budgets, moyenne, _ = courbe()
    donnees = json.dumps([[n, round(v, 4)] for n, v in zip(budgets, moyenne)])
    return f'''<div class="boucle" id="boucle" data-courbe="{html.escape(donnees, quote=True)}">
<div class="boucle-tel" aria-label="Maquette de l’écran verrouillé de l’iPhone">
<div class="tel"><span class="tel-ilot" aria-hidden="true"></span>
<p class="tel-date" id="tel-date"></p><p class="tel-heure" id="tel-heure"></p>
<div class="tel-notifs" id="tel-notifs" aria-live="polite"></div>
<span class="tel-barre" aria-hidden="true"></span></div>
</div>
<div class="boucle-texte">
<p class="boucle-consigne">Imaginez <button type="button" data-imagine="gauche">la main gauche</button> ou <button type="button" data-imagine="droite">la main droite</button>.</p>
<p class="boucle-lecture" id="boucle-lecture" aria-live="polite">Le décodeur attend un geste imaginé.</p>
<div class="tableau"><table class="boucle-journal">
<thead><tr><th>Imaginé</th><th>Lu</th><th>Réponse</th><th>Délai</th><th>Appris</th></tr></thead>
<tbody id="boucle-journal"><tr class="vide"><td colspan="5">Aucune réponse pour l’instant.</td></tr></tbody>
</table></div>
<p class="boucle-etat" id="boucle-etat"></p>
</div>
</div>
<noscript><p>La démonstration demande JavaScript.</p></noscript>'''


# ------------------------------------------------------------------ texte
def corps() -> tuple[str, str]:
    """(entête, corps) de la page /cap/."""
    personnes = signatures()
    n = nombres(personnes)
    entete = (f'<figure class="cap-maquette">{casquette()}<figcaption>Maquette. Une casquette noire, le Æ brodé sur le côté. '
              'Les huit électrodes sont dessous, contre le cuir chevelu : rien ne se voit.</figcaption></figure>')
    texte = f'''
<h2 id="explication">Explication</h2>
<p><strong>CAP est une casquette noire qui écoute l’activité électrique du cerveau.</strong> Sous le tissu, huit électrodes sèches passent entre les cheveux et touchent le cuir chevelu, au-dessus des zones qui commandent les mains. Elles ne font qu’écouter&nbsp;: aucun courant n’est envoyé. Le signal part en Bluetooth vers l’iPhone, qui reste dans la poche.</p>
<p>On apprend à CAP deux commandes, toujours les mêmes&nbsp;: imaginer serrer la main gauche, imaginer serrer la main droite. Quand le téléphone croit en reconnaître une, il pose une question sur l’écran verrouillé&nbsp;: «&nbsp;Main gauche&nbsp;?&nbsp;» Trois réponses possibles&nbsp;: oui&nbsp;; non, l’autre&nbsp;; non, rien. Chaque réponse devient un exemple qui lui apprend à vous lire, vous.</p>
<p>CAP ne lit pas les pensées. Elle reconnaît deux gestes imaginés, et le repos. La suite explique pourquoi elle doit apprendre chaque personne, ce que valent ses réponses et ce qu’on peut honnêtement en attendre.</p>

<h3>Même intention, signal différent</h3>
<p>Chaque cerveau s’est câblé à sa façon. Les plis du cortex ne sont pas orientés pareil, le crâne n’a pas la même épaisseur, et chacun imagine un geste à sa manière. L’EEG ne voit que la somme de millions de neurones, à travers l’os&nbsp;: une même intention n’arrive donc pas sur les électrodes sous la même forme d’une personne à l’autre.</p>
<p>La figure le montre sur de vrais enregistrements&nbsp;: {n['essais']} essais de {n['personnes']} personnes à qui l’on demandait d’imaginer la main gauche ou la main droite. Pour chacune, on compare le rythme mu, entre 8 et 13&nbsp;Hz, d’une consigne à l’autre, au-dessus de C3, Cz et C4.</p>
<figure class="cap-figure">{figure_signatures(personnes)}
<figcaption>Imaginer la main gauche plutôt que la droite&nbsp;: disque plein, le rythme mu baisse&nbsp;; anneau, il monte. La taille suit l’écart standardisé&nbsp;; les marques pâles restent dans le bruit (moins de deux erreurs types). Le motif des manuels, un disque sur C4 et un anneau sur C3, ne ressort que chez {n['attendu']} personnes sur {n['personnes']}, et chez {n['dans_le_bruit']} aucune électrode ne sort du bruit avec {n['par_personne']} essais. Données ouvertes PhysioNet EEG Motor Movement/Imagery, enregistrements 4, 8 et 12.</figcaption></figure>
<p>Conséquence directe&nbsp;: un décodeur appris sur d’autres cerveaux ne fait pas mieux que le hasard sur une personne qu’il n’a jamais vue. Dans <a href="/bci-generalisation/">notre réanalyse</a>, il obtient {n['inconnue']} sur une personne inconnue, pour un hasard de 50&nbsp;%, et {n['meme']} quand il a appris sur d’autres enregistrements de la même personne. CAP garde donc un socle commun et lui ajoute une couche qui n’appartient qu’à vous.</p>

<h3>Une question à la fois</h3>
<p>La couche personnelle apprend de vos réponses. Essayez&nbsp;: imaginez une main, laissez le décodeur lire ce qu’il peut, puis répondez sur l’écran verrouillé. Au départ, il se trompe presque une fois sur deux. Une réponse dans les trente secondes compte pleinement&nbsp;; plus tard, elle compte moins, parce qu’on ne sait plus à quel instant du signal elle se rapporte.</p>
{demonstration()}
<p class="note-figure">Simulation dans le navigateur, sans aucun signal réel. L’exactitude affichée suit la courbe du Monte-Carlo ci-dessous.</p>

<h3>Ce que la calibration peut espérer</h3>
<p>Chaque réponse est un essai étiqueté. Notre <a href="/bci-monte-carlo/">simulation Monte-Carlo</a>, calée sur les mêmes enregistrements, estime ce qu’un décodeur simple gagne quand on lui en donne davantage&nbsp;: de {n['mc_debut']} sans aucun essai personnel à {n['mc_fin']} avec {n['mc_budget_fin']}. C’est modeste. CAP ne promettra pas plus que ce que les mesures montreront.</p>
<figure class="cap-figure cap-courbe">{figure_courbe()}
<figcaption>Exactitude équilibrée moyenne d’un décodeur linéaire qui part du socle commun et donne aux essais de la personne un poids n/(n+16), sur 600 campagnes simulées&nbsp;; la bande couvre du 10<sup>e</sup> au 90<sup>e</sup> centile des campagnes. Au-delà de 45 essais, nombre réel d’essais par personne, la simulation extrapole. Simulation conditionnelle à un modèle ajusté sur des mesures humaines, pas une mesure.</figcaption></figure>

<h3>Ce que CAP ne fera pas</h3>
<ul>
<li><strong>Lire vos pensées.</strong> Deux gestes imaginés et le repos, rien d’autre.</li>
<li><strong>Agir sans vous demander.</strong> Tant que les critères ne tiennent pas plusieurs jours, elle pose la question&nbsp;; jamais d’action engageante comme un message, un appel ou un paiement.</li>
<li><strong>Envoyer votre cerveau en ligne.</strong> Le signal reste chiffré sur le téléphone&nbsp;; tout s’exporte et s’efface.</li>
<li><strong>Envoyer du courant.</strong> L’EEG est passif&nbsp;; le module tourne sur batterie et n’est jamais branché pendant qu’on le porte.</li>
</ul>

<h2 id="analyse-detaillee">Analyse détaillée</h2>
<h3>La chaîne</h3>
<p>Huit électrodes sèches Ag/AgCl en peigne entourent C3, Cz et C4&nbsp;: FC3, FC4, C3, Cz, C4, CP3, CPz et CP4, disposition à confirmer à réception du casque. Deux pinces d’oreille servent de référence et de bias. Le module PiEEG IronBCI numérise les 8 voies sur 24 bits, 250 fois par seconde, et les envoie en Bluetooth basse énergie&nbsp;: environ 6&nbsp;ko/s, soit 21,6&nbsp;Mo par heure.</p>
<p>L’application iPhone, en Swift avec Core Bluetooth, contrôle chaque voie et découpe le signal en fenêtres de 2&nbsp;s qui glissent de 250&nbsp;ms. Elle ne propose une détection que si la qualité est bonne, la probabilité au-dessus du seuil et la détection stable sur plusieurs fenêtres. Le décodeur a trois étages&nbsp;: un socle commun (filtrage, motifs spatiaux ou covariances), un recalage de deux minutes au repos à chaque pose, parce que la casquette n’est jamais posée exactement au même endroit, et la couche personnelle, une petite tête linéaire réentraînée la nuit.</p>

<h3>Ce que vaut une réponse</h3>
<div class="tableau"><table class="phrases">
<thead><tr><th>Réponse à «&nbsp;Main gauche&nbsp;?&nbsp;»</th><th>Exemple appris</th></tr></thead>
<tbody>
<tr><td>Oui</td><td>la fenêtre de signal reçoit l’étiquette «&nbsp;main gauche&nbsp;»</td></tr>
<tr><td>Non, l’autre</td><td>elle reçoit «&nbsp;main droite&nbsp;»</td></tr>
<tr><td>Non, rien</td><td>elle reçoit «&nbsp;repos&nbsp;»</td></tr>
<tr><td>Pas de réponse</td><td>aucune étiquette&nbsp;; la question compte comme une gêne</td></tr>
</tbody></table></div>
<div class="tableau"><table>
<thead><tr><th>Délai de la réponse</th><th>Poids de l’exemple</th></tr></thead>
<tbody><tr><td>30&nbsp;s au plus</td><td>1</td></tr><tr><td>de 30&nbsp;s à 5&nbsp;min</td><td>0,3</td></tr><tr><td>plus de 5&nbsp;min</td><td>0, statistiques seulement</td></tr></tbody>
</table></div>
<p>Une fenêtre de mauvaise qualité ne reçoit jamais d’étiquette, et aucune prédiction du modèle ne sert d’exemple&nbsp;: le décodeur n’apprend que de vos réponses et des sessions guidées. Ces seuils sont un point de départ&nbsp;; ils seront fixés sur les journaux réels.</p>

<h3>Deux apprentissages séparés</h3>
<p>Le détecteur, qui dit quelle commande, apprend en supervisé. La politique, qui décide s’il faut demander, agir ou se taire, apprend par renforcement, en bandit contextuel&nbsp;: un «&nbsp;oui&nbsp;» rapporte 1, un «&nbsp;non, rien&nbsp;» coûte 1, une question ignorée 0,5, une action fausse 5. Elle ne peut jamais dépasser six questions par heure ni parler quand une électrode décroche, et un bouton pause coupe tout. Le renforcement ne fabrique jamais d’étiquette pour le détecteur.</p>
<p>Les détections ratées ne déclenchent pas de question&nbsp;: on ne saurait rien d’elles. D’où trois à cinq minutes de calibration guidée par jour, avec des consignes audio et le téléphone en poche, et un bouton «&nbsp;j’ai voulu A&nbsp;».</p>

<h3>Quand une version remplace la précédente</h3>
<p>Un jeu de test est figé&nbsp;: un jour de calibration guidée sur cinq et 20&nbsp;% des exemples forts, tirés par jour entier pour éviter les fuites. Chaque nuit, une version candidate apprend sur le reste. Elle n’est gardée que si, sur ce test, l’exactitude équilibrée ne baisse pas, les fausses alertes par heure n’augmentent pas et l’étalonnage des probabilités ne se dégrade pas. Sinon la version précédente reste&nbsp;; chaque version est conservée et le retour arrière se fait en un geste.</p>

<h3>Le matériel</h3>
<div class="tableau"><table class="phrases">
<thead><tr><th>Élément</th><th>Référence</th><th>Prix public</th></tr></thead>
<tbody>
<tr><td>Acquisition</td><td><a href="https://www.pieeg.com/store/ironbci" rel="noopener">PiEEG IronBCI</a>, 8 voies, 24 bits, BLE 5.0</td><td>420&nbsp;$</td></tr>
<tr><td>Électrodes</td><td><a href="https://www.pieeg.com/store/8ch-dry-cap" rel="noopener">casque sec 8 voies</a> Ag/AgCl, 2 pinces d’oreille</td><td>370&nbsp;$</td></tr>
<tr><td>Batterie</td><td>LiPo une cellule, environ 200&nbsp;mAh</td><td>15 à 30&nbsp;$, estimation</td></tr>
<tr><td>Casquette</td><td>noire, Æ brodé, électrodes intégrées sous le tissu</td><td>à concevoir</td></tr>
</tbody></table></div>
<p>Environ 825 à 880&nbsp;$ pour un premier exemplaire, hors transport, taxes et main-d’œuvre. Prix publics lus le 16 novembre 2026.</p>

<h3>Feuille de route</h3>
<div class="tableau"><table class="phrases">
<thead><tr><th>Phase</th><th>Ce qui doit être prouvé</th></tr></thead>
<tbody>
<tr><td>0 · Acquisition</td><td>huit voies réelles à travers les cheveux, dix minutes enregistrées, test yeux ouverts et fermés</td></tr>
<tr><td>1 · Socle</td><td>deux commandes et le repos, évalués sur des jours séparés</td></tr>
<tr><td>2 · Application</td><td>Bluetooth téléphone verrouillé, reconnexion, autonomie, liste des actions possibles sans déverrouiller</td></tr>
<tr><td>3 · Questions</td><td>détection sur le téléphone, questions, journal, réentraînement de nuit, retour arrière</td></tr>
<tr><td>4 · Port quotidien</td><td>plusieurs jours de port réel, seuils réglés, décision de continuer ou d’arrêter</td></tr>
</tbody></table></div>
<p>Phase en cours&nbsp;: 0. Aucune mesure EEG n’a encore été faite avec CAP&nbsp;; tous les chiffres de cette page viennent de données ouvertes ou de simulations, présentées comme telles.</p>

<h3>Sources</h3>
<ul class="sources">
<li>Schalk G. et al., <a href="https://physionet.org/content/eegmmidb/1.0.0/" rel="noopener">EEG Motor Movement/Imagery Dataset</a>, PhysioNet, version 1.0.0, doi&nbsp;10.13026/C28G6P, licence Open Data Commons Attribution 1.0.</li>
<li>ÆTERNAM, <a href="/bci-generalisation/">BCI&nbsp;: un décodeur face à une nouvelle personne</a>, et <a href="/bci-monte-carlo/">la simulation Monte-Carlo de calibration</a>.</li>
<li>Apple, <a href="https://developer.apple.com/documentation/corebluetooth" rel="noopener">Core Bluetooth</a> et <a href="https://developer.apple.com/documentation/appintents" rel="noopener">App Intents</a>.</li>
</ul>
'''
    return entete, texte
