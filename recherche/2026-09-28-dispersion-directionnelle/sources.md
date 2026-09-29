# Correction du 29 septembre 2026

La couverture de Bonferroni porte sur huit sources, soit au moins 60 % sous les hypothèses nominales, et non sur les trois contraintes sélectionnées après optimisation (85 %). L’optimisation des orientations n’est pas un certificat global.

Les passages ci-dessous conservent le relevé documentaire et le raisonnement antérieur pour traçabilité. En cas de conflit, le script actuel, ses résultats régénérés et le [rapport d’audit](../../AUDIT-SCIENTIFIQUE.md) font foi.

---

# Test n° 3 : sources de chaque chiffre d'entrée

Tout a été relevé le 28 septembre 2026 dans le PDF de la version arXiv indiquée
(téléchargé par `https://arxiv.org/pdf/<identifiant>`), et non de mémoire. Les
pages sont celles du PDF. « Sous-luminal » : les photons de haute énergie
arrivent en retard, le seul cas que prévoit la grille (Q_eff ≥ 0).

Règle de choix, fixée avant le calcul : limite à 95 %, sous-luminale, n = 2,
temps de vol seulement ; quand l'article donne plusieurs méthodes, on garde la
**moins contraignante** (comme au test n° 1) ; avec systématiques quand l'article
les inclut.

## Convention commune

Tous les articles retenus utilisent la même vitesse de groupe
v = c[1 − s (n+1)/2 (E/E_QG,n)^n] et le même retard de Jacob et Piran
Δt = s (n+1)/2 (ΔE^n / E_QG,n^n) ∫₀^z (1+z')^n / H(z') dz'
(pour le Crabe, l'intégrale est remplacée par d/c). La grille donne
v/c = 1 − (1/8) Q_eff (aE/ħc)², donc (3/2)/E_QG,2² = Q_eff a² / (8 ħ²c²), soit
**E_QG,2 = √12 ħc / (a √Q_eff)** : chaque limite E_QG,2 > E_i devient
a·√Q_eff ≤ B_i = √12 ħc / E_i. Seule la cosmologie diffère d'un article à
l'autre ; on ramène chaque limite à celle de LHAASO (H0 = 67,36 km/s/Mpc,
Ωm = 0,315, plat) par E_commune = E_publiée × √(K2_commune / K2_publiée) (la
contrainte porte sur Δt/ΔE², donc sur K2/E²). Effet : +0 à +3,2 %.

## Les huit sources retenues

### 1. GRB 221009A (LHAASO)
- Article : https://arxiv.org/abs/2402.06009v3
- Convention : p. 2, éq. (2) « υ(E) ≈ c[1 − s (n+1)/2 (E/E_QG,n)^n] », éq. (3) Jacob et Piran avec « H0 = 67.36 km s−1 Mpc−1, … Ωm = 0.315, and … ΩΛ = 1 − Ωm » ; éq. (5) « η2 = 10−15 × s E²Pl/E²QG,2 ».
- Redshift : p. 3, « This object is located at redshift z = 0.151 ».
- Limite : p. 6, tableau I, méthode CCF, « η2 … 0.66 » (limite haute) ; ligne « EQG,2 [10¹¹ GeV] » : 4.7 (sous-luminal, CCF). Recalcul : 1,22e19 × √(1e-15/0,66) = 4,75e11 GeV. Autres méthodes : 6.9 (ML MINOS), 7.2 (ML étalonnée).
- Même entrée qu'au test n° 1 (continuité vérifiée par autotest).

### 2. GRB 190114C (MAGIC)
- Article : https://arxiv.org/abs/2001.09728v4
- Convention : p. 2, éq. (2)-(3) avec facteur (n+1)/2 et D_n(z) éq. (6) ; « we use H0 = 70 km s−1 Mpc−1, ΩΛ = 0.7, and Ωm = 0.3 » ; éq. (5) « η2 = 10−16 × s E²Pl/E²QG,2 » (attention : 10⁻¹⁶, pas 10⁻¹⁵).
- Redshift : p. 3, « z = 0.4245 ± 0.0005 ».
- Limite : p. 6, tableau I, « EQG,2 [10¹⁰ GeV] » : 6.3 (théorique, sous-luminal) ; 7.3 (modèle minimal). Retenu : 6,3e10 GeV (η2 < 3.7 ; recalcul 6,34e10).

