# ÆTERNAM : le blog de recherche

Décision d’Aitor du 20 novembre 2026 : ÆTERNAM traite de l’immortalité et ouvre un blog de recherche, avec ses articles et ceux de la communauté, rangés par thème, en français et en anglais. Les articles, leurs sources et leurs calculs constituent le contenu du site.

## Les sept thèmes

Chaque thème part d’une question sur une vie qui dure. L’ordre est le même partout.

| Thème | Question | Adresse |
| --- | --- | --- |
| Mémoire | Peut-on garder un souvenir pour toujours ? | `/sujets/memoire/` |
| Interfaces cerveau-machine | Peut-on lire dans un cerveau ? | `/sujets/interfaces-cerveau-machine/` |
| Vision et perception | Peut-on rendre la vue ? | `/sujets/vision/` |
| Rêve et temps vécu | Peut-on vivre une vie entière en une nuit ? | `/sujets/reve-temps/` |
| Relativité et trous noirs | Peut-on ralentir le temps ? | `/sujets/relativite-trous-noirs/` |
| Théorie de la simulation | Notre monde est-il une simulation ? | `/sujets/simulation/` |

Les BCI constituent un sujet de méthodes et d’interfaces. La vision et la mémoire ont leurs propres questions, même lorsqu’elles emploient ces interfaces. Le rêve et le temps vécu restent regroupés autour de l’expérience ; la simulation conserve ses preuves philosophiques et physiques distinctes. Un article peut appartenir à plusieurs thèmes.

## Organisation du blog

- L’accueil pose la question, « Peut-on vivre pour toujours ? », puis présente le blog thème par thème : la question, pourquoi elle compte, ce que l’on sait aujourd’hui avec les nombres des études, les derniers articles et le lien vers le thème entier. Il se termine par l’invitation à écrire.
- `/recherches/` est le blog : tous les articles par thème, puis les articles de la communauté. `/sujets/` liste les sept thèmes ; `/a-propos/` explique la démarche ; `/ecrire/` permet à chacun de proposer un article signé, relu en public.
- Chaque page de thème donne sa question, la réponse actuelle et l’étude qui la porte, ses questions ouvertes, des lectures pour commencer et les articles associés. Chaque article propose l’article suivant de son premier thème, puis ses thèmes et le blog.
- Les deux éditions ont les mêmes pages : le français à la racine, l’anglais sous `/en/`. Un article de la communauté paraît dans sa langue et il est listé dans les deux éditions.
- Les articles existants gardent leurs adresses et leurs fichiers de recherche. `/projet/` est l’article « Une vie en une nuit : une hypothèse à examiner » ; `/programme/` est « Rêve, temps et mémoire : un carnet de calculs ».

## Ligne éditoriale

Une question ambitieuse peut ouvrir un article. La conclusion doit correspondre à ce que les sources et les calculs permettent réellement d’établir. Conserver la distinction entre résultat publié, réanalyse exécutée, simulation sur hypothèses et proposition de recherche. Chaque sujet dispose de ses propres critères de preuve.

« Une vie en une nuit » est une hypothèse parmi les autres. Les applications de la mémoire sont examinées avec leurs limites scientifiques et les questions de consentement déjà développées dans les articles ; le blog ne propose pas de protocole d’expérimentation sur des personnes.

La présentation reste sobre et typographique : texte, liens et figures utiles, sans cartes ni panneaux. Conserver les préférences de lecture de `CLAUDE.md`.

## Ajouter un article

Un article signé d’un lecteur suit [contributions/README.md](contributions/README.md). Pour un article d’ÆTERNAM :

Définir le texte dans `site/langues/fr.py` et sa traduction, de même structure, dans `site/langues/en.py`, puis son adresse, son dossier de recherche, sa table de nombres et ses `sujets` dans `ETUDES` de `site/generer.py`. Les clés disponibles sont `relativite`, `bci`, `vision`, `memoire`, `reve-temps` et `simulation`.

Dans chaque thème, les articles sont classés par la date du dossier ; renseigner `publication` au format ISO si la date de publication diffère. Les pages de sujets, les liens en fin d’article, l’index et le plan du site sont générés depuis ce classement. Une proposition encore sans résultat n’a pas à être présentée comme un article ou une expérience déjà réalisée.
