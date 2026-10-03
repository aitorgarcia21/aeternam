# Calibration BCI et bruit : simulation Monte-Carlo

Étude numérique exécutée le 3 octobre 2026. Question : combien d’essais personnels étiquetés permettent à notre décodeur d’améliorer son score, et comment cette quantité dépend-elle du bruit et du modèle de mesure ?

## Données humaines servant à construire le générateur

Les 540 essais, 12 personnes, 36 fichiers EDF et leurs annotations proviennent de [PhysioNet EEG Motor Movement/Imagery, version 1.0.0](https://physionet.org/content/eegmmidb/1.0.0/), Gerwin Schalk et contributeurs BCI2000, licence Open Data Commons Attribution 1.0, DOI [10.13026/C28G6P](https://doi.org/10.13026/C28G6P). Le dossier voisin `2026-10-03-bci-generalisation` contient l’extraction réellement exécutée, les empreintes des fichiers bruts et les contrôles SciPy/scikit-learn.

Nous utilisons son CSV de six log-puissances : C3/Cz/C4, bandes [8,13[ et [13,30[ Hz, segments de 0,5 à 3,5 secondes après la consigne. Son SHA-256 est contrôlé dans `protocole.json`. Les annotations décrivent la consigne ; les contrastes peuvent inclure des indices sensoriels ou des artefacts corrélés, pas uniquement l’intention motrice.

Les caractéristiques sont standardisées pour définir les unités du générateur. Par personne, nous estimons deux moyennes de classe, une covariance résiduelle à l’intérieur de chaque couple classe/run, et une variance diagonale de décalage entre runs. La covariance est contractée à 20 % vers sa diagonale. La variance des centres de run est diminuée de l’erreur d’échantillonnage estimée, puis tronquée à zéro. Avec trois runs, cette composante reste très incertaine.

## Générateur et expérience propres à Aeternam

Pour chaque campagne, le profil cible est tiré uniformément parmi les douze profils ajustés. Les onze autres fournissent chacun 48 observations synthétiques pour l’apprentissage source. Le profil cible fournit indépendamment un bloc de calibration, un bloc de test de 1 200 essais et les observations de référence. Aucun paramètre latent ni aucune étiquette du test n’entre dans le décodeur.

Le générateur gaussien est une approximation statistique des six valeurs reçues par le décodeur. Il ne génère ni anatomie, ni EEG temporel complet, ni activité neuronale biophysique. La réutilisation des paramètres de douze personnes ne crée aucune nouvelle diversité humaine. Les essais au sein d’un bloc sont indépendants conditionnellement à un décalage partagé. Les budgets sont imbriqués et équilibrés entre classes.

Les quatre hypothèses et tous les réglages sont consignés avant les premières courbes, sans préenregistrement externe : contrastes empiriques, contrastes divisés par deux, amplitude de dérive triplée, absence de contraste. La division par deux est un test de sensibilité arbitraire, pas une correction statistique estimée de la surestimation des contrastes. Les 600 campagnes utilisent les mêmes aléas entre hypothèses et conditions pour réduire le bruit de comparaison.

L’adaptation mélange les moyennes et covariances du modèle source et des essais cibles, avec un poids cible `n/(n+16)`. Le classifieur linéaire utilise des a priori égaux et une covariance contractée à 10 % vers la diagonale. Un comparateur entraîné sur les seuls essais cibles est également calculé. Aucune recherche d’hyperparamètres n’est effectuée sur les courbes.

Le bruit supplémentaire est un mélange de deux perturbations communes aux trois canaux, une par bande, dans l’espace des caractéristiques. Son intensité et celle des capteurs de référence sont des hypothèses fixées ; elles ne sont pas mesurées dans une salle et ne se convertissent pas en teslas ou en tension. Le niveau initial conserve la variabilité des mesures humaines, dont nous n’isolons pas les composantes neurales et non neurales.

La correction apprend une régression sur 256 observations cibles non étiquetées, distinctes de calibration et test. Ce coût s’ajoute aux essais étiquetés. Une autre condition suppose une amplitude de perturbation réduite à 20 % ; c’est une hypothèse numérique, sans reproduction d’un blindage. Un stress supplémentaire laisse entrer de l’activité utile dans le capteur de référence.

## Critère, précision et contrôles

Le critère fixé est un gain moyen d’au moins 5 points sur le même décodeur à zéro étiquette, avec borne inférieure Monte-Carlo 95 % positive, maintenu à tous les budgets supérieurs testés. Le zéro de la condition avec référence inclut déjà ses 256 observations non étiquetées. Le critère de 5 points est un choix exploratoire, pas une utilité clinique démontrée. Les seuils sont des minima sur la grille, pas des minima exacts.

Les intervalles valent moyenne ± 1,96 erreur standard entre campagnes. Ils décrivent la précision Monte-Carlo sous le modèle fixé, sans incertitude sur ses paramètres, sans garantie de couverture humaine et sans correction de comparaisons multiples. Les quantiles entre campagnes sont conservés séparément. Le seuil du bruit non corrigé est proche de la frontière des 5 points : son intervalle la traverse. Les conclusions doivent montrer cette fragilité.

`verifier.py` compare 48 000 décisions aux densités gaussiennes de SciPy, la correction par référence à Ridge de scikit-learn, et les 20 seuils aux calculs de la bibliothèque standard Python. Les autotests comprennent un cas gaussien à résultat analytique, un retrait exact de bruit et un exemple où la référence retire le signal utile. Le scénario sans contraste doit rester proche de 50 %.

Un contrôle descriptif ajuste un modèle sur deux runs humains et regarde la couverture du troisième par une ellipse gaussienne indicative. Il examine la plausibilité d’une hypothèse de dispersion, sans valider les prévisions de calibration à 64–256 essais. Les données d’origine ne contiennent que 45 essais par personne.

## Ce que font les équipes chinoises consultées

- **Beihang, notamment son institut de Ningbo — contrôle magnétique.** [Dou et al., ISA Transactions, mis en ligne le 5 août 2025](https://doi.org/10.1016/j.isatra.2025.07.050), [résumé et affiliations](https://pubmed.ncbi.nlm.nih.gov/40783370/). Source primaire : résumé, introduction et descriptions du montage accessibles chez l’éditeur. Leur système combine une enceinte blindée, des bobines conçues pour limiter le bruit propre et une commande avec rejet actif des perturbations. Il traite le champ autour d’un magnétomètre, en vue de mesures MEG/MCG. Notre atténuation numérique n’est pas une reproduction de leur montage ; aucun de leurs niveaux magnétiques ne paramètre notre simulation EEG.
- **NCCLab, Southern University of Science and Technology, Shenzhen — artefacts EEG.** [Zhang et al., EEGdenoiseNet, Journal of Neural Engineering, 2021](https://doi.org/10.1088/1741-2552/ac2bf8), [code et données des auteurs](https://github.com/ncclabsustech/EEGdenoiseNet). Leur méthode de comparaison mélange des segments EEG de référence à des artefacts oculaires ou musculaires, puis mesure la reconstruction. Les références dites propres ont elles-mêmes été préparées par traitement et inspection. Cette construction fournit une cible connue mais ne garantit pas le comportement dans tout enregistrement réel. Nous retenons le principe d’une contamination contrôlée ; nous n’avons ni entraîné leurs réseaux ni importé leurs données ici.
- **Traitement standard des artefacts.** La [documentation primaire MNE sur l’ICA](https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html) et celle sur les [filtres](https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html) décrivent des outils complémentaires. Un filtre fréquentiel, une composante oculaire et une perturbation magnétique externe ne sont pas un même problème. Notre simulateur ne reproduit pas l’ICA ni un filtre temporel.

## Reproduction dans le dépôt

1. Avec NumPy, exécuter `python3 recherche/2026-10-03-bci-monte-carlo/analyse.py`. Le CSV humain versionné dans le dossier voisin est la seule entrée de mesure ; `--out` permet un rejeu indépendant.
2. Pour les vérifications indépendantes et les figures, utiliser un environnement contenant `requirements-verification.txt`, puis lancer `verifier.py` et `figures.py` dans ce dossier.
3. `resultats.json` contient les paramètres ajustés, les scores de toutes les campagnes, les courbes, les intervalles, les comparateurs et les seuils manquants conservés comme `null`.

La simulation sert à préparer une expérience humaine future. La mesure du bénéfice réel exigerait des personnes et des séances indépendantes, le bruit effectivement enregistré, une séparation chronologique des phases et un examen des commandes déclenchées pendant le repos.
