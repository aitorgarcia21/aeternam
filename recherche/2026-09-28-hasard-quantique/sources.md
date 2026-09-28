# Test n° 4 : sources

Chaque affirmation factuelle du test n° 4, avec sa source primaire. Les nombres
calculés viennent de `resultats.json` (produit par `analyse.py`) ; les fichiers
de `donnees/` sont refaits par `telecharger.py`, qui vérifie leurs empreintes.
Consulté le 28 septembre 2026.

## Données testées

### 1. Parity QRNG : bits quantiques bruts, sans post-traitement

- Jeu de données : J. T. Kavulich, B. P. Van Deren, M. Schlosshauer, Zenodo,
  fichier `parity.zip` (md5 `9dd06b096f135f067d8e6af30b446c13`, identique à
  celui publié par Zenodo), licence CC BY 4.0.
  https://zenodo.org/records/4440318
- Article : Phys. Lett. A 388, 127032 (2021), https://doi.org/10.1016/j.physleta.2020.127032 ;
  version ouverte arXiv:2101.01238, https://arxiv.org/abs/2101.01238
  - Affiliation : Department of Physics, University of Portland (Oregon).
  - § II.A.2 : bits tirés de mesures conjointes sur des paires de photons
    intriqués en polarisation (conversion paramétrique de type I) ;
    « The output from our QRNG is not postprocessed in any way » ; parité des
    comptages de quatre détecteurs pendant τ = 0,1 s, quatre bits par
    intervalle, environ 26 bits/s ; une seule chaîne de 6,4 × 10^6 bits,
    coupée en 100 chaînes de 64 000 bits, chacune répétée en boucle dans les
    fichiers `parity_k` jusqu'à 1 677 721 600 bits.
  - Le même paragraphe indique que l'inégalité de Bell–CHSH est violée mais
    que le test n'est pas « loophole-free » : la source n'est pas certifiée.
- Description détaillée de la source : Van Deren, Kavulich, Schlosshauer,
  « Parity-based, bias-free optical quantum random number generation with
  min-entropy estimation », J. Opt. Soc. Am. B 37, 2088 (2020),
  https://arxiv.org/abs/2006.11425
