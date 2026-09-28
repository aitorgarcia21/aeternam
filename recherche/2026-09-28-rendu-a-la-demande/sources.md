# Test n° 5 : sources

Chaque affirmation factuelle du test n° 5, avec sa source primaire. Les nombres
calculés viennent de `resultats.json` (produit par `analyse.py`). Les points de
mesure sont relevés par `extraire.py` dans les dessins vectoriels des PDF arXiv
(coordonnées exactes des marqueurs, étalonnées sur les graduations) et écrits dans
`donnees/figures.json` (SHA-256
`d0628f962815a717726a218f235e37d28e3bd4ea9918777553310d70d9fc649a`, vérifié par
`analyse.py`). Les PDF téléchargés sont contrôlés par leur SHA-256. Consulté le
28 septembre 2026. Les passages entre guillemets sont recopiés tels quels du PDF.

Statuts : **lu** = texte intégral lu ; **résumé seulement** = seul le résumé est
accessible (article payant) ; **cité** = contenu connu uniquement par la citation
qu'en fait une autre source lue.

## L'hypothèse testée

### 1. Bostrom, FAQ (2025) — lu

- N. Bostrom, « The Simulation Argument FAQ (2025) », version 2.0,
  https://simulation-argument.com/faq (page HTML, SHA-256 du fichier reçu
  `5067bc413b35196060368be298a57d5280e01125a43c1dd9e1553288482c1559`).
- Question 6 : « Many of the remaining details could be filled in only when
  somebody is looking at them or performing relevant experiments. Graphics
  engines typically render only that which is seen by some player character ».

### 2. Campbell, Owhadi, Sauvageau, Watkinson (2017) — lu

- T. Campbell, H. Owhadi, J. Sauvageau, D. Watkinson, « On testing the
  simulation theory », arXiv:1703.00058v2 (6 juin 2017),
  https://arxiv.org/abs/1703.00058 (PDF SHA-256
  `a5f9ded573676cbd10b8cd594eba217318bd00cf569ad5424250cbe0512ca753`).
- Résumé, p. 1 : un tel système « would, as in a video game, render content
  (reality) only at the moment that information becomes available for
  observation by a player and not at the moment of detection by a machine ».
- § 4, p. 5 : « our hypothesis is that wave or particle duality patterns are not
  determined at the moment of detection but by the existence and availability
  of the which-way data when the pattern is observed. »
- § 4.2, p. 8-9 (expérience proposée « Detecting but not making the data
  available to an observer ») : « the which-way data is detected but not
  recorded (which translates into the non availability of the which-way data to
  the experimenter/observer) » ; version à photons intriqués : « Simply removing
  the coincidence counter from the experimental setup and recording (only) the
  output of D0 (result screen). D0 should display the wave pattern if the
  experiment is successful. »
- § 4.2, p. 9 : « “availability of the which-way data” is implied by the
  which-way data being recorded on objective media ».
- C'est la prédiction que `analyse.py` appelle HR : tant que l'information de
  chemin n'est ni lue ni enregistrée, la figure d'interférence subsiste.

## Le cadre quantique

### 3. Englert (1996) — cité

