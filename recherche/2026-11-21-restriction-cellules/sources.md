# Sources de l'analyse « Ce que la restriction change dans les cellules du sang »

Relevés le 21 novembre 2026. Le plan (`plan.md`) a été enregistré dans Git (commit `bcf792f`)
avant tout calcul liant une mesure à la survie ; `analyse.py` l'applique, `verifier.py` refait
les tests avec d'autres logiciels (statsmodels, scipy ; hors déploiement).

## Les données

Di Francesco A, Deighan AG, Litichevskiy L, et al., « Dietary restriction impacts health and
lifespan of genetically diverse mice », *Nature* 2024;634:684-692,
doi:10.1038/s41586-024-08026-3 (texte intégral PMC11485257). Voir
`../2026-11-21-piste-restriction/sources.md` pour le plan de l'étude et les relevés.

Fichier : `data/phenotyping_data.csv` du dépôt https://github.com/calico/DRiDO_Paper_Release
(licence MIT, Calico, 2024 ; commit 28f84d361bb87843bcec1a0d7a3d38dcda70325b), copié tel quel
dans `donnees/` (empreinte SHA-256 23c2089128ab6a514bd1bf12fa1898d3a38900c162a2eed599e08f1ad1d7bde1,
vérifiée à chaque exécution). 937 souris, 675 colonnes. Les âges de chaque série de mesures
sont lus dans les colonnes `*_AgeInDays` du fichier : numération sanguine (`CBC`) vers 343 et
707 jours, cytométrie (`FLOW`) vers 155 (avant les régimes), 490 et 853 jours.

## Ce qui s'écarte du plan

1. **Le témoin négatif n'est pas passé.** Sur les 109 mesures prises avant le début des
   régimes, le test 1 trouve 21 % de p < 0,05 et 10 découvertes après correction, au lieu
   d'environ 5 % et d'aucune. Les souris promises à la restriction différaient donc déjà un peu
   avant de la commencer (poids à 3 mois : z = 2,6 ; activité en cage métabolique ; quelques
   cellules immunitaires), et les mesures d'une même série sont liées entre elles. Les p du
   test 1 sont trop optimistes. Correction ajoutée après coup, comme l'étude du 20 novembre
   l'avait fait pour son seuil : les z du test 1 sont divisés par la racine du facteur
   d'inflation mesuré sur ce témoin (médiane de z² rapportée à 0,4549, soit 3,15). Après cette
   correction, 25 des 27 candidates restent candidates. Deux contrôles supplémentaires, eux aussi
   ajoutés après coup : le test 1 refait avec le poids à 3 mois, et, pour la cytométrie, avec la
   même mesure prise à 155 jours, avant les régimes. Les effets de la restriction tiennent.
2. **Les générations absentes.** Quelques mesures n'ont été prises que dans certaines
   générations ; une génération sans souris mesurée n'a pas d'indicatrice (sans quoi le calcul
   est impossible). Cela ne change rien d'autre.
3. **Le score sanguin.** En plus de la pente avec les candidates en covariables (prévue), la
   même pente avec un seul score qui les résume (prédicteur linéaire d'un modèle de Cox), pour
   vérifier que le résultat ne vient pas du nombre de covariables. Même conclusion.
4. **La taille d'une expérience sur le rythme.** Ajoutée : le nombre de souris mesurées deux
   fois qu'il faudrait pour voir, avec 90 % de chances, un effet de la taille de celui observé
   sur la variation des cellules T.

## Les travaux cités dans l'article

- Lymphocytes B associés à l'âge : Hao Y, O'Neill P, Naradikian MS, Scholz JL, Cancro MP,
  « A B-cell subset uniquely responsive to innate stimuli accumulates in aged mice », *Blood*
  2011;118:1294, doi:10.1182/blood-2011-01-330530 (résumé : « We have discovered a distinct
  mature B-cell subset that accumulates with age, which we have termed age-associated B
  cells. »). Revue : Ma S, Wang C, Mao X, Hao Y, « B Cell Dysfunction Associated With Aging and
  Autoimmune Diseases », *Frontiers in Immunology* 2019;10:318, doi:10.3389/fimmu.2019.00318 :
  parmi les marqueurs décrits pour ces cellules chez la souris, CD11c et CD11b ; la revue
  rapporte aussi le basculement, avec l'âge, des cellules souches du sang vers les cellules
  myéloïdes. Notre cytométrie ne mesure que CD11b sur les lymphocytes B : nous écrivons qu'ils
  « ressemblent » à ces cellules, pas qu'ils le sont.
- Cellules T naïves (CD62L+ CD44−) et effectrices-mémoire (CD62L− CD44+) : définitions
  d'usage chez la souris. Leur évolution avec l'âge est mesurée ici, chez les souris nourries à
  volonté, entre 490 et 853 jours.

## Ce qui n'est pas dans ce dossier

Aucune expérience menée par ÆTERNAM. Une association à régime égal n'est pas une cause. Les
simulations du contrôle du moteur de Cox ne sont pas des mesures.
