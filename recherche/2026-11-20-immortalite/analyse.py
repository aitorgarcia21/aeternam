#!/usr/bin/env python3
"""Ce que vieillir change au risque de mourir, sur une table de mortalité publique.

Table de période 2023 de la Social Security Administration des États-Unis
(donnees/table-mortalite-ssa-2023.csv, domaine public) : q(x) est la probabilité de mourir
dans l'année à l'âge x. Le script calcule, pour chaque sexe :

- l'âge où ce risque est le plus bas, et sa valeur ;
- le temps au bout duquel une personne sur deux serait encore en vie si ce risque restait
  le même toute la vie : ln 2 / −ln(1 − q). C'est un calcul sur une hypothèse, pas une prévision ;
- le temps de doublement du risque entre 30 et 90 ans : droite ajustée sur ln q(x).

Aucune dépendance hors bibliothèque standard. `--out` choisit le fichier de résultats.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from math import isclose, log
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
TABLE = DOSSIER / 'donnees' / 'table-mortalite-ssa-2023.csv'
SEXES = {'hommes': 'male_q', 'femmes': 'female_q'}


def lire(chemin: Path) -> dict[str, list[float]]:
    lignes = [ligne for ligne in chemin.read_text(encoding='utf-8').splitlines() if not ligne.startswith('#')]
    table = list(csv.DictReader(lignes))
    ages = [int(ligne['age']) for ligne in table]
    if ages != list(range(len(ages))):
        raise ValueError('La table doit donner chaque âge une fois, à partir de 0.')
    return {sexe: [float(ligne[colonne]) for ligne in table] for sexe, colonne in SEXES.items()}


def mediane_a_risque_constant(q: float) -> float:
    """Années au bout desquelles la moitié d'un groupe est encore en vie, si q ne change jamais."""
    return log(2) / -log(1 - q)


def doublement(q: list[float], debut: int, fin: int) -> float:
    """Temps de doublement du risque : ln 2 divisé par la pente de ln q(x) (moindres carrés)."""
    ages = list(range(debut, fin + 1))
    logs = [log(q[age]) for age in ages]
    moyenne_age, moyenne_log = sum(ages) / len(ages), sum(logs) / len(logs)
    pente = (sum((a - moyenne_age) * (v - moyenne_log) for a, v in zip(ages, logs))
             / sum((a - moyenne_age) ** 2 for a in ages))
    return log(2) / pente


def analyser(table: dict[str, list[float]]) -> dict:
    resultats = {}
    for sexe, q in table.items():
        minimum = min(q)
        resultats[sexe] = {
            'age_du_risque_minimal': q.index(minimum),
            'risque_minimal_par_an': minimum,
            'un_sur': round(1 / minimum),
            'risque_a_10_ans': q[10],
            'mediane_si_risque_de_10_ans_constant_ans': mediane_a_risque_constant(q[10]),
            'mediane_si_risque_minimal_constant_ans': mediane_a_risque_constant(minimum),
            'doublement_30_90_ans': doublement(q, 30, 90),
            'risque_a_30_ans': q[30], 'risque_a_90_ans': q[90],
        }
    return resultats


def autotests() -> None:
    # Risque constant de 50 % par an : la moitié du groupe reste au bout d'un an.
    assert isclose(mediane_a_risque_constant(0.5), 1.0)
    # Risque qui double exactement tous les 8 ans : la droite ajustée rend 8.
    artificiel = [1e-4 * 2 ** (age / 8) for age in range(100)]
    assert isclose(doublement(artificiel, 30, 90), 8.0, rel_tol=1e-9)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER / 'resultats.json')
    args = parser.parse_args()
    autotests()
    resultats = {
        'source': 'Social Security Administration, Period Life Table, 2023 (2026 Trustees Report)',
        'adresse': 'https://www.ssa.gov/oact/STATS/table4c6.html',
        'empreinte_sha256': hashlib.sha256(TABLE.read_bytes()).hexdigest(),
        'resultats': analyser(lire(TABLE)),
    }
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for sexe, r in resultats['resultats'].items():
        print(f"{sexe} : risque à 10 ans {r['risque_a_10_ans']:.6f} ; médiane à ce risque "
              f"{r['mediane_si_risque_de_10_ans_constant_ans']:.0f} ans ; doublement {r['doublement_30_90_ans']:.2f} ans")


if __name__ == '__main__':
    main()
