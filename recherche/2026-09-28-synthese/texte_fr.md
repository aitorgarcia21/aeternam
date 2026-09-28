# Avons-nous de meilleures raisons de nous croire simulés ?

Brouillon d'article : synthèse centrale du site. Chaque nombre calculé par
`modele.py` est écrit `[[clé]] = valeur`, où la clé est le chemin dans
`resultats.json` (indices de liste compris), pour que l'intégrateur pose les
marqueurs. Les nombres tirés de la littérature sont suivis de leur source. Les
citations sont traduites par nous ; l'original anglais et la page figurent dans
`sources.md`, qui donne pour chaque référence le passage vérifié.

Description : perception, conscience, faisabilité, argument de Bostrom, physique,
métaphysique ; ce que valent, une fois vérifiées à la source, les raisons de penser
que notre monde est produit par un autre système.

## Verdict

**Non.** En l'état, nous n'avons pas de meilleures raisons de penser que notre monde
et nos expériences sont produits par un autre système que de penser le contraire. La
simulation n'est pas une explication étayée de notre situation : aucune observation
ne la favorise, et le seul argument qui lui donne du poids, celui de Nick Bostrom,
conclut à une alternative dont l'issue dépend de grandeurs que personne ne connaît.
Bostrom l'écrit lui-même : son argument « ne cherche pas à établir que nous vivons
probablement dans une simulation ».

Ce « non » ne démontre pas le contraire. Nos trois tests, comme ceux de la
littérature, excluent des architectures précises, par exemple une grille cubique
naïve de maille égale ou supérieure à [[tests.test3.maille_exclue_toutes_orientations_m]] = 1,7 × 10⁻²⁶ m ;
aucun ne peut exclure une simulation conçue pour ne laisser aucune trace, et les
« preuves » d'impossibilité publiées reposent sur des prémisses qui ne sont pas
établies. Deux choses changeraient la réponse : une anomalie physique reproductible
dont aucune autre explication ne rende compte, ou le jour où nous saurions nous-mêmes
créer des êtres simulés conscients.

## Explication

Dire que nous vivons « dans une simulation » peut vouloir dire trois choses. Soit nos
esprits sont ailleurs et reçoivent les images d'un monde artificiel, comme dans le
film *Matrix*. Soit nous sommes nous-mêmes des personnages calculés par un ordinateur,
en même temps que le monde qui nous entoure. Soit, enfin, les lois de la nature
fonctionnent comme un programme, sans que personne ne l'ait écrit. Seules les deux
premières répondent vraiment à la question posée, car seules elles supposent un autre
système qui nous produit. Et même dans ces cas, notre monde ne deviendrait pas
irréel : les tables, les personnes et leurs souffrances resteraient ce qu'elles sont.
Ce qui changerait, c'est ce qui les fait exister.

Le premier argument est le plus intuitif : nos rêves paraissent réels, donc une vie
entière pourrait être une illusion bien faite. C'est vrai, et cela suffit à montrer
qu'on ne peut pas écarter l'idée d'un revers de main. Mais cela ne donne aucune raison
de la croire. Si un monde simulé et un monde qui ne l'est pas nous paraissent
exactement pareils, ce que nous percevons ne favorise ni l'un ni l'autre.

Deuxième point : pour que nous soyons des personnages calculés, il faudrait qu'un
calcul puisse ressentir quelque chose. Des philosophes le pensent, avec de bons
arguments ; d'autres le contestent, avec de bons arguments aussi. La question n'est
pas tranchée, et aucune expérience ne sait aujourd'hui la trancher.

Troisième point : pourrait-on seulement fabriquer un tel monde ? Calculer tout
l'Univers dans ses moindres détails est hors de portée de toute machine soumise à nos
lois physiques : il y faudrait bien plus d'énergie que l'Univers n'en contient. Les
partisans de l'idée répondent qu'il suffirait de calculer ce que les habitants
voient, au moment où ils le regardent. C'est concevable, mais une telle simulation
est faite pour ne laisser aucune trace. Elle échappe alors aux mesures, et les
mesures ne peuvent plus rien dire en sa faveur.

Le raisonnement qui a rendu l'idée célèbre, celui du philosophe Nick Bostrom en 2003,
est plus subtil. Si des civilisations avancées fabriquaient beaucoup de mondes
simulés peuplés d'êtres conscients, les êtres simulés seraient bien plus nombreux
que les autres, et nous serions probablement parmi eux. Mais le raisonnement contient
un « si ». Il ne dit pas si de telles civilisations existent, ni si elles le
voudraient. Bostrom conclut seulement que l'une de trois possibilités est vraie :
presque aucune civilisation n'atteint ce stade, ou presque aucune ne simule ses
ancêtres, ou nous sommes presque sûrement simulés. Il ne dit pas laquelle. Nos calculs
montrent que la réponse chiffrée dépend entièrement de ce qu'on suppose sur ces
inconnues : selon des choix qui paraissent tous raisonnables, on obtient presque une
certitude ([[scenarios.genereux.exact.confiance_c_fois_esperance]] = 0,999), environ
une chance sur sept ([[scenarios.ignorance.exact.confiance_c_fois_esperance]] = 0,14)
ou moins de trois chances sur cent
([[scenarios.ignorance_observateurs.exact.confiance_c_fois_esperance]] = 0,029). Un
astronome qui avait trouvé « un peu moins d'une chance sur deux » avait en réalité
retrouvé le pari à égalité qu'il avait posé au départ.

Quatrième point : la physique a-t-elle trouvé un indice ? Non. Les étrangetés de la
physique quantique, souvent citées, s'expliquent sans ordinateur caché : elles ne
dépendent pas de la présence d'un observateur conscient et ne réécrivent pas le
passé. Le fait que les lois de la nature semblent réglées pour permettre la vie ne
distingue pas un monde simulé d'un monde qui ne l'est pas. Et les tests qui cherchent
la trace d'un quadrillage de l'espace, dont les trois nôtres, n'ont rien trouvé : ils
excluent un quadrillage grossier, pas une simulation en général.

Au bout du compte, aucune observation ne penche pour la simulation, et l'argument qui
la soutient dépend de paris invérifiables. Nous n'avons donc pas de meilleures raisons
de nous croire simulés que de penser le contraire. Cela ne prouve pas que nous ne le
sommes pas : une simulation parfaite serait, par définition, indiscernable. La réponse
changerait si l'on découvrait une anomalie physique qu'aucune autre explication ne
rende, ou si nous savions un jour créer nous-mêmes des êtres simulés conscients.

## Analyse détaillée

### 1. De quelle simulation parle-t-on ?

Chalmers (*The Matrix as Metaphysics*, 2005) ramène l'hypothèse de *Matrix* à la
conjonction de trois thèses distinctes, complétée par l'idée que le calcul a été conçu
comme la simulation d'un monde. L'hypothèse computationnelle : « les processus
microphysiques, partout dans l'espace-temps, sont constitués par des processus
computationnels sous-jacents ». L'hypothèse de création : « l'espace-temps physique
et son contenu ont été créés par des êtres extérieurs à l'espace-temps physique ».
L'hypothèse corps-esprit : « mon esprit est constitué par des processus extérieurs à
l'espace-temps physique et reçoit ses entrées perceptives de processus situés dans
l'espace-temps physique ». Ces trois briques séparent les trois sens du mot.

