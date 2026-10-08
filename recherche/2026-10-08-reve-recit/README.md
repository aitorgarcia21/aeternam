# Rêve et récit

Cette étude livre un audit d'accès aux données, une réanalyse descriptive d'un tableau publié et un plan exécutable de comparaison de jugements de durée. Elle ne contient aucune nouvelle observation humaine ni paire de durée pendant/après acquise.

## Reproduire

```sh
python3 recherche/2026-10-08-reve-recit/analyse.py
python3 recherche/2026-10-08-reve-recit/verifier.py
python3 recherche/2026-10-08-reve-recit/figures.py
```

L'analyse principale utilise la bibliothèque standard. Le vérificateur utilise NumPy ; les figures utilisent la version de Matplotlib fixée dans `requirements-figures.txt`. L'archive DREAM déjà versionnée est nécessaire à l'inspection du schéma. Aucun accès réseau n'est requis pour ces commandes.

## Réutiliser le plan sur des données appropriées

`schema-paires.csv` est un en-tête vide. Les colonnes portant `_s` expriment des secondes. Les horodatages sont relatifs à une même origine dans l'épisode ; les estimations sont des durées positives. Les identifiants doivent être pseudonymes. Une ligne représente une tentative portant sur un intervalle ; toutes les tentatives doivent être présentes, y compris celles sans rappel ou sans réponse interprétable.

`sommeil_verifie`, `signal_verifie` et `retour_information_avant_apres` acceptent `oui`, `non` ou `inconnu`. Le dernier indique si la durée physique ou la première réponse a été révélée avant le rapport au réveil. `statut_apres` accepte `observe`, `absence_rappel` ou `manquant`. Une absence de rappel ne reçoit jamais une durée de zéro. Les cellules numériques manquantes restent vides ; `NaN`, les infinis et les durées non positives sont refusés.

Les identifiants d'intervalle désignent réellement le même segment borné. Les identifiants de question désignent la même formulation et la même unité. Leur concordance textuelle est nécessaire, mais ne suffit pas : le responsable des données doit vérifier les consignes et la provenance. Les variables de contrôle restent des attestations fournies par le jeu ; le logiciel ne certifie pas le sommeil à partir d'un EEG.

```sh
python3 recherche/2026-10-08-reve-recit/analyse.py --paires chemin/mesures.csv --out chemin/analyse-secondaire.json
```

L'import ne transforme pas automatiquement un fichier en données humaines validées. Il faut documenter sa source, son droit d'usage, sa méthode d'acquisition et l'ensemble des tentatives avant toute interprétation. Un fichier de sortie distinct préserve le bilan documentaire publié.

La réponse pendant le rêve est attendue après la fin de l'intervalle délimité et avant le réveil. Le rapport après réveil doit être recueilli dans le délai de 120 secondes défini par ce plan, sans retour d'information. Cette convention est modifiable dans un nouveau plan explicitement versionné, pas après inspection des résultats sans déclaration.

Le contraste principal est une moyenne des logarithmes des rapports après/pendant, d'abord par personne puis entre personnes. Le bootstrap conserve cette unité ; l'intervalle n'est produit qu'à partir de dix personnes admissibles, seuil opérationnel qui ne garantit pas la validité de l'inférence. La sélection des répondants et les biais de rapport persistent.
