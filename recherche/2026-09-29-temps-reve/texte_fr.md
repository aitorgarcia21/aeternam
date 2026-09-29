# Le temps d'un rêve

*Description : nous avons rassemblé toutes les mesures qui comparent le temps vécu dans un rêve au temps réellement dormi, refait les calculs et analysé une base ouverte de réveils en laboratoire : le rêve ne va jamais plus vite que l'horloge.*

*Brouillon. Chaque nombre tiré de `resultats.json` est suivi de sa clé en commentaire HTML ; les autres viennent des publications citées dans `sources.md`.*

## Verdict

**Non.** Aucune mesure ne montre qu'un rêve fasse vivre plus de temps qu'il n'en dure : combinées, les mesures donnent un rapport entre temps vécu et temps dormi de 0,84 <!-- verdict.F_global -->, et tout rapport supérieur à 0,92 <!-- verdict.X_borne_sup_95 --> est exclu à 95 % ; dans la variante de calcul la moins favorable, tout rapport supérieur à 1,03 <!-- meta_sensibilite.borne_sup_95_la_plus_haute --> reste exclu. Le rêve va au pas de l'horloge, ou un peu plus lentement. Même « par moments », rien ne tient : dans la base ouverte que nous avons analysée, aucun des 112 <!-- donnees_ouvertes_tononi.n_bornees --> récits datés ne décrit une expérience plus longue que le temps écoulé depuis le réveil précédent, et la seule étude qui annonce une forte accélération la mesure sur des récits faits après coup, que son autrice attribue elle-même à la mise en ordre du récit.

## Explication

L'idée est ancienne. En 1861, Alfred Maury raconte un long rêve de Révolution qui finit sous la guillotine, au moment précis où un morceau de son lit lui tombe sur la nuque : tout ce rêve, pense-t-il, a tenu dans l'instant du choc. Si c'était vrai en général, le cerveau saurait déjà faire vivre beaucoup de temps en peu de temps, et notre projet « Une vie en une nuit » partirait d'un acquis. Nous avons donc cherché toutes les expériences qui mesurent la chose, au lieu de la supposer.

Ces expériences sont peu nombreuses, parce que la durée d'un rêve est difficile à connaître : le rêveur ne la raconte qu'une fois réveillé. Trois méthodes contournent l'obstacle.

La première réveille les dormeurs à un moment choisi. En 1957, William Dement et Nathaniel Kleitman ont réveillé leurs volontaires cinq ou quinze minutes après le début du sommeil où l'on rêve le plus, et leur ont demandé : avez-vous rêvé cinq ou quinze minutes ? Ils ont bien répondu dans 92 réveils sur 111. Si le rêve accélérait le temps, un rêve de cinq minutes serait souvent vécu comme en durant quinze : cela n'est arrivé que dans 6 <!-- dement_kleitman.faux_apres_5min --> réveils sur 51, à peine plus souvent que l'erreur inverse. Nous avons tiré de ces réponses le rapport entre durée vécue et durée dormie : 0,89 <!-- dement_kleitman.frontiere_geometrique.F -->.

La deuxième marque le temps de l'intérieur du rêve. En 1968, David Koulack a envoyé de petites impulsions électriques au poignet de dormeurs en plein rêve, puis les a réveillés trente secondes ou trois minutes plus tard. Quand le rêve racontait l'impulsion, il demandait : c'était il y a plutôt trente secondes, ou plutôt trois minutes ? Onze réponses sur douze étaient justes. Si le rêve accélérait le temps d'un facteur six, trente secondes auraient paru trois minutes.

La troisième, la plus précise, utilise des rêveurs lucides, qui savent qu'ils rêvent et peuvent agir selon une consigne. Avant de dormir, on leur demande de compter jusqu'à dix, vingt et trente, de marcher un nombre donné de pas ou de faire un enchaînement de gymnastique, et de signaler le début et la fin par un mouvement convenu des yeux, que les appareils enregistrent pendant le sommeil. On sait donc exactement combien de temps l'action a pris. Résultat : la même action prend plus de temps en rêve qu'éveillé, de 23 % pour la gymnastique à 52 % pour la marche. Le rêve ne condense pas l'action, il l'étire.

Enfin, nous avons analysé nous-mêmes une base de données ouverte, où des dormeurs réveillés au hasard de la nuit ont estimé combien de temps durait l'expérience qu'ils étaient en train de vivre. Aucun n'a décrit plus d'une heure, et aucun n'a décrit une durée plus longue que le temps écoulé depuis qu'on l'avait réveillé la fois précédente.

