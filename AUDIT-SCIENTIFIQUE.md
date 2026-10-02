# Audit scientifique d’Aeternam — 29 septembre 2026

## Complément du 3 octobre 2026 : BCI, MEG et mémoire

Deux études sont ajoutées, sans nouvelle acquisition humaine. Les références du texte transmis ont été vérifiées ; la recherche a été étendue à la vision artificielle et aux interventions sur la mémoire.

- Brain2Qwerty mesure une tâche de frappe. La v2 reste non causale à l’échelle de la phrase selon sa propre discussion. Une sortie fluide n’établit pas une lecture fidèle d’un rêve.
- La similarité EEG entre conditions de livres audio n’est pas un décodage instantané du contenu individuel. Les données partagées s’arrêtent avant le réveil ; les intervalles absents ne doivent pas être reconstruits comme observations.
- Le cumul d’incorporation REM du pilote inclut des épisodes ultérieurs et des rappels de consigne. Les dénominateurs et l’absence de contrôle sont conservés.
- Un composant optique miniaturisé n’est pas un système MEG complet ; une salle moins blindée n’est pas une chambre ordinaire. Le prix de marché à 830 000 euros n’a pas été corroboré ; la fiche CEA citée possède un début de poste en 2020 malgré sa date de page récente.
- PRIMA est une intervention rétinienne dans une indication clinique. Les événements graves, les suivis manquants et le plan non randomisé sont conservés. Les bornes arithmétiques sur les résultats manquants ne sont pas des intervalles de confiance.
- Les travaux de mémoire humaine portent sur des informations présentées, ceux de faux souvenirs chez la souris sur des associations expérimentales. Aucune étude retenue ne démontre une autobiographie arbitraire injectée ou une vie consciente accélérée.

Les calculs exacts nouveaux et leurs autotests sont dans `recherche/2026-10-03-meg-eeg-reves/` et `recherche/2026-10-03-interfaces-cerveau/`. Les benchmarks de décodage, les simulations de prothèse visuelle et les réanalyses de signaux bruts sont proposés, pas exécutés. Le complément ne réaudite pas les autres analyses du dépôt.

## Conclusion

Le projet possède un point de départ scientifique : des expériences de rêve peuvent être interrogées, certains contenus peuvent être influencés, et des données ouvertes permettent de commencer à mesurer les phénomènes. Le dépôt ne démontre pas une vie accélérée. Il contenait plusieurs conclusions plus larges que les mesures ; celles identifiées ci-dessous sont corrigées dans les scripts, les résultats et les pages publiques.

La théorie de la simulation reste une recherche fondamentale distincte. Le programme du rêve n’a pas besoin que cette hypothèse soit vraie.

## Corrections apportées

| Analyse | Problème | Correction |
| --- | --- | --- |
| Temps du rêve | Tâches, choix forcé et déclarations traités comme un même paramètre ; méta-analyse donnant 0,84 et borne 0,92 | Agrégation retirée ; champs globaux null ; mesures séparées |
| Choix forcé 5/15 minutes | Échelle ressentie confondue avec critère de décision arbitraire | Invariance par multiplication simultanée du critère et du facteur démontrée et testée |
| DREAM | Non-détection dans un intervalle inter-réveils interprétée comme borne de fréquence d’accélération | Borne retirée ; contre-exemple de non-détection ; regroupement par personne |
| Interventions | Absence d’intervalle remplacée par le point 1 ; borne générale 1,09 | Incertitude conservée ; aucune conversion du score d’une tâche en vitesse de conscience |
| Jones | Erreur type de la moyenne de pourcentages inférée du F d’un autre contraste | Intervalle retiré ; gains descriptifs conservés |
| Stetson | Ratios avec dénominateur incertain et nature des ± non clarifiée | Ratios descriptifs seulement ; pas de borne inférée |
| Une vie en une nuit | Rejeu neuronal et vécu conscient sur une même échelle ; « instants par seconde » déduits de fenêtres perceptives | Graphique, écarts et faux comptage d’instants retirés |
| Sommeil paradoxal | Produit de médianes présenté comme durée médiane observée | Renommé scénario arithmétique |
| Huit sources gamma | Multiplicité réduite après optimisation aux trois contraintes actives | Bonferroni sur les huit sources : au moins 60 % sous les hypothèses nominales, pas 85 % |
| Probabilité cosmique | Scénario arbitraire à environ 7 % présenté comme choix neutre d’Aeternam | Scénarios de sensibilité ; aucune probabilité empirique publiée |
| Ciel complet | Approximation normale et balayage fini présentés comme borne uniforme exacte | Portée explicitée dans résultats et article |
| Rendu à la demande | Significativités de figures numérisées additionnées en supposant indépendance et erreurs complètes | Diagnostics conditionnels conservés ; significativité combinée non retenue comme niveau de preuve validé |

