"""Articles signés proposés par tous (dossier contributions/ à la racine du dépôt).

Chaque article est un fichier Markdown nommé AAAA-MM-JJ-titre-court.md, précédé d'un
en-tête simple (titre, auteur, thème, résumé, langue : fr par défaut, ou en). Il arrive par une proposition publique
sur GitHub, relue avant publication ; l'historique de chaque fichier reste visible.

Le texte est rendu par un sous-ensemble sûr de Markdown : tout est échappé, aucun HTML
brut n'est accepté, les liens sont http(s) ou internes au site, les images viennent de
contributions/medias/. Une erreur arrête la construction avec un message qui dit quoi
corriger, ce qui sert aussi de vérification automatique des propositions.
Bibliothèque standard uniquement.
"""
from __future__ import annotations

import datetime as dt
import html
import re
from pathlib import Path

DEPOT = 'https://github.com/aitorgarcia21/aeternam'
LICENCE = ('CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0/deed.fr')
NOM_FICHIER = re.compile(r'^(\d{4}-\d{2}-\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$')
CLES = {'titre', 'auteur', 'date', 'theme', 'resume', 'orcid', 'licence', 'langue'}
ORCID = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$')
IMAGES = ('.png', '.jpg', '.jpeg', '.webp', '.gif')  # jamais de SVG : il pourrait exécuter du code

CODE = re.compile(r'`([^`\n]+)`')
FORMULE = re.compile(r'\$\$.+?\$\$|\\\(.+?\\\)', re.S)
LIEN = re.compile(r'\[([^\]\n]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)')  # une paire de parenthèses permise dans l'adresse
GRAS = re.compile(r'\*\*(?=\S)(.+?)(?<=\S)\*\*')
ITALIQUE = re.compile(r'(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])')
RESERVE = re.compile(r'\x00(\d+)\x00')
IMAGE = re.compile(r'^!\[([^\]]*)\]\(([^)\s]+)\)\s*$')


class ErreurContribution(ValueError):
    pass


def typographie(texte: str) -> str:
    """Espace fine insécable avant : ; ! ? et à l'intérieur des guillemets français."""
    texte = re.sub(r' ?([:;!?»])', lambda m: ' ' + m.group(1) if m.group(0).startswith(' ') else m.group(0), texte)
    return re.sub(r'« ?', '« ', texte)


def en_ligne(texte: str, nom: str) -> str:
    """Code, formules et liens mis de côté, puis échappement, gras et italique."""
    reserves: list[str] = []

    def garder(fragment: str) -> str:
        reserves.append(fragment)
        return f'\x00{len(reserves) - 1}\x00'

    texte = CODE.sub(lambda m: garder('<code>' + html.escape(m.group(1)) + '</code>'), texte)
    texte = FORMULE.sub(lambda m: garder(html.escape(m.group(0), quote=False)), texte)

    def lien(m):
        etiquette, cible = m.group(1), m.group(2)
        if not re.match(r'^(https?://[^\s"<>]+|/(?!/)[^\s"<>]*|#[\w-]+)$', cible):
            raise ErreurContribution(f'{nom} : lien refusé « {cible} » (http, https ou adresse du site seulement)')
        externe = ' rel="noopener"' if cible.startswith('http') else ''
        return garder(f'<a href="{html.escape(cible, quote=True)}"{externe}>{mise_en_forme(etiquette)}</a>')

    texte = LIEN.sub(lien, texte)
    texte = mise_en_forme(texte)
    while RESERVE.search(texte):
        texte = RESERVE.sub(lambda m: reserves[int(m.group(1))], texte)
    return texte


def mise_en_forme(texte: str) -> str:
    texte = typographie(html.escape(texte, quote=False))
    texte = GRAS.sub(r'<strong>\1</strong>', texte)
    return ITALIQUE.sub(r'<em>\1</em>', texte)


def debut_de_bloc(ligne: str) -> bool:
    return bool(re.match(r'^(#{1,3}\s|>|[-*]\s+\S|\d+[.)]\s+\S|```|\$\$|!\[)', ligne))


