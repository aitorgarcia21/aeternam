# aeternam

[aeternam.org](https://aeternam.org) — une vie entière, le temps d’une nuit.

Aeternam porte un projet de recherche sur le rêve et le temps vécu, avec l’ambition d’ouvrir d’autres vies possibles. Le [cadrage de la startup](STARTUP.md) décrit la mission, le premier produit proposé et le plan de lancement.

- `recherche/` : les analyses, chacune avec son script Python reproductible et ses résultats.
- `site/` : le générateur (`generer.py`), le style et les textes par langue (le français est la source).
- Le site est en français à la racine ; le générateur redirige les anciennes adresses avec préfixe de langue.
- `netlify/` : la redirection de aeternam.org vers www (le DNS du domaine est chez Netlify).

Construire en local : `python3 site/generer.py` (le résultat va dans `public/`).
Déployer : envoyer sur `main` ; GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages.
