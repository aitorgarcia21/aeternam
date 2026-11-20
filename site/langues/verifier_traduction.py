#!/usr/bin/env python3
"""Vérifie qu'une traduction garde la structure de l'original français.

Usage : python3 site/langues/verifier_traduction.py site/langues/en_parts/p1.py [...]

Pour chaque dictionnaire d'article du fichier, compare avec site/langues/fr.py : mêmes clés,
mêmes marqueurs [[...]], même suite de balises HTML (avec leurs id, href, class), mêmes
formules. Sort en erreur à la moindre différence, avec ce qu'il faut corriger.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

ICI = Path(__file__).resolve().parent
MARQUEUR = re.compile(r'\[\[[a-z0-9_]+\]\]')
BALISE = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)((?:\s+[a-zA-Z-]+(?:="[^"]*")?)*)\s*/?>')
ATTRIBUT = re.compile(r'\b(id|href|class|scope|colspan|rowspan|src)="([^"]*)"')
FORMULE = re.compile(r'\$\$.+?\$\$|\\\(.+?\\\)', re.S)
TEXTE_MATHS = re.compile(r'\\(?:text|mathrm|textrm)\{[^{}]*\}')
FRANCAIS = re.compile(r'&nbsp;[:;?!»]|«&nbsp;|\b(?:les|des|une|est|dans|avec|pour|nous|cette|sont|mais|donc|aussi|très)\b')


def charger(chemin: Path):
    spec = importlib.util.spec_from_file_location(chemin.stem, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def balises(texte: str) -> list[tuple]:
    return [(m.group(1).lower(), tuple(sorted(ATTRIBUT.findall(m.group(2))))) for m in BALISE.finditer(texte)]


def formules(texte: str) -> list[str]:
    return [re.sub(r'\s+', ' ', TEXTE_MATHS.sub(r'\\text{}', f)) for f in FORMULE.findall(texte)]


def comparer(nom: str, fr: dict, en: dict) -> list[str]:
    erreurs = []
    if set(fr) != set(en):
        erreurs.append(f'clés différentes : manquent {sorted(set(fr) - set(en))}, en trop {sorted(set(en) - set(fr))}')
    for cle in sorted(set(fr) & set(en)):
        a, b = fr[cle], en[cle]
        if not isinstance(a, str):
            continue
        ma, mb = Counter(MARQUEUR.findall(a)), Counter(MARQUEUR.findall(b))
        if ma != mb:
            erreurs.append(f'{cle} : marqueurs différents : manquent {sorted((ma - mb).elements())}, en trop {sorted((mb - ma).elements())}')
        ba, bb = balises(a), balises(b)
        if ba != bb:
            i = next((k for k, (x, y) in enumerate(zip(ba, bb)) if x != y), min(len(ba), len(bb)))
            erreurs.append(f'{cle} : balises différentes à partir de la n° {i + 1} : '
                           f'attendu {ba[i:i + 3]}, trouvé {bb[i:i + 3]} ({len(ba)} balises en français, {len(bb)} en anglais)')
        fa, fb = formules(a), formules(b)
        if fa != fb:
            i = next((k for k, (x, y) in enumerate(zip(fa, fb)) if x != y), min(len(fa), len(fb)))
            erreurs.append(f'{cle} : formules différentes à partir de la n° {i + 1} : '
                           f'attendu {fa[i:i + 1]}, trouvé {fb[i:i + 1]} ({len(fa)} en français, {len(fb)} en anglais)')
        sans_balises = FORMULE.sub(' ', re.sub(r'<[^>]+>', ' ', b))
        restes = FRANCAIS.findall(sans_balises)
        if len(restes) > 3:
            erreurs.append(f'{cle} : il reste du français ou sa typographie ({len(restes)} indices, par exemple {restes[:6]})')
        if len(b) < 0.6 * len(a):
            erreurs.append(f'{cle} : traduction trop courte ({len(b)} caractères contre {len(a)}) : rien ne doit être résumé')
    return [f'{nom} · {e}' for e in erreurs]


def principal(fichiers: list[str]) -> int:
    fr = charger(ICI / 'fr.py')
    erreurs, vus = [], 0
    for fichier in fichiers:
        en = charger(Path(fichier).resolve())
        for nom, valeur in vars(en).items():
            if nom.startswith('_') or not isinstance(valeur, dict) or 'corps' not in valeur:
                continue
            if not hasattr(fr, nom):
                erreurs.append(f'{nom} : inconnu dans fr.py')
                continue
            vus += 1
            erreurs += comparer(nom, getattr(fr, nom), valeur)
    for e in erreurs:
        print('ERREUR', e)
    print(f'{vus} article(s) vérifié(s), {len(erreurs)} erreur(s)')
    return 1 if erreurs or not vus else 0


if __name__ == '__main__':
    sys.exit(principal(sys.argv[1:]))
