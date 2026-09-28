# Audit infodynamique : sources vérifiées

Relevé le 28 septembre 2026, à la source primaire et non de mémoire. Pour chaque
référence : citation complète, lien, passage vérifié (tel quel, en anglais), usage dans
`texte_fr.md`, statut. Les métadonnées (titre, revue, volume, date, DOI) viennent de
l'API Crossref (`api.crossref.org/works/<doi>`) sauf mention contraire.

Point de départ : une analyse d'un tiers et son script
(`simulation_audit_preuves_2026-09-28.py`), non tenus pour fiables. Chaque affirmation a
été reprise à la source ; les corrections sont signalées en fin de fichier.

## 1. Vopson 2026 (symétrie des polygones)

- M. M. Vopson, « The Role of Information Entropy in Symmetry of Euclidean Polygons »,
  *Entropy* 28(5), article 564, MDPI. Reçu le 25 mars 2026, révisé le 10 mai, accepté le
  15 mai, publié le 18 mai 2026. DOI [10.3390/e28050564](https://doi.org/10.3390/e28050564) ;
  PMC13205927 (<https://pmc.ncbi.nlm.nih.gov/articles/PMC13205927/>). Licence CC BY 4.0.
- Accès : la page PMC renvoie un défi reCAPTCHA aux requêtes automatiques ; le texte
  intégral (XML JATS, équations comprises) a été lu par l'API NCBI E-utilities
  (`efetch.fcgi?db=pmc&id=13205927`).
- Résumé : « Using Lagrange multiplier formalism, we derive the condition for minimum
  entropy in a system of fixed size, showing that it occurs when all elements have equal
  multiplicity. »
- Section 2, équation (5) : \(I = \log_b N - \frac{1}{N}\sum_{i=1}^{n} g_i \log_b g_i\),
  avec la contrainte (3) \(\sum g_i = N\) ; (6) \(f(g_i) = \frac1N \sum g_i\log_b g_i\) ;
  (9) à (13) multiplicateur de Lagrange ; (14) \(g_i = N/n\).
- Section 2, avant (6) : « Examining (5), since 1/N·Σ gi·logb gi > 0, then for a given N
  constant, the minimum I is obtained when the term 1/N·Σ gi·logb gi is maximum. »
- Section 2, après (14) : « Condition (14) indicates that extremal information entropy
  states for fixed N occur when all gi are equal. When n≠1, the minimum information
  entropy is non-zero and the condition is given by (14). »
- Section 2, même article : « While the maximization of Shannon entropy for uniform
  probability distributions is a well-established result in information theory, the
  present analysis focuses specifically on the characterization of the minimum
  attainable information entropy under fixed system size N ».
- Conclusion (section 4) : « Using the method of Lagrange multipliers, we demonstrate
  that the minimum entropy configuration occurs when all elements describing the system
  have equal multiplicity, gi=N/n. »
- Section 3 (polygones) : triangle quelconque « I = 2.585 bits », équilatéral « I = 1
  bit » ; quadrilatère quelconque « I = 3 bits », carré « I = 1 bits » ; pentagone
  quelconque « I = 3.321 bits », régulier « I = 1 bit ». Les côtés et les angles forment
  N = 2m caractères ; le polygone régulier a « only two distinct characters, n = 2,
  X=x1,α1 ».
- Section 1 : l'article se place « within the framework of the second law of information
  dynamics » ; section 4 : « the results should be interpreted as an
  information-theoretic characterization of geometrical symmetry rather than a complete
  physical theory of symmetry formation ».
- Usage : Analyse détaillée, sections 1 et 2 ; `CITE` de `analyse.py`.
- Statut : **vérifiée** (titre, revue, date, DOI, numéros d'équations, citations).
  Remarque : \(\log_2 10 = 3{,}32193\) ; la valeur imprimée 3.321 est tronquée, sans
  conséquence.

## 2. Vopson 2023 (AIP Advances)

- M. M. Vopson, « The second law of infodynamics and its implications for the simulated
  universe hypothesis », *AIP Advances* 13(10), 105308 (octobre 2023, licence CC BY à
  partir du 6 octobre 2023). DOI [10.1063/5.0173278](https://doi.org/10.1063/5.0173278).
- Résumé (Crossref / OUCI) : « we provide scientific evidence that appears to underpin
  the simulated universe hypothesis. »
- Accès : **texte intégral inaccessible** à nos requêtes. `pubs.aip.org` (page et PDF) :
  défi Cloudflare, HTTP 403 ; dépôt de l'université de Portsmouth
  (`researchportal.port.ac.uk/files/80585274/105308_1_5.0173278.pdf`) : même défi ;
  Internet Archive : connexion interrompue. La section « V » et la formulation exacte de
  2023 ne sont donc **pas vérifiées** par nous.
- Ce qui est vérifié : le contenu de la dérivation de 2023, tel que l'auteur le résume
  lui-même en 2025 (source 3) : « the universe does not exchange heat with anything,
  expanding adiabatically » ; « In the original publication, the relation that links
  heat to entropy, dQ = TdS, was used […] it was concluded that dS = 0. This implies that
  the total entropy of the universe must be constant. » ; « It was proposed that the
  missing entropy term is the entropy associated with the information content of the
  universe ».
- Usage : Analyse détaillée, section 3.
- Statut : référence **vérifiée** ; passage de 2023 **invérifiable directement**,
  contenu établi par le résumé de l'auteur.

## 3. Vopson 2025 (réponse)

- M. M. Vopson, « On the Second Law of Infodynamics from Cosmological Thermodynamics »,
  *IPI Letters* 3(1), N6-N9, rubrique « News and Views ». Reçu le 21 octobre 2024,
  accepté le 8 janvier 2025, publié le 10 janvier 2025 (version 2 mise en ligne le
  13 janvier 2025). DOI [10.59973/ipil.137](https://doi.org/10.59973/ipil.137). PDF
  lu : <https://ipipublishing.org/index.php/ipil/article/download/137/91> (4 pages).
- Section 2 : « The main criticism of this approach was the fact that we used the
  relation dQ = TdS = 0, which in reality is only valid for reversible processes. […] The
  condition dQ = 0 still applies, but we can no longer infer that dS = 0, which would
  nullify the requirement for the introduction of the information entropy. »
- Section 3, équations (5) à (9) : « dQPhys + dQInfo = 0 » ;
  « dQPhys = TdSPhys − dU^Loss_Phys » ; « We now assume a similar relation for the
  information process, so: dQInfo = TdSInfo − dU^Loss_Info ».
- Équation (11) : « dSInfo = −dSPhys + dULoss/T ». Équation (12) :
  « dSInfo/dt = −dSPhys/dt + d/dt(dULoss/T) ». Équation (13) : dérivée du quotient.
- Hypothèses énoncées pour (13) : « The second term is always negative or zero, because
  the loss decreases over time, dULoss/dt ≤ 0 » ; « Please note that dULoss is a
  positive quantity, but its rate of change is decreasing » ; « T must decrease over
  time » ; « the positive contribution of the third term can not offset the negative
  contribution of the first two terms, because it scales as 1/T², and the rate of T
  change is also negligible or very small » ; « if we impose T = constant, which is a
  reasonable approximation even over large periods of cosmic time ».
- Conclusion : « Here we managed to demonstrate that the second law of infodynamics is
  derived identically regardless whether a reversible or irreversible process is
  considered. »
- Usage : Analyse détaillée, section 4.
- Statut : **vérifiée** (texte intégral de l'éditeur).

## 4. Détente libre d'un gaz parfait

- MIT, *16 Unified: Thermodynamics and Propulsion*, notes de cours, section 5.5,
  « Calculation of Entropy Change in Some Basic Processes »,
  <https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html>.
- Passages : « For the free expansion: ΔS_system = N R ln(V2/V1); ΔS_surroundings = 0.
  There is no change in the entropy of the surroundings because there is no interaction
  between the system and the surroundings. » ; « ΔS_system > ∫dQ/T = 0; the equality
  between ΔS and dQ/T is only for a reversible process. »
- Usage : Analyse détaillée, section 3.
- Statut : **vérifiée**.

## 5. Constantes

- NIST, CODATA 2022 : constante de Boltzmann « 1.380 649 x 10^-23 J K^-1 », « (exact) » ;
  constante d'Avogadro « 6.022 140 76 x 10^23 mol^-1 », « (exact) » ; constante molaire
  des gaz « 8.314 462 618... J mol^-1 K^-1 », « (exact) ».
  <https://physics.nist.gov/cgi-bin/cuu/Value?k>, `?na`, `?r`.
- Usage : \(R = k_B N_A\) dans `analyse.py`.
- Statut : **vérifiée**.

## 6. Campbell et al.

- T. Campbell, H. Owhadi, J. Sauvageau, D. Watkinson, « On testing the simulation
  theory », arXiv:[1703.00058](https://arxiv.org/abs/1703.00058) (v1 du 28 février 2017,
  v2 du 6 juin 2017, lue). Commentaire arXiv : « final version to appear in IJQF » ; la
  parution dans *International Journal of Quantum Foundations* n'a pas été vérifiée
  (revue absente de Crossref pour ce titre).
- Résumé : « Guided by this principle we describe conceptual wave/particle duality
  experiments aimed at testing the simulation theory. »
- Section 4 : « Although we cannot predict the outcome of the experiments proposed in
  Subsection 4.5 we can rigorously prove that their outcome will be new in comparison to
  classical wave-duality experiments. »
- Usage : Analyse détaillée, section 6 (propositions d'expériences, pas de résultat).
- Statut : **vérifiée** (préprint) ; parution en revue **non vérifiée**. Aucun résultat
  de ces expériences publié à comité de lecture n'a été trouvé (voir aussi
  `recherche/2026-09-28-video-legend/analyse.md`).

## 7. Wolpert

- D. H. Wolpert, « Implications of computer science theory for the simulation
  hypothesis », arXiv:[2404.16050](https://arxiv.org/abs/2404.16050), v1 du 9 avril 2024,
  **v5 du 19 mars 2026** (lue, 62 pages). Parution en revue non vérifiée.
- Résumé (v5) : « I use Kleene's second recursion theorem to prove that it is
  mathematically possible for us to be a simulation that is being run on a computer — by
  us. »
- Section 1.2 : « In particular, in this paper I am only concerned with establishing the
  logical possibility of a physical system V that can (contain a computer that can)
  simulate some universe V′. I do not investigate the possibility of such a system under
  the laws of physics as currently understood — never mind the even more narrowly defined
  question of whether there is such a physical system in our universe ».
- Usage : Analyse détaillée, section 6 (possibilité logique, pas indice).
- Statut : **vérifiée**.

## Corrections apportées à l'analyse du tiers

1. Vopson 2026 : l'objection est **confirmée** (égalité des multiplicités = maximum à N et
   n fixés), avec deux précisions : l'article reconnaît lui-même que la loi uniforme
   maximise l'entropie de Shannon, ce qui le met en contradiction avec sa propre
   conclusion ; et, pour les polygones, la conclusion « polygone régulier = entropie
   minimale » est **juste** mais pour une autre raison (règle de chaîne), l'équation (14)
   n'y jouant aucun rôle. La contrainte géométrique change donc la portée : elle sauve le
   résultat de la section 3, pas le lemme de la section 2.
2. Vopson 2023 : le passage n'a pas pu être lu dans l'article lui-même (accès refusé) ;
   son contenu est établi par le résumé de l'auteur en 2025, qui **reconnaît** l'objection
   (« only valid for reversible processes »).
3. Vopson 2025 : en plus des hypothèses signalées par le tiers, l'équation (12) applique
   \(d/dt\) au seul terme de pertes alors que les deux autres ont été divisés par \(dt\),
   et le texte suppose à la fois « T must decrease over time » et « T = constant ».
4. Script du tiers : `entropy_after` recopiait la formule de `entropy_before` ; corrigé
   (entropie calculée sur la loi des mots de code émis, et exemple avec perte ajouté).
5. Wolpert : la version de mars 2026 est la v5 du 19 mars 2026, confirmée.
