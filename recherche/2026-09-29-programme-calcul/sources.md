# Programme de calcul Aeternam — 29 septembre 2026

## Question et périmètre

Commencer la recherche sur le cerveau, le rêve et le temps vécu avec les ressources existantes : données ouvertes, statistiques publiées, modèles et calculs locaux. Aucun recrutement, aucune stimulation et aucun achat. Les cinq axes publics sont accessibles dans `/programme/` : accès, contenu, temps, mémoire, méthodes de calcul.

Le programme central garde l'objectif d'une vie en une nuit. Une histoire à ellipses, la vitesse de rejeu neuronal, une durée racontée et une durée d'action mesurée ne sont pas des substituts interchangeables à cet objectif.

## Sources et disponibilité vérifiées

| Source primaire | Données utilisées | Traitement ici |
| --- | --- | --- |
| [DREAM, Wong et al., Nature Communications, 2025](https://doi.org/10.1038/s41467-025-61945-1) ; [Tononi Serial Awakenings v3](https://doi.org/10.26180/23306054.v3) | `Records.csv` et `AdditionalData.csv`, archive publique sous CC BY 4.0 | Réanalyse individuelle de 287 réveils ; transformation décrite ci-dessous |
| [Erlacher et al., 2014, tableau 2](https://doi.org/10.3389/fpsyg.2013.01013) | Moyennes, effectifs et tests t appariés | Différences de durée et intervalles reconstruits à partir de résumés arrondis |
| [Konkoly et al., 2021, tableau 2](https://doi.org/10.1016/j.cub.2021.01.026) | Effectifs agrégés d'essais de communication | Recalcul de taux selon différents dénominateurs ; pas d'inférence par essai indépendant |
| [Dormio, Haar Horowitz et al., 2020](https://doi.org/10.1016/j.concog.2020.102938) | Décomptes de récits avec thème | Différence et rapport de proportions descriptifs |
| [Konkoly et al., lucidité à domicile, 2024](https://doi.org/10.1016/j.concog.2024.103759) | Article ; données annoncées sur demande | Contexte documentaire seulement ; pas de réanalyse individuelle |
| [Bellaiche et al., Dormio Light, 2024](https://doi.org/10.3389/frsle.2024.1258345) | Article ; données annoncées par les auteurs | Approche logicielle déjà existante ; aucune nouveauté revendiquée par Aeternam sur ce principe |
| [Haar Horowitz et al., incubation jusqu'au REM, 24 juin 2026](https://doi.org/10.3389/frsle.2026.1812535) | Résultats 3.2 : 7/8 participants avec REM, 11 au total, 10/21 récits REM | Recalcul des dénominateurs, sans groupe contrôle et sans reconstruction de données individuelles |
| [Horowitz et al., créativité, 2023](https://doi.org/10.1038/s41598-023-31361-w) | Article ; données sur demande | Piste distincte sur la performance après sommeil, pas mesure d'années vécues |
| [Kurth-Nelson et al., 2016](https://doi.org/10.1016/j.neuron.2016.05.028) | Séquences neuronales de représentations | Contexte de mémoire ; aucune conversion en expérience consciente accélérée |

Les deux références de 2024 et le pilote de 2026 ne donnent pas de lien direct vers leurs données individuelles dans leur déclaration de disponibilité. Nous n'avons contacté personne et n'avons pas inventé ces observations. La publication d'un article ne suffit pas à rendre ses données brutes téléchargeables.

## Réanalyse individuelle DREAM

Archive : `https://ndownloader.figshare.com/files/59168237`, déjà conservée dans `../2026-09-29-temps-reve/donnees/tononi_part1.zip`. SHA-256 : `e4d7932ed96e65fe6ff1e25df9fea0229b2e7e3d3cca1730f9dd637531ff62b0`.

La jointure se fait sur `Filename`, dont l'unicité et la couverture sont vérifiées dans les deux tables. `Subject ID` définit la grappe statistique. Tous les enregistrements ont `Last sleep stage=2`. Les codes d'expérience sont conservés : 0, 1, 2 ; les durées sont renseignées sur les 124 lignes de code 2, parmi 287 réveils de 39 personnes. Les 163 absences ne sont jamais converties en zéro.

Variable exploratoire : appartenance à une classe de durée d'au moins une minute (codes 4, 5 ou 6). Pas de milieu de classe imposé, et donc pas de fausse moyenne en secondes. Deux estimands sont séparés : proportion parmi les rapports disponibles et moyenne des proportions individuelles. Le second donne le même poids aux personnes, malgré des nombres différents de réveils.

Bootstrap percentile de 20 000 rééchantillonnages des 39 personnes, avec remise. Les lignes d'un sujet ne sont pas tirées indépendamment. L'intervalle obtenu n'est pas une garantie de représentativité de la population générale. La sélection des expériences rappelées reste constitutive de l'estimand.

Exploration secondaire : différence des proportions de classes longues entre réponses 1 et 0 à la question `Perception`, calculée par personne puis moyennée parmi les 20 personnes qui ont les deux catégories. L'intervalle recouvre zéro. Aucun test causal, aucune hypothèse confirmatoire préenregistrée, aucune recherche exhaustive de seuils pour obtenir un résultat significatif.

Les identifiants de sujets dans `resultats.json` sont les identifiants pseudonymes du jeu ouvert. Aucun récit personnel n'est reproduit.

## Tâches chronométrées

Pour une tâche : différence Δ = moyenne en rêve − moyenne à l'éveil, erreur type SE = Δ/t, intervalle bilatéral Δ ± t(0,975 ; n−1) × SE. Les quantiles sont calculés par la fonction de Student conservée dans le script sur les interventions ; ils sont contrôlés indépendamment contre SciPy pendant l'audit local.

Les résumés publiés sont arrondis. Les intervalles sont marginaux, sans correction des trois comparaisons. Comptage et marche partagent des participants. Pas de méta-analyse entre ces tâches, pas de ratio global du temps vécu.

## Laboratoire numérique

54 000 jeux simulés (6 000 pour chacune des neuf configurations). Pour chaque personne i et mesure j :

`log_ratio_ij = μ + 0,35 × (sqrt(ρ) × Z_i + sqrt(1−ρ) × Z_ij)`.

Les Z sont des normales indépendantes. μ vaut 0 sous le nul, puis log(1,2) dans le scénario de gain ; les mêmes bruits sont réutilisés pour comparer les effets sans ajouter de variance Monte-Carlo. Effectifs : 20, 40, 80 personnes ; trois répétitions ; ρ : 0, 0,3, 0,6. Les paramètres sont choisis, pas appris sur un dispositif Aeternam.

Le test pertinent porte sur la moyenne des log-ratios de chaque personne. Le test naïf considère les 3n répétitions comme indépendantes. Test t unilatéral à 2,5 %, seuil t(0,975). Sous ces hypothèses gaussiennes, la statistique par sujet est bien calibrée. La dépendance invalide le dénominateur du test naïf.

L'erreur Monte-Carlo maximale à 95 % pour chaque taux estimé est d'environ 1,27 point (1,96 × sqrt(0,25 / 6000)). Les simulations constituent un contrôle de méthode, jamais une expérience humaine ni une prévision de succès.

## Temps, scènes et mémoire

Le rapport 87 660 correspond à 80 années de 365,25 jours, 24 heures vécues par jour, en huit heures. Avec 16 heures vécues par jour, l'objectif arithmétique devient 58 440. Cent scènes choisies de trois minutes totalisent cinq heures. Ce dernier calcul ne prouve ni la possibilité de diriger ces scènes en rêve ni leur continuité autobiographique. Il rend explicite la différence entre une vie continue et une sélection de moments représentant une vie.

## Exécution

Depuis la racine du dépôt :

```sh
python3 recherche/2026-09-29-programme-calcul/analyse.py
```

Dépendance : numpy, déjà utilisée dans le dépôt. Les scripts de temps du rêve et d'interventions sont importés pour leurs fonctions et leurs données sourcées. Leurs blocs principaux ne s'exécutent pas à l'import. La graine est fixe ; les sources et champs manquants sont conservés dans les résultats.
