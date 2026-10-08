# Validation locale — 8 octobre 2026

- Tableau 1 de Konkoly et al. 2026 relu dans le PDF de l'auteur et sur l'image exacte de la page 367. Les 13 lignes transcrites donnent 150 signaux, 11 personnes avec signal, 102 signaux pour les deux plus grandes contributions et 27 sessions répertoriées. Les 19 sessions avec signaux proviennent du texte de l'article, pas du calcul du nombre de sessions totales.
- Empreintes du PDF de référence, du CSV, du protocole et de l'archive DREAM conservées. Les tableaux DREAM ont été réellement inspectés et leurs clés vérifiées. Aucun jeu apparié de jugements de durée n'a été acquis ; la sortie maintient `null` pour le contraste principal.
- `analyse.py` : 17 autotests, dont refus des doublons, chronologies impossibles, données non finies et zéro remplaçant une durée ; conservation des absences ; appariement des questions et intervalles ; invariance d'unité et pondération par personne.
- `verifier.py` : second relevé des totaux individuels, calcul de référence des moyennes et quantiles avec NumPy, invariance au nombre de copies des épisodes d'une personne. Ces contrôles emploient des cas artificiels explicitement identifiés ; ils ne valident aucun effet biologique.
- Rejeu par `--out` comparé octet par octet à `resultats.json` : identique.
- Génération du site : six sujets, vingt articles. Liens internes et fichier de figure présents. Les 16 expressions KaTeX de la nouvelle page se rendent sans erreur.
- Chromium/Chrome, fenêtres de 1280 et 390 pixels : nouvel article, deux pages de sujet et index des recherches en HTTP 200, sans débordement global, marqueur numérique résiduel, image cassée ou erreur JavaScript. Graphique final réinspecté après augmentation des caractères et espacement de la légende ; PNG et SVG dérivent des mêmes décomptes.
- Sources complètes et résultats JSON rouverts avant livraison. Le plan reste proposé, sans préenregistrement indépendant ni examen externe par des chercheurs.

Ces preuves concernent le travail local. Elles ne valent pas confirmation du déploiement ni du travail GitHub qui rejoue toutes les analyses historiques. La publication doit être vérifiée séparément sur le commit envoyé et les ressources publiques correspondantes.
