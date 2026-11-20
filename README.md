# ÆTERNAM

[æternam.com](https://xn--ternam-oua.com) — l’immortalité, et un blog de recherche ouvert, en français et en anglais : chacun peut y publier un article signé de son nom ([mode d’emploi](contributions/README.md)).

Six thèmes, six questions sur une vie qui dure : la mémoire, les interfaces cerveau-machine, la vision, le rêve et le temps vécu, la relativité et les trous noirs, la théorie de la simulation. La [structure éditoriale](BLOG.md) définit les thèmes et la manière de classer les articles.

- `recherche/` : les analyses, leurs scripts Python reproductibles et leurs résultats.
- `site/langues/fr.py` : les textes et les six thèmes du blog ; `site/langues/en.py` : leur traduction, dont la structure est vérifiée à chaque construction.
- `site/generer.py` : le générateur et le classement des articles dans `ETUDES`.
- `site/accueil.py`, `site/accueil/` : l’accueil (le nom, la question, le sablier dont le sable s’arrête, puis le blog).
- `site/dessins.py` : les dessins au trait de l’accueil et des pages de thème.
- `site/style.css`, `site/base.js` et `site/visuels.py` : la présentation, la barre de navigation et les figures tirées des résultats.
- `site/lecture.js` : suivi du sommaire des articles et navigation au clavier.
- `contributions/`, `site/contributions.py`, `site/ecrire.js` : les articles signés que chacun peut proposer (`/ecrire/`), relus en public, sous licence CC BY 4.0 ; mode d’emploi dans [contributions/README.md](contributions/README.md).
- `site/theme.js`, `site/univers-scene.mjs`, `site/trou-noir.js` : les anciennes scènes WebGL, que le site ne charge plus ; leurs tests tournent encore.
- `site/polices/` : Newsreader et DM Sans, servies localement avec leurs licences.
- `netlify/` : la redirection de aeternam.org vers æternam.com.

Construire en local : `python3 site/generer.py` (résultat dans `public/`, ignoré par Git). La construction vérifie aussi chaque article signé et s’arrête sur la moindre erreur.
Déployer : envoyer sur `main` ; GitHub Actions construit et publie sur Cloudflare Pages. Un travail séparé rejoue les calculs de contrôle. Chaque demande de publication (pull request) est construite sans être publiée.

Deux éditions, aux mêmes adresses : le français à la racine, l’anglais sous `/en/`. L’accueil montre le nom « ÆTERNAM » et une question, « Peut-on vivre pour toujours ? », puis le blog thème par thème et l’invitation à écrire. `/recherches/` donne accès à tous les articles (articles signés compris), `/sujets/` aux six thèmes, `/ecrire/` à la publication d’un article signé et `/a-propos/` à la démarche. Les anciennes adresses d’articles restent disponibles ; `/fr/…` et `/cap/` sont redirigées.

Les dessins sont des illustrations au trait, hors échelle, jamais des observations. Les tests (`node --test site/tests/*.test.mjs`) font partie du déploiement. Le texte reste lisible sans JavaScript ; la préférence de mouvement réduit est respectée : l’accueil montre alors le nom et la question.

La présentation typographique utilise une grille ouverte pour les index et une colonne de lecture avec sommaire pour les articles. Le sommaire devient repliable sur mobile ; les ancres existantes sont conservées. Les liens de section fonctionnent aussi sans JavaScript.

Le [carnet de calculs sur le rêve](recherche/2026-09-29-programme-calcul/sources.md) documente les réanalyses et simulations exécutées. Le [rapport d’audit](AUDIT-SCIENTIFIQUE.md) explique les conclusions retirées et corrigées.

Les études du 3 octobre approfondissent les [BCI, la vision et la mémoire](recherche/2026-10-03-interfaces-cerveau/sources.md), ainsi que la [MEG, l’EEG et le contenu du rêve](recherche/2026-10-03-meg-eeg-reves/sources.md). Une [première réanalyse EEG](recherche/2026-10-03-bci-generalisation/sources.md) traite effectivement 540 essais de 12 personnes depuis les fichiers EDF de PhysioNet : protocole, provenance, contrôles indépendants et résultats individuels sont conservés. Elle n’est ni une reproduction du classement MOABB ni une BCI en ligne.

L’ancien [cadrage de startup](STARTUP.md) est conservé comme archive. Il est remplacé par le blog de recherche.

Les [trois études Einstein–Hawking du 8 octobre](recherche/2026-10-08-einstein-hawking/sources.md) traitent la relativité restreinte, les horloges terrestres et proches des trous noirs, puis les singularités, le rayonnement et l’information. Les calculs distinguent les modèles exécutés des résultats publiés repris, notamment l’estimation PREM du centre terrestre. Ce sont des revues et calculs pédagogiques, sans expérience physique nouvelle.

L’étude [Rêve et souvenir](recherche/2026-10-08-reve-recit/README.md) vérifie huit sources ou jeux candidats, recalcule la répartition des signaux du tableau de Konkoly et al. 2026 et prépare une analyse de jugements de durée appariés. Deux personnes produisent 68 % des 150 signaux du tableau. Aucune paire humaine de durée pendant/après n’a été acquise : l’effet principal reste non estimé. Le plan proposé et ses contrôles logiciels ne constituent ni un préenregistrement externe ni une expérience nouvelle.

La [simulation Monte-Carlo de calibration BCI](recherche/2026-10-03-bci-monte-carlo/sources.md) utilise ces EEG pour ajuster un générateur de caractéristiques. Elle exécute 600 campagnes virtuelles par hypothèse, huit budgets d’étiquettes et cinq conditions de bruit. Les résultats restent conditionnels au modèle ; le coût des observations de référence et la sensibilité aux hypothèses sont documentés.

## Licence

- Les textes, les figures et les résultats d’ÆTERNAM, articles signés compris, sont sous licence [CC BY 4.0](LICENSE) : chacun peut les reprendre, les adapter et les republier en citant leur auteur.
- Le code (le générateur, les scripts et les tests de `site/`, les scripts d’analyse de `recherche/`, les workflows de `.github/`) est sous licence [MIT](LICENSE-CODE).
- Ce qui vient d’ailleurs garde sa licence : les jeux de données et les publications sont attribués à leur source dans chaque analyse, et les polices de `site/polices/` sont accompagnées de la leur.
