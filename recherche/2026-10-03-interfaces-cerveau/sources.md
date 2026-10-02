# BCI, vision et mémoire

Recherche vérifiée le 3 octobre 2026. Cette revue sélective distingue résultats humains, animaux, modèles et hypothèses. Elle ne constitue pas un recensement exhaustif ni un protocole clinique. Aucun participant, dispositif ou partenariat Aeternam n'est revendiqué.

## Sources primaires retenues

| Source | Preuve utilisée | Portée conservée |
| --- | --- | --- |
| [Willett et al., Nature, 2023](https://doi.org/10.1038/s41586-023-06377-x) | Décodage de parole tentée par une personne paralysée | Tâche volontaire et entraînée ; pas lecture de toute pensée |
| [Littlejohn et al., Nature Neuroscience, 2025](https://doi.org/10.1038/s41593-025-01905-6) | Synthèse vocale continue à partir d'une interface implantée | Traitement par incréments temporels ; ni EEG grand public ni lecture de rêve |
| [Beauchamp et al., Cell, 2020](https://doi.org/10.1016/j.cell.2020.04.033) | Reconnaissance de formes grâce à une stimulation corticale organisée dans le temps | Perceptions simples dans un protocole ; pas d'image arbitraire réaliste |
| [PRIMAvera, NEJM, 2025](https://doi.org/10.1056/NEJMoa2501396) | Résumé primaire : critères, plan, 38 implantations, 32 suivis, 26 réponses, événements graves | Implant rétinien pour atrophie géographique, pas implant cortical ni superposition visuelle chez une personne voyante |
| [Contrôle de l'activité évoquée dans le cortex visuel, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12632539/) | Texte intégral lu via NCBI BioC : modèle de réponse et contrôle chez un participant aveugle implanté | Amélioration du contrôle de l'activité et de certains percepts ; pas restitution d'une scène complexe |
| [Hampson et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6576290/) | Étude humaine de facilitation de l'encodage et du rappel | Informations réellement présentées dans une tâche ; pas biographie nouvelle |
| [Roeder et al., Frontiers in Computational Neuroscience, 2024](https://doi.org/10.3389/fncom.2024.1263311) | Texte intégral : reconnaissance d'images, effets dépendant des personnes et catégories | Améliorations et dégradations ; les pourcentages de combinaisons personne/catégorie ne sont pas des pourcentages de souvenirs écrits |
| [Ramirez et al., Science, 2013](https://doi.org/10.1126/science.1239073) | Résumé primaire : association artificielle de contexte chez la souris | Résultat animal limité ; aucune équivalence avec un épisode autobiographique humain complexe |
| [UNESCO, recommandation sur l'éthique des neurotechnologies](https://www.unesco.org/en/node/86248) et [présentation des principes](https://www.unesco.org/en/articles/ethics-neurotechnology-unesco-adopts-first-global-standard-cutting-edge-technology) | Cadre adopté en 2025, consentement et intégrité mentale | Cadre normatif ; pas assimilation à une loi pénale nationale |
| [MOABB](https://moabb.neurotechx.com/docs/paper_results.html) | Méthode officielle de comparaison reproductible de BCI EEG | Les tâches, sessions, personnes et licences doivent rester identifiées |
| [pulse2percept](https://pulse2percept.readthedocs.io/en/stable/) et [FAQ sur la portée des percepts simulés](https://pulse2percept.readthedocs.io/en/stable/users/faq.html) | Documentation officielle : modèles de prothèses visuelles et variabilité | Une simulation est conditionnelle au modèle ; elle n'est pas l'expérience exacte d'un patient |

## Calculs et limites

Le script ne contient aucune méthode de stimulation et aucun modèle d'implantation de souvenirs. Il réalise deux vérifications :

- PRIMA : 26/32 parmi les personnes suivies. Sur 38 implantations, l'issue des six personnes non évaluées produit des bornes arithmétiques 26/38 et 32/38. Elles ne sont ni un intervalle de confiance ni le résultat de l'imputation multiple publiée. L'article rapporte séparément une estimation imputée de 80 %. Aucun effet comparatif contre un groupe randomisé n'est calculé.
- Durée : vingt années, avec la convention explicite 365,25 jours par an, divisées par une heure ou huit heures. Ces rapports définissent l'hypothèse d'un vécu continu ; ils ne mesurent pas le cerveau et ne s'appliquent pas à un simple récit rétrospectif.

## Contributions proposées, pas encore exécutées

1. **Vision artificielle, priorité exploratoire.** Reproduire un modèle publié dans pulse2percept ; comparer plusieurs représentations de scènes sur des scènes et paramètres individuels réservés. Livrer reproductibilité, sensibilité aux hypothèses, échecs et critères fonctionnels. Aucun réglage destiné à une personne ni commande de matériel.
2. **Décodage EEG.** Reproduire une référence MOABB sur un jeu circonscrit ; distinguer évaluation au sein d'une session, entre sessions et entre personnes ; conserver le regroupement des observations. Mesurer incertitude, mémoire et temps de calcul. Une amélioration doit se maintenir hors du jeu qui a servi à choisir la méthode.
3. **Rêve et contenu.** Vérifier les annotations disponibles puis reproduire un résultat des livres audio, décrit dans l'étude MEG/EEG. Le dépôt ouvert est repéré ; les 46,6 Go de signaux n'ont pas été téléchargés et le résultat n'a pas été reproduit ici.

La création de souffrance punitive ou de souvenirs imposés n'est pas un objectif expérimental de ce programme. L'exemple de vingt ans de prison est étudié comme distinction conceptuelle entre souvenir, croyance rétrospective et expérience consciente, avec les problèmes de consentement qu'impliquerait une intervention imposée.
