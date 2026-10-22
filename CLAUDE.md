# aeternam.org

Blog de recherche personnel, en français.

## Objectif

Décision d’Aitor du 3 octobre 2026 : Aeternam devient uniquement un blog de recherche organisé autour des sujets qui l’intéressent. Cette décision remplace le cadrage de startup du 29 septembre. La structure éditoriale est dans `BLOG.md` ; `STARTUP.md` est une archive.

Six rubriques depuis le 8 octobre 2026 : relativité et trous noirs ; interfaces cerveau-machine ; vision et perception ; mémoire ; rêve et temps vécu ; théorie de la simulation. Aucun sujet ne sert de preuve à un autre. Un article transversal peut être classé dans plusieurs rubriques. « Une vie en une nuit » reste une question étudiée dans un article, pas la promesse du site.

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
- Accueil : un parcours au défilement « du cosmos au cerveau » (voir la section du 18 octobre), terminé par les articles rangés par thème. `/sujets/` regroupe les rubriques ; `/recherches/` regroupe tous les articles par thème ; `/a-propos/` explique la démarche. Les textes et rubriques sont définis dans `site/langues/fr.py`, le classement de chaque article dans `ETUDES` de `site/generer.py`. Visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, www.aeternam.org) si le secret `CLOUDFLARE_API_TOKEN` existe.
- DNS chez Netlify (domaine acheté chez Netlify) : `www` → CNAME `aeternam.pages.dev` ; `aeternam.org` redirige vers www par le petit site Netlify de `netlify/`.

## État après l’audit du 29 septembre 2026

- Le carnet « Rêve, temps et mémoire » reste accessible à `/programme/`, calculs dans `recherche/2026-09-29-programme-calcul/` : DREAM individuel, tâches chronométrées, dénominateurs publiés et simulations de méthode.
- Depuis le 3 octobre, tous les articles sont classés dans les rubriques du blog (six depuis le 8 octobre) ; les anciennes adresses restent accessibles.
- Les anciens facteurs globaux 0,84, 0,92 et 1,09 sont retirés. Ne pas les réutiliser comme mesures ou bornes du temps vécu.
- Rejeu neuronal, durée racontée, tâche chronométrée et expérience consciente ne partagent pas une échelle mesurée commune.
- Le « 7 % » de simulation est un scénario arbitraire, pas une probabilité estimée de notre Univers.
- Huit sources gamma : correction de Bonferroni sur huit contraintes, couverture minimale conditionnelle 60 %, pas 85 %. Optimisation d’orientation numérique sans certificat global.
- Ciel complet : p-valeur du test principal conservée ; bornes d’amplitude approximatives sur un balayage fini.
- Interférences : diagnostics conditionnels aux erreurs reconstruites ; significativité combinée non retenue comme preuve validée.
- Les corrections et leur portée sont dans `AUDIT-SCIENTIFIQUE.md`. Les anciens résultats restent accessibles par Git.
- Secret Cloudflare existant ; chaque envoi sur main publie le site.

## Extension du 3 octobre 2026

- `/bci-monte-carlo/` : à la demande d’Aitor, expérience Monte-Carlo de calibration personnelle et de bruit, calée sur les six caractéristiques EEG humaines déjà extraites. 600 campagnes par hypothèse, huit budgets, quatre hypothèses, cinq conditions. Dans le scénario empirique : minimum testé de 64 étiquettes avec référence, 128 avec bruit non corrigé, pour un gain moyen de cinq points. La référence exige aussi 256 observations cibles non étiquetées ; ne pas présenter cela comme une réduction démontrée des données personnelles totales. Les scénarios à contraste moitié ou dérive triple n’atteignent pas le critère jusqu’à 256. Modèle statistique de caractéristiques, sans EEG temporel ou simulation biophysique ; intervalles de précision Monte-Carlo, pas intervalles humains. Références chinoises : Beihang/Ningbo (compensation MEG) et SUSTech/Shenzhen (contamination contrôlée EEG), sans reproduction de leurs montages ni réseaux.
- `/bci-generalisation/` : revue de quatre études BCI publiées en 2026 et réanalyse effective de 36 EDF PhysioNet, 540 essais, 12 personnes. Modèle simple à trois canaux : 55,3 % sur un run réservé de la même personne, 51,8 % sur une personne entièrement réservée ; référence équilibrée 50 %. Tests exploratoires par permutations corrigés : p = 0,020 et 0,149 respectivement. Ce résultat ne mesure ni le plafond des BCI ni un effet causal de la calibration. Vérifications SciPy/scikit-learn, sources, paramètres et empreintes conservés ; les bruts téléchargés sont ignorés par Git.
- `/interfaces-cerveau/` : lecture et intervention, preuves humaines sur la vision, limites des travaux sur la mémoire, contributions proposées avec MOABB et pulse2percept.
- `/meg-eeg-reves/` : audit des articles, disponibilité réelle des données et contrôles d’une future étude sur le contenu du rêve.
- Calculs exécutés : dénominateurs de PRIMA et du pilote REM, scénarios exacts d’information partielle, confusion son/contenu, valeur prédictive, test binomial et rapports de durée. Ce ne sont pas des mesures cérébrales Aeternam.
- Brain2Qwerty v2 est présenté comme une prépublication ; son architecture traite une phrase entière, même si l’entrée est asynchrone. Données v2 indiquées sous embargo au contrôle. Ne pas assimiler la v1 à un enregistrement EEG/MEG simultané.
- Les dépôts Kumral et Brain2Qwerty v1 sont repérés ; les signaux bruts n’ont pas été téléchargés ni réanalysés dans ces deux études. Leurs volumes et accès sont des instantanés à revérifier.
- Les souvenirs imposés à des fins punitives sont discutés comme problème conceptuel et éthique, pas comme protocole ni produit d’Aeternam. Distinguer souvenir, croyance rétrospective et vécu continu.

