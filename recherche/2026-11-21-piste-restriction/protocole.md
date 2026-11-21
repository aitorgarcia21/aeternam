# Protocole proposé : la restriction ralentit-elle le vieillissement humain ?

ÆTERNAM n'a mené aucune expérience. Ce document décrit celles qu'il faudrait mener ; leurs
effectifs viennent de `analyse.py`, leurs hypothèses de `sources.md`.

## La question

Chez la souris, la restriction calorique ne fait pas que retarder le vieillissement : elle le
ralentit. Le temps que met le risque de mourir à doubler est multiplié par 1,37 avec 40 % de
restriction (intervalle à 95 % : 1,08 à 1,72). Les 27 traitements de l'ITP, eux, ne
l'allongent pas. Le même ralentissement existe-t-il chez l'humain, et que change-t-il dans les
cellules ?

## Ce qui est montré, et ce qui ne l'est pas

- Montré chez la souris (Di Francesco et al. 2024, refait ici) : 20 % et 40 % de restriction
  ralentissent, le jeûne d'un ou deux jours par semaine non. Femelles seulement, un laboratoire.
- Montré chez le macaque (Mattison et al. 2017) : la restriction modérée améliore la survie
  quand on réunit les deux grandes études, dont l'une, seule, ne voyait pas d'effet. Pente non
  calculée : pas de données individuelles.
- Montré chez l'humain (CALERIE, Waziry et al. 2023) : en deux ans, la restriction ralentit de
  2 à 3 % un rythme du vieillissement mesuré dans le sang (DunedinPACE), avec 11,9 % de
  restriction obtenue en moyenne au lieu des 25 % prescrits.
- Non montré : que ce rythme mesuré dans le sang soit la pente de la mortalité ; qu'il reste
  ralenti au-delà de deux ans ; qu'il ralentisse chez les plus de 50 ans, chez qui le risque de
  mourir monte vraiment.

## Étape 0, sans financement : ce que la restriction change dans les cellules

Les 937 souris de Di Francesco et al. ont des centaines de mesures publiques (sang, système
immunitaire, poids, santé), relevées chaque année. Question : lesquelles changent sous
restriction **et** suivent la pente de chaque souris ? Plan, déposé avant l'analyse :
1. Pour chaque mesure, l'effet du régime à âge fixe (modèle linéaire, génération en strate).
2. Pour chaque mesure, son lien avec le risque de mourir ensuite (modèle de survie à partir de
   l'âge de la mesure).
3. Une mesure « candidate » doit passer les deux, avec une correction pour le nombre de mesures,
   et prédire la survie à l'intérieur de chaque régime, pas seulement entre régimes.
Ce qui réfuterait la piste : aucune mesure ne passe les deux tests. Données et code publics :
ce travail ne demande que du temps.

## Expérience 1, chez l'humain : le rythme du vieillissement sous restriction

### L'hypothèse, écrite avant l'expérience

Chez des adultes de 40 à 65 ans, trois ans de restriction calorique encadrée ralentissent le
rythme du vieillissement mesuré par DunedinPACE. Le résultat qui la réfute : un intervalle de
confiance à 95 % de l'écart de rythme (restriction moins régime libre) entièrement au-dessus
de −1 %, c'est-à-dire un ralentissement de 1 % ou plus exclu.

### Le plan

- Deux groupes tirés au sort : restriction de 20 % de l'apport mesuré au départ, avec
  accompagnement diététique, ou régime habituel. Les adultes de CALERIE avaient de 21 à 50 ans :
  nous visons 40 à 65 ans, l'âge où ce risque, qui double environ tous les huit ans, devient grand.
- Sang prélevé au départ, puis tous les six mois. Les personnes qui mesurent ignorent le groupe.
- Critère principal : DunedinPACE à 36 mois. Critères secondaires : les 19 mesures de sang et
  d'organes dont DunedinPACE est tiré, mesurées directement (pour ne pas dépendre d'une seule
  horloge) ; les horloges PhenoAge et GrimAge ; la composition du corps et l'immunité, puisque la
  restriction de 40 % fait perdre de la masse maigre et modifie le système immunitaire chez la
  souris (Di Francesco et al. 2024).
