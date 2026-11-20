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
