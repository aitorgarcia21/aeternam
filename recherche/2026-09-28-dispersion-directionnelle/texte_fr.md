# La lumière va-t-elle moins vite dans certaines directions ?

Brouillon d'article, test n° 3. Chaque nombre tiré de `resultats.json` est écrit
`[[clé]] = valeur` (chemin dans le JSON, indices de liste compris) pour que
l'intégrateur pose les marqueurs.

## Verdict

**Oui : une grille cubique de maille égale ou supérieure à [[resume.maille_exclue_toutes_orientations_m]] = 1,7 × 10⁻²⁶ m est exclue, quelle que soit son orientation et quel que soit son pas de temps.** L'angle mort du test n° 1 est fermé ([[resume.angle_mort_ferme]] = vrai) : huit sources vues dans des directions différentes ne peuvent pas être toutes placées sur des diagonales de la grille.

**Non : aucune trace de grille.** Aucune des huit sources ne montre de retard de la lumière de haute énergie. Le test pose une limite ; il ne découvre rien.

## Pour tous

Si l'Univers était calculé sur une grille, comme une image est faite de pixels, la lumière n'y avancerait pas tout à fait à la même vitesse dans toutes les directions. La lumière la plus énergétique prendrait un tout petit retard, plus fort le long des arêtes du quadrillage que le long de ses diagonales. Sur des milliards d'années de voyage, ce retard deviendrait mesurable.

Le test n° 1 cherchait ce retard dans l'explosion d'étoile la plus brillante jamais observée. Rien n'a été vu. Mais il restait une faille : si la grille avance dans le temps au pas le plus grand possible, la lumière ne prend plus aucun retard le long des diagonales. Une seule source, par malchance placée sur une diagonale, ne pouvait alors rien exclure.

Ici, on regarde huit sources en même temps, dans huit coins du ciel : trois explosions d'étoiles lointaines, quatre galaxies à trou noir très actif, et le pulsar de la nébuleuse du Crabe. Pour chacune, des équipes de chercheurs ont déjà mesuré qu'aucun retard n'apparaît, jusqu'à une certaine finesse. On a relu chaque article, remis tous les résultats dans la même unité, puis cherché l'orientation de la grille la plus favorable à une grille cachée : celle qui rendrait la limite la plus faible possible.

Résultat : il est impossible d'aligner les huit sources sur des diagonales en même temps. Même dans l'orientation la plus favorable, trois sources voient la grille « de biais » et auraient dû voir un retard. Une grille dont les pixels mesurent au moins 1,7 × 10⁻²⁶ m est donc exclue, dans toutes les orientations. C'est inimaginablement petit, mais encore environ un milliard de fois ([[resume.rapport_sur_longueur_Planck]] = 1,03 × 10⁹) au-dessus de la plus petite longueur que la physique sache nommer, la longueur de Planck.

En résumé : la faille du test n° 1 est refermée, mais la limite obtenue quand la grille avance au pas maximal est environ sept fois moins bonne que celle du cas ordinaire. Aucune trace de simulation n'apparaît.

## Pour les spécialistes

**1. Modèle.** Maxwell discrétisé sur un réseau cubique de maille a (schéma de Yee), pas de temps c dt = σ a/√3 avec 0 ≤ σ ≤ 1 (stabilité). La relation de dispersion exacte (2/(c dt))² sin²(ω dt/2) = (2/a)² Σ sin²(k_i a/2) donne, à l'ordre dominant,
v/c = 1 − (1/8) Q_eff (aE/ħc)², avec Q = Σ n_i⁴ dans les axes du réseau et Q_eff = Q − σ²/3.
Comme 1/3 ≤ Q ≤ 1, Q_eff ≥ 0 : le photon est toujours sous-luminal, et Q_eff = 0 exactement sur les grandes diagonales quand σ = 1. Le développement est vérifié contre la dispersion exacte (autotest, écart relatif < 10⁻³ à ak = 10⁻²). À la borne finale, aE/ħc = [[resume.aE_sur_hbar_c_20TeV_a_la_borne]] = 1,7 × 10⁻⁶ à 20 TeV : le développement est largement valide.

