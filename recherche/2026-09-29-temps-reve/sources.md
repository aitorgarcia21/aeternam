# Temps vécu en rêve contre temps dormi : sources

Statuts : **primaire lue** (texte intégral lu par nous) ; **résumé lu** (seul le résumé officiel a été lu) ; **secondaire** (chiffres connus seulement par une autre publication, citée) ; **non lue** (accès refusé).

## 1. Données ouvertes utilisées

### 1a. Base DREAM
Wong W., Herzog R., Andrade K.C., Andrillon T., de Araujo D.B., Arnulf I., et al. (2025). A dream EEG and mentation database. *Nature Communications*, 16, 7495. DOI : 10.1038/s41467-025-61945-1. PMCID PMC12350935. Licence CC BY 4.0. Métadonnées : figshare/Monash Bridges, DOI 10.26180/22133105 (« Data records.csv », md5 6f9be5b4abb0b603ee802fffb015155f, 3 191 lignes, lu).

Passages lus : « Each awakening consists, at minimum, of sleep M/EEG (≥ 20 s, ≥100 Hz, ≥2 electrodes) up to the time of waking and a standardized dream report classification » ; « The database records metadata of each awakening from every study in the table “Data records” as a single record with 20 fields ».

Constat : la table générale ne contient aucune durée subjective. Parmi les 20 jeux, un seul fournit une estimation de durée en unités de temps : le jeu n° 13 (ci-dessous). Le jeu n° 15 (Noreika_Motor_tDCS) n'a que des échelles de Likert « 1 = Never » à « 9 = Throughout ». Statut : **primaire lue**.

### 1b. Jeu « Tononi Serial Awakenings » (DREAM n° 13, amendement 2)
Siclari F., Baird B., Perogamvros L., Boly M., LaRocque J., Tononi G. Données : DOI 10.26180/23306054.v3, licence CC BY 4.0. Archive utilisée : « Tononi Serial Awakenings-Part1-No_PSGs.zip », https://ndownloader.figshare.com/files/59168237, SHA-256 `e4d7932ed96e65fe6ff1e25df9fea0229b2e7e3d3cca1730f9dd637531ff62b0` (versionnée dans `donnees/tononi_part1.zip`, redistribution permise par CC BY 4.0 avec attribution).

Passages lus (ExperimentalDescription.txt) :
- « File "Data/AdditionalData.csv" contains data on "Perception (yes=1, no=0)", and "Duration of continuous experiences before alarm 0-5s=1, >5-10s=2, >10s-1min=3,>1-10min=4,>10min-1h=5, >1h=6". »
- « Awakenings in the sleep laboratory were performed at pseudorandom intervals, irrespective of sleep stage, using a computerized sound that lasted 1.5 s »
- « They then underwent a structured interview via intercom about their mental activity that lasted between 20 s and 3.5 min »
- Métadonnées : « Number of samples: 287 », « Number of subjects: 39 », « Proportion N2: 100% ».

Formulation exacte de la question (Siclari F., Larocque J.J., Postle B.R., Tononi G. (2013). Assessing sleep consciousness within subjects using a serial awakening paradigm. *Frontiers in Psychology*, 4, 542, DOI 10.3389/fpsyg.2013.00542, PMC3747360, **primaire lue**) : « Duration of CE: Participants were asked: “For how long were you having continuous experiences before the alarm sound?” » ; « subjects had been instructed to provide answers in units of time (i.e., seconds, minutes, or hours) ».

Lecture des heures : « Time of awakening » est une heure d'horloge (valeurs de 22 h à 7 h) ; l'écart au réveil précédent est pris modulo 24 h ; un écart de plus de 6 h marque une autre nuit (sujet 39). Statut : **primaire lue, recalculée** (`analyse.py`).