Mises ensemble, ces mesures donnent un rapport de 0,84 <!-- verdict.F_global --> : une minute de rêve fait vivre un peu moins d'une minute. Pour vivre une vie entière en une nuit, il faudrait un rapport de 87 660 <!-- verdict.facteur_necessaire_une_vie_en_une_nuit -->. Le rêve ordinaire n'est donc pas un raccourci du temps ; si ce projet aboutit un jour, ce ne sera pas en s'appuyant sur une accélération que le rêve posséderait déjà.

## Analyse détaillée

### 1. La grandeur mesurée

On note \(F\) le rapport entre la durée vécue et la durée réellement dormie :

$$F = \frac{\text{durée vécue}}{\text{durée dormie}}.$$

\(F > 1\) serait une compression du temps (plus de temps vécu que de temps écoulé), \(F = 1\) un rêve au pas de l'horloge, \(F \lt 1\) un ralentissement. Les calculs portent sur \(\ln F\), symétrique entre accélération et ralentissement.

### 2. Règle de décision

Écrite dans l'en-tête de `analyse.py` avant la première exécution (les ordres de grandeur publiés étaient connus, pas les résultats combinés) :

- **oui** si la borne inférieure unilatérale à 95 % du facteur global (effets aléatoires) dépasse 1, ou si, dans les données ouvertes, la borne inférieure unilatérale à 95 % de la proportion d'expériences dont le vécu dépasse *certainement* le dormi dépasse 5 % ;
- **non** sinon, si la borne supérieure unilatérale à 95 % \(X\) du facteur global est inférieure à 2 ;
- **indéterminé** dans les autres cas.

### 3. Données ouvertes : 124 durées vécues, aucune au-delà du temps disponible

La base DREAM (Wong et al., *Nature Communications*, 2025) réunit 20 études de réveils provoqués avec enregistrement du sommeil. Sa table générale ne contient aucune durée vécue ; un seul jeu en fournit une en unités de temps, celui de Siclari, Baird, Perogamvros, Boly, LaRocque et Tononi (Madison, jeu n° 13, licence CC BY 4.0, archive vérifiée par empreinte SHA-256). Les dormeurs y sont réveillés à des moments tirés au hasard, en sommeil lent de stade 2, et répondent à la question « For how long were you having continuous experiences before the alarm sound? » en six classes : 0 à 5 s, 5 à 10 s, 10 s à 1 min, 1 à 10 min, 10 min à 1 h, plus d'une heure.

Sur 124 <!-- donnees_ouvertes_tononi.n_estimations --> estimations, les effectifs par classe sont 21 <!-- donnees_ouvertes_tononi.effectifs_par_classe.1 -->, 22 <!-- donnees_ouvertes_tononi.effectifs_par_classe.2 -->, 39 <!-- donnees_ouvertes_tononi.effectifs_par_classe.3 -->, 36 <!-- donnees_ouvertes_tononi.effectifs_par_classe.4 -->, 6 <!-- donnees_ouvertes_tononi.effectifs_par_classe.5 --> et 0 <!-- donnees_ouvertes_tononi.effectifs_par_classe.6 -->. La durée réelle de l'expérience n'est pas connue, mais elle ne peut pas dépasser le temps écoulé depuis le réveil précédent du même dormeur, la même nuit, noté \(T_{\max}\) (heures d'horloge du fichier, écart pris modulo 24 h, nouvelle nuit au-delà de 6 h d'écart). Le vécu dépasse *certainement* le dormi quand la borne basse \(L\) de la classe déclarée vérifie \(L > T_{\max}\).

Pour 112 <!-- donnees_ouvertes_tononi.n_bornees --> estimations, \(T_{\max}\) est défini (les autres suivent le premier réveil de la nuit) ; il va de 14 <!-- donnees_ouvertes_tononi.dormi_max_min_minutes --> à 185 <!-- donnees_ouvertes_tononi.dormi_max_max_minutes --> minutes, médiane 39 <!-- donnees_ouvertes_tononi.dormi_max_mediane_minutes -->. Nombre de cas où \(L > T_{\max}\) : 0 <!-- donnees_ouvertes_tononi.n_vecu_depasse_certainement_dormi -->. Borne supérieure unilatérale à 95 % (Clopper-Pearson) de la proportion de tels cas : 2,6 % <!-- donnees_ouvertes_tononi.proportion_certaine_borne_sup_95 -->. Le plus grand rapport garanti \(L / T_{\max}\) vaut 0,4 <!-- donnees_ouvertes_tononi.rapport_vecu_min_sur_dormi_max_le_plus_grand -->.

