# Les démonstrations du « oui » tiennent-elles ?

Description : nous avons refait, pas à pas, les calculs publiés par Melvin Vopson et
d'autres pour appuyer l'idée que notre univers est simulé ; aucun ne démontre ce qu'il
annonce.

Chaque nombre calculé vient de `resultats.json` (clé en commentaire juste après) ; chaque
citation, de `sources.md`, qui donne l'original anglais et la page consultée. Les
citations sont traduites par nous.

## Verdict

**Non.** Aucune des démonstrations examinées n'établit que nous vivons dans une
simulation : la plus récente repose sur une erreur mathématique vérifiable, la
dérivation thermodynamique de 2023 sur une égalité qui ne vaut pas pour les
transformations réelles, et sa réparation de 2025 sur des hypothèses non démontrées.

Ce « non » porte sur ces démonstrations, pas sur l'hypothèse elle-même. Qu'un
raisonnement échoue ne prouve pas que la simulation est impossible ; cela montre
seulement que ces articles ne la rendent pas plus probable. Les travaux de Campbell et de
Wolpert, souvent cités dans le même sens, ne prétendent d'ailleurs pas l'établir : les
premiers proposent des expériences, le second démontre une possibilité logique.

## Explication

Melvin Vopson, physicien à l'université de Portsmouth, défend depuis 2022 une « seconde
loi de l'infodynamique » : dans tout système qui porte de l'information, le désordre de
cette information ne pourrait que rester stable ou diminuer. Il y voit la marque d'un
univers qui, comme un ordinateur, économise ses ressources, donc un indice en faveur de
la simulation. Nous avons repris trois de ses démonstrations.

La première, publiée en mai 2026, veut prouver qu'un système atteint son désordre le
plus faible quand toutes ses pièces se répètent le même nombre de fois. C'est l'inverse
qui est vrai. Prenons six objets de deux sortes. Trois et trois, c'est la répartition la
plus mélangée possible, donc la plus imprévisible ; cinq et un, c'est la plus ordonnée,
car on devine presque à coup sûr la sorte d'un objet pris au hasard. Le calcul exact le
confirme dans chacun des cas que nous avons passés en revue, sans exception. L'article
reconnaît d'ailleurs, quelques lignes plus haut, que la répartition égale donne le
désordre maximal. Ses exemples de polygones (le carré « plus ordonné » que le
quadrilatère quelconque) restent justes, mais pour une autre raison, que nous
démontrons, et qui ne dit rien d'une loi générale.

La deuxième, publiée en 2023, part d'un fait admis : l'univers n'échange de chaleur avec
rien. Vopson en tirait que son désordre total ne peut pas changer ; comme le désordre
physique augmente, il fallait qu'autre chose, l'information, compense en diminuant. Or
l'absence d'échange de chaleur n'empêche pas le désordre de croître. Un gaz enfermé dans
une boîte isolée, qui s'échappe d'un coup dans une moitié vide, ne reçoit ni chaleur ni
travail, et pourtant son désordre augmente d'une quantité que tout manuel calcule. Vopson
l'a reconnu en 2025.

La troisième est sa réparation de 2025. Elle ajoute des termes de pertes et conclut de
nouveau que le désordre de l'information diminue. Mais la conclusion ne sort pas du
calcul : elle vient d'hypothèses posées en chemin (les pertes diminuent avec le temps,
la température de l'univers est constante), que l'article affirme sans les établir, et
dont l'une contredit une phrase du même texte, où la température « doit décroître ». Le
calcul lui-même, fait correctement, laisse le résultat indéterminé.

Enfin, on lit souvent qu'un univers qui « compresse » l'information trahirait un
ordinateur soucieux d'économie. Trois choses différentes se mélangent là. Qu'une quantité
diminue n'implique pas qu'il y ait compression. Qu'il existe une compression n'implique
pas qu'un calculateur l'ait voulue : une compression parfaite ne change d'ailleurs rien à
la quantité d'information transmise, elle l'écrit seulement plus court. Et seule une
compression qui perd de l'information la réduit vraiment.

## Analyse détaillée

### 1. Le lemme de Vopson (2026) : un maximum pris pour un minimum

Vopson (*Entropy* 28, 564, 18 mai 2026, section 2) considère \(N\) éléments répartis en
\(n\) catégories de multiplicités \(g_i \ge 1\), avec \(\sum_i g_i = N\) (équation 3), et
l'entropie (équation 5)

$$ I(g) = \log_2 N - \frac{1}{N}\sum_{i=1}^{n} g_i \log_2 g_i . $$

