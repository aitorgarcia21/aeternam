# Articles signés

ÆTERNAM est un carnet de science ouvert : chacun peut y publier un article sous son nom. Un article est un fichier Markdown de ce dossier. Il arrive par une demande de publication (*pull request*), relue en public avant d’être fusionnée, puis paraît à l’adresse `æternam.com/contributions/AAAA-MM-JJ-titre-court/`.

Le plus simple est le formulaire de la page [Écrire](https://xn--ternam-oua.com/ecrire/) : il prépare le fichier et l’ouvre sur GitHub, déjà rempli. Il faut un compte GitHub, gratuit.

## Le fichier

Nom : `AAAA-MM-JJ-titre-court.md`, la date de la proposition puis quelques mots du titre, en minuscules, chiffres et tirets. Les fichiers dont le nom commence par `_` ne sont pas publiés ([`_modele.md`](_modele.md) sert de point de départ).

Il commence par un en-tête entre deux lignes `---` :

```
---
titre: Ce que mesure vraiment un EEG sec
auteur: Prénom Nom
date: 2026-11-17
theme: bci
resume: Une ou deux phrases qui disent ce que l’article établit.
orcid: 0000-0000-0000-0000
licence: CC BY 4.0
---
```

| Clé | Obligatoire | Règle |
| --- | --- | --- |
| `titre` | oui | 3 à 140 caractères |
| `auteur` | oui | votre nom, sans lien |
| `date` | non | si présente, la même que dans le nom du fichier |
| `theme` | non | `relativite`, `vision`, `memoire`, `reve-temps`, `bci` ou `simulation` |
| `resume` | non | 300 caractères au plus |
| `orcid` | non | forme `0000-0000-0000-0000` |
| `licence` | non | toujours `CC BY 4.0` |

Le texte suit l’en-tête, en Markdown : `##` et `###` pour les titres, `**gras**`, `*italique*`, `[lien](https://…)`, listes `-` ou `1.`, citations `>`, formules `$$…$$` et `\(…\)`, blocs de code entre deux lignes ```` ``` ````. Le HTML n’est pas interprété. Les images vont dans [`medias/`](medias/) (PNG, JPEG, WebP ou GIF, jamais de SVG) et s’appellent avec `![légende](medias/nom.png)`. Il faut au moins 200 caractères de texte.

## Les règles

- **Signer de son nom.** L’article engage son auteur ; la signature, la date et l’historique des versions restent publics.
- **Séparer ce qui est mesuré, calculé et supposé.** Chaque nombre renvoie à sa source primaire ou à un calcul que d’autres peuvent refaire ; une simulation se présente comme une simulation.
- **Citer à l’endroit où l’on s’en sert**, dans la phrase qui s’appuie sur la source.
- **Expliquer, puis détailler** : `## Explication` en mots simples, puis `## Analyse détaillée`, puis `## Sources`.
- **Accepter la relecture.** Les remarques se font en public, sur la demande de publication. Elles portent sur les preuves et la clarté, pas sur les opinions.

## La vérification

À chaque demande de publication, GitHub construit le site avec l’article (`python3 site/generer.py`). Si quelque chose ne va pas (en-tête, lien, image, longueur), la construction s’arrête et son message dit quoi corriger. On peut lancer la même commande chez soi.

## Licence

Les articles sont publiés sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr) : chacun peut les reprendre en citant leur auteur. En proposant un article, vous confirmez l’avoir écrit et accepter cette licence.