Ce test ne peut voir qu'une compression grossière : \(T_{\max}\) est une borne haute, et l'expérience réelle peut être bien plus courte. Il établit seulement qu'en sommeil lent, aucune expérience vécue n'a été décrite comme plus longue que le temps matériellement disponible, et que de tels cas, s'ils existent, concernent moins de 2,6 % <!-- donnees_ouvertes_tononi.proportion_certaine_borne_sup_95 --> des expériences.

### 4. Dement et Kleitman (1957) : un facteur tiré des erreurs

Effectifs (original non lu ; trois sources secondaires concordantes, voir `sources.md`) : réveils après 5 min de sommeil paradoxal, 45 bonnes réponses sur 51 ; après 15 min, 47 sur 60. Modèle : la durée vécue \(S\) d'un rêve de durée réelle \(T\) vérifie

$$\ln S = \ln F + \ln T + \sigma\,\varepsilon, \qquad \varepsilon \sim \mathcal N(0,1),$$

et le rêveur répond « 15 min » si \(S > c\), avec \(c\) entre 5 et 15 min. Avec \(p_5\) la part des réveils à 5 min jugés « 15 » et \(p_{15}\) la part des réveils à 15 min jugés « 5 » :

$$\frac{\ln(c/5) - \ln F}{\sigma} = \Phi^{-1}(1-p_5), \qquad \frac{\ln(c/15) - \ln F}{\sigma} = \Phi^{-1}(p_{15}),$$

d'où \(\sigma = \ln 3 / [\Phi^{-1}(1-p_5) - \Phi^{-1}(p_{15})]\) et \(\ln F = \ln(c/5) - \sigma\,\Phi^{-1}(1-p_5)\). Avec \(p_5 = 6/51\), \(p_{15} = 13/60\) et la frontière naturelle \(c = \sqrt{5 \times 15}\) = 8,66 <!-- dement_kleitman.frontiere_geometrique.frontiere_min --> min : \(\sigma\) = 0,56 <!-- dement_kleitman.frontiere_geometrique.sigma_ln -->, \(F\) = 0,89 <!-- dement_kleitman.frontiere_geometrique.F -->, intervalle à 90 % (bootstrap paramétrique, 20 000 tirages) de 0,78 <!-- dement_kleitman.frontiere_geometrique.F_borne_inf_95 --> à 1,02 <!-- dement_kleitman.frontiere_geometrique.F_borne_sup_95 -->. Avec \(c\) = 10 min : \(F\) = 1,03 <!-- dement_kleitman.frontiere_arithmetique.F -->, borne supérieure 1,18 <!-- dement_kleitman.frontiere_arithmetique.F_borne_sup_95 -->.

Une borne qui ne dépend pas du modèle de bruit : si la durée vécue *médiane* d'un rêve de 5 min dépassait la frontière \(c\), au moins la moitié des réveils à 5 min seraient jugés « 15 min ». Or cette part vaut 12 % <!-- dement_kleitman.part_jugee_15_apres_5min -->, borne supérieure à 95 % 22 % <!-- dement_kleitman.part_jugee_15_apres_5min_borne_sup_95 -->. Donc \(F_{\text{médian}} \lt c/5\) : moins de 1,73 <!-- dement_kleitman.borne_robuste.F_median_max_frontiere_geometrique --> avec la frontière géométrique, moins de 3 <!-- dement_kleitman.borne_robuste.F_median_max_frontiere_15min --> même si le rêveur ne répondait « 15 » qu'au-delà de 15 min vécues.

Les erreurs existent dans les deux sens. Le modèle ajusté attribue à un rêve une probabilité de 0,42 <!-- dement_kleitman.frontiere_geometrique.proba_vecu_superieur_au_dormi_modele --> d'être vécu plus long qu'il n'a duré : c'est le bruit ordinaire d'une estimation de durée, compensé par autant de sous-estimations, pas une accélération.

### 5. Koulack (1968) : un repère dans le rêve

