# Einstein, Hawking et les limites de nos descriptions

Revue ciblée vérifiée le 8 octobre 2026. Trois études : relativité restreinte ;
horloges, Terre et trous noirs ; travaux de Hawking et questions ouvertes.
Ce travail est une revue critique avec calculs pédagogiques, sans mesure nouvelle,
sans réanalyse des signaux des expériences citées et sans prétention d'exhaustivité.

## Sources et usage

| Référence primaire | Usage et portée |
| --- | --- |
| A. Einstein (1905), [Zur Elektrodynamik bewegter Körper](https://doi.org/10.1002/andp.19053221004), Annalen der Physik 322, 891–921 | Relativité restreinte et transformation entre référentiels. Notice originale vérifiée. |
| A. Einstein (1916), [Die Grundlage der allgemeinen Relativitätstheorie](https://doi.org/10.1002/andp.19163540702), Annalen der Physik 354, 769–822 | Exposé de la relativité générale, après la formulation de 1915. |
| C. W. Chou et al. (2010), [Optical Clocks and Relativity](https://doi.org/10.1126/science.1192720), Science 329, 1630–1633 ; [texte NIST](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=905055) | Comparaisons d'horloges, mouvement et altitude. Le papier est dans Science ; une notice NIST l'étiquette à tort Nature. |
| T. Bothwell et al. (2022), [Resolving the gravitational redshift in a millimetre-scale atomic sample](https://doi.org/10.1038/s41586-021-04349-7) ; [compte rendu JILA/NIST](https://www.nist.gov/news-events/news/2022/02/jila-atomic-clocks-measure-einsteins-general-relativity-millimeter-scale) | Mesure du gradient de fréquence dans un échantillon atomique. Ce n'est pas une expérience avec une personne au centre terrestre. |
| U. I. Uggerhøj, R. E. Mikkelsen, J. Faye (2016), [The young centre of the Earth](https://arxiv.org/abs/1604.05507), European Journal of Physics 37, 035602 | Équations 3, 7, 12 et discussion : sphère homogène et valeur PREM publiée de 2,49 ans pour 4,54 milliards d'années. Le profil PREM n'est pas recalculé ici. |
| GRAVITY Collaboration (2018), [Detection of the gravitational redshift in the orbit of the star S2](https://arxiv.org/abs/1807.09409), A&A 615, L15 | Signal combinant décalage gravitationnel et Doppler transverse. Pas une horloge immobile à l'horizon. |
| LIGO/Virgo (2016), [Observation of Gravitational Waves from a Binary Black Hole Merger](https://arxiv.org/abs/1602.03837), PRL 116, 061102 | Signal GW150914 détecté en 2015, publié en 2016 ; test de la dynamique de coalescence. |
| S. W. Hawking, R. Penrose (1970), [The singularities of gravitational collapse and cosmology](https://doi.org/10.1098/rspa.1970.0021), Proc. R. Soc. A 314, 529–548 | Théorème conditionnel d'incomplétude, et non observation d'une densité infinie. |
| S. W. Hawking (1975), [Particle creation by black holes](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-43/issue-3/Particle-creation-by-black-holes/cmp/1103899181.pdf), CMP 43, 199–220 | Calcul de création de particules sur géométrie classique ; horizon, température et limites de l'approximation. |
| LIGO/Virgo/KAGRA (2025), [GW250114: testing Hawking's area law and the Kerr nature of black holes](https://arxiv.org/abs/2509.08054), PRL 135, 111403 | Données compatibles avec augmentation de l'aire totale dans une fusion. Test conditionné par les modèles d'analyse ; pas détection du rayonnement de Hawking. |
| A. Almheiri et al. (2020), [Replica Wormholes and the Entropy of Hawking Radiation](https://arxiv.org/abs/1911.12333), JHEP 05, 013 | Résultat théorique notamment en gravité JT bidimensionnelle. |
| A. Almheiri et al. (2021), [The entropy of Hawking radiation](https://arxiv.org/abs/2006.06872), RMP 93, 035002 | Synthèse des progrès sur l'entropie fine, les îlots et la courbe de Page. |
| J. Steinhauer (2016), [Observation of quantum Hawking radiation and its entanglement in an analogue black hole](https://arxiv.org/abs/1510.00621), Nature Physics 12, 959 | Analogue dans un condensat ; distinction avec un horizon gravitationnel astrophysique. |
| E. E. Erkul, U. Leonhardt (2025), [Dispersion in Analogue Gravity](https://arxiv.org/abs/2510.02542), prépublication v2 | Contexte des analogues ; ses spéculations cosmologiques ne sont pas reprises comme résultats. |
| J. B. Hartle, S. W. Hawking (1983), [Wave function of the Universe](https://doi.org/10.1103/PhysRevD.28.2960), PRD 28, 2960 | Proposition d'état quantique cosmologique ; résumé original vérifié. |
| J. Maldacena (2024), [Comments on the no boundary wavefunction and slow roll inflation](https://arxiv.org/abs/2403.10510) | Difficultés de la proposition sans bord : hypothèses et confrontation cosmologique. |
| A. I. Abdalla et al. (2026), [Consistent Evaluation of the No-Boundary Proposal](https://arxiv.org/abs/2602.02682), prépublication | Discussion récente de la normalisation des probabilités. Ce n'est pas une confirmation observationnelle ni un consensus annoncé. |

## Constantes et conventions de calcul

- [NIST, CODATA 2022](https://physics.nist.gov/cuu/Constants/) :
  c = 299792458 m/s, h = 6,62607015 × 10⁻³⁴ J s et kB = 1,380649 × 10⁻²³ J/K sont exacts en SI.
  G = 6,67430 × 10⁻¹¹ m³ kg⁻¹ s⁻² est mesuré ; les chiffres du script ne suppriment pas son incertitude.
- [UAI, résolution B3 de 2015](https://www.iau.org/static/resolutions/IAU2015_English.pdf) :
  GM solaire nominal = 1,3271244 × 10²⁰ m³/s² ; terrestre = 3,986004 × 10¹⁴ m³/s².
  Ce sont des facteurs de conversion nominaux, pas des masses mesurées exactes.
- Rayon terrestre arrondi 6371 km et âge de référence 4,54 milliards d'années : Uggerhøj et al.
  Année de calcul = 365,25 jours ; g = 9,81 m/s² est une valeur locale illustrative.

## Ce qui a réellement été calculé

Transformation de Lorentz et addition colinéaire des vitesses ; durées propres
pour des trajets idéalisés ; écarts d'horloges sur de petites différences de hauteur ;
potentiel intérieur d'une Terre homogène ; conversion de la valeur PREM publiée
vers 80 ans ; rythmes statiques et orbitaux de Schwarzschild ; rayon, température,
entropie et ordre de grandeur d'évaporation d'un trou noir sans rotation.

Le coefficient 5120π du temps d'évaporation résulte d'un modèle de corps noir de
surface 4πr_s². Il ignore les facteurs de transmission, les espèces de particules,
l'accrétion et la phase quantique finale. Il n'est pas une durée astrophysique précise.

Les autotests comparent des formulations distinctes : différences dx/dt après
Lorentz, invariant d'intervalle, rapidités, intégration par coquilles, solution
intérieure exacte de densité constante et première loi thermodynamique.
Ils vérifient les calculs ; ils ne confirment pas expérimentalement les théories.

Le script accepte `--out` pour produire un résultat ailleurs sans modifier celui
versionné. Les figures sont générées à partir de ce résultat par `figures.py`.
