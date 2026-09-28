# Le hasard quantique trahit-il un programme ?

*Brouillon, test n° 4. Chaque nombre tiré de `resultats.json` est écrit
[[clé]] = valeur ; la clé est le chemin dans ce fichier.*

## Verdict

**Non.** Nous avons testé [[volume.bits_total]] = 41 674 752 bits de hasard
quantique publié, dont [[volume.bits_bruts_non_haches]] = 20 703 232 bits
bruts, jamais passés par un algorithme de brassage. Sur les bits bruts
exploitables, aucun des tests conçus pour reconnaître un générateur
pseudo-aléatoire ne réagit ([[verdict.trace_de_pseudo_hasard]] = false),
alors que ces mêmes tests repèrent sans difficulté quatre générateurs
simples utilisés comme témoins. Ce résultat négatif a une portée limitée :
un générateur de qualité cryptographique n'aurait laissé aucune trace, et
aucun test statistique ne peut l'exclure.

## Explication

Si le monde était une simulation, il faudrait bien produire le résultat de
chaque mesure quantique, pile ou face, 0 ou 1. La physique dit que ce
résultat est imprévisible par nature. Un ordinateur, lui, ne sait pas faire
de vrai hasard : il le fabrique avec une recette de calcul, un
« générateur pseudo-aléatoire ». Une simulation économe utiliserait une
recette rapide et simple. Or les recettes simples laissent des empreintes :
des répétitions, des régularités cachées, une structure qu'on peut
retrouver en calculant.

Nous avons donc pris des suites de 0 et de 1 produites par de vraies
expériences quantiques et publiées par leurs auteurs, et nous y avons
cherché ces empreintes.

