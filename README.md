# aeternam

[aeternam.org](https://aeternam.org) — recherche sur la théorie de la simulation.

- `recherche/` : les analyses, chacune avec son script Python reproductible et ses résultats.
- `site/` : le générateur (`generer.py`), le style et les textes par langue (le français est la source).
- `functions/_middleware.js` : envoie chaque visiteur vers sa langue.
- `netlify/` : la redirection de aeternam.org vers www (le DNS du domaine est chez Netlify).

Construire en local : `python3 site/generer.py` (le résultat va dans `public/`).
Déployer : envoyer sur `main` ; GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages.
