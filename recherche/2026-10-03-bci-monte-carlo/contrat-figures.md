# Figures de la simulation BCI

- Support : figures scientifiques exportables SVG/PNG, intégrées au blog de recherche existant. Rendu standard Matplotlib ; pas de bibliothèque JavaScript supplémentaire.
- Question 1 : comment varie le gain moyen avec le nombre d’essais étiquetés, selon le bruit ? Trois courbes appariées du scénario empirique, sept budgets strictement positifs.
- Question 2 : le seuil résiste-t-il à d’autres hypothèses ? Trois courbes après correction par référence, mêmes aléas et mêmes axes.
- Famille : courbes à marqueurs. Abscisse logarithmique en base deux, de 4 à 256 ; le budget zéro définit la référence du gain et figure dans le tableau numérique.
- Ordonnée commune : gain en points, de −1 à 10. Zéro visible, critère exploratoire +5 indiqué. Bandes : intervalle Monte-Carlo de la moyenne, conditionnel au modèle fixé.
- Palette : or, bleu et gris du site sombre. Carrés, cercles, triangles et styles de traits distinguent aussi les séries sans couleur.
- Taille : 3,9 × 4,5 pouces, affichage limité à 520 px ; contrôle dans une page de 390 px et une de 1440 px. Titres et contexte dans le HTML de l’article ; aucune date sous son titre principal.
- Limites près des figures : 600 campagnes par hypothèse, 12 profils humains d’origine ; répétitions appariées, pas 600 nouvelles personnes mesurées. Les seuils restent une grille exploratoire conditionnelle.
