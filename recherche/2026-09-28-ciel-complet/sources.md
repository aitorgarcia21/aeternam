# Correction du 29 septembre 2026

Les bornes d’amplitude utilisent une approximation normale et un balayage fini des orientations. Elles ne certifient pas une couverture uniforme sur le continuum.

Les passages ci-dessous conservent le relevé documentaire et le raisonnement antérieur pour traçabilité. En cas de conflit, le script actuel, ses résultats régénérés et le [rapport d’audit](../../AUDIT-SCIENTIFIQUE.md) font foi.

---

# Test n° 6 : sources de chaque donnée et de chaque chiffre d'entrée

Tout a été relevé le 28 septembre 2026 dans les fichiers et PDF indiqués
(PDF arXiv téléchargés par `https://arxiv.org/pdf/<identifiant>`), et non de
mémoire. Les pages sont celles du PDF. Les nombres calculés viennent de
`resultats.json`, produit par `analyse.py`.

## 1. Ce qui a été cherché, et ce qui existe

| Jeu cherché | Public ? | Utilisé ? |
|---|---|---|
| Auger, 2 635 événements ≥ 32 EeV, 2004-2020 (ApJ 935, 170, 2022) | oui, Zenodo, CC BY-SA 4.0 | **oui : échantillon sud** |
| Auger, 100 événements ≥ 78 EeV (ApJS 264, 50, 2023 ; test n° 2) | oui | contenu dans le précédent (vérifié) |
| Auger, 231 événements ≥ 52 EeV, 2004-2014 (ApJ 804, 15, 2015) | oui, tableau 2 | non : période et reconstruction dépassées par la liste de 2022 |
| Auger, données ouvertes (sous-échantillon des verticaux, ApJ 935, 170, p. 16) | oui | non : la liste complète au-dessus de 32 EeV rend le sous-échantillon inutile |
| TA, 72 événements > 57 EeV, 2008-2013 (ApJL 790, L21, 2014) | table publiée, © AAS | **oui : échantillon nord**, téléchargé à l'exécution, non redistribué |
| TA, « Amaterasu », 244 EeV, 27 mai 2021 (Science 382, 903, 2023) | oui, Zenodo, CC BY 4.0 | variante seulement (événement isolé, hors période) |
| TA, 28 événements > 100 EeV, 2008-2021 (même article) | figure seulement, aucune table | non : pas de coordonnées publiées |
| TA, jeux 2008-2019 et 2008-2024 des analyses communes Auger-TA | non publiés | non |

Recherches faites : site de TA (`https://www.telescopearray.org/`, rubrique
« research » : publications seulement, aucune donnée), Zenodo (recherches
« Telescope Array » : seul l'enregistrement Amaterasu vient de la
collaboration), articles TA et communs listés ci-dessous. Aucune autre liste
TA d'événements avec coordonnées n'a été trouvée ; on n'en a reconstitué
aucune (par exemple en relevant des points sur une figure).

## 2. Auger : la liste des 2 635 événements