Première difficulté : la plupart des sources publiques de hasard quantique
passent leurs résultats dans un « mixeur » mathématique avant de les
publier (l'université nationale australienne, ANU, et la balise de hasard
du NIST, l'institut américain des normes). Ce mixeur est lui-même conçu pour
effacer toute structure. Tester sa sortie ne dit donc rien de la source :
cela revient à juger la farine après la boulangerie. Nous avons testé ces
données quand même, mais elles ne comptent pas dans le verdict.

Il reste deux sources brutes, sans mixeur : un appareil à photons intriqués
de l'université de Portland (Oregon), qui publie ses bits tels quels, et neuf
ordinateurs quantiques d'IBM à qui l'on a demandé des millions de fois de
tirer à pile ou face avec un seul qubit.

Résultat :

- Les photons intriqués passent tous les tests, les généraux comme les
  spécialisés.
- Les ordinateurs d'IBM échouent aux tests généraux : ils donnent un peu
  trop de 0. C'est un défaut connu et expliqué par leurs auteurs : le qubit
  part de l'état 0 et le réglage qui le met en équilibre n'est pas parfait.
  Quand on corrige ce déséquilibre par une méthode simple et classique, tous
  les tests passent. Une des neuf machines, Belem, est en outre restée
  « bloquée » sur 0 ou sur 1 pendant des séries entières de mesures ; c'est
  une panne de mesure, pas une recette de calcul. Les huit autres machines
  ne montrent aucune empreinte de générateur.
- Les témoins se comportent comme prévu : les recettes simples sont
  démasquées, y compris le Mersenne Twister, un générateur très répandu qui
  passe pourtant toute la batterie officielle du NIST ; les recettes
  sophistiquées ne le sont pas, pas plus que les chiffres de √2, qui sont
  pourtant parfaitement calculables.

Ce dernier point dit la limite du test : si la simulation utilise une bonne
recette, aucune analyse de ce genre ne peut la voir. Le résultat exclut une
simulation « bon marché », pas une simulation soignée.

## Analyse détaillée

### 1. Ce qui est testable

Un test statistique sur une suite de bits ne renseigne que sur le dernier
traitement subi par cette suite. Une sortie passée par une fonction de
hachage cryptographique ressemble au hasard parfait quelle que soit
l'entrée, pourvu que l'entrée ait assez d'entropie. Nous distinguons donc :

| jeu | origine | traitement | bits testés |
|---|---|---|---|
| parity | parité des comptages de quatre détecteurs, photons intriqués en polarisation (Kavulich et al. 2021) | aucun | [[donnees.parity.n_bits]] = 6 400 000 |
| ibm | « Basic QRNG » : Hadamard puis mesure d'un qubit, neuf machines IBM (Root et Becker 2024) | aucun | [[donnees.ibm.n_bits]] = 14 303 232 |
| anu | fluctuations du vide, ANU | AES-128 (Haw et al. 2015) | [[donnees.anu.n_bits]] = 16 777 216 |
| beacon | NIST Beacon 2.0, `localRandomValue` | SHA-512 d'au moins deux générateurs (NISTIR 8213, F9) | [[donnees.beacon.n_bits]] = 4 194 304 |

Seuls parity et ibm portent sur la nature du hasard quantique. Les
données brutes des tests de Bell « sans échappatoire » du NIST (2015)
existent, mais leurs choix de mesure sont le XOR de sources physiques et
d'une source pseudo-aléatoire fixée d'avance (Shalm et al. 2015), et leurs
résultats de détection ne sont pas des bits uniformes : ils n'ont pas été
retenus. L'API actuelle de l'ANU exige une clé (réponse 403 sans clé) ;
l'ancienne répond encore mais trop lentement pour des dizaines de
mégabits ; comme sa sortie est hachée, nous avons pris les fichiers ANU
archivés sur Zenodo. Pour le Beacon, nous avons vérifié la chaîne
d'engagements : precommitmentValue(i) = SHA-512(localRandomValue(i+1)) sur
[[donnees.beacon.engagements_verifies]] = 8191 couples consécutifs sur
8 191.

### 2. Niveau 1 : batterie NIST SP 800-22

La batterie complète (15 tests, jusqu'à 188 p-valeurs par séquence de
10^6 bits) est réimplémentée dans `analyse.py`. Elle reproduit les
[[autotests.annexe_b_valeurs_verifiees]] = 64 p-valeurs publiées dans
l'annexe B du document (π, e, √2, √3) à
[[autotests.annexe_b_ecart_max]] = 6,9 × 10^-7 près, et à
[[autotests.annexe_b_ecart_max_chevauchant]] = 2,0 × 10^-5 près pour le
test des gabarits chevauchants. Deux constantes du code de référence
diffèrent du texte (voir `sources.md`) : l'autotest utilise celles du code,
l'analyse celles du texte.

Les données sont coupées en [[volume.sequences_nist_total]] = 38 séquences
de 10^6 bits (les séquences IBM ne chevauchent pas deux machines). Toutes
les p-valeurs des quatre jeux, soit
[[familles.principale_niveau1_nist.n_p]] = 6624, forment une seule famille
corrigée par la méthode de Holm au risque global de 1 %.

- parity : [[donnees.parity.niveau1.n_p]] = 1102 p-valeurs, aucun rejet ;
  plus petite p-valeur ajustée [[donnees.parity.niveau1.p_holm_min]] = 0,81.
  Fraction de 1 : [[donnees.parity.fraction_de_1]] = 0,49998.
- anu : [[donnees.anu.niveau1.n_p]] = 2852 p-valeurs, aucun rejet
  ([[donnees.anu.niveau1.p_holm_min]] = 0,44).
- beacon : [[donnees.beacon.niveau1.n_p]] = 726 p-valeurs, aucun rejet
  ([[donnees.beacon.niveau1.p_holm_min]] = 1,0).
- ibm : [[donnees.ibm.niveau1.rejets]] = 473 rejets sur
  [[donnees.ibm.niveau1.n_p]] = 1944. Fraction de 1 :
  [[donnees.ibm.fraction_de_1]] = 0,4871, soit un écart de
  [[donnees.ibm.z_biais]] = −97,5 écarts-types. Le test des excursions
  aléatoires ne s'applique pas (moins de 500 cycles, § 2.14.4).

Diagnostic : sans la machine Belem (voir § 4), l'extracteur de von Neumann
(01 → 0, 10 → 1, 00 et 11 jetés), qui supprime exactement un biais
constant, laisse [[diagnostic_von_neumann.ibm_sans_belem.bits_apres_extraction]]
= 3 297 358 bits ; la batterie y donne
[[diagnostic_von_neumann.ibm_sans_belem.rejets]] = 0 rejet sur
[[diagnostic_von_neumann.ibm_sans_belem.n_p]] = 512 p-valeurs
([[diagnostic_von_neumann.ibm_sans_belem.p_holm_min]] = 0,17). Les échecs
IBM viennent donc du biais, conforme à ce que décrivent Root et Becker.
Sur ces huit machines, les tests rejetés sont tous sensibles au biais
(fréquence, fréquence par blocs, sommes cumulées, suites, plus longue
suite, gabarits, entropie approchée, série) ; les tests de rang, spectral,
universel et de complexité linéaire n'y rejettent pas.

### 3. Niveau 2 : signatures d'un générateur pseudo-aléatoire

La batterie NIST dit si une suite s'écarte du hasard idéal, pas pourquoi.
Trois tests visent les défauts propres aux générateurs algorithmiques :

a. **Complexité linéaire globale.** L'algorithme de Berlekamp-Massey donne
la longueur L du plus court registre à décalage linéaire qui reproduit un
segment de n bits. Pour une suite aléatoire, L vaut n/2 à quelques unités
près ; la loi exacte de L (2^min(2n−2L, 2L−1) suites de complexité L) est
vérifiée dans `analyse.py` par énumération des 4 096 suites de 12 bits.
Tout générateur linéaire sur GF(2) dont l'état compte moins de n/2 bits
donne L < n/2. Nous prenons des segments de [[methode.segment_bm]] = 50 000
bits, lus en continu (huit segments) ou un bit sur 48 et un bit sur 64
(deux segments chacun), répartis sur tout le jeu : un générateur qui sort
des mots de 8, 16, 32 ou 64 bits est ainsi couvert, jusqu'à un état de
[[methode.etat_max_detecte_bits]] = 25 000 bits. Un test auxiliaire a
vérifié qu'une source physique biaisée et corrélée (chaîne de Markov) garde
L ≈ n/2 : sur cet exemple, le test ne confond pas défaut physique et algorithme.

b. **Répétitions.** Toute fenêtre de 64 bits, à chaque position, est
comparée à toutes les autres. Sous le hasard, le nombre attendu de paires
identiques est de l'ordre de 10^-6 (par exemple
[[donnees.parity.niveau2.repetitions.attendu_poisson]] = 1,1 × 10^-6 pour
parity) ; une seule répétition signalerait une période ou une graine
réutilisée.