### 1c. Données examinées et non retenues
Michalak A., Marzoli D., Pietrogiacomi F., Bergamo D., Elce V., Pedreschi B., et al., Bernardi G. (2026). Immersive NREM2 dreaming preserves subjective sleep depth against declining sleep pressure. *PLOS Biology*, 24, e3003683, DOI 10.1371/journal.pbio.3003683 ; données Zenodo 10.5281/zenodo.15372992 (CC BY 4.0). Passages lus : « For CE reports, they were asked to estimate the length of the conscious experience in minutes » ; « Awakenings were induced using a 1.5 s computerized alarm sound after at least 15 min from sleep onset and 5 min of stable N2 sleep ». Non retenue : sommeil N2 seulement, comme 1b, et table fournie au format objet MATLAB (`fulldatatable_10-Nov-2025_w90.mat`), illisible sans MATLAB. Statut : **primaire lue (méthodes), données non exploitées**.

## 2. Études primaires : durée vécue contre durée réelle

### 2a. Dement & Kleitman (1957)
Dement W., Kleitman N. (1957). The relation of eye movements during sleep to dream activity: an objective method for the study of dreaming. *Journal of Experimental Psychology*, 53(5), 339–346. DOI : 10.1037/h0048189. PMID 13428941.
Original **non lu** (APA, accès fermé ; aucune copie ouverte trouvée par Unpaywall ni Semantic Scholar).
Chiffres par sources secondaires concordantes :
- Erlacher et al. 2014 (2c) : « participants were awakened randomly, either 5 or 15 min after REM onset, and were then asked if they had dreamed 5 or 15 min. In 92 out of 111 awakenings (83%) the participants judged correctly. The authors also found a correlation between the elapsed amount of time and length of dream reports (r = 0.40 to r = 0.71). »
- Guide Simply Psychology (PDF « simplypsychology.org-Dement-and-Kleitman-1957.pdf ») : « On 88% of trials (45/51) the participants estimated 5 mins correctly » ; « On 78% of trials (47/60) the participants estimated 15 mins correctly ». 45 + 47 = 92, 51 + 60 = 111.
- Koulack 1968 (2b) : « All but one of their Ss made judgments in direct correspondence to the length of the REM period ».
Statut : **secondaire** (trois sources concordantes). Utilisé dans le modèle de détection du signal de `analyse.py`.

### 2b. Koulack (1968)
Koulack D. (1968). Dream time and real time. *Psychonomic Science*, 11(6), 202. DOI : 10.3758/BF03327656. PDF Springer (accès libre « bronze »), lu.
Passages : « The external stimulus was presented to the Ss either immediately after or 3 min after the first eye movement of a REM period » ; « The S was awakened either 30 sec or 3 min after the end of the stimulation » ; « S was asked to estimate if that event had occurred more nearly 30 sec before the buzzer or more nearly 3 min before the buzzer » ; « There were 12 instances obtained from five of the Ss where the presence of the stimulus in the dream could be identified clearly; 92% of S-judgments (11 of 12) placed those incidents at a time corresponding to the time of stimulation. » Sujets : « Ten adult males ranging in age from 20 to 40 years ». Le texte ne précise pas combien des 12 cas étaient à 30 s.
Le même article cite, sans chiffres vérifiables, Schjelderup H.K. (1960), Time relations in dreams, *Scand. J. Psychol.* 1, 62–64 : rêves longs « during a period of 1 to 2 sec of hypnotically induced sleep » (sommeil hypnotique, pas sommeil réel ; **non lu**).
Statut : **primaire lue**.