Choc électrique au poignet en sommeil paradoxal, réveil 30 s ou 3 min après ; quand le choc apparaît nettement dans le récit, le rêveur dit s'il remonte « plutôt à 30 s » ou « plutôt à 3 min ». Résultat publié : 11 bons jugements sur 12, chez 5 sujets. Taux d'erreur borné à 34 % <!-- koulack.taux_erreur_borne_sup_95 --> (unilatéral, 95 %). Une compression d'un facteur 6 <!-- koulack.rapport_des_durees_a_distinguer --> ferait paraître 30 s comme 3 min et renverserait les jugements à 30 s ; l'article ne dit pas combien des 12 cas étaient à 30 s, si bien que nous n'en tirons pas de facteur chiffré et ne l'intégrons pas à la combinaison.

### 6. Rêves lucides chronométrés : le temps vécu est plus lent

Erlacher, Schädlich, Stumbrys et Schredl (2014, tableau 2) mesurent la durée \(W\) d'une tâche à l'éveil et sa durée \(D\) en rêve lucide, bornée par des signaux oculaires gauche-droite-gauche-droite visibles sur l'enregistrement. Ce que le rêveur a vécu, exprimé en temps d'éveil, est \(W\) ; le temps dormi est \(D\) ; donc \(F = W/D\). L'erreur type de \(\ln F\) se tire du \(t\) apparié publié : \(\mathrm{ET}(D-W) = (D-W)/t\), et, par la méthode delta avec la corrélation inconnue bornée par Cauchy-Schwarz,

$$\mathrm{ET}(\ln F) \le \frac{\mathrm{ET}(D-W)}{D} + \frac{|D-W|}{W D}\,\frac{s_W}{\sqrt n}.$$

- Comptage jusqu'à 10, 20 et 30 (\(n = 5\)) : \(F\) = 0,79 <!-- erlacher.comptage.F -->, intervalle à 90 % (loi de Student) de 0,60 <!-- erlacher.comptage.F_borne_inf_95_t --> à 1,02 <!-- erlacher.comptage.F_borne_sup_95_t --> ;
- marche (\(n = 7\)) : \(F\) = 0,66 <!-- erlacher.marche.F -->, de 0,51 <!-- erlacher.marche.F_borne_inf_95_t --> à 0,84 <!-- erlacher.marche.F_borne_sup_95_t --> ;
- gymnastique (\(n = 8\), autre groupe) : \(F\) = 0,81 <!-- erlacher.gymnastique.F -->, de 0,72 <!-- erlacher.gymnastique.F_borne_inf_95_t --> à 0,92 <!-- erlacher.gymnastique.F_borne_sup_95_t -->.

L'étude antérieure d'Erlacher et Schredl (2004) trouve 39,9 % de temps en plus pour des flexions en rêve, soit \(F\) = 0,71 <!-- erlacher_schredl_2004_F_squats --> (sans écart type publié, donc hors combinaison) ; LaBerge (1985) rapporte un comptage jusqu'à dix « about the same » qu'à l'éveil, sans chiffres.

### 7. Combinaison

Échantillons indépendants retenus : comptage d'Erlacher (les mêmes personnes ont fait la marche, qui n'est donc pas ajoutée), gymnastique d'Erlacher, Dement et Kleitman (frontière géométrique). Pour les petits effectifs d'Erlacher, l'erreur type est multipliée par le rapport des quantiles de Student (\(n-1\) degrés de liberté) et normal. Moyenne pondérée de \(y_i = \ln F_i\) :

$$\hat\mu = \frac{\sum_i w_i y_i}{\sum_i w_i}, \quad w_i = \frac{1}{s_i^2 + \tau^2}, \quad X = \exp\!\big(\hat\mu + 1{,}645\,\mathrm{ET}(\hat\mu)\big),$$

avec \(\tau^2\) de DerSimonian-Laird. Hétérogénéité : \(Q\) = 0,90 <!-- meta.Q --> pour 2 <!-- meta.ddl --> degrés de liberté (\(p\) = 0,64 <!-- meta.p_heterogeneite -->), donc \(\tau^2\) = 0 <!-- meta.tau2 --> et les effets aléatoires coïncident avec les effets fixes. Poids : comptage 11 % <!-- meta.poids_effets_aleatoires.erlacher_comptage -->, gymnastique 47 % <!-- meta.poids_effets_aleatoires.erlacher_gymnastique -->, Dement et Kleitman 42 % <!-- meta.poids_effets_aleatoires.dement_kleitman -->.

