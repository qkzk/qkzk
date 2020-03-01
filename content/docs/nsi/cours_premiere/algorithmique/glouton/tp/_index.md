---
title: Problème du rendu de monnaie
author: qkzk
weight: 3
---

_Puisqu'il paraît que cela vous motive, je vous l'annonce : vous serez évalués_
_en D.S. sur ce problème et donc sur ce T.P. Tenez-vous le pour dit._

## Épreuve pratique de NSI pour le baccalauréat

> 2. Partie pratique
> Durée : 1 heure
>
> Modalités
> La partie pratique consiste en la résolution de deux exercices sur ordinateur, chacun étant noté sur 4 points.
>
> Le candidat est évalué sur la base d'un dialogue avec un professeur-examinateur. Un examinateur évalue au maximum quatre élèves. L'examinateur ne peut pas évaluer un élève qu'il a eu en classe durant l'année en cours.
>
> L'évaluation de cette partie se déroule au cours du deuxième trimestre pendant la période de l'épreuve écrite de spécialité.
>
> Premier exercice
> Le premier exercice consiste à programmer un algorithme figurant explicitement au programme, ne présentant pas de difficulté particulière, dont on fournit une spécification. Il s'agit donc de restituer un algorithme rencontré et travaillé à plusieurs reprises en cours de formation. Le sujet peut proposer un jeu de test avec les réponses attendues pour permettre au candidat de vérifier son travail.
>
> Deuxième exercice
> Pour le second exercice, un programme est fourni au candidat. Cet exercice ne demande pas l'écriture complète d'un programme, mais permet de valider des compétences de programmation suivant des modalités variées : le candidat doit, par exemple, compléter un programme « à trous » afin de répondre à une spécification donnée, ou encore compléter un programme pour le documenter, ou encore compléter un programme en ajoutant des assertions, etc.


_Le TP que vous allez réaliser aujourd'hui vise à vous faire travailler cette épreuve._

## Consignes pour le TP

* Vous ferez ce TP en binôme dans _sublime text_.
* Vous rendrez deux documents via Classroom :

  1. un fichier _markdown_ intitulé `nom1_nom2_reponses.md` contenant les réponses aux questions textuelles. [Quelques exemples](https://fr.wikipedia.org/wiki/Markdown#Quelques_exemples) de syntaxe markdown.
  2. un fichier _python_ intitulé `nom1_nom2_programme.py` contenant votre programme.

Votre programme sera testé et commenté. Vous créerez des fonctions afin de le
découper et de rendre le code lisible.

Vous êtes libres de nommer les objets (variables, fonctions) mais cela fera partie
des critères d'évaluations.

Vous ne manquerez pas de _documenter_ votre travail. Cela aussi sera évalué.

Rassurez-vous, l'énoncé est long mais il y a peu de choses à faire.

---

# Le problème du rendu de monnaie

Rappelons le principe : on dispose d'un jeu de pièces, par
exemple `[1, 2, 5, 10]` et d'une somme à construire, par exemple $S=12$.

Quel est le nombre minimal de pièces nécessaires pour atteindre $S$ ?

Dans notre exemple, la solution $12 = 10 + 2$ convient. C'est aussi la
solution optimale, il faut donc deux pièces : `[10, 2]`.

L'objectif du TP est de construire un script qui résolve ce problème.


## Système canonique.

Rappelons aussi ce concept : un système de monnaie est **canonique** si la
somme des $n$ premières valeurs est inférieure à la valeur $n+1$.

**À faire 1**

* Le système de monnaie actuel (l'euro) est-il canonique ?
* Chercher sur internet un exemple historique de système de monnaie non canonique.

**À faire 2**

* Proposer un algorithme testant si un tableau de valeurs (par exemple `[1, 2, 5, 10, 20, 50, 100]`) est canonique.
* Programmer cet algorithme en Python. Tester sur des exemples des deux types (canoniques et non).

## Solution gloutonne

La solution _gloutonne_ au problème de rendu de monnaie consiste à choisir systématiquement la plus haute valeur possible en premier.

On démontre (et on l'acceptera) que cet algorithme est optimal pour un système de
monnaie canonique.

**Par exemple :**

~~~python
pieces = [1, 2, 5, 10, 20, 50, 100]
total = 17
~~~

- la plus haute valeur possible est 10. Il reste 17 - 10 = 7
- la plus haute valeur possible est 5. Il reste 7 - 5 = 2.
- la plus haute valeur possible est 2. Il reste 2 - 2 = 0.

L'algorithme est terminé et propose comme solution : `solution = [10, 5, 2]`

**à faire 3**

* Quelle _précondition_ doit vérifier ce tableau de pièces ?
* Proposer un algorithme glouton en langage naturel pour le rendu de monnaie.


**à faire 4**

Programmer cet algorithme en Python. Testez le avec un système canonique et un
non canonique. Utiliser des exemples qui montrent que l'algorithme glouton
échoue si le système n'est pas canonique.

## Ouverture sur le programme de terminale

Comment résoudre le problème de rendu de monnaie si le système n'est pas
canonique ?

En faisant une recherche exhaustive des solutions, c'est à dire en listant
toutes les combinaisons possibles.

C'est nettement plus délicat à écrire et cela pose des difficultés (à la fois dans
les concepts et dans la pratique).

Nous verrons deux méthodes qui permettent d'aborder ce problème : avec ou sans "programmation dynamique".

La _programmation dynamique_ est une méthode qui consiste à sacrifier un peu
de mémoire pour ensuite gagner beaucoup de calculs.

On cherche, en _programmation dynamique_ à se _souvenir_ de ce qu'on a déjà fait
afin de ne plus le refaire inutilement.

Par exemple, pour le système de pièces `[1, 5, 7]` qui n'est pas canonique,
la solution optimale pour rendre `11` est `[5, 5, 1]` (et pas `7, 1, 1, 1, 1`).

On garde donc en mémoire ce résultat lors d'une résolution de problème plus difficile.
Ainsi, si on rencontre à nouveau `11` à rendre, on va chercher en mémoire plutôt
que de recalculer. Dans de nombreux cas, c'est plus efficace.

Parfois c'est ajouter de la complexité sans gagner grand chose, parfois c'est
le seul moyen de concevoir un algorithme qui se termine rapidement.
