# Le ciel entier dessine-t-il une grille ?

Les rayons cosmiques les plus énergétiques vus par l'observatoire Pierre Auger au sud et par Telescope Array au nord, réunis pour couvrir tout le ciel et confrontés à la trace qu'une grille cubique devrait leur laisser.

<!-- Chaque nombre tiré de resultats.json est suivi de sa clé (chemin dans le JSON,
indices de liste compris) en commentaire HTML ; ceux qui viennent d'une source
publiée renvoient à la section de sources.md. -->

## Verdict

**Non : le ciel entier ne montre aucune trace de grille cubique.** Avec 1 022 <!-- resultats.n_evenements --> rayons cosmiques couvrant toute la sphère céleste, 12 % <!-- resultats.p_valeur_l4 --> des ciels simulés sans grille présentent, après la même recherche, un motif cubique au moins aussi marqué que le vrai ciel.

Ce « non » a une portée précise. Il ne dit pas qu'il n'y a pas de grille : il dit qu'un motif cubique fort est exclu. Un excès de flux de plus d'environ 36 % <!-- limite_superieure_95.toutes_orientations_borne_analytique.exces_axes_max --> le long des axes du cube, ou de plus d'environ 23 % <!-- limite_superieure_95.toutes_orientations_borne_analytique.exces_diagonales_max --> le long de ses diagonales, est exclu à 95 %, quelle que soit l'orientation du cube : c'est environ trois fois <!-- comparaison.gain_pire_orientation_axes --> mieux que le test n° 2. Un contrôle, qui ajoute les événements d'Auger d'énergie plus basse, descend à p = 0,008 <!-- variantes.n_maximal.p_valeur_l4 --> ; nous l'avons suivi jusqu'au bout : il tient pour l'essentiel aux deux excès astrophysiques déjà connus, n'est plus significatif après leur retrait (p = 0,056 <!-- variantes.n_maximal_exces_masques.p_valeur_l4 -->) et ne se reproduit pas de façon significative sur des événements indépendants (voir l'analyse, § 7).

## Explication

Si notre monde était calculé par un ordinateur, l'espace serait peut-être découpé en tout petits cubes, comme une image est faite de pixels. Trois physiciens ont remarqué en 2012 qu'un tel découpage laisserait une trace : les particules les plus énergétiques de l'Univers n'arriveraient pas de la même façon de toutes les directions. Certaines directions seraient favorisées, disposées comme les faces ou comme les coins d'un cube.

Le test n° 2 cherchait cette trace dans les 100 <!-- test2_meme_methode.n_evenements --> particules les plus énergétiques captées par l'observatoire Pierre Auger, en Argentine. Il n'a rien trouvé, mais il avait deux faiblesses : un observatoire de l'hémisphère sud ne voit pas le ciel du grand Nord, et 100 particules ne permettent de voir qu'un motif très fort.

Nous avons donc réuni deux observatoires. Auger, au sud, a publié la liste de ses 2 635 <!-- donnees.auger.n_liste --> particules les plus énergétiques, captées de 2004 à 2020. Telescope Array, dans l'Utah, au nord, a publié la liste de ses 72 <!-- donnees.telescope_array.n --> plus énergétiques, captées de 2008 à 2013. Les deux observatoires ne mesurent pas l'énergie tout à fait de la même façon ; leurs équipes ont publié ensemble la règle qui permet de passer d'une échelle à l'autre. Avec cette règle, nous avons retenu dans la liste d'Auger les particules d'énergie comparable à celles de Telescope Array. Il en reste 950 <!-- resultats.n_auger -->, soit 1 022 <!-- resultats.n_evenements --> au total, dix fois plus qu'au test n° 2, et cette fois sur tout le ciel.

La méthode est celle du test n° 2. On essaie 20 000 <!-- methode.orientations --> positions du cube et l'on garde celle qui colle le mieux aux données. Puis on fabrique 20 000 <!-- methode.ciels_isotropes --> faux ciels sans grille, vus par les mêmes observatoires, et l'on refait exactement la même recherche sur chacun. Dans 12 % <!-- resultats.p_valeur_l4 --> d'entre eux, le meilleur cube colle au moins aussi bien que sur le vrai ciel. Le vrai ciel ne se distingue donc pas des faux ciels : aucune grille n'est détectée.

Nous avons ensuite vérifié que ce résultat ne dépend pas de nos choix : autre règle de conversion des énergies, seulement les particules les plus énergétiques, exposition calculée autrement, et ainsi de suite. Un contrôle sort du lot : quand on ajoute toutes les particules d'Auger d'énergie plus basse, un cube semble coller mieux que presque tous les faux ciels. Nous avons cherché pourquoi, sans rien présumer.

