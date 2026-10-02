#!/usr/bin/env python3
"""Dénominateurs publiés de PRIMA et arithmétique de durée, sans extrapolation clinique."""
from __future__ import annotations
import argparse
import json
from math import isclose
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent


def bornes_manquants(succes: int, evalues: int, total: int) -> tuple[float, float]:
    if not 0 <= succes <= evalues <= total or total == 0:
        raise ValueError("Effectifs incohérents.")
    return succes / total, (succes + total - evalues) / total


def analyser() -> dict:
    r = json.loads((DOSSIER / 'releves.json').read_text(encoding='utf-8'))
    p = r['prima_2025']
    assert p['non_evalues'] == p['implantes'] - p['evalues_12_mois']
    bornes = bornes_manquants(p['amelioration_critere_principal'], p['evalues_12_mois'], p['implantes'])
    assert bornes_manquants(0, 0, 4) == (0, 1)
    assert bornes_manquants(2, 4, 4) == (0.5, 0.5)
    assert isclose(bornes[1] - bornes[0], 6 / 38)
    facteurs = {str(h): 20 * 365.25 * 24 / h for h in (1, 8)}
    assert facteurs['1'] == 8 * facteurs['8']
    return {
        'statut': 'recalcul documentaire et scénario de définition ; aucune simulation biologique',
        'releves': r,
        'prima': {
            'reponse_parmi_evalues': p['amelioration_critere_principal'] / p['evalues_12_mois'],
            'bornes_sur_implantes': list(bornes),
            'interpretation': 'bornes arithmétiques si les six résultats manquants valent tous échec ou tous succès ; ni intervalle de confiance ni estimation imputée',
        },
        'duree': {
            'annees_hypothetiques': 20, 'jours_par_an_convention': 365.25,
            'facteurs_selon_heures_reelles': facteurs,
            'nature': "rapports de durée définissant un scénario ; aucune faisabilité ni accélération mesurée",
        },
        'injection_memoire_autobiographique_aeternam': None,
        'performance_prothese_visuelle_aeternam': None,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER / 'resultats.json')
    args = parser.parse_args()
    args.out.write_text(json.dumps(analyser(), ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print('Dénominateurs, bornes de données manquantes et rapports de durée vérifiés.')