- Vérifié par nous (`telecharger.py`) : dans chacun des 100 fichiers, les
  8 000 premiers octets se répètent exactement avec une période de 8 000
  octets ; on garde ces 8 000 octets, dans l'ordre parity_1 … parity_100.
  L'ordre des bits dans l'octet (poids fort d'abord) est une convention ; les
  tests n'en dépendent pas pour leur validité.

### 2. IBM « Basic QRNG » : bits quantiques bruts

- Jeu de données : « QRNG Trial Sequences », Zenodo, DOI
  10.5281/zenodo.10542216, fichier `S_2023_trials.zip` (md5
  `c76329c507922b97b3ce0a9b67162610`), licence CC BY 4.0 : « The raw binary
  outputs from the results of various quantum random number generator
  algorithms ran on various IBM quantum computers ».
  https://zenodo.org/records/10542216
- Article : O. Root, M. Becker, « Does True Randomness Exist? Efficacy
  Testing IBM Quantum Computers via Statistical Randomness », arXiv:2401.12250,
  https://arxiv.org/abs/2401.12250
  - § II.A : Basic QRNG = un qubit initialisé dans l'état 0, une porte de
    Hadamard, une mesure ; le résultat est stocké classiquement.
  - § II.C : les auteurs constatent un biais vers 0 et l'attribuent à
    l'initialisation dans l'état 0 et à une porte de Hadamard imparfaite.
  - § II.D : un « essai » = 8 192 exécutions du circuit (« shots »), rendues
    dans l'ordre chronologique ; les fichiers « combined » sont des essais
    mis bout à bout ; neuf machines (Belem, Jakarta, Lagos, Lima, Manila,
    Nairobi, Oslo, Perth, Quito).
- Utilisé : `combined_sequences/combined_Basic_QRNG_<machine>.txt` pour les
  neuf machines (caractères « 0 » et « 1 »), compactés 8 bits par octet.

### 3. ANU QRNG : sortie hachée (AES-128)

- Jeu de données : même dépôt Zenodo que 1, fichier `ANU.zip` (21 Go) ; nous
  n'en lisons, par requête HTTP Range, que le début du membre `anubits_1`
  (2 097 152 octets décompressés). https://zenodo.org/records/4440318
- Kavulich et al. 2021 (arXiv:2101.01238, § II.A.1) : 200 fichiers de l'ANU
  téléchargés en 2017, débit 5,7 Gbit/s, et « the raw output is
  significantly postprocessed […] with the aid of a cryptographic hashing
  algorithm ».
- Le hachage lui-même : J. Y. Haw et al., « Maximization of extractable
  randomness in a quantum random-number generator », Phys. Rev. Applied 3,
  054004 (2015), arXiv:1411.4512, https://arxiv.org/abs/1411.4512 , § II et
  annexe E : « A cryptographic hashing function (AES-128) is applied » ;
  sortie publiée sur https://qrng.anu.edu.au .
- Principe physique : T. Symul, S. M. Assad, P. K. Lam, Appl. Phys. Lett. 98,
  231103 (2011), arXiv:1107.4438, https://arxiv.org/abs/1107.4438
  (mesure homodyne des fluctuations du vide).
- API de l'ANU (vérifié le 28/09/2026) :
  - https://qrng.anu.edu.au/contact/api-documentation/ : l'ancienne API JSON
    (`https://qrng.anu.edu.au/API/jsonI.php?length=…&type=…&size=…`, au plus
    1 024 valeurs par requête) « will be scaled back and eventually
    retired » ; le nouveau service est « ANU Quantum Numbers », hébergé sur
    AWS (https://quantumnumbers.anu.edu.au).
  - Test direct : l'ancienne API répond (4 octets obtenus), mais une requête
    de 1 024 blocs de 1 024 octets a été coupée au bout de 60 s puis de
    120 s : inutilisable pour des dizaines de mégabits. Le nouveau point
    d'accès `https://api.quantumnumbers.anu.edu.au` renvoie
    `403 {"message":"Forbidden"}` sans clé d'API. Les conditions (gratuité,
    quotas) ne sont pas lisibles sans JavaScript et n'ont pas été vérifiées.
  - https://qrng.anu.edu.au/contact/faq/ : génération à 5,7 Gbit/s ; « How
    do we know that we have true randomness? We don't. »
  - Sans importance pour le verdict : la sortie de l'ANU est hachée de toute
    façon.

### 4. NIST Randomness Beacon 2.0 : sortie hachée (SHA-512)

- Impulsions : https://beacon.nist.gov/beacon/2.0/chain/2/pulse/<index>,
  index 1 950 000 à 1 958 191 (8 192 impulsions, 20 septembre 2026 à partir de
  18:06 UTC), toutes avec `cipherSuite` 0 et `statusCode` 0.
- Documentation de l'API (points d'accès par impulsion, par date, dernière
  impulsion ; pas d'archive en bloc documentée) :
  https://csrc.nist.gov/Projects/interoperable-randomness-beacons/beacon-20
- J. Kelsey, L. T. A. N. Brandão, R. Peralta, « A Reference for Randomness
  Beacons », Draft NISTIR 8213 (mai 2019), https://doi.org/10.6028/NIST.IR.8213-draft
  (PDF : https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8213-draft.pdf)
  - champ F9 : « localRandomValue — the hash() of two or more high-quality
    random bit sources » ;
  - champ F18 : « precommitmentValue — the hash() of the next pulse's
    localRandomValue » (vérifié par `analyse.py` sur les 8 191 couples
    consécutifs) ;
  - « Promise 2 » : randLocal = hash() d'au moins deux sorties de
    générateurs indépendants ;
  - figure 2 : RNG #1 (« on chip »), RNG #2 et, en option, RNG #3
    (« Quantum ») ; cipherSuite 0 = SHA-512. Le document ne dit pas quels
    générateurs sont en service aujourd'hui ; nous ne l'affirmons pas.
  - Remerciements : NIST a mis au point en 2017 un générateur fondé sur les
    probabilités de détection de photons.

## Données brutes envisagées mais non utilisées

- Test de Bell « loophole-free » du NIST 2015 : L. K. Shalm et al., Phys.
  Rev. Lett. 115, 250402 (2015), arXiv:1511.03189,
  https://arxiv.org/abs/1511.03189 . Les données brutes (fichiers d'horodatage
  binaires, plusieurs Go) sont publiques :
  https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-3
  Écartées : les choix de mesure y sont le XOR de deux sources physiques et
  d'une source pseudo-aléatoire fixée à l'avance (films, séries, décimales de
  π) (Shalm et al., p. 3) ; ils ne sont donc pas du hasard quantique pur, et
  les résultats de détection suivent des lois physiques non uniformes
  (corrélations de Bell, faible taux de détection) qui ne se prêtent pas à
  une batterie de tests de bits uniformes.