- B.-G. Englert, « Fringe Visibility and Which-Way Information: An Inequality »,
  Phys. Rev. Lett. 77, 2154-2157 (1996), https://doi.org/10.1103/PhysRevLett.77.2154
  (titre, volume et pages vérifiés par l'API Crossref ; texte intégral payant,
  non lu : la page de l'éditeur renvoie 403).
- L'inégalité est prise dans la source n° 5, dont Englert est co-auteur :
  « The Duality Relation accessible to experimental test then becomes [5,9]:
  V 2 + K2 ≤1 . (1) The equality holds for pure initial states of the WWM,
  while the inequality applies to (partially-)mixed states. » (p. 1 ; [5] =
  Englert, PRL 77, 2154). La distinguabilité y est définie ainsi : « the optimal
  strategy maximizes K and identifies the Distinguishability D = max{K} ».
- `analyse.py` vérifie en outre D² + V² ≤ 1 numériquement (autotest) sur des
  états aléatoires chemin ⊗ marqueur, et l'égalité V = |⟨M1|M2⟩|, D² + V² = 1
  pour un marqueur pur.

### 4. Dürr, Nonn, Rempe (1998) — résumé seulement

- S. Dürr, T. Nonn, G. Rempe, « Origin of quantum-mechanical complementarity
  probed by a ‘which-way’ experiment in an atom interferometer », Nature 395,
  33-37 (1998), https://doi.org/10.1038/25653 (références vérifiées par Crossref).
- Résumé (page de l'éditeur) : « Here we report a which-way experiment in an atom
  interferometer in which the ‘back action’ of path detection on the atom's
  momentum is too small to explain the disappearance of the interference
  pattern. We attribute it instead to correlations between the which-way
  detector and the atomic motion, rather than to the uncertainty principle. »
- Aucun chiffre de cet article n'est utilisé : ni le texte de Nature ni
  l'article compagnon (Phys. Rev. Lett. 81, 5705, 1998, page de l'éditeur en
  403) n'ont pu être lus, et nous n'avons trouvé aucune version arXiv
  (recherche dans l'API arXiv, auteurs Dürr et Rempe). La source n° 5, p. 5,
  note [8], le décrit ainsi : « a recent atom-interferometry experiment
  investigated the equality of (1), with scaled results constant to within 10%,
  but achieving unscaled values of only ∼0.6 ».

## Les données analysées

### 5. Schwindt, Kwiat, Englert (1999) — lu, données de la fig. 2

- P. D. D. Schwindt, P. G. Kwiat, B.-G. Englert, « Quantitative wave-particle
  duality and non-erasing quantum erasure », Phys. Rev. A 60, 4285 (1999),
  https://doi.org/10.1103/PhysRevA.60.4285 ; version arXiv lue :
  quant-ph/9908072v1, https://arxiv.org/abs/quant-ph/9908072 (PDF SHA-256
  `9e6d5453ca61705d5484dc6b441ee9dc8a64e501029c61335b19e4d09ebf3d90`).
- Protocole, p. 2 : « For Visibility measurements the polarization analyzer was
  lowered out of the beam path » ; pour la connaissance K : « With the
  polarization analyzer in place, and path 2 blocked, the counts on the two
  detectors were measured. » La visibilité est donc mesurée sans que le
  marqueur de chemin soit lu ; la connaissance, en le lisant.
- p. 2 : « The measured values of V are slightly lower than the theoretical
  curve because the intrinsic visibility of the interferometer (even without
  the HWP) is only ∼98% » ; « V > 4.4% even though L > 99.9%! » ;
  « The average of all the data points in Fig. 2 gives 0.976 ± 0.017 » ;
  « for the minimum-visibility arrangement, V 2 + K2 = 0.998 ».
- Légende de la fig. 3, p. 3 : « A mixed state input from the filtered
  white-light source yielded an average value for V 2 + K2 of 0.003 ± 0.001;
  the theoretical prediction based on the measured input state is 0.017±0.003 ».
- Fig. 2, p. 3 : sept angles de la lame demi-onde (0° à 45° par 7,5°), V
  (croix), K dans la base optimale (losanges), K dans la base H/V (triangles),
  V² + K² (disques), avec barres d'erreur ; relevés par `extraire.py`. Contrôle :
  la moyenne des V² + K² relevés vaut 0,9757 (imprimé : 0,976), le point à 45°
  0,9984 (imprimé : 0,998), V à 45° 0,0447 (imprimé : « V > 4.4% »).

### 6. Walborn, Terra Cunha, Pádua, Monken (2002) — lu, données des fig. 2 à 9

- S. P. Walborn, M. O. Terra Cunha, S. Pádua, C. H. Monken, « Double-slit quantum
  eraser », Phys. Rev. A 65, 033818 (2002), https://doi.org/10.1103/PhysRevA.65.033818 ;
  version arXiv lue : quant-ph/0106078v1 (PDF SHA-256
  `33bb3bd7f17d8ad7fdb24c5ad2ad6e34e3dd8fd4a7bdb01468696061ee554ce5`).
- p. 1 : « the disappearance of the interference pattern is not dependent on
  such a measurement. The which-path marker’s presence alone is sufficient [...] » ;
  p. 2 : « it is enough that the which-path information is available to
  destroy interference ».
- p. 4, § IV : photons de 702,2 nm ; fentes « 200µm wide and separated by a
  distance of 200µm » ; fentes à 42 cm du cristal ; « Detectors Ds and Dp are
  located 125 cm and 98 cm from the BBO crystal » ; montage retardé : « detector
  Dp and POL1 were placed at a new distance of 2 meters ».
- p. 5 : « Figure 3 shows the absence of interference due to the quarter-wave
  plates. Nearly all interference present in figure 2 was destroyed. The
  residual interference present is due to a small error in aligning the
  quarter-wave plates. » ; « The averaged sum of these two interference patterns
  gives a pattern roughly equal to that of figure 3. » ; figures 6 à 9 : « The
  experimental results are comparable to the case in which photon p is detected
  before photon s. »
- Fig. 2 à 9 (p. 8 à 15) : coïncidences en fonction de la position de Ds, avec
  barres d'erreur ; durées de comptage lues sur les axes (400, 400, 800, 800,
  500, 500, 1000, 1000 s). Contrôle de `extraire.py` : barres d'erreur égales à
  √N à 0,5 % près en moyenne sur chaque figure. Aux fig. 3 et 7, aucun
  polariseur n'est placé nulle part : l'information de chemin, portée par la
  polarisation, n'est ni analysée ni enregistrée.

