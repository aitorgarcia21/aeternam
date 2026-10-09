"""Vues d'artiste locales ; les légendes et les explications restent en HTML."""
import hashlib
from html import escape
from pathlib import Path

DOSSIER = Path(__file__).parent / 'illustrations'
ILLUSTRATIONS = {
    'apercu': ('galaxie', 'Vue d’artiste d’une galaxie spirale : cœur doré, bras bleus et bandes de poussière.', ()),
    'particules': ('plasma', 'Représentation conceptuelle d’un milieu primordial chaud et dense, avant les atomes.', ()),
    'protons': ('protons', 'Deux compositions de quarks de valence : deux up dorés et un down bleu pour le proton ; un up doré et deux down bleus pour le neutron.', ('Proton · 2 up + 1 down', 'Neutron · 1 up + 2 down')),
    'noyaux': ('noyaux', 'À gauche, un proton ; à droite, un noyau d’hélium 4 formé de deux protons dorés et deux neutrons bleus.', ('Hydrogène · 1 proton', 'Hélium 4 · 2 protons + 2 neutrons')),
    'plasma': ('plasma', 'Vue conceptuelle d’un plasma opaque. Le tracé superposé montre la lumière qui change de direction.', ()),
    'atomes': ('atome', 'Représentation d’un atome d’hydrogène : petit noyau doré dans un nuage électronique bleu, sans orbite dessinée.', ('Noyau doré · nuage électronique bleu',)),
    'galaxies': ('galaxie', 'Vue d’artiste d’une galaxie spirale, exemple de structure évoluée, et non portrait d’une toute première galaxie.', ()),
    'systeme-solaire': ('soleil', 'Vue d’artiste du jeune Soleil dans un disque de gaz et de poussières où se forment des planètes.', ()),
}


def illustration(identifiant):
    if identifiant not in ILLUSTRATIONS:
        return ''
    nom, description, labels = ILLUSTRATIONS[identifiant]
    version = hashlib.sha256((DOSSIER / f'{nom}-1536.webp').read_bytes()).hexdigest()[:12]
    src = f'/illustrations/{nom}-1536.webp?v={version}'
    petit = f'/illustrations/{nom}-768.webp?v={version}'
    chargement = 'loading="eager" fetchpriority="high"' if identifiant == 'apercu' else 'loading="lazy"'
    reperes = ''.join(f'<span>{escape(label)}</span>' for label in labels)
    reperes = f'<div class="univ-art-labels">{reperes}</div>' if reperes else ''
    photons = '''<svg class="univ-photons" viewBox="0 0 600 400" aria-hidden="true"><path d="M 65 280 L 190 128 L 258 258 L 405 165 L 478 295 L 535 112"/></svg>''' if identifiant == 'plasma' else ''
    return f'''<figure class="univ-illustration" data-art="{identifiant}">
<div class="univ-image-wrap"><img src="{src}" srcset="{petit} 768w, {src} 1536w" sizes="(max-width: 760px) 100vw, 65vw" width="1536" height="1024" {chargement} decoding="async" alt="{escape(description)}">{photons}</div>
{reperes}<figcaption>Vue d’artiste · hors échelle</figcaption></figure>'''