- Article : Pierre Auger Collaboration, « Arrival Directions of Cosmic Rays
  above 32 EeV from Phase One of the Pierre Auger Observatory », ApJ 935, 170
  (2022), https://arxiv.org/abs/2206.13492v2 (licence arXiv CC BY-SA 4.0).
  - p. 1 : « We publish this data set, the largest available at such
    energies from an integrated exposure of 122,000 km2 sr yr ».
  - p. 2 : période 1er janvier 2004 - 31 décembre 2020 ; « events with zenith
    angles, θ, less than 60° are called vertical events, while events
    arriving with zenith angles from 60° to 80° are called inclined events ».
  - p. 3 : « The selection results in 2,040 events with θ < 60° and 595 with
    θ ≥ 60° above 32 EeV » ; exposition géométrique, « above the energy
    threshold for full efficiency for both data samples (3 EeV for vertical
    and 4 EeV for inclined) » ; 95 700 et 26 300 km² sr an ; échelle
    d'énergie : systématique ∼14 %, résolution ∼7 % ; « a deficit of inclined
    events is observed at a significance level of 2.5σ » au-dessus de 80 EeV.
  - p. 16 (annexe A) : description des colonnes (année, jour, temps UTC,
    zénith, azimut, α et δ J2000, énergie en EeV, exposition cumulée) ;
    « The full list of 2,635 events […] is available at DOI
    10.5281/zenodo.6504276 ». Même page : au-dessus de 80 EeV, 10 inclinés
    pour 86 verticaux ; « a subsample of the vertical events used here is
    included in the recent Data Release » (données ouvertes d'Auger).
  - p. 11 (§ 5) : excès autour de Centaurus A, « (α, δ) = (201.4°, −43.0°) »,
    « Eth = 38 EeV in a circle of top-hat radius Ψ = 27°, where […] Nobs = 215
    while Nexp = 152.0 », p-valeur après pénalisation 4,5 × 10⁻⁵.
- Données : Zenodo, DOI 10.5281/zenodo.6504276 (version 1.0,
  10.5281/zenodo.6759610, 27 juin 2022), archive `Anisotropy_ ApJS_2022.zip`
  (3 058 911 octets, md5 `458fa456df118a516716ab0d1b5dca04`, identique à
  celui publié par Zenodo). Licence : la fiche Zenodo indique CC BY 4.0, la
  description « released under the (CC BY-SA 4.0) International License » ;
  on applique la plus exigeante, CC BY-SA 4.0 (attribution, partage dans les
  mêmes conditions).
- Fichier copié tel quel : `donnees/AugerApJS2022_Yr_JD_UTC_Th_Ph_RA_Dec_E_Expo.dat`
  (2 635 lignes, sha256
  `b03b91b5b4bf98b373cde2a9f41044704a32af77029cf9c07044e6860ffabb35`,
  vérifiée à chaque exécution).
- Code d'exposition de la même archive, `Data/exposure.cc` : latitude
  `augerLat = -35.2`, bande inclinée `thetaMin = 60`, `thetaMax = 80`,
  formule de Sommers par bande, et exposition totale
  `covV/covV.Total()*nVert + covH/covH.Total()*nHor` : chaque bande est
  pondérée par son nombre d'événements. Nous faisons de même en tenant fixe
  le nombre d'événements de chaque bande.
- Vérifié par nous : les 100 événements du catalogue du test n° 2 sont tous
  dans cette liste (même temps UTC à 1 s près, énergies à 0,5 EeV près,
  ascension droite à 0,1° près) ; la liste en compte 105 au-dessus de
  78 EeV, les 5 autres ayant été écartés du catalogue de 2023.
- Latitude : Pierre Auger Collaboration, ApJ 804, 15 (2015),
  https://arxiv.org/abs/1411.6111v3, p. 9, « located in Malargüe, Argentina,
  at latitude 35.2°S, longitude 69.5°W ».

## 3. Telescope Array : les 72 événements

- Article : Telescope Array Collaboration (R. U. Abbasi et al.),
  « Indications of Intermediate-Scale Anisotropy of Cosmic Rays with Energy
  Greater Than 57 EeV in the Northern Sky Measured with the Surface Detector
  of the Telescope Array Experiment », ApJL 790, L21 (2014),
  https://arxiv.org/abs/1404.5890v3 (licence arXiv non exclusive).
  - p. 5 : « in full operation in Millard Country, Utah, USA (39.°30N,
    112.°91W) » ; « 72 met the following conditions: (1) each event included
    at least four SD counters; (2) the zenith angle […] was less than 55°;
    and (3) the reconstructed energy was greater than 57 EeV » ; période du
    11 mai 2008 au 4 mai 2013.
  - p. 6 : « We used a geometrical exposure g(θ) = sinθcosθ as a function of
    zenith angle (θ) because the detection efficiency above 57 EeV is
    ∼100% » : l'exposition est celle de Sommers avec latitude 39,30° et
    zénith < 55°.
  - p. 7 : point chaud centré en « R.A. = 146.°7, Dec. = 43.°2 », cercles de
    20°, « Non = 19, Nbg = 4.49 », probabilité 3,7 × 10⁻⁴ après essais.
  - p. 9 : annexe A, « the list of events with energy E > 57 EeV and zenith
    angle θ < 55° that have been recorded […] from May 11, 2008 to May 4,
    2013. During this period, 72 such events were observed » ; p. 15-16 :
    tableau 1, date et heure UTC, zénith, énergie, α et δ des 72 événements.
- Table lisible par machine de l'éditeur :
  https://content.cld.iop.org/journals/2041-8205/790/2/L21/revision1/apjl498370t1_mrt.txt
  (6 387 octets, sha256
  `0c8dcc83e95e7b2bc30c787ffcce7330783aa2c488d4b44a1d7b82c990134525`),
  colonnes décrites dans son en-tête (« Right Ascension in decimal degrees
  (J2000) »). La page de l'article porte « © 2014. The American Astronomical
  Society. All rights reserved. » : aucune licence n'autorise la
  redistribution. Le fichier **n'est donc pas versionné** (voir `.gitignore`) ;
  `analyse.py` le télécharge à la première exécution et vérifie son
  empreinte. En secours, il lit la source LaTeX de la version arXiv
  (https://arxiv.org/e-print/1404.5890v3, fichier `ms.tex`, sha256
  `f93ba17024acb77cbf83b2c7c5896ccf0f7a96dcc396e249a38e1f086653c878`).
- Vérifié par nous : la table de l'éditeur, la source LaTeX et le texte du PDF
  arXiv donnent exactement les mêmes 72 lignes (empreinte de la liste lue,
  `e5c47447625d53dc6955c70a96d921e1db64f71c2735e543718eb127fbcfaee8`,
  contrôlée à chaque exécution) ; énergies de 57,3 à 162,2 EeV ; zénith
  maximal 54,73° ; déclinaisons de −4,78° à 81,53°.
- Code de la collaboration TA (archive Zenodo de l'événement Amaterasu,
  `2_skymaps/utility4anisotropy.py`) : `lat = 39.30`, `zenith_max = 55.0`,
  même formule de Sommers.

## 4. L'événement Amaterasu (variante seulement)

- Article : Telescope Array Collaboration, « An extremely energetic cosmic
  ray observed by a surface detector array », Science 382, 903 (2023),
  https://arxiv.org/abs/2311.14231v1.
  - p. 5, tableau 1 : 27 mai 2021, 10:35:56 UTC, 244 ± 29 (stat.) +51/−76
    (syst.) EeV, zénith 38,6°, α = 255,9 ± 0,6°, δ = 16,1 ± 0,5°.
  - p. 10 : « the 28 TA SD events with energy >100 EeV observed between
    2008 May and 2021 November » : montrés sur la figure 3, sans table.
  - p. 17 : « Data of the extremely energetic cosmic ray event and codes are
    available at Zenodo ».
- Données : Zenodo, DOI 10.5281/zenodo.8427755 (4 octobre 2023), CC BY 4.0,
  archive `Data_Release_TASD.zip` (md5 `2f8063d9b9490bbe467dd432bc23f9c3`).
  Fichier copié : `donnees/tasd_highest_event_244EeV_backtrack_JF_PT_eq.dat`
  (sha256 `980b0cb04f78edbed022a5d059d72b5ebc27467c664694a7b81cd96aa44ed0ee`) ;
  sa première ligne donne la direction mesurée (255,845° ; 16,0845°) et
  243,611 EeV, les suivantes les directions recalculées à travers le champ
  magnétique galactique (non utilisées).

## 5. L'écart d'échelle d'énergie entre Auger et TA

Les deux collaborations ont un groupe de travail commun qui recale les
énergies en comparant les flux dans la bande de ciel vue par les deux
observatoires. Forme publiée : E_Auger / 10 EeV = exp(α) (E_TA / 10 EeV)^β.

- **Retenu** : A. Gálvez Ureña pour les collaborations Auger et TA,
  « New full-sky studies of the distribution of ultra-high-energy
  cosmic-ray arrival directions », ICRC 2025,
  https://arxiv.org/abs/2507.10441v1, p. 3 : « for the intermediate scale
  anisotropies and the harmonic analyses we use the TA loose-cut data for
  E_TA ≥ 57 EeV. However, since this dataset does not have available
  atmospheric corrections, we use the energy calibration from [2], with
  α = −0.159, β = 0.954, and E_Auger = 32 EeV ↔ E_TA = 40.0 EeV ». La
  sélection « loose-cut » est celle de la réf. [6] = ApJL 790 (2014) L21,
  c'est-à-dire exactement notre liste TA (p. 8, références ; [2] = PoS
  (UHECR2024) 009 ; [4] = ApJ 935 (2022) 170, notre liste Auger). D'où
  57 EeV (TA) = 44,88 EeV (Auger), et 78 EeV (Auger) = 101,7 EeV (TA).
