# Correction du 29 septembre 2026

Le scénario à environ 7 % n’est plus une estimation d’Aeternam. Les lois a priori sont arbitraires ; les résultats sont des analyses de sensibilité conditionnelles.

Les passages ci-dessous conservent le relevé documentaire et le raisonnement antérieur pour traçabilité. En cas de conflit, le script actuel, ses résultats régénérés et le [rapport d’audit](../../AUDIT-SCIENTIFIQUE.md) font foi.

---

# Synthèse : sources vérifiées

Relevé le 28 septembre 2026, à la source primaire et non de mémoire : métadonnées
déposées par l'éditeur (API Crossref, `api.crossref.org/works/<doi>`), pages et PDF
d'arXiv, PDF des éditeurs en accès libre (Frontiers), versions des auteurs
(consc.net, simulation-argument.com), dépôts institutionnels (LSE Research Online,
Oxford Research Archive). Les sites d'OUP, Wiley, Springer, MDPI, AIP et PhilPapers
refusent l'accès automatisé (403 ou défi JavaScript) ; pour ces articles, le texte
vient de la version de l'auteur ou du dépôt institutionnel, et les métadonnées de
Crossref.

Pour chaque référence : citation complète, lien, passage vérifié (tel quel, en
anglais), usage dans `texte_fr.md`, statut. Les pages sont celles du document
consulté, précisé à chaque fois.

## Bilan des références demandées

| Référence demandée | Statut |
|---|---|
| Chalmers, *Reality+* (2022) | vérifiée |
| Chalmers, « The Matrix as Metaphysics » | vérifiée ; 2005 selon l'auteur, notice Crossref datée du 1ᵉʳ septembre 2004 |
| Chalmers 1995 / 1996 (qualia évanescents) | vérifiées |
| Searle 1980 (chambre chinoise) | vérifiée |
| Mogensen, fin 2025, contre l'argument des qualia évanescents | **existe** : *Synthese* 206, 252, en ligne le 5 novembre 2025 ; vérifiée |
| Lloyd, *Nature* 2000 ; *PRL* 2002 | vérifiées |
| Vazza 2025 | vérifiée ; référence exacte : *Front. Phys.* 13, 1561873, 17 avril 2025 |
| Commentaire « Edge et Brown » (2026) | **existe** : *Front. Phys.* 14, 1808725, 21 avril 2026 ; vérifié |
| Bibeau-Delisle et Brassard, *Proc. R. Soc. A* 2021 | vérifiée |
| Birch, *Erkenntnis* 2013 | vérifiée (en ligne 2012, numéro 78(1) de 2013) |
| Bostrom, *Philosophical Quarterly* 2003 | vérifiée ; **titre corrigé** : la version publiée s'intitule « Are We Living in a Computer Simulation? » |
| Hartle et Srednicki, « Are we typical? », *PRD* 2007 | vérifiée |
| Kipping, *Universe* 2020 | vérifiée ; équations relevées dans la version arXiv, identique à la version publiée selon l'auteur |
| Hensen et al., Giustina et al., Shalm et al. (2015) | vérifiées |
| Zurek, *RMP* 2003 | vérifiée |
| Jacques et al., *Science* 2007 ; « Ma et al. » | vérifiées ; pour « Ma et al. », retenu Ma, Kofler, Zeilinger, *RMP* 88, 015005 (2016) |
| Barnes, *PASA* 2012 | vérifiée |
| Beane, Davoudi, Savage 2012 | vérifiée (arXiv 2012, *EPJA* 50, 148, 2014) |

Références ajoutées, parce que la vérification les rendait nécessaires : Bostrom 2005
(réponse à Weatherson), Bostrom et Kulczycki 2011, FAQ de Bostrom (2025), Weatherson
2003, Faizal et al. 2025, 't Hooft 2016, Vopson 2019, 2022, 2023 et 2025.

Références retirées : **aucune**. Toutes les références demandées existent et disent
ce que le texte leur attribue.

## Points relevés en vérifiant

