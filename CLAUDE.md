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
- Jamais de cartes ni d'encadrés (fond, bordure, barre colorée) : texte nu, typographique.
- Jamais de surtitre, d'étiquette en petites capitales au-dessus d'un titre, ni de sélecteur de langue visible.
- La langue est choisie automatiquement selon le navigateur ; tout le contenu doit exister dans les 11 langues (fr, en, es, de, it, pt, ru, zh, ja, ko, ar).
- Chaque chiffre vient d'une source primaire vérifiée ou d'un calcul reproductible du dépôt ; jamais de mémoire.

## Fonctionnement

- Recherche : `recherche/<date>-<sujet>/`, avec un script Python reproductible (`analyse.py`, autotests) et ses `resultats.json`.
- Textes : `site/langues/<code>.py` ; le français est la source, les traductions se font dans la session et doivent passer `python3 site/generer.py --verifier <code>`.
- Construire : `python3 site/generer.py` (résultat dans `public/`, ignoré par git).
- Déployer : envoyer sur `main`. GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages (projet `aeternam`, www.aeternam.org) si le secret `CLOUDFLARE_API_TOKEN` existe.
- `functions/_middleware.js` envoie chaque visiteur vers sa langue ; n'y lister que les langues publiées.
- DNS chez Netlify (domaine acheté chez Netlify) : `www` → CNAME `aeternam.pages.dev` ; `aeternam.org` redirige vers www par le petit site Netlify de `netlify/`.

## État au 28 septembre 2026

- Test n° 1 (grille cubique face à GRB 221009A) : `recherche/2026-09-28-grille-lhaaso/` ; article publié en fr, en, es, de, it, pt, ru. Chinois en brouillon partiel (`site/langues/_brouillon_zh.py`) ; japonais, coréen, arabe à faire.
- Test n° 2 (symétrie cubique des 100 rayons cosmiques les plus énergétiques d'Auger) : `recherche/2026-09-28-rayons-cosmiques/` ; verdict non (p = 0,20) ; article publié en fr, en, es, de, it, pt, ru (`ARTICLE_2`). Demande numpy.
- Test n° 3 (huit sources gamma combinées, angle mort fermé) : `recherche/2026-09-28-dispersion-directionnelle/` ; maille ≥ 1,7e-26 m exclue pour toute orientation ; article `ARTICLE_3` en 7 langues.
- Secret `CLOUDFLARE_API_TOKEN` créé par Aitor le 28/09/2026 : chaque envoi sur main publie le site.
