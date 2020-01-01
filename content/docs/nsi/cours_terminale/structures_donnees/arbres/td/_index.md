---
title: Travaux dirigés
date: novembre-décembre 2019
lang: fr
weight: 1
---

Qu'est-ce qu'un arbre ?
=======================

Dessinons un arbre !

<!--
figures des arbres cours ASD Jean-Stéphane.
Images libres de droits ?
-->

Arbre en informatique
---------------------

Les _arbres_ sont des structures de données[^arbre-informatique]

* hiérarchiques,
* naturellement récursives,

utilisées pour représenter des ensembles de données structurées
hiérarchiquement.
Par exemple[^arbre-exemple] :

* système de fichiers,
* base de données,
* sites web,
* fichiers XML.

[^arbre-informatique]: Le terme d'arbre recouvre plusieurs notions
distinctes : arbres libres, arbres enracinés, arbres binaires, etc. \
Nous ne traiterons pas des arbres libres qui relèvent de la théorie des
graphes. \
Nous nous intéresserons aux _arbres enracinés_ que nous nommerons plus
simplement _arbres_, et aux _arbres binaires_, un cas particulier de
ces arbres enracinés.

[^arbre-exemple]: Voir aussi la section
[_Examples of trees_](https://runestone.academy/runestone/books/published/pythonds/Trees/ExamplesofTrees.html)
de _Problem Solving with Algorithms and Data Structures using Python_,
	Brad Miller and David Ranum, Luther College.
	Franklin, Beedle & Associates Inc. (2011).
	Consultable en ligne à [runestone.academy/runestone/static/pythonds/index.html](https://runestone.academy/runestone/static/pythonds/index.html).

Un arbre est une structure de données non-linéaire (comparée aux
tableaux, listes, piles, et files qui sont des strutures linéaires).

Une structure de données arborescente peut être définie récursivement
comme un ensemble de nœuds accessibles depuis un nœud racine. Chaque
nœud étant une structure composée d'une valeur et d'une liste de
références vers d'autres nœuds, avec les contraintes suivantes :
aucune référence n'est dupliquée (chaque nœud a un unique parent), et
aucune référence ne désigne le nœud racine (qui n'a donc pas de parent).

Nous allons nous restreindre aux _arbres binaires_ pour lesquels la
liste des références vers d'autres nœuds comporte au plus deux
éléments. \
Ces arbres binaires sont largement utilisés, par exemple sous forme
d'[ABR – arbres binaires de recherche](https://fr.wikipedia.org/wiki/Arbre_binaire_de_recherche) –,
de [tas](https://fr.wikipedia.org/wiki/Tas_binaire), d'arbres
équilibrés comme les [AVL](https://fr.wikipedia.org/wiki/Arbre_AVL),
ou encore
d'[arbres bicolores rouge-noir](https://fr.wikipedia.org/wiki/Arbre_bicolore).

Un peu (beaucoup...) de vocabulaire préliminaire
------------------------------------------------

### → Terminologie ###

* un _nœud_ est caractérisé par
  - une donnée (on parle aussi d'étiquette),
  - un nombre fini de fils.

* une _arête_ relie deux nœuds. Chaque nœud, à l'exception de la
  racine, est relié à un autre nœud, son père, par exactement une arête
  entrante. Chaque nœud peut avoir une ou plusieurs arêtes sortantes
  le reliant à ses fils. On parle aussi de _lien_.

* la _racine_ d'un arbre est le seul nœud sans père.

* un _chemin_ est une liste de nœuds reliés par des arêtes.

* une _branche_ est le chemin le plus court reliant un nœud à la
  racine.

* les _fils_ sont l'ensemble des nœuds reliés à un même nœud par des
  arêtes entrantes.

* le _père_ ou _parent_ est le nœud relié à ses nœuds fils par une
  arête sortante.

* un _sous-arbre_ est l'ensemble des nœuds et arêtes d'un nœud
  parent et de ses descendants.

* une _feuille_ est un nœud sans fils.

* un _nœud interne_ est un nœud qui n'est pas une feuille.

Pour assurer la cohérence de ces définitions, on considère que l'arbre
vide n'est pas un nœud.

### → Quelques mesures sur les arbres ###

* la _taille_ d'un arbre est le nombre de nœuds de l'arbre.

* la _profondeur_ d'un nœud est le nombre d'arêtes sur la branche qui
  le relie à la racine. La profondeur de la racine est nulle.

* la _hauteur_ d'un arbre est la profondeur maximale de l'ensemble des
  nœuds de l'arbre.

* l'_arité d'un nœud_ est le nombre de fils du nœud.

* l'_arité d'un arbre_ est le nombre maximal de fils des nœuds de
  l'arbre.

### → _Définition._ Arbre binaire ###

Un _arbre binaire_ est donc un arbre d'arité deux.

Un arbre binaire est

* soit l'arbre vide, noté $\Delta$ ;
* soit un triplet (e, g, d), appelée _nœud_, dans lequel
  - e est l'élément, ou encore _étiquette_, de la racine de l'arbre,
  - g est le sous-arbre gauche de l'arbre, et
  - d est le sous-arbre droit de l'arbre.

Les sous-arbres gauche et droit d’un arbre binaire non vide sont
eux-mêmes des arbres binaires. La structure d’arbre binaire est donc
une structure récursive.

* on appelle _fils gauche_, resp. _fils droit_, le sous-arbre gauche,
  resp. droit, d'un nœud.

Se familiariser avec les arbres binaires
----------------------------------------

### $\gg$ Quelques arbres binaires ###

Dessinez chacun des arbres ci-dessous, donnez sa taille et sa hauteur,
le nombre de feuilles, le nombre de nœuds à chaque profondeur.

1. (1, $\Delta$, $\Delta$)
2. (3, (1, $\Delta$, (4, (1, $\Delta$, (5, $\Delta$, $\Delta$)), $\Delta$)), $\Delta$)
3. (3, (1, (1, $\Delta$, $\Delta$), $\Delta$), (4, (5, $\Delta$, $\Delta$), (9, $\Delta$, $\Delta$)))
4. (3, (1, (1, $\Delta$, $\Delta$), (5, $\Delta$, $\Delta$)), (4, (9, $\Delta$, $\Delta$), (2, $\Delta$, $\Delta$)))

<!-- réponses

| arbre | taille | hauteur | nbre feuilles | nbre nœuds à profondeur donnée |
| ----- | ------ | ------- | ------------- | ------------------------------ |
| 1.    | 1      | 0       | 1             | à profondeur 0 : 1, à profondeur >0 : 0 |
| 2. | 5 | 4 | 1 | à  profondeur ≤4 : 1, à profondeur >4 : 0 |
| 3. | 6 | 2 | 3 | à profondeur 0 : 1, à profondeur 1 : 2, à profondeur 2 : 3, à profondeur >2 : 0 |
| 4. | 7 | 2 | 4 | à profondeur 0 : 1, à profondeur 1 : 2, à profondeur 2 : 4, à profondeur >2 : 0 |

-->

### $\gg$ Des arbres binaires ###

* Combien de feuilles au minimum comporte un arbre binaire de hauteur _h_ ? \
  Au maximum ?

* Combien de nœuds au minimum comporte un arbre binaire de hauteur _h_ ? \
  Au maximum ?

<!-- réponses

* au minimum une feuille et h+1 nœuds d'arité 1.
  Nous avons affaire à un arbre _filiforme_.
* au maximum 2^{h} feuilles.
  Nous avons affaire à un arbre localement complet.
  Au maximum  et 2^{h+1}-1 nœuds.
  Nous avons affaire à un arbre complet.

-->


### $\gg$ Squelettes d'arbres binaires ###

On appelle squelette ou forme d'arbres binaires tout arbre binaire
dans lequel on ne tient pas compte des étiquettes.

Combien y a-t-il de squelettes d'arbres binaires de taille 0, de taille
1 ?

Dessinez tous les squelettes d'arbres binaires de taille 2, 3, 4 ;
donnez-en le nombre.

<!-- réponses

    $n$    0   1   2   3   4    5
  ------- --- --- --- --- ---- ----
   $c_n$   1   1   2   5   14   42

| $n$   |  0  |  1  |  2  |  3  |  4   |  5   |
| ----- | --- | --- | --- | --- | ---- | ---- |
| $c_n$ |  1  |  1  |  2  |  5  |  14  |  42  |

-->

### $\gg$ Taille et hauteur ###

Proposez des algorithmes pour calculer

* la taille d'un arbre binaire
* la hauteur d'un arbre binaire. On conviendra conventionnellement que
  la hauteur de l'arbre vide $\Delta$ est -1.

<!-- réponses

```
taille (a) :
    si a est l'arbre vide
        renvoyer 0
	a de la forme (e, g, d)
	taille_g = taille(g)
	taille_d = taille(d)
	renvoyer 1 + taille_g + taille_d
```

-->

Caractériser les arbres binaires
================================

Les arbres binaires sont caractérisés par le fait que chaque nœud
possède au plus deux fils.

D'autres caractéristiques sont définies, qui permettent par exemple
d'identifier des arbres pour lesquels le coût de certaines opérations
sera minimal, ou de définir des algorithmes spécifiques à ces arbres.

* Un arbre binaire _**filiforme**_ ou _dégénéré_ est un arbre dans lequel
  tous les _nœuds internes_ n'ont qu'un seul _fils_. \
  _(Un arbre filiforme ne possède donc qu'une unique feuille.)_

* Un arbre binaire _**localement complet**_ ou arbre binaire _strict_ est
  un arbre dont tous les _nœuds internes_ possèdent exactement deux
  _fils_.\
  _(Autrement dit, un arbre binaire localement complet est un arbre
  dont chaque nœud possède zéro ou 2 fils. L'arbre vide n'est pas
  localement complet.)_

* Un arbre binaire _**complet**_ est un arbre binaire _localement
  complet_ dans lequel toutes les _feuilles_ sont à la même
  _profondeur_. \
  _(Il s'agit d'un arbre dont tous les niveaux sont remplis.)_

* Un arbre binaire _**parfait**_ est un arbre dans lequel tous les
  niveaux sont remplis à l'exception _éventuelle_ du dernier, et dans
  ce cas les feuilles du dernier niveau sont alignées à gauche.

* Un arbre binaire _**équilibré**_ est un arbre dont les deux fils
  sont des arbres équilibrés dont les hauteurs diffèrent d'au plus
  une unité. \
  Ainsi, l'accès à n'importe lequel des _nœuds_ est en moyenne
  minimisé.

_Comme le mentionne la
[page Wikipedia _Arbre_binaire#Types_d'arbres_binaires_](https://fr.wikipedia.org/wiki/Arbre_binaire#Types_d'arbres_binaires),
il existe des usages contradictoires des termes _complet_ et
_parfait_ qui peuvent parfois être intervertis. Des confusions peuvent
aussi exister entre le français et l'anglais, dans lequel on trouve
les termes _perfect_ et _complete_. \
La terminologie utilisée ici est cohérente avec celle de Froidevaux
_et al._[^FroidevauxGaudelSoria], alors que Beauquier _et
al._[^BeauquierBerstelChretienne] en utilisent une autre._

[^FroidevauxGaudelSoria]: _Types de données et algorithmes_,
	Christine Froidevaux, Marie-Claude Gaudel, Michèle Soria.
	McGraw-Hill (Paris, 1990), Ediscience (1994).
	Téléchargeable depuis la page de Marie-Claude Gaudel [lri.fr/~mcg/](https://www.lri.fr/~mcg/)
	<!-- https://www.lri.fr/~mcg/PDF/FroidevauxGaudelSoria.pdf -->

[^BeauquierBerstelChretienne]: _Eléments d'algorithmique_
	Danièle Beauquier, Jean Berstel, Philippe Chrétienne.
	Masson (1992 pour la 1re édition).
	Téléchargeable depuis la page de Jean Berstel [www-igm.univ-mlv.fr/~berstel/](http://www-igm.univ-mlv.fr/~berstel/)
	<!-- http://www-igm.univ-mlv.fr/~berstel/Elements/Elements.pdf -->


Se repérer dans cette forêt d'arbres
------------------------------------

### $\gg$ Compter ces arbres ###

* Combien de nœuds au maximum comporte un arbre localement complet de
  hauteur _h_ ? \
  Au minimum ?

* Combien de nœuds comporte un arbre complet de hauteur _h_ ?

* Combien de squelettes d'arbres parfaits de hauteur _h_ existe-t-il ?

* Combien de squelettes d'arbres filiformes de hauteur _h_
  exite-t-il ?

### $\gg$ Reconnaître ces arbres ###

Proposez des algorithmes pour les prédicats

* reconnaître un arbre binaire filiforme
* reconnaître un arbre binaire localement complet
* reconnaître un arbre binaire complet
* reconnaître un arbre binaire parfait

### $\gg$ Superposer deux arbres ###

Proposez un prédicat pour tester l'égalité du squelette de deux arbres
binaires.

### $\gg$ Numéroter les nœuds ###

La numérotation de Sosa-Stradonitz des nœuds d'un arbre binaire,
utilisée notamment en généalogie, est la suivante :

* le nœud racine est numéroté par 1
* si un nœud numéroté par $i$
  - son fils gauche est numéroté par $2i$
  - son fils droit est numéroté par $2i + 1$

Cette numérotation peut être utilisée pour représenter un arbre dans
un tableau : l'élément $j$ du tableau mémorise le nœud numéroté par
$j$.

Combien d'éléments doit contenir un tableau utilisé pour représenter

* un arbre binaire complet de $n$ nœuds ?
* un arbre binaire parfait de $n$ nœuds ?
* un arbre binaire quelconque de $n$ nœuds (dans le pire des cas) ?


À suivre...
===========

Il s'agira de

* parcourir les arbres
* identifier les opérations primitives pour manipuler les arbres

et de découvrir les ABR, _arbres binaires de recherche_.
