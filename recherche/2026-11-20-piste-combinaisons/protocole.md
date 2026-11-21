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

## Révision du 21 novembre 2026 : viser la pente

### Ce qui a changé

- L'étude « Retarder ou ralentir » (20 novembre) montre que les 27 traitements de l'ITP qui
  allongent la vie, dont 11 comparaisons avec la rapamycine, n'allongent pas le temps de
  doublement du risque. Refaite avec une fragilité individuelle (21 novembre,
  `../2026-11-21-piste-restriction/`), la rapamycine est à λ = 1,03 en médiane (au plus 1,15) :
  elle ne raidit plus la pente, mais aucun ralentissement n'est établi.
- La restriction calorique, elle, ralentit : λ = 1,37 avec 40 % de restriction (intervalle à
  95 % : 1,08 à 1,72), chez des souris femelles génétiquement variées.
- Le tramétinib n'est pas dans l'ITP : sa pente est inconnue. Nous n'avons pas les durées de vie
  individuelles de Gkioni et al. 2025 pour la calculer.

Deux molécules qui retardent, données ensemble, devraient retarder davantage. Cela ne vise pas,
en soi, la pente.

### Changement 1 : la pente devient un critère principal

- λ est mesuré avec le modèle de l'étude du 20 novembre, seuil corrigé par son étalonnage (6,99).
- Avec 221 souris par groupe, le plan ci-dessus aurait moins d'une chance sur deux de voir un
  ralentissement de 1,25 (simulations numériques : 28,5 % avec 150 souris par groupe, 62,5 %
  avec 300). Il en faut 450 par groupe pour 83,5 %, 600 pour 93,5 %.

### Changement 2 proposé : retarder et ralentir ensemble

Un plan 2 × 2 « restriction × rapamycine » : la seule intervention qui ralentit, et la molécule
la plus testée, qui retarde. Question : un retard et un ralentissement s'additionnent-ils ?
Si oui, la combinaison décale la courbe **et** change sa pente.

- Unnikrishnan et al. 2020 prédisent que la combinaison fera mieux que chacune seule ; Ham et al.
  2022 trouvent des effets additifs sur le muscle de souris âgées. Nous n'avons pas trouvé de
  durée de vie de souris publiée qui croise les deux : à revérifier avant tout financement.
- Hypothèse, écrite avant : dans le groupe qui reçoit les deux, λ est supérieur à 1 et le risque
  est décalé (θ inférieur à 1). Réfutation : un intervalle à 95 % de λ entièrement au-dessous de
  1,10 dans ce groupe.
- Effectifs : 450 souris par groupe et par sexe pour le critère λ, soit 1 800 souris par sexe.

### Pour l'humain

Rien ici ne dit qu'une personne vivrait plus longtemps avec ces molécules. Le tramétinib est un
anticancéreux aux effets indésirables connus. Chez l'humain, la seule intervention de cette
liste dont un effet sur le rythme du vieillissement a été mesuré dans un essai randomisé est la
restriction (CALERIE) : voir la piste restriction.