C'est exactement l'entropie de Shannon de la loi \(p_i = g_i/N\) :
\(I = -\sum_i p_i \log_2 p_i\) (ses équations 2 et 4). Il cherche le minimum de \(I\) à
\(N\) fixé, pose \(f = \frac1N\sum g_i \log_2 g_i\) (équation 6), écrit que « le minimum de
I est obtenu quand [f] est maximal », puis annule la dérivée du lagrangien
\(L = f - \lambda(\sum g_i - N)\) et obtient \(g_i = N/n\) (équation 14). Il conclut :
« quand n ≠ 1, l'entropie informationnelle minimale est non nulle et la condition est
donnée par (14) », et, dans le résumé comme dans la conclusion, que la configuration
d'entropie minimale est celle des multiplicités égales.

**Le point stationnaire est un maximum.** Sur l'ensemble admissible
\(\{g \in \mathbb{R}_{>0}^n : \sum g_i = N\}\), avec \(N\) constant,

$$ \frac{\partial I}{\partial g_i} = -\frac{1}{N}\left(\log_2 g_i + \frac{1}{\ln 2}\right),
\qquad
\frac{\partial^2 I}{\partial g_i\,\partial g_j} = -\frac{\delta_{ij}}{N \ln 2 \; g_i}. $$

La hessienne est diagonale à termes strictement négatifs, donc définie négative : pour
toute direction admissible \(d \ne 0\) (\(\sum d_i = 0\)),
\(d^{\mathsf T} \nabla^2 I \, d = -\sum_i d_i^2/(N\ln 2\, g_i) \lt 0\). \(I\) est
strictement concave sur un ensemble convexe ; son unique point stationnaire, qui est
bien \(g_i = N/n\) (le gradient y est proportionnel à \((1,\dots,1)\), donc orthogonal à
la contrainte), est son **maximum global**, qui vaut \(\log_2 n\). La méthode de Lagrange
ne distingue pas un maximum d'un minimum ; c'est la condition du second ordre qui
tranche, et elle n'est pas examinée dans l'article. L'étape « minimum de I ⇔ maximum de
f » est juste ; l'erreur est de prendre le point stationnaire de \(f\), qui est convexe,
pour son maximum, alors que c'est son minimum.

L'article écrit lui-même, dans la même section, que « la maximisation de l'entropie de
Shannon pour des lois de probabilité uniformes est un résultat bien établi ». Or, à
\(N\) et \(n\) fixés, multiplicités égales et loi uniforme sont la même chose : le lemme
contredit le résultat que l'article rappelle.

**Contre-exemple.** \(N = 6\), \(n = 2\) :

- \((3,3)\) : \(I = 1\) bit <!-- multiplicites.contre_exemple_N6.egal_3_3_bits --> ;
- \((4,2)\) : \(I = 0{,}918295834\) bit <!-- multiplicites.contre_exemple_N6.g_4_2_bits --> ;
- \((5,1)\) : \(I = 0{,}650022422\) bit <!-- multiplicites.contre_exemple_N6.g_5_1_bits -->.

La répartition égale donne la plus grande valeur, pas la plus petite.

**Énumération exhaustive.** Pour \(N\) de 2 à 15 et \(n\) de 2 à \(\min(5, N)\), soit
50 cas <!-- multiplicites.enumeration.nb_cas --> et 4 928 compositions
<!-- multiplicites.enumeration.nb_compositions_examinees --> examinées une à une, le
maximum de \(I\) est atteint par la répartition la plus égale
\((\lceil N/n\rceil, \dots, \lfloor N/n\rfloor)\) et le minimum par
\((N-n+1, 1, \dots, 1)\). Sur les 42 cas <!-- multiplicites.enumeration.nb_cas_non_triviaux -->
où toutes les compositions n'ont pas la même entropie, la répartition la plus égale est
le maximum dans 42 <!-- multiplicites.enumeration.nb_cas_ou_repartition_la_plus_egale_est_le_maximum -->
et le minimum dans 0 <!-- multiplicites.enumeration.nb_cas_ou_repartition_la_plus_egale_est_le_minimum -->.
Le vrai minimum à \(N\) et \(n\) fixés est donc la répartition la plus déséquilibrée ; à
\(N\) seul fixé, c'est \(n = 1\), \(I = 0\), cas que l'article mentionne à part.

