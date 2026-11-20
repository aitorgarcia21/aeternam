#!/usr/bin/env python3
"""Lire un souvenir dans un cerveau conservé : combien d'animaux pour un test à l'aveugle ?

Le test : des souris dont la moitié a appris une association, des cerveaux conservés puis
imagés, et un lecteur qui ne connaît pas les groupes et doit dire, pour chaque cerveau, si
l'animal avait appris. Au hasard, il a raison une fois sur deux.

Le script calcule, par la loi binomiale exacte (test unilatéral à 5 %) :

- le plus petit nombre de cerveaux qui donne 80 % ou 90 % de chances de conclure, selon la
  justesse réelle du lecteur (70 %, 80 %, 90 %) ;
- ce que peuvent montrer cinq cerveaux, l'effectif de l'étude de microscopie la plus poussée
  à ce jour (Uytiepo et al. 2025 : trois souris conditionnées, deux témoins).

Ce sont des calculs de plan d'expérience : aucune mesure n'est produite ici.
Bibliothèque standard seule. `--out` choisit le fichier de résultats.
"""
from __future__ import annotations

import argparse
import json
from math import comb, isclose
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
ALPHA = 0.05


def queue(n: int, k: int, p: float) -> float:
    """Probabilité d'au moins k réussites sur n, chacune de probabilité p."""
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def seuil(n: int) -> int | None:
    """Plus petit nombre de bonnes réponses que le hasard atteint moins de 5 fois sur 100."""
    for k in range(n + 1):
        if queue(n, k, 0.5) <= ALPHA:
            return k
    return None


def puissance(n: int, justesse: float) -> float:
    k = seuil(n)
    return 0.0 if k is None else queue(n, k, justesse)


def effectif(justesse: float, cible: float) -> int:
    """Plus petit n à partir duquel la puissance ne redescend plus sous la cible."""
    n = 1
    while True:
        if all(puissance(m, justesse) >= cible for m in range(n, n + 12)):
            return n
        n += 1


def analyser() -> dict:
    plan = {}
    for justesse in (0.7, 0.8, 0.9):
        cle = f'justesse_{int(justesse * 100)}'
        plan[cle] = {'justesse': justesse}
        for cible in (0.8, 0.9):
            n = effectif(justesse, cible)
            plan[cle][f'cerveaux_puissance_{int(cible * 100)}'] = n
            plan[cle][f'bonnes_reponses_requises_{int(cible * 100)}'] = seuil(n)
    cinq = {'cerveaux': 5, 'bonnes_reponses_requises': seuil(5), 'p_si_cinq_sur_cinq': queue(5, 5, 0.5),
            'puissance_si_justesse_80': puissance(5, 0.8), 'puissance_si_justesse_90': puissance(5, 0.9)}
    return {'plan': plan, 'cinq_cerveaux': cinq}


def autotests() -> None:
    assert isclose(queue(5, 5, 0.5), 1 / 32)
    assert seuil(4) is None and seuil(5) == 5          # quatre cerveaux ne peuvent rien établir
    assert isclose(puissance(5, 0.8), 0.8 ** 5)
    assert effectif(0.9, 0.8) <= effectif(0.8, 0.8) <= effectif(0.7, 0.8)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER / 'resultats.json')
    args = parser.parse_args()
    autotests()
    resultats = analyser()
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for cle, p in resultats['plan'].items():
        print(cle, p)
    print('cinq cerveaux', {k: round(v, 3) if isinstance(v, float) else v for k, v in resultats['cinq_cerveaux'].items()})


if __name__ == '__main__':
    main()
