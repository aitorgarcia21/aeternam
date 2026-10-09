# Aeternam : blog de recherche

Décision d’Aitor du 3 octobre 2026 : organiser Aeternam comme un blog autour de ses principaux intérêts de recherche. Les articles, leurs sources et leurs calculs constituent le contenu du site.

## Les six sujets

Le 8 octobre 2026, les études demandées sur Einstein, Hawking et les horloges ajoutent la rubrique « Relativité et trous noirs » aux cinq sujets initiaux.

| Sujet | Question directrice | Adresse |
| --- | --- | --- |
| Relativité et trous noirs | Comment les trajectoires et la gravitation modifient-elles les durées, et où nos théories atteignent-elles leurs limites ? | `/sujets/relativite-trous-noirs/` |
| Interfaces cerveau-machine | Quelles informations lire dans le cerveau, et comment les relier à une machine ? | `/sujets/interfaces-cerveau-machine/` |
| Vision et perception | Comment provoquer une perception utile ou ajouter une image à la vision ? | `/sujets/vision/` |
| Mémoire | Que peut-on former, renforcer ou modifier dans un souvenir ? | `/sujets/memoire/` |
| Rêve et temps vécu | Comment étudier le contenu du rêve et la durée de l’expérience ? | `/sujets/reve-temps/` |
| Théorie de la simulation | Quels arguments et quelles observations permettent d’examiner des modèles de monde simulé ? | `/sujets/simulation/` |

Les BCI constituent un sujet de méthodes et d’interfaces. La vision et la mémoire ont leurs propres questions, même lorsqu’elles emploient ces interfaces. Le rêve et le temps vécu restent regroupés autour de l’expérience ; la simulation conserve ses preuves philosophiques et physiques distinctes. Un article peut appartenir à plusieurs sujets.

## Organisation du blog

- Depuis la demande du 9 octobre 2026, l’accueil présente une histoire de l’Univers au défilement, de ses limites initiales à aujourd’hui, suivie d’expériences sur l’espace-temps et la relativité. Un seul titre « aeternam », des informations et des schémas ; pas d’accroche ni de bouton d’entrée dans le parcours.
- Chaque étape et expérience affiche une seule phrase essentielle. Les développements et sources restent dans les volets « Analyse détaillée », fermés par défaut ; les questions sur l’origine et le futur suivent le même principe.
- Aucun compteur d’étapes ni barre de progression. Les schémas nomment directement les objets scientifiques ; les formes et les couleurs n’ajoutent pas de précision physique non étayée. Le défilement reste libre, avec une navigation discrète entre chapitres.
- Les vues d’artiste occupent l’essentiel de la scène : matière en volume, nuage électronique, galaxie et disque protoplanétaire. Elles sont signalées comme telles, sans photographie ou simulation revendiquée. Les schémas de composition restent dans l’analyse détaillée ; les expériences de relativité conservent leurs calculs et commandes.
- Les six rubriques restent accessibles par « Thèmes », et les articles sont regroupés par thème dans « Articles ». Le parcours cosmologique ne change ni leur classement ni leurs adresses.
- Chaque page de sujet décrit ses questions, propose des passages pour commencer et rassemble les articles associés.
- `/recherches/` regroupe tous les articles par thème ; `/a-propos/` explique la démarche.
- Chaque article permet de revenir à ses sujets et à l’index.
- Les articles existants gardent leurs adresses et leurs fichiers de recherche. `/projet/` devient l’article « Une vie en une nuit : une hypothèse à examiner » ; `/programme/` devient « Rêve, temps et mémoire : un carnet de calculs ».

## Ligne éditoriale

Une question ambitieuse peut ouvrir un article. La conclusion doit correspondre à ce que les sources et les calculs permettent réellement d’établir. Conserver la distinction entre résultat publié, réanalyse exécutée, simulation sur hypothèses et proposition de recherche. Chaque sujet dispose de ses propres critères de preuve.

« Une vie en une nuit » est une hypothèse parmi les autres. Les applications de la mémoire sont examinées avec leurs limites scientifiques et les questions de consentement déjà développées dans les articles ; le blog ne propose pas de protocole d’expérimentation sur des personnes.

La présentation reste sobre et typographique : texte, liens et figures utiles, sans cartes ni panneaux. Conserver les préférences de lecture de `CLAUDE.md`.

## Ajouter un article

Définir le texte dans `site/langues/fr.py`, puis son adresse, son dossier de recherche, sa table de nombres et ses `sujets` dans `ETUDES` de `site/generer.py`. Les clés disponibles sont `relativite`, `bci`, `vision`, `memoire`, `reve-temps` et `simulation`.

Dans chaque thème, les articles sont classés par la date du dossier ; renseigner `publication` au format ISO si la date de publication diffère. Les pages de sujets, les liens en fin d’article, l’index et le plan du site sont générés depuis ce classement. Une proposition encore sans résultat n’a pas à être présentée comme un article ou une expérience déjà réalisée.
