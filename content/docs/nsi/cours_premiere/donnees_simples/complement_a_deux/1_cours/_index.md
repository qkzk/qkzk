---
title: "Cours"
bookCollapseSection: true
author: "qkzk"
weight: 1
date: 2020/07/25

---

pdf [pour impression](./complement_a_2_eleves.pdf)


# Le complément à deux : comment représenter les entiers relatifs ?

## Les entiers relatifs

* **Entiers naturels :** entiers positifs ou nuls
    (0, 1, 2 etc.)
* **Entiers relatifs :** entiers de n'importe quel signe
    (..., -2, -1, 0, 1,...)

### Le problème du signe :

Un signe n'est pas un nombre... On ne peut pas l'encoder directement en binaire.


{{< hint info >}}
Le principe est d'attribuer au _bit de poids fort_ (premier bit) le signe du
nombre.

* Si le _bit de poids_ fort est **0**, le nombre est **positif**,
* Si le _bit de poids_ fort est **1**, le nombre est **négatif**.
{{< /hint >}}

## Nombres encodés sur un octet

### Contrainte immédiate :
Il faut que la machine sache quelle est la taille du nombre !

Sinon :

* Comment déterminer "le bit de poids fort" ?
* Comment savoir où s'arrête le nombre ?

{{< hint danger >}}
Dans tout ce document, on encodera **nos nombres entiers sur 8 bits.**
{{< /hint >}}

## Approche naïve : binaire signé

Essayons avec cette simple règle :

Pour encoder un entier sur 8 bits,

* On détermine la représentation binaire de sa valeur absolue
* Ensuite on remplit de `0` à gauche.

**Signe**

* Si le nombre est positif, on garde le bit de poids fort à 0,
* **Sinon, on met le bit de poids fort à 1.**

Ce qui fait donc :

{{< hint info >}}
**Binaire signé sur un octet**
* 1 bit de signe (0: positif, 1, négatif),
* 7 bits pour la valeur absolue.
{{< /hint >}}


On peut donc représenter de `1 111 1111` à `0 111 1111` soit de -127 à 127.

Que dire des nombres : `1 000 0000` et `0 000 0000` ? 

Ils valent tous deux 0... on les note -0 et +0.

**Premier exemple : 27**

```

27 = 0b11011

On complète sur 8 bits :
27 = 0001 1011

27 > 0 on garde le premier bit à 0
```

La représentation en binaire signé sur un octet de 27 est `0 001 1011`

**Autre exemple : -9**

```

La valeur absolue de -9 est 9.

9 = 0b1001

On complète sur 8 bits :
9 = 0000 1001

-9 < 0 on remplace le premier bit par -1 :

-9 = 1 000 1001
```

La représentation en binaire signé sur un octet de -9 est `1 000 1001`

**Jusqu'ici tout va bien...**

### Et soudain, c'est le drame...

Essayons d'ajouter ces exemples :

Vérifions que $27 + (-9) = 18$

```
   0001 1011
+  1000 1001
------------
=  1010 0100
```

... mais `1 010 0100 = -36` en binaire signé sur un octet...


{{< hint info >}}
**Le binaire signé ne permet pas de réaliser les additions habituelles**
{{< /hint >}}

---

### Exercice 1

On suppose toujours nos entiers encodés sur un octet.

1. Donner la représentation binaire signé de 12, de -100 et de -88.
2. Réaliser l'addition binaire bit à bit 12 + (-100).
3. Comparer avec le résultat obtenu.



Avec le binaire signé, **on ne peut plus réaliser d'opération naturelle sur les entiers**.
On a maintenant deux objectifs :

1. Représenter les entiers relatifs,

2. Conserver le même algorithme pour l'addition

---

## Le complément à deux


On doit encore travailler avec **une taille fixe**

On choisit à nouveau 8 bits par simplicité.

### Entiers positifs


1. Coder l'entier en binaire comme d'habitude,
2. Compléter l'octet avec des 0 devant.

### Entiers négatifs


1. Coder la valeur absolue du nombre en binaire,
2. Compléter l'octet avec des 0 devant,
3. Échanger tous les bits ($1 \leftrightarrow 0$),
4. Ajouter 1.


### Signe du complément à deux

* Si le bit de poids fort est 0, le nombre est positif
* Si le bit de poids fort est 1, le nombre est négatif

**Exemple 1 : 27**


```

1. coder l'entier en binaire comme d'habitude,
    27 = 0b11011
2. compléter l'octet avec des 0 devant.
    27 = 0b 0001 1011
```

Le complément à 2 sur un octet de 27 est `0b 0001 1011`

**Exemple 2 : -9**


```

1. coder la valeur absolue du nombre :
    9 = 0b1001
2. compléter l'octet :
    0b 0000 1001
3. échanger tous les bits :
    0b 1111 0110
4. ajouter 1 :
    0b 1111 0111
```

Le complément à 2 sur un octet de $-9$ est `0b 1111 0111`

## Complément à 2, méthode rapide


La méthode précédente se code facilement, elle est plus pénible à la main.

La méthode rapide : complément à 2 sur un octet de $n$ :

{{< hint info >}}
Si l'entier est négatif : 

1. donner la représentation binaire de la valeur absolue
2. Compléter à gauche jusqu'à avoir la taille voulue
3. de droite à gauche, conserver tous les bits jusqu'au premier 1 inclus
4. changer tous les bits à gauche
{{< /hint >}}


**Exemple $n = -108$**

1. Valeur absolue : 

    $|n| = 108 = 64 + 32 + 8 + 4$

    Représentation binaire :

    $|n| = 108$ = `110 1100`