Résultat : \(F\) = 0,84 <!-- meta.F_effets_aleatoires -->, intervalle à 95 % de 0,76 <!-- meta.F_effets_aleatoires_ic95_bilateral.0 --> à 0,94 <!-- meta.F_effets_aleatoires_ic95_bilateral.1 --> ; borne supérieure unilatérale à 95 % \(X\) = 0,92 <!-- meta.F_effets_aleatoires_borne_sup_95 --> ; probabilité unilatérale de \(F \ge 1\) sous l'estimation : \(p\) = 0,0007 <!-- meta.p_unilateral_F_superieur_a_1 -->.

### 8. Sensibilité

| Variante | \(F\) | Borne sup. 95 % |
|---|---|---|
| Principale | 0,84 <!-- meta.F_effets_aleatoires --> | 0,92 <!-- meta.F_effets_aleatoires_borne_sup_95 --> |
| Marche au lieu du comptage | 0,81 <!-- meta_sensibilite.marche_au_lieu_du_comptage.F_effets_aleatoires --> | 0,91 <!-- meta_sensibilite.marche_au_lieu_du_comptage.F_effets_aleatoires_borne_sup_95 --> |
| Frontière de Dement et Kleitman à 10 min | 0,89 <!-- meta_sensibilite.frontiere_arithmetique.F_effets_aleatoires --> | 1,03 <!-- meta_sensibilite.frontiere_arithmetique.F_effets_aleatoires_borne_sup_95 --> |
| Rêves lucides seuls | 0,81 <!-- meta_sensibilite.reves_lucides_seuls.F_effets_aleatoires --> | 0,91 <!-- meta_sensibilite.reves_lucides_seuls.F_effets_aleatoires_borne_sup_95 --> |
| Dement et Kleitman seul | 0,89 <!-- dement_kleitman.frontiere_geometrique.F --> | 1,02 <!-- meta_sensibilite.dement_kleitman_seul_borne_sup_95 --> |

Dans toutes les variantes, la borne supérieure ne dépasse pas 1,03 <!-- meta_sensibilite.borne_sup_95_la_plus_haute -->, très loin du seuil de 2 de la règle. Application de la règle : borne inférieure du facteur global 0,77 <!-- verdict.F_borne_inf_95 --> (non supérieure à 1) ; proportion certaine dans les données ouvertes, borne inférieure 0 <!-- donnees_ouvertes_tononi.proportion_certaine_borne_inf_95 --> (non supérieure à 5 %) ; \(X\) = 0,92 <!-- verdict.X_borne_sup_95 --> \(\lt 2\). Verdict : **non**.

### 9. Ce qui plaide pour le oui, examiné

- **Moiseeva (1975)** est la seule étude à annoncer une accélération : pour des rêves « with a complex structure », une « major overestimation of their duration » ; les facteurs 2 à 10, 25 à 50, voire 100, ne sont connus que par Erlacher et al. (2014), l'article étant fermé. La durée vécue y est reconstruite à partir du récit (« Estimation of the temporal structure of the dream was made from the verbal account of the subject »), et l'autrice conclut que le rêveur, en racontant, « tends to place the events in a certain temporal order which creates the effect of considerable acceleration of the time flow ». Sans effectif, sans incertitude, et sur un récit fait après coup, ce résultat ne peut pas entrer dans le calcul ; il décrit un effet du récit, pas une mesure du vécu.
- **Carlson, Feinberg et Goodenough (1978)** : des dormeurs estiment le temps écoulé depuis une image montrée avant de se rendormir ; estimations moyennes 61,6 min pour 38,7 min réelles, rapport 1,59 <!-- carlson_rapport_estimation_sur_reel -->. Il s'agit du temps écoulé, éveils compris (24 % du temps dans les intervalles surtout paradoxaux), pas du temps vécu dans un rêve ; les auteurs jugent eux-mêmes la comparaison des moyennes « equivocal », et seule la corrélation (0,60 pour les intervalles surtout paradoxaux) est interprétée. Surestimer au réveil la durée d'une nuit n'est pas avoir vécu plus longtemps.
- **Longueur des récits.** Dement et Kleitman trouvent des corrélations de 0,40 à 0,71 entre la durée du sommeil paradoxal et la longueur du récit ; Rosenlicht, Maloney et Feinberg (1994) ne trouvent pas de différence de longueur entre 5 et 10 min de sommeil paradoxal, mais un doublement entre le deuxième et le quatrième cycle de la nuit. La longueur d'un récit suit l'état d'éveil au moment du réveil plus que la durée vécue : elle ne mesure pas \(F\).

