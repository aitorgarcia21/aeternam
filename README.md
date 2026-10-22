# aeternam

[aeternam.org](https://www.aeternam.org) — blog de recherche.

Un carnet consacré aux interfaces cerveau-machine, à la vision, à la mémoire, au rêve et au temps vécu, à la relativité et aux trous noirs, ainsi qu’à la théorie de la simulation. La [structure éditoriale](BLOG.md) définit les six rubriques et la manière de classer les articles.

- `recherche/` : les analyses, leurs scripts Python reproductibles et leurs résultats.
- `site/langues/fr.py` : les textes et les six sujets du blog.
- `site/generer.py` : le générateur et le classement des articles dans `ETUDES`.
- `site/style.css` et `site/visuels.py` : la présentation et les figures tirées des résultats.
- `site/lecture.js` : suivi du sommaire des articles et navigation au clavier.
- `site/trou-noir.js` : le trou noir calculé en relativité générale (WebGL) : l’arrivée sur l’accueil, qui nous avale, et la scène du thème Relativité.
- `site/univers-scene.mjs` : illustrations procédurales en WebGL, avec repli Canvas, des pages de thème ; aucune image présentée comme une observation ou un enregistrement.
- `site/theme.js` : la scène de chaque page de thème, dessinée une fois.
- `site/polices/` : Newsreader et DM Sans, servies localement avec leurs licences.
- `netlify/` : la redirection de aeternam.org vers www.

Construire en local : `python3 site/generer.py` (résultat dans `public/`, ignoré par Git).
Déployer : envoyer sur `main` ; GitHub Actions construit et publie sur Cloudflare Pages. Un travail séparé rejoue les calculs de contrôle.

Le site est en français à la racine. L’accueil suit l’histoire de l’Univers en douze étapes au défilement, explique l’espace-temps par cinq expériences interactives, passe au cerveau (neurones, vision, mémoire, rêve), puis aux questions ouvertes (lire un cerveau, simulation, origine et futur de l’Univers), et se termine par les articles rangés par thème. Le seul titre principal est « aeternam », sans accroche ni appel à commencer. `/sujets/` donne accès aux six rubriques, `/recherches/` à tous les articles et `/a-propos/` à la démarche. Les anciennes adresses d’articles restent disponibles ; les préfixes de langue sont redirigés.

Les scènes cosmologiques sont schématiques, sans échelle temporelle linéaire. Les horloges utilisent les rapports relativistes annoncés ; la lumière suit une géodésique de Schwarzschild intégrée par Runge–Kutta. Vérifier les cas analytiques, la capture, la convergence, la limite de champ faible et les scènes : `node --test site/tests/*.test.mjs`. Ces contrôles font partie du déploiement. Le texte reste lisible sans JavaScript et les animations peuvent être figées ; la préférence de mouvement réduit est respectée.

La présentation typographique utilise une grille ouverte pour les index et une colonne de lecture avec sommaire pour les articles. Le sommaire devient repliable sur mobile ; les ancres existantes sont conservées. La pluie de bits reste discrète derrière le texte et devient fixe lorsque le navigateur demande de réduire les animations. Les liens de section fonctionnent aussi sans JavaScript.

Le [carnet de calculs sur le rêve](recherche/2026-09-29-programme-calcul/sources.md) documente les réanalyses et simulations exécutées. Le [rapport d’audit](AUDIT-SCIENTIFIQUE.md) explique les conclusions retirées et corrigées.

Les études du 3 octobre approfondissent les [BCI, la vision et la mémoire](recherche/2026-10-03-interfaces-cerveau/sources.md), ainsi que la [MEG, l’EEG et le contenu du rêve](recherche/2026-10-03-meg-eeg-reves/sources.md). Une [première réanalyse EEG](recherche/2026-10-03-bci-generalisation/sources.md) traite effectivement 540 essais de 12 personnes depuis les fichiers EDF de PhysioNet : protocole, provenance, contrôles indépendants et résultats individuels sont conservés. Elle n’est ni une reproduction du classement MOABB ni une BCI en ligne.

L’ancien [cadrage de startup](STARTUP.md) est conservé comme archive. Il est remplacé par le blog de recherche.

Les [trois études Einstein–Hawking du 8 octobre](recherche/2026-10-08-einstein-hawking/sources.md) traitent la relativité restreinte, les horloges terrestres et proches des trous noirs, puis les singularités, le rayonnement et l’information. Les calculs distinguent les modèles exécutés des résultats publiés repris, notamment l’estimation PREM du centre terrestre. Ce sont des revues et calculs pédagogiques, sans expérience physique nouvelle.

L’étude [Rêve et souvenir](recherche/2026-10-08-reve-recit/README.md) vérifie huit sources ou jeux candidats, recalcule la répartition des signaux du tableau de Konkoly et al. 2026 et prépare une analyse de jugements de durée appariés. Deux personnes produisent 68 % des 150 signaux du tableau. Aucune paire humaine de durée pendant/après n’a été acquise : l’effet principal reste non estimé. Le plan proposé et ses contrôles logiciels ne constituent ni un préenregistrement externe ni une expérience nouvelle.

La [simulation Monte-Carlo de calibration BCI](recherche/2026-10-03-bci-monte-carlo/sources.md) utilise ces EEG pour ajuster un générateur de caractéristiques. Elle exécute 600 campagnes virtuelles par hypothèse, huit budgets d’étiquettes et cinq conditions de bruit. Les résultats restent conditionnels au modèle ; le coût des observations de référence et la sensibilité aux hypothèses sont documentés.