On sait que les rayons cosmiques arrivent en surnombre de deux régions du ciel : l'une autour de la galaxie Centaurus A, vue par Auger, l'autre dans le ciel du nord, vue par Telescope Array. Ce sont des sources astronomiques, pas des cubes. Or, déjà dans l'échantillon principal, le cube qui colle le mieux place justement deux de ses coins à une dizaine de degrés de ces deux régions. Quand on retire ces deux régions du ciel, le motif s'affaiblit nettement et n'est plus significatif. Surtout, une vraie grille devrait se retrouver, avec la même orientation, dans des lots de particules différents. Nous avons choisi le meilleur cube sur les seules particules de basse énergie, puis regardé s'il colle aussi aux autres, qui n'ont servi à rien dans ce choix : il colle un peu, mais pas assez pour sortir du hasard, et encore moins une fois les deux régions retirées. Enfin, la prédiction porte sur les particules les plus énergétiques, les moins déviées en chemin ; c'est l'inverse qu'on observe, le motif venant des moins énergétiques. Ce contrôle ne montre donc pas une grille, mais surtout ces deux amas de particules, que le cube le plus proche essayait d'attraper.

Ce que ce test montre : là où l'on pouvait regarder, c'est-à-dire sur tout le ciel et avec dix fois plus de particules, il n'y a pas de motif cubique fort. Ce qu'il ne montre pas : qu'il n'y a aucune grille. Un motif faible passerait encore inaperçu, et les champs magnétiques de notre galaxie dévient ces particules en chemin, ce qui brouillerait une partie de la trace.

## Analyse détaillée

### 1. La prédiction

Sur un réseau cubique, tout effet de la grille sur les directions d'arrivée est une fonction de la direction \(\mathbf n\) invariante par le groupe du cube \(O_h\). Les harmoniques sphériques invariantes par \(O_h\) n'existent que pour \(\ell=0,4,6,8,\dots\) : la première anisotropie permise est l'harmonique cubique \(\ell=4\), proportionnelle à \(Q-3/5\), avec

$$Q(\mathbf n)=\sum_{i=1}^{3}n_i^{4}.$$

Beane, Davoudi et Savage (arXiv:1210.1847) écrivent qu'une simulation sur réseau pourrait se révéler dans les rayons cosmiques de plus haute énergie par une brisure de la symétrie de rotation reflétant la grille. Test principal fixé d'avance : \(\ell=4\) ; tests secondaires : \(\ell=6\) et \(\ell=4+6\). Méthode, statistique, orientations et graine sont celles du test n° 2.

### 2. Les données

**Sud.** Pierre Auger Collaboration, ApJ 935, 170 (2022) : liste publique complète des 2 635 <!-- donnees.auger.n_liste --> événements d'énergie supérieure ou égale à 32 EeV <!-- donnees.auger.energie_min_liste_EeV --> (du 1er janvier 2004 au 31 décembre 2020, zénith jusqu'à 80°), dont 2 040 <!-- donnees.auger.n_verticaux_liste --> « verticaux » (zénith \(\lt\) 60°) et les autres « inclinés » (60° à 80°), chiffres identiques à ceux de l'article (sources.md, § 2). Énergie maximale : 165,5 EeV <!-- donnees.auger.energie_max_EeV -->. Les 100 événements du test n° 2 sont tous dans cette liste (vérifié, sources.md, § 2).

**Nord.** Telescope Array Collaboration, ApJL 790, L21 (2014), tableau 1 : les 72 <!-- donnees.telescope_array.n --> événements d'énergie supérieure à 57 EeV <!-- etalonnage.seuil_TA_EeV --> et de zénith \(\lt\) 55°, du 11 mai 2008 au 4 mai 2013, de 57,3 <!-- donnees.telescope_array.energie_min_EeV --> à 162,2 EeV <!-- donnees.telescope_array.energie_max_EeV -->, déclinaisons jusqu'à −4,78° <!-- donnees.telescope_array.declinaison_min_deg --> vers le sud. C'est la seule liste d'événements de Telescope Array publiée avec leurs coordonnées (sources.md, § 1) ; les jeux plus récents utilisés dans les analyses communes Auger-TA ne sont pas publics.

Les empreintes SHA-256 de tous les fichiers sont vérifiées à chaque exécution. La table de Telescope Array étant sous droits de l'éditeur, elle n'est pas redistribuée : le script la télécharge et contrôle l'empreinte du fichier et celle de la liste lue (sources.md, § 3).

### 3. Mettre les deux énergies sur la même échelle

Le groupe de travail commun Auger-TA recale les énergies en comparant les flux dans la bande de ciel vue par les deux observatoires :

$$\frac{E_{\mathrm{Auger}}}{10\ \mathrm{EeV}}=e^{\alpha}\left(\frac{E_{\mathrm{TA}}}{10\ \mathrm{EeV}}\right)^{\beta},$$

