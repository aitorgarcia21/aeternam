# ÆTERNAM : la recherche et le blog

Décision d’Aitor du 21 novembre 2026 : le site a trois étages. L’accueil explique tout, avec l’ambition (la thèse : le vieillissement se joue dans les cellules ; savoir le ralentir, puis le réparer, plutôt que remplacer des organes). `/recherche/` dit où en est la recherche d’ÆTERNAM sur le vieillissement, étape par étape (mesuré, prêt à financer, à faire). `/recherches/` est le blog des curieux : les sujets sans rapport direct avec cette recherche, et les articles de la communauté. Cette décision complète celle du 20 novembre (un blog de recherche rangé par thème, en français et en anglais).

Une étude de la recherche porte `'recherche': True` dans `ETUDES` de `site/generer.py` : elle apparaît sur `/recherche/` (textes : `RECHERCHE` de `site/langues/`), jamais dans le blog. Les autres études forment le blog.

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

- L’accueil pose la question, « Peut-on vivre pour toujours ? », explique pourquoi l’on vieillit, où cela se joue (les cellules), ce que nous avons mesuré et ce qui reste à financer. Il se termine par l’appel.
- `/recherche/` : où nous en sommes. `/recherches/` est le blog : les articles des curieux par thème (seuls les thèmes qui ont des articles du blog y figurent), puis les articles de la communauté. `/sujets/` liste les sept thèmes ; `/a-propos/` explique la démarche ; `/ecrire/` permet à chacun de proposer un article signé, relu en public.
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