### 3. GRB 090510 (Fermi-LAT)
- Article : https://arxiv.org/abs/1305.3463v1
- Convention : p. 3, éq. (2)-(4), « τn ≡ Δt/(E^n_h − E^n_l) ≃ s± (1+n)/(2H0) κn/E^n_QG » ; p. 4, « ΩM = 0.272 and ΩΛ = 0.728 … H0 = 73.8 ± 2.4 km s−1 Mpc−1 ».
- Redshift : p. 4, tableau I, « 090510 0.903 ± 0.003 … κ2 1.50 » (κ2 recalculé : 1,503).
- Limite : p. 15, tableau IV, « n=2, s±=+1 (10¹⁰ GeV units) », ligne 090510, 95 % : PairView 6.7, SMM 13, Likelihood 8.6. Retenu : 6,7e10 GeV (le 1,3e11 du résumé est la meilleure des trois).
- Variante : p. 18, tableau V (effets intrinsèques pris en compte), n = 2, s± = +1 : 4.0 (×10¹⁰ GeV).

### 4. Mrk 501 (H.E.S.S., éruption de 2014)
- Article : https://arxiv.org/abs/1901.05209v1
- Convention : p. 6, éq. (2), « τn = Δtn/ΔEn ≃ ± (n+1)/2 (1/E^n_QG) ∫(1+z')^n/H(z') dz' » ; « H0 = 67.74 km·Mpc−1·s−1, … Ωm = 0.31 … ΩΛ = 0.69 ».
- Redshift : p. 4, « blazar at a redshift z = 0.034 ».
- Limite : p. 7, « τ2,best = −0.6 ± 1.8(stat) ± 0.7(syst) s·TeV−2 » et « EQG,2 > 8.5 × 10¹⁰ GeV (subluminal) ». Recalcul (1,96 σ, stat ⊕ syst) : 8,65e10 GeV.
- Écartée : la limite « spectrale » 7,8e11 GeV (absorption sur la lumière de fond extragalactique), autre physique que le temps de vol.

### 5. Mrk 421 (MAGIC, éruption de 2014)
- Article : https://arxiv.org/abs/2406.07140v1
- Convention : p. 6, éq. (1.3)-(1.5), facteur (n+1)/2, κn(zs) = (1/H0)∫(1+z)^n/√(ΩΛ+Ωm(1+z)³) dz, « ΩΛ ≅ 0.69 and Ωm ≅ 0.31 … H0 ≡ 70 km Mpc−1 s−1 ».
- Redshift : p. 15, « κ2(zs = 0.03) = 1.35 × 10¹⁶ seconds » (recalculé : 1,353e16 s) ; p. 8 donne z = 0.031 pour la galaxie hôte, on garde 0,03 comme l'article dans son calcul.
- Limite : p. 16, tableau 2, « Quadratic scenario … Including systematic uncertainties » : superluminal 2.6 × 10¹⁰, subluminal 2.5 × 10¹⁰. Le résumé (arXiv abs) intervertit : « subluminal … 2.6 × 10¹⁰ GeV and … superluminal 2.5 × 10¹⁰ GeV ». Retenu : la plus faible, 2,5e10 GeV.
- Contrôle : sans systématiques, η2 < 16 s/TeV² → 3,56e10 GeV (imprimé 3.5).