c. **Corrélations à longue portée.** Autocorrélation aux décalages 17 à
[[methode.lag_max]] = 65 536, avec correction de Bonferroni sur les 65 520
décalages. Les décalages 1 à 16 sont rapportés à part : une corrélation
courte est le défaut attendu d'un détecteur.

Famille principale, Holm à 1 % sur [[familles.principale_niveau2_cible.n_p]]
= 54 p-valeurs :

- parity : aucun rejet ([[donnees.parity.niveau2.p_holm_min]] = 1,0) ;
  écart maximal de L à n/2 :
  [[donnees.parity.niveau2.complexite_ecart_max_a_n_sur_2]] = 2 ; aucune
  répétition ; corrélations à longue portée
  [[donnees.parity.niveau2.autocorrelation.longue_portee_17_65536.p_bonferroni]] = 0,91.
- anu et beacon : aucun rejet ([[donnees.anu.niveau2.p_holm_min]] = 1,0).
- ibm : [[donnees.ibm.niveau2.rejets]] = 3 rejets (complexité linéaire d'un
  segment, répétitions, corrélations à longue portée).

### 4. Les trois rejets d'IBM : une machine bloquée

Les rejets IBM ont une cause unique et vérifiable. Les données sont faites
d'essais de 8 192 tirs (Root et Becker, § II.D), soit
[[donnees.ibm.n_essais]] = 1746 essais. Parmi eux,
[[donnees.ibm.n_essais_tous_egaux]] = 17 sont constants
([[donnees.ibm.n_essais_tous_a_0]] = 10 entièrement à 0,
[[donnees.ibm.n_essais_tous_a_1]] = 7 entièrement à 1) et
[[donnees.ibm.n_essais_quasi_constants]] = 6 autres le sont à plus de 99 % ;
tous proviennent de la machine Belem, aucun des huit autres machines
(vérifié par une assertion du script). Les
[[donnees.ibm.niveau2.repetitions.paires_identiques]] = 10 266 473 272
paires de fenêtres identiques sont toutes des suites de bits égaux :
parmi les fenêtres « typiques » (16 à 48 bits à 1), il y en a
[[donnees.ibm.niveau2.repetitions.paires_identiques_fenetres_typiques]] = 0.
Le segment de complexité anormale (log10 p =
[[donnees.ibm.niveau2.complexite_log10_p_min]] = −5188) commence dans ces
essais bloqués. Une sortie figée n'est pas une sortie de générateur
pseudo-aléatoire : c'est l'absence de sortie.

