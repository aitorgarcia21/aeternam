# aeternam

[aeternam.org](https://aeternam.org) — une vie entière, le temps d’une nuit.

Aeternam porte un projet de recherche sur le rêve et le temps vécu, avec l’ambition d’ouvrir d’autres vies possibles. Le [cadrage de la startup](STARTUP.md) décrit les cinq axes et la stratégie de recherche sans budget expérimental.

- `recherche/` : les analyses, chacune avec son script Python reproductible et ses résultats.
- `site/` : le générateur (`generer.py`), le style et les textes par langue (le français est la source).
- Le site est en français à la racine ; le générateur redirige les anciennes adresses avec préfixe de langue.
- `netlify/` : la redirection de aeternam.org vers www (le DNS du domaine est chez Netlify).

Construire en local : `python3 site/generer.py` (le résultat va dans `public/`).
Déployer : envoyer sur `main` ; GitHub Actions refait les calculs, construit et publie sur Cloudflare Pages.

Le [programme de calcul](recherche/2026-09-29-programme-calcul/sources.md) documente les réanalyses et simulations exécutées. Le [rapport d’audit](AUDIT-SCIENTIFIQUE.md) explique les conclusions retirées et corrigées. La théorie de la simulation reste une branche de recherche distincte.
