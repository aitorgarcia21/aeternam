# Répartition des signaux publiés

- Question : comment les 150 signaux du tableau 1 de Konkoly et al. 2026 se répartissent-ils entre les personnes ?
- Message : deux personnes produisent 68 % des signaux ; un signal supplémentaire n'est pas une personne indépendante supplémentaire.
- Données : les 13 lignes du tableau, y compris les deux lignes à zéro ; quatre catégories additionnées par personne. Identifiants remplacés par le numéro de ligne source. Nombres de sessions conservés dans le CSV pour le contexte.
- Famille : comparaison, barres horizontales triées ; axe de quantité commençant à zéro, étiquettes numériques directes.
- Support : figure scientifique autonome SVG et PNG par Matplotlib, intégrée au site Aeternam existant. Pas de nouveau moteur HTML ni de composant interactif.
- Palette : une racine bleue `#3475a3`, texte `#252525`, guides gris ; ordre et valeurs portent l'information sans dépendre de la couleur.
- Emprise : 6,4 × 5,8 pouces, adaptée à la colonne d'article et contrôlée à 390 px. Pas de légende redondante ; titre neutre, dénominateur et référence visibles.
- Portée : réanalyse d'un tableau tiers, pas mesure de durée ni performance d'un dispositif Aeternam. Nombres de sessions différents ; pas d'inférence sur une aptitude individuelle.
- Livraison : `signaux-par-personne.svg`, `signaux-par-personne.png`, source `figures.py`. Contrôle visuel du PNG exact puis de l'article sur mobile et ordinateur.