### 7. Kim, Yu, Kulik, Shih, Scully (2000) — lu, données des fig. 3 à 5

- Y.-H. Kim, R. Yu, S. P. Kulik, Y. H. Shih, M. O. Scully, « Delayed “Choice”
  Quantum Eraser », Phys. Rev. Lett. 84, 1 (2000),
  https://doi.org/10.1103/PhysRevLett.84.1 ; version arXiv lue : quant-ph/9903047v1
  (PDF SHA-256 `164a96a6c4cc49310748ad26a969ac5fae398c47cab254fbbbff444c38bee1d5`).
- p. 2 : « The width of the SPDC region is about 0.3mm and the distance between
  the center of A and B is about 0.7mm » ; « any information one can learn from
  photon 2 must be at least 8ns later than what one has learned from the
  registration of photon 1 ».
- p. 2 : « Figs.3 and 4 show the “joint detection” rates R01 and R02 [...] there
  is a π phase shift between the two interference fringes » ; « Fig.5 reports a
  typical R03 (R04) [...] An absence of interference is clearly demonstrated. »
- Fig. 3 à 5 (p. 4) : 28, 28 et 15 points, sans barres d'erreur (analyse.py
  prend l'erreur de Poisson √N). Ici l'information de chemin est lue et
  enregistrée (coïncidences avec D3) : c'est le cas « lu ».

### 8. Hornberger et al. (2003) — lu, données des fig. 2 et 3

- K. Hornberger, S. Uttenthaler, B. Brezger, L. Hackermüller, M. Arndt,
  A. Zeilinger, « Collisional Decoherence Observed in Matter Wave
  Interferometry », Phys. Rev. Lett. 90, 160401 (2003),
  https://doi.org/10.1103/PhysRevLett.90.160401 ; version arXiv lue :
  quant-ph/0303093v1 (PDF SHA-256
  `06d3ae4ad0af56fc114d65e532eb453be9dc59eb19c127d6643471e4466c6de5`).
- p. 1 : « a fullerene molecule still enters the detector after a typical
  collision, while the gas particle is left in a state distinguishing the path
  taken. » ; p. 2, éq. (2) : « This form follows from a trace over the scattered
  gas particle. » Les molécules de gaz ne sont jamais détectées.
