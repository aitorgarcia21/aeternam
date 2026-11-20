# Protocole proposé : deux molécules font-elles mieux que s'ajouter ?

ÆTERNAM n'a mené aucune expérience. Ce document décrit celle qu'il faudrait mener ; ses
effectifs viennent de `analyse.py`, ses hypothèses de `sources.md`.

## La question

Chez la souris, la rapamycine et le tramétinib donnés ensemble allongent la vie plus que chacun
seul. Leurs effets s'ajoutent-ils seulement, ou la combinaison fait-elle mieux ?

## Ce qui est montré, et ce qui ne l'est pas

- Montré (Gkioni et al. 2025) : chaque molécule allonge la vie des deux sexes ; la combinaison
  fait mieux que chaque molécule seule.
- Non montré : une interaction. Chez les femelles, l'effet du tramétinib est plus fort en
  présence de rapamycine (rapport 0,65), mais l'étude avait 37 % de chances de détecter un écart
  de cette taille. Chez les mâles, le rapport est de 1,11 : les effets s'ajoutent.
- Non montré : que ce résultat se retrouve dans une autre lignée, un autre laboratoire, ou chez
  une autre espèce.

## L'hypothèse, écrite avant l'expérience

Chez la femelle, le rapport entre l'effet du tramétinib avec rapamycine et son effet seul est
inférieur à 1. Le résultat qui la réfute : un intervalle de confiance à 95 % de ce rapport
entièrement au-dessus de 0,80.

## Le plan

- Quatre groupes égaux menés en même temps : témoins, rapamycine, tramétinib, les deux.
  Doses et calendriers : ceux de l'étude publiée, pour que la comparaison ait un sens.
- Souris génétiquement variées (UM-HET3), pour ne pas dépendre d'une lignée ; la lignée de
  l'étude d'origine (C3B6F1) en second bras si le budget le permet.
- Les deux sexes, analysés séparément : l'hypothèse porte sur les femelles, les mâles servent
  de contrôle du résultat additif.
- Répartition au hasard par cage ; personnel qui relève les morts sans connaître le groupe.
- Au moins deux sites, avec les mêmes aliments préparés par un seul fournisseur.

## Les effectifs

Test bilatéral à 5 %, formule de Schoenfeld pour une interaction dans un plan 2 × 2.

| Interaction réelle | Morts à observer (80 %) | Morts à observer (90 %) | Par groupe (90 %) |
|---|---|---|---|
| 0,65 (observée) | 660 | 884 | 221 |
| 0,75 | 1 517 | 2 031 | 508 |
| 0,80 | 2 522 | 3 376 | 844 |

Ces nombres comptent des morts, pour un seul sexe. Toute souris retirée avant sa mort doit être
remplacée dans le calcul. Avec les deux sexes et 221 souris par groupe : 1 768 souris.

## Ce que l'on mesure

- Critère principal : la durée de vie, de l'entrée dans l'étude à la mort naturelle ou à
  l'euthanasie selon des critères fixés à l'avance.
- Critères secondaires : état de santé à âges fixes, tumeurs relevées à l'autopsie, poids.
- Analyse : modèle de Cox avec les deux traitements et leur interaction, par sexe, stratifié par
  site. Le plan d'analyse est déposé publiquement avant le début.

## Durée

La vie médiane des témoins de l'étude publiée dépasse deux ans : l'expérience dure environ
quatre ans, du premier animal à la dernière mort.

## Budget

À chiffrer sur devis auprès d'animaleries habilitées. Aucun prix n'est avancé ici : nous n'en
avons pas de source publique vérifiée.

## Ce qu'un résultat permettrait

- Interaction confirmée : il existe une synergie entre deux voies du vieillissement chez un
  mammifère. L'étape suivante est de chercher la troisième molécule, avec le même plan.
- Interaction exclue : les effets s'ajoutent, et l'on sait combien chaque molécule apporte.
- Dans les deux cas, cela ne dit rien d'un effet chez l'humain : le tramétinib est un
  médicament anticancéreux dont les effets indésirables sont connus.