def rendre(corps: str, nom: str, medias: set[str]) -> str:
    lignes = corps.replace('\r\n', '\n').split('\n')
    sortie, i = [], 0
    while i < len(lignes):
        ligne = lignes[i].rstrip()
        if not ligne.strip():
            i += 1
            continue
        if ligne.startswith('```'):
            code, i = [], i + 1
            while i < len(lignes) and not lignes[i].startswith('```'):
                code.append(lignes[i])
                i += 1
            sortie.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
            i += 1
            continue
        titre = re.match(r'^(#{1,3})\s+(.+?)\s*#*$', ligne)
        if titre:
            niveau = 2 if len(titre.group(1)) <= 2 else 3
            sortie.append(f'<h{niveau}>{en_ligne(titre.group(2), nom)}</h{niveau}>')
            i += 1
            continue
        if ligne.startswith('$$'):
            formule = [ligne]
            ferme = len(ligne) > 2 and ligne.endswith('$$')
            while not ferme and i + 1 < len(lignes):
                i += 1
                formule.append(lignes[i].rstrip())
                ferme = lignes[i].rstrip().endswith('$$')
            if not ferme:
                raise ErreurContribution(f'{nom} : formule « $$ » jamais refermée')
            sortie.append('<p>' + html.escape('\n'.join(formule), quote=False) + '</p>')
            i += 1
            continue
        image = IMAGE.match(ligne)
        if image:
            alt, cible = image.group(1), image.group(2)
            if not cible.startswith('medias/') or not cible.lower().endswith(IMAGES) or '..' in cible:
                raise ErreurContribution(f'{nom} : image « {cible} » à placer dans contributions/medias/ (png, jpg, webp ou gif)')
            if cible not in medias:
                raise ErreurContribution(f'{nom} : image introuvable « contributions/{cible} »')
            legende = f'<figcaption>{en_ligne(alt, nom)}</figcaption>' if alt else ''
            sortie.append(f'<figure><img src="/contributions/{html.escape(cible, quote=True)}" alt="{html.escape(alt, quote=True)}" '
                          f'loading="lazy">{legende}</figure>')
            i += 1
            continue
        if ligne.startswith('>'):
            cite = []
            while i < len(lignes) and lignes[i].startswith('>'):
                cite.append(lignes[i][1:].strip())
                i += 1
            sortie.append('<blockquote><p>' + en_ligne(' '.join(cite), nom) + '</p></blockquote>')
            continue
        liste = re.match(r'^([-*]|\d+[.)])\s+', ligne)
        if liste:
            ordonnee = liste.group(1)[0].isdigit()
            motif = r'^\d+[.)]\s+' if ordonnee else r'^[-*]\s+'
            elements = []
            while i < len(lignes) and lignes[i].strip():
                courante = lignes[i].rstrip()
                if re.match(motif, courante):
                    elements.append(re.sub(motif, '', courante))
                elif elements and courante.startswith((' ', '\t')):
                    elements[-1] += ' ' + courante.strip()
                else:
                    break
                i += 1
            balise = 'ol' if ordonnee else 'ul'
            sortie.append(f'<{balise}>' + ''.join(f'<li>{en_ligne(e, nom)}</li>' for e in elements) + f'</{balise}>')
            continue
        paragraphe = []
        while i < len(lignes) and lignes[i].strip() and not (paragraphe and debut_de_bloc(lignes[i])):
            paragraphe.append(lignes[i].strip())
            i += 1
        sortie.append('<p>' + en_ligne(' '.join(paragraphe), nom) + '</p>')
    return '\n'.join(sortie)