### 2c. Erlacher, Schädlich, Stumbrys & Schredl (2014)
Erlacher D., Schädlich M., Stumbrys T., Schredl M. (2014). Time for actions in lucid dreams: effects of task modality, length, and complexity. *Frontiers in Psychology*, 4, 1013. DOI : 10.3389/fpsyg.2013.01013. PMID 24474942, PMCID PMC3893623. Texte intégral lu (Europe PMC).
Tableau 2 (« Comparisons of times in wakefulness and lucid dreaming ») : comptage (N = 5) total éveil M = 50.3 s (SD 11.5), rêve lucide M = 64.0 s (SD 17.1), écart 27.2 %, t = 2.10, p = 0.10 ; marche (n = 7) éveil 37.7 (1.7), rêve 57.5 (19.2), 52.5 %, t = 2.82, p = 0.03 ; gymnastique (n = 8) éveil 6.6 (0.1), rêve 8.1 (1.5), 23.2 %, t = 2.81.
Passages : « In the lucid dream condition, the durations for counting were 27.2%, for walking 52.5% and for the gymnastic routine 23.2% longer than in wakefulness » ; « Statistically significant differences were found for the two tasks with motor activity, walking (p = 0.03) and gymnastics (p = 0.03) but not for the counting task (p = 0.10) » ; comptage : « In three cases (P2m32, P3m23, P4f24) the absolute time was longer during lucid dreaming than in wakefulness » ; marche : « In five cases (P2m32, P3m23, P4f24, P5m34, P7f22) the absolute time was longer » et « P8m24 exhibits significantly shorter time; however, the participant [...] reported he was running instead of walking » ; gymnastique : « In six cases [...] the absolute time was longer [...]. In the other two cases (P10m24, P15f35) the duration of the gymnastic routine was slightly shorter in the lucid dream state than in wakefulness. » Participants (tableau 1) : « a All participants of the counting task also completed the walking task » ; gymnastique : 8 personnes (2 hommes, 6 femmes), groupe distinct.
Statut : **primaire lue**.