avec \(\alpha=-0{,}159\) <!-- etalonnage.principal.alpha --> et \(\beta=0{,}954\) <!-- etalonnage.principal.beta -->, valeurs publiées précisément pour cette sélection de Telescope Array (arXiv:2507.10441, p. 3 ; sources.md, § 5). Le seuil de 57 EeV de Telescope Array équivaut donc à 44,88 EeV <!-- etalonnage.seuil_Auger_equivalent_EeV --> sur l'échelle d'Auger. L'échantillon principal réunit les événements Auger d'au moins cette énergie et les 72 événements TA :

| Lot | Latitude | Zénith | Événements |
|---|---|---|---|
| Auger vertical | −35,2° <!-- methode.lots.0.latitude_deg --> | 0-60° | 725 <!-- resultats.n_auger_verticaux --> |
| Auger incliné | −35,2° <!-- methode.lots.1.latitude_deg --> | 60-80° | 225 <!-- resultats.n_auger_inclines --> |
| Telescope Array | 39,30° <!-- methode.lots.2.latitude_deg --> | 0-55° | 72 <!-- resultats.n_ta --> |
| Total | | | 1 022 <!-- resultats.n_evenements --> |

### 4. L'exposition, lot par lot

Un détecteur au sol à la latitude \(a_0\), acceptant les zéniths \(\theta\le\theta_m\), a une exposition uniforme en ascension droite et, en déclinaison \(\delta\) (Sommers, 2001),

$$\omega_{\theta_m}(\delta)\propto\cos a_0\cos\delta\,\sin\alpha_m+\alpha_m\sin a_0\sin\delta,\qquad \alpha_m=\arccos\left(\mathrm{clip}_{[-1,1]}\,\frac{\cos\theta_m-\sin a_0\sin\delta}{\cos a_0\cos\delta}\right).$$

Pour une bande de zénith \([\theta_1,\theta_2]\), \(\omega=\omega_{\theta_2}-\omega_{\theta_1}\). À ces énergies, l'efficacité de détection est totale et l'exposition purement géométrique (arXiv:1404.5890 p. 6 pour TA ; code d'exposition d'Auger publié avec les données ; sources.md, § 2 et 3).

Chaque lot \(d\) garde son exposition \(\omega_d\) et son nombre d'événements \(N_d\) est tenu fixe dans les simulations : on conditionne sur lui, comme Auger le fait pour ses lots vertical et incliné. Le test ne dépend alors ni des expositions absolues des deux observatoires, ni de l'écart d'échelle d'énergie au-delà du choix des seuils. Auger voit jusqu'à la déclinaison +44,8° <!-- methode.declinaison_max_Auger_deg -->, Telescope Array jusqu'à −15,7° <!-- methode.declinaison_min_TA_deg --> : le ciel entier est couvert (fraction visible 1 <!-- methode.fraction_du_ciel_visible -->, contre 85 % <!-- test2_meme_methode.fraction_du_ciel_visible --> au test n° 2) ; 49 % <!-- methode.fraction_du_ciel_vue_par_les_deux --> de la sphère est vue par les deux, 15 % <!-- methode.fraction_du_ciel_vue_par_TA_seul --> par Telescope Array seul.

### 5. La statistique

Soit \(R\) une orientation de la grille, de lignes \(\mathbf e_k\), et \(f(R\mathbf n)=\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\). Étendue aux lots :

$$T(R)=\frac{\sum_{i=1}^{N}f(R\mathbf n_i)-\sum_d N_d\,\langle f\rangle_{\omega_d}}{\sqrt{\sum_d N_d\,\mathrm{Var}_{\omega_d} f}},\qquad Z_4=\max_R\,\lvert T(R)\rvert,$$

où \(\langle\cdot\rangle_{\omega_d}\) est la moyenne sur un ciel isotrope vu par le lot \(d\), calculée exactement par quadrature de Gauss-Legendre sur les 15 monômes de degré 4. \(T\gt0\) signale un excès le long des axes du cube, \(T\lt0\) le long de ses diagonales. Le maximum porte sur les 20 000 <!-- methode.orientations --> orientations du test n° 2 (même graine, 20260928 <!-- methode.graine -->). Pour \(\ell=6\) : \(f_6=\sum_k(\mathbf e_k\cdot\mathbf n)^{6}+\alpha_6\sum_k(\mathbf e_k\cdot\mathbf n)^{4}\), avec \(\alpha_6=-15/11\approx-1{,}364\) <!-- methode.fonction_l6_alpha -->, orthogonale à \(\ell=4\) ; le test combiné maximise \(T_4^{2}+T_6^{2}\).