La décision d'écarter Belem a été prise **après** avoir vu ces données ;
elle est donc traitée comme une analyse secondaire, avec sa propre famille
de Holm, et la règle initiale appliquée aux données publiées reste
rapportée dans `resultats.json` (`verdict.rejets_niveau2_donnees_publiees`).
Sur les huit autres machines ([[donnees.ibm_sans_belem.n_bits]] = 13 254 656
bits) :

- niveau 2 : [[donnees.ibm_sans_belem.niveau2.rejets]] = 0 rejet sur
  [[donnees.ibm_sans_belem.niveau2.n_p]] = 14
  ([[donnees.ibm_sans_belem.niveau2.p_holm_min]] = 0,58) ; écart maximal de
  L à n/2 : [[donnees.ibm_sans_belem.niveau2.complexite_ecart_max_a_n_sur_2]] = 2 ;
  [[donnees.ibm_sans_belem.niveau2.repetitions.paires_identiques]] = 0
  répétition ; corrélations à longue portée
  [[donnees.ibm_sans_belem.niveau2.autocorrelation.longue_portee_17_65536.p_bonferroni]] = 1,0 ;
- une corrélation au décalage 1 existe
  ([[donnees.ibm_sans_belem.niveau2.autocorrelation.r_lag1]] = 0,0047, soit
  [[donnees.ibm_sans_belem.niveau2.autocorrelation.courte_portee_1_16.z_max]]
  = 15,5 écarts-types) : un défaut de mesure à courte portée, sans rapport
  avec la structure d'un générateur ;
- niveau 1 : [[donnees.ibm_sans_belem.niveau1.rejets]] = 341 rejets sur
  [[donnees.ibm_sans_belem.niveau1.n_p]] = 1782, expliqués par le biais
  (§ 2).

### 5. Contrôles

La même chaîne est appliquée à [[methode.bits_par_controle]] = 4 194 304
bits de chaque générateur connu :

| générateur | attendu | détecté par |
|---|---|---|
| LFSR degré 20 (période 1 048 575) | oui | NIST (rang, complexité linéaire, spectral) ; niveau 2 (L = 20, [[controles.lfsr_degre_20.repetitions_paires]] = 6 291 270 paires répétées) |
| LFSR degré 31 | oui | NIST (rang, complexité linéaire) ; niveau 2 (L = 31, log10 p = [[controles.lfsr_degre_31.complexite_log10_p_min]] = −15 033) |
| LCG 32 bits | oui | NIST (spectral) ; niveau 2 (corrélations à longue portée) |
| Mersenne Twister (MT19937) | oui | **niveau 2 seulement** : L = 19 937 exactement à la décimation 64 (log10 p = [[controles.mersenne_twister.complexite_log10_p_min]] = −3048) ; batterie NIST muette ([[controles.mersenne_twister.niveau1_p_holm_min]] = 1,0) |
| PCG64 | non | rien ([[controles.pcg64.niveau1_p_holm_min]] = 0,32 ; [[controles.pcg64.niveau2_p_holm_min]] = 0,5) |
| SHA-256 en mode compteur | non | rien ([[controles.sha256_compteur.niveau1_p_holm_min]] = 0,33 ; [[controles.sha256_compteur.niveau2_p_holm_min]] = 1,0) |
| décimales binaires de √2 | non | rien ([[controles.racine_de_2.niveau1_p_holm_min]] = 1,0 ; [[controles.racine_de_2.niveau2_p_holm_min]] = 1,0) |