**Contrôle numérique de la concavité.** En 2 000 points
<!-- multiplicites.concavite.nb_points --> tirés au hasard (graine fixe), avec des
directions admissibles aléatoires, la dérivée seconde par différences finies est
toujours négative (la plus grande vaut \(-1{,}8 \times 10^{-3}\)
<!-- multiplicites.concavite.derivee_seconde_max_observee -->) et s'écarte de la formule
analytique d'au plus \(1{,}3 \times 10^{-4}\) en valeur relative
<!-- multiplicites.concavite.ecart_relatif_max_numerique_vs_hessienne -->.

### 2. Les polygones : conclusion juste, raison différente

La section 3 décrit un polygone à \(m\) sommets par ses \(m\) longueurs et ses \(m\)
angles, soit \(N = 2m\) caractères, longueurs et angles restant des caractères
distincts (le polygone régulier a « seulement deux caractères distincts, n = 2 »). Nous
retrouvons ses valeurs : triangle quelconque 2,585 bits
<!-- polygones.formes.triangle_quelconque.I_bits -->, quadrilatère quelconque 3 bits
<!-- polygones.formes.quadrilatere_quelconque.I_bits -->, pentagone quelconque 3,322 bits
<!-- polygones.formes.pentagone_quelconque.I_bits --> (l'article imprime 3.321, valeur
tronquée), polygones réguliers 1 bit <!-- polygones.formes.carre.I_bits -->.

Soit \(K\) l'espèce d'un caractère tiré au hasard (longueur ou angle) : elle vaut
« longueur » avec probabilité exactement \(1/2\). Par la règle de chaîne,

$$ I = H(K) + H(X \mid K) = 1 + \tfrac12 H_{\text{côtés}} + \tfrac12 H_{\text{angles}}
\;\ge\; 1 \text{ bit}, $$

avec égalité si et seulement si toutes les longueurs sont égales et tous les angles
égaux, c'est-à-dire pour le polygone régulier. Le script vérifie l'identité sur neuf
formes, dont le triangle isocèle (1,918295834 bit
<!-- polygones.formes.triangle_isocele.I_bits -->), le rectangle et le losange (1,5 bit
<!-- polygones.formes.rectangle.I_bits -->).

La contrainte géométrique change donc la portée de l'objection. Elle sauve le résultat
de la section 3 : parmi les polygones à \(m\) côtés, le régulier a bien l'entropie la
plus basse. Mais l'équation (14) n'y est pour rien. Dès que \(n = 2\), la seule
répartition géométriquement possible est \((m, m)\) ; l'accord avec « \(g_i = N/n\) » est
automatique, et ce qui fait baisser l'entropie est la diminution de \(n\) (de 6 à 2 pour
le triangle), non l'égalité des multiplicités. Le lemme général de la section 2 reste
faux, et le résultat sur les polygones, une propriété de la mesure choisie, ne dit rien
d'une tendance physique vers le minimum.

### 3. Vopson (2023) : l'égalité \(dS = \delta Q/T\) ne vaut que pour une transformation réversible

Nous n'avons pas pu lire l'article de 2023 (*AIP Advances* 13, 105308) lui-même : l'éditeur
et le dépôt de Portsmouth refusent l'accès automatisé (voir `sources.md`). Sa dérivation
est connue par le résumé qu'en donne l'auteur en 2025 : l'univers « n'échange de chaleur
avec rien » ; la relation \(dQ = T\,dS\) a été utilisée ; « on en a conclu que dS = 0 » ;
le terme d'entropie manquant serait celui de l'information, d'où
\(\partial S_{\text{info}}/\partial t = -\partial S_{\text{phys}}/\partial t \le 0\).

L'inégalité de Clausius donne seulement \(dS \ge \delta Q/T\), avec égalité pour une
transformation réversible. **Contre-exemple** : une mole de gaz parfait dans une enceinte
rigide et isolée se détend dans le vide jusqu'à doubler son volume. \(Q = 0\), \(W = 0\),
donc \(\Delta U = 0\) et la température ne change pas ; l'entropie étant une fonction
d'état, on la calcule sur le chemin réversible isotherme de mêmes états extrêmes :

$$ \Delta S = n R \ln\frac{V_2}{V_1} = R \ln 2 = 5{,}763146322 \ \text{J/K}
\quad\text{alors que}\quad \int \frac{\delta Q}{T} = 0 . $$
<!-- thermodynamique.detente_libre.Delta_S_J_par_K_arrondi -->

