# Accueil « Du cosmos au cerveau » : sources des nouvelles étapes

Relevé du 18 octobre 2026. Les étapes « Le cerveau » et « Les frontières » de l'accueil (`ETAPES_CERVEAU` dans `site/langues/univers_fr.py`) reprennent des résultats déjà établis dans les articles du site, avec leurs sources. Deux sources sont nouvelles ; leur texte a été relu à la source le 18 octobre 2026.

## Sources nouvelles

- Azevedo F. A. C. et al. (2009), « Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain », *Journal of Comparative Neurology* 513(5), 532–541. https://doi.org/10.1002/cne.21974 (PMID 19226510).
  - Résumé : « the adult male human brain contains on average 86.1 ± 8.1 billion NeuN-positive cells ("neurons") ».
  - Résumé : « only 19% of all neurons located in the cerebral cortex ».
  - Repris sur l'accueil : 86,1 milliards en moyenne, écart type 8,1 milliards, cerveaux d'hommes adultes ; 19 % dans le cortex cérébral. Le titre « 86 milliards de neurones » arrondit cette moyenne.
- NINDS, « Brain Basics: The Life and Death of a Neuron ». https://www.ninds.nih.gov/health-information/public-education/brain-basics/brain-basics-life-and-death-neuron
  - « They use electrical and chemical signals to send information ».
  - « A neuron has three basic parts: a cell body, an axon, and dendrites. »
  - « sending chemicals, called neurotransmitters, across a tiny space called a synapse ».

## Résultats repris des articles du site

| Étape | Résultat | Article | Source primaire |
| --- | --- | --- | --- |
| Vision | phosphène ; formes de lettres reconnues par stimulation séquentielle ; une électrode n'est pas un pixel | /interfaces-cerveau/#vision | Beauchamp et al., *Cell* 2020, https://doi.org/10.1016/j.cell.2020.04.033 |
| Vision | PRIMAvera : 38 implantés, 26 sur 32 évalués au critère à 12 mois, essai ouvert, 26 événements indésirables graves chez 19 participants | /interfaces-cerveau/#prima | Holz et al., *NEJM*, https://doi.org/10.1056/NEJMoa2501396 |
| Mémoire | association mnésique artificielle chez l'animal | /interfaces-cerveau/#memoire | Ramirez et al., *Science* 2013, https://doi.org/10.1126/science.1239073 |
| Mémoire | rétention d'informations : améliorations et dégradations selon les personnes | /interfaces-cerveau/#memoire | Hampson et al., *J Neural Eng* 2018 ; Roeder et al., *Front Comput Neurosci* 2024 |
| Rêve | 158 essais, 29 réponses correctes (18,4 % des essais ; 85,3 % des réponses interprétables) ; 78,5 % de silences ou réponses ambiguës | /programme/#acces | Konkoly et al., *Current Biology* 2021, https://doi.org/10.1016/j.cub.2021.01.026 |
| Rêve | durées de tâches en rêve lucide, pas une mesure du temps vécu | /temps-reve/#analyse | Erlacher et al., *Front Psychol* 2014, https://doi.org/10.3389/fpsyg.2013.01013 |
| Interfaces | parole décodée par implant, protocole précis | /interfaces-cerveau/#decodage | Willett et al., *Nature* 2023, https://doi.org/10.1038/s41586-023-06377-x |
| Interfaces | 29 % d'erreurs par caractère en MEG, 65 % en EEG | /meg-eeg-reves/#preuves | Lévy et al., *Nature Neuroscience* 2026, https://doi.org/10.1038/s41593-026-02303-2 |
| Interfaces | 55,3 % et 51,8 % d'exactitude équilibrée, référence 50 % | /bci-generalisation/#resultats | calcul du dépôt, `recherche/2026-10-03-bci-generalisation/` |
| Simulation | maille inférieure à 2,5 × 10⁻²⁷ m (grille cubique, temps continu, toutes orientations) | /test-1/ | LHAASO, arXiv:2402.06009v3, `recherche/2026-09-28-grille-lhaaso/` |
| Simulation | motif cubique fort exclu dans les directions des rayons cosmiques | /test-2/, /test-6/ | Pierre Auger, arXiv:2211.16020 |
| Simulation | générateur pseudo-aléatoire simple exclu, pas un générateur cryptographique | /test-4/ | Kavulich et al., arXiv:2101.01238 |

## Ce que les scènes ne sont pas

Les scènes 13 à 19 de `site/univers-scene.mjs` sont des schémas procéduraux. Le curseur « Électrodes » réduit une lettre à une grille de points selon le modèle naïf « une électrode, un point » ; l'étape rappelle que les expériences ne valident pas ce modèle. Le passage de la toile cosmique au réseau de neurones est une transition de mise en scène.
