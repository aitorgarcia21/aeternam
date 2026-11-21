# Protocole proposé : la restriction freine-t-elle le vieillissement des cellules T ?

ÆTERNAM n'a mené aucune expérience. Ce document décrit celle qu'il faudrait mener ; son effectif
vient de `analyse.py` (`rythme.souris_pour_90_pourcent`), ses observations de `resultats.json`.

## La question

Sous restriction calorique, le sang des souris est plus jeune, et ce sang annonce une vie plus
longue à régime égal. Mais une mesure prise une seule fois explique le décalage du risque, pas
sa pente. La restriction ralentit-elle le vieillissement des cellules T elles-mêmes ?

## Ce qui est montré, et ce qui ne l'est pas

- Montré (ce dossier) : chez les souris nourries à volonté, entre 490 jours et un an plus
  tard, la part des lymphocytes T naïfs recule et celle des lymphocytes T effecteurs-mémoire
  avance, pour les CD8 comme pour les CD4.
- Non montré : que la restriction freine ces changements. Pour les quatre mesures, l'effet de
  la dose va dans le sens d'un frein ; le plus net (CD8 effecteurs-mémoire) donne z = −1,7
  (p = 0,09) sur 297 souris mesurées deux fois, soit environ un quart d'écart-type de moins
  pour 40 % de restriction. Seules les souris encore en vie à la seconde mesure comptent.

## L'hypothèse, écrite avant l'expérience

La dose de restriction (0, 20 % ou 40 %, à partir de 6 mois) réduit l'augmentation, entre 16 et
28 mois, de la part des lymphocytes T CD8 effecteurs-mémoire parmi les CD8. Le résultat qui la
réfute : un intervalle de confiance à 95 % de l'effet de la dose qui exclut un frein de la
moitié de l'effet observé ici (un huitième d'écart-type pour 40 % de restriction).

## Le plan

- Souris génétiquement variées (Diversity Outbred ou UM-HET3), les deux sexes, trois régimes
  à partir de 6 mois : volonté, 20 % et 40 % de restriction, en groupes égaux.
- Cytométrie du sang à 16 et 28 mois, mêmes marqueurs (CD4, CD8, CD44, CD62L) et même
  protocole de marquage pour toutes les souris ; analyse des échantillons dans un ordre tiré au
  sort, par des personnes qui ignorent le régime.
- Critère principal : la variation de la part des CD8 effecteurs-mémoire entre les deux
  mesures, en rangs normalisés ; régression sur la dose, avec le sexe et la cohorte.
- Critères secondaires : les trois autres mesures (CD8 naïfs, CD4 naïfs, CD4
  effecteurs-mémoire) ; la survie après 28 mois, pour relier la vitesse de ces changements à la
  pente du risque.
- Plan d'analyse et seuils déposés publiquement avant la première mesure.

## L'effectif

Pour voir, avec 90 % de chances (test bilatéral à 5 %), un effet de la taille de celui observé :
environ 1 100 souris encore en vie et mesurées à 28 mois. Il faut en mettre davantage en
expérience, puisqu'une part meurt avant : le nombre exact dépend de la survie à 28 mois dans
chaque régime, à calculer avec la lignée choisie avant le dépôt du plan. Des mesures plus
fréquentes (tous les trois mois) réduiraient ce nombre ; il faudra le simuler avant de choisir.

## Budget

À chiffrer sur devis. Aucun prix n'est avancé ici : nous n'en avons pas de source publique
vérifiée.

## Ce qu'un résultat permettrait

- Frein confirmé : la restriction ralentit le vieillissement d'un type de cellules précis, que
  l'on sait mesurer dans le sang, chez la souris comme chez l'humain. C'est une cible pour
  obtenir l'effet de la restriction autrement, et un critère mesurable dans un essai humain.
- Frein exclu : la restriction rajeunit le sang sans changer la vitesse à laquelle les cellules
  T vieillissent, et la pente se joue ailleurs.