avec \(R = k_B N_A = 8{,}31446261815324\) J·mol⁻¹·K⁻¹
<!-- thermodynamique.detente_libre.R_J_par_mol_K -->, produit de deux constantes exactes
du SI. Les notes du MIT le disent : « l'égalité entre ΔS et dQ/T ne vaut que pour une
transformation réversible ». Une absence d'échange de chaleur n'impose donc pas une
entropie constante, et il n'y a rien à compenser. Vopson l'admet en 2025 : sans
réversibilité, « on ne peut plus en déduire que dS = 0, ce qui annulerait la nécessité
d'introduire l'entropie informationnelle ».

### 4. La réparation de 2025 : un signe qui ne suit pas des équations

Vopson (*IPI Letters* 3(1), N6-N9, 10 janvier 2025) sépare la chaleur en deux parts,
\(dQ_{\text{phys}} + dQ_{\text{info}} = 0\) (équation 5), écrit
\(dQ_{\text{phys}} = T dS_{\text{phys}} - dU^{\text{loss}}_{\text{phys}}\) (équation 8),
puis « suppose une relation semblable pour le processus informationnel » (équation 9).
Il obtient (équation 11)

$$ dS_{\text{info}} = -\,dS_{\text{phys}} + \frac{dU^{\text{loss}}}{T},
\qquad dS_{\text{phys}} \ge 0,\quad dU^{\text{loss}} \ge 0 , $$

la positivité des pertes étant écrite dans l'article (« dULoss est une quantité
positive »). Quatre points.

1. **Le signe est indéterminé.** Le membre de droite est la différence de deux termes
   positifs. \(dS_{\text{info}} \le 0\) exige \(dU^{\text{loss}} \le T\,dS_{\text{phys}}\),
   que rien n'établit. Le script tabule les cas : pour \(dS_{\text{phys}} = 1\) et
   \(dU^{\text{loss}}/T = 2\), \(dS_{\text{info}} = 1 \gt 0\)
   <!-- thermodynamique.reponse_2025_signe.cas.3.dS_info -->. Rapportée au temps, (11)
   donne \(\dot S_{\text{info}} = -\dot S_{\text{phys}} + \dot U^{\text{loss}}/T\), où le
   taux de pertes \(\dot U^{\text{loss}} \ge 0\) s'oppose à la conclusion.
2. **L'équation (12) mélange deux opérations.** Les deux premiers termes y sont divisés
   par \(dt\), le troisième dérivé par \(d/dt\) comme si la perte infinitésimale
   \(dU^{\text{loss}}\) était une fonction du temps. C'est ce qui fait apparaître, en (13),
   la variation du taux de pertes au lieu du taux de pertes lui-même.
3. **Même en admettant (13), la conclusion repose sur des hypothèses.** Le deuxième terme
   n'est négatif que si « la perte diminue avec le temps », ce qui est posé, pas démontré.
   Le troisième est positif (\(T\) décroît) ; l'argument selon lequel il « ne peut
   compenser » car il « varie en 1/T² » ne compare pas des grandeurs : le rapport du
   troisième au deuxième terme vaut
   \(-\,dU^{\text{loss}}\,\dot T / (T\, \tfrac{d}{dt}dU^{\text{loss}})\), qui dépend des
   taux et non d'une puissance de \(T\). Enfin, l'hypothèse « T = constante » contredit la
   phrase précédente du même texte (« T doit décroître avec le temps ») et n'est
   justifiée par aucun calcul.
4. **Le terme informationnel est postulé.** Ni \(Q_{\text{info}}\), ni
   \(S_{\text{info}}\) de l'univers, ni \(U^{\text{loss}}_{\text{info}}\) ne reçoivent de
   définition indépendante ou de mesure ; l'équation (9) est une hypothèse, annoncée comme
   telle.

La phrase finale, « la seconde loi de l'infodynamique se déduit à l'identique, que le
processus soit réversible ou irréversible », n'est donc pas démontrée par l'article.

### 5. Compression : trois affirmations à ne pas confondre