**2. Correspondance avec les limites publiées.** Les huit articles utilisent v = c[1 − (3/2)(E/E_QG,2)²] pour n = 2 sous-luminal et le retard de Jacob et Piran Δt = (3/2)(ΔE²/E_QG,2²) K2, K2 = ∫₀^z (1+z')²/H(z') dz' (d/c pour le Crabe). Identifier (3/2)/E_QG,2² = Q_eff a²/(8ħ²c²) donne
E_QG,2 = √12 ħc / (a √Q_eff), donc chaque limite E_QG,2 > E_i devient a √Q_eff(n_i) ≤ B_i = √12 ħc / E_i.
Si la grille était comobile plutôt que physique, K2 changerait ; on ne traite que la maille physique, comme le test n° 1.

**3. Sources et conversions.** Règle fixée d'avance : 95 %, sous-luminal, temps de vol, méthode la moins contraignante de chaque article, systématiques incluses si l'article les donne. Chaque limite est ramenée à la cosmologie de LHAASO (H0 = 67,36 km/s/Mpc, Ωm = 0,315) par E × √(K2_commune/K2_publiée), puisque la contrainte porte sur Δt/ΔE². Le facteur va de [[resume.facteur_cosmologie_min]] = 1,000 à [[resume.facteur_cosmologie_max]] = 1,032. Chaque conversion publiée a été refaite à partir des paramètres imprimés (κ2 de Fermi, κ2 de PG 1553+113, κ2 de Mrk 421 en secondes, η2, ζ, τ2) ; toutes retombent sur la valeur imprimée à l'arrondi près (autotests).

| Source | E_QG,2 publiée | E_QG,2 cosmologie commune | B = borne sur a√Q_eff |
|---|---|---|---|
| GRB 221009A (LHAASO, z = 0,151) | [[sources.0.EQG2_publie_GeV]] = 4,75 × 10¹¹ GeV | [[sources.0.EQG2_commun_GeV]] = 4,75 × 10¹¹ GeV | [[sources.0.a_racine_Qeff_max_m]] = 1,44 × 10⁻²⁷ m |
| GRB 190114C (MAGIC, z = 0,4245) | [[sources.1.EQG2_publie_GeV]] = 6,3 × 10¹⁰ GeV | [[sources.1.EQG2_commun_GeV]] = 6,41 × 10¹⁰ GeV | [[sources.1.a_racine_Qeff_max_m]] = 1,07 × 10⁻²⁶ m |
| GRB 090510 (Fermi-LAT, z = 0,903) | [[sources.2.EQG2_publie_GeV]] = 6,7 × 10¹⁰ GeV | [[sources.2.EQG2_commun_GeV]] = 6,91 × 10¹⁰ GeV | [[sources.2.a_racine_Qeff_max_m]] = 9,89 × 10⁻²⁷ m |
| Mrk 501 (H.E.S.S., z = 0,034) | [[sources.3.EQG2_publie_GeV]] = 8,5 × 10¹⁰ GeV | [[sources.3.EQG2_commun_GeV]] = 8,52 × 10¹⁰ GeV | [[sources.3.a_racine_Qeff_max_m]] = 8,02 × 10⁻²⁷ m |
| Mrk 421 (MAGIC, z = 0,03) | [[sources.4.EQG2_publie_GeV]] = 2,5 × 10¹⁰ GeV | [[sources.4.EQG2_commun_GeV]] = 2,55 × 10¹⁰ GeV | [[sources.4.a_racine_Qeff_max_m]] = 2,68 × 10⁻²⁶ m |
| PKS 2155-304 (H.E.S.S., z = 0,116) | [[sources.5.EQG2_publie_GeV]] = 6,4 × 10¹⁰ GeV | [[sources.5.EQG2_commun_GeV]] = 6,56 × 10¹⁰ GeV | [[sources.5.a_racine_Qeff_max_m]] = 1,04 × 10⁻²⁶ m |
| PG 1553+113 (H.E.S.S., z = 0,49) | [[sources.6.EQG2_publie_GeV]] = 2,1 × 10¹⁰ GeV | [[sources.6.EQG2_commun_GeV]] = 2,13 × 10¹⁰ GeV | [[sources.6.a_racine_Qeff_max_m]] = 3,21 × 10⁻²⁶ m |
| Crabe (MAGIC, 2,0 kpc) | [[sources.7.EQG2_publie_GeV]] = 5,9 × 10¹⁰ GeV | [[sources.7.EQG2_commun_GeV]] = 5,9 × 10¹⁰ GeV | [[sources.7.a_racine_Qeff_max_m]] = 1,16 × 10⁻²⁶ m |