- Plan d'analyse et seuils déposés publiquement avant le premier participant.
- Suivi médical ; critères d'arrêt individuels fixés à l'avance (perte de poids excessive,
  anémie, troubles du comportement alimentaire).

### Les effectifs

Test bilatéral à 5 %, 90 % de chances de voir l'effet, deux groupes égaux.

| Effet supposé | D'où il vient | Personnes par groupe |
|---|---|---|
| d = 0,27 | CALERIE, en intention de traiter (moyenne de 0,29 et 0,25) | 289 |
| d = 0,43 | CALERIE, pour 20 % de restriction réellement obtenue | 114 |

Nous retenons l'hypothèse prudente : 289 personnes par groupe, 362 à recruter par groupe si un
participant sur cinq abandonne, soit 724 personnes.

### Durée

Trois ans de restriction, plus le recrutement.

### Ce que l'on peut en attendre, et ce que l'on ne peut pas

Un ralentissement de 2 à 3 % ne fait pas vivre beaucoup plus longtemps : appliqué à la table de
mortalité américaine de 2023 à partir de 40 ans, il ajoute environ un an à l'âge médian au
décès (0,8 à 1,4 an selon le sexe et l'effet). Si l'humain répondait comme la souris
(λ = 1,25 à 1,37), il en ajouterait 10 à 16,5. Ces nombres sont des conversions sur des
hypothèses, pas des prévisions. L'expérience dit si l'humain est plus proche de l'un ou de
l'autre.

## Expérience 2, chez la souris : la pente chez les mâles et dans un autre laboratoire

### L'hypothèse, écrite avant l'expérience

La restriction de 40 % commencée à 6 mois multiplie le temps de doublement du risque par plus
de 1, dans les deux sexes. Le résultat qui la réfute : un intervalle de vraisemblance à 95 % de
λ entièrement au-dessous de 1,10.

### Le plan

- Souris génétiquement variées (UM-HET3, celles de l'ITP), les deux sexes, deux sites ; régime
  libre ou restriction de 40 %, à partir de 6 mois ; suivies jusqu'à leur mort.
- Critère principal : λ, avec le modèle de Gompertz de cette étude (et sa version avec
  fragilité), seuil corrigé par l'étalonnage de l'étude du 20 novembre (6,99).
- Une cohorte parallèle, sacrifiée à âges fixes, pour mesurer dans les tissus ce que l'étape 0
  aura désigné.

### Les effectifs

Simulations numériques, pas des mesures (`puissance_pente` dans `analyse.py`) : pour voir un
ralentissement de 1,25 avec le seuil corrigé, il faut 450 souris par groupe pour 83,5 % de
chances, 600 pour 93,5 %. Par sexe : 2 × 450 = 900 souris ; pour les deux sexes, 1 800.

## Budget

À chiffrer sur devis. Aucun prix n'est avancé ici : nous n'en avons pas de source publique
vérifiée.

## Ce qu'un résultat permettrait

- Ralentissement confirmé chez l'humain : la pente du vieillissement humain se règle. La
  question devient de trouver comment obtenir l'effet sans la restriction, que peu de gens
  tiennent, à partir de ce que l'étape 0 aura trouvé dans les cellules.
- Ralentissement exclu : la restriction humaine, telle qu'on sait la tenir, ne suffit pas, et
  il faut le dire.
- Dans aucun cas une restriction sévère ne se conseille sans suivi médical.

## Étape 0 : faite le 21 novembre 2026

Voir `../2026-11-21-restriction-cellules/` (plan enregistré avant le calcul, commit `bcf792f`).
Sur 75 mesures du sang, 25 changent sous restriction et annoncent la survie à régime égal
(après correction par le témoin négatif, qui n'est pas passé : 27 avant). Elles expliquent le
décalage du risque (θ revient vers 1), pas la pente (λ ne baisse pas). Chez les souris nourries
à volonté, les lymphocytes T naïfs reculent avec l'âge et les effecteurs-mémoire avancent ; la
restriction va dans le sens d'un frein pour les quatre mesures, sans le prouver. Prochaine
expérience : suivre les cellules T des mêmes souris dans le temps.