2. Compléter :

    $|n| = 108$ = `0110 1100`

3. Conserver les 0 à droite jusqu'au premier 1 inclus, changer tous les
    bits à gauche.

    $n = -108$ = `  10010  100`

La représentation en complément à 2 sur un octet de $-108$ est `1001 0100`.





**Vérifions : $27 + (-9)$**


```
  0001 1011
+ 1111 0111
-----------
= 0001 0010
```

On a bien `18 = 0b10010`

**Remarque** la dernière retenue (tout à gauche) disparait.

---

### Exercice 2

Donner les compléments de à 2 sur un octet de 12, -100 et de -88.


### Exercice 3

1. Réaliser l'addition binaire des compléments à 2 des nombres 12 et -100.
2. Vérifier qu'on retrouve bien le résultat précédent pour -88.

---

## Du complément à deux au décimal

### Si l'entier est positif (son premier bit est 0)

On fait comme d'habitude.

**Exemple :** `0b 0001 1011`

$1 \times 1 + 1\times 2 + 1\times 8 + 1\times 16 = 27$


### Si l'entier est négatif (son premier bit est 1)

1. Échanger tous les bits $0 \leftrightarrow 1$,
2. Ajouter 1,
3. Convertir en décimal normalement,
4. Changer le signe.

**Exemple : `0b 1111 0111`, en complément à 2 sur 8 bits,**


```
1. On échange tous les bits,
    0b 0000 1000
2. On ajoute 1,
    0b 0000 1001
3. On converti en binaire comme d'habitude,
    0b 1001 = 1 * 1 + 1 * 8 = 9
4. On change le signe.
    0b 1111 0111 = -9
```

{{< hint info >}}
## Du complément à 2 au le décimal, méthode rapide.

Si le nombre est positif, comme d'habitude.

Si le nombre est négatif :

1. De droite à gauche, conserver tous jusqu'au premier 1 inclus,
2. Échanger tous les bits **à gauche** de ce 1,
3. Convertir en décimal normalement,
4. Changer le signe,
{{< /hint >}}

**Exemple : `0b 1010 1000`, en complément à 2 sur 8 bits**


1. De droite à gauche, conserver tous jusqu'au premier 1 inclus,\
    `0000` et `1000` qui sera conservé
2. Échanger tous les bits à gauche de ce 1,\
    `0101 1000`
3. Convertir en décimal normalement,\
    `0101 1000` = $8 + 16 + 64 = 88$
4. Changer le signe :\
    en complément à 2 sur un octet $n =$ `1010 1000` $=-88$

---

### Exercice 4

Donner les notations décimales des compléments à deux sur un octet suivants :

1. `a = 0b1111 1111`
2. `b = 0b1000 0000`
3. `c = 0b0111 1111`
4. `d = 0b1010 0011`
5. Calculer `a + b` et `c + d` en binaire et vérifier le résultat.

---

## Propriétés

### Table de valeurs

La table de valeur est remarquable, en particulier les "petits" nombres négatifs sont remplis de 1.

```
 bit
 de
signe
    0 1 1 1 1 1 1 1 =  127
    0      ...      =  ...
    0 0 0 0 0 0 1 0 =    2
    0 0 0 0 0 0 0 1 =    1
    0 0 0 0 0 0 0 0 =    0
    1 1 1 1 1 1 1 1 =   -1
    1 1 1 1 1 1 1 0 =   -2
    1      ...      =  ...
    1 0 0 0 0 0 0 1 = -127
    1 0 0 0 0 0 0 0 = -128
```

### Combien d'entiers relatifs sur un octet ?


> Sur 8 bits en complément à deux, on peut encoder de $-128$ à $127$,

### Combien d'entiers relatifs sur avec `n` bits ?


{{< hint info >}}
Sur  $n$ bits on peut encoder de $-2^{n-1}$ à $2^{n-1} - 1$.
{{< /hint >}}


### Exercice 5

1. Combien d'entiers positifs peut-on encoder en binaire sur 32 bits ?
2. Combien d'entiers peut-on encoder en complément à 2 sur 32 bits ?
3. Expliquer.

---

## Complément à 2 : résumé

{{< hint info >}}
* Le complément à 2 sur $n$ bits permet de représenter des entiers positifs et négatifs,
* Le signe du nombre est donné par le premier bit,
* L'addition usuelle fonctionne aussi avec les entiers _négatifs_.
* Cette méthode permet d'encoder sur $n$ bits les entiers de $-2^{n-1}$ à $2^{n-1} - 1$
* La méthode rapide pour encoder un entier en complément à 2 sur un octet :
    * s'il est positif, on l'écrit en binaire et on complète l'octet avec des 0 à gauche,
    * s'il est négatif, 

        * on écrit sa valeur absolue en binaire qu'on complète à gauche,
        * on conserve tous les 0 à droite jusqu'au premier 1 inclus,
        * on inverse tous les bits à gauche de ce premier 1.
* Pour décoder on fait le contraire
{{< /hint >}}

---


## Python et le complément à 2.

Les opérations précédentes imposent de choisir une **taille maximale pour les entiers** 

Dans Python les entiers ont une **taille arbitraire**, il ne peut afficher nativement le complément à deux.

```python
>>> bin(12)
'0b1100'
>>> bin(-12)
'-0b1100'
```

Pour obtenir le complément à 2, il faut le programmer.

_Dans de nombreux langages, on distingue les entiers positifs des négatifs et différentes tailles sont proposées._
