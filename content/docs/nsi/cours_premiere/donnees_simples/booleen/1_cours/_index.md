---
title: "Booléens : cours"
bookCollapseSection: true
author: "qkzk"
weight: 1

---

### pdf : [diaporama](/uploads/docsnsi/booleens/booleen_cours.pdf)

# Booléen

## Booléen

En programmation, un booléen est un type de variable à deux états : _vrai_ et _faux_.

Ils sont nommés ainsi d'après George Boole, fondateur de l'alèbre de Boole.


## Booléen en Python


En Python, les booléens sont `True` et `False`, ils sont du type `bool`

```python
True
print(type(True))   # <class 'bool'>
False
print(type(False))  # <class 'False'>
```

## Comparaison

Les opérateurs de comparaison courants sont identiques à ceux des mathématiques
mais ATTENTION, il ne faut pas confondre l'égalité et l'affectation

```python
variable = 5    # une affectation
5 == 8          # une égalité (qui est fausse)
```

**Le résultat d'une comparaison est toujours un booléen**

## Comparaisons des nombres

| Comparaison       | Symbole | Exemple       | Résultat |
|-------------------|---------|---------------|----------|
| Égalité           | `==`    | `1 + 2 == 3`  | `True`   |
| Différence        | `!=`    | `1 + 2 != 3`  | `False`  |
| Supérieur         | `>`     | `4 > 3`       | `True`   |
| Inférieur         | `<`     | `2.2 < 2 * 3` | `True`   |
| Supérieur ou égal | `>=`    | `5 >= 6`      | `False`  |
| Inférieur ou égal | `<=`    | `8 <= 3`      | `False`  |

## Appartenance à une structure

On peut tester qu'un élément appartient à une structure avec le mot clé `in`

```python
"a"     in "bonjour"        # False
"bon"   in "bonjour"        # True
1        in [2, 3, 4]        # False
```

# Opérations sur les booléens


Les opérateurs sur les booléens sont de deux types :

* opérateur unaire : prend _un_ booléen et en renvoie _un_.
* opérateur binaire : prend _deux_ booléens et en renvoie _un_.

## Opérateur unaire : la négation

### La négation: `not`

C'est le seul opérateur _unaire_, il donne le contraire de ce qu'on lui passe.

```python
not True    # s'évalue à False
not False   # s'évalue à True
```

### Table de vérité avec `True` et `False`

| `a`     | `not a` |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |

## Table de vérité avec des bits

Les _tables de vérité_ sont abbregées en notant :

* `1` pour `True`
* `0` pour `False`

| `a` | `not a` |
|-----|---------|
| `1` | `0`     |
| `0` | `1`     |

## Opérateur binaire : le OU, noté `or`


**Il est vrai si l'un des deux booléens est vrai.**


```python
False or False  # False
False or True   # True
True or False   # True
True or True    # True
```

| `a` | `b` | `a or b` |
|-----|-----|:--------:|
| 0   | 0   | 0        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 1        |




## Opérateur binaire : le ET, noté `and`


**Il est vrai si les deux booléens sont vrais.**


```python
False and False  # False
False and True   # False
True and False   # False
True and True    # True
```

| `a` | `b` | `a and b` |
|-----|-----|:--------:|
| 0   | 0   | 0        |
| 0   | 1   | 0        |
| 1   | 0   | 0        |
| 1   | 1   | 1        |

## Opérateur binaire : le XOR noté `^`

**Il est vrai si EXACTEMENT un des deux booléens est vrai**


```python
False ^ False  # False
False ^ True   # True
True ^ False   # True
True ^ True    # False
```

| `a` | `b` | `a XOR b` |
|-----|-----|:--------:|
| 0   | 0   | 0        |
| 0   | 1   | 1        |
| 1   | 0   | 1        |
| 1   | 1   | 0        |

## Python et les booléens

Python permet de comparer n'importe quoi à un booleen.

Par exemple, une chaîne de caractère vide est évaluée à fausse.

```python
bool(1)             # True
bool(0)             # False
bool("")            # False
bool("abc")         # True
bool([])            # False
bool([1, 2])        # True
```

* 0 est faux, les autres entiers sont vrais,
* une structure vide est fausse, les autres sont vraies.

## Complément : `None` et l'identité `is`

Python propose la valeur `None` (rien) qui est fréquement utilisé pour
représenter l'absence d'une valeur.

Étant le seul objet du type `NoneType`, on peut tester son _identité_ avec `is` :

```python
1 is None       # False
"abc" is None   # False
None is None    # True
a = 5
a is None       # False
```

On verra plus tard qu'une _fonction_ qui ne se termine par `return ...` renvoie
néanmoins `None`.

## Table de vérité plus complexe

On peut chaîner les opérations booléennes pour construire une _expression booléenne._

Une colonne par valeur et une colonne pour l'expression :

| `a` | `b` | `c` | `(a and b) or (not c)` |
|-----|-----|-----|:----------------------:|
| 0   | 0   | 0   |            1           |
| 0   | 0   | 1   |            0           |
| 0   | 1   | 0   |            1           |
| 0   | 1   | 1   |            0           |
| 1   | 0   | 0   |            1           |
| 1   | 0   | 1   |            0           |
| 1   | 1   | 0   |            1           |
| 1   | 1   | 1   |            1           |

















