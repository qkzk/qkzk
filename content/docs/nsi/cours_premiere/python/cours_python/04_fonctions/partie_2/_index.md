---
title: "Partie 2"
bookCollapseSection: true
author: "qkzk"
date: ""
weight: 2

---

## Simplifier le code d'une fonction

C'est une démarche qu'il faut envisager systématiquement : nos fonctions doivent
être les plus simples possibles.

Commençons par un exemple simple : la fonction `est_pair` accepte un entier
en parametre et renvoie un booléen vrai si l'entier est pair, faux sinon.

{{< python title="est pair ?" >}}def est_pair(entier):
    if entier % 2 == 0:
        return True
    else:
        return False
{{< /python >}}

### Exercice 1 : 

1. Lire et tester la fonction précédente. Remarquez que le mot clé `return` est présent
  deux fois.
2. Ajouter la documentation et les indications de type.
3. Quelles sont les valeurs possibles de `entier % 2` ?
4. Quelles sont les valeurs possibles de `entier % 2 == 0` ? Dans quel cas
  est-il égal à `True` ? à `False` ?

On en déduit qu'il est possible d'écrire la fonction ainsi :

```python
def est_pair_plus_court(entier):
    return entier % 2 == 0
```

5. Vérifiez sur des exemples que les deux versions font la même chose.



## Portée des variables : variables globales et locales

La _portée_ d'une variable et la partie du programme dans laquelle cette variable
est définie.

On distingue essentiellement deux types de portées : les variables _globales_
qui sont accessibles partout et les variables _locales_ qui n'existent
que dans une fonction.

Considérons l'exemple suivant :

```python
a = 10          # a est une variable GLOBALE

def ma_fonction():

    return a
```

Exécutons le script

Lorsqu'on exécute `ma_fonction()` elle renvoie 10.

```python
>>> a               # nous sommes dans l'espace GLOBAL
10
>>> ma_fonction()   # ma_fonction a accès à l'espace global
10
```


Et maintenant :

```python
a = 10          # a est une variable GLOBALE

def ma_fonction():

    a = 20      # on défini une variable LOCALE
    return a
```

```python
>>> a               # a vaut toujours 10 :)
10
>>> ma_fonction()   # ma_fonction renvoie SA VALEUR de a
20
>>> a               # la valeur GLOBALE de a n'a pas changé !
10
```

Exécutez le script suivant et recommencez en commentant la ligne `a = 20`

{{< python title="Portée locale et globale" >}}
a = 10

def ma_fonction():
    a = 20  # Commentez cette ligne et exécutez à nouveau
    return a

print("avant l'exécution", a)
print("exécution", ma_fonction())
print("après l'exécution", a)
{{< /python >}}

Maintenant commentez les deux affectations à `a` : `a = 10` et `a = 20`.

Quelle erreur obtient-on ?


### Résumé : 
{{< hint warning >}}
Lorsque Python rencontre un nom de variable, il utilise la définition _locale_. 

Sans définition locale, il utilise la définition _globale_.

Sinon il plante et lève une exception `NameError`.
{{< /hint >}}

### Le mot clé `global`

Le mot clé `global`, indiqué au début du bloc de code d'une fonction, précise
qu'une variable est maintenant globale et qu'on peut la modifier.


```python
a = 10          # a est une variable GLOBALE

def ma_fonction():

    global a    # a est maintenant globale !

    a = 20      # on défini une variable LOCALE
    return a
```

```python
>>> a               # a vaut toujours 10 :)
10
>>> ma_fonction()   # ma_fonction renvoie SA VALEUR de a, MAIS !!!
20
>>> a               # la valeur GLOBALE A ETE CHANGEE PAR ma_fonction
20
```

**L'utilisation de variables globales est une mauvaise pratique.**

Il est difficile de suivre l'évolution de variables globales lorsqu'on lit
un script.

{{< python title="Mot clé global" >}}
a = 10

def ma_fonction():
    global a
    a = 20  # Commentez cette ligne et exécutez à nouveau