- Variantes : même article, p. 3, coupures strictes, α = −0,150 ± 0,011,
  β = 0,962 ± 0,016 (seuil Auger 45,9 EeV) ; A. di Matteo et al., ICRC 2021,
  https://arxiv.org/abs/2111.12366v1, p. 3, éq. (1),
  « E_TA ↦ E_Auger = 8.57 (E_TA/10 EeV)^0.937 EeV » (seuil Auger 43,8 EeV) ;
  rapport UHECR 2022, https://arxiv.org/abs/2302.04502v1, p. 3,
  α = −0,159 ± 0,012 et β = 0,945 ± 0,016 (seuil 44,2 EeV, entre les deux).
  Les correspondances imprimées (32 ↔ 40,0 ; 10 ↔ 8,60 ; 16 ↔ 19,1 ;
  32 ↔ 39,2 ; 32 ↔ 40,5 ; 32 ↔ 40,8 ; 38 ↔ 49,0 ; 59 ↔ 78,4 ; 80 ↔ 108,6)
  sont refaites par les autotests.
- Incertitudes d'échelle absolue : ±14 % (Auger), ±21 % (TA),
  arXiv:2507.10441v1 p. 3.
- Historique, non utilisé : en 2015, les collaborations IceCube, Auger et TA
  abaissaient les énergies TA de 13 % (https://arxiv.org/abs/1511.09408v2,
  p. 9), valeur tirée de la région de la cheville du spectre ; la
  comparaison des spectres de 2025 (https://arxiv.org/abs/2509.05530v1,
  p. 3-5) trouve un décalage de 11,2 % sous 10¹⁹ eV et un écart qui croît de
  16 à 20 % par décade au-dessus, d'où la forme en loi de puissance retenue
  par le groupe de travail.

## 6. Méthode : ce qui vient d'ailleurs

- Prédiction : S. R. Beane, Z. Davoudi, M. J. Savage, arXiv:1210.1847
  (voir le test n° 2 et ses sources).
- Exposition : P. Sommers, Astropart. Phys. 14, 271 (2001),
  arXiv:astro-ph/0004016 ; utilisée sous la même forme par Auger
  (`exposure.cc`), par TA (`utility4anisotropy.py`) et par le groupe commun
  (arXiv:2111.12366v1, p. 3 : « computed in the approximation of 100%
  detector efficiency [18] », [18] = Sommers).
- Statistique, calibration, orientations et graine : test n° 2,
  `recherche/2026-09-28-rayons-cosmiques/analyse.py` ; les résultats du test
  n° 2 cités ici sont lus dans son `resultats.json`.

## 7. Excès connus masqués dans une variante

- Centaurus A : cercle de 27° autour de (201,4° ; −43,0°), arXiv:2206.13492v2 p. 11.
- Point chaud TA : cercle de 20° autour de (146,7° ; 43,2°), arXiv:1404.5890v3 p. 7.
Ces paramètres sont ceux publiés par les collaborations, fixés avant notre
analyse ; nous ne les avons pas ajustés.
