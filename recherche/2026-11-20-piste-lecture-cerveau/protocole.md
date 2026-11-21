# Protocole proposé : reconnaître à l'aveugle un cerveau qui a appris

ÆTERNAM n'a mené aucune expérience. Ce document décrit celle qu'il faudrait mener ; ses
effectifs viennent de `analyse.py`, ses hypothèses de `sources.md`.

## La question

Un souvenir précis laisse-t-il, dans un cerveau conservé, une trace que l'on peut lire sans
rien savoir de l'animal ?

## Ce qui est montré, et ce qui ne l'est pas

- Montré : un apprentissage survit à la vitrification chez un ver de 302 neurones ; chez la
  souris, un apprentissage modifie la structure des connexions de l'hippocampe, visible en
  microscopie électronique ; la structure d'un cerveau entier de mammifère peut être conservée.
- Non montré : qu'un lecteur qui ignore l'histoire de l'animal retrouve, dans la seule
  structure, s'il avait appris. Dans l'étude de 2025, les neurones concernés étaient marqués.

## L'hypothèse, écrite avant l'expérience

À partir de mesures de structure fixées à l'avance (part des boutons à synapses multiples
touchant plus de deux épines, taille des synapses), un lecteur classe correctement plus d'un
cerveau sur deux. Le résultat qui la réfute : moins de 18 bonnes réponses sur 26.

## Le plan

- 26 souris, tirées au sort : 13 apprennent une association (conditionnement de peur au
  contexte), 13 sont exposées au même contexte sans association.
- Cerveaux conservés par le même procédé pour tous, puis codés par une personne extérieure.
- Même région imagée chez tous (trajet CA3–CA1 de l'hippocampe), même volume, mêmes réglages.
- Mesures et règle de décision déposées publiquement avant l'ouverture des codes. Aucun
  marquage génétique des neurones : seule la structure est lue.
- Les codes ne sont ouverts qu'une fois les 26 réponses remises.

## Les effectifs

Test binomial exact, unilatéral à 5 %.

| Justesse réelle du lecteur | Cerveaux (80 % de chances) | Cerveaux (90 % de chances) |
|---|---|---|
| 70 % | 42 | 58 |
| 80 % | 18 | 26 |
| 90 % | 11 | 13 |

Avec cinq cerveaux, il faut cinq bonnes réponses sur cinq ; un lecteur juste à 80 % n'y
parvient qu'une fois sur trois.

## Ce que l'on mesure

- Critère principal : le nombre de cerveaux correctement classés.
- Critère secondaire : la même lecture après conservation longue (plusieurs mois), pour savoir
  si la trace tient dans le temps.

## Budget

À chiffrer sur devis (animalerie, conservation, temps de microscope, reconstruction). Aucun
prix n'est avancé ici : nous n'en avons pas de source publique vérifiée.

## Ce qu'un résultat permettrait

- Réussite : un souvenir précis se lit dans un cerveau conservé. L'étape suivante est de
  distinguer deux souvenirs différents, puis de passer à un cerveau plus grand.
- Échec : la structure visible à cette échelle ne suffit pas ; il faut conserver autre chose
  (molécules, état des synapses), et le dire.
- Dans les deux cas, cela ne ranime personne : un cerveau fixé est mort. La question posée est
  celle de l'information conservée, pas de la vie.

## Révision du 21 novembre 2026 : une étape pilote, et ce qui s'appliquerait à l'humain

### Une étape pilote avant les 26 cerveaux

Les 26 cerveaux supposent un lecteur juste à 80 %. Rien ne le garantit : dans l'étude de 2025,
les neurones qui avaient servi à l'apprentissage étaient marqués, et l'effet se lisait sur eux.
Sans marquage, cette trace est noyée parmi les neurones qui n'ont pas servi.

- Pilote : 3 souris qui apprennent et 3 qui n'apprennent pas, avec marquage génétique des
  neurones actifs pendant l'apprentissage, imagées comme dans le plan principal.
- Mesure : l'écart de structure entre les deux groupes, sur les neurones marqués puis sur tous
  les neurones sans tenir compte du marquage.
- Décision, écrite avant : la justesse attendue sans marquage fixe le nombre de cerveaux du plan
  principal (58 pour un lecteur juste à 70 %, 26 à 80 %, 13 à 90 %, pour 90 % de chances). Si
  l'écart disparaît sans marquage, le plan principal ne se lance pas, et on le dit.

### Ce qui s'appliquerait à l'humain

- Cette expérience est chez la souris. Chez l'humain, il faudrait encore conserver un cerveau
  à la mort sans perdre sa structure : ce n'est pas démontré pour une lecture (McKenzie et al.
  2024 ; Society for Cryobiology, 2018).
- L'échelle : un seul millimètre cube de cortex humain, environ 57 000 cellules, a demandé
  1,4 pétaoctet d'images (Shapson-Coe et al. 2024).
- La place de cette piste : c'est la voie de secours. La voie principale d'ÆTERNAM est de
  réparer le vieillissement des cellules, pour ne pas avoir à conserver quoi que ce soit.