- p. 3 : « A central molecular velocity of vm = 117 m/s was chosen,
  corresponding to a maximal vacuum visibility of 41% » ; « our calculation,
  which contains no adjustable parameters, agrees well with the observed
  decrease of the visibility. »
- p. 4 : « The experimental error is mainly due to the uncertainty in the
  pressure measurement (about 15%). The uncertainty of the theoretical values
  amounts to about 5% (not drawn in the figure) ».
- Fig. 2 (p. 3) : 17 visibilités (méthane) avec barres, échelle logarithmique,
  et la droite théorique ; fig. 3 : p0 mesuré (10 gaz, avec barres) et calculé.

### 9. Hackermüller et al. (2004) — lu, données de la fig. 4

- L. Hackermüller, K. Hornberger, B. Brezger, A. Zeilinger, M. Arndt,
  « Decoherence of matter waves by thermal emission of radiation », Nature 427,
  711-714 (2004), https://doi.org/10.1038/nature02276 ; version arXiv lue :
  quant-ph/0402146v1 (PDF SHA-256
  `f1f38ac71b1a03102e1b09937eab5f855e0cd5b6a02ace2f5bb83d2a8c217a24`).
- p. 3 : « They transmit (partial) which-path information to the environment » ;
  p. 4 (Methods) : « the absorbing walls of the apparatus are located in the
  far-field » ; les photons émis ne sont pas détectés.
- Légende de la fig. 4, p. 4 : « The maximum contrast without heating was
  V0=47% » (a) ; « The maximum contrast for this velocity class was V0=19% » (b).
- p. 4 : « The experiment is reproducible within the indicated error bars for a
  given laser alignment, but small displacements of the laser focus will
  influence the shape and slope of the observed decoherence curve. The
  difference between the theoretical and the experimental curve is of the order
  of this variation. »
- Fig. 4 : 21 et 11 points avec barres, et les deux courbes théoriques.

### 10. Ma et al. (2013) — lu, tableaux I et II

- X.-S. Ma, J. Kofler, A. Qarry, N. Tetik, T. Scheidl, R. Ursin, S. Ramelow,
  T. Herbst, L. Ratschbacher, A. Fedrizzi, T. Jennewein, A. Zeilinger,
  « Quantum erasure with causally disconnected choice », PNAS 110, 1221-1226
  (2013), https://doi.org/10.1073/pnas.1213201110 ; version arXiv lue :
  1206.6578v2 (29 janvier 2013) (PDF SHA-256
  `f23631be55f1be074c185662f6f794472bf6673f750b1381df02b2d79d5f2c36`).
- p. 2 : « The presence of path information anywhere in the universe is
  sufficient to prohibit any possibility of interference. It is irrelevant
  whether a future observer might decide to acquire it. The mere possibility is
  enough. »
- p. 5-6 : « P (a |V) = 0.023(5) », « P (b |V) = 0.978(5) », « The value
  0.955(7) of the parameter I(i) », « I(ii) [...] has the small value 0.077(22) »,
  « the visibility of V(ii) = 0.951(18) ».
- p. 12 : correction factors « ηI of about 0.97 » et « ηV of about 0.95 ».
- Tableau I, p. 11 (Vienne, six scénarios) et tableau II, p. 13 (Canaries,
  144 km, trois scénarios ; délais du choix −721 µs, 0 µs et 454 µs pour III,
  II’ et II, p. 12), recopiés dans `VALEURS_PUBLIEES['ma2013']` ; le tableau I a
  été lu sur le rendu de la page (les X des colonnes ne sortent pas en texte).
- p. 12 : « These three scenarios gave similar results up to statistical
  errors. » Notre calcul ne confirme pas cette phrase pour V(ii) du tableau II
  (voir `resultats.json`, `ma2013.tableau_II`).

## Reproductibilité

- `python3 extraire.py` (PyMuPDF, accès à arxiv.org) refait `donnees/figures.json`
  à l'identique (vérifié deux fois le 28/09/2026).
- `python3 analyse.py --out resultats.json` (numpy seul) : autotests, puis
  calculs ; graine fixe, résultat identique d'une exécution à l'autre (vérifié).
