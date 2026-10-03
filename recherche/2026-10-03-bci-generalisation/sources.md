# BCI : usages récents et première réanalyse de signaux EEG

Vérification documentaire du 3 octobre 2026. Revue sélective de sources primaires, accompagnée d’une analyse exploratoire indépendante sur un sous-ensemble ouvert. L’EEG d’imagerie motrice ne reproduit pas les résultats des implants de communication.

## Sources primaires récentes

- [Card et al., Nature Medicine, 15 juin 2026](https://doi.org/10.1038/s41591-026-04414-6). Sections « Independent use », « Speech decoding », « Discussion », « Data availability » et figure 2. Distinguer le score par mot dans la tâche de copie du jugement personnel sur les phrases. Les signaux et transcriptions de l’usage personnel ne sont pas publics ; des données de figures sont annoncées dans le dépôt des auteurs.
- [Brosler et al., Nature Neuroscience, 14 septembre 2026](https://doi.org/10.1038/s41593-026-02446-2). Sections « Participants », « Real-time speech-and-gesture blocks » et figure 5. Les dénominateurs varient selon l’expérience ; les conversations sont des démonstrations limitées. Les ECoG sont à accès restreint ; code et données de figures sont annoncés publics.
- [Choudhari et al., Nature Neuroscience, 11 mai 2026](https://doi.org/10.1038/s41593-026-02281-5). Résultats, expérience 1 et disponibilité. L’article mesure le bénéfice perceptif de la boucle, avec un équipement intracrânien. Les signaux sont annoncés sur demande, les données de figures sont fournies.
- [Spalding et al., Nature Communications, 16 juillet 2026](https://doi.org/10.1038/s41467-026-75455-1), [texte de la version publiée dans PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13490415/). Sections « Cross-patient phoneme decoding », discussion et disponibilité. L’alignement utilise l’apprentissage du patient cible. Cette version publiée remplace, pour notre revue, la prépublication de 2025. Accès aux signaux restreint.

Les observations numériques et leur portée sont consignées dans `releves.json`. Nous n’avons pas demandé d’accès aux données cliniques ni contacté les équipes.

## Données effectivement traitées

[Schalk, EEG Motor Movement/Imagery Dataset, PhysioNet, version 1.0.0](https://physionet.org/content/eegmmidb/1.0.0/), DOI [10.13026/C28G6P](https://doi.org/10.13026/C28G6P). Attribution : Gerwin Schalk et les contributeurs BCI2000. Référence instrumentale : [Schalk et al., 2004](https://doi.org/10.1109/TBME.2004.827072). Licence : Open Data Commons Attribution License 1.0.

Le sous-ensemble est défini dans `protocole.json` : S001 à S012, runs 04, 08 et 12. La [documentation officielle MNE](https://mne.tools/stable/generated/mne.datasets.eegbci.load_data.html) confirme que ces runs portent sur l’imagerie main gauche/main droite. Les annotations T1/T2 sont interprétées conformément à la documentation du jeu. Les fichiers EDF proviennent directement de PhysioNet ; leurs URL, tailles et SHA-256 sont conservés dans `donnees/manifest.json`.

## Méthode propre à cette réanalyse

Le choix du sous-ensemble et des paramètres est écrit avant le calcul des scores. Il s’agit d’un choix de convenance, sans préenregistrement externe. Aucun hyperparamètre n’est recherché sur les résultats.

Un essai produit six caractéristiques : puissances sur C3, Cz et C4, dans les bandes [8, 13[ et [13, 30[ Hz, calculées entre 0,5 et 3,5 secondes après la consigne. La référence enregistrée est conservée. Le segment est centré puis pondéré par Hann ; les puissances unilatérales sont intégrées puis transformées en log10. Aucun essai n’est écarté sur son amplitude ou son score.

Le décodeur est une analyse discriminante linéaire. Les moyennes, écarts types, moyennes par classe et covariance sont appris uniquement sur le lot d’apprentissage. La covariance est régularisée avec un coefficient fixé à 0,1 vers une identité de même trace ; les probabilités a priori sont égales.

La comparaison porte sur deux cadres : personne entièrement réservée, et run réservé au sein d’une personne. Les predictions hors apprentissage sont agrégées sur chaque personne ; la moyenne donne le même poids à chaque personne. Les fenêtres ne sont ni découpées ni mélangées entre apprentissage et test. Les runs réservés ne constituent pas un essai prospectif sur un autre jour.

Le contrôle par permutations réentraîne toute la chaîne après mélange des étiquettes dans chaque bloc personne/run. Deux tests unilatéraux sont corrigés par Holm. Leur interprétation suppose l’échangeabilité des essais dans ces blocs ; ils restent exploratoires, notamment face aux dépendances temporelles possibles. Ils ne peuvent pas exclure la classification d’indices visuels ou musculaires associés à la consigne.

La figure montre les résultats individuels. Son étendue représente la variation observée, pas un intervalle de confiance de population. Les plis partagent des données d’apprentissage ; nous ne les traitons pas comme des réplications indépendantes pour fabriquer un intervalle binomial.

## Reproduction

1. Créer un environnement Python et installer `requirements-extraction.txt`.
2. Exécuter `extraire.py`. Les bruts sont mis en cache dans `donnees/brutes/`, hors Git ; les caractéristiques et le manifeste sont versionnés.
3. Exécuter `analyse.py` avec NumPy. Le résultat est écrit dans `resultats.json`, ou dans le chemin fourni à `--out`.
4. Exécuter `verifier.py` pour comparer le traitement du signal avec SciPy et les prédictions avec scikit-learn.
5. Exécuter `figure.py` pour régénérer le graphique depuis les résultats.

L’[exemple officiel MNE sur l’imagerie motrice](https://mne.tools/stable/auto_examples/decoding/decoding_csp_eeg.html) est un repère logiciel. Notre modèle à trois canaux et notre découpage par personne/run sont différents ; aucun score de cet exemple ni classement MOABB n’est revendiqué.