Les anciennes versions restent dans Git. Les relevés documentaires historiques portent une notice de correction ; ils ne sont plus la source du verdict actuel.

## Programme nouveau, réellement exécuté

Le dossier `recherche/2026-09-29-programme-calcul/` contient le script, les résultats et les méthodes.

- Jointure de 287 réveils de 39 sujets dans la série Tononi de DREAM, empreinte de l’archive contrôlée.
- 124 déclarations de durée et 163 absences conservées comme manquantes ; 42 déclarations dans les classes d’au moins une minute.
- Proportion parmi les déclarations : 33,87 %. Moyenne des proportions par personne : 33,44 %, bootstrap par sujet à 95 % de 22,56 à 44,76 %. Fréquences de déclarations, pas vitesses de conscience.
- Comparaison exploratoire de réponses de perception : 20 sujets comparables, différence −20,17 points, intervalle −46,67 à +6,33 points ; pas de conclusion d’association stable.
- Intervalles reconstruits des différences de durée des trois tâches lucides ; pas de regroupement des tâches.
- Recalcul des dénominateurs des résultats de communication et d’incubation, y compris le pilote REM publié en juin 2026.
- Neuf configurations numériques, 6 000 jeux chacune. Dans l’exemple de 40 personnes, trois mesures et corrélation 0,6, le nul donne 9,68 % de rejets avec l’analyse naïve et 2,73 % avec l’analyse par personne, pour un seuil unilatéral de 2,5 %.

Ces simulations vérifient une méthode. Elles ne sont ni des expériences humaines ni une prédiction d’efficacité. Les paramètres de puissance sont choisis et documentés.

## Étendue de la validation

Cet audit combine inspection du code, vérification des unités et des inférences, consultation de publications primaires, recalcul des scripts modifiés et contrôles numériques indépendants. Il ne constitue pas une revue externe par des chercheurs ni une nouvelle analyse des événements bruts des collaborations de physique.

Les scripts de dispersion directionnelle, synthèse, rêve, interventions, projet et programme ont été rejoués. Les scripts du ciel complet et des interférences sont également rejoués pour conserver une provenance cohérente après modification de leur portée. Les détails d’exécution et l’état de publication doivent être vérifiés dans le commit et le workflow associés, pas inférés de ce texte.

Les valeurs individuelles des figures d’interférence restent des numérisations ; leurs covariances et erreurs systématiques n’ont pas été reconstruites. La recherche de maximum continu des orientations n’a pas été certifiée mathématiquement. Les études de lucidité à domicile et d’incubation dont les données sont sur demande n’ont pas été réanalysées individuellement.

Pour les autres tests anciens : les résultats numériques sont conservés, avec portée clarifiée dans la synthèse. Leur conservation n’équivaut pas à une validation exhaustive de chaque source, chaque choix postérieur à l’observation et chaque modèle instrumental.

## Ce qui ferait progresser le projet

L’objet le plus utile maintenant est une série ouverte liant, pour la même personne, des événements horodatés pendant le rêve et un contenu ou un rappel après réveil. Elle permettrait de travailler la continuité et de distinguer performance pendant le rêve, durée ressentie et mémoire.

La littérature sur le rejeu neuronal n’autorise pas à multiplier des années vécues par une vitesse de réactivation. Le facteur 87 660 reste une définition arithmétique de l’objectif littéral. Une histoire condensée peut faire l’objet d’un autre test, mais ne prouve pas ce facteur.

Le résultat stratégique de l’audit est donc un programme précis de calcul, avec unités, données et conditions de réfutation. Il remplace l’addition d’analogies par des questions que les données peuvent effectivement examiner.