1. **Bostrom 2003, note 10** (version de l'auteur, p. 6) : « 100 billion humans × 50
   years/human × 30 million secs/year × [10^14, 10^17] operations in each human brain
   per second ≈ [10^33, 10^36] operations. » Le produit des facteurs vaut
   1,5 × 10³⁴ à 1,5 × 10³⁷, quinze fois plus que la valeur imprimée (autotest de
   `analyse.py`, vérifié sur l'image de la page). Sans effet sur l'argument : Bostrom
   écrit (p. 6) que « even if our estimate is off by several orders of magnitude,
   this does not matter much for our argument ». Le texte retient le produit recalculé.
   La version publiée n'a pas pu être consultée (accès refusé).
2. **Bostrom 2003, titre** : Crossref, Wiley et OUP donnent « Are We Living in a
   Computer Simulation? » ; la version de l'auteur (simulation-argument.com) et sa FAQ
   disent « Are You Living in a Computer Simulation? ».
3. **Kipping 2020** : deux phrases de la version arXiv intervertissent « base » et
   « simulation ». Section 2.9 : « the probability that we live in a simulated reality
   radically shifts from just below one-half to just approaching zero » ; d'après
   l'équation (32) et le résumé, c'est la probabilité d'être dans la réalité de base
   qui tend vers zéro. Section 3 : « the probability we live in base reality […] is
   still not the favored outcome, with a probability less than 50% » ; d'après
   l'équation (22), c'est la probabilité d'être simulé qui est inférieure à 50 %. Les
   équations et le résumé sont cohérents entre eux. Par ailleurs, la seconde forme de
   l'équation (3) vaut n_G / N_sim et non n_G / (N_sim + 1) : écart relatif
   1/(N_sim + 1), négligeable (autotest).
4. **Vazza 2025** : pour la Terre à pleine résolution, le tableau 1 donne une énergie
   minimale de 3,0 × 10⁵⁹ erg, l'équation (13) 2,55 × 10⁵⁹ erg. Écart interne sans
   effet sur ses conclusions ; le texte n'utilise pas ce nombre.
5. **Hensen et al. 2015** : le titre arXiv (« Experimental loophole-free violation of a
   Bell inequality using entangled electron spins separated by 1.3 km ») diffère du
   titre publié dans *Nature*, retenu dans le texte.
6. **Faizal et al. 2025** : le DOI annoncé (10.22128/jhap.2025.1024.1118) est inconnu de
   Crossref ; la référence est vérifiée par la notice arXiv (« Journal of Holography
   Applications in Physics 5 (2), 10-21 (2025) »).
7. **Vazza 2025, durée de calcul** (arXiv:2504.08461v1, p. 9, relu le 28 septembre 2026
   à l'intégration au site) : « tCPU ∼ 4.2 · 10^13 s of computing time, i.e. ∼ 1.4 · 10^7
   yr ». À 3,16 × 10⁷ s par an, 4,2 × 10¹³ s font environ 1,3 × 10⁶ ans, non
   1,4 × 10⁷ ; le second cas de la même page (« tCPU ∼ 3.0 · 10^15 s », « ∼ 1 · 10^8 yr »)
   est cohérent. Écart de conversion sans effet sur sa conclusion (« requires
   geologically-long timescales », même page). La page du site ne reprend que la durée en
   secondes et cette qualification.

## Détail par référence

### 1. Chalmers, « The Matrix as Metaphysics »
- D. J. Chalmers, dans C. Grau (dir.), *Philosophers Explore The Matrix*, Oxford
  University Press, p. 132-176. DOI 10.1093/oso/9780195181067.003.0009 (Crossref :
  chapitre de livre, pages 132-176, date 2004-09-01). Texte de l'auteur :
  https://consc.net/papers/matrix.html
- En-tête de l'auteur : « This paper was originally written for the philosophy section
  of the official The Matrix website (2003) and was subsequently published in
  (Christopher Grau, ed.) Philosophers Explore the Matrix (Oxford University Press,
  2005). »
- Passages : « The Computational Hypothesis says: Microphysical processes throughout
  space-time are constituted by underlying computational processes. » ; « The Creation
  Hypothesis says: Physical space-time and its contents were created by beings outside
  physical space-time. » ; « The Mind-Body Hypothesis says: My mind is (and has always
  been) constituted by processes outside physical space-time, and receives its
  perceptual inputs from and sends its outputs to processes in physical space-time. » ;
  « Even if contemporary science tends to suggest that the hypothesis is false, we
  cannot rule it out conclusively. » ; « I think that even if I am in a matrix, my world
  is perfectly real. » ; « If so, the Matrix Hypothesis is not a skeptical hypothesis » ;
  « If it is true, there are still electrons and protons. On this picture, electrons
  and protons will be analogous to molecules: they are made up of something more basic,
  but they still exist. » ; « Most famously, Edward Fredkin has postulated that the
  universe is at bottom some sort of computer. More recently, Stephen Wolfram has taken
  up the idea in his book A New Kind of Science ».
- Usage : section 1 (trois sens, réalité du monde simulé), section 3.
- Statut : vérifiée.

### 2. Chalmers, *Reality+*
- D. J. Chalmers, *Reality+: Virtual Worlds and the Problems of Philosophy*, W. W.
  Norton (New York) et Allen Lane, 2022 ; ISBN 9780393635805 (relié). Page de
  l'auteur : https://consc.net/reality/ ; extrait (introduction et chapitre 1) :
  https://consc.net/reality+/excerpt.pdf
- Page de l'auteur : « Reality+: Virtual Worlds and the Problems of Philosophy was
  published by W. W. Norton (US) and Allen Lane (UK) on January 25, 2022. » ; « The
  central thesis of the book is virtual reality is genuine reality. »
- Extrait, introduction : « The central thesis of this book is: Virtual reality is
  genuine reality. » ; « Virtual worlds are not illusions or fictions, or at least they
  need not be. » ; « Life in virtual worlds can be as good, in principle, as life
  outside virtual worlds. You can lead a fully meaningful life in a virtual world. » ;
  « The world we’re living in could be a virtual world. I’m not saying it is. But it’s
  a possibility we can’t rule out. »
- Usage : sections 1 et 7.
- Statut : vérifiée.

### 3. Bostrom 2003
- N. Bostrom, « Are We Living in a Computer Simulation? », *The Philosophical
  Quarterly* 53 (211), 243-255 (2003). DOI 10.1111/1467-9213.00309 (Crossref : titre,
  revue, volume, numéro, pages). Version de l'auteur, « Are You Living in a Computer
  Simulation? », 14 pages : https://simulation-argument.com/simulation.pdf (pages
  ci-dessous : celles de cette version).
- p. 2 : « Provided a system implements the right sort of computational structures and
  processes, it can be associated with conscious experiences. » ; « Arguments for this
  thesis have been given in the literature, and although it is not entirely
  uncontroversial, we shall here take it as a given. »
- p. 5 : « The simulation may therefore need to include a continuous representation of
  computers down to the level of individual logic elements. »
- p. 6 et note 10 : voir « Points relevés », n° 1.
- p. 6-7 : notations f_P, N, H ; « f_sim = f_P N H / ((f_P N H) + H) » ; avec
  N = f_I N_I, « f_sim = f_P f_I N_I / ((f_P f_I N_I) + 1) (*) » ; « at least one of the
  following three propositions must be true: (1) f_P ≈ 0 (2) f_I ≈ 0 (3) f_sim ≈ 1 » ;
  p. 7-8 : « Cr(SIM | f_sim = x) = x (#) ».
- p. 10 : « If the number of ancestor-simulations created by the interested
  civilizations is extremely large, the rarity of such civilizations must be
  correspondingly extreme. »
- p. 11 : « an ethical prohibition against running ancestor-simulations because of the
  suffering that is inflicted on the inhabitants of the simulation ».
- p. 12 : « If we do go on to create our own ancestor-simulations, this would be strong
  evidence against (1) and (2) » ; « Even if it is necessary for the hierarchy to
  bottom out at some stage – the metaphysical status of this claim is somewhat
  obscure – ».
- p. 13 : « There would have to be about 100 billion times as many “me-simulations”
  (simulations of the life of only a single mind) as there are ancestor-simulations in
  order for most simulated persons to be in me-simulations. » ; « one can consider the
  following (farfetched) solution to the problem of evil: that there is no suffering in
  the world and all memories of suffering are illusions. » ; « the implications are
  not all that radical. Our best guide to how our posthuman creators have chosen to set
  up our world is the standard empirical study of the universe we see. »
- p. 14 : « In the dark forest of our current ignorance, it seems sensible to
  apportion one’s credence roughly evenly between (1), (2), and (3). »
- Usage : sections 1, 4, 5, 7, 8 ; formule (*) et répartition en trois parts dans
  `analyse.py`.
- Statut : vérifiée ; titre corrigé ; écart de calcul relevé (note 10).

### 4. Bostrom 2005 (réponse à Weatherson)
- N. Bostrom, « The Simulation Argument: Reply to Weatherson », *The Philosophical
  Quarterly* 55 (218), 90-97 (2005). DOI 10.1111/j.0031-8094.2005.00387.x (Crossref).
  PDF : https://simulation-argument.com/weathersonreply.pdf
- Passage (première page de l'article) : « My view is that we do not currently have
  strong evidence for or against any of the particular disjuncts. At any rate, the
  disjunction is all that the simulation argument purports to show; it does not seek to
  establish that we are probably living in a computer simulation. »
- Usage : verdict, section 5.
- Statut : vérifiée.

### 5. Bostrom et Kulczycki 2011
- N. Bostrom, M. Kulczycki, « A Patch for the Simulation Argument », *Analysis* 71 (1),
  54-61 (2011). DOI 10.1093/analys/anq107 (Crossref). Version des auteurs :
  https://simulation-argument.com/patch.pdf
- Résumé : « This article reports on a newly discovered bug in the original simulation
  argument. Two different ways of patching the argument are proposed, each of which
  preserves the original conclusion. » p. 2 : « This result would seem to suggest the
  possibility of the three propositions in the central tripartite disjunction of the
  simulation argument all being simultaneously false ». p. 3 : « the typical duration
  (or more precisely, the typical cumulative population) of the pre-posthuman phase
  does not differ by an astronomically large factor between civilizations that never
  run a significant number of ancestor simulations and those that eventually do. For
  example, in an appendix we show how by assuming that the difference is no greater than
  a factor of one million we can derive the key tripartite disjunction. »
- Usage : section 5 (populations réelles).
- Statut : vérifiée (ajoutée).

### 6. FAQ de Bostrom (2025)
- N. Bostrom, « The Simulation Argument FAQ », « (2025) », « version 2.0 »,
  https://simulation-argument.com/faq.html, consultée le 28 septembre 2026.
- Question 2 : « I would assign a “substantial probability” to the simulation
  hypothesis. I tend to refrain from providing a specific number. (This is for various
  reasons, including that it could convey a false sense of precision.) »
- Question 5 : « If the simulators don’t want us to know that we are simulated, they
  could easily prevent us from finding out. Consider that even our own humble
  brains—unaided by technology—usually manage to prevent us from realizing when we are
  dreaming at night, even though the typical dream is teeming with the most fantastic
  anomalies. »
- Question 6 : « Critiques based on the assumption that a simulation would have to be
  fully comprehensive (e.g. Vazza (2025)) thus miss the point. »
- Question 12 : « there is little reason to suppose that the hypothetical
  superintelligent simulators would use the crude simulation technique that such a test
  would detect. As the authors themselves note, modern lattice quantum dynamics
  simulations run by human physicists routinely use improved lattice techniques that
  remove this kind of artifacts. »
- Question 17 : « No clarity is gained by asserting that the world isn’t “really real”
  if we are in a simulation. »
- Usage : sections 1, 2, 4, 5, 6.
- Statut : vérifiée (ajoutée). Document en ligne susceptible d'évoluer.

### 7. Weatherson 2003
- B. Weatherson, « Are You a Sim? », *The Philosophical Quarterly* 53 (212), 425-431
  (2003). DOI 10.1111/1467-9213.00323 (Crossref). Version de l'auteur :
  https://simulation-argument.com/weatherson.pdf
- Résumé : « I set out four possible interpretations of the principle, none of which
  can be used to support Bostrom’s argument. On the first two interpretations the
  principle is false, on the third it does not entail the conclusion, and on the fourth
  it only entails the conclusion given an auxiliary hypothesis that we have no reason to
  believe. »
- Usage : section 5 (règle de sélection).
- Statut : vérifiée (ajoutée).

### 8. Hartle et Srednicki 2007
- J. B. Hartle, M. Srednicki, « Are we typical? », *Physical Review D* 75, 123523
  (2007). DOI 10.1103/PhysRevD.75.123523 ; arXiv:0704.2630 (v3).
- Résumé : « Some theoretical calculations make the selection fallacy that we are
  randomly chosen from a class of objects by some physical process, despite the absence
  of any evidence for such a process, or any observational evidence favoring our
  typicality. It is possible to favor theories in which we are typical by appropriately
  choosing their prior probabilities, but such assumptions should be made explicit to
  avoid confusion. »
- Usage : section 5.
- Statut : vérifiée.

### 9. Kipping 2020
- D. Kipping, « A Bayesian Approach to the Simulation Argument », *Universe* 6 (8),
  109 (2020). DOI 10.3390/universe6080109 (Crossref). arXiv:2008.12254v1, commentaire
  de l'auteur : « Published in Universe. This version is formatted using the AAS 6.2
  template ». Équations relevées dans le PDF et la source LaTeX de la version arXiv.
- Résumé : « Using Bayesian model averaging, it is shown that the probability that we
  are sims is in fact less than 50%, tending towards that value in the limit of an
  infinite number of simulations. […] if humanity does start producing such
  simulations, then this would radically shift the odds and make it very probable that
  we are in fact sims. »
- Équations (numérotation arXiv) : (1) N_sim = Σ_{g=2}^{G} p^{g−2} λ^{g−1}
  = (pλ − (pλ)^G)/(p − p²λ) ; (2) Pr(simulated | CES, H_S) = N_sim/(N_sim + 1) ;
  (3) Pr(g = G | CES, H_S) ; (7) Pr(nulliparous | H_S) ; (8) limite (λ − 1)/λ ;
  (12) facteur de Bayes (λ − 1)/λ ; (22) Pr(g = 1 | CES) = 1/2 + 1/(2(N_sim + 1)) ;
  (27) Pr(g = 1 | nulliparous) = 1/(2 − λ⁻¹) ; (32) Pr(g = 1 | parous) = λ/N_sim.
  Toutes reproduites et vérifiées dans `analyse.py` (autotests « kipping_* »).
- Section 3 : « A standard choice is to assume all models are a-priori as likely as
  each other, but this could be challenged as being too generous to model H_S, on the
  basis that it is an intrinsically far more complex model. »
- Affiliation (source LaTeX) : « Department of Astronomy, Columbia University ».
- Usage : section 5, section 8 ; `analyse.py`.
- Statut : vérifiée ; deux inversions de formulation relevées (voir « Points relevés »,
  n° 3).

### 10. Bibeau-Delisle et Brassard 2021
- A. Bibeau-Delisle, G. Brassard, « Probability and consequences of living inside a
  computer simulation », *Proceedings of the Royal Society A* 477 (2247), 20200658
  (2021). DOI 10.1098/rspa.2020.0658 (Crossref) ; arXiv:2008.09275v1.
- Résumé : « It is shown that under reasonable assumptions a Drake-style equation can
  be obtained for the probability that our universe is the result of a deliberate
  simulation. Evaluating loose bounds for certain terms in the equation shows that the
  probability is unlikely to be as high as previously reported in the literature,
  especially in a scenario where the simulations are recursive. »
- arXiv, p. 3, équation (4) : f_Sim = f_Civ f_Ded R_Cal / (1 + f_Civ f_Ded R_Cal) ;
  p. 4 : « In fact, fSim is only a baseline probability that needs to be adjusted
  according to Bayes’ inference rules in the light of other factors, which are virtually
  impossible to evaluate. » ; p. 9 : « fSim also is upper-bounded by fEff, which is most
  likely under 50% » ; « the situation is analogous to that of Drake’s equation [15],
  which contains too many hard-to-estimate factors ».
- Usage : section 4.
- Statut : vérifiée.

### 11. Birch 2013
- J. Birch, « On the ‘Simulation Argument’ and Selective Scepticism », *Erkenntnis* 78
  (1), 95-107 (2013). DOI 10.1007/s10670-012-9400-9 (Crossref). Résumé relevé sur LSE
  Research Online : https://researchonline.lse.ac.uk/id/eprint/61813/
- Résumé : « I first show that the Simulation Argument requires a curious form of
  selective scepticism, for it presupposes that we possess good evidence for claims
  about the physical limits of computation and yet lack good evidence for claims about
  our own physical constitution. […] There is no good reason to uphold the selective
  scepticism the Simulation Argument presupposes. There is thus no good reason to
  believe its conclusion. »
- Usage : section 4.
- Statut : vérifiée.

### 12. Chalmers 1995 et 1996
- D. J. Chalmers, « Absent Qualia, Fading Qualia, Dancing Qualia », dans T. Metzinger
  (dir.), *Conscious Experience*, Imprint Academic, 1995. Texte de l'auteur :
  https://consc.net/papers/qualia.html (en-tête : « Published in Conscious Experience,
  edited by Thomas Metzinger. Imprint Academic, 1995. »).
- Passages : « given any system that has conscious experiences, then any system that
  has the same functional organization at a fine enough grain will have qualitatively
  identical conscious experiences » ; « To be sure, Fading Qualia may be logically
  possible. » ; « It follows that the possibility of Fading Qualia requires either a
  bizarre relationship between belief contents and physical states, or the possibility
  of beings that are massively mistaken about their own conscious experiences despite
  being fully rational. » ; à propos de Searle (1992) : « Here, Searle embraces the
  possibility of Fading Qualia ».
- D. J. Chalmers, *The Conscious Mind: In Search of a Fundamental Theory*, Oxford
  University Press, 1996 (« published with Oxford University Press in April 1996 »,
  https://consc.net/books/tcm/). Précis de l'auteur (https://consc.net/papers/precis.html) :
  « Chapter 7: Absent Qualia, Fading Qualia, Dancing Qualia. I argue for a principle of
  organizational invariance […] ». Mogensen (2025) situe l'argument aux pages 253-263.
- Usage : section 3.
- Statut : vérifiées.

### 13. Searle 1980
- J. R. Searle, « Minds, brains, and programs », *Behavioral and Brain Sciences* 3 (3),
  417-424 (1980). DOI 10.1017/S0140525X00005756 (Crossref, résumé de l'éditeur).
- Résumé : « (2) Instantiating a computer program is never by itself a sufficient
  condition of intentionality. […] The form of the argument is to show how a human agent
  could instantiate the program and still not have the relevant intentionality. […]
  (5) Any attempt literally to create intentionality artificially (strong AI) could not
  succeed just by designing programs but would have to duplicate the causal powers of
  the human brain. »
- Usage : section 3.
- Statut : vérifiée.

### 14. Mogensen 2025
- A. L. Mogensen, « How to resist the Fading Qualia Argument », *Synthese* 206 (5), 252
  (2025). DOI 10.1007/s11229-025-05338-3 (Crossref : publié en ligne le 5 novembre 2025,
  licence CC BY 4.0). Texte : Oxford Research Archive,
  https://ora.ox.ac.uk/objects/uuid:12beef7f-6769-4066-ac01-84cb2a707535 (« Received:
  30 July 2024 / Accepted: 18 October 2025 »).
- Résumé : « The Fading Qualia Argument is perhaps the strongest argument supporting the
  view that in order for a system to be conscious, it does not need to be made of
  anything in particular […]. I show how the argument can be resisted given two key
  assumptions: that consciousness is associated with vagueness at its boundaries and
  that conscious neural activity has a particular kind of holistic structure. »
- Conclusion (p. 15) : « I regard each of these assumptions as plausible, although both
  are obviously controversial. » ; « Nonetheless, I take myself to have exposed
  important weaknesses in the Fading Qualia Argument. »
- Usage : section 3.
- Statut : l'article existe ; vérifié.

### 15. Lloyd 2000
- S. Lloyd, « Ultimate physical limits to computation », *Nature* 406, 1047-1054
  (2000). DOI 10.1038/35023282 (Crossref) ; arXiv:quant-ph/9908043v3.
- arXiv : « quantitative bounds are put to the computational power of an ‘ultimate
  laptop’ with a mass of one kilogram confined to a volume of one liter » ; « the
  ultimate laptop can perform a maximimum of 5.4258 × 10^50 operations per second » ;
  « available memory space I = S/kB ln 2 = 2.13×10^31 bits ».
- Usage : section 4 ; `analyse.py` (valeurs citées).
- Statut : vérifiée.

### 16. Lloyd 2002
- S. Lloyd, « Computational Capacity of the Universe », *Physical Review Letters* 88,
  237901 (2002). DOI 10.1103/PhysRevLett.88.237901 (Crossref) ; arXiv:quant-ph/0110141v1.
- arXiv : « The universe can have performed no more than 10^120 ops on 10^90 bits. » ;
  « the total number of bits (≈10^90 in matter, ≈10^120 if gravitation is taken into
  account) and ops (≈10^120) » ; interprétations : « 2. They give lower bounds to the
  number of ops and bits required to simulate the entire universe on a quantum
  computer. 3. If one chooses to regard the universe as performing a computation, these
  numbers give the numbers of ops and bits in that computation. »
- Usage : sections 1 et 4 ; `analyse.py`.
- Statut : vérifiée.

### 17. Vazza 2025
- F. Vazza, « Astrophysical constraints on the simulation hypothesis for this Universe:
  why it is (nearly) impossible that we live in a simulation », *Frontiers in Physics*
  13, 1561873 (publié le 17 avril 2025). DOI 10.3389/fphy.2025.1561873 (Crossref ;
  PDF de l'éditeur) ; arXiv:2504.08461.
- Résumé : « In all cases, the amounts of energy or power required by any version of
  the simulation hypothesis are entirely incompatible with physics or (literally)
  astronomically large, even in the lowest resolution case. Only universes with very
  different physical properties can produce some version of this Universe as a
  simulation. […] It is simply impossible for this Universe to be simulated by a
  universe sharing the same properties, regardless of technological advancements in the
  far future. »
- p. 2, tableau 1 (Univers à pleine résolution : 3,5 × 10¹²⁴ bits, 8,9 × 10¹⁰⁸ erg) ;
  p. 3, équation (8) : E_U ∼ 2,7 × 10⁷⁸ erg ; p. 4 : « the initialization of a complete
  simulation of “just” a planet like Earth requires either converting the entire
  stellar mass of a typical globular cluster into energy or […] » ; p. 5 : λ_ν ∼ 1,2 ×
  10⁻²¹ cm, I_⊕,low ≈ 1,65 × 10⁵¹ bits ; p. 6 : « tCPU ∼ 4.2 · 10^13 s of computing time,
  that is, ∼ 1.4 · 10^7 yr, using the computing power given by Equation 20 » ; p. 7-8
  (section 4.4) : « it is implausible that the information budget quoted in this work
  can be reduced by several orders of magnitude » ; p. 10 : « the question of whether
  universes with entirely different sets of physical laws or dimensionalities could
  produce our Universe as a simulation seems to be entirely outside of what is
  scientifically testable, even in theory » ; « a possible “simulation hypothesis,”
  which does not pose obvious constraints on computing, might be the solipsistic
  scenario » ; « nothing is new from Renee Descartes’ “evil genius” […] to “Boltzmann
  brains” ».
- Usage : sections 2, 4, 7, 8.
- Statut : vérifiée ; écart interne relevé (« Points relevés », n° 4).

### 18. Edge et Brown 2026
- E. Edge, C. A. Brown, « Commentary: Astrophysical constraints on the simulation
  hypothesis for this Universe: why it is (nearly) impossible that we live in a
  simulation », *Frontiers in Physics* 14, 1808725 (publié le 21 avril 2026). DOI
  10.3389/fphy.2026.1808725 (Crossref ; PDF de l'éditeur, « TYPE General Commentary »).
- p. 2 : « Vazza’s strongest conclusions follow for a shared-world, planet-level (and
  experiment-consistent) simulation under physics like our own, but that scope is
  broader than the minimal rendering commitments Bostrom outlines for sustaining
  verisimilitude in subjective experience » ; p. 2 : « This commentary does not propose
  a new variant of the SH, nor does it evaluate the probability of its truth ».
- Usage : sections 4 et 8.
- Statut : le commentaire existe ; vérifié.

### 19. Faizal, Krauss, Shabir, Marino 2025
- M. Faizal, L. M. Krauss, A. Shabir, F. Marino, « Consequences of Undecidability in
  Physics on the Theory of Everything », *Journal of Holography Applications in
  Physics* 5 (2), 10-21 (2025) (référence donnée par la notice arXiv) ; arXiv:2507.22950v1.
- Résumé : « Because any putative simulation of the universe would itself be
  algorithmic, this framework also implies that the universe cannot be a simulation. »
  p. 8 : « These proposals assume that every physical truth is reducible to the output
  of a finite algorithm executed on a sufficiently powerful substrate. » ; « Since it is
  impossible to simulate a complete and consistent universe, our universe is definitely
  not a simulation. As the universe is produced by MToE, the simulation hypothesis is
  logically impossible rather than merely implausible. »
- Usage : section 4 (et verdict).
- Statut : vérifiée par arXiv (ajoutée) ; DOI absent de Crossref.

### 20. 't Hooft 2016
- G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer
  (Fundamental Theories of Physics), 2016. DOI 10.1007/978-3-319-41285-6 (Crossref) ;
  arXiv:1405.1548v3.
- Résumé arXiv : « we argue that even the Standard Model, together with gravitational
  interactions, might be viewed as a quantum mechanical approach to analyse a system
  that could be classical at its core. We explain how such thoughts can conceivably be
  reconciled with Bell's theorem, and how the usual objections voiced against the
  notion of ‘superdeterminism’ can be overcome, at least in principle. »
- Usage : sections 1 et 6.
- Statut : vérifiée (ajoutée).

### 21-23. Tests de Bell sans échappatoire (2015)
- B. Hensen et al., « Loophole-free Bell inequality violation using electron spins
  separated by 1.3 kilometres », *Nature* 526, 682-686 (2015). DOI 10.1038/nature15759
  (Crossref, 19 auteurs) ; arXiv:1508.05949v1. Résumé arXiv : « We perform 245 trials
  testing the CHSH-Bell inequality S ≤ 2 and find S = 2.42 ± 0.20. A null hypothesis
  test yields a probability of p = 0.039 that a local-realist model for space-like
  separated sites produces data with a violation at least as large as observed ». arXiv
  p. 7 : « Strictly speaking, no Bell experiment can exclude the infinite number of
  conceivable local realist theories, because it is fundamentally impossible to prove
  when and where free random input bits and output values came into existence. »
- M. Giustina et al., « Significant-Loophole-Free Test of Bell’s Theorem with Entangled
  Photons », *Physical Review Letters* 115, 250401 (2015). DOI
  10.1103/PhysRevLett.115.250401 (Crossref) ; arXiv:1511.03190. Résumé : « The purely
  statistical probability of our results to occur under local realism does not exceed
  3.74 × 10^-31, corresponding to an 11.5 standard deviation effect. »
- L. K. Shalm et al., « Strong Loophole-Free Test of Local Realism », *Physical Review
  Letters* 115, 250402 (2015). DOI 10.1103/PhysRevLett.115.250402 (Crossref) ;
  arXiv:1511.03189. Résumé : « we compute p-values as small as 5.9 × 10^-9 for our Bell
  violation while maintaining the spacelike separation of our events. […] our smallest
  adjusted p-value is 2.3 × 10^-7. We therefore reject the hypothesis that local realism
  governs our experiment. »
- Usage : section 6.
- Statut : vérifiées.

### 24. Zurek 2003
- W. H. Zurek, « Decoherence, einselection, and the quantum origins of the classical »,
  *Reviews of Modern Physics* 75, 715-775 (2003). DOI 10.1103/RevModPhys.75.715
  (Crossref) ; arXiv:quant-ph/0105127v3 (« the text is identical with that in the Rev.
  Mod. Phys. July issue »).
- Résumé : « Decoherence is caused by the interaction with the environment. Environment
  monitors certain observables of the system, destroying interference between the
  pointer states corresponding to their eigenvalues. » ; texte : « Von Neumann (1932),
  London and Bauer (1939) and Wigner (1963) have all appealed to the special role of the
  conscious observer. […] Quantum formalism has led us to a different view » ;
  « decoherence – through einselection – helps solve the measurement problem ».
- Usage : section 6.
- Statut : vérifiée.

### 25. Jacques et al. 2007
- V. Jacques, E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, J.-F. Roch,
  « Experimental Realization of Wheeler’s Delayed-Choice Gedanken Experiment »,
  *Science* 315, 966-968 (2007). DOI 10.1126/science.1136303 (Crossref) ;
  arXiv:quant-ph/0610241.
- Résumé arXiv : « The choice between measuring either the ‘open’ or ‘closed’
  configuration is made by a quantum random number generator, and is space-like
  separated -- in the relativistic sense -- from the entering of the photon into the
  interferometer. Measurements in the closed configuration show interference with a
  visibility of 94%, while measurements in the open configuration allow us to determine
  the followed path with an error probability lower than 1%. » ; texte : « Once more, we
  find that Nature behaves in agreement with the predictions of Quantum Mechanics even
  in surprising situations where a tension with Relativity seems to appear. »
- Usage : section 6.
- Statut : vérifiée.

### 26. Ma, Kofler, Zeilinger 2016
- X.-S. Ma, J. Kofler, A. Zeilinger, « Delayed-choice gedanken experiments and their
  realizations », *Reviews of Modern Physics* 88, 015005 (2016). DOI
  10.1103/RevModPhys.88.015005 (Crossref) ; arXiv:1407.2930v3.
- Conclusion (arXiv) : « It is a general feature of delayed-choice experiments that
  quantum effects can mimic an influence of future actions on past events. However,
  there never emerges any paradox if the quantum state is viewed only as ‘catalogue of
  our knowledge’ […] no physical interactions or signals, let alone into the past, are
  necessary to explain the experimental results. »
- Usage : section 6.
- Statut : vérifiée (choix pour « Ma et al. »).

### 27. Barnes 2012
- L. A. Barnes, « The Fine-Tuning of the Universe for Intelligent Life », *Publications
  of the Astronomical Society of Australia* 29 (4), 529-564 (2012). DOI 10.1071/AS12015
  (Crossref, résumé de l'éditeur) ; arXiv:1112.4647.
- Résumé : « The claim is that in the space of possible physical laws, parameters and
  initial conditions, the set that permits the evolution of intelligent life is very
  small. […] I do not attempt to defend any conclusion based on the fine-tuning of the
  universe for intelligent life. »
- Usage : section 6.
- Statut : vérifiée.

### 28-30. Vopson
- M. M. Vopson, « The second law of infodynamics and its implications for the simulated
  universe hypothesis », *AIP Advances* 13, 105308 (2023). DOI 10.1063/5.0173278
  (Crossref, résumé de l'éditeur) : « Despite the lack of evidence, this idea is gaining
  traction in scientific circles […] we provide scientific evidence that appears to
  underpin the simulated universe hypothesis. »
- M. M. Vopson, « Is gravity evidence of a computational universe? », *AIP Advances* 15,
  045035 (2025). DOI 10.1063/5.0264945 (Crossref) : « This is another example of data
  compression and computational optimization in our universe, which supports the
  possibility of a simulated or computational universe. […] This is fully aligned with
  Verlinde’s entropic gravity studies published in 2011 ».
- M. M. Vopson, S. Lepadatu, « Second law of information dynamics », *AIP Advances* 12,
  075310 (2022). DOI 10.1063/5.0100358 (Crossref) : « the second law of infodynamics
  requires the information entropy to remain constant or to decrease over time ».
- M. M. Vopson, « The mass-energy-information equivalence principle », *AIP Advances* 9,
  095206 (2019), DOI 10.1063/1.5123794 ; M. M. Vopson, « Experimental protocol for
  testing the mass–energy–information equivalence principle », *AIP Advances* 12, 035311
  (2022), DOI 10.1063/5.0087175 (Crossref : titres, auteur, dates).
- Le texte intégral n'a pas pu être consulté (AIP refuse l'accès automatisé) : le texte
  ne s'appuie que sur les résumés et les métadonnées de l'éditeur.
- Usage : section 6.
- Statut : vérifiées (ajoutées).

### 31. Beane, Davoudi, Savage
- S. R. Beane, Z. Davoudi, M. J. Savage, « Constraints on the Universe as a Numerical
  Simulation », *European Physical Journal A* 50, 148 (2014). DOI
  10.1140/epja/i2014-14148-0 (Crossref) ; arXiv:1210.1847 (4 octobre 2012).
- Résumé : « we assume that our universe is an early numerical simulation with
  unimproved Wilson fermion discretization […] the most stringent bound on the inverse
  lattice spacing of the universe, b^(-1) >~ 10^(11) GeV, is derived from the
  high-energy cut off of the cosmic ray spectrum. The numerical simulation scenario could
  reveal itself in the distributions of the highest energy cosmic rays exhibiting a
  degree of rotational symmetry breaking that reflects the structure of the underlying
  lattice. » ; conclusion (arXiv) : « Given the ease with which current lattice QCD
  simulations incorporate improvement or employ discretizations that preserve chiral
  symmetry, it seems unlikely that any but the very earliest universe simulations would
  be unimproved with respect to the lattice spacing. Of course, improvement in this
  context masks much of our ability to probe the possibility that our universe is a
  simulation ».
- Usage : section 6.
- Statut : vérifiée.

### 32. Tests n° 1 à 4 d'aeternam
- Valeurs recopiées par `analyse.py` depuis `recherche/2026-09-28-grille-lhaaso/`,
  `recherche/2026-09-28-rayons-cosmiques/` et
  `recherche/2026-09-28-dispersion-directionnelle/` (`resultats.json`), avec leur
  empreinte SHA-256 enregistrée dans `resultats.json` (clé `tests`).
- Lues directement dans leur `resultats.json` par `site/generer.py` (`table_synthese`) :
  le nombre de bits bruts du test n° 4 (`recherche/2026-09-28-hasard-quantique/`,
  `volume.bits_bruts_non_haches`) et l'excès non exclu du test n° 2, pris comme dans son
  article à la pire des orientations fixées (`limite_superieure_95.pire_orientation_epsilon_axes_max`).
  La valeur `tests.test2.exces_axes_non_exclu_95` de `resultats.json` est la limite
  moyenne sur les orientations, que l'article du test n° 2 ne retient pas.

### 33. Musk, Code Conference 2016
- E. Musk, entretien à la Code Conference 2016 ; vidéo :
  https://www.youtube.com/watch?v=2KK_kzrJPS8.
- Motherboard (Vice), 2 juin 2016,
  https://www.vice.com/en/article/elon-musk-simulated-universe-hypothesis/ :
  « 40 years ago, we had pong, two rectangles and a dot […] Now 40 years later we have
  photorealistic 3D simulations with millions of people playing simultaneously and it’s
  getting better every year. And soon we’ll have virtual reality, augmented reality, if
  you assume any rate of improvement at all, the games will become indistinguishable from
  reality. » ; « we will create simulations that are indistinguishable from reality or
  civilization will cease to exist. Those are the two options. »
- TechCrunch, 24 juin 2016,
  https://techcrunch.com/2016/06/24/a-running-tab-of-what-tech-people-think-about-whether-were-living-in-a-simulation :
  « there would probably be billions of such computers and set-top boxes, it would seem
  to follow that the odds that we’re in base reality is one in billions. »
- Usage : accueil (bloc « La théorie ») et section 5 : borne haute de \(N_I\) (10^9) dans
  notre choix central.
- Statut : vérifiée (passages relus le 28 septembre 2026 dans les deux articles).