### 10. « Par moments »

L'hypothèse la plus faible est qu'il existe, dans certains rêves, des moments de compression. Trois éléments y répondent. Dans les rêves lucides, les seules mesures seconde par seconde, 2 <!-- erlacher.comptage.participants_plus_rapides_ou_egaux_en_reve --> participants sur 5 ont compté aussi vite ou plus vite qu'éveillés, et 2 <!-- erlacher.gymnastique.participants_plus_rapides_ou_egaux_en_reve --> sur 8 ont fait leur enchaînement « slightly shorter » : l'écart individuel existe, il est faible et minoritaire, et la moyenne va dans l'autre sens. Chez Dement et Kleitman, les surestimations sont aussi fréquentes que ne le prévoit un simple bruit d'estimation. Dans la base ouverte, aucune expérience ne dépasse le temps disponible. Aucune donnée ne montre donc un moment de compression qui se distingue de l'erreur ordinaire d'estimation d'une durée.

### 11. Conséquence pour « Une vie en une nuit »

Facteur nécessaire : 80 ans × 365,25 × 24 h / 8 h = 87 660 <!-- verdict.facteur_necessaire_une_vie_en_une_nuit -->. Facteur que le rêve ordinaire ne dépasse pas, à 95 % : 0,92 <!-- verdict.X_borne_sup_95 -->. Écart : un facteur d'environ 95 000 <!-- verdict.ecart_au_facteur_necessaire -->. L'hypothèse de travail « le rêve fait déjà vivre plus de temps qu'il n'en dure » est fermée.

## Limites

- **Peu de mesures, petits effectifs.** Le calcul repose sur 13 rêveurs lucides retenus (deux groupes) et 111 réveils de Dement et Kleitman. Les incertitudes sont prudentes (Cauchy-Schwarz, quantiles de Student), mais elles ne corrigent pas un biais commun.
- **Dement et Kleitman lus en secondaire.** L'article de 1957 est fermé ; les effectifs 45/51 et 47/60 viennent de sources secondaires concordantes (total 92/111 confirmé par Erlacher et al.). Le facteur tiré du choix forcé dépend de la frontière de décision : 0,89 <!-- dement_kleitman.frontiere_geometrique.F --> ou 1,03 <!-- dement_kleitman.frontiere_arithmetique.F --> selon qu'on la place à 8,7 <!-- dement_kleitman.frontiere_geometrique.frontiere_min --> ou 10 <!-- dement_kleitman.frontiere_arithmetique.frontiere_min --> min. La borne robuste (\(F_{\text{médian}} \lt 3\) quelle que soit la frontière) ne dépend pas de ce choix.
- **Rêves lucides.** Ce sont des rêves particuliers, avec une tâche imposée ; ils mesurent le rythme de l'action rêvée. Un rêve ordinaire pourrait comporter des sauts de scène (on passe d'un lieu à un autre sans vivre le trajet) ; un saut n'est pas du temps vécu, mais du temps omis, et il ne produit pas de compression au sens de ce test.
- **Données ouvertes en sommeil lent.** La seule base ouverte avec une durée vécue ne contient que des réveils en stade 2, et la durée réelle de l'expérience n'y est bornée que par le haut : elle ne peut détecter qu'une compression grossière. Aucune base ouverte ne contient, pour le sommeil paradoxal, à la fois une estimation de durée et la durée du sommeil paradoxal avant le réveil.
- **Sources non lues.** Glaubman et Lewin (1977), présentée comme une réplication de Dement et Kleitman, est fermée ; Moiseeva (1975) n'est lue qu'en résumé.
- **Mesure qui trancherait mieux.** Des réveils en sommeil paradoxal à durée tirée au hasard entre 1 et 30 min, avec une estimation libre de la durée vécue (en minutes) et la durée exacte du sommeil paradoxal précédent, sur plusieurs centaines de réveils, publiés en données ouvertes ; et, chez des rêveurs lucides, l'estimation d'intervalles longs (plusieurs minutes, sans compter) bornés par des signaux oculaires, avec et sans stimulation. Un rapport vécu/dormi dont la borne inférieure dépasserait 1 renverserait ce verdict.
