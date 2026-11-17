# æternam.com

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
- Le site est en français seulement, servi à la racine : æternam.com/, jamais /fr/ (décisions d'Aitor du 28/09/2026). Les anciennes adresses à préfixe de langue (/fr/…, /en/…) redirigent (301) vers la racine par `public/_redirects`, écrit par `site/generer.py`.
- Chaque chiffre vient d'une source primaire vérifiée ou d'un calcul reproductible du dépôt ; jamais de mémoire.

## Fonctionnement

- Recherche : `recherche/<date>-<sujet>/`, avec un script Python reproductible (`analyse.py`, autotests) et ses `resultats.json`.
- Textes : `site/langues/fr.py`.
- Accueil : directement le titre « ÆTERNAM » (nom écrit en capitales avec la ligature Æ partout où il s’affiche : titre, logo, pied de page, onglets ; décision d’Aitor du 17/11/2026), les articles rangés par thème et l’invitation à écrire. Plus de trou noir à l’arrivée (décision d’Aitor du 17/11/2026) : `site/trou-noir.js` ne sert qu’à la scène du thème Relativité. Favicon : la ligature Æ (`site/favicon.svg`), sur toutes les pages. `/sujets/` regroupe les rubriques ; `/recherches/` regroupe tous les articles par thème ; `/a-propos/` explique la démarche. Les textes et rubriques sont définis dans `site/langues/fr.py`, le classement de chaque article dans `ETUDES` de `site/generer.py`. Visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, æternam.com) si le secret `CLOUDFLARE_API_TOKEN` existe.
- Adresse principale : æternam.com (`xn--ternam-oua.com`, acheté chez GoDaddy le 17/11/2026 ; décision d’Aitor du 17/11/2026), DNS chez Cloudflare, domaines personnalisés du projet Pages `aeternam` : racine + `www` (redirigé vers la racine). aeternam.org (acheté chez Netlify) a expiré et ne répond plus (constaté le 17/11/2026) ; son renouvellement passe par le support Netlify, après quoi le petit site Netlify de `netlify/` le redirige vers æternam.com. Section CAP : `/cap/`, page d’article générée par `site/cap.py` (texte, maquette de la casquette noire au Æ, figures tirées des données de `/bci-generalisation/` et `/bci-monte-carlo/`) avec `site/cap/cap.css` et `site/cap/cap.js` ; le projet lui-même est suivi dans `~/Projects/ae-cap`.

## Articles signés (décision d’Aitor du 17 novembre 2026)

- ÆTERNAM est de la science ouverte : chacun peut publier un article signé de son nom. Barre de navigation : Thèmes, Articles, CAP, Écrire, À propos.
- Un article = `contributions/AAAA-MM-JJ-titre-court.md` (en-tête titre, auteur, date, thème, résumé, ORCID, licence, puis Markdown). Rendu par `site/contributions.py` : sous-ensemble sûr de Markdown, tout est échappé, liens http(s) ou internes seulement, images de `contributions/medias/` (jamais de SVG). Toute erreur arrête la construction avec le message à corriger. Mode d’emploi public : `contributions/README.md` ; modèle : `contributions/_modele.md` (non publié).
- Arrivée par pull request : le formulaire `/ecrire/` (`site/ecrire.js`) ouvre GitHub avec le fichier rempli. Le job `verifier` de `.github/workflows/deployer.yml` construit le site sur chaque pull request, sans publier. Relecture publique, licence CC BY 4.0, historique visible depuis chaque article.
- Relire une proposition avec les exigences d’ÆTERNAM (sources primaires, mesures, calculs et simulations distingués), mais ne pas réécrire la thèse de l’auteur. Une proposition qui touche autre chose que `contributions/` s’examine à part.
- Pages : `/contributions/<date>-<titre-court>/`, signature en fin de texte (jamais sous le titre). Listées sur l’accueil, dans `/recherches/#signes`, sur la page de leur thème et sur `/ecrire/`.
- Le dépôt GitHub est public depuis le 17/11/2026 (décision d’Aitor) : tout compte GitHub peut proposer, GitHub crée la copie (fork) tout seul. Pour un premier contributeur, le job `verifier` attend qu’Aitor clique sur « Approve and run » (réglage Actions par défaut, `first_time_contributors`). Le secret `CLOUDFLARE_API_TOKEN` ne sert qu’au job `deployer`, jamais lancé sur une pull request.
- Licences (décision d’Aitor du 17/11/2026) : textes, figures et résultats sous CC BY 4.0 (`LICENSE`), code sous MIT (`LICENSE-CODE`), textes de référence de GitHub laissés tels quels pour qu’il les reconnaisse ; le détail est dans la section « Licence » du README.

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

## Pages de thème

- Les thèmes suivent le même ordre partout (`SUJETS` de `fr.py`) : relativité, vision, mémoire, rêve et temps vécu, interfaces, simulation. Chaque page de thème a sa scène (`SCENES_SUJETS` de `site/generer.py`, dessinée par `site/theme.js`), une fois, sans cadre, avec sa légende : nuages de points procéduraux (`site/univers-scene.mjs`), schémas hors échelle, jamais des observations. Celle de la relativité est le trou noir calculé. Chaque article propose l’article suivant de son premier thème.
- Tests : `node --test site/tests/*.test.mjs` (scènes des thèmes), lancés à chaque déploiement.

## Arrivée sur le trou noir (22 octobre 2026)

- Décision d’Aitor du 22 octobre : on arrive sur un trou noir, vivant, qui nous avale ; dedans, seulement le titre « aeternam » et les articles rangés par thème. Le même jour, Aitor retire le parcours « du cosmos au cerveau » (histoire illustrée de l’Univers, scènes du cerveau, expériences de relativité), jugé beau mais mal fait ; il reste dans l’historique Git. `site/trou-noir.js` le calcule en WebGL : trou noir de Schwarzschild, rayons de lumière suivis à rebours (u'' + u = 3/2 u²), disque d’accrétion képlérien avec décalages Doppler et gravitationnel, étoiles déviées. Légende : calculé, pas une observation. Le même calcul remplace l’illustration du trou noir (scène 19) sur la page du thème Relativité, en une image immobile ; sans WebGL, l’illustration et sa légende reviennent.
- Au bout de cinq secondes, ou dès qu’on défile, tape ou appuie sur une touche, la caméra tombe ; sous la sphère de photons tout est noir devant elle, puis la page apparaît. Pas d’arrivée en revenant d’une autre page du site, par le bouton Précédent ou par un lien avec ancre (`/#…`) ; sans JavaScript ni WebGL, page normale ou image fixe. Mouvements réduits : image fixe puis fondu.
- Couleurs du site depuis le 22 octobre : la lumière froide de ce trou noir (fond `#05070c`, texte `#e8ecf5`, accent `#a9c2ff`) ; l’or des scènes de thème reste pour la lumière chaude. Favicon : le trou noir.
