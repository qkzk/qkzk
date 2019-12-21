---
title: Travaux dirigés assembleur AQA
author: qkzk
theme: metropolis
weight: 6
# mainfont: Noto Sans CJK JP
---

# TD assembleur AQA


Dans ce TD nous allons travailler avec l'assembleur AQA disponible
[ici](http://www.peterhigginson.co.uk/AQA/).

La documentation d'origine est [ici](http://www.peterhigginson.co.uk/AQA/info.html)
et une traduction des commandes principales est disponible [ici](../doc)

Après avoir réalisé les [premières questions](../assembleur_aqa_intro),
répondre aux questions suivantes.

## Exercice 1 - quelques exemples

Exécuter les différents exemples qui sont proposés (menu **select**, **run**)

Hormis pour "new IO" qui est très long, suivre le parcours de l'information
dans chacun des cas.

## Exercice 2 - minimum

En vous inspirant de l'exemple proposé, créer un programme qui renvoie
dans sa sortie le minimum de deux nombres donnés en entrée.

## Exercice 3 - multiplication

On souhaite écrire un programme qui réalise une **multiplication**.
(Vérifiez dans les commandes, il n'y a pas...)

* En entrée (saisie clavier), 2 nombres entiers positifs
* En sortie (affichage), leur produit.

1. Comment, à l'aide d'addition, réaliser le produit $3 \times 4$ ?
2. Ecrire un programme Python (ou un progammme en langage naturel) qui réalise
    ce cahier des charges.
3. Ecrire le code assembleur AQA correspondant et le tester.

## Exercice 4 - suite de Fibonacci

Vous connaissez peut-être la suite de Fibonacci qui est souvent citée en
informatique. En voici une définition simple :

* Son premier terme est 0.
* Son second terme est 1.
* Pour obtenir le terme suivant, on ajoute les deux précédents

Donc $u_0=0, u_1=1$ et $u_2=u_1 + u_0=1+0 = 1$

Ensuite on obtient : $u_2=1+1=2, u_3=2+1=3, u_4=3+2=5, u_5=8, u_6=13$

les premiers termes, sans indices sont :

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233$ etc.


**On souhaite construire cette suite dans l'assembleur AQA.**

Voici un programme Python qui affiche ligne par ligne les termes inférieurs à
255 :

~~~python
x = 0
y = 1
while x < 255:
  print(x)
  z = y
  y = x + y
  x = y
~~~

1. Vérifiez que ce programme Python fonctionne.

    Remarquez bien ce qui est fait pour échanger les valeurs (`x` devient `y`)

2. Ecrire ce programme en assembleur.

_Remarquez qu'on obtient les résultats en lignes, ce qui nous convient tout à_
_à fait_
