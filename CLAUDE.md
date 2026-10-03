# aeternam.org

Blog de recherche personnel, en français.

## Objectif

Décision d’Aitor du 3 octobre 2026 : Aeternam devient uniquement un blog de recherche organisé autour des sujets qui l’intéressent. Cette décision remplace le cadrage de startup du 29 septembre. La structure éditoriale est dans `BLOG.md` ; `STARTUP.md` est une archive.

Cinq rubriques : interfaces cerveau-machine ; vision et perception ; mémoire ; rêve et temps vécu ; théorie de la simulation. Aucun sujet ne sert de preuve à un autre. Un article transversal peut être classé dans plusieurs rubriques. « Une vie en une nuit » reste une question étudiée dans un article, pas la promesse du site.

Les études scientifiques gardent leurs résultats exacts et leurs adresses. Travailler avec les données ouvertes, la littérature et les calculs locaux ; ne pas inventer de participants, de partenariats ou de capacités démontrées. Les simulations numériques doivent être explicitement distinguées des mesures humaines.

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
- Accueil : présentation du blog, sommaire des cinq thèmes, puis articles regroupés sous chaque thème. `/sujets/` regroupe les rubriques ; `/recherches/` regroupe tous les articles par thème ; `/a-propos/` explique la démarche. Les textes et rubriques sont définis dans `site/langues/fr.py`, le classement de chaque article dans `ETUDES` de `site/generer.py`. Visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, www.aeternam.org) si le secret `CLOUDFLARE_API_TOKEN` existe.
- DNS chez Netlify (domaine acheté chez Netlify) : `www` → CNAME `aeternam.pages.dev` ; `aeternam.org` redirige vers www par le petit site Netlify de `netlify/`.

## État après l’audit du 29 septembre 2026

- Le carnet « Rêve, temps et mémoire » reste accessible à `/programme/`, calculs dans `recherche/2026-09-29-programme-calcul/` : DREAM individuel, tâches chronométrées, dénominateurs publiés et simulations de méthode.
- Depuis le 3 octobre, tous les articles sont classés dans les cinq rubriques du blog ; les anciennes adresses restent accessibles.
- Les anciens facteurs globaux 0,84, 0,92 et 1,09 sont retirés. Ne pas les réutiliser comme mesures ou bornes du temps vécu.
- Rejeu neuronal, durée racontée, tâche chronométrée et expérience consciente ne partagent pas une échelle mesurée commune.
- Le « 7 % » de simulation est un scénario arbitraire, pas une probabilité estimée de notre Univers.
- Huit sources gamma : correction de Bonferroni sur huit contraintes, couverture minimale conditionnelle 60 %, pas 85 %. Optimisation d’orientation numérique sans certificat global.
- Ciel complet : p-valeur du test principal conservée ; bornes d’amplitude approximatives sur un balayage fini.
- Interférences : diagnostics conditionnels aux erreurs reconstruites ; significativité combinée non retenue comme preuve validée.
- Les corrections et leur portée sont dans `AUDIT-SCIENTIFIQUE.md`. Les anciens résultats restent accessibles par Git.
- Secret Cloudflare existant ; chaque envoi sur main publie le site.

## Extension du 3 octobre 2026

- `/interfaces-cerveau/` : lecture et intervention, preuves humaines sur la vision, limites des travaux sur la mémoire, contributions proposées avec MOABB et pulse2percept.
- `/meg-eeg-reves/` : audit des articles, disponibilité réelle des données et contrôles d’une future étude sur le contenu du rêve.
- Calculs exécutés : dénominateurs de PRIMA et du pilote REM, scénarios exacts d’information partielle, confusion son/contenu, valeur prédictive, test binomial et rapports de durée. Ce ne sont pas des mesures cérébrales Aeternam.
- Brain2Qwerty v2 est présenté comme une prépublication ; son architecture traite une phrase entière, même si l’entrée est asynchrone. Données v2 indiquées sous embargo au contrôle. Ne pas assimiler la v1 à un enregistrement EEG/MEG simultané.
- Les dépôts Kumral et Brain2Qwerty v1 sont repérés ; les signaux bruts n’ont pas été téléchargés ni réanalysés dans ces deux études. Leurs volumes et accès sont des instantanés à revérifier.
- Les souvenirs imposés à des fins punitives sont discutés comme problème conceptuel et éthique, pas comme protocole ni produit d’Aeternam. Distinguer souvenir, croyance rétrospective et vécu continu.
