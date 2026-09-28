# aeternam.org

Recherche sur la théorie de la simulation.

## Objectif

Prouver, si c'est vrai, que nous vivons dans une simulation : chercher dans des données réelles les traces qu'une simulation laisserait forcément. Rapporter honnêtement ce qui sort, positif ou non ; une preuve qui ne tient pas détruirait aeternam.

Pistes, dans l'ordre :

1. Rayons cosmiques : anisotropie à symétrie cubique des directions d'arrivée aux plus hautes énergies (prédiction de Beane, Davoudi et Savage, arXiv:1210.1847), sur les données ouvertes de l'observatoire Pierre Auger.
2. Vitesse de la lumière selon la direction : combiner sursauts gamma et blazars de tout le ciel et chercher le motif cubique Q(n) de la dispersion (voir le test n° 1).
3. Hasard quantique : tests statistiques de flux publics (ANU, NIST Beacon).

## Préférences d'Aitor

- Agents autorisés (demande du 28/09/2026) pour les recherches, tests et traductions ; l'intégration au site reste centralisée. Réponses courtes, en français.
- Après chaque avancée validée : envoyer sur `main` (déploiement) et continuer sans attendre.
- Toujours deux niveaux : « Explication » (claire, sans formule ni jargon) puis « Analyse détaillée » (démonstration complète). Ton sérieux ; jamais d'intitulés « pour tous » / « pour les spécialistes ».
- Toujours un verdict net, par oui ou par non ; creuser l'analyse jusqu'au bout.
- Jamais de cartes ni d'encadrés (fond, bordure, barre colorée) : texte nu, typographique. Fond de l'accueil : une pluie de bits façon Matrix (les vrais bits quantiques du test n° 4) sur toute la page, à peine devinable (floue derrière le texte), sans légende.
- Jamais de section « Fichiers » ni de liste de téléchargements dans les textes : ni ligne « Calcul reproductible » : la preuve est dans les calculs et analyses du texte. Les fichiers restent servis sous /fichiers/ sans être listés.
- Jamais de surtitre, d'étiquette en petites capitales au-dessus d'un titre, ni de sélecteur de langue visible.
- Le site est en français seulement, servi à la racine : www.aeternam.org/, jamais /fr/ (décisions d'Aitor du 28/09/2026). Les anciennes adresses à préfixe de langue (/fr/…, /en/…) redirigent (301) vers la racine par `public/_redirects`, écrit par `site/generer.py`.
- Chaque chiffre vient d'une source primaire vérifiée ou d'un calcul reproductible du dépôt ; jamais de mémoire.

## Fonctionnement

- Recherche : `recherche/<date>-<sujet>/`, avec un script Python reproductible (`analyse.py`, autotests) et ses `resultats.json`.
- Textes : `site/langues/fr.py`.
- Accueil : page de présentation (un seul bloc « La théorie » : Bostrom, Musk en une phrase et notre probabilité calculée, scénario `aeternam` de la synthèse ; puis les traces cherchées avec visuels, notre réponse, les travaux). Priorité aux preuves et aux calculs, pas de théorie en plus. Texte dans `ACCUEIL` de `site/langues/fr.py`, visuels SVG tirés des données réelles dans `site/visuels.py`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, www.aeternam.org) si le secret `CLOUDFLARE_API_TOKEN` existe.
- DNS chez Netlify (domaine acheté chez Netlify) : `www` → CNAME `aeternam.pages.dev` ; `aeternam.org` redirige vers www par le petit site Netlify de `netlify/`.

## État au 28 septembre 2026

- Test n° 1 (grille cubique face à GRB 221009A) : `recherche/2026-09-28-grille-lhaaso/` ; article publié en français.
- Test n° 2 (symétrie cubique des 100 rayons cosmiques les plus énergétiques d'Auger) : `recherche/2026-09-28-rayons-cosmiques/` ; verdict non (p = 0,20) ; article publié en français (`ARTICLE_2`). Demande numpy.
- Test n° 3 (huit sources gamma combinées, angle mort fermé) : `recherche/2026-09-28-dispersion-directionnelle/` ; maille ≥ 1,7e-26 m exclue pour toute orientation ; article `ARTICLE_3` en français.
- Test n° 4 (hasard quantique, bits bruts de photons intriqués et de qubits IBM, contrôles PRNG) : `recherche/2026-09-28-hasard-quantique/` ; verdict non (exclusion a posteriori de la machine Belem, signalée) ; `ARTICLE_4`.
- Synthèse centrale (`SYNTHESE`, page `/synthese/`, en tête de l'accueil) : `recherche/2026-09-28-synthese/` ; verdict non (pas de meilleures raisons de nous croire simulés ; simulation indétectable non exclue). Notre probabilité, choix central déclaré (ignorance log-uniforme, c = 1/2) : 0,069, soit environ 7 %. Les quatre tests en sont les études de cas. Une étude n'est publiée qu'une fois présente en français.
- Test n° 6 (ciel complet, Auger + Telescope Array, 1 022 événements, `ARTICLE_6`, `/test-6/`) : `recherche/2026-09-28-ciel-complet/` ; verdict non (p = 0,12) ; excès > 36 % le long des axes et > 23 % le long des diagonales exclus pour toute orientation. Table TA téléchargée (© AAS, non versionnée). ~10 min.
- Test n° 5 (rendu à la demande de l'observateur, `ARTICLE_5`, `/test-5/`) : `recherche/2026-09-28-rendu-a-la-demande/` ; verdict non (information jamais lue = information lue ; forme de Campbell et al. rejetée, le plus faible jeu à 5,3 σ). Demande numpy (~1 min).
- Nombres des nouvelles études : `site/nombres/<page>.json` (marqueur, clé de resultats.json, échelle, genre, précision), lus par `table_par_marqueurs`.
- Audit des démonstrations du « oui » (`AUDIT_1`, page `/audit-infodynamique/`) : `recherche/2026-09-28-audit-infodynamique/` ; verdict non (lemme de Vopson 2026 : maximum pris pour un minimum ; dérivation 2023 : Q = 0 n'implique pas ΔS = 0 ; réparation 2025 : hypothèses non démontrées). Texte intégral de Vopson 2023 non lu (accès refusé).
- Projet annexe « Une vie en une nuit » (`PROJET`, page `/projet/`, hors liste des travaux, annoncé en bas de l'accueil) : `recherche/2026-09-28-une-vie-en-une-nuit/` ; développement annoncé ; verdict « possible aujourd'hui : non » (facteur nécessaire 87 660, mesuré ≤ 1).
- Secret `CLOUDFLARE_API_TOKEN` créé par Aitor le 28/09/2026 : chaque envoi sur main publie le site.