print("avant l'exécution", a)
ma_fonction()   # la fonction change la valeur GLOBALE
print("après l'exécution", a)
{{< /python >}}

## Exercices

Pour chaque fonction produite on attend :

* des noms explicites,
* la documentation complète,
* des exemples qui attestent que la fonction fait ce qui est attendu,

_Remarque_ : trop d'exercices différents pour mon site, vous devrez les traiter à l'extérieur.

### Exercice 2

Écrire une fonction `carre` qui calcule le carré d'un nombre.


### Exercice 3

Écrire une fonction qui calcule l'aire d'un disque.

```python
>>> from math import pi
>>> pi
3.141592653589793
```

Rappels aux grands géomètres que vous êtes : 

> L'aire d'un disque de rayon $R$ est donnée par : $$\mathcal{A} = \pi R^2$$


### Exercice 4

Écrire une fonction qui prend deux chaînes de caractères et renvoie la plus
courte des deux.

```python
>>> plus_court("abc", "abcd")
'abc'
>>> plus_court("abcd", "ab")
'ab'
```


### Exercice 5 - la fonction `sum`

Python propose de nombreuses fonctions très pratiques... pourquoi les réécrire ?

Et bien pour apprendre c'est le seul moyen.

1. Que fait la fonction `sum` ?
2. Comment calculer la somme des entiers de 1 à 100 avec la fonction `sum` ?
3. Voici un algorithme pour calculer la somme des entiers entre $a$ et $b$ inclus :

    ```
    somme = 0
    Pour k allant de a à b inclus,
        somme = somme + k
    fin du pour

    # à cette étape, somme contient la valeur !
    ```

    Programmer cet algorithme dans une fonction `somme` qui accepte deux
    paramètres `a` et `b` et renvoie la somme des entiers entre `a` et `b`.

    On suppose que $a \leq b$.

    On prendra garde aux noms, dans l'algorithme `somme` désigne un _nombre_
    mais pour notre fonction, `somme` est _la fonction elle-même !_, il faudra
    donc employer un _autre nom_ pour désigner la valeur de la somme.



### Exercice 6 - générateur de mot de passe

1. Relisez l'aide de la fonction `random.choice`.
2. À l'aide de cette fonction, créer une fonction `password` qui prend un
  paramètre entier (la taille du mot de passe) et renvoie un mot de passe
  constitué de lettres ou de chiffres respectant la taille donnée.

    ```python
    symboles = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ```

    ```python
    >>> password(10)
    'mHVeC5rs8P'
    >>> password(6)
    'PYthoN'
    ```


### Exercice 7 - déterminer la sortie

Pour chaque question suivante, vous analysez le code écrit, prédisez la sortie
et vérifiez. Faites le sérieusement sinon vous aurez de grandes surprises
en devoir...

1. Qu'affiche le script suivant ?

    ```python
    def func(a):
        a += 2.0
        return a

    a = func(8.0)
    print(a)
    ```
2. Qu'affiche le script suivant ?

    ```python
    def diff(val1,val2):
        return val2 - val1

    a = diff(3.0,-2.0)
    print(a)
    ```
3. Qu'affiche le script suivant ?

    ```python
    def func(val):
      if val < 0.0:
          return 0
      return val

    a = func(-1.5)
    print(a)
    ```
4. Qu'affiche le script suivant ?

    ```python
    def carre(val):
        return val*val

    def inc(val):
        return val + 1

    a = carre(inc(3.0))
    print(a)
    ```

5. Qu'affiche le script suivant ?

    ```python

    def func(a):
      a += 2.0
      return a

    a = 5.0
    b = func(a)
    print(a, b)
    ```
7. Qu'affiche le script suivant ?

    ```python
    def func(a):
        a += 7

    a = 9
    b = func(a)
    print(a, b)
    ```


6. _Plus difficile_. Qu'affiche le script suivant ?

    ```python
    def f(x):
        return x

    y = f(4)
    print(y)
    g = f(f)
    print(g(2))
    f = f(3)
    print(f)
    print(g(5))
    print(f(6))
    ```

