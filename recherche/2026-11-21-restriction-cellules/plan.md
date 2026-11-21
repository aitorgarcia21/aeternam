# Plan d'analyse : ce que la restriction change dans les cellules du sang

Écrit et enregistré dans Git le 21 novembre 2026, **avant** tout calcul liant une mesure à la
survie. Le script `analyse.py` applique ce plan tel quel ; tout écart sera écrit dans
`sources.md`, avec sa raison.

## Ce que nous avions vu avant d'écrire ce plan

- Les noms des 675 colonnes de `donnees/phenotyping_data.csv`, l'âge médian de chaque série de
  mesures et le nombre de souris mesurées. Aucune moyenne par régime, aucun lien avec la survie.
- Le résumé de l'article de Di Francesco et al. (*Nature* 2024) : les effets de la restriction
  sur la santé y sont décrits comme découplés de la longévité ; la baisse de la graisse et du
  sucre du sang n'y est pas liée à une vie plus longue ; parmi les liens les plus forts avec la
  durée de vie figurent le maintien du poids et des mesures du sang (globules rouges, système
  immunitaire).
- Les deux premières lignes du fichier de résultats des auteurs (`SurvTest.csv`), qui portent
  sur le poids à 3 et 6 mois. Nous n'utilisons pas ce fichier.

Ce plan n'est donc pas aveugle à la littérature ; il l'est aux données de survie.

## La question

La restriction calorique ralentit le vieillissement de ces souris (temps de doublement du
risque multiplié par 1,37 avec 40 % de restriction, `../2026-11-21-piste-restriction/`).
Quelles mesures des cellules du sang changent sous restriction **et** annoncent la survie de
chaque souris, à régime égal ?

## Les mesures

Famille principale : les cellules du sang, à leur première mesure après le début des régimes
(6 mois, 183 jours environ).

- Numération sanguine (`Y1_CBC_*`, vers 343 jours) : 26 mesures (les colonnes `AgeInDays` et
  `BWTest` ne sont pas des mesures du sang).
- Cytométrie des cellules immunitaires (`Y2_FLOW_*`, vers 490 jours ; la série `Y1_FLOW`, à
  155 jours, précède les régimes) : 49 mesures.

Famille secondaire, rapportée sans porter la conclusion : les autres mesures à leur première
série après le début des régimes (`Y1_Echo`, `Y1_PIXI`, `Y1_Rotarod`, `Y1_Void`, `Y1_Wheel`,
`Y1_AS`, `Y1B_Frailty`, `Y1B_Grip`, `Y1D_BW`, `Y2_Glu.F`, `Y2_Glu.NF`, `Y2_MetCage`).

Témoin négatif : les mesures prises **avant** les régimes (`Y1_FLOW` à 155 jours, `Y1_Glu.F`,
`Y1_Glu.NF`, `Y1_MetCage` vers 99 jours, `Y1A_Frailty`, `Y1A_Grip`, `Y1A_BW`). Le régime ne
peut pas encore les avoir changées : le test 1 devrait y trouver environ 5 % de p < 0,05 et
aucune découverte après correction.

Une mesure est écartée si moins de 300 souris l'ont, ou si elle a moins de 10 valeurs
distinctes. Chaque mesure est transformée en rangs normalisés (transformation inverse normale
des rangs, constante de Blom 3/8) sur les souris analysées.

## Les tests

**Test 1, l'effet du régime.** Sur les souris nourries à volonté, restreintes de 20 % et de
40 % : régression linéaire de la mesure sur la dose (0 ; 0,2 ; 0,4), l'âge au jour de la
mesure et la génération (6 générations). Test bilatéral du coefficient de la dose (loi normale,
les effectifs dépassant 400).

**Test 2, le lien avec la survie à régime égal.** Sur toutes les souris mesurées (cinq
régimes) : modèle de Cox de la mort après l'âge de la mesure (troncature à gauche à cet âge,
souris retirées censurées), avec la mesure, le régime (4 indicatrices) et la génération (5
indicatrices). Test de Wald du coefficient de la mesure.

**Correction.** Benjamini-Hochberg sur la famille principale, séparément pour chaque test
(75 mesures).

**Candidate.** Une mesure est candidate si q < 0,05 au test 1, q < 0,05 au test 2, et si la
restriction la déplace du côté où le risque de mourir est plus bas (signe du coefficient de
dose opposé au signe du coefficient de Cox).

**Ce qui réfuterait la piste.** Aucune mesure candidate dans la famille principale.

## Ce que l'on rapporte pour chaque candidate

1. **La part de l'effet de la restriction qu'elle porte.** Le coefficient de Cox de la
   restriction de 40 % (contre le régime à volonté) sans la mesure, puis avec, sur les mêmes
   souris : part expliquée = 1 − (avec / sans).
2. **La pente.** Le modèle de Gompertz de la piste restriction (40 % contre volonté, entrée au
   plus tard entre 365 jours et l'âge de la mesure), sans puis avec les candidates de la même
   série de mesures en covariables (risque multiplié par exp(β·mesure)) : λ avant et après.
   Descriptif, sans seuil.
3. **Le poids.** Le test 2 refait en ajoutant le poids pesé le jour de la mesure (`BWTest`),
   puisque la restriction fait maigrir.
4. **Le rythme.** Pour les candidates de la numération (mesurée vers 343 et 707 jours) et de la
   cytométrie (vers 490 et 853 jours) : la variation de chaque souris entre ses deux mesures ;
   sa moyenne chez les souris nourries à volonté (ce que l'âge change), et l'effet de la dose
   sur cette variation (régression avec la génération). Descriptif : seules les souris en vie à
   la seconde mesure comptent.

## Limites connues d'avance

Une seule expérience, des femelles, un laboratoire. Une association à régime égal n'est pas une
cause : une mesure peut annoncer la mort sans y être pour rien. Les mesures du sang ne sont pas
les cellules des organes. Ce travail désigne des pistes à tester, il ne les démontre pas.