def entete(texte: str, nom: str) -> tuple[dict, str]:
    if not texte.startswith('---\n'):
        raise ErreurContribution(f'{nom} : le fichier doit commencer par un en-tête entre deux lignes « --- »')
    fin = texte.find('\n---', 4)
    if fin < 0:
        raise ErreurContribution(f'{nom} : en-tête non fermé (ligne « --- » manquante)')
    meta = {}
    for numero, ligne in enumerate(texte[4:fin].split('\n'), start=2):
        if not ligne.strip() or ligne.lstrip().startswith('#'):
            continue
        if ':' not in ligne:
            raise ErreurContribution(f'{nom}, ligne {numero} : « clé: valeur » attendu')
        cle, valeur = ligne.split(':', 1)
        cle = cle.strip().lower()
        if cle not in CLES:
            raise ErreurContribution(f'{nom}, ligne {numero} : clé inconnue « {cle} » ({", ".join(sorted(CLES))})')
        meta[cle] = valeur.strip()
    return meta, texte[fin + 4:].lstrip('\n')


def lire(racine: Path, sujets: dict, langues: tuple = ('fr',)) -> list[dict]:
    dossier = racine / 'contributions'
    if not dossier.exists():
        return []
    medias = {f'medias/{p.name}' for p in (dossier / 'medias').glob('*')} if (dossier / 'medias').exists() else set()
    articles = []
    for chemin in sorted(dossier.glob('*.md')):
        nom = chemin.name
        if nom.lower() == 'readme.md' or nom.startswith('_'):
            continue
        fichier = NOM_FICHIER.match(nom)
        if not fichier:
            raise ErreurContribution(f'{nom} : nom attendu AAAA-MM-JJ-titre-court.md (minuscules, chiffres, tirets)')
        try:
            jour = dt.date.fromisoformat(fichier.group(1))
        except ValueError:
            raise ErreurContribution(f'{nom} : date invalide dans le nom du fichier') from None
        meta, corps = entete(chemin.read_text(encoding='utf-8'), nom)
        if meta.get('date') and meta['date'] != fichier.group(1):
            raise ErreurContribution(f'{nom} : la date de l’en-tête ({meta["date"]}) doit être celle du nom du fichier')
        titre, auteur = meta.get('titre', ''), meta.get('auteur', '')
        if not 3 <= len(titre) <= 140:
            raise ErreurContribution(f'{nom} : titre manquant ou trop long (140 caractères au plus)')
        if not 2 <= len(auteur) <= 80:
            raise ErreurContribution(f'{nom} : signature manquante ; « auteur: Prénom Nom »')
        if re.search(r'https?://|[<>]', auteur):
            raise ErreurContribution(f'{nom} : la signature est un nom, sans lien ni chevrons')
        theme = meta.get('theme', '')
        if theme and theme not in sujets:
            raise ErreurContribution(f'{nom} : thème inconnu « {theme} » ({", ".join(sujets)})')
        orcid = meta.get('orcid', '')
        if orcid and not ORCID.match(orcid):
            raise ErreurContribution(f'{nom} : ORCID attendu sous la forme 0000-0000-0000-0000')
        if meta.get('licence', LICENCE[0]) != LICENCE[0]:
            raise ErreurContribution(f'{nom} : les articles sont publiés sous licence {LICENCE[0]}')
        langue = meta.get('langue', langues[0])
        if langue not in langues:
            raise ErreurContribution(f'{nom} : langue inconnue « {langue} » ({", ".join(langues)})')
        resume = meta.get('resume', '')
        if len(resume) > 300:
            raise ErreurContribution(f'{nom} : résumé trop long (300 caractères au plus)')
        if len(corps.strip()) < 200:
            raise ErreurContribution(f'{nom} : texte trop court pour un article (200 caractères au moins)')
        articles.append({
            'fichier': nom, 'slug': fichier.group(2), 'jour': jour, 'langue': langue,
            'chemin': f'/contributions/{fichier.group(1)}-{fichier.group(2)}/',
            'titre': titre, 'auteur': auteur, 'orcid': orcid, 'theme': theme, 'resume': resume,
            'corps': rendre(corps, nom, medias),
        })
    chemins = [a['chemin'] for a in articles]
    if len(chemins) != len(set(chemins)):
        raise ErreurContribution('deux articles portent la même date et le même titre court')
    return sorted(articles, key=lambda a: (a['jour'], a['slug']), reverse=True)