- **(a) Un environnement artificiel perçu par une conscience extérieure** : création,
  calcul et esprit extérieur. C'est *Matrix*, ou le cerveau dans une cuve. La
  conscience n'y est pas simulée ; elle est ailleurs. Chalmers juge l'hypothèse
  corps-esprit cohérente, « même si la science contemporaine tend à suggérer qu'elle
  est fausse ».
- **(b) Un monde calculé qui contient ses propres êtres conscients** : création et
  calcul, les esprits étant eux-mêmes calculés. C'est le cas de Bostrom (2003), qui
  pose la prémisse d'indépendance du substrat : « pourvu qu'un système implémente le
  bon type de structures et de processus computationnels, il peut être associé à des
  expériences conscientes ». Il la prend « comme donnée », en reconnaissant qu'elle
  « n'est pas entièrement incontestée ».
- **(c) Un univers dont les lois sont computationnelles, sans concepteur** : le
  calcul seul. Chalmers cite Fredkin et Wolfram ; Lloyd (2002) en donne une version
  chiffrée (« si l'on choisit de regarder l'Univers comme effectuant un calcul », ce
  calcul compte environ 10¹²⁰ opérations élémentaires sur 10⁹⁰ bits) ; 't Hooft (2016)
  défend l'idée qu'un système classique, de type automate cellulaire, pourrait se
  cacher sous la mécanique quantique.

La question posée, « notre monde et nos expériences sont-ils produits par un autre
système ? », porte sur (a) et (b). Dans (c), rien d'extérieur ne produit le monde :
le calcul est la physique elle-même, et (c) peut être vraie sans que la réponse soit
oui. Une grille détectée ne départagerait d'ailleurs pas (b) de (c) : une physique
fondamentalement discrète produirait le même signal (test n° 1, section 7).

Deuxième précision : même vraie, (a) ou (b) ne rendrait pas le monde irréel. Selon
Chalmers, l'hypothèse de *Matrix* « n'est pas une hypothèse sceptique » : « même si je
suis dans une matrice, mon monde est parfaitement réel » ; si l'hypothèse
computationnelle est vraie, « il y a toujours des électrons et des protons », faits
de quelque chose de plus fondamental, comme les molécules sont faites d'atomes.
*Reality+* (2022) généralise : « la réalité virtuelle est une réalité authentique ».
Bostrom va dans le même sens : « on ne gagne aucune clarté à affirmer que le monde
n'est pas “vraiment réel” si nous sommes dans une simulation » ; il ne serait
qu'une partie de la réalité. La question ne porte donc pas sur l'existence des choses
mais sur leur constitution et leur origine causale. Elle peut recevoir deux sortes de
raisons : des arguments a priori, qui portent sur le nombre d'observateurs simulés
(section 5), et des traces observables (section 6). Les deux supposent d'abord qu'on
sache ce que vaut la perception (section 2), qu'un calcul puisse être conscient
(section 3) et qu'un tel monde puisse être construit (section 4).

### 2. L'argument par la perception

Il enchaîne trois propositions qu'il faut séparer.

**(P1) Une expérience peut paraître réelle sans être véridique.** C'est établi : le
rêve et l'illusion en sont des exemples quotidiens. Bostrom le rappelle : nos cerveaux,
sans aide technique, nous empêchent « d'ordinaire » de remarquer que nous rêvons, alors
que le rêve typique « fourmille des anomalies les plus fantastiques ».

**(P2) Une expérience équivalente à la nôtre pourrait être produite artificiellement.**
« Équivalente » veut dire : aussi riche, cohérente sur toute une vie, partagée par des
milliards de personnes qui se la confirment les unes aux autres, et compatible avec
toutes les mesures accumulées par les sciences. (P1) n'en fournit qu'un cas très
partiel, puisque le rêve est bref, privé et incohérent. (P2) est une conjecture, qui
dépend de la faisabilité (section 4) et, pour la version (b), de la conscience des
êtres calculés (section 3).

**(P3) La nôtre l'est.** (P3) ne suit pas de (P2) : qu'une chose soit possible ne dit
pas qu'elle est le cas.

En probabilités : si une version simulée reproduit exactement notre expérience E,
alors P(E | simulation) = P(E | pas de simulation), et le rapport de vraisemblance vaut
1. L'expérience ne déplace pas la balance, ni dans un sens ni dans l'autre. L'argument
par la perception est un argument sceptique, qui interdit la certitude, et non un
indice. Sa place légitime est de bloquer le rejet d'office : on ne peut pas écarter
l'hypothèse en invoquant la vivacité de nos perceptions. Sa limite est sa symétrie :
il soutiendrait aussi bien n'importe quelle hypothèse indécelable, le malin génie de
Descartes ou le « cerveau de Boltzmann », rapprochement que fait Vazza (2025). Il ne
distingue donc pas la simulation parmi les scénarios sceptiques, et s'il existe de
meilleures raisons de la croire, elles doivent venir d'ailleurs.

### 3. Un calcul peut-il être conscient ?

Pour la version (b), c'est la prémisse décisive. L'argument « peut-être le plus fort »
en sa faveur, selon son critique le plus récent lui-même, est celui de Chalmers (1995 ;
*The Conscious Mind*, 1996, chapitre 7). Le principe
d'invariance organisationnelle affirme qu'« étant donné un système qui a des
expériences conscientes, tout système qui a la même organisation fonctionnelle, à un
grain suffisamment fin, aura des expériences conscientes qualitativement
identiques ». L'argument des qualia évanescents le soutient : on remplace un à un les
neurones d'un cerveau par des puces qui ont exactement la même fonction
entrée-sortie ; le comportement et les jugements restent identiques à chaque étape.
Si l'expérience s'éteignait graduellement, un être parfaitement rationnel se
tromperait massivement sur sa propre expérience, ou ses croyances flotteraient
au-dessus de ses états physiques selon des règles arbitraires. Chalmers juge ces deux
options bien moins plausibles que la conservation de l'expérience. C'est un argument
de plausibilité, non une démonstration : les qualia évanescents sont « peut-être
logiquement possibles », écrit-il ; il les tient pour empiriquement invraisemblables.

Contre, Searle (1980) et la chambre chinoise : « instancier un programme d'ordinateur
n'est jamais, par soi-même, une condition suffisante de l'intentionnalité » ; un homme
peut exécuter le programme sans rien comprendre, et seule une machine dotée de
pouvoirs causaux équivalents à ceux du cerveau pourrait penser. Chalmers relève que
Searle admet d'ailleurs la possibilité des qualia évanescents.

L'objection la plus récente est celle de Mogensen (*Synthese*, en ligne le
5 novembre 2025). Il montre comment résister à l'argument des qualia évanescents en
admettant deux hypothèses : la conscience a des frontières vagues, et l'activité
neuronale consciente a une structure holistique. Il juge ces hypothèses
« plausibles », quoique « évidemment controversées », et estime avoir mis au jour
« d'importantes faiblesses » de l'argument.

