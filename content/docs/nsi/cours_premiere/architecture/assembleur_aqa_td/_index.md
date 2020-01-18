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


## 5. Test de parité

### Problème

On souhaite écrire un programme assembleur qui résolve le problème suivant :

on lui donne un nombre entier et il affiche "pair" ou "impair".

### Solution naïve en Python

En Python, c'est trivial : il suffit d'utiliser modulo. `n % 2` renvoie le
reste de la division entière par 2. Si ce reste est nul, l'entier est pair.
Sinon, l'entier est impair.

Dans une fonction, on peut envisager ceci :

~~~python
def parite(entier):
  '''
  @param entier: (int)
  @return: (str)
  '''
  if entier % 2 == 0:
    return "pair"
  else:
    return "impair"
~~~

qui s'utilise comme ceci :

~~~python
>>> parite(20)
"pair"
>>> parite(21)
"impair"
~~~

On le comprend bien :

**Créer un test de parité équivaut à créer un opérateur "modulo 2"**

C'est ce que nous allons faire.

Mais comment faire quand on ne dispose que de très peu d'opérations comme
dans l'assembleur AQA ?

### Solution avec des soustractions

Considérons l'algorithme suivant :

~~~
n un entier positif
Tant que n > 0:
    n prend la valeur n - 2
Si n == 0:
    renvoyer "pair"
Si n < 0:
    renvoyer "impair"
~~~

* Testons pour `n=3` :

  `n` prend successivement les valeurs `3, 1 et -1` ensuite la boucle s'arrête.\
  `-1` étant négatif, l'algorithme renvoie "impair". C'est juste.

* Testons pour `n=4` :

  `n` prend successivement les valeurs `4, 2, 0` et la boucle s'arrête.\
  `n=0` et l'algorithme renvoie "pair". C'est juste encore une fois.


### Programmer cet algorithme en AQA

Description des étapes du code assembleur.

On commence par demander une entrée, sous la forme d'un entier:

~~~
   INP R0, 2
~~~

Ensuite on crée un label "soustraction"

~~~
soustraction:
~~~

On compare le registre 0 avec l'entier `1`. Si la comparaison  est égale, on saute au label "impair"
On compare le registre 0 avec l'entier `0`. Si la comparaison  est égale, on saute au label "pair"


Sinon, on soustrait 2 au registre 0 et on revient à "soustraction"

* programmer cette partie

~~~
SUB R0, R0, #2
B soustraction
~~~

Après avoir écrit la boucle, il faut écrire ce que contiennent les labels "pair" et "impair"

~~~
impair:
      MOV R1,#1
      OUT R1,4
      HALT
~~~

Ajouter ensuite le label "pair"

<!--
### Correction complète

~~~
  INP R0,2
soustraction:
  CMP R0,#1
  BEQ impair
  CMP R0,#0
  BEQ pair
  SUB R0, R0, #2
  B soustraction
impair:
  MOV R1,#1
  OUT R1,4
  HALT
pair:
  MOV R1,#0
  OUT R1,4
  HALT
~~~
-->

### Complément : l'opérateur modulo

L'opérateur modulo peut se programmer pour n'importe quel couple d'entier `a, b`
de la même manière, par soustraction successives.

Écrire un algorithme en langage naturel qui renvoie `a % b` et n'utilise
que des soustraction.

Programmez le dans l'assembleur AQA.

Votre programme a deux entrées successives (`a` et `b`) et une sortie `a % b`

<!--
~~~
  INP R0,2
  INP R1,2
soustraction:
  CMP R0,R1
  BLT sortie
  SUB R0, R0, R1
  B soustraction
sortie:
  OUT R0,4
  HALT
~~~
-->


### Complément : la division entière

Améliorez votre algorithme pour qu'il renvoie le quotient et le reste de la
division entière de `a` par `b`.

Par exemple, pour les entiers `a=7` et `b=3` votre algorithme renvoie `2` et `1`

car `7 = 2 * 3 + 1`


<!--
~~~
  INP R0,2
  INP R1,2
  MOV R2,#0
soustraction:
  CMP R0,R1
  BLT sortie
  SUB R0, R0, R1
  ADD R2, R2, #1
  B soustraction
sortie:
  OUT R2,4
  OUT R0,4
  HALT
~~~
-->
