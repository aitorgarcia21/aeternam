# aeternam.org

Une vie entière, le temps d’une nuit. Projet de startup centré sur le rêve et le temps vécu.

## Objectif

Décision d’Aitor du 29 septembre 2026 : le projet « Une vie en une nuit » devient le cœur d’Aeternam. Le manifeste relie l’automatisation à une inquiétude sur la perte de sens ; il doit conserver ce ton sombre et affirmé. Retirer du récit de marque l’ancienne ambition de vaincre la mort. Le cadrage et les propositions de lancement sont dans `STARTUP.md`.

Les études scientifiques restent publiées avec leurs résultats exacts. L’hypothèse de la simulation demeure un axe de recherche :

La théorie de la simulation reste dans la rubrique « Nos recherches », séparée du projet onirique. Chercher des signatures de modèles précis ; aucune trace n'est nécessaire à toute simulation. Les arguments cosmologiques ne valident pas la technologie du rêve.

Décision du 29 septembre : aucun moyen expérimental disponible. Travailler avec données ouvertes, littérature et calculs locaux ; ne pas inventer de participants, de partenariats ou de capacité démontrée. Les cinq axes sont accès, contenu, temps, mémoire et validation des méthodes. Les simulations numériques doivent être explicitement distinguées des mesures humaines.

## Préférences d'Aitor

- Agents autorisés (demande du 28/09/2026) pour les recherches, tests et traductions ; l'intégration au site reste centralisée. Réponses courtes, en français.
- Après chaque avancée validée : envoyer sur `main` (déploiement) et continuer sans attendre.
- Toujours deux niveaux : « Explication » (claire, sans formule ni jargon) puis « Analyse détaillée » (démonstration complète). Ton sérieux ; jamais d'intitulés « pour tous » / « pour les spécialistes ».
- Répondre nettement à une question précise ; distinguer « non démontré » et « impossible ». Une donnée absente ne vaut pas zéro.
- Jamais de cartes ni d'encadrés (fond, bordure, barre colorée) : texte nu, typographique. Fond de chaque page : une pluie de bits façon Matrix (les vrais bits quantiques du test n° 4), visible mais discrète (floue derrière le texte), sans légende.
- Jamais de section « Fichiers » ni de liste de téléchargements dans les textes : ni ligne « Calcul reproductible » : la preuve est dans les calculs et analyses du texte. Les fichiers restent servis sous /fichiers/ sans être listés.
- Sous le titre d'une page : ni sous-titre ni date (la description ne sert qu'aux métadonnées).
- Jamais de surtitre, d'étiquette en petites capitales au-dessus d'un titre, ni de sélecteur de langue visible.
- Le site est en français seulement, servi à la racine : www.aeternam.org/, jamais /fr/ (décisions d'Aitor du 28/09/2026). Les anciennes adresses à préfixe de langue (/fr/…, /en/…) redirigent (301) vers la racine par `public/_redirects`, écrit par `site/generer.py`.
- Chaque chiffre vient d'une source primaire vérifiée ou d'un calcul reproductible du dépôt ; jamais de mémoire.

## Fonctionnement

- Recherche : `recherche/<date>-<sujet>/`, avec un script Python reproductible (`analyse.py`, autotests) et ses `resultats.json`.
- Textes : `site/langues/fr.py`.
- Accueil : ambition « Une vie entière, le temps d’une nuit », puis manifeste du projet, puis les cinq axes du programme et ses travaux. La théorie de la simulation est accessible depuis `/recherches/`. Le manifeste est partagé avec la page du projet via `MANIFESTE` dans `site/langues/fr.py`. Visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, www.aeternam.org) si le secret `CLOUDFLARE_API_TOKEN` existe.
- DNS chez Netlify (domaine acheté chez Netlify) : `www` → CNAME `aeternam.pages.dev` ; `aeternam.org` redirige vers www par le petit site Netlify de `netlify/`.

## État après l’audit du 29 septembre 2026

- Le programme central est `/programme/`, calculs dans `recherche/2026-09-29-programme-calcul/` : DREAM individuel, tâches chronométrées, dénominateurs publiés et simulations de méthode.
- `/recherches/` sépare cerveau/rêve et simulation ; l’accueil présente le projet.
- Les anciens facteurs globaux 0,84, 0,92 et 1,09 sont retirés. Ne pas les réutiliser comme mesures ou bornes du temps vécu.
- Rejeu neuronal, durée racontée, tâche chronométrée et expérience consciente ne partagent pas une échelle mesurée commune.
- Le « 7 % » de simulation est un scénario arbitraire, pas une probabilité estimée de notre Univers.
- Huit sources gamma : correction de Bonferroni sur huit contraintes, couverture minimale conditionnelle 60 %, pas 85 %. Optimisation d’orientation numérique sans certificat global.
- Ciel complet : p-valeur du test principal conservée ; bornes d’amplitude approximatives sur un balayage fini.
- Interférences : diagnostics conditionnels aux erreurs reconstruites ; significativité combinée non retenue comme preuve validée.
- Les corrections et leur portée sont dans `AUDIT-SCIENTIFIQUE.md`. Les anciens résultats restent accessibles par Git.
- Secret Cloudflare existant ; chaque envoi sur main publie le site.