Le script s'arrête si un contrôle ne se comporte pas comme attendu. Le cas
du Mersenne Twister montre que le niveau 2 ajoute une vraie sensibilité à
la batterie officielle ; ceux de PCG64, de SHA-256 et de √2 montrent qu'une
suite entièrement déterministe peut n'avoir aucune signature détectable.

### 6. Conclusion

Règle fixée avant l'analyse : « trace de pseudo-hasard » si un test du
niveau 2 rejette, après correction de Holm à 1 %, sur une source quantique
brute. Appliquée aux données publiées, elle rejette sur IBM, à cause de la
seule machine Belem bloquée ; sur les photons intriqués et sur les huit
machines IBM en état de marche, elle ne rejette pas. Verdict : **non**.

## Limites

- **Un générateur de qualité cryptographique est indiscernable.** Les
  contrôles PCG64, SHA-256 et √2 le montrent : des suites déterministes
  passent tout. Ce test exclut une simulation qui tirerait ses mesures
  quantiques d'un générateur simple (linéaire, à courte période, à
  corrélations longues), pas une simulation qui utiliserait un bon
  générateur. NIST SP 800-22 le dit lui-même : aucun ensemble de tests ne
  remplace la cryptanalyse.
- **Couverture du niveau 2.** Les générateurs linéaires ne sont détectés que
  si leur état compte moins de 25 000 bits et que leur taille de mot divise
  48 ou 64 ; les répétitions, que si la période est plus courte que le jeu
  de données.
- **Volume brut modeste.** 6,4 millions de bits de photons intriqués
  (environ 26 bits par seconde selon les auteurs) et 13,3 millions de bits
  IBM exploitables. Aucune de ces sources n'est certifiée par un test de
  Bell sans échappatoire.
- **Choix après lecture.** L'exclusion de la machine Belem a été décidée
  après avoir vu les données ; la cause est documentée et le résultat brut
  est publié, mais c'est une étape a posteriori.
- **Données hachées.** Les résultats ANU et Beacon ne mesurent que la
  qualité de l'AES-128 et du SHA-512 ; ils ne disent rien sur la source.
- **Ordre des bits.** Pour parity, l'ordre des bits dans l'octet est une
  convention de lecture (poids fort d'abord) ; l'ordre des 100 chaînes est
  celui des fichiers parity_1 … parity_100.

## Sources

Détail, citations et URL dans `sources.md`.

- Kavulich, Van Deren, Schlosshauer, Phys. Lett. A 388, 127032 (2021),
  arXiv:2101.01238 ; données Zenodo 4440318 (parity, ANU).
- Root, Becker, arXiv:2401.12250 ; données Zenodo 10.5281/zenodo.10542216.
- Haw et al., Phys. Rev. Applied 3, 054004 (2015), arXiv:1411.4512 (hachage
  AES-128 de l'ANU).
- Kelsey, Brandão, Peralta, Draft NISTIR 8213 (2019) ; impulsions
  https://beacon.nist.gov/beacon/2.0/chain/2/pulse/1950000 à 1958191.
- Shalm et al., Phys. Rev. Lett. 115, 250402 (2015), arXiv:1511.03189.
- NIST SP 800-22 rév. 1a (2010).
- Calcul : `analyse.py`, `resultats.json`, `telecharger.py` (ce dossier).
