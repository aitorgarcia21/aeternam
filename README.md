# aeternam

[aeternam.org](https://www.aeternam.org) — blog de recherche.

Un carnet consacré aux interfaces cerveau-machine, à la vision, à la mémoire, au rêve et au temps vécu, ainsi qu’à la théorie de la simulation. La [structure éditoriale](BLOG.md) définit les cinq rubriques et la manière de classer les articles.

- `recherche/` : les analyses, leurs scripts Python reproductibles et leurs résultats.
- `site/langues/fr.py` : les textes et les cinq sujets du blog.
- `site/generer.py` : le générateur et le classement des articles dans `ETUDES`.
- `site/style.css` et `site/visuels.py` : la présentation et les figures tirées des résultats.
- `netlify/` : la redirection de aeternam.org vers www.

Construire en local : `python3 site/generer.py` (résultat dans `public/`, ignoré par Git).
Déployer : envoyer sur `main` ; GitHub Actions construit et publie sur Cloudflare Pages. Un travail séparé rejoue les calculs de contrôle.

Le site est en français à la racine. L’accueil présente les sujets et les derniers articles ; `/sujets/` donne accès aux rubriques, `/recherches/` à tous les articles et `/a-propos/` à la démarche. Les anciennes adresses d’articles restent disponibles ; les préfixes de langue sont redirigés.

Le [carnet de calculs sur le rêve](recherche/2026-09-29-programme-calcul/sources.md) documente les réanalyses et simulations exécutées. Le [rapport d’audit](AUDIT-SCIENTIFIQUE.md) explique les conclusions retirées et corrigées.

Les études du 3 octobre approfondissent les [BCI, la vision et la mémoire](recherche/2026-10-03-interfaces-cerveau/sources.md), ainsi que la [MEG, l’EEG et le contenu du rêve](recherche/2026-10-03-meg-eeg-reves/sources.md). Les pistes de reproduction sur signaux bruts restent des travaux proposés.

L’ancien [cadrage de startup](STARTUP.md) est conservé comme archive. Il est remplacé par le blog de recherche.
