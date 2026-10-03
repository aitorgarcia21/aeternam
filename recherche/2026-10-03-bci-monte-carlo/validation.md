# Validation de l’analyse

Évaluation : partage avec réserves explicites, comme simulation conditionnelle. Aucune estimation clinique du nombre de données nécessaires n’est établie.

## Méthode

La question, les huit budgets, quatre hypothèses et cinq conditions de bruit sont exécutés. Les paramètres proviennent de 540 essais de douze personnes ; les nouvelles observations et tous les résultats de calibration sont simulés. Les mêmes tirages sont réutilisés pour les comparaisons appariées, avec indépendance entre apprentissage et test.

## Points importants pour l’interprétation

- Le coût des 256 observations cibles non étiquetées doit accompagner tout seuil de la correction par référence. Une réduction des essais étiquetés n’est pas une réduction démontrée du nombre total d’observations personnelles.
- Les intervalles mesurent la précision numérique du Monte-Carlo, conditionnellement aux paramètres. La variabilité et l’incertitude humaines ne sont pas couvertes par ces intervalles.
- Les contrastes ajustés sur 45 essais par personne peuvent être surestimés. Le stress à contraste divisé par deux fait disparaître l’atteinte du critère sur la grille ; ce résultat doit être aussi visible que le scénario empirique.
- Les budgets supérieurs à 45 extrapolent la distribution ajustée. Les runs d’origine ne sont pas des journées indépendantes.
- Le minimum à 128 dans le bruit non corrigé se situe près du seuil moyen de 5 points. Il ne faut pas présenter le rapport 128/64 comme une économie humaine certaine.
- Le bruit est ajouté aux caractéristiques ; le montage MEG de Beihang et les réseaux de Shenzhen ne sont pas reproduits. Un gain logiciel simulé n’est pas une performance matérielle.

## Contrôles effectués

`verification.json` conserve la comparaison des décisions avec SciPy, de la régression avec scikit-learn et des agrégations avec la bibliothèque standard. Les contrôles internes sont dans `resultats.json`, avec un scénario nul, un cas analytique et le diagnostic descriptif sur un run humain réservé.

## Visuels et restitution

Les deux figures utilisent les mêmes axes. Les quantités sur l’abscisse doublent à chaque graduation. Les bandes sont nommées Monte-Carlo et le seuil de 5 points est présenté comme choix exploratoire. Les tableaux dérivent du même JSON que les figures. La rubrique du blog est BCI ; « simulation » désigne ici une méthode, pas la rubrique consacrée à l’hypothèse d’un Univers simulé.

## Ce qui reste non vérifié

Validité prédictive chez de nouvelles personnes, profils non représentés, artefacts temporels et anatomie, matériel de référence réel, stabilité entre jours, fatigue, apprentissage de la tâche et bénéfice fonctionnel en usage libre. Ces limites n’empêchent pas de publier l’expérience numérique ; elles empêchent de la présenter comme mesure clinique.
