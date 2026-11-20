# æternam.com

ÆTERNAM : l’immortalité, et un blog de recherche ouvert, en français et en anglais.

## Objectif

Décision d’Aitor du 20 novembre 2026 : ÆTERNAM traite d’un seul sujet, l’immortalité, et ouvre un blog de recherche : ses articles et ceux de la communauté, rangés par thème, expliqués simplement, en français comme en anglais. Le Musée et CAP sont retirés du site. Cette décision remplace le blog personnel du 3 octobre et l’accueil du 17 novembre. La structure éditoriale est dans `BLOG.md` ; `STARTUP.md` est une archive.

Six thèmes, chacun avec sa question, dans le même ordre partout (`SUJETS` de `site/langues/fr.py`) : mémoire ; interfaces cerveau-machine ; vision et perception ; rêve et temps vécu ; relativité et trous noirs ; théorie de la simulation. Aucun sujet ne sert de preuve à un autre. Un article transversal peut être classé dans plusieurs thèmes. « Une vie en une nuit » reste une question étudiée, pas la promesse du site.

Les études scientifiques gardent leurs résultats exacts et leurs adresses. Travailler avec les données ouvertes, la littérature et les calculs locaux ; ne pas inventer de participants, de partenariats ou de capacités démontrées. Les simulations numériques doivent être explicitement distinguées des mesures humaines.

## Préférences d'Aitor

- Agents autorisés (demande du 28/09/2026) pour les recherches, tests et traductions ; l'intégration au site reste centralisée. Réponses courtes, en français.
- Après chaque avancée validée : envoyer sur `main` (déploiement) et continuer sans attendre.
- Toujours deux niveaux : « Explication » (claire, sans formule ni jargon) puis « Analyse détaillée » (démonstration complète). Ton sérieux ; jamais d'intitulés « pour tous » / « pour les spécialistes ».
- Répondre nettement à une question précise ; distinguer « non démontré » et « impossible ». Une donnée absente ne vaut pas zéro.
- Des textes simples, clairs, qui mènent quelque part. Le site ne se décrit jamais (« un site sur l’immortalité » est une consigne de travail, pas une phrase à afficher) : il pose la question, « Peut-on vivre pour toujours ? ».
- La voix porte une conviction (demande d’Aitor du 20/11/2026) : jamais « nous cherchons », mais « nous trouverons ». C’est une quête pour toute l’humanité : ce qui est trouvé est à tout le monde. La conviction est dans la voix du site (accueil, À propos) ; les articles gardent leurs résultats exacts et leurs limites.
- Le style : celui d’Ordalie et d’Anthropic. Dessins au trait faits à la main, grand serif, nuit et ivoire, mouvement au défilement. Jamais de cartes ni d’encadrés (fond, bordure, barre colorée) : texte nu, typographique. Fond uni : plus de pluie de bits.
- Au millimètre : chaque mesure de mise en page (encre des lettres, ligne de base, grille, blancs) est mesurée dans le navigateur, jamais estimée, et vérifiée à 1440, 705 et 390 px de large.
- Jamais de surtitre ni d’étiquette au-dessus d’un titre : un titre se suffit, ce qui le précise vient après lui.
- Jamais de section « Fichiers » ni de liste de téléchargements dans les textes : ni ligne « Calcul reproductible » : la preuve est dans les calculs et analyses du texte. Les fichiers restent servis sous /fichiers/ sans être listés.
- Sous le titre d’un article : ni sous-titre ni date (la description ne sert qu’aux métadonnées). Une page de thème porte sa question sous son titre.
- Deux éditions : le français à la racine (æternam.com/, jamais /fr/) et l’anglais sous /en/, avec les mêmes adresses. L’autre langue est un lien dans la barre et dans le pied. Les anciennes adresses en /fr/… redirigent (301) vers la racine par `public/_redirects`, écrit par `site/generer.py`.
- Chaque chiffre vient d’une source primaire vérifiée ou d’un calcul reproductible du dépôt ; jamais de mémoire. Une citation entre guillemets est vérifiée mot pour mot à sa source, dans sa langue ; sinon elle passe en discours rapporté.

## Fonctionnement