**4. Borne pour une orientation, pire orientation.** Pour une rotation R du réseau, a ≤ A(R) = min_i B_i / √Q_eff(R n_i) (une source avec Q_eff = 0 ne borne rien). On cherche max_R A(R) : [[constantes.n_orientations]] = 100 000 rotations uniformes (quaternions gaussiens normalisés, graine 20260928), plus 8 × 720 orientations construites (chaque source posée sur la diagonale (1,1,1)/√3 puis tournée autour d'elle), puis montée aléatoire à pas décroissant depuis les 48 meilleures. Une seconde graine indépendante retrouve le même maximum à σ = 1 à [[resume.ecart_relatif_deux_graines_sigma1]] = 4 × 10⁻⁷ près. L'optimiseur est validé sur des cas connus : une source seule donne B√3 à σ = 0 et aucune borne à σ = 1 ; deux sources séparées de arccos(1/3) peuvent être mises ensemble sur des diagonales (aucune borne).

| σ | pire orientation | 95 % des orientations |
|---|---|---|
| 0 | [[resume.pire_sigma0_m]] = 2,49 × 10⁻²⁷ m | [[resume.q95_sigma0_m]] = 2,38 × 10⁻²⁷ m |
| 0,5 | [[resume.pire_sigma05_m]] = 2,88 × 10⁻²⁷ m | [[resume.q95_sigma05_m]] = 2,71 × 10⁻²⁷ m |
| 0,9 | [[resume.pire_sigma09_m]] = 5,72 × 10⁻²⁷ m | [[resume.q95_sigma09_m]] = 4,65 × 10⁻²⁷ m |
| 1 | [[resume.pire_sigma1_m]] = 1,66 × 10⁻²⁶ m | [[resume.q95_sigma1_m]] = 8,00 × 10⁻²⁷ m |

« 95 % des orientations » : pour 95 % des rotations tirées, la borne est au moins aussi bonne que cette valeur. La médiane à σ = 1 vaut [[resume.mediane_sigma1_m]] = 3,06 × 10⁻²⁷ m.

**5. Lecture.** Pour σ < 1, rien ne change par rapport au test n° 1 : GRB 221009A domine, les autres sources sont de [[resume.rapport_B_autres_sur_LHAASO_min]] = 5,6 à [[resume.rapport_B_autres_sur_LHAASO_max]] = 22 fois moins sensibles, et la pire orientation reste celle qui met GRB 221009A sur une diagonale (B√(3/(1 − σ²))). Tout se joue à σ = 1. Placer GRB 221009A sur une diagonale ne suffit plus, car les autres sources voient alors la grille de biais. Le pire compromis écarte GRB 221009A de [[resume.angle_diag_GRB221009A_pire_sigma1_deg]] = 4,3° de la diagonale la plus proche (Q_eff = [[resume.Qeff_GRB221009A_pire_sigma1]] = 0,0075) et équilibre [[resume.n_sources_actives_sigma1]] = 3 contraintes actives : GRB 221009A, GRB 090510 et le Crabe. La borne vaut alors [[resume.pire_sigma1_m]] = 1,66 × 10⁻²⁶ m, soit une échelle 1/a ≥ [[resume.echelle_min_toutes_orientations_GeV]] = 1,19 × 10¹⁰ GeV. Comme A(R) croît avec σ pour toute R, cette valeur vaut pour tout σ ≤ 1.

La fermeture n'est pas triviale : GRB 190114C et GRB 090510 sont séparés de [[resume.angle_GRB190114C_GRB090510_deg]] = 70,84°, presque l'angle entre deux diagonales ([[resume.angle_entre_diagonales_deg]] = 70,53°), et GRB 090510 et PKS 2155-304 ne sont qu'à [[resume.angle_GRB090510_PKS2155_deg]] = 4,96° l'un de l'autre. C'est la diversité du reste du ciel (hémisphère nord, Crabe) qui ferme l'angle mort.

**6. Robustesse.** Pire orientation à σ = 1 :
- sans GRB 221009A : [[variantes.sans_LHAASO.sigma_1.pire_m]] = 4,61 × 10⁻²⁶ m (toujours fermé) ;
- limites publiées sans conversion de cosmologie : [[variantes.sans_cosmologie_commune.sigma_1.pire_m]] = 1,68 × 10⁻²⁶ m ;
- Fermi avec effets intrinsèques (tableau V, 4,0 × 10¹⁰ GeV) : [[variantes.Fermi_tableau_V.sigma_1.pire_m]] = 1,77 × 10⁻²⁶ m ;
- sursauts gamma seuls : [[variantes.sursauts_seuls.sigma_1.pire_m]] = 2,64 × 10⁻²⁶ m ;
- blazars et pulsar seuls : [[variantes.blazars_et_pulsar_seuls.sigma_1.pire_m]] = 6,58 × 10⁻²⁶ m.

**7. Comparaisons.** Test n° 1 (GRB 221009A seul) : [[resume.test1_pire_sigma0_m]] = 2,49 × 10⁻²⁷ m à σ = 0, aucune borne à σ = 1. La borne toutes orientations et tout σ est [[resume.rapport_sur_test1_sigma0]] = 6,7 fois plus faible que le cas σ = 0. Beane, Davoudi et Savage (arXiv:1210.1847) : 1/b ≳ 10¹¹ GeV, soit b ≲ [[resume.beane_b_max_m]] = 1,97 × 10⁻²⁷ m, tiré de la coupure des rayons cosmiques et non d'une mesure de retard. Notre borne à σ = 0 est [[resume.rapport_sigma0_sur_beane]] = 1,26 fois au-dessus ; la borne toutes orientations et tout σ est [[resume.rapport_sur_beane]] = 8,4 fois au-dessus.

## Limites

- La borne combinée prend, pour chaque orientation, la plus contraignante de limites publiées à 95 % une par une : ce n'est pas une vraisemblance combinée (les vraisemblances ne sont pas publiées). À la pire orientation, trois limites sont actives ; par Bonferroni, la couverture est d'au moins [[resume.couverture_min_bonferroni_sigma1]] = 85 %, pas 95 %.
- Chaque article suppose qu'aucun décalage propre à la source ne vient compenser ou imiter le retard. Un tel décalage, s'il existait, pourrait masquer une grille.
- Les redshifts de Mrk 421 (0,03) et surtout de PG 1553+113 (0,49 ± 0,04, estimé par l'article) portent une incertitude ; ces deux sources ne sont pas actives à la pire orientation.
- La distance du Crabe (2,0 ± 0,5 kpc) est incluse dans les systématiques de MAGIC ; le Crabe est actif à la pire orientation.
- Les fractions d'orientations sont géométriques, pas des probabilités sur l'Univers.
- Un schéma amélioré (erreur en a⁴), des termes compensateurs, une grille non cubique ou comobile échappent à cette borne.
- Analyse secondaire : aucun photon n'est réanalysé.

## Sources

- LHAASO, GRB 221009A : arXiv:2402.06009v3, tableau I p. 6.
- MAGIC, GRB 190114C : arXiv:2001.09728v4, tableau I p. 6.
- Fermi-LAT, GRB 090510 : arXiv:1305.3463v1, tableau IV p. 15 (variante : tableau V p. 18).
- H.E.S.S., Mrk 501 : arXiv:1901.05209v1, p. 7.
- MAGIC, Mrk 421 : arXiv:2406.07140v1, tableau 2 p. 16.
- H.E.S.S., PKS 2155-304 : arXiv:1101.3650v2, p. 20.
- H.E.S.S., PG 1553+113 : arXiv:1501.05087v1, tableau 5 p. 23.
- MAGIC, pulsar du Crabe : arXiv:1709.00346v1, tableau 6 p. 21.
- Beane, Davoudi, Savage : arXiv:1210.1847v2, p. 1 et p. 11.
- Coordonnées : SIMBAD (CDS), fiches copiées dans `donnees/`.
- Détail des citations : `sources.md` ; calcul : `analyse.py`, `resultats.json`.