### 6. PKS 2155-304 (H.E.S.S., éruption du MJD 53944)
- Article : https://arxiv.org/abs/1101.3650v2
- Convention : p. 5, éq. (5) « Δt/ΔE² ≈ 3ζ/(2E²P H0) ∫(1+z')²dz'/√(Ωm(1+z')³+ΩΛ) », « Ωm = 0.3, ΩΛ = 0.7 and H0 = 2.3 × 10−18 s−1 ».
- Redshift : p. 8, « located at redshift z = 0.116 ».
- Limite : p. 20, « Mq_QG > 6.4 × 10¹⁰ GeV (ζ < 3.6 × 10¹⁶) » à 95 %. Recalcul : 1,22e19/√3,6e16 = 6,43e10.

### 7. PG 1553+113 (H.E.S.S., éruption de 2012)
- Article : https://arxiv.org/abs/1501.05087v1 (article complet ; le compte rendu 1502.02920v2 donne 2.11e10 sans convention ni cosmologie, non retenu)
- Convention : p. 7, « H0 = 70.4 ±1.4 km s−1 Mpc−1, Ωm = 0.27 ±0.03, ΩΛ = 0.73 » ; p. 19, éq. (3)-(4), facteur (1+n)/(2H0) et κn.
- Redshift : p. 19, « Using the central value of z = 0.49 … κ1 = 0.541 and κ2 = 0.677 » (recalculés : 0,541 et 0,6766). Ce redshift est estimé par l'article lui-même (z = 0.49 ± 0.04).
- Limite : p. 23, tableau 5, n = 2 : « ULcalib+syst 1012.4 » s TeV⁻², « s = +1 : 2.10 10¹⁰ » GeV. Recalcul : 2,096e10.

### 8. Pulsar du Crabe (MAGIC)
- Article : https://arxiv.org/abs/1709.00346v1
- Convention : p. 3, éq. (1), facteur ξn (n+1)/2 ; p. 5, éq. (2), retard proportionnel à d_Crab/c ; p. 4, distance « generally stated as 2.0 ± 0.5 kpc ».
- Limite : p. 21, tableau 6, « EQG2 (GeV) ξ2 = +1 … (Incl. Systematics) 5.9 × 10¹⁰ » (l'incertitude sur la distance est dans les systématiques, tableau 5 p. 20). Pas de cosmologie : aucune conversion.

## Coordonnées (SIMBAD)

Relevées par `https://simbad.cds.unistra.fr/simbad/sim-id?Ident=<nom>&output.format=ASCII`, copies brutes dans `donnees/` (empreintes sha256 vérifiées par `analyse.py`). Ligne « Coordinates(ICRS,ep=J2000,eq=2000) » :

| Source | Identifiant SIMBAD | α (ICRS) | δ (ICRS) | Référence SIMBAD |
|---|---|---|---|---|
| GRB 221009A | GRB 221009A | 19 13 03.85 | +19 46 22.7 | Swift (X) |
| GRB 190114C | GRB 190114C | 03 38 01.18 | −26 56 47.8 | Swift (X) |
| GRB 090510 | Fermi bn090510016 | 22 14 12.6230 | −26 34 58.550 | 2022ApJ...940...56F |
| Mrk 501 | Mrk 501 | 16 53 52.21668403 | +39 45 36.6088754 | 2020A&A...644A.159C |
| Mrk 421 | Mrk 421 | 11 04 27.3140835504 | +38 12 31.798495872 | Gaia (2020yCat.1350) |
| PKS 2155-304 | PKS 2155-304 | 21 58 52.0652249880 | −30 13 32.118447792 | Gaia (2020yCat.1350) |
| PG 1553+113 | PG 1553+113 | 15 55 43.0440048528 | +11 11 24.365649948 | Gaia (2020yCat.1350) |
| Crabe | PSR B0531+21 | 05 34 31.9474694616 | +22 00 52.153698024 | Gaia (2020yCat.1350) |

Une précision d'un degré suffirait : Q varie lentement avec la direction.

## Comparaisons

- Beane, Davoudi et Savage, https://arxiv.org/abs/1210.1847v2 : p. 1 (résumé) « b^(−1) >∼ 10^11 GeV » ; p. 11, « a lattice spacing of b ∼ 10−12 fm, or a mass scale of b−1 ∼ 10^11 GeV ».
- Test n° 1 : `recherche/2026-09-28-grille-lhaaso/resultats.json`, CCF, σ = 0, pire orientation 2,4931583193889674e-27 m.
- Constantes : CODATA 2022 exactes (h, c, e) ; E_Pl = 1,22e19 GeV comme LHAASO et MAGIC.

## Sources examinées mais non retenues

- MAGIC, Mrk 501 (2005), https://arxiv.org/abs/0708.2889v3 : M_QG2 > 0,26e11 GeV (p. 8). Écartée : convention différente (ω = k[1 − k²/(3M²)], soit v = 1 − (E/M)², sans facteur 3/2), intégrale de distance du cas quadratique non précisée (« or similarly for the quadratic case », p. 5), cosmologie non donnée, et retard mesuré non nul (τq = (3.71 ± 2.57)e-6 s/GeV²). Même direction que la source 4, qui la domine de toute façon (0,26e11 × √1,5 = 3,2e10 < 8,5e10).
- H.E.S.S., PG 1553+113, compte rendu https://arxiv.org/abs/1502.02920v2 : remplacé par l'article complet (source 7).
- VERITAS, pulsar du Crabe, https://arxiv.org/abs/1307.8382v1 : compte rendu sans limite n = 2 relevable dans le résumé ; même direction que la source 8 ; non téléchargé.
- Combinaison H.E.S.S./MAGIC/VERITAS, https://arxiv.org/abs/2108.03992v1 : méthode seulement, pas de limite publiée.
