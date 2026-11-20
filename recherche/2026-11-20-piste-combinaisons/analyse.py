#!/usr/bin/env python3
"""Deux molécules qui allongent la vie des souris s'additionnent-elles ? Et que faut-il pour le savoir ?

Entrée : releves.json, des nombres publiés relevés mot pour mot (aucune donnée individuelle).

1. Gkioni et al. 2025 (rapamycine, tramétinib, les deux, témoins menés en même temps) :
   - la médiane attendue si les effets s'ajoutent (somme des pourcentages, ou produit des rapports) ;
   - l'interaction sur les risques : rapport entre l'effet du tramétinib avec rapamycine et son
     effet seul. 1 = les effets se multiplient sur le risque (« additifs » sur son logarithme),
     moins de 1 = la combinaison fait mieux. Son incertitude est reconstruite à partir des
     intervalles publiés, en supposant les deux estimations indépendantes (elles partagent en
     réalité des animaux : l'incertitude donnée ici est une approximation).
2. La puissance que cette étude avait pour voir l'interaction qu'elle a observée.
3. Le nombre de morts qu'un plan factoriel 2 × 2 doit observer pour établir une interaction
   donnée : D = 16 (z_alpha + z_puissance)² / ln(interaction)², réparti également entre les
   quatre groupes ; et pour un effet simple : D = 4 (z_alpha + z_puissance)² / ln(rapport)²
   (formule de Schoenfeld, test bilatéral à 5 %).
4. Strong et al. 2022 (rapamycine + acarbose) : comparaison descriptive seulement, la
   rapamycine seule venant d'autres cohortes.

Ce sont des calculs sur des résultats publiés chez la souris ; rien ici ne porte sur l'humain.
Bibliothèque standard seule. `--out` choisit le fichier de résultats.
"""
from __future__ import annotations

import argparse
import json
from math import erf, isclose, log, sqrt
from pathlib import Path
from statistics import NormalDist

DOSSIER = Path(__file__).resolve().parent
Z = NormalDist()
ALPHA = 0.05


def repartition(x: float) -> float:
    return 0.5 * (1 + erf(x / sqrt(2)))


def ecart_type_log(bas: float, haut: float) -> float:
    """Écart-type du logarithme d'un rapport, à partir de son intervalle à 95 %."""
    return (log(haut) - log(bas)) / (2 * Z.inv_cdf(0.975))


def interaction(seul: list[float], avec: list[float]) -> dict:
    rapport = avec[0] / seul[0]
    et = sqrt(ecart_type_log(*seul[1:]) ** 2 + ecart_type_log(*avec[1:]) ** 2)
    z = log(rapport) / et
    return {'rapport': rapport, 'ecart_type_log': et, 'z': z, 'p_bilaterale': 2 * (1 - repartition(abs(z))),
            'puissance_pour_cet_ecart': repartition(abs(log(rapport)) / et - Z.inv_cdf(1 - ALPHA / 2))}


def morts_interaction(rapport: float, puissance: float) -> float:
    return 16 * (Z.inv_cdf(1 - ALPHA / 2) + Z.inv_cdf(puissance)) ** 2 / log(rapport) ** 2


def morts_effet_simple(rapport: float, puissance: float) -> float:
    return 4 * (Z.inv_cdf(1 - ALPHA / 2) + Z.inv_cdf(puissance)) ** 2 / log(rapport) ** 2


