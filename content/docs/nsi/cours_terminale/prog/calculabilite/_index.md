---
title: "Problème de l'arrêt en Python"
bookCollapseSection: true
author: qkzk
date: 2020/03/03
weight: 100
---

# Calculabilité - Problème de l'arrêt en Python

## Terminaison

On dit qu'une fonction **termine** si elle renvoie une valeur ou si elle lève une exception (par exemple `ZeroDivisionError` si une division par zéro est tentée).

Avec cette définition, seulement deux situations peuvent se présenter lorsqu'on appelle une fonction :

* Elle _termine_,

ou 

* Elle _continue à calculer à l'infini_

Ainsi, la fonction `ma_fonction` (voir ci-dessous), termine pour un entier `n` inférieur ou égal à 10 (elle renvoie `None`) et ne termine pas pour `n` strictement plus grand que 10.

En outre, cette fonction termine pour une chaîne de caractères `n` (en levant l'exception `TypeError` à cause de l'opération `+`).

~~~python
def ma_fonction (n):
  while n != 10 :
    n = n + 1
~~~

## De l'utilité d'une fonction `arret`

On pourrait penser qu'il serait utile d'avoir en Python une fonction arrêt : 

* qui termine sur toutes les entrées possibles, 
* telle que `arret(f, x)` renvoie `True` si le calcul de `f(x)` termine 
* et `False` sinon.

Une telle fonction, si elle était ajoutée au langage, permettrait d'éviter les boucles infinies en faisant un simple test.

Si on voulait programmer une telle fonction, il serait naturel que la fonction `arret` accède au code de la fonction `f` (ce qui est possible grâce au module  `dis`), et analyse ce code, par quelque moyen compliqué, pour en déduire si oui ou non le calcul de `f(x)` va un jour terminer.

## Le Problème de l'arrêt...

La question _Est-il possible de programmer une telle fonction ?_ est connue sous le nom de **problème de l'arrêt**. 

## est impossible.

Nous allons montrer qu'une telle fonction ne peut pas exister. 

Pour cela, nous allons employer un raisonnement par l'absurde.

### Hypothèse

Supposons que quelqu'un ait réussi à programmer cette fonction `arret`.

### La fonction `strange`

Nous pouvons alors l'utiliser pour programmer la fonction `strange` suivante :

~~~python
def strange(f, x):
  if arret(f, x):
    while True:
      pass
~~~

Cette fonction teste si le calcul de `f(x)` termine.

* si c'est le cas, elle rentre dans une boucle infinie dans laquelle elle ne fait rien.

* Si ce n'est pas le cas, elle ne fait rien et termine.


**Autrement dit, `strange(f, x)` termine si et seulement si `f(x)` ne termine pas.**

### La fonction `paradox`

La précédente fonction nous permet d'en définir une nouvelle, la fonction `paradox`.

~~~python
def paradox(f):
  strange(f, f)
~~~

Par construction, le calcul de `paradox(f)` termine si et seulement si le calcul de `f(f)` ne termine pas. Appelons (1) cette propriété.

### `paradox(paradox)` ?

Maintenant, demandons-nous si le calcul de `paradox(paradox)` termine.

Pour cela, dans la propriété (1), remplaçons `f` par `paradox`.

La propriété devient : " le calcul de paradox(paradox) termine si et seulement si le calcul de paradox(paradox) ne termine pas ".


Cette dernière propriété est évidemment absurde (elle se contredit elle même).


Nous pouvons donc conclure notre raisonnement par l'absurde et affirmer qu'il est impossible de programmer la fonction `arret`.

### Remarque

Cela reste impossible même si on se limite à ce que les arguments de arrêt soient une fonction `f` des entiers dans les entiers et un entier `x`. Pourquoi ? Simplement parce que n'importe quelle valeur de n'importe quel type sera représenté en machine par une suite d'octet, soit à peu près un entier naturel.


## Complément

La résolution du problème de l'arrêt par Alonzo Church et lan Turing, en 1936 a eu de nombreuses conséquences
en informatique et en mathématiques. La résolution de ce problème a conduit Alan Turing à créer les machines de Turing, modèle mathématiques à l'origine des ordinateurs modernes...

En particulier, il n'est pas possible d'écrire un assistant de programmation qui repère
tous les problèmes qu'un code présente avant de l'avoir exécuté.

Il n'est pas non plus possible d'écrire un ramasse miette (_garbage collector_) qui soit parfait.
Un ramasse miette cherche à libérer des zones de la mémoire après leur dernière utilisation
dans un programme.
Ces outils existent dans beaucoup de langages modernes (python, java, Golang etc.) mais
ne sont jamais parfaits, en effet, l'existance d'un ramasse miette parfait est équivalente
au problème de l'arrêt.

## Vidéo

Voici une [vidéo](https://www.youtube.com/watch?v=a5MNIzu9Ia4) de l'université de Rennes qui expose la preuve précédente.