- Autres tests de Bell sans échappatoire (Delft 2015, ETH 2023) : non
  examinés dans ce test.

## Méthodes

- NIST SP 800-22 rév. 1a, « A Statistical Test Suite for Random and
  Pseudorandom Number Generators for Cryptographic Applications » (avril 2010),
  https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
  - Tests § 2.1 à 2.15, paramètres et probabilités de la section 3.
  - Annexe B, p. B-1 à B-3 : p-valeurs publiées pour 10^6 bits de π, e, √2,
    √3 (et une suite SHA-1, non utilisée). `analyse.py` les reproduit toutes
    (64 valeurs) à 1,5 × 10^-6 près, sauf le test des gabarits chevauchants
    (écart ≤ 3 × 10^-5).
  - Deux constantes du code de référence diffèrent du texte : π0 = 0,01047 au
    lieu de 0,010417 (complexité linéaire, § 2.10.4) et les anciennes
    probabilités 0,367879 ; 0,183940 ; … au lieu de 0,364091 ; 0,185659 ; …
    (gabarits chevauchants, § 2.8.4 et 3.8). Les valeurs de l'annexe B ne
    sont reproduites qu'avec les constantes du code ; l'analyse utilise
    celles du texte.
- Distribution de la complexité linéaire d'une suite aléatoire (nombre de
  suites de longueur n et de complexité L = 2^min(2n−2L, 2L−1), résultat
  classique attribué à Rueppel) : non reprise d'une source ici, mais
  vérifiée par énumération exhaustive des 4 096 suites de 12 bits dans
  `analyse.py` ; la moyenne ≈ n/2 est aussi celle du § 2.10 de SP 800-22.
- Berlekamp-Massey : J. L. Massey, « Shift-register synthesis and BCH
  decoding », IEEE Trans. Inf. Theory 15, 122 (1969),
  https://doi.org/10.1109/TIT.1969.1054260
- Mersenne Twister, récurrence linéaire de degré 19 937 sur GF(2) :
  M. Matsumoto, T. Nishimura, ACM TOMACS 8, 3 (1998),
  https://doi.org/10.1145/272991.272995 ; observé dans `analyse.py`
  (complexité linéaire exactement 19 937 à la décimation 64).
- Correction de Holm (procédure pas à pas de Bonferroni, valable quelle que
  soit la dépendance entre tests) : S. Holm, Scand. J. Statist. 6, 65 (1979),
  https://www.jstor.org/stable/4615733
- Extracteur de von Neumann (paires 01 → 0, 10 → 1, 00 et 11 jetées) : décrit
  et programmé dans `analyse.py` ; sert seulement de diagnostic.
- Gamma incomplète : même méthode que le code de référence de SP 800-22, qui
  renvoie à Numerical Recipes in C (SP 800-22, § 5 et réf. [6]).
- LCG x ← 1664525 x + 1013904223 mod 2^32 : exemple de générateur congruentiel
  32 bits ; ses propriétés utilisées ici (détecté ou non) sont calculées par
  `analyse.py`, pas reprises d'une source.
- Trinômes primitifs x^20 + x^3 + 1 et x^31 + x^3 + 1 : vérifiés dans
  `analyse.py` (période 2^20 − 1 observée ; complexité linéaire 20 et 31).

## Prédiction et portée

- Limite des tests statistiques : SP 800-22, résumé : « no set of statistical
  tests can absolutely certify a generator […] statistical testing cannot
  serve as a substitute for cryptanalysis » ; § 1.1.2 : un PRNG
  cryptographique doit rester imprévisible pour qui ignore la graine, alors
  que « the values produced by a PRNG are completely predictable if the seed
  and generation algorithm are known ». Un tel générateur est construit pour
  qu'aucun test connu ne le distingue du hasard : un test négatif ne peut
  donc pas l'exclure. Les contrôles PCG64 et SHA-256 de `analyse.py`
  l'illustrent.
- Contrôles positifs et négatifs : calculés par `analyse.py` (section
  `controles` de `resultats.json`).
