---
title: "binaire - TD"
bookCollapseSection: true
author: qkzk
weight: 2

---

### pdf : [pour impression](/uploads/docsnsi/donnees_qkzk_img/TD_binaire.pdf)

## 1. Conversion binaire vers décimal.

1. Donnez les valeurs entières décimales représentées par les nombres :

    * `0b101`
    * `0b10101`
    * `0b0101`
    * `0b00101`
    * `0b1101 1101`
    * `0b1001 0111`
    * `0b1011 1000`

2. Comment savoir qu'un entier représenté en binaire est divisible par 2 ? Par 4 ?

## 2. Conversion décimal vers binaire.

1. Convertir les nombres suivants en binaire :

  * 12
  * 23
  * 35
  * 127
  * 211
  * 254
  * 231

2. Calculer mentalement les puissances de 2 jusque $2^{20}$.

3. On considère des entiers représentés sur 1 octet. Quel est le plus grand
    entier représentable ?
    Réaliser l'addition binaire entre $a = 0b1101 1001$ et $b = 0b1110 1100$.

    Qu'advient-il du premier bit lors de cette addition ?
4. Quelle est la représentation binaire d'un nombre de la forme $2^k-1$ ?
    De la forme $2^k$ ?
5. En remarquant que $2~048=2^{11}$, donner la représentation binaire de $2021$.

## 3. Binaire et python

Python permet d'obtenir la représentation binaire d'un entier à l'aide de la
fonction `bin`. Voici ce qu'on obtient avec `help(bin)` :

```
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.

    >>> bin(2796202)
    '0b1010101010101010101010'
```

Inversement, la conversion d'une base $b$ vers la représentation décimale
s'obtient en passant à `int` une chaîne de caractères ainsi que la base.

Voici ce qu'on obtient avec `help(int)`

```
class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
```

1. Quelle instruction saisir pour obtenir la représentation décimale de `0b1101001` ?
2. $x$ est un entier dont la réprésentation binaire est `110100`. Donner
  deux instructions différentes permettant d'obtenir sa représentation décimale.
3. Quel sera le résultat des instructions suivantes ?

  ```python
  >>> bin(123)
  >>> int("0b1111")
  >>> int("0b10101", 2)
  >>> bin(0)
  >>> int("0b101211", 2)
  ```


## 4. Capacité

Parmi les additions suivantes, lesquelles vont provoquer un dépassement de
capacité lorsque les nombres sont encodés sur 8 bits ?

* $1111~1011 + 1001~1111$
* $1001~1011 + 0111~1011$
* $0011~1011 + 1001~1001$
* $1010~1011 + 0001~0100$

