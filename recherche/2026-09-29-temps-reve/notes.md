# Notes de travail (temps vécu en rêve)

Départ : sources déjà lues dans recherche/2026-09-28-une-vie-en-une-nuit/sources.md (Moiseeva résumé, Dement-Kleitman secondaire, Erlacher 2004/2014).

## Données ouvertes trouvées (29/09)
- DREAM database (Wong et al. 2025 Nat Commun, PMC12350935, CC BY 4.0), figshare 10.26180/22133105 : Data records.csv (md5 6f9be5b4abb0b603ee802fffb015155f). Pas de durée subjective dans la table générale.
- Jeu 13 « Tononi Serial Awakenings » (10.26180/23306054.v3, CC BY 4.0) : Part1-No_PSGs.zip (https://ndownloader.figshare.com/files/59168237, sha256 e4d7932ed96e65fe6ff1e25df9fea0229b2e7e3d3cca1730f9dd637531ff62b0) : Data/AdditionalData.csv « Duration of continuous experiences before alarm 0-5s=1, >5-10s=2, >10s-1min=3,>1-10min=4,>10min-1h=5, >1h=6 » ; 124 réponses (1:21, 2:22, 3:39, 4:36, 5:6, 6:0). Tout en N2. Records.csv : heure de réveil.
- Siclari 2013 (PMC3747360) : « For how long were you having continuous experiences before the alarm sound? »
## Pistes littérature
- Glaubman & Lewin 1977 PMS 44(3):929 doi 10.2466/pms.1977.44.3.929 (« Rem and Dreaming ») : c'est peut-être LEUR étude qui a les 92/111 (et non Dement-Kleitman ?) -> vérifier.
- Rosenlicht, Maloney, Feinberg 1994 Brain Res Bull PMID 8044693 : TWC après 5 vs 10 min REM pas différent.
- « The subjective and the objective duration of static NREM sleep dreams » (ResearchGate 318467728) -> à lire.
## Lu en primaire
- Koulack D. (1968) Dream time and real time. Psychon Sci 11(6):202. doi 10.3758/BF03327656 (PDF Springer bronze, lu). Choc au poignet en REM, réveil 30 s ou 3 min après ; 12 incorporations nettes chez 5 sujets ; « 92% of S-judgments (11 of 12) placed those incidents at a time corresponding to the time of stimulation ». Cite Schjelderup 1960 (Scand J Psychol 1:62-64 : rêves longs en 1-2 s de sommeil hypnotique).
- Erlacher et al. 2014 (PMC3893623, lu) Table 2 : comptage N=5 éveil 50.3 (11.5) rêve 64.0 (17.1) t=2.10 p=.10 ; marche n=7 37.7 (1.7) / 57.5 (19.2) t=2.82 p=.03 ; gym n=8 6.6 (0.1) / 8.1 (1.5) t=2.81. Comptage et marche = mêmes participants ; gym = autre groupe (2 h 6 f).
- Erlacher 2014 sur Erlacher & Schredl 2004 : squats éveil M=17.84 s SD 6.8 ; comptages 6.26 (1.7) et 6.48 (1.0) ; « about 40% more time » ; « squats: 39.9% ».
- Dement & Kleitman 1957 : original inaccessible (APA, fermé). Secondaires concordants : Erlacher 2014 « 92 out of 111 (83%) » ; guide simplypsychology : 45/51 à 5 min, 47/60 à 15 min ; r 0.40 à 0.71 longueur récit/durée REM. Koulack 1968 : « All but one of their Ss made judgments in direct correspondence ».
- Michalak et al. 2026 PLOS Biol (doi 10.1371/journal.pbio.3003683), Zenodo 15372992 : durée subjective en minutes, mais N2 seulement ; table MATLAB opaque.
- Idée d'analyse D&K : modèle de détection du signal log-normal -> facteur k et sigma à partir de 6/51 et 13/60 ; dépend du critère (moyenne géométrique 8.66 min).
- Carlson, Feinberg, Goodenough 1978 Physiol Psychol 6(4):497-500 doi 10.3758/BF03326756 (PDF lu) : intervalles réels 10 min à 2 h (moy 38.7, SD 18.6) ; estimations 5 min à 3 h (moy 61.6, SD 39.6) ; corrélation estimations/durée 0.60 (REM prédominant), 0.33 (N2), 0.30 (delta) ; auteurs : comparaison des moyennes « equivocal ». Porte sur le temps écoulé (dont 24 % d'éveil), pas sur le vécu d'un rêve.
- Moiseeva 1975 résumé PubMed lu : rêves « evoked by stimuli of a certain duration » ; « major overestimation of their duration » pour rêves complexes ; attribué à la mise en ordre du récit.
- Rosenlicht 1994 résumé lu : 22 sujets ; 5 vs 10 min REM ; TWC non différent.
- Tononi DREAM : heures = heure d'horloge (22:xx..), s39 plusieurs nuits. Intervalle = (t2-t1) mod 1440 ; > 360 min => nouvelle nuit. Intervalle min 11 min, médiane 39.
- Glaubman & Lewin 1977 : fermé, non lu (403).
- Konkoly 2026 JoCN : pas de mesure de durée.
## Plan analyse.py : (1) Tononi borne ; (2) D&K détection du signal ; (3) Erlacher delta ; (4) méta ; règle : OUI si borne inf 95 % unilat > 1 ou proportion certaine > 5 % ; NON si borne sup 95 % < 2 ; sinon indéterminé.