### 2d. Erlacher & Schredl (2004)
Erlacher D., Schredl M. (2004). Time required for motor activity in lucid dreams. *Perceptual and Motor Skills*, 99(3 Pt 2), 1239–1242. DOI : 10.2466/pms.99.3f.1239-1242. PMID 15739850. Original **non lu** (fermé).
Par Erlacher 2014 : « participants required about 40% more time for performing squats in lucid dreams than in the waking state » ; « squats: 39.9% » ; « the motor task (M = 17.84 s, SD = 6.8) lasted almost three times as long as the counting task (first counting: M = 6.26 s, SD = 1.7; second counting: M = 6.48 s, SD = 1.0), when measured in wakefulness » ; « there was no significant difference between wakefulness and dream state for the counting intervals ». Statut : **secondaire** ; hors méta-synthèse (pas d'écart type du rêve).

### 2e. LaBerge (1985)
LaBerge S. (1985). *Lucid Dreaming*. Los Angeles : Tarcher (livre). Par Erlacher 2014 : « In a pilot study, LaBerge (1985) demonstrated that the time interval for counting from one to ten in a lucid dream is about the same compared to that of wakefulness. » Aucun chiffre. Statut : **secondaire**.

### 2f. Moiseeva (1975) : la seule affirmation d'accélération
Moiseeva N.I. (1975). The characteristics of EEG activity and the subjective estimation of time during dreams of different structure. *Electroencephalography and Clinical Neurophysiology*, 38(6), 569–577. DOI : 10.1016/0013-4694(75)90157-1. PMID 50182.
Résumé lu (PubMed) : « During dreams evoked by stimuli of a certain duration, the EEF was studied in healthy subjects and in patients with implanted electrodes » ; « Estimation of the temporal structure of the dream was made from the verbal account of the subject. In the case of an unformed dream the duration of the dream was shown to be adequately estimated » ; « Dreams with a complex structure, with simultaneous action in different aspects and with major overestimation of their duration » ; « in the verbal account, the subject tends to place the events in a certain temporal order which creates the effect of considerable acceleration of the time flow. »
Par Erlacher 2014 : « time can be perceived as flowing much faster, exceeding the absolute time span of a dream by 2–10, 25–50 or even 100 times ». Effectifs, fréquence de ces cas et incertitudes inconnus. Statut : **résumé lu ; facteurs seulement en secondaire** ; hors méta-synthèse (ni effectif ni incertitude).

### 2g. Glaubman & Lewin (1977)
Glaubman H., Lewin I. (1977). REM and dreaming. *Perceptual and Motor Skills*, 44(3), 929–930. DOI : 10.2466/pms.1977.44.3.929. **Non lue** (SAGE, 403 ; aucune copie ouverte). Erlacher 2014 dit seulement que les résultats de Dement et Kleitman « were replicated by other researchers (e.g., Glaubman and Lewin, 1977; Hobson and Stickgold, 1995) ».

### 2h. Hall (1981), Goblot, Maury
Par Erlacher 2014 : Hall C.S. (1981), *Percept. Motor Skills* 53, 239–246, cherchait des preuves de l'hypothèse de Goblot (rêve fabriqué au réveil) ; « Hall admitted himself that this does not prove that these dreams are generated during awakening ». Statut : **secondaire**, qualitatif.

## 3. Études voisines (hors méta-synthèse)

### 3a. Carlson, Feinberg & Goodenough (1978) : estimation du temps écoulé en dormant
Carlson V.R., Feinberg I., Goodenough D.R. (1978). Perception of the duration of sleep intervals as a function of EEG sleep stage. *Physiological Psychology*, 6(4), 497–500. DOI : 10.3758/BF03326756. PDF Springer (bronze), lu.
Passages : « Subjects were able to estimate with relative accuracy the durations of sleep intervals made up predominantly of EEG stage I-REM but not of delta » ; « The actual time intervals varied from 10 min to 2 h (mean = 38.7 min, SD = 18.6) » ; « The subjects' time estimates ranged from 5 min to 3 h (mean = 61.6 min, SD = 39.6) » ; corrélations moyennes estimation/durée réelle « .60 » (intervalles surtout REM), « .33 » (stade 2), « .30 » (delta, n.s.) ; « Correlation of time estimates with elapsed time for REM periods but not for delta periods makes comparison of the mean time estimates for these two conditions equivocal. » ; intervalles surtout REM : 24 % d'éveil en moyenne (tableau 2, ligne « Awake », colonne I-REM : 24).
Statut : **primaire lue**. Mesure le temps écoulé entre une image et le réveil (éveil compris), pas le temps vécu dans un rêve.

### 3b. Danilin & Latash (1979)
Danilin V.P., Latash L.P. (1979). *Zh Vyssh Nerv Deiat Im I P Pavlova*, 29(3), 502–509 (en russe). PMID 224613. Résumé lu : « Subjective estimations of the duration of night sleep periods and their actual duration were compared in 29 healthy men » ; « The course of subjective time count in the sleep cycle seems to be uneven: it is slowed down in delta-sleep and accelerated in REM sleep following delta-sleep. » Durée de sommeil estimée, pas vécu d'un rêve ; pas de chiffres dans le résumé. Statut : **résumé lu**.

### 3c. Rosenlicht, Maloney & Feinberg (1994) : longueur du récit
Rosenlicht N., Maloney T., Feinberg I. (1994). Dream report length is more dependent on arousal level than prior REM duration. *Brain Research Bulletin*, 34(2), 99–101. DOI : 10.1016/0361-9230(94)90004-3. PMID 8044693. Résumé lu : « Twenty two young adult subjects » ; « Length of time in each REMP prior to awakening was either 5 or 10 min » ; « TWC after 5 min of prior REM sleep did not differ significantly from TWC after 10 min of prior REM sleep. However, mean TWC from REMP4 awakenings was almost twice that from REMP2 awakenings. » Statut : **résumé lu**. Conséquence : la longueur d'un récit ne mesure pas le temps vécu.

### 3d. Louie & Wilson (2001)
Par Erlacher 2014 : rejeu hippocampique du rat en sommeil paradoxal, « Most scaling factors were bigger than 1.0 (i.e., there was a slower corresponding activity during REM sleep) and the average was 1.4 ± 0.6 ». Statut : **secondaire** (déjà dans `recherche/2026-09-28-une-vie-en-une-nuit/sources.md`).

## 4. Calculs de ce dossier (`analyse.py`, `resultats.json`)
- Règle de décision écrite dans l'en-tête du script avant la première exécution.
- Facteur nécessaire au projet : 80 × 365,25 × 24 / 8 = 87 660 (même calcul que `recherche/2026-09-28-une-vie-en-une-nuit/`).