Source à quatre symboles de probabilités \(1/2, 1/4, 1/8, 1/8\) : entropie \(H = 1{,}75\) bit
<!-- codage.H_source_bits -->. Le code préfixe \(0, 10, 110, 111\) est injectif et
décodable sans ambiguïté ; nous calculons l'entropie **sur la loi des mots de code
réellement émis** (le script du tiers dont nous sommes partis recopiait l'entropie
d'entrée, ce qui aurait masqué une perte) : 1,75 bit
<!-- codage.H_mots_de_code_bits -->. Sur les 64 messages de trois symboles
<!-- codage.messages_de_3_symboles.nb -->, l'entropie est de 5,25 bits avant comme après
codage <!-- codage.messages_de_3_symboles.H_codes_bits -->. Une application injective
conserve les probabilités, donc l'entropie des messages complets.

Ce qui change, c'est la longueur : 1,75 bit par symbole <!-- codage.longueur_moyenne_prefixe_bits -->
au lieu de 2 <!-- codage.longueur_moyenne_fixe_bits --> pour un code de longueur fixe.
L'entropie **par bit émis** augmente même, de 0,875 <!-- codage.entropie_par_bit_code_fixe -->
à 1 <!-- codage.entropie_par_bit_code_prefixe --> : dans le flux compressé, 0 et 1 sont
équiprobables (fréquence des 1 : 1/2 <!-- codage.frequence_des_1_code_prefixe -->).
Compresser sans perte n'abaisse donc pas l'entropie de l'information ; cela la rend plus
dense.

Seul un codage non injectif la réduit. En confondant les deux symboles rares
(\(c, d \mapsto 11\)), l'entropie de la sortie tombe à 1,5 bit
<!-- codage.avec_perte.H_apres_bits -->, et 0,25 bit <!-- codage.avec_perte.information_perdue_bits -->
d'information est définitivement perdu : on ne sait plus lequel des deux a été émis.

D'où trois affirmations distinctes :

1. **une quantité informationnelle diminue** : fait mesurable, qui demande une définition
   de la quantité et une mesure ;
2. **il existe une compression** : propriété d'un codage, qui n'implique pas la
   précédente (sans perte, l'entropie des messages est conservée) ;
3. **un simulateur optimise son calcul** : hypothèse sur une cause, qui n'est impliquée
   ni par 1 ni par 2. Pour qu'une observation la favorise, il faudrait montrer qu'elle est
   plus probable avec un simulateur que sans ; aucun des articles examinés ne calcule ce
   rapport.

### 6. Campbell et al., Wolpert : ce qu'ils affirment réellement

Campbell, Owhadi, Sauvageau et Watkinson (« On testing the simulation theory »,
arXiv:1703.00058, 2017) « décrivent des expériences conceptuelles de dualité
onde-corpuscule destinées à tester la théorie de la simulation », sous l'hypothèse qu'un
simulateur aux ressources finies ne « rendrait » le réel qu'au moment de l'observation.
Ils écrivent : « nous ne pouvons pas prédire le résultat des expériences proposées ». Ce
sont des protocoles, pas des résultats ; nous n'avons trouvé aucun résultat de ces
expériences publié avec comité de lecture.

Wolpert (« Implications of computer science theory for the simulation hypothesis »,
arXiv:2404.16050, version 5 du 19 mars 2026) démontre, par le second théorème de
récursion de Kleene, qu'il est « mathématiquement possible » que nous soyons une
simulation, y compris exécutée par nous-mêmes. Il précise ne s'intéresser qu'à « la
possibilité logique » d'un tel système, sans examiner s'il en existe un « dans notre
univers ». Un résultat de possibilité n'est pas un indice.

## Limites

- Le texte intégral de Vopson (2023) n'a pas été lu : sa dérivation est connue par le
  résumé qu'en fait l'auteur en 2025 ; la numérotation « section V » n'est pas vérifiée
  par nous.
- Nous n'avons examiné que trois démonstrations de Vopson ; ses autres arguments
  (données numériques, génomes, règles de Hund, gravité) ne sont pas audités ici, et
  l'erreur de 2026 ne les invalide pas à elle seule.
- L'énumération couvre un domaine fini ; la validité générale vient de la preuve de
  concavité, que l'énumération et le contrôle numérique ne font qu'illustrer.
- La détente libre est un modèle de gaz parfait, pas un modèle cosmologique : elle suffit
  à réfuter l'implication générale « Q = 0 ⇒ ΔS = 0 », pas à décrire l'entropie de
  l'univers.
- Nous n'avons pas vérifié la parution en revue des travaux de Campbell et al. et de
  Wolpert, lus en préprint.
- Réfuter une démonstration n'établit pas le contraire de sa conclusion : une
  simulation reste possible, comme le montre Wolpert, et aucun de ces calculs ne peut
  l'exclure.

## Fichiers

- `analyse.py` : calculs et autotests, bibliothèque standard seulement ;
  `python3 analyse.py --out resultats.json` (moins d'une seconde).
- `resultats.json` : résultats, valeurs citées (`valeurs_citees`) et détail de
  l'énumération.
- `sources.md` : références complètes, passages vérifiés en anglais, statuts, et
  corrections apportées à l'analyse d'un tiers.