La p-valeur, \((1+\#\{Z\ge Z_{\mathrm{obs}}\})/(1+n)\), vient de \(n\) = 20 000 <!-- methode.ciels_isotropes --> ciels isotropes tirés lot par lot, soumis à la même maximisation : elle inclut le coût du choix de l'orientation. Sous isotropie, \(Z_4\) a pour médiane 2,46 <!-- resultats.seuils_Z4_isotrope.0.5 --> ; il dépasse 3,58 <!-- resultats.seuils_Z4_isotrope.0.95 --> dans 5 % des cas, 4,09 <!-- resultats.seuils_Z4_isotrope.0.99 --> dans 1 % et 4,62 <!-- resultats.seuils_Z4_isotrope.0.999 --> dans 0,1 %.

### 6. Résultat

| Test | Statistique observée | p-valeur |
|---|---|---|
| \(\ell=4\) (principal) | \(Z_4\) = 3,24 <!-- resultats.Z4_observe --> | 0,122 <!-- resultats.p_valeur_l4 --> |
| \(\ell=6\) | \(Z_6\) = 2,94 <!-- resultats.Z6_observe --> | 0,385 <!-- resultats.p_valeur_l6 --> |
| \(\ell=4\) et \(\ell=6\) | \(\max(T_4^{2}+T_6^{2})\) = 16,4 <!-- resultats.Z46_observe --> | 0,079 <!-- resultats.p_valeur_l4_l6 --> |

Aucun test ne descend sous 0,05. À la meilleure orientation, \(T_4\) = −3,24 <!-- resultats.meilleure_orientation_T4 --> : l'écart va vers les diagonales. La moyenne de \(Q\) y vaut 0,5886 <!-- resultats.Q_moyen_observe --> contre 0,6065 <!-- resultats.Q_moyen_attendu_isotrope --> attendu, soit −2,9 % <!-- resultats.ecart_relatif_Q -->. Cette orientation est à 49,9° <!-- resultats.meilleure_orientation_ecart_au_test2_deg --> (au groupe du cube près) de la meilleure orientation du test n° 2 : la « meilleure grille » n'est pas stable d'un échantillon à l'autre, ce qu'on attend du bruit.

Lot par lot, à cette même orientation : \(T_4\) = −2,46 <!-- resultats.T4_par_lot_meilleure_orientation.Auger vertical --> pour Auger vertical, −0,35 <!-- resultats.T4_par_lot_meilleure_orientation.Auger incliné --> pour Auger incliné, −3,78 <!-- resultats.T4_par_lot_meilleure_orientation.Telescope Array --> pour Telescope Array. Ces valeurs sont prises à l'orientation choisie sur l'ensemble : elles ne sont pas des tests indépendants.

**D'où vient l'écart ?** Dans des cônes de 30° <!-- methode.rayon_cones_deg --> autour des huit diagonales de la meilleure orientation, on observe 574 <!-- resultats.cones_meilleure_orientation.diagonales.observe_total --> événements pour 533,9 <!-- resultats.cones_meilleure_orientation.diagonales.attendu_total --> attendus. L'excès se concentre dans deux cônes : 148 <!-- resultats.cones_meilleure_orientation.diagonales.cones.5.observe --> observés pour 111,5 <!-- resultats.cones_meilleure_orientation.diagonales.cones.5.attendu --> attendus autour de la diagonale pointant vers (215,0° ; −45,8°) <!-- resultats.cones_meilleure_orientation.diagonales.cones.5.ra_deg, .dec_deg -->, à 10,1° <!-- resultats.cones_meilleure_orientation.diagonales.cones.5.distance_centaurus_a_deg --> de Centaurus A ; 36 <!-- resultats.cones_meilleure_orientation.diagonales.cones.3.observe --> pour 28,6 <!-- resultats.cones_meilleure_orientation.diagonales.cones.3.attendu --> autour de (135,6° ; 37,4°) <!-- resultats.cones_meilleure_orientation.diagonales.cones.3.ra_deg, .dec_deg -->, à 10,3° <!-- resultats.cones_meilleure_orientation.diagonales.cones.3.distance_point_chaud_ta_deg --> du point chaud de Telescope Array. Les six autres diagonales ne montrent rien de tel. Ce sont les deux excès astrophysiques publiés par les collaborations elles-mêmes : autour de Centaurus A, 215 événements observés pour 152,0 attendus dans un cercle de 27° au-dessus de 38 EeV (arXiv:2206.13492 p. 11) <!-- sources.md § 2 --> ; le point chaud de TA, 19 observés pour 4,49 attendus dans un cercle de 20° (arXiv:1404.5890 p. 7) <!-- sources.md § 3 et § 7 -->.

### 7. Contrôles

Neuf variantes fixées avant le calcul (10 000 <!-- methode.ciels_par_variante --> ciels isotropes chacune), puis quatre ajoutées après coup, et signalées comme telles, pour comprendre la variante « N maximal » :

| Variante | N | \(Z_4\) | p (\(\ell=4\)) |
|---|---|---|---|
| Principale | 1 022 <!-- resultats.n_evenements --> | 3,24 <!-- resultats.Z4_observe --> | 0,122 <!-- resultats.p_valeur_l4 --> |
| Auger seul, même seuil | 950 <!-- variantes.auger_seul.n_evenements --> | 2,63 <!-- variantes.auger_seul.Z4_observe --> | 0,398 <!-- variantes.auger_seul.p_valeur_l4 --> |
| Plus hautes énergies (Auger ≥ 78 EeV, TA ≥ 101,7 EeV <!-- etalonnage.seuil_TA_equivalent_a_78_EeV_Auger -->) | 113 <!-- variantes.hautes_energies.n_evenements --> | 3,15 <!-- variantes.hautes_energies.Z4_observe --> | 0,148 <!-- variantes.hautes_energies.p_valeur_l4 --> |
| Étalonnage ICRC 2021 (seuil Auger 43,78 EeV <!-- etalonnage.seuils_Auger_selon_etalonnage_EeV.icrc2021 -->) | 1 102 <!-- variantes.etalonnage_icrc2021.n_evenements --> | 3,14 <!-- variantes.etalonnage_icrc2021.Z4_observe --> | 0,148 <!-- variantes.etalonnage_icrc2021.p_valeur_l4 --> |
| Étalonnage ICRC 2025 strict (seuil 45,92 EeV <!-- etalonnage.seuils_Auger_selon_etalonnage_EeV.icrc2025_strict -->) | 934 <!-- variantes.etalonnage_icrc2025_strict.n_evenements --> | 3,12 <!-- variantes.etalonnage_icrc2025_strict.Z4_observe --> | 0,161 <!-- variantes.etalonnage_icrc2025_strict.p_valeur_l4 --> |
| Exposition Auger d'un seul bloc | 1 022 <!-- variantes.auger_un_bloc.n_evenements --> | 3,24 <!-- variantes.auger_un_bloc.Z4_observe --> | 0,120 <!-- variantes.auger_un_bloc.p_valeur_l4 --> |
| Avec l'événement Amaterasu (244 EeV, 2021) | 1 023 <!-- variantes.avec_amaterasu.n_evenements --> | 3,23 <!-- variantes.avec_amaterasu.Z4_observe --> | 0,120 <!-- variantes.avec_amaterasu.p_valeur_l4 --> |
| Centaurus A et point chaud TA retirés | 865 <!-- variantes.exces_masques.n_evenements --> | 1,97 <!-- variantes.exces_masques.Z4_observe --> | 0,796 <!-- variantes.exces_masques.p_valeur_l4 --> |
| Sans correction d'échelle (Auger ≥ 57 EeV) | 483 <!-- variantes.sans_correction.n_evenements --> | 3,69 <!-- variantes.sans_correction.Z4_observe --> | 0,033 <!-- variantes.sans_correction.p_valeur_l4 --> |
| N maximal (Auger ≥ 32 EeV, TA > 57 EeV) | 2 707 <!-- variantes.n_maximal.n_evenements --> | 4,15 <!-- variantes.n_maximal.Z4_observe --> | 0,008 <!-- variantes.n_maximal.p_valeur_l4 --> |
| *Après coup :* N maximal, Auger seul | 2 635 <!-- variantes.n_maximal_auger_seul.n_evenements --> | 3,93 <!-- variantes.n_maximal_auger_seul.Z4_observe --> | 0,017 <!-- variantes.n_maximal_auger_seul.p_valeur_l4 --> |
| *Après coup :* N maximal, excès retirés | 2 359 <!-- variantes.n_maximal_exces_masques.n_evenements --> | 3,55 <!-- variantes.n_maximal_exces_masques.Z4_observe --> | 0,056 <!-- variantes.n_maximal_exces_masques.p_valeur_l4 --> |
| *Après coup :* Auger 32 à 44,88 EeV seul | 1 685 <!-- variantes.auger_32_a_seuil.n_evenements --> | 3,63 <!-- variantes.auger_32_a_seuil.Z4_observe --> | 0,045 <!-- variantes.auger_32_a_seuil.p_valeur_l4 --> |
| *Après coup :* Auger 32 à 44,88 EeV, excès retirés | 1 494 <!-- variantes.auger_32_a_seuil_exces_masques.n_evenements --> | 3,19 <!-- variantes.auger_32_a_seuil_exces_masques.Z4_observe --> | 0,137 <!-- variantes.auger_32_a_seuil_exces_masques.p_valeur_l4 --> |

Deux variantes prévues descendent sous 0,05 : « sans correction » (0,033 <!-- variantes.sans_correction.p_valeur_l4 -->) et surtout « N maximal » (0,008 <!-- variantes.n_maximal.p_valeur_l4 -->). Nous les avons creusées ; aucune ne met en cause le verdict.

1. **Ce sont des contrôles, pas le test.** Le test principal a été fixé d'avance. Sur neuf variantes prévues, la probabilité qu'au moins une descende à 0,008 par hasard est bornée par \(9\times0{,}008\approx0{,}07\) (Bonferroni) ; les variantes, très corrélées entre elles, rendent cette borne prudente sans la rendre fausse.
2. **Le signal vient des énergies les plus basses, et du sud.** Auger seul, dès 32 EeV, donne déjà p = 0,017 <!-- variantes.n_maximal_auger_seul.p_valeur_l4 --> ; les seuls événements Auger de 32 à 44,88 EeV, absents de l'échantillon principal, donnent p = 0,045 <!-- variantes.auger_32_a_seuil.p_valeur_l4 -->. Aux plus hautes énergies, là où la prédiction de Beane, Davoudi et Savage porte et où les déviations magnétiques sont les plus faibles, rien : p = 0,148 <!-- variantes.hautes_energies.p_valeur_l4 -->. Une grille donnerait le profil inverse.
3. **Il suit les excès connus.** Centaurus A et le point chaud TA retirés, avec les cercles publiés par les collaborations : « N maximal » remonte à p = 0,056 <!-- variantes.n_maximal_exces_masques.p_valeur_l4 -->, la tranche 32-44,88 EeV à p = 0,137 <!-- variantes.auger_32_a_seuil_exces_masques.p_valeur_l4 -->, l'échantillon principal à p = 0,796 <!-- variantes.exces_masques.p_valeur_l4 -->.
4. **Il ne se reproduit pas de façon significative.** Test de reproduction : on choisit la meilleure orientation sur les seuls événements Auger de 32 à 44,88 EeV (\(T_4\) = −3,63 <!-- apres_coup.reproduction_par_energie.sans_masque.T4_choix -->), puis on calcule \(T_4\) à cette orientation fixée dans l'échantillon principal, qui ne partage aucun événement avec eux. À orientation fixée, \(T_4\) suit une loi normale centrée réduite sous isotropie (autotest). On obtient \(T_4\) = −1,92 <!-- apres_coup.reproduction_par_energie.sans_masque.T4_echantillon_principal_meme_orientation -->, soit p = 0,055 <!-- apres_coup.reproduction_par_energie.sans_masque.p_bilaterale_normale --> (bilatéral) : même signe, mais pas significatif. Excès retirés : \(T_4\) = −1,49 <!-- apres_coup.reproduction_par_energie.exces_masques.T4_echantillon_principal_meme_orientation -->, p = 0,136 <!-- apres_coup.reproduction_par_energie.exces_masques.p_bilaterale_normale -->. La faible concordance qui subsiste est compatible avec une même anisotropie astrophysique vue à deux énergies voisines.
5. **Un dipôle n'explique pas tout, et ce n'est pas nécessaire.** Nous avons aussi simulé des ciels portant le dipôle ajusté aux données, plutôt que des ciels isotropes (amplitude 0,137 <!-- apres_coup.nul_dipolaire.n_maximal.amplitude --> pour « N maximal ») : la p-valeur ne change presque pas, 0,006 <!-- apres_coup.nul_dipolaire.n_maximal.p_valeur_l4_sous_dipole --> (0,120 <!-- apres_coup.nul_dipolaire.principal.p_valeur_l4_sous_dipole --> pour le test principal). L'anisotropie qui compte ici n'est pas l'anisotropie à grande échelle, mais les excès à échelle intermédiaire de Centaurus A et du point chaud, dont le retrait fait remonter toutes les p-valeurs au-dessus de 0,05.
6. **« Sans correction »** compare Auger au-dessus de 57 EeV de son échelle à TA au-dessus de 57 EeV de la sienne, alors que l'étalonnage commun fait correspondre 57 EeV de TA à 44,88 EeV <!-- etalonnage.seuil_Auger_equivalent_EeV --> d'Auger : le rapport des flux entre le nord et le sud est alors faussé. Avec les trois étalonnages publiés que nous avons testés, p reste entre 0,122 <!-- resultats.p_valeur_l4 --> et 0,161 <!-- variantes.etalonnage_icrc2025_strict.p_valeur_l4 -->.

Bilan : le seul écart notable des contrôles est porté par des événements de plus basse énergie, se concentre près des deux excès astrophysiques connus, s'efface quand on les retire et ne se reproduit pas de façon significative sur un échantillon indépendant. Ce n'est pas la signature d'une grille.

### 8. Ce que le test pouvait voir

On injecte un motif cubique : densité proportionnelle à \(\omega_d(\delta)\left[1+\varepsilon\,(5Q(R\mathbf n)-3)/2\right]\). Le long d'un axe (\(Q=1\)) le flux vaut \(1+\varepsilon\) fois la moyenne ; le long d'une diagonale (\(Q=1/3\)), \(1-2\varepsilon/3\). Avec \(\varepsilon\gt0\), l'excès porte sur les axes ; avec \(\varepsilon\lt0\), sur les diagonales, et il vaut \(2\lvert\varepsilon\rvert/3\). Limites supérieures à 95 %, trois conventions :

| Convention | Axes : \(\varepsilon\le\) | Diagonales : \(\lvert\varepsilon\rvert\le\) | Test n° 2, même convention (axes / diagonales) |
|---|---|---|---|
| Orientation tirée au hasard pour chaque ciel (1 000 <!-- methode.ciels_par_amplitude --> ciels par amplitude) | 0,321 <!-- limite_superieure_95.moyenne_orientations.epsilon_axes_max --> | 0,319 <!-- limite_superieure_95.moyenne_orientations.epsilon_diagonales_max --> | 0,955 <!-- test2_meme_methode.limite_moyenne_axes --> / 0,916 <!-- test2_meme_methode.limite_moyenne_diagonales --> |
| Pire de 16 orientations fixes, dont la moins visible (400 <!-- methode.ciels_par_amplitude_orientation_fixe --> ciels par point) | 0,330 <!-- limite_superieure_95.pire_orientation_fixe_epsilon_axes_max --> | 0,319 <!-- limite_superieure_95.pire_orientation_fixe_epsilon_diagonales_max --> | 1,036 <!-- test2_meme_methode.pire_16_orientations_axes --> / 0,929 <!-- test2_meme_methode.pire_16_orientations_diagonales --> |
| Pire des 20 000 orientations, borne analytique | 0,356 <!-- limite_superieure_95.toutes_orientations_borne_analytique.axes.pire --> | 0,347 <!-- limite_superieure_95.toutes_orientations_borne_analytique.diagonales.pire --> | 1,081 <!-- test2_meme_methode.borne_toutes_orientations.axes.pire --> / 0,992 <!-- test2_meme_methode.borne_toutes_orientations.diagonales.pire --> |

La borne analytique repose sur \(Z_4\ge\lvert T(R_0)\rvert\) : si le ciel porte le motif à l'orientation \(R_0\), il suffit que \(\lvert T(R_0)\rvert\) dépasse \(Z_4^{\mathrm{obs}}\) avec une probabilité d'au moins 95 %. \(T(R_0)\) est une somme de \(N\) termes indépendants, de loi normale à très bonne approximation, dont la moyenne et la variance sous le signal se calculent exactement :

$$\mathbb E_\varepsilon[f]_d=\frac{\langle f\rangle_{\omega_d}+\varepsilon\,\langle f g\rangle_{\omega_d}}{1+\varepsilon\,\langle g\rangle_{\omega_d}},\qquad g=\frac{5Q(R_0\mathbf n)-3}{2},$$

et de même pour \(\mathbb E_\varepsilon[f^{2}]_d\). La borne est conservatrice (elle ignore le gain du maximum) : pour chacune des 16 orientations fixes, elle est au-dessus de la limite simulée. Autotest : à \(\varepsilon=0{,}3\) et à une orientation donnée, moyenne analytique 4,192 <!-- autotests.borne_contre_MC.0.3.moyenne_analytique --> contre 4,187 <!-- autotests.borne_contre_MC.0.3.moyenne_MC --> simulée.

En flux : **un excès de plus d'environ 36 % <!-- limite_superieure_95.toutes_orientations_borne_analytique.exces_axes_max --> le long des axes, ou de plus d'environ 23 % <!-- limite_superieure_95.toutes_orientations_borne_analytique.exces_diagonales_max --> le long des diagonales, est exclu à 95 % pour toute orientation.** Le gain sur le test n° 2 est d'un facteur 3,0 <!-- comparaison.gain_pire_orientation_axes --> vers les axes et 2,9 <!-- comparaison.gain_pire_orientation_diagonales --> vers les diagonales, pour 10,2 <!-- comparaison.rapport_N --> fois plus d'événements, proche du facteur \(\sqrt{10{,}2}\approx3{,}2\) attendu d'une sensibilité en \(1/\sqrt N\).

### 9. Autotests

Le script vérifie d'abord sa propre chaîne : effectifs et bornes publiés des deux listes ; correspondances d'énergie imprimées dans les quatre articles d'étalonnage ; invariance de \(Q\) par le groupe du cube et développement polynomial exact ; \(\ell=6\) orthogonal à \(\ell=4\) ; limites des ciels visibles (Auger +44,8°, TA −15,7°) et somme des bandes vertical et incliné ; accord entre quadrature et grands tirages, masques compris ; \(T\) centré réduit sous isotropie ; moments analytiques égaux au Monte-Carlo ; enfin un motif cubique franc injecté sur tout le ciel est détecté et son orientation retrouvée à 3,1° <!-- autotests.orientation_retrouvee_ecart_deg --> près.

## Limites

- Les rayons cosmiques sont chargés : les champs magnétiques dévient leurs directions, d'autant plus que les noyaux sont lourds. Le motif cherché est large (un axe et une diagonale sont séparés de \(\arccos(1/\sqrt3)\approx54{,}7^\circ\)) et résiste à des déviations modestes, mais une empreinte fixée à la source ou en chemin serait en partie effacée.
- Le nord pèse peu : 72 <!-- resultats.n_ta --> événements TA contre 950 <!-- resultats.n_auger --> pour Auger. La seule liste de Telescope Array publiée avec coordonnées s'arrête en 2013 ; les jeux plus riches des analyses communes ne sont pas publics.
- L'étalonnage croisé des énergies a une incertitude : chaque observatoire annonce ±14 % (Auger) et ±21 % (TA) sur son échelle absolue (arXiv:2507.10441 p. 3) <!-- sources.md § 5 -->. Les variantes d'étalonnage publiées ne changent pas le résultat ; l'absence de toute correction le change (p = 0,033 <!-- variantes.sans_correction.p_valeur_l4 -->), pour la raison donnée au § 7.
- Les anisotropies astrophysiques (excès de Centaurus A et du point chaud TA, et plus généralement toute anisotropie à grande échelle) projettent en partie sur \(\ell=4\) à travers des expositions non uniformes. Le test n'en modélise aucune ; il ne les retire que dans les variantes à excès masqués, avec les cercles publiés par les collaborations, non ajustés par nous. Un résultat positif aurait exigé de les exclure ; le verdict négatif n'en dépend pas.
- Quatre variantes, le test de reproduction et les ciels à dipôle ont été ajoutés après avoir vu la variante « N maximal » ; ils servent à l'expliquer, pas à construire le verdict. Le test de reproduction reste faible : l'échantillon principal ne compte que 1 022 <!-- resultats.n_evenements --> événements.
- L'écart de la variante « N maximal » n'est pas expliqué par un modèle physique complet : nous montrons qu'il suit les excès connus et qu'il ne se reproduit pas, sans modéliser ces excès eux-mêmes.
- La grille est supposée fixe par rapport aux étoiles lointaines. Une grille en mouvement ou en rotation par rapport à elles demanderait un autre test.
- Aucune probabilité d'être simulés n'est calculée : le test porte sur une signature précise, celle d'une grille cubique.

## Fichiers

- `recherche/2026-09-28-ciel-complet/analyse.py` : le script (Python ≥ 3.10, numpy) ; `python3 analyse.py --out resultats.json`, graine fixe, résultats identiques d'une exécution à l'autre.
- `recherche/2026-09-28-ciel-complet/resultats.json` : toutes les valeurs calculées.
- `recherche/2026-09-28-ciel-complet/sources.md` : source, page et licence de chaque donnée et de chaque paramètre d'entrée.
- `recherche/2026-09-28-ciel-complet/donnees/AugerApJS2022_Yr_JD_UTC_Th_Ph_RA_Dec_E_Expo.dat` : les 2 635 événements d'Auger (Pierre Auger Collaboration, DOI 10.5281/zenodo.6504276, licence CC BY-SA 4.0).
- `recherche/2026-09-28-ciel-complet/donnees/tasd_highest_event_244EeV_backtrack_JF_PT_eq.dat` : l'événement Amaterasu (Telescope Array Collaboration, DOI 10.5281/zenodo.8427755, licence CC BY 4.0).
- Table des 72 événements de Telescope Array : non redistribuée (© AAS) ; téléchargée par `analyse.py` depuis le site de l'éditeur (ou, en secours, depuis la source arXiv:1404.5890v3), empreintes SHA-256 vérifiées.

## Sources

- S. R. Beane, Z. Davoudi, M. J. Savage, « Constraints on the Universe as a Numerical Simulation », arXiv:1210.1847 (2012).
- Pierre Auger Collaboration, « Arrival Directions of Cosmic Rays above 32 EeV from Phase One of the Pierre Auger Observatory », ApJ 935, 170 (2022), arXiv:2206.13492 ; données DOI 10.5281/zenodo.6504276.
- Telescope Array Collaboration, « Indications of Intermediate-Scale Anisotropy of Cosmic Rays with Energy Greater Than 57 EeV in the Northern Sky », ApJL 790, L21 (2014), arXiv:1404.5890.
- Telescope Array Collaboration, « An extremely energetic cosmic ray observed by a surface detector array », Science 382, 903 (2023), arXiv:2311.14231 ; données DOI 10.5281/zenodo.8427755.
- A. Gálvez Ureña pour les collaborations Auger et TA, ICRC 2025, arXiv:2507.10441 ; A. di Matteo et al., ICRC 2021, arXiv:2111.12366 ; rapport UHECR 2022, arXiv:2302.04502.
- P. Sommers, « Cosmic Ray Anisotropy Analysis with a Full-Sky Observatory », Astropart. Phys. 14, 271 (2001), arXiv:astro-ph/0004016.
