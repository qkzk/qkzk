---
title: "Résumé - Arbres"
bookCollapseSection: true
weight: 100

---

pdf: [pour impression](/uploads/docnsitale/arbres/cours_resume_print.pdf)

# Qu'est-ce qu'un arbre en informatique ?

**Arbre** :

> Les _arbres_ sont des structures de données
>
> * hiérarchiques,
> * naturellement récursives,
>
> utilisées pour représenter des ensembles de données structurées
> hiérarchiquement.

* Les dossiers d'un ordinateur forment un arbre

    . ![dossiers UNIX](/docs/nsi/cours_terminale/structures_donnees/arbres/resume/img/0.png)

* Les balises d'une page html forment un arbre.

## Particularité de la structure des arbres

* Elle **non linéaire** (par opposition aux listes, files, piles, tableaux)
* Elle peut être définie **récursivement** :

  * L'arbre est un ensemble de nœuds accessibles depuis un nœud racine
  * Chaque nœud étant une structure composée d'une valeur et d'une liste de
      références vers d'autres nœuds
  * **contraintes :**
    1. aucune référence n'est dupliquée (chaque nœud a un unique parent),
    1. aucune référence ne désigne le nœud racine (qui n'a donc pas de parent).

## Arbres binaires

On se restreint aux _arbres binaires_ pour lesquels la
liste des références vers d'autres nœuds comporte au plus deux
éléments.

# Vocabulaire


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
  le relie à la racine. Racine : profondeur nulle.

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


Caractériser les arbres binaires
================================

Les arbres binaires sont caractérisés par le fait que chaque nœud
possède au plus deux fils.

Autres caractéristiques, permettant d'identifier des arbres pour lesquels le
coût de certaines opérations sera minimal, ou de définir des algorithmes
spécifiques.

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
  _profondeur_.
  _(Il s'agit d'un arbre dont tous les niveaux sont remplis.)_

* Un arbre binaire _**parfait**_ est un arbre dans lequel tous les
  niveaux sont remplis à l'exception _éventuelle_ du dernier, et dans
  ce cas les feuilles du dernier niveau sont alignées à gauche.

* Un arbre binaire _**équilibré**_ est un arbre dont les deux fils
  sont des arbres équilibrés dont les hauteurs diffèrent d'au plus
  une unité. \
  Ainsi, l'accès à n'importe lequel des _nœuds_ est en moyenne
  minimisé.
