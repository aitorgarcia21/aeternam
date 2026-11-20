# Sources de l’étude « Retarder ou ralentir »

## Les données

Interventions Testing Program (ITP), National Institute on Aging : durées de vie individuelles
des souris UM-HET3, cohortes C2004 à C2021, trois sites (The Jackson Laboratory, University of
Michigan, University of Texas Health Science Center at San Antonio). Publiées par la Mouse
Phenome Database, The Jackson Laboratory, projet ITP1 (MPD:508) : Miller RA, Strong R,
Korstanje R, Harrison DE, Rosenthal NA, « Interventions Testing Program: Effects of various
treatments on lifespan and related phenotypes in genetically heterogeneous mice (UM-HET3)
(2004-2026) », https://phenome.jax.org/projects/ITP1, fichiers de durée de vie par cohorte
relevés le 20 novembre 2026.

Conditions d’utilisation lues le 20 novembre 2026 (https://phenome.jax.org/about/termsofuse) :
« MPD data contributors waive copyright and related rights, making their data freely available
whereby MPD users may freely build upon, enhance and reuse those data for any purpose without
restriction. Scholarly citation norms must be followed for content reuse. »

`donnees/itp-survie.csv` réunit les 36 975 lignes de ces fichiers, sans l’identifiant de
chaque souris : cohorte, site, sexe, groupe, dose, âge de début du traitement, mort (1) ou
retirée (0), âge en jours. Aucune valeur n’est modifiée. Les abréviations des groupes sont
celles de la base (Rapa : rapamycine ; ACA : acarbose ; 17aE2 : 17-α-estradiol ; Cana :
canagliflozine ; NDGA : acide nordihydroguaïarétique ; OH-EST : 16-α-hydroxyestriol ; MetRapa :
metformine et rapamycine ; RaAc : rapamycine et acarbose).

## Le résultat publié refait pour contrôle

Harrison DE et al., « Rapamycin fed late in life extends lifespan in genetically heterogeneous
mice », *Nature* 2009;460:392-5, doi:10.1038/nature08221 (résumé PubMed) : « On the basis of age
at 90% mortality, rapamycin led to an increase of 14% for females and 9% for males. »

## Travaux antérieurs (résumés PubMed lus le 20 novembre 2026)

- Garratt M, Nakagawa S, Simons MJP, *Aging Cell* 2016;15:737-43, doi:10.1111/acel.12489,
  48 études publiées : « life extension in mice and yeast occurs largely by pushing back the
  onset of aging, but not altering the shape of the mortality curve once aging starts ».
- Simons MJP, Koch W, Verhulst S, *Aging Cell* 2013;12:410-4, doi:10.1111/acel.12061, 82 paires
  de courbes de rats et de souris : « We find that DR reduced aging rate without affecting
  vulnerability. »
- Stroustrup N et al., *Nature* 2016;530:103-7, doi:10.1038/nature16550, *C. elegans* : des
  interventions très diverses « all alter lifespan distributions by an apparent stretching or
  shrinking of time ».

## Ce qui n’est pas dans ce dossier

Aucune expérience menée par ÆTERNAM. Aucune donnée humaine. Les simulations de `analyse.py`
servent à contrôler le calcul : ce ne sont pas des mesures.