- Recherche : `recherche/<date>-<sujet>/`, avec un script Python reproductible (`analyse.py`, autotests) et ses `resultats.json`.
- Textes : `site/langues/fr.py` (la source) et `site/langues/en.py` (la traduction, de même structure). La construction compare les balises, les marqueurs de nombres et les formules des deux langues (`site/langues/verifier_traduction.py`) et s’arrête au premier écart. Un mot du français garde le même mot en anglais d’un article à l’autre (« grille » : *grid* ; « réseau » : *lattice*).
- Accueil (`site/accueil.py`, `site/accueil/`) : au premier écran, le nom ÆTERNAM et la question, seuls. Au défilement, le nom s’efface et un sablier arrive ; son sable tombe pendant que les étoiles filent, puis ralentit et reste suspendu. Pas de signe de l’infini ni de boucle (décision d’Aitor du 20/11/2026). Puis la feuille : trois phrases, le blog en six questions (pourquoi la question compte, ce que l’on sait avec les nombres des études, les articles), l’invitation à écrire. Sans JavaScript ou en mouvement réduit : le nom et la question.
- Le nom s’écrit ÆTERNAM, en capitales avec la ligature, partout où il s’affiche (décision d’Aitor du 17/11/2026). Favicon : la ligature Æ (`site/favicon.svg`).
- Barre de navigation, la même partout : le signe Æ seul, sans pastille (décision d’Aitor du 20/11/2026 : le Æ peut y être, à condition d’être parfait), puis Blog, Thèmes, Écrire, À propos et l’autre langue. Ses mesures sont écrites à côté de ses règles dans `site/style.css` : capitale de 16 px centrée dans une pilule de 44 px, encre à 18 px du bord.
- Dessins : `site/dessins.py`, au trait, hors échelle, jamais présentés comme des observations ; le même dessin sur l’accueil et en tête de la page du thème.
- `/recherches/` : le blog, tous les articles par thème, ceux de la communauté compris ; `/sujets/` : les six thèmes ; `/ecrire/` : proposer un article ; `/a-propos/` : la démarche. Le classement de chaque article est dans `ETUDES` de `site/generer.py`. Visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (les deux éditions ; résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, æternam.com) si le secret `CLOUDFLARE_API_TOKEN` existe.
- Adresse principale : æternam.com (`xn--ternam-oua.com`, acheté chez GoDaddy le 17/11/2026 ; décision d’Aitor du 17/11/2026), DNS chez Cloudflare, domaines personnalisés du projet Pages `aeternam` : racine + `www` (redirigé vers la racine). aeternam.org (acheté chez Netlify) a expiré et ne répond plus (constaté le 17/11/2026) ; son renouvellement passe par le support Netlify, après quoi le petit site Netlify de `netlify/` le redirige vers æternam.com. CAP n’a plus de page sur le site : `/cap/` redirige vers l’accueil ; le projet est suivi dans `~/Projects/ae-cap`.

## Articles signés (décision d’Aitor du 17 novembre 2026)

- ÆTERNAM est de la science ouverte : chacun peut publier un article signé de son nom.
- Un article = `contributions/AAAA-MM-JJ-titre-court.md` (en-tête titre, auteur, date, thème, résumé, ORCID, licence, langue : `fr` par défaut ou `en`, puis Markdown). Il est servi une fois, dans sa langue, et listé dans les deux éditions. Rendu par `site/contributions.py` : sous-ensemble sûr de Markdown, tout est échappé, liens http(s) ou internes seulement, images de `contributions/medias/` (jamais de SVG). Toute erreur arrête la construction avec le message à corriger. Mode d’emploi public : `contributions/README.md` ; modèle : `contributions/_modele.md` (non publié).
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

- Chaque page de thème s’ouvre sur son titre, sa question et son dessin (`DESSINS_SUJETS` de `site/generer.py`), dit pourquoi la question compte et ce que l’on sait (nombres tirés des études), puis renvoie à l’étude ; viennent ensuite les questions, les lectures pour commencer et les articles. Chaque article propose l’article suivant de son premier thème.
- Tests : `node --test site/tests/*.test.mjs`, lancés à chaque déploiement. Ils portent sur les anciennes scènes WebGL (`site/univers-scene.mjs`, avec `site/theme.js` et `site/trou-noir.js`), que le site ne charge plus depuis le 20/11/2026.

## Identité visuelle (20 novembre 2026)

- Couleurs (`site/style.css`) : le papier `#f2efe7` et l’encre `#171614` pour les pages ; la nuit `#131211` et l’os `#ece8de` pour l’accueil, les en-têtes de thème et le pied ; un accent bronze `#8c5d14` sur le papier, or `#d6b36a` sur la nuit. Polices : Newsreader (titres et texte) et DM Sans (interface), servies depuis `site/polices/`.
- Le nom en grand (accueil, pied) est composé sur les mesures du caractère : son encre occupe exactement la grille, du haut des capitales à la ligne de base. Les mesures et leur calcul sont écrits à côté des règles, dans `site/accueil/accueil.css` et `site/style.css`.
- L’arrivée sur le trou noir (22 octobre), le parcours « du cosmos au cerveau », les scènes de thème et la pluie de bits sont dans l’historique Git.