## Étude rêve et récit du 8 octobre 2026

- `/reve-recit/`, dossier `recherche/2026-10-08-reve-recit/` : audit ciblé de huit candidats et recalcul du tableau 1 de Konkoly et al. 2026. Les 150 signaux proviennent de 11 des 13 personnes ; les deux plus grandes contributions totalisent 102 signaux (68 %). Réanalyse descriptive de décomptes, sans réanalyse EEG ni découverte biologique revendiquée.
- Aucune paire humaine de jugements de durée pendant/après acquise ; effet principal `null`, jamais zéro. Plan d’analyse secondaire proposé, non préenregistré auprès d’un registre indépendant. Les conditions de mesure ne sont pas un protocole clinique à exécuter.
- Comparer le même intervalle et la même question ; poids égal des personnes ; préserver absence de rappel et autres manquants. Un écart entre rapports ne mesure ni une vitesse de conscience ni un effet causal pur de la mémoire. Le contre-exemple de non-identification est algébrique et les contrôles du logiciel sont artificiels.

## Accueil « Du cosmos au cerveau » (9 et 18 octobre 2026)

- Décision d’Aitor du 9 octobre : l’accueil raconte l’histoire de l’Univers au défilement. Un seul titre « aeternam », sans accroche ni appel à commencer ; une phrase par étape, les développements et les sources dans « Analyse détaillée », fermée par défaut ; ni compteur d’étapes ni barre de progression.
- Décision d’Aitor du 18 octobre : le parcours continue jusqu’au cerveau pour rejoindre les sujets du blog. Ordre : l’Univers (douze étapes, `ETAPES` de `site/langues/univers_fr.py`), la relativité (cinq expériences, `EXPERIENCES`), le cerveau (neurones, vision, mémoire, rêve), les frontières (lire un cerveau, simulation, avant le Big Bang, après aujourd’hui ; `ETAPES_CERVEAU`), puis les articles rangés par thème et les sources. Sommaire : Univers · Relativité · Cerveau · Frontières · Articles.
- Les scènes sont des nuages de points procéduraux (`site/univers-scene.mjs`) : 0 à 12 pour le cosmos, 13 à 19 pour neurones, vision, mémoire, rêve, interface, simulation et trou noir. Ce sont des schémas hors échelle, jamais des observations, des enregistrements ou une interface réelle ; chaque étape affiche sa légende. Le passage de la toile cosmique au réseau de neurones est une mise en scène : aucune ressemblance de forme ne relie les deux sujets.
- Le curseur « Électrodes » de l’étape vision réduit une lettre à une grille de points lumineux : modèle volontairement simple, pas la perception d’un patient ni un implant précis.
- Les thèmes suivent l’ordre du parcours partout (`SUJETS` de `fr.py`) : relativité, vision, mémoire, rêve et temps vécu, interfaces, simulation. Chaque page de thème reprend sa scène (`site/theme.js`), dessinée une fois, sans cadre. Chaque article propose l’article suivant de son premier thème.
- Les nombres de ces étapes suivent la même règle que les articles : source primaire vérifiée ou calcul du dépôt (par exemple 86,1 ± 8,1 milliards de neurones chez l’homme adulte, Azevedo et al. 2009).
- Tests : `node --test site/tests/*.test.mjs` (modèles de relativité et scènes), lancés à chaque déploiement.

## Arrivée sur le trou noir (22 octobre 2026)

- Décision d’Aitor du 22 octobre : on arrive sur un trou noir, vivant, qui nous avale ; le parcours « du cosmos au cerveau » commence à l’intérieur. `site/trou-noir.js` le calcule en WebGL : trou noir de Schwarzschild, rayons de lumière suivis à rebours (u'' + u = 3/2 u²), disque d’accrétion képlérien avec décalages Doppler et gravitationnel, étoiles déviées. Légende : calculé, pas une observation. Le même calcul remplace l’illustration du trou noir (scène 19) sur la page du thème Relativité, en une image immobile ; sans WebGL, l’illustration et sa légende reviennent. Il ouvre aussi le chapitre Relativité du parcours (« L’espace-temps se courbe », `#trou-noir-calcule`), animé seulement quand on le voit et figé avec le bouton du parcours ; sans WebGL, la figure disparaît et le texte reste.
- Au bout de cinq secondes, ou dès qu’on défile, tape ou appuie sur une touche, la caméra tombe ; sous la sphère de photons tout est noir devant elle, puis la page apparaît. Pas d’arrivée en revenant d’une autre page du site, par le bouton Précédent ou par un lien vers une étape (`/#…`) ; sans JavaScript ni WebGL, page normale ou image fixe. Mouvements réduits : image fixe puis fondu.
- Couleurs du site depuis le 22 octobre : la lumière froide de ce trou noir (fond `#05070c`, texte `#e8ecf5`, accent `#a9c2ff`) ; l’or des scènes reste pour la lumière chaude. Favicon : le trou noir.
