# Sources de la piste « Restriction : ralentir le vieillissement, de la souris à l'humain »

Relevés le 21 novembre 2026. Les citations entre guillemets ont été lues dans leur langue, à
l'endroit indiqué ; le reste est rapporté. Les calculs sont dans `analyse.py`, la
contre-vérification indépendante dans `verifier.py` (scipy, hors déploiement).

## Les données des souris

Di Francesco A, Deighan AG, Litichevskiy L, et al., « Dietary restriction impacts health and
lifespan of genetically diverse mice », *Nature* 2024;634:684-692,
doi:10.1038/s41586-024-08026-3 (texte intégral PMC11485257).

- Le plan, dans le résumé : « Here we performed an extensive assessment of graded levels of
  caloric restriction (20% and 40%) and intermittent fasting (1 and 2 days fasting per week) on
  the health and survival of 960 genetically diverse female mice. »
- Début des régimes (Méthodes) : « Feeding schedules for DR were started at 6 months of age. »
  937 souris étaient vivantes à 6 mois ; 13 ont été censurées (blessures sans lien avec une mort
  imminente) : nos données comptent les mêmes 937 souris et les mêmes 13 censures.
- Contrôle de lecture (Résultats) : « 40% CR mice achieved a median lifespan of around 9 months
  (36.3%) greater than mice in the AL group. » Nous trouvons 36,34 % (`analyse.py`).
- Le résultat des auteurs sur la pente, que nous retrouvons avec notre propre modèle : ils
  rapportent une baisse significative du rythme du vieillissement (« rate of ageing ») chez les
  souris restreintes, et non chez les souris à jeun intermittent, comparées aux souris nourries
  à volonté (Résultats ; temps de doublement estimés par un modèle de Gompertz, figure 1d).
- Le coût, dans le résumé : « 40% caloric restriction had the strongest lifespan extension
  effect but led to a loss of lean mass and changes in the immune repertoire that could confer
  susceptibility to infections. »

Fichier : `data/phenotyping_data.csv` du dépôt https://github.com/calico/DRiDO_Paper_Release
(licence MIT, Calico, 2024 ; commit 28f84d361bb87843bcec1a0d7a3d38dcda70325b, empreinte SHA-256
du fichier d'origine 23c2089128ab6a514bd1bf12fa1898d3a38900c162a2eed599e08f1ad1d7bde1).
`donnees/drido-survie.csv` en garde quatre colonnes, sans l'identifiant des souris :
génération, régime (AL, 1D, 2D, 20, 40), mort (1) ou censurée (0), âge en jours (colonnes
`Generation`, `Diet`, `Died`, `SurvDays`). Aucune valeur n'est modifiée.

## Les traitements de l'ITP, refaits avec la fragilité

Les 27 comparaisons retenues par l'étude du 20 novembre (`../2026-11-20-retarder-ou-ralentir/`),
mêmes données (Interventions Testing Program, Mouse Phenome Database, MPD:508). Notre moteur
redonne leur λ à 0,01 % près avant d'ajouter la fragilité.

## Les travaux qui allaient déjà dans ce sens

Résumés PubMed lus le 20 novembre 2026 (voir `../2026-11-20-retarder-ou-ralentir/sources.md`).

- Simons MJP, Koch W, Verhulst S, *Aging Cell* 2013;12:410-4, doi:10.1111/acel.12061 :
  « We find that DR reduced aging rate without affecting vulnerability. »
- Garratt M, Nakagawa S, Simons MJP, *Aging Cell* 2016;15:737-43, doi:10.1111/acel.12489 :
  « life extension in mice and yeast occurs largely by pushing back the onset of aging, but not
  altering the shape of the mortality curve once aging starts ».

## Le primate

- Mattison JA et al., « Caloric restriction improves health and survival of rhesus monkeys »,
  *Nature Communications* 2017;8:14063, doi:10.1038/ncomms14063 (PMC5247583). Dans le résumé :
  « The University of Wisconsin study reported a significant positive impact of CR on survival,
  but the National Institute on Aging study detected no significant survival effect. »
  L'article compare les deux études et conclut que la restriction modérée améliore la santé et
  la survie du macaque. Nous n'avons pas les données individuelles : aucune pente n'est calculée.

## L'humain

Waziry R, Ryan CP, Corcoran DL, et al., « Effect of long-term caloric restriction on DNA
methylation measures of biological aging in healthy adults from the CALERIE trial »,
*Nature Aging* 2023;3:248-257, doi:10.1038/s43587-022-00357-y (texte intégral PMC10148951).

- Essai randomisé : 220 adultes sans obésité, 25 % de restriction prescrite ou régime libre,
  deux ans ; hommes de 21 à 50 ans, femmes non ménopausées de 21 à 47 ans.
- Restriction réellement obtenue : « most participants achieving doses below the prescribed 25%
  (mean = 11.9, s.e.m. = 0.7%) ».
- Mesures : « for n = 197 participants (128 CR and 69 AL) ».
- Effet en intention de traiter sur DunedinPACE : « 12-month d = −0.29 (95% confidence interval
  −0.45, −0.13), 24-month d = −0.25 (95% CI −0.41, −0.09) ».
- Traduction des auteurs : « Standardized treatment effects on DunedinPACE correspond to a
  reduction in the pace of aging of 2–3%. »
- Pour 20 % de restriction (analyse par variable instrumentale) : « the effect of 20% CR on
  DunedinPACE was d = −0.43 (95% CI −0.67, −0.19) at 12 months and d = −0.40 (95% CI −0.67,
  −0.12) at 24 months ».
- Lien avec la mortalité, extrapolé par les auteurs d'études d'observation (pas mesuré dans
  l'essai) : « the CALERIE treatment effect of 2–3% slower pace of aging corresponds to a
  reduction in mortality risk of as much as 10–15% ».
- Ce que mesure DunedinPACE (tableau 2) : « Pace of aging was measured from within-person
  change over time in 19 blood chemistry and organ function test metrics of system integrity »,
  puis résumé par la méthylation de l'ADN du sang.
- Les auteurs notent que les autres horloges (PhenoAge, GrimAge) n'ont pas bougé.

La table de mortalité humaine est celle de `../2026-11-20-immortalite/` (Social Security
Administration, 2023, domaine public).

## Restriction et rapamycine ensemble

- Unnikrishnan A, Kurup K, Salmon AB, Richardson A, « Is Rapamycin a Dietary Restriction
  Mimetic? », *J Gerontol A* 2020;75:4-13, doi:10.1093/gerona/glz060 (PMC6909904). Les auteurs
  prédisent que la combinaison fera mieux que chacune seule, et notent que très peu d'études
  l'ont évaluée ; la seule durée de vie combinée qu'ils citent est chez la drosophile.
- Ham DJ et al., *Nature Communications* 2022, doi:10.1038/s41467-022-29714-6 : effets
  distincts et additifs de la restriction et de la rapamycine sur le muscle de souris âgées
  (titre : « Distinct and additive effects of calorie restriction and rapamycin in aging
  skeletal muscle »). Pas de durée de vie.
- Nous n'avons pas trouvé de durée de vie de souris publiée qui croise les deux dans les mêmes
  animaux. Ce n'est pas une preuve qu'il n'en existe aucune : à revérifier avant tout financement.

## Ce qui n'est pas dans ce dossier

Aucune expérience menée par ÆTERNAM, aucune donnée humaine individuelle. Les conversions vers
l'humain sont des calculs sur des hypothèses écrites dans `analyse.py`, pas des prévisions. Les
simulations servent à contrôler le calcul et à dimensionner les expériences : ce ne sont pas des
mesures.