La conscience d'un être calculé n'est donc ni démontrée ni réfutée, et aucune
expérience ne sait aujourd'hui la tester. Dans la suite, sa probabilité est un
paramètre libre, noté c. Il pèse directement. Si les êtres calculés ne sont pas
conscients, aucun être conscient n'est simulé, et comme nous nous savons conscients,
nous ne le serions pas : la confiance d'être simulé est au plus c. La version (a)
échappe à ce paramètre, mais au prix de l'hypothèse corps-esprit, que Chalmers
lui-même présente comme contraire à la tendance de la science contemporaine.

### 4. Un tel monde peut-il être construit ?

Les limites physiques du calcul sont connues. Selon Lloyd (2000), un « ordinateur
portable ultime » d'un kilogramme dans un litre effectuerait au plus 5,4258 × 10⁵⁰
opérations par seconde sur environ 2,13 × 10³¹ bits. Selon Lloyd (2002), l'Univers n'a
pu effectuer depuis son origine plus de 10¹²⁰ opérations sur 10⁹⁰ bits (10¹²⁰ bits si
l'on compte la gravitation) ; ces nombres sont aussi, écrit-il, des bornes inférieures
du nombre d'opérations et de bits nécessaires pour simuler l'Univers entier sur un
ordinateur quantique.

À l'autre extrême, Bostrom estime le coût d'une simulation de toute l'histoire mentale
de l'humanité : 10¹¹ personnes × 50 ans × 3 × 10⁷ secondes par an × 10¹⁴ à 10¹⁷
opérations par seconde et par cerveau. Il imprime « ≈ [10³³, 10³⁶] opérations » ; le
produit de ses propres facteurs donne [[faisabilite.bostrom_note10.produit_min]] = 1,5 × 10³⁴ à [[faisabilite.bostrom_note10.produit_max]] = 1,5 × 10³⁷,
soit [[faisabilite.bostrom_note10.facteur_ecart]] = 15 fois plus. L'écart ne change
rien à son argument, qui tolère selon lui plusieurs ordres de grandeur d'erreur. Le
nombre de Lloyd étant une borne inférieure, l'écart entre simuler les cerveaux et
simuler l'Univers est d'au moins [[faisabilite.decades_univers_sur_histoire_min]] = 83
à [[faisabilite.decades_univers_sur_histoire_max]] = 86 ordres de grandeur, selon
l'estimation retenue pour les cerveaux. Tout le débat sur la faisabilité tient dans cet
écart : que faut-il calculer ?

Vazza (2025) traite trois cas, en prenant la borne holographique pour la mémoire
nécessaire et le coût thermodynamique minimal de l'effacement d'un bit pour l'énergie.
L'Univers observable à la résolution de Planck demanderait 3,5 × 10¹²⁴ bits et
8,9 × 10¹⁰⁸ erg, quand l'Univers observable ne contient qu'environ 2,7 × 10⁷⁸ erg. La
Terre à la résolution de Planck demanderait, rien que pour initialiser le calcul,
l'énergie de masse de toutes les étoiles d'un amas globulaire. La Terre à la
résolution la plus grossière compatible avec les neutrinos de haute énergie qui la
traversent (1,2 × 10⁻²¹ cm) tiendrait en 1,65 × 10⁵¹ bits, mais une seconde simulée
demanderait, même avec un trou noir pour calculateur, 4,2 × 10¹³ s de calcul, soit
environ 1,4 × 10⁷ ans. Sa conclusion : il est « tout simplement impossible que cet
Univers soit simulé par un univers partageant les mêmes propriétés » ; seuls des
univers aux propriétés physiques « très différentes » le pourraient, et savoir si des
univers aux lois entièrement différentes le pourraient lui paraît « entièrement hors de
ce qui est scientifiquement testable ». Deux réserves figurent dans l'article même. La
borne holographique est un maximum d'information, et Vazza discute (section 4.4) le
cas où l'évolution se décrirait avec moins de bits, qu'il juge peu plausible à
plusieurs ordres de grandeur près. Et un scénario solipsiste, qui ne simulerait que le
cerveau d'un seul observateur, « ne pose pas de contrainte évidente » au calcul.

La réponse est venue de deux côtés. Edge et Brown (2026), dans un commentaire publié
par la même revue, notent que Vazza vise la simulation d'un monde partagé, à l'échelle
d'une planète et cohérent avec les expériences, alors que Bostrom ne s'engage que sur
le rendu d'une expérience subjective sans anomalie décelable. Bostrom lui-même, dans
la version 2025 de sa FAQ : « les critiques qui supposent qu'une simulation devrait
être entièrement complète (par exemple Vazza (2025)) manquent donc leur cible » ; les
détails seraient produits à la demande, et les simulateurs pourraient « facilement
nous empêcher de le découvrir ».

Le débat aboutit à un dilemme. Une simulation complète, qui calcule le monde à partir
de ses lois, est exclue, sous les hypothèses de Vazza, pour un simulateur soumis à
notre physique. C'est le cas des « simulations d'ancêtres » de Bostrom si leurs auteurs
vivent sous la même physique que leurs ancêtres. Une simulation minimale n'est pas
exclue, mais personne n'en a
chiffré le coût réel. L'estimation de Bostrom ne compte que les cerveaux, pas le
maintien d'un monde partagé et cohérent avec les collisionneurs, les neutrinos qui
traversent la Terre, les tests de Bell ou les ordinateurs, que Bostrom admet devoir
simuler « jusqu'au niveau des éléments logiques individuels ». Surtout, elle est
conçue pour ne laisser aucune trace : sa faisabilité, même accordée, ne fournit donc
aucune raison de croire qu'elle existe (section 8).

Deux travaux resserrent encore la prémisse technique. Bibeau-Delisle et Brassard
(2021) réécrivent l'argument sous la forme d'une équation « à la Drake » et montrent
que, si chaque niveau simulé consacre à son tour sa puissance de calcul à des
simulations, la fraction d'êtres simulés est bornée par l'efficacité du calcul,
« très probablement sous 50 % » ; ils rappellent que la fraction de Bostrom n'est
qu'une « probabilité de base » à corriger par des facteurs « pratiquement impossibles
à évaluer ». Birch (2013) relève une tension logique : l'argument suppose que nous
avons de bonnes raisons de croire ce que notre physique dit des limites du calcul, et
en même temps de mauvaises raisons de croire ce qu'elle dit de notre propre
constitution. Ce « scepticisme sélectif » n'étant pas justifié, il n'y a pas, conclut-il,
de bonne raison de croire la conclusion.

À l'inverse, les « preuves » d'impossibilité ne sont pas plus solides que leurs
prémisses. Celle de Vazza vaut pour un simulateur soumis à notre physique. Celle de
Faizal, Krauss, Shabir et Marino (2025) s'appuie sur les théorèmes d'incomplétude pour
conclure que l'hypothèse de la simulation est « logiquement impossible ». Elle suppose
que la réalité contient des vérités accessibles seulement par une « compréhension non
algorithmique », et qu'une simulation devrait reproduire la théorie complète du monde.
Or un simulateur n'a pas à démontrer les vérités de son monde, seulement à en calculer
l'évolution ; et l'indécidabilité apparaît déjà pour des programmes ordinaires, dont on
ne peut pas décider en général s'ils s'arrêteront. L'argument établit au mieux
qu'aucune théorie algorithmique complète ne décrit tout, pas qu'aucun calcul ne peut
produire un monde tel que le nôtre.

La faisabilité n'apporte donc pas de raison positive : elle élimine la version
complète sous notre physique et laisse ouverte une version minimale que rien ne peut
détecter. S'il y a une raison de croire à la simulation, elle doit venir du
dénombrement des observateurs.

### 5. L'argument de Bostrom

Notations de Bostrom : f_P, fraction des civilisations de niveau humain qui atteignent
un stade « posthumain » ; f_I, fraction des civilisations posthumaines intéressées par
les simulations d'ancêtres ; N_I, nombre moyen de simulations d'ancêtres qu'elles
exécutent. Si chaque simulation contient autant d'observateurs que l'histoire réelle
qu'elle reproduit, la fraction des observateurs à expérience humaine qui sont simulés
vaut (sa formule (*))

f_sim = f_P f_I N_I / (f_P f_I N_I + 1).

Comme N_I peut être astronomique, au moins une de trois propositions est vraie :
(1) f_P ≈ 0, (2) f_I ≈ 0, (3) f_sim ≈ 1. Un principe d'indifférence « faible » fait le
reste : si une fraction x des observateurs comme nous sont simulés et que rien ne nous
indique lesquels, notre confiance d'être simulés doit valoir x (sa formule (#)).

**Sa force.** Le trilemme ne demande pas que beaucoup de civilisations simulent.
Comme N_I est immense, la rareté des civilisations intéressées « doit être extrême en
proportion » pour que (3) soit fausse : quelques producteurs suffisent. C'est ce qui
rend l'argument difficile à écarter.

**Sa sensibilité.** f_sim ne dépend que du produit x = f_P f_I N_I, et presque en
tout ou rien : elle passe de 1 % à 99 % quand x varie de [[bostrom.x_pour_f_sim_1_pct]] = 0,010
à [[bostrom.x_pour_f_sim_99_pct]] = 99, soit sur [[bostrom.largeur_transition_decades]] = 4,0
ordres de grandeur. Hors de cette bande, elle vaut presque 0 ou presque 1. Or chacun
des facteurs est inconnu sur bien plus de quatre ordres de grandeur. Trois difficultés
s'y ajoutent.

**Les populations réelles.** Bostrom et Kulczycki (2011) ont signalé une faille de la
formule : elle suppose que les civilisations qui simulent et celles qui ne simulent
pas ont eu, avant le stade posthumain, la même population moyenne. Si les secondes
étaient bien plus peuplées, les trois propositions pourraient être fausses ensemble.
Leur réparation ajoute une hypothèse : l'écart de population n'est pas
« astronomiquement grand », par exemple pas plus d'un facteur un million. De même, une
simulation ne contient pas forcément autant d'observateurs que l'histoire réelle.
Bostrom envisage des « simulations de moi », qui ne simulent pleinement qu'une
personne, et calcule qu'il en faudrait environ cent milliards de fois plus que de
simulations d'ancêtres pour qu'elles l'emportent. Nous notons r le rapport entre le
nombre d'observateurs d'une simulation et la population réelle moyenne : r = 1 chez
Bostrom, r ≈ [[bostrom.r_me_simulation]] = 10⁻¹¹ pour une simulation d'une seule
personne.

**Les observateurs conscients.** C'est le paramètre c de la section 3. Avec cette
extension, qui est la nôtre, x = f_P f_I N_I r et la confiance d'être simulé vaut
c x / (1 + x).

**La règle de sélection.** Le principe (#) suppose que nous sommes un échantillon
quelconque des observateurs « comme nous ». Weatherson (2003) en distingue quatre
lectures : deux sont fausses, la troisième n'entraîne pas la conclusion, et la
quatrième ne l'entraîne qu'avec une hypothèse auxiliaire « que nous n'avons aucune
raison de croire ». Bostrom (2005) maintient le principe. Hartle et Srednicki (2007)
montrent, à propos de cosmologie, que se supposer « typique » n'est pas un résultat
de la physique mais un choix de probabilités a priori, qu'il faut rendre explicite.

**Ce que donnent les chiffres.** `modele.py` tire f_P, f_I, N_I et r selon des lois
log-uniformes (chaque ordre de grandeur également probable dans l'intervalle choisi)
et calcule exactement la loi de x ; un tirage Monte-Carlo à graine fixe la contrôle.
Ces lois ne sont pas des estimations : elles montrent comment la réponse suit le
choix.

| Hypothèses a priori | Confiance d'être simulé |
|---|---|
| f_P et f_I entre 0,1 et 1 ; N_I entre 10³ et 10⁹ ; r = 1 ; c = 1 | [[scenarios.genereux.exact.confiance_c_fois_esperance]] = 0,999 |
| idem, mais une chance sur deux que les êtres simulés soient conscients (c = 1/2) | [[scenarios.genereux_conscience.exact.confiance_c_fois_esperance]] = 0,50 |
| f_P et f_I inconnus sur dix ordres de grandeur chacun ; N_I entre 1 et 10⁹ | [[scenarios.ignorance.exact.confiance_c_fois_esperance]] = 0,14 |
| idem, avec N_I jusqu'à 10³⁰ | [[scenarios.ignorance_N_astronomique.exact.confiance_c_fois_esperance]] = 0,67 |
| comme la troisième ligne, avec r entre 10⁻¹¹ et 1 | [[scenarios.ignorance_observateurs.exact.confiance_c_fois_esperance]] = 0,029 |

Le point de bascule est net : avec N_I entre 1 et 10⁹, la confiance passe sous 1/2
dès qu'on admet ignorer f_P et f_I sur plus de [[largeur_critique_decades_par_fraction]] = 4,5
ordres de grandeur chacun. Le résultat lit la largeur des intervalles d'ignorance que
l'on se donne, pas une propriété du monde, et aucune donnée ne fixe ces intervalles.

**Kipping (2020).** Kipping traite l'argument par moyenne bayésienne de modèles. Il
regroupe (1) et (2) en une hypothèse « physique » H_P et leur oppose (3), H_S : une
réalité de base engendre λ simulations, dont une fraction p en engendre à son tour,
sur G générations, soit N_sim = (pλ − (pλ)^G) / (p − p²λ) simulations (son équation 1).
Avec des probabilités a priori égales, il obtient pour la réalité de base
P(base) = 1/2 + 1/(2(N_sim + 1)) (équation 22) : la probabilité d'être simulé est
inférieure à 1/2 et tend vers 1/2 quand N_sim croît. Nous avons reproduit ses
équations et vérifié leur cohérence interne (autotests). Pour p = 0,5, λ = 10 et G = 6,
par exemple, N_sim = [[kipping.exemples.0.N_sim]] = 7 810 et la probabilité d'être
simulé vaut [[kipping.exemples.0.P_simule_CES]] = 0,49994 ; elle vaut [[kipping.exemples.0.P_simule_nullipare]] = 0,474
si l'on tient compte de ce que nous n'avons encore créé aucune simulation (équation 27).

La lecture de ce résultat est simple. La seule donnée de Kipping, « je pense », a la
même probabilité sous les deux hypothèses : son facteur de Bayes vaut 1. La
probabilité a posteriori de H_S est donc égale à sa probabilité a priori π, et la
probabilité d'être simulé vaut π N_sim / (N_sim + 1), soit π à très peu près. Le
« presque 50 % » est le pari à égalité posé au départ. Avec π = 1/3, on obtient
[[kipping.prior_general_N_sim_1e9.1.P_simule_CES]] = 0,333 ; avec π = 1/10,
[[kipping.prior_general_N_sim_1e9.2.P_simule_CES]] = 0,100. Le simple découpage des
hypothèses décide : à parts égales entre les deux hypothèses de Kipping, on obtient
[[partition.deux_hypotheses_egales_kipping]] = 0,50 ; à parts égales entre les trois
propositions de Bostrom, comme celui-ci le suggérait en 2003,
[[partition.trois_propositions_egales_bostrom]] = 0,33. Kipping le reconnaît : l'a
priori égal « pourrait être contesté comme trop généreux » envers H_S, « modèle
intrinsèquement bien plus complexe ». Deux phrases de son article (sections 2.9 et 3
de la version arXiv) intervertissent « réalité de base » et « simulation » ; ses
équations et son résumé, eux, sont cohérents.

Une conséquence de Kipping mérite d'être retenue. Si nous créions un jour des
simulations peuplées d'êtres conscients, la probabilité d'être dans la réalité de base
tomberait à λ / N_sim (équation 32), soit [[kipping.exemples.0.P_base_si_nous_simulions_eq32]] = 0,0013
dans l'exemple ci-dessus. Bostrom le disait aussi : ce serait « un fort indice contre
(1) et (2) ». C'est la seule voie connue par laquelle l'argument deviendrait probant.

Enfin, Bostrom ne tire pas lui-même de probabilité de son argument. En 2005 : « la
disjonction est tout ce que l'argument de la simulation prétend montrer ; il ne cherche
pas à établir que nous vivons probablement dans une simulation ». En 2025, il accorde
une « probabilité substantielle » à l'hypothèse mais refuse d'avancer un nombre, qui
donnerait « une fausse impression de précision ».

L'argument donne donc à l'hypothèse un poids non nul, mais pas une valeur : cette
valeur est celle des probabilités a priori qu'on y injecte. Pour la déplacer, il
faudrait des données.

### 6. Ce que dit la physique

Plusieurs phénomènes sont souvent invoqués en faveur de la simulation. Voici ce
qu'ils montrent, et ce qu'ils ne montrent pas.

**Les inégalités de Bell.** En 2015, trois expériences les ont violées en fermant en
même temps les principales échappatoires : Hensen et al. (spins d'électrons distants
de 1,3 km ; 245 essais, S = 2,42 ± 0,20 alors que toute théorie réaliste locale impose
S ≤ 2 ; p = 0,039), Giustina et al. (photons ; probabilité sous le réalisme local au
plus 3,74 × 10⁻³¹) et Shalm et al. (photons ; p jusqu'à 5,9 × 10⁻⁹, ou 2,3 × 10⁻⁷ en
tenant compte de la prévisibilité des choix). Elles montrent qu'aucune théorie à la
fois locale et réaliste ne rend compte des corrélations observées, pourvu que les
réglages soient choisis indépendamment du système mesuré. Elles ne montrent pas que le
monde est calculé : un programme qui calcule l'état quantique global, comme n'importe
quel simulateur quantique, reproduit ces corrélations sans difficulté de principe, car
la localité en cause est celle de l'espace simulé, pas celle du calculateur. Elles ne
l'excluent pas non plus. L'échappatoire qui reste, et que Hensen et al. reconnaissent
(« aucune expérience de Bell ne peut exclure l'infinité des théories réalistes locales
concevables »), porte sur l'indépendance des réglages ; 't Hooft l'assume sous le nom
de superdéterminisme, pour un monde qui serait au fond un automate classique,
c'est-à-dire la version (c), sans concepteur.

**La décohérence.** Selon Zurek (2003), elle « est causée par l'interaction avec
l'environnement », qui « surveille » certaines grandeurs du système et détruit les
interférences. Aucune conscience n'est requise : Zurek rappelle que von Neumann,
London et Bauer, puis Wigner, avaient donné un rôle spécial à l'observateur conscient,
et que le formalisme quantique a conduit à une autre vue. L'image d'un monde « rendu
seulement quand on le regarde » ne correspond donc pas à la physique quantique : les
interférences disparaissent dès que l'information fuit dans l'environnement, qu'un
être conscient la recueille ou non. Zurek écrit que la décohérence « aide à résoudre »
le problème de la mesure, pas qu'elle le résout entièrement.

**Le choix retardé.** Jacques et al. (2007) ont réalisé l'expérience imaginée par
Wheeler avec des photons uniques : la configuration de l'interféromètre, ouverte ou
fermée, est tirée au sort par un générateur quantique, séparé au sens de la relativité
de l'entrée du photon. Les interférences apparaissent avec une visibilité de 94 % en
configuration fermée, et le chemin est déterminé avec moins de 1 % d'erreur en
configuration ouverte ; la nature s'y comporte « en accord avec les prédictions de la
mécanique quantique ». Ma, Kofler et Zeilinger (2016) en tirent la leçon générale :
ces effets peuvent « imiter une influence d'actions futures sur des événements
passés », mais « aucune interaction ni aucun signal physique, a fortiori vers le
passé, n'est nécessaire pour expliquer les résultats ». Il n'y a pas de passé réécrit,
donc pas d'indice d'un calcul fait après coup.

**L'ajustement fin.** Barnes (2012) passe en revue les cas où l'ensemble des lois,
des constantes et des conditions initiales compatibles avec la vie paraît très petit,
en précisant qu'il ne défend « aucune conclusion fondée sur l'ajustement fin ». Pour la
simulation, ce fait ne discrimine pas. Il serait attendu d'un simulateur qui veut des
observateurs, mais aussi d'un grand ensemble d'univers filtré par le fait même que nous
sommes là pour l'observer, ou d'une loi plus profonde encore inconnue. Et dans le cas
de Bostrom, où l'on simule ses ancêtres, la physique simulée recopie celle des
simulateurs : l'ajustement fin serait hérité, non expliqué (section 7).

**Les revendications d'indices positifs.** Vopson (2023) présente comme des indices
qui « semblent étayer » l'hypothèse d'un univers simulé une « seconde loi de
l'infodynamique », que l'entropie de l'information ne peut que rester constante ou
décroître, et un principe d'équivalence masse-énergie-information. Il note lui-même,
en tête de son résumé, le « manque de preuves » de l'hypothèse. En 2025, il dérive la
gravitation newtonienne comme une force entropique d'origine informationnelle, « en
accord » avec les travaux de Verlinde, et y voit un exemple de « compression de
données et d'optimisation computationnelle ». Ces deux lois sont ses propres
propositions : la seconde loi de l'infodynamique date de 2022, et le principe
d'équivalence de 2019, pour lequel il publiait en 2022 un protocole expérimental de
test. Surtout, montrer qu'une loi admet une formulation informationnelle ne dit pas
qu'elle est plus probable dans un monde simulé que dans un monde qui ne l'est pas : ce
rapport n'est calculé dans aucun des deux articles, et une physique informationnelle
relève au mieux de la version (c), sans autre système.

**Les grilles.** C'est la seule piste qui vise une signature propre au calcul. Beane,
Davoudi et Savage (2012, publié en 2014) supposent une simulation sur une grille
cubique avec le schéma le plus simple (Wilson, sans amélioration) ; la coupure du
spectre des rayons cosmiques leur donne une échelle inverse de maille d'au moins
10¹¹ GeV, et ils proposent de chercher une anisotropie cubique des rayons cosmiques
les plus énergétiques. Ils notent eux-mêmes qu'il « semble peu probable » que des
simulations autres que « les toutes premières » se passent de schémas améliorés, et
que l'amélioration « masque une grande partie » de notre capacité à tester
l'hypothèse. Nos trois tests :

- [Test n° 1](/fr/test-1/) : aucun retard des photons de GRB 221009A ; une grille
  cubique (schéma de Yee, temps continu) de maille supérieure à
  [[tests.test1.maille_max_pire_orientation_temps_continu_m]] = 2,5 × 10⁻²⁷ m est
  exclue dans la pire orientation, mais un pas de temps maximal laisse un angle mort
  le long des diagonales de la grille.
- [Test n° 2](/fr/test-2/) : les [[tests.test2.n_evenements]] = 100 rayons cosmiques
  les plus énergétiques de l'observatoire Pierre Auger ne montrent aucune symétrie de
  cube (p = [[tests.test2.p_valeur_l4]] = 0,20) ; mais un excès relatif de
  [[tests.test2.exces_axes_non_exclu_95]] = 0,96 le long des axes n'est pas exclu :
  le test ne voit que les motifs très marqués.
- [Test n° 3](/fr/test-3/) : [[tests.test3.n_sources]] = 8 sources de rayons gamma
  combinées ferment l'angle mort ; une grille cubique de maille égale ou supérieure à
  [[tests.test3.maille_exclue_toutes_orientations_m]] = 1,7 × 10⁻²⁶ m est exclue pour
  toute orientation et tout pas de temps. C'est encore
  [[tests.test3.rapport_sur_longueur_planck]] = 1,0 × 10⁹ fois la longueur de Planck.

Leur portée exacte : ils excluent une famille précise, celle des grilles cubiques à
schéma naïf, à maille fixe et sans terme de compensation, au-dessus de ces tailles. Ils
ne disent rien des grilles plus fines, des schémas d'ordre supérieur, des maillages non
cubiques ou adaptatifs, ni d'une simulation qui calcule à la demande. La FAQ de
Bostrom est explicite : il y a « peu de raisons de supposer » que des simulateurs
superintelligents utiliseraient « la technique de simulation grossière qu'un tel test
détecterait ». Même un signal positif ne désignerait pas un ordinateur : une physique
fondamentalement discrète, la version (c), produirait le même.

La physique n'a donc trouvé aucune trace positive, et ses résultats négatifs ne portent
que sur des architectures particulières. Leur poids dépend du poids qu'on donne a
priori à ces architectures, ce qui ramène à la section 8.

### 7. Arguments métaphysiques

**La souffrance et le choix.** Bostrom envisage qu'une interdiction éthique, « à
cause de la souffrance infligée aux habitants de la simulation », détourne les
civilisations avancées des simulations d'ancêtres ; il évoque aussi, en la qualifiant
de « tirée par les cheveux », une solution au problème du mal : les souvenirs de
souffrance seraient des illusions. La souffrance n'est un argument contre la
simulation que si l'on suppose des simulateurs bienveillants et maîtres de leur
œuvre ; contre des simulateurs indifférents ou curieux, sur lesquels l'argument de
Bostrom ne suppose rien, elle ne pèse rien. Elle ne devient pertinente que dans les
modèles où les participants choisissent d'entrer dans la simulation, c'est-à-dire la
version (a) avec une conscience extérieure qui aurait consenti. Mais on peut alors
ajuster les motifs supposés pour rendre compte de n'importe quelle souffrance, ce qui
retire à l'hypothèse tout pouvoir de test : une hypothèse qui s'accommode de tout ne
prédit rien.

**La régression.** La simulation n'explique pas l'existence d'un monde : elle la
reporte sur un monde de base, ses simulateurs et leurs machines. Si notre monde
réclame une explication, pour ses lois ou son ajustement fin, le monde de base la
réclame tout autant. Bostrom reconnaît que le statut de la thèse selon laquelle la
hiérarchie des simulations doit s'arrêter quelque part est « quelque peu obscur », et
Vazza juge la physique d'un univers simulateur très différent du nôtre hors de ce qui
est testable. On peut accepter qu'un niveau soit un fait brut, sans explication ; mais
alors rien n'oblige à placer ce niveau ailleurs que dans notre propre monde.

**La simplicité, traitée symétriquement.** Si l'on compte la simplicité, elle compte
contre l'hypothèse qui ajoute un monde, des agents, des machines et des motifs, à
moins que cet ajout ne réduise d'autant les faits inexpliqués, ce qu'il ne fait pas
puisqu'il les reporte. Si l'on invoque le caractère mathématique ou « compressible »
de nos lois comme indice de programme, il faut appliquer la même mesure à un monde non
simulé dont les lois seraient simples : il présenterait exactement le même caractère,
et le rapport de vraisemblance vaut 1. Quant à la neutralité, l'indifférence n'en est
pas une : on l'a vu à la section 5, parts égales entre deux hypothèses ou entre trois
propositions donnent une moitié ou un tiers.

**La valeur d'un monde simulé.** Chalmers soutient que la vie dans un monde virtuel
peut être « aussi bonne, en principe », et « pleinement signifiante » ; Bostrom, que
les implications d'une simulation ne seraient « pas si radicales », notre meilleur
guide restant « l'étude empirique ordinaire de l'univers que nous voyons ». Même si la
réponse était oui, les personnes, leurs souffrances et leurs choix resteraient réels.
L'enjeu pratique de la question est moindre qu'il n'y paraît ; raison de plus pour ne
pas lui donner une réponse plus assurée que ne le permettent les raisons.

### 8. Ce qu'il faudrait calculer

Notons S l'hypothèse « notre monde et nos expériences sont produits par un autre
système », D l'ensemble des données, θ les caractéristiques d'une simulation
(architecture, résolution, schéma, stratégie de rendu, motifs des simulateurs) et
π(θ | S) leur loi a priori. Alors

P(S | D) = P(D | S) P(S) / [P(D | S) P(S) + P(D | non S) (1 − P(S))],
avec P(D | S) = ∫ P(D | S, θ) π(θ | S) dθ.

**Ce que renseignent les tests.** Ils donnent P(D | S, θ) pour certains θ. Pour une
grille cubique naïve plus grossière que les bornes, un résultat nul est exclu :
P(D | S, θ) ≈ 0. Pour les autres θ, la simulation reproduit nos observations :
P(D | S, θ) = P(D | non S). Si w est le poids a priori des architectures exclues, le
facteur de Bayes vaut 1 − w. Les tests ne donnent pas w : ce poids n'est pas une
mesure, c'est un jugement sur ce que feraient des simulateurs. Avec w = 0,1, une
confiance de 1/2 passe à [[tests_de_grille.mise_a_jour.1.P_apres]] = 0,47. Pour la faire
tomber à 1/10, il faudrait w = [[tests_de_grille.w_pour_passer_de_un_demi_a_un_dixieme]] = 0,89,
c'est-à-dire tenir les grilles naïves pour presque la seule manière de simuler un
monde, ce que ni Beane et al. ni Bostrom ne soutiennent.

**Les arguments dépendants.** « Nos perceptions pourraient être fabriquées », « la
simulation serait indiscernable » et « la physique quantique ressemble à un rendu à la
demande » reposent sur la même hypothèse d'indiscernabilité ; « l'Univers est réglé
pour la vie » et « un concepteur l'a voulu » reposent sur la même hypothèse sur les
motifs des simulateurs. Formellement, P(D₁, D₂ | S) = P(D₁ | S) P(D₂ | S, D₁), et non
P(D₁ | S) P(D₂ | S) : multiplier les rapports de vraisemblance d'arguments qui
partagent une prémisse compte cette prémisse autant de fois qu'il y a d'arguments.

**L'équivalence observationnelle.** Pour la famille de simulations que décrivent
Bostrom et, à sa suite, Edge et Brown, qui produisent les apparences à la demande et
corrigent les incohérences, P(D | S, θ) = P(D | non S) pour toute donnée D que nous pouvons
recueillir : aucune expérience ne peut augmenter P(S). La confiance dans cette version
est alors exactement sa probabilité a priori, et la section 5 a montré que cette
probabilité n'est fixée par rien d'objectif. Les versions qui laissent des traces sont,
elles, soit contraintes par nos tests et par ceux de la littérature, soit exclues sous
notre physique par les bornes de Vazza. C'est la structure de la réponse : les versions
testables de l'hypothèse perdent du terrain, les versions intestables n'en gagnent
pas.

**Ce qui changerait la réponse.** Une anomalie reproductible, vue par plusieurs
messagers indépendants, avec une signature propre au calcul (par exemple une
anisotropie cubique de même orientation dans la lumière et dans les rayons cosmiques),
qu'aucune physique ordinaire, discrète ou continue, n'expliquerait. Ou notre propre
capacité à créer des simulations peuplées d'êtres dont nous aurions des raisons de
croire qu'ils sont conscients : c'est l'équation 32 de Kipping et le « fort indice » de
Bostrom.

## Bilan

| Question | Conclusion |
|---|---|
| De quelle simulation parle-t-on ? | Seules (a), une conscience extérieure branchée sur un monde artificiel, et (b), un monde calculé avec ses propres êtres conscients, supposent un autre système ; (c), des lois computationnelles sans concepteur, n'en suppose pas. Dans tous les cas, le monde resterait réel. |
| La perception suggère-t-elle la simulation ? | Non. Elle interdit de l'exclure par introspection ; pour une simulation indiscernable, le rapport de vraisemblance vaut 1. |
| Un calcul peut-il être conscient ? | Question ouverte : Chalmers pour, Searle contre, et Mogensen (2025) affaiblit l'argument des qualia évanescents. Pour la version (b), la confiance d'être simulé est au plus c. |
| Est-ce faisable ? | Une simulation complète sous notre physique est exclue (Vazza 2025) ; une simulation minimale ne l'est pas, mais son coût n'a jamais été chiffré et elle ne laisse, par construction, aucune trace. |
| L'argument de Bostrom établit-il la simulation ? | Non. Il établit une disjonction ; la probabilité qu'on en tire reflète les hypothèses a priori, de [[scenarios.ignorance_observateurs.exact.confiance_c_fois_esperance]] = 0,029 à [[scenarios.genereux.exact.confiance_c_fois_esperance]] = 0,999 dans nos scénarios ; le « presque 50 % » de Kipping est son a priori ; Bostrom refuse lui-même d'avancer un nombre. |
| La physique en montre-t-elle une trace ? | Non. Bell, la décohérence et le choix retardé s'expliquent sans calcul caché ; l'ajustement fin ne discrimine pas ; les indices revendiqués par Vopson ne calculent pas de rapport de vraisemblance ; les tests de grille, dont nos trois, ne trouvent rien. |
| La métaphysique la favorise-t-elle ? | Non. L'hypothèse reporte l'explication sans la réduire ; la simplicité, appliquée symétriquement, ne la favorise pas ; la souffrance ne pèse que dans les modèles où les participants choisissent. |
| Les tests ou les « preuves » démontrent-ils son impossibilité ? | Non. Les tests renseignent P(D \| S, θ) pour certains θ seulement, dont le poids n'est pas mesurable ; les preuves d'impossibilité valent sous leurs prémisses (notre physique pour Vazza, une réalité non algorithmique pour Faizal et al.). |

**Réponse à la question posée : non.** Nous n'avons pas, en l'état, de meilleures
raisons de penser que notre monde et nos expériences sont produits par un autre système
que de penser le contraire. Aucune donnée ne favorise la simulation ; l'argument qui la
rend concevable ne fixe pas sa probabilité ; les seules données pertinentes retirent
des versions de l'hypothèse sans jamais en ajouter. Elles ne démontrent pas pour autant
son impossibilité.

## Sources

1. D. J. Chalmers, « The Matrix as Metaphysics », dans C. Grau (dir.), *Philosophers Explore The Matrix*, Oxford University Press, 2005, p. 132-176, [doi:10.1093/oso/9780195181067.003.0009](https://doi.org/10.1093/oso/9780195181067.003.0009) ; texte de l'auteur : [consc.net/papers/matrix.html](https://consc.net/papers/matrix.html).
2. D. J. Chalmers, *Reality+ : Virtual Worlds and the Problems of Philosophy*, W. W. Norton et Allen Lane, 2022 (ISBN 9780393635805) ; présentation de l'auteur : [consc.net/reality](https://consc.net/reality/).
3. N. Bostrom, « Are We Living in a Computer Simulation? », *The Philosophical Quarterly* 53 (211), 243-255 (2003), [doi:10.1111/1467-9213.00309](https://doi.org/10.1111/1467-9213.00309) ; version de l'auteur, intitulée « Are You Living in a Computer Simulation? » : [simulation-argument.com/simulation.pdf](https://simulation-argument.com/simulation.pdf).
4. N. Bostrom, « The Simulation Argument: Reply to Weatherson », *The Philosophical Quarterly* 55 (218), 90-97 (2005), [doi:10.1111/j.0031-8094.2005.00387.x](https://doi.org/10.1111/j.0031-8094.2005.00387.x).
5. N. Bostrom, M. Kulczycki, « A Patch for the Simulation Argument », *Analysis* 71 (1), 54-61 (2011), [doi:10.1093/analys/anq107](https://doi.org/10.1093/analys/anq107).
6. N. Bostrom, « The Simulation Argument FAQ », version 2.0 (2025), [simulation-argument.com/faq.html](https://simulation-argument.com/faq.html), consultée le 28 septembre 2026.
7. B. Weatherson, « Are You a Sim? », *The Philosophical Quarterly* 53 (212), 425-431 (2003), [doi:10.1111/1467-9213.00323](https://doi.org/10.1111/1467-9213.00323).
8. J. B. Hartle, M. Srednicki, « Are we typical? », *Physical Review D* 75, 123523 (2007), [doi:10.1103/PhysRevD.75.123523](https://doi.org/10.1103/PhysRevD.75.123523), [arXiv:0704.2630](https://arxiv.org/abs/0704.2630).
9. D. Kipping, « A Bayesian Approach to the Simulation Argument », *Universe* 6 (8), 109 (2020), [doi:10.3390/universe6080109](https://doi.org/10.3390/universe6080109), [arXiv:2008.12254](https://arxiv.org/abs/2008.12254).
10. A. Bibeau-Delisle, G. Brassard, « Probability and consequences of living inside a computer simulation », *Proceedings of the Royal Society A* 477 (2247), 20200658 (2021), [doi:10.1098/rspa.2020.0658](https://doi.org/10.1098/rspa.2020.0658), [arXiv:2008.09275](https://arxiv.org/abs/2008.09275).
11. J. Birch, « On the ‘Simulation Argument’ and Selective Scepticism », *Erkenntnis* 78 (1), 95-107 (2013), [doi:10.1007/s10670-012-9400-9](https://doi.org/10.1007/s10670-012-9400-9).
12. D. J. Chalmers, « Absent Qualia, Fading Qualia, Dancing Qualia », dans T. Metzinger (dir.), *Conscious Experience*, Imprint Academic, 1995, [consc.net/papers/qualia.html](https://consc.net/papers/qualia.html) ; repris dans *The Conscious Mind*, Oxford University Press, 1996, chapitre 7.
13. J. R. Searle, « Minds, brains, and programs », *Behavioral and Brain Sciences* 3 (3), 417-424 (1980), [doi:10.1017/S0140525X00005756](https://doi.org/10.1017/S0140525X00005756).
14. A. L. Mogensen, « How to resist the Fading Qualia Argument », *Synthese* 206, 252 (2025), [doi:10.1007/s11229-025-05338-3](https://doi.org/10.1007/s11229-025-05338-3).
15. S. Lloyd, « Ultimate physical limits to computation », *Nature* 406, 1047-1054 (2000), [doi:10.1038/35023282](https://doi.org/10.1038/35023282), [arXiv:quant-ph/9908043](https://arxiv.org/abs/quant-ph/9908043).
16. S. Lloyd, « Computational Capacity of the Universe », *Physical Review Letters* 88, 237901 (2002), [doi:10.1103/PhysRevLett.88.237901](https://doi.org/10.1103/PhysRevLett.88.237901), [arXiv:quant-ph/0110141](https://arxiv.org/abs/quant-ph/0110141).
17. F. Vazza, « Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation », *Frontiers in Physics* 13, 1561873 (2025), [doi:10.3389/fphy.2025.1561873](https://doi.org/10.3389/fphy.2025.1561873).
18. E. Edge, C. A. Brown, « Commentary: Astrophysical constraints on the simulation hypothesis for this Universe: why it is (nearly) impossible that we live in a simulation », *Frontiers in Physics* 14, 1808725 (2026), [doi:10.3389/fphy.2026.1808725](https://doi.org/10.3389/fphy.2026.1808725).
19. M. Faizal, L. M. Krauss, A. Shabir, F. Marino, « Consequences of Undecidability in Physics on the Theory of Everything », *Journal of Holography Applications in Physics* 5 (2), 10-21 (2025), [arXiv:2507.22950](https://arxiv.org/abs/2507.22950).
20. G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*, Springer, collection Fundamental Theories of Physics, 2016, [doi:10.1007/978-3-319-41285-6](https://doi.org/10.1007/978-3-319-41285-6), [arXiv:1405.1548](https://arxiv.org/abs/1405.1548).
21. B. Hensen et al., « Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres », *Nature* 526, 682-686 (2015), [doi:10.1038/nature15759](https://doi.org/10.1038/nature15759), [arXiv:1508.05949](https://arxiv.org/abs/1508.05949).
22. M. Giustina et al., « Significant-Loophole-Free Test of Bell’s Theorem with Entangled Photons », *Physical Review Letters* 115, 250401 (2015), [doi:10.1103/PhysRevLett.115.250401](https://doi.org/10.1103/PhysRevLett.115.250401), [arXiv:1511.03190](https://arxiv.org/abs/1511.03190).
23. L. K. Shalm et al., « Strong Loophole-Free Test of Local Realism », *Physical Review Letters* 115, 250402 (2015), [doi:10.1103/PhysRevLett.115.250402](https://doi.org/10.1103/PhysRevLett.115.250402), [arXiv:1511.03189](https://arxiv.org/abs/1511.03189).
24. W. H. Zurek, « Decoherence, einselection, and the quantum origins of the classical », *Reviews of Modern Physics* 75, 715-775 (2003), [doi:10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715), [arXiv:quant-ph/0105127](https://arxiv.org/abs/quant-ph/0105127).
25. V. Jacques et al., « Experimental Realization of Wheeler’s Delayed-Choice Gedanken Experiment », *Science* 315, 966-968 (2007), [doi:10.1126/science.1136303](https://doi.org/10.1126/science.1136303), [arXiv:quant-ph/0610241](https://arxiv.org/abs/quant-ph/0610241).
26. X.-S. Ma, J. Kofler, A. Zeilinger, « Delayed-choice gedanken experiments and their realizations », *Reviews of Modern Physics* 88, 015005 (2016), [doi:10.1103/RevModPhys.88.015005](https://doi.org/10.1103/RevModPhys.88.015005), [arXiv:1407.2930](https://arxiv.org/abs/1407.2930).
27. L. A. Barnes, « The Fine-Tuning of the Universe for Intelligent Life », *Publications of the Astronomical Society of Australia* 29 (4), 529-564 (2012), [doi:10.1071/AS12015](https://doi.org/10.1071/AS12015), [arXiv:1112.4647](https://arxiv.org/abs/1112.4647).
28. M. M. Vopson, « The second law of infodynamics and its implications for the simulated universe hypothesis », *AIP Advances* 13, 105308 (2023), [doi:10.1063/5.0173278](https://doi.org/10.1063/5.0173278).
29. M. M. Vopson, « Is gravity evidence of a computational universe? », *AIP Advances* 15, 045035 (2025), [doi:10.1063/5.0264945](https://doi.org/10.1063/5.0264945).
30. M. M. Vopson, « The mass-energy-information equivalence principle », *AIP Advances* 9, 095206 (2019), [doi:10.1063/1.5123794](https://doi.org/10.1063/1.5123794) ; « Experimental protocol for testing the mass–energy–information equivalence principle », *AIP Advances* 12, 035311 (2022), [doi:10.1063/5.0087175](https://doi.org/10.1063/5.0087175) ; M. M. Vopson, S. Lepadatu, « Second law of information dynamics », *AIP Advances* 12, 075310 (2022), [doi:10.1063/5.0100358](https://doi.org/10.1063/5.0100358).
31. S. R. Beane, Z. Davoudi, M. J. Savage, « Constraints on the Universe as a Numerical Simulation », *European Physical Journal A* 50, 148 (2014), [doi:10.1140/epja/i2014-14148-0](https://doi.org/10.1140/epja/i2014-14148-0), [arXiv:1210.1847](https://arxiv.org/abs/1210.1847) (2012).
32. aeternam, [test n° 1](/fr/test-1/), [test n° 2](/fr/test-2/), [test n° 3](/fr/test-3/) : scripts et résultats dans `recherche/2026-09-28-grille-lhaaso/`, `recherche/2026-09-28-rayons-cosmiques/` et `recherche/2026-09-28-dispersion-directionnelle/`.
