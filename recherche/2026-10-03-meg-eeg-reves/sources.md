# MEG, EEG et contenu du rêve

Vérification le 3 octobre 2026. Analyse documentaire et contre-exemples mathématiques exécutés. Aucun enregistrement cérébral ni entraînement d'un décodeur Aeternam dans ce dossier.

## Sources et portée

| Source primaire | Éléments vérifiés | Limite retenue |
| --- | --- | --- |
| [Lévy et al., Nature Neuroscience, 2026](https://doi.org/10.1038/s41593-026-02303-2) | Résumé, résultats, analyse des erreurs et méthodes de Brain2Qwerty v1 | Frappe réelle ; modalités enregistrées en sessions distinctes ; sortie après la phrase et dépendance aux horodatages de frappe |
| [Zhang et al., Brain2Qwerty v2, prépublication](https://facebookresearch.github.io/brain2qwerty/assets/brain2qwerty_v2.pdf) | Résumé, discussion p. 10, méthodes et limites temporelles | Le passage « Real-time latency » indique une architecture non causale travaillant sur la phrase entière. Asynchrone ne signifie pas sortie immédiate |
| [Dépôt officiel Brain2Qwerty](https://github.com/facebookresearch/brain2qwerty) et [SpanishBCBL](https://huggingface.co/datasets/bcbl190626/SpanishBCBL) | README du code et des données ; API publique listant EEG et MEG | Code et données v1 indiqués CC BY-NC 4.0. V2 annoncée sous embargo. Les sessions répétées d'une même personne doivent être regroupées |
| [Holmes et al., IEEE TBME, 2025](https://doi.org/10.1109/TBME.2024.3465654) | Résumé primaire et protocole comparant des salles blindées | Un blindage allégé reste un blindage ; pas de démonstration d'une chambre domestique |
| [Cho et al., Microsystems & Nanoengineering, 2026](https://doi.org/10.1038/s41378-026-01226-z) | Détecteur optique intégré, sensibilité mesurée à 10 Hz | Miniaturisation d'un composant, pas d'un système complet ; pas de prix de casque |
| [QuSpin QZFM Gen-3](https://quspin.com/products-qzfm/) | Tarif affiché pour petites quantités et supplément triaxial | Instantané commercial, pas devis d'une installation. Le marché à 830 000 € du texte transmis n'a pas été corroboré par une référence d'attribution identifiable ; montant écarté |
| [Salfi et al., J Sleep Res, 2025](https://doi.org/10.1111/jsr.70000) | Texte intégral : mémoire de pseudomots, effectifs, variations test-retest, interaction statistique, disponibilité | Le +8,6 % est une variation de traduction des items indicés ; ne pas le présenter comme un gain de contenu rêvé. Données sur demande |
| [Konkoly et al., Neuropsychologia, 2025](https://doi.org/10.1016/j.neuropsychologia.2025.109229) | Méthodes et résultats sur indices sonores en REM, incorporations dans les récits | Manipulation de certains éléments rapportés ; pas une narration choisie dans son ensemble |
| [Kumral et al., iScience, 2025](https://doi.org/10.1016/j.isci.2025.113032) | Texte intégral, RSA intersujets, puissance spectrale, sommeil, disponibilité | Une similarité par condition n'est pas un classifieur instantané de rêve. Le lien avec un rapport ne date pas le contenu à la seconde près |
| [Haar Horowitz et al., Frontiers in Sleep, 2026](https://doi.org/10.3389/frsle.2026.1812535) | Effectifs et premier REM distingués du cumul ; rappels de consigne ; limites du classement du sommeil | Pas de contrôle ; les épisodes ultérieurs peuvent suivre de nouvelles consignes. Les rapports répétés ne sont pas indépendants |

Les textes ouverts de Salfi, Kumral et Haar Horowitz ont également été lus via le service public NCBI BioC lorsque la page PMC affichait une vérification de navigateur. Les relevés numériques utilisés sont dans `releves.json` ; ce fichier n'est pas une reproduction des données individuelles des articles.

## Données effectivement repérées

Les métadonnées d'accès retenues sont conservées dans `disponibilite.json`. Les empreintes annoncées par les dépôts ne sont pas présentées comme des empreintes recalculées sur des archives téléchargées.

- **Kumral.** L'[API FreiData](https://freidata.uni-freiburg.de/api/records/31mg4-mfq53) répond et annonce une archive `Kumral et al., 2023.zip`, de 46 588 397 863 octets. L'année du nom d'archive n'est pas l'année de publication de l'article. Le contenu brut n'a pas été téléchargé ni validé. L'article indique que le segment partagé s'arrête environ 30–60 secondes avant le réveil : un futur test ne doit pas inventer cette période manquante.
- **Code Kumral.** L'[API OSF](https://api.osf.io/v2/nodes/2bkus/files/osfstorage/) répond. Le dossier `code` contient notamment `LOSS1_pipeline_PSD_preprocess_run.m`, `LOSS2_implement_statistics.m`, `sleep_time.m`, `functions`, `visualization` et un README. Liste et README lus ; scripts non exécutés. L'appariement entre condition de livre, identifiant EEG et rapport reste à vérifier dans l'archive.
- **Brain2Qwerty v1.** L'[API Hugging Face](https://huggingface.co/api/datasets/bcbl190626/SpanishBCBL/tree/main) répond. La fiche annonce environ 262 Go : pas de téléchargement intégral sur le Mac. Les données brutes n'ont pas été relues. La présence d'EEG et de MEG dans un dépôt ne prouve pas leur simultanéité.
- **MNE Sample.** La [documentation officielle](https://mne.tools/stable/documentation/datasets.html#sample) décrit EEG et MEG simultanés, pour une tâche éveillée auditive/visuelle. Elle réserve explicitement ce jeu à l'apprentissage du logiciel et exclut son usage pour évaluer les performances du matériel. Utile pour vérifier une chaîne d'alignement, pas pour démontrer un transfert de contenu onirique.

## Institutions : compétence, disponibilité et partenariat sont distincts

La [plateforme NeuroSpin](https://www.cea.fr/drf/joliot/Pages/Plateformes_et_infrastructures/plateformes_imagerie/plateforme-neurospin.aspx) décrit sa MEG et ses EEG. [Clinatec](https://www.cea.fr/cea-tech/leti/Pages/recherche-appliquee/infrastructures-de-recherche/plateforme-CLINATEC.aspx) mentionne la MEG. Le [portrait Inserm de Delphine Oudiette](https://www.inserm.fr/actualite/portrait/comprendre-et-controler-lendormissement-le-reve-de-delphine-oudiette/) documente son champ scientifique. Aucun contact, accès à une machine ni partenariat Aeternam n'est établi.

La [fiche CEA-Leti ID 361](https://www.cea.fr/cea-tech/leti/english/Lists/Postdocs/StructuredDisplayForm.aspx?ID=361) présente une date de page de 2026 mais une prise de poste au 1er janvier 2020. Elle ne suffit pas à attester une offre actuellement ouverte. La [présentation CEA du 25 novembre 2021](https://www.cea.fr/cea-tech/leti/english/Pages/What%27s-On/News/magnetoencephalography-towards-high-resolution-at-room-temperature.aspx) distingue capteurs à hélium réellement à température ambiante et capteurs alcalins chauffés ; les jalons futurs qu'elle annonce ne sont pas des réalisations vérifiées.

## Calculs de méthode

`analyse.py` utilise seulement la bibliothèque standard. Il recalcule les dénominateurs du pilote et quatre expériences de pensée exactes :

1. **Information disponible.** Deux bits indépendants définissent quatre états. Le professeur observe les deux, l'élève un seul. La meilleure exactitude possible est obtenue à la fois par somme des maxima de probabilités jointes et par énumération de tous les classifieurs déterministes. Le cas bruité inverse le bit visible avec une probabilité hypothétique de 0,2. Ce sont des canaux abstraits ; aucun plafond réel de l'EEG n'en découle.
2. **Mauvaise cible.** Toutes les paires d'un son et d'un contenu indépendants sont énumérées. Identifier le son ne démontre aucun accès au contenu.
3. **Événement rare.** La valeur prédictive positive est calculée par Bayes avec prévalence, sensibilité et spécificité choisies pour l'exemple, sans estimation sur une population.
4. **Détection.** Queue binomiale exacte unilatérale, probabilité nulle 0,25, alternative hypothétique 0,4, seuil 0,05. Le seuil de rejet respecte le caractère discret du test. La puissance n'est valable que sous indépendance, équilibre des classes, test fixé et comparaison unique. Elle ne détermine pas un effectif humain : le regroupement par personne, les nuits, les absences de rappel et la multiplicité exigent un modèle séparé.

Ces démonstrations sont des résultats mathématiques d'Aeternam. Elles n'établissent ni faisabilité d'un casque, ni lecture du rêve, ni effet de stimulation. Les champs correspondants restent `null`.
