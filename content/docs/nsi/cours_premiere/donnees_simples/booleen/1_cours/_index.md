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

Ils sont nommés ainsi d'après George Boole, fondateur de l'algèbre de Boole.

## Booléen en Python

En Python, les booléens sont `True` et `False`, ils sont du type `bool`

```python
True
print(type(True))   # <class 'bool'>
False
print(type(False))  # <class 'bool'>
```

### Comparaison

Les opérateurs de comparaison courants sont identiques à ceux des mathématiques
mais ATTENTION, il ne faut pas confondre l'égalité et l'affectation

```python
variable = 5    # une affectation
5 == 8          # une égalité (qui est fausse)
```

{{< hint info >}}
**Le résultat d'une comparaison est toujours un booléen**
{{< /hint >}}

### Comparaisons des nombres

| Comparaison       | Symbole | Exemple       | Résultat |
| ----------------- | ------- | ------------- | -------- |
| Égalité           | `==`    | `1 + 2 == 3`  | `True`   |
| Différence        | `!=`    | `1 + 2 != 3`  | `False`  |
| Supérieur         | `>`     | `4 > 3`       | `True`   |
| Inférieur         | `<`     | `2.2 < 2 * 3` | `True`   |
| Supérieur ou égal | `>=`    | `5 >= 6`      | `False`  |
| Inférieur ou égal | `<=`    | `8 <= 3`      | `False`  |

### Appartenance à une structure

On peut tester qu'un élément appartient à une structure avec le mot clé `in`

```python
"a"     in "bonjour"        # False
"bon"   in "bonjour"        # True
1       in [2, 3, 4]        # False
```

## Opérations sur les booléens

Les opérateurs sur les booléens sont de deux types :

- opérateur unaire : prend _un_ booléen et en renvoie _un_.
- opérateur binaire : prend _deux_ booléens et en renvoie _un_.

### Opérateur unaire : la négation

C'est le seul opérateur _unaire_, il donne le contraire de ce qu'on lui passe.

En français l'opérateur de négation est noté NON.
En Python, l'opérateur de négation est `not`.

```python
not True    # s'évalue à False
not False   # s'évalue à True
```

### Table de vérité avec `True` et `False`

| `a`     | `not a` |
| ------- | ------- |
| `True`  | `False` |
| `False` | `True`  |

## Table de vérité avec des bits

Les _tables de vérité_ sont abregées en notant :

- `1` pour `True`
- `0` pour `False`

| `a` | `not a` |
| --- | ------- |
| `1` | `0`     |
| `0` | `1`     |

## Opérateur binaire : le OU, noté `or`

**Il est vrai si l'un des deux booléens est vrai.**

```python
False or False  # False
False or True   # True
True  or False   # True
True  or True    # True
```

| `a` | `b` | `a or b` |
| --- | --- | :------: |
| 0   | 0   |    0     |
| 0   | 1   |    1     |
| 1   | 0   |    1     |
| 1   | 1   |    1     |

## Opérateur binaire : le ET, noté `and`

**Il est vrai si les deux booléens sont vrais.**

```python
False and False  # False
False and True   # False
True  and False   # False
True  and True    # True
```

| `a` | `b` | `a and b` |
| --- | --- | :-------: |
| 0   | 0   |     0     |
| 0   | 1   |     0     |
| 1   | 0   |     0     |
| 1   | 1   |     1     |

## Opérateur binaire : le XOR noté `^`

**Il est vrai si EXACTEMENT un des deux booléens est vrai**

```python
False ^ False  # False
False ^ True   # True
True  ^ False   # True
True  ^ True    # False
```

| `a` | `b` | `a XOR b` |
| --- | --- | :-------: |
| 0   | 0   |     0     |
| 0   | 1   |     1     |
| 1   | 0   |     1     |
| 1   | 1   |     0     |

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

- 0 est faux, les autres entiers sont vrais,
- une structure vide est fausse, les autres sont vraies.

## Complément : `None` et l'identité `is`

Python propose la valeur `None` (rien) qui est fréquement utilisé pour
représenter l'absence d'une valeur.

Étant le seul objet du type `NoneType`, on peut tester son _identité_ avec `is` :

```python
1     is None   # False
"abc" is None   # False
None  is None   # True
a = 5
a is None       # False
```

On verra plus tard qu'une _fonction_ qui ne se termine par `return ...` renvoie
néanmoins `None`.

## Table de vérité plus complexe

On peut chaîner les opérations booléennes pour construire une _expression booléenne._

Une colonne par valeur et une colonne pour l'expression :

| `a` | `b` | `c` | `(a and b) or (not c)` |
| --- | --- | --- | :--------------------: |
| 0   | 0   | 0   |           1            |
| 0   | 0   | 1   |           0            |
| 0   | 1   | 0   |           1            |
| 0   | 1   | 1   |           0            |
| 1   | 0   | 0   |           1            |
| 1   | 0   | 1   |           0            |
| 1   | 1   | 0   |           1            |
| 1   | 1   | 1   |           1            |

## Propriétés mathématiques de l'algèbre de Boole

Il existe de nombreuses notations utilisées pour décrire l'algèbre de Boole,
nous utiliserons les notations de Python.

### Définition

On considère l'ensemble `{0, 1}` ou `{False, True}` muni de trois opérations :

la **négation** `not`, le **et logique** `and`, le **ou logique** `or`.

Elles sont définies par les tables de vérité présentées plus haut.

### Complémentarité

- `not(not(a)) = a`
- `a or (not a) = 1`
- `a and (not a) = 0`

### Associativité

- `a or (b or c) = (a or b) or c`
- `a and (b and c) = (a and b) and c`

### Distributivité

- `a or (b and c) = (a and b) or (a and c)`
- `a and (b or c) = (a or b) and (a or c)`

_Ainsi, on retrouve les propriétés des opérations sur les nombres. Pour simplifier, `or` se comporte comme une somme et `and` comme un produit_.

### Autres tables de vérité

Toutes les opérations binaires peuvent être définies à l'aide des trois opérateurs présentés plus haut.

Par exemple : `a xor b = (a and not b) or (not a and b)`

Pour le vérifier, on construit les tables de vérité de chaque membre et on les compare.

### `a xor b = (a and not b) or (not a and b)`

<script src="/js/logic_simulator.js"></script>
<div style="width: 600px; height: 400px">
<logic-editor id="editor1" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [50, 50], id: 0, val: 1},
    in1: {type: 'in', pos: [50, 155], id: 1, val: 1},
    out0: {type: 'out', pos: [465, 100], id: 5},
    in2: {type: 'in', pos: [45, 285], id: 2, val: 1},
    out1: {type: 'out', pos: [470, 310], id: 3},
    in3: {type: 'in', pos: [45, 330], id: 4, val: 1},
    xor0: {type: 'xor', pos: [245, 310], in: [6, 7], out: 8},
    not0: {type: 'not', pos: [150, 50], in: 9, out: 10},
    not1: {type: 'not', pos: [150, 155], in: 11, out: 12},
    and0: {type: 'and', pos: [245, 60], in: [13, 14], out: 15},
    or0: {type: 'or', pos: [370, 100], in: [16, 17], out: 18},
    and1: {type: 'and', pos: [245, 145], in: [19, 20], out: 21},
  },
  wires: [[8, 3], [2, 6], [4, 7], [0, 9], [10, 13], [1, 14], [15, 16], [18, 5], [1, 11], [21, 17], [12, 20], [0, 19]]
}
</script>
</logic-editor>

</div>
