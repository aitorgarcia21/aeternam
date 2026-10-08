# Vérification locale du 8 octobre 2026

Les trois articles sont des revues critiques avec calculs illustratifs.
Ils ne constituent pas de nouvelles mesures de relativité ou de rayonnement.

- `analyse.py` exécuté, autotests réussis ; second calcul avec `--out` comparé
  octet par octet au résultat versionné : identique.
- Contrôles mathématiques : transformation de Lorentz, invariant d'intervalle,
  addition de rapidités, potentiel par coquilles, limite faible de la solution
  intérieure homogène exacte, première loi thermodynamique et domaines physiques.
- Calculs principaux : 0,9944751381 c pour la composition 0,9 c / 0,9 c ;
  34,4454 ps/an pour 1 cm ; 0,878724 s sur 80 ans pour le centre homogène.
  Conversion de l'estimation PREM publiée : 1,384642 s sur 80 ans.
- Les 2,49 ans PREM sont explicitement cités, pas revendiqués comme une
  réanalyse locale. Les trajectoires statiques, orbitales et en chute sont distinguées.
- Construction complète par `python3 site/generer.py` : six sujets, dix-neuf articles.
- Quatre nouvelles pages ouvertes dans Chrome à 1280 et 390 pixels de largeur :
  aucun débordement de page, aucune erreur JavaScript, aucune erreur KaTeX,
  aucune image cassée ni marqueur numérique restant.
- Les trois articles rendent respectivement 13, 13 et 5 expressions KaTeX.
- Figures SVG vues dans leur page sur mobile, PNG exportés également inspectés.
  Les trois tableaux numériques tiennent dans la largeur mobile.
- Liens internes et ancres des trois articles et de la rubrique vérifiés.

Les contrôles portent sur le contenu et la construction locale. Le statut de
publication et le contrôle global GitHub Actions doivent être vérifiés séparément
sur le commit effectivement envoyé ; ce document ne les présume pas réussis.