def analyser(releves: dict) -> dict:
    g = releves['gkioni_2025']
    sortie = {'gkioni_2025': {}, 'plan': {}, 'strong_2022': {}}
    for sexe in ('femelles', 'males'):
        m, r = g['mediane_pourcent'][sexe], g['rapport_de_risque'][sexe]
        produit = ((1 + m['trametinib'] / 100) * (1 + m['rapamycine'] / 100) - 1) * 100
        combinaison = r['rapamycine_seule'][0] * r['trametinib_avec_rapamycine'][0]
        autre_chemin = r['trametinib_seul'][0] * r['rapamycine_avec_trametinib'][0]
        sortie['gkioni_2025'][sexe] = {
            'mediane_observee': m['combinaison'],
            'mediane_attendue_somme': m['trametinib'] + m['rapamycine'],
            'mediane_attendue_produit': produit,
            'ecart_a_la_somme_points': m['combinaison'] - (m['trametinib'] + m['rapamycine']),
            'risque_combinaison_contre_temoin': combinaison,
            'risque_combinaison_autre_chemin': autre_chemin,
            'risque_attendu_si_additif': r['trametinib_seul'][0] * r['rapamycine_seule'][0],
            'interaction': interaction(r['trametinib_seul'], r['trametinib_avec_rapamycine']),
        }
    observee = sortie['gkioni_2025']['femelles']['interaction']['rapport']
    for nom, rapport in (('interaction_observee_femelles', observee), ('interaction_0_75', 0.75), ('interaction_0_80', 0.80)):
        sortie['plan'][nom] = {'rapport': rapport} | {
            f'morts_puissance_{int(p * 100)}': morts_interaction(rapport, p) for p in (0.8, 0.9)} | {
            f'morts_par_groupe_puissance_{int(p * 100)}': morts_interaction(rapport, p) / 4 for p in (0.8, 0.9)}
    for nom, rapport in (('effet_simple_0_70', 0.70), ('effet_simple_0_80', 0.80)):
        sortie['plan'][nom] = {'rapport': rapport} | {
            f'morts_deux_groupes_puissance_{int(p * 100)}': morts_effet_simple(rapport, p) for p in (0.8, 0.9)}
    s, acarbose = releves['strong_2022']['mediane_pourcent'], releves['harrison_2014']['mediane_pourcent']
    for sexe in ('males', 'femelles'):
        sortie['strong_2022'][sexe] = {
            'combinaison_observee': [s[sexe]['combinaison_deux_sites'], s[sexe]['combinaison_trois_sites']],
            'somme_des_effets_seuls': [s[sexe][f'rapamycine_seule_{an}'] + acarbose[sexe]['acarbose'] for an in (2009, 2006)],
            'limite': 'cohortes différentes : comparaison descriptive, pas un test',
        }
    return sortie


def autotests() -> None:
    assert isclose(repartition(0), 0.5) and isclose(repartition(1.959964), 0.975, abs_tol=1e-6)
    assert isclose(ecart_type_log(1 / 2, 2), log(2) / Z.inv_cdf(0.975))
    # Deux effets identiques avec et sans l'autre molécule : aucune interaction.
    neutre = interaction([0.5, 0.4, 0.625], [0.5, 0.4, 0.625])
    assert isclose(neutre['rapport'], 1) and isclose(neutre['p_bilaterale'], 1)
    # Schoenfeld, rapport 0,5, puissance 80 % : 65,3 morts ; l'interaction en demande quatre fois plus.
    assert isclose(morts_effet_simple(0.5, 0.8), 65.35, abs_tol=0.01)
    assert isclose(morts_interaction(0.5, 0.8), 4 * morts_effet_simple(0.5, 0.8))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DOSSIER / 'resultats.json')
    args = parser.parse_args()
    autotests()
    resultats = analyser(json.loads((DOSSIER / 'releves.json').read_text(encoding='utf-8')))
    args.out.write_text(json.dumps(resultats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for sexe, r in resultats['gkioni_2025'].items():
        i = r['interaction']
        print(f"{sexe} : médiane +{r['mediane_observee']} % contre +{r['mediane_attendue_somme']:.1f} % attendus ; "
              f"interaction {i['rapport']:.3f} (p = {i['p_bilaterale']:.3f}, puissance {i['puissance_pour_cet_ecart']:.0%})")
    for nom, p in resultats['plan'].items():
        print(nom, {k: round(v, 3 if k == 'rapport' else 0) for k, v in p.items()})


if __name__ == '__main__':
    main()
