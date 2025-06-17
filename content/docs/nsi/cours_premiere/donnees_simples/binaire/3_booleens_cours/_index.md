---
title: Booléens - cours
author: qkzk
theme: metropolis
weight: 3
geometry: "margin=1.5cm"

---
Le terme *booléen* vient du nom du mathématicien britannique [George Boole](http://fr.wikipedia.org/wiki/George_Boole). Il est le créateur de la logique moderne qui s'appuie sur l'algèbre qui porte désormais son nom : l'*algèbre de Boole*. 

## Booléen

{{< hint info >}}
Un booléen est un type de variable à deux états : _vrai_ ou _faux_.

On note : `vrai = 1` et `faux = 0`.
{{< /hint >}}

{{< expand "" "..." >}}
En électronique, on emploie les booléens pour modéliser une situation à deux états possibles.

"Le courant passe" : 1, "le courant ne passe pas" : 0.

Cela peut aussi représenter une tension définie : +5V=1, -5V=0 ou +3V=1, -3V=0. etc.
{{< /expand >}}

### Python et les booléens

En Python, les booléens sont `True` et `False`, ils sont du type `bool`

```python
>>> True
True
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
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

### `casting`

En programmation, _caster_ signifie _changer le type d'une valeur_.

{{< expand "" "..." >}}
Par exemple : on peut caster des entiers vers les flottants :

```python 
>>> type(12)
<class 'int'>
>>> float(12)
12.0 
>>> type(12.0)
<class 'float'>
```
{{< /expand >}}

Python permet de caster à peu près n'importe quoi en booléen et les booléens en entiers :

```python 
>>> bool(12)
True
>>> bool(0)
False
>>> int(True)
1
>>> int(False)
0
>>>
```

{{< expand "" "..." >}}
Plus exotique 

```python 
>>> bool([]) # liste vide: faux 
False 
>>> bool([1, 2, 3]) # liste non vide: vrai 
True 
>>> bool("") # chaîne vide: faux 
False 
>>> bool("Super") # chaîne non vide: vrai
```

De manière générale, cela permet d'écrire des boucles comme ça :

```python 
tab = [5, 4, 3, 2, 1]
total = 0
while tab:
    x = tab.pop()
    total = total + x 
```

C'est un exemple peu utile (on pourrait faire `sum(tab)` ou utiliser une boucle `for`) mais vous rencontrerez peut-être cette construction.
{{< /expand >}}

### Fonction qui renvoie un booléen

On peut tout à fait renvoyer un booléen.

```python
def est_majeur(age: int) -> bool:
    """Vrai ssi l'age est d'au moins 18 ans"""
    return age >= 18
```

Et quand on l'exécute :

```python
>>> est_majeur(22)
True
```

Comment reconnaître un débutant ?

{{< expand "" "...">}}

Il écrit des trucs comme ça :

```python
def est_majeur(age):
    if age >= 18:
        return True
    else:
        return False
```
{{< /expand >}}

### Exercice 1 

Simplifier les fonctions suivantes :

{{< python title="Simplifier une fonction renvoyant un booléen" init="" >}}
def est_assez_grand(taille: int) -> bool:
    """La personne peut entrer si elle mesure au moins 130cm"""
    if taille < 130:
        return False
    else:
        return True

print(est_assez_grand(129))
print(est_assez_grand(131))

def contient_un_a(mot: str) -> bool:
    """Faux si la lettre 'a' ne figure pas dans le mot et vrai sinon"""
    if a not in mot:
        return False 
    else:
        return True

print(contient_un_a("elephant"))
print(contient_un_a("rhinoceros"))

def est_vide(tableau: list) -> bool:
    """Vrai si le tableau ne contient aucun élément"""
    if len(tableau) > 0:
        return False
    else:
        return True

print(est_vide([1, 2, 3]))
print(est_vide([]))
{{< /python >}}

Une fonction qui renvoie un booléen est appelé un _prédicat_.

--- 

## Opérations sur les booléens

_Comme pour les entiers, on peut opérer sur les booléens_.

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

### Table de vérité avec des bits

Les _tables de vérité_ sont abregées en notant :

- `1` pour `True`
- `0` pour `False`

| `a` | `not a` |
| --- | ------- |
| `1` | `0`     |
| `0` | `1`     |

### Opérateur binaire : le OU, noté `or`

**Il est vrai si l'un des deux booléens est vrai.**

```python
False or False   # False
False or True    # True
True  or False   # True
True  or True    # True
```

| `a` | `b` | `a or b` |
| --- | --- | :------: |
| 0   | 0   |    0     |
| 0   | 1   |    1     |
| 1   | 0   |    1     |
| 1   | 1   |    1     |

### Opérateur binaire : le ET, noté `and`

**Il est vrai si les deux booléens sont vrais.**

```python
False and False   # False
False and True    # False
True  and False   # False
True  and True    # True
```

| `a` | `b` | `a and b` |
| --- | --- | :-------: |
| 0   | 0   |     0     |
| 0   | 1   |     0     |
| 1   | 0   |     0     |
| 1   | 1   |     1     |

### Opérateur binaire : le XOR noté `^`

**Il est vrai si EXACTEMENT un des deux booléens est vrai**

```python
False ^ False   # False
False ^ True    # True
True  ^ False   # True
True  ^ True    # False
```

| `a` | `b` | `a XOR b` |
| --- | --- | :-------: |
| 0   | 0   | 0         |
| 0   | 1   | 1         |
| 1   | 0   | 1         |
| 1   | 1   | 0         |


## Expressions complexes avec des booléens 

Il est parfaitement possible de combiner plusieurs expressions booléennes pour former une expression complexe avec autant d'entrées que l'on veut.

### not not not not not...

Deux négations successives s'annulent.

_"Je ne suis pas en désaccord avec ce propos..."_ = _"Je suis d'accord avec ce propos"_.

En logique : `not (not a) = a`

| `a` | `not a` | `not (not a)` |
| --- | ---     | :-------:     |
| 0   | 1       | 0             |
| 1   | 0       | 1             |

{{< expand "" "..." >}}
Cela signifie aussi que : $a = \text{not }b \Longleftrightarrow \text{not } a = b$
{{< /expand >}}

### Exemple : simplifier une expression complexe 

Essayons de simplifier :

`not ((not a) and (not b))`

Mais comment ?

On construit une table de vérité étape par étape.

1. Combien de colonnes ? 

    - a
    - b  
    - not a 
    - not b 
    - (not a) and (not b)
    - une pour la sortie tout à droite 

    On va utiliser 6 colonnes. On peut faire moins mais il faut a minima 1 par entrée et 1 pour la sortie.

2. Combien de lignes ?

    Avec 2 entrées, il faut $2^2 = 4$ lignes. 

    Avec 7 entrées, il en faudrait $2^7 = 128$, difficile...

3. Par où commencer ? Énumérer les valeurs de a et b en partant de 00 jusque 11 comme si on comptait en binaire.
    Ainsi : 

    - c'est toujours rangé pareil,
    - c'est par ordre croissant,
    - on n'oublie aucun cas.


| a   | b   | not a   | not b   | (not a) and (not b)  | not ((not a) and (not b)) |
| --- | --- | ------- | ------- | -------------------- | ------------------------- |
|     |     | x       | y       | x and y              |                           |
| 0   | 0   | 1       | 1       | 1                    | 0                         |
| 0   | 1   | 1       | 0       | 0                    | 1                         |
| 1   | 0   | 0       | 1       | 0                    | 1                         |
| 1   | 1   | 0       | 0       | 0                    | 1                         |


Reconnait-on quelqu'un ?

{{< expand "" "..." >}}
Examinez les colonnes d'entrée `a`, `b` et la colonne de sortie `not((not a) and (not b))`

{{< /expand >}}

Oui ! C'est la table de `a or b` !

Donc, on a démontré que `not((not a) and (not b)) = a or b`.

On peut aussi dire :

### Première loi de Morgan :

`not (a or b) = (not a) and (not b)`

### Exercice 2

1. Construire une expression équivalente à `a and b` qui n'utilise que les opérateurs `not` et `or`.
2. Vérifier sa validité dans une table de vérité.

### Distributivité

On connait les règles de distributivité de la multiplication des nombres : `x(y + z) = xy + xz`.

Qu'en est-il des booléens ?

### Exercice 3 

1. Vérifier à l'aide d'une table de vérité que `a and (b or c) = (a and b) or (a and c)`
2. Donner l'expression développée de `a or (b and c)` et la vérifier dans une table.

### Lois de Morgan 

On a déjà rencontré la première loi de Morgan : `not (a or b) = (not a) and (not b)`

1. Échanger les opérateurs `or` et `and` dans l'égalité précédente.
2. Déplacer le `not` tout à gauche vers le membre de droite.
3. Vérifier cette égalité dans une table de vérité.
4. Énoncer la seconde loi de Morgan.

## Booléens et électronique : les portes logiques

On peut modéliser les opérations booléennes par des circuits électronique. C'est la base de l'informatique moderne.

### Non logique 

<script src="/js/logic_simulator.js"></script>
<div style="width: 600px; height: 400px">
<logic-editor id="editor1" showonly="in,out,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in6: {type: 'in', pos: [45, 40], id: 18},
    not0: {type: 'not', pos: [250, 40], in: 19, out: 20},
    out3: {type: 'out', pos: [460, 40], id: 21},
  },
  wires: [[18, 19], [20, 21]]
}
</script>
</logic-editor>
</div>

Cliquez sur le rond avec 0 ou 1 à gauche pour en changer l'état et voir le résultat.

### Ou logique 

<div style="width: 600px; height: 400px">
<logic-editor id="editor2" showonly="in,out,or">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in2: {type: 'in', pos: [45, 100], id: 0},
    in3: {type: 'in', pos: [45, 160], id: 1, val: 1},
    or0: {type: 'or', pos: [250, 130], in: [8, 9], out: 10},
    out1: {type: 'out', pos: [460, 130], id: 11},
  },
  wires: [[0, 8], [1, 9], [10, 11]]
}
</script>
</logic-editor>
</div>

### Et logique 

<div style="width: 600px; height: 400px">
<logic-editor id="editor3" showonly="in,out,and">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in2: {type: 'in', pos: [45, 100], id: 0},
    in3: {type: 'in', pos: [45, 160], id: 1, val: 1},
    or0: {type: 'and', pos: [250, 130], in: [8, 9], out: 10},
    out1: {type: 'out', pos: [460, 130], id: 11},
  },
  wires: [[0, 8], [1, 9], [10, 11]]
}
</script>
</logic-editor>
</div>

### XOR logique 



<div style="width: 600px; height: 400px">
<logic-editor id="editor3" showonly="in,out,xor">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in2: {type: 'in', pos: [45, 100], id: 0},
    in3: {type: 'in', pos: [45, 160], id: 1, val: 1},
    or0: {type: 'xor', pos: [250, 130], in: [8, 9], out: 10},
    out1: {type: 'out', pos: [460, 130], id: 11},
  },
  wires: [[0, 8], [1, 9], [10, 11]]
}
</script>
</logic-editor>
</div>

### Exercice 4 

1. Constuire un circuit qui prend `a` en entrée, un bit valant 0 ou 1 et qui renvoie _toujours_ 1.

<div style="width: 600px; height: 400px">
<logic-editor id="editor6" showonly="in,out,not,or,and,xor">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in2: {type: 'in', pos: [45, 200], id: 0, name: 'a'},
    out1: {type: 'out', pos: [460, 200], id: 1, name: 'out'},
  },
  wires: []
}
</script>
</logic-editor>
</div>

2. Modifier votre circuit pour qu'il renvoie _toujours 0_.
3. Traduire vos deux circuits en expressions logiques.

### Exercice 5 

On a illustré certaines des expressions de [l'exercice 3](#exercice-3).

1. Reconnaître les règles et expressions déjà rencontrées 
2. Tester tous les cas en changeant les valeurs des entrées et vérifier la validité

<div style="width: 600px; height: 600px">
<logic-editor id="editor4" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in7: {type: 'in', pos: [50, 55], id: 22, val: 1},
    in8: {type: 'in', pos: [50, 140], id: 23, val: 1},
    in9: {type: 'in', pos: [50, 230], id: 24},
    or1: {type: 'or', pos: [230, 100], in: [25, 26], out: 27},
    and1: {type: 'and', pos: [340, 55], in: [28, 29], out: 30},
    out4: {type: 'out', pos: [465, 55], id: 31},
    and2: {type: 'and', pos: [230, 185], in: [32, 33], out: 34},
    and3: {type: 'and', pos: [230, 260], in: [35, 36], out: 37},
    or2: {type: 'or', pos: [350, 220], in: [38, 39], out: 40},
    out5: {type: 'out', pos: [470, 220], id: 41},
    or3: {type: 'or', pos: [225, 365], in: [42, 43], out: 44},
    not1: {type: 'not', pos: [350, 365], in: 45, out: 46},
    in10: {type: 'in', pos: [50, 355], id: 47},
    in11: {type: 'in', pos: [55, 530], id: 48},
    out6: {type: 'out', pos: [470, 365], id: 49},
    not2: {type: 'not', pos: [225, 460], in: 50, out: 51},
    not3: {type: 'not', pos: [225, 525], in: 52, out: 53},
    and4: {type: 'and', pos: [350, 490], in: [54, 55], out: 56},
    out7: {type: 'out', pos: [470, 490], id: 57},
  },
  wires: [[23, 25], [24, 26], [22, 28], [27, 29], [30, 31], [40, 41], [34, 38], [37, 39], [22, 32], [22, 35], [23, 33], [24, 36], [47, 42], [48, 43], [44, 45], [46, 49], [56, 57], [51, 54], [53, 55], [47, 50], [48, 52]]
}
</script>
</logic-editor>
</div>


### Exercice 6

1. Construire les schéma electroniques illustrant les deux autres règles 
2. Vérifier que vos circuits sont valides



<div style="width: 600px; height: 600px">
<logic-editor id="editor4" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
  },
  wires: []
}
</script>
</logic-editor>
</div>

### Exercice 7 : Demi additionneur

1. Rappeler les tables de `XOR` et `AND`

Lorsqu'on additionne deux bits, on obtient un nombre pouvant occuper 2 bits.
Par exemple : `1 + 0 = 1` (un bit) et `1 + 1 = 2 = 0b10` (deux bits).

2. En notant `s` la somme (le dernier bit) et `r` la retenue (le bit de gauche), construire dans une seule table la table de `s` et de `r`

3. Comparer avec les tables de `a xor b` et `a and b`

4. Dans le circuit ci-dessous, connecter `a` et `b` à `a and b` et à `a xor b`

5. Vérifier la table de vérité écrite plus haut.

<div style="width: 600px; height: 600px">
<logic-editor id="editor7" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [55, 105], id: 0, name: 'a'},
    in1: {type: 'in', pos: [55, 205], id: 1, name: 'b'},
    and0: {type: 'and', pos: [250, 200], in: [2, 3], out: 4},
    xor0: {type: 'xor', pos: [250, 110], in: [8, 9], out: 10},
    out0: {type: 'out', pos: [405, 110], id: 11, name: 's'},
    out1: {type: 'out', pos: [405, 200], id: 12, name: 'r'},
  }
}
</script>
</logic-editor>
</div>

### Additionneur complet

Un additionneur complet contient trois entrées : `a`, `b` et `c0` et a 2 sorties `s` et `c1`.

- `a` et `b` sont les bits des nombres qu'on ajoute et `c0` est la retenue du calcul précédent.
- `s` est le bit de la somme à cette position et `c1` est la retenue qui part dans la somme suivante.
- Cette retenue `c1` est calculée en faisant un `or` entre `a and b` et `c0 and (a xor b)` : `c1 = (a and b) or (c0 and (a xor b))`.

<div style="width: 600px; height: 400px">
<logic-editor id="editor5" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    in4: {type: 'in', pos: [55, 185], id: 10, name: 'a'},
    in5: {type: 'in', pos: [55, 225], id: 11, name: 'b', val: 1},
    in0: {type: 'in', pos: [55, 145], id: 0, name: 'c0'},
    xor1: {type: 'xor', pos: [185, 205], in: [18, 19], out: 20},
    and1: {type: 'and', pos: [180, 260], in: [21, 22], out: 23},
    or0: {type: 'or', pos: [405, 240], in: [40, 41], out: 42},
    and4: {type: 'and', pos: [315, 200], in: [43, 44], out: 45},
    xor4: {type: 'xor', pos: [315, 150], in: [46, 47], out: 48},
    out2: {type: 'out', pos: [490, 180], id: 16, name: 's'},
    out0: {type: 'out', pos: [490, 240], id: 1, name: 'c1'},
  },
  wires: [[11, 19], [10, 18], [11, 22], [10, 21], [20, 47], [48, 16], [45, 40], [23, 41], [20, 44], [0, 46], [42, 1], [0, 43]]
}
</script>
</logic-editor>
</div>


### Additionneur 4 bits

Comment réaliser l'addition de nombres à plusieurs bits ? La méthode ci-dessous, appelée "_propagation des retenues_" est simple, fastidieuse et peu efficace. Il existe une méthode beaucoup plus rapide que nous n'aborderons pas.

Un additionneur complet sur 4 bits est obtenu en raccordant successivement :

un demi additionneur pour les bits de poids faibles à trois additionneurs complets pour les bits suivant. Le bit de poids fort de la somme est la dernière retenue.


En notant `a = a3 a2 a1 a0` les bits de `a` et de la même manière les bits de `b` et `s = a + b`, on peut dessiner le circuit plus bas.

Utilisation : 

- Les bits d'entrée sont à gauche et se lisent de haut en bas, le bit de poids faible est en haut.
- Les bits de sortie sont à droite et se lisent aussi de haut en bas.

- colonne tout à gauche : les bits de `a`. On peut lire `a = 0b1101 = 13`
- colonne juste à droite : les bits de `b`. On lit `b = 0b1001 = 9`

| a      | a3 | a2 | a1 | a0 |
|--------|----|----|----|----|
| valeur | 1  | 1  | 0  | 1  |

| b      | b3 | b2 | b1 | b0 |
|--------|----|----|----|----|
| valeur | 1  | 0  | 0  | 1  |

Donc la somme :

```
  a     1 1 0 1
+ b     1 0 0 1
----------------
= s   1 0 1 1 0
```

$13 + 9 = 22 = 16 + 4 + 2 = 0b10110$

- colonne de droite, les bits de `s=a+b`. On lit de haut en bas : `s = 0b11000`. C'est correct.

| s = a+b | s4 | s3 | s2 | s1 | s0 |
|---------|----|----|----|----|----|
| valeur  | 1  | 1  | 0  | 0  | 0  |

Changez les bits d'entrée et vérifiez quelques valeurs.


<div style="width: 600px; height: 1000px">
<logic-editor id="editor5" showonly="in,out,and,or,xor,not">
<script type="application/json">
{ // JSON5
  v: 6,
  components: {
    and0: {type: 'and', pos: [175, 95], in: [0, 1], out: 2},
    xor0: {type: 'xor', pos: [180, 40], in: [3, 4], out: 5},
    in0: {type: 'in', pos: [50, 350], id: 6, name: 'a2', val: 1},
    in1: {type: 'in', pos: [50, 560], id: 7, name: 'a3', val: 1},
    in2: {type: 'in', pos: [80, 410], id: 8, name: 'b2'},
    in3: {type: 'in', pos: [90, 610], id: 9, name: 'b3', val: 1},
    in4: {type: 'in', pos: [45, 195], id: 10, name: 'a1'},
    in5: {type: 'in', pos: [70, 245], id: 11, name: 'b1'},
    in6: {type: 'in', pos: [70, 120], id: 12, name: 'b0', val: 1},
    in7: {type: 'in', pos: [45, 50], id: 13, name: 'a0', val: 1},
    out0: {type: 'out', pos: [495, 370], id: 14, name: 's2'},
    out1: {type: 'out', pos: [490, 550], id: 15, name: 's3'},
    out2: {type: 'out', pos: [490, 180], id: 16, name: 's1'},
    out3: {type: 'out', pos: [490, 35], id: 17, name: 's0'},
    xor1: {type: 'xor', pos: [190, 195], in: [18, 19], out: 20},
    and1: {type: 'and', pos: [185, 250], in: [21, 22], out: 23},
    and2: {type: 'and', pos: [195, 420], in: [24, 25], out: 26},
    and6: {type: 'and', pos: [200, 620], in: [30, 31], out: 32},
    xor2: {type: 'xor', pos: [200, 370], in: [33, 34], out: 35},
    xor6: {type: 'xor', pos: [200, 565], in: [36, 37], out: 38},
    out4: {type: 'out', pos: [500, 655], id: 39, name: 's4'},
    or0: {type: 'or', pos: [435, 240], in: [40, 41], out: 42},
    and4: {type: 'and', pos: [330, 215], in: [43, 44], out: 45},
    xor4: {type: 'xor', pos: [335, 150], in: [46, 47], out: 48},
    xor5: {type: 'xor', pos: [340, 340], in: [49, 50], out: 51},
    and5: {type: 'and', pos: [340, 410], in: [52, 53], out: 54},
    or1: {type: 'or', pos: [440, 465], in: [55, 56], out: 57},
    xor3: {type: 'xor', pos: [345, 545], in: [67, 68], out: 69},
    or2: {type: 'or', pos: [430, 655], in: [76, 77], out: 78},
    and3: {type: 'and', pos: [350, 615], in: [27, 28], out: 29},
  },
  wires: [[13, 4], [5, 17], [13, 1], [11, 19], [10, 18], [11, 22], [10, 21], [20, 47], [2, 46], [2, 43], [48, 16], [45, 40], [23, 41], [6, 33], [8, 34], [8, 25], [6, 24], [35, 50], [54, 55], [26, 56], [51, 14], [42, 49], [42, 52, {via: [[395, 365, 'w']]}], [7, 36], [7, 30], [9, 37], [9, 31], [38, 68], [57, 67, {via: [[370, 510, 'w']]}], [69, 15], [78, 39], [32, 77], [35, 53], [12, 3], [12, 0], [20, 44], [38, 28], [57, 27, {via: [[395, 575, 'w'], [310, 580, 'w']]}], [29, 76]]
}
</script>
</logic-editor>
</div>

Vous pouvez vérifier [ici](https://logic.modulo-info.ch/?id=OH5655&mode=full&data=N4NwXAbANAxg9gWwA5wHYFNUBcDOZgCGqAJgAz5YCeS6YA5EcXVCngNoDsATAKxQCMADlIBdKAEtUYNqQFi4AVyxguAXygAPOACdywKjXpbtzVtI4BmWf15jJ0i1AAs8pWB7rJeg7TqTTcOwQpLJOFjx2xJBQqAQIvgRczCAEADZg-J6o-BTUvv4sgdLBshBOERJRHDFxCRbJaRlZXLmGfqgBQSFQPCGRYII18fQARklQKemZEqgWrfkdhUFOpQCcFeJRq0O+I-VZTvP0BWZsPOtQXML9-LKxwwz8DVNZPEftncVcshZWN-w7UZPCaNaaSCDvE5FNgQb6XUgbKI2QF0EakOhZDiQxanCD8Pj8P6VDKOe4JdHqRRYbx5ehUz5sW7lZw8REZJwonBJSlKHL6Wl0elLaRM0rhG58Mn0HD7KBUlr8tpC06iy4QNn8aBSug4J48rBzRW+ZXQ1U2UTE-jVbU4CmaHR8nxGHQMjgrS7XGYiwb8VauZTfdSMR0Cxiu8JQX4bKRsLgArhcf0qCxBkgKp0MEiu5m9aPSLgc2xytxcCCp4gQo30MPCzi9KAcBF2GNWSP8JMWNT27TpgXGV318p5ti-SMuYvKcLqYyVjP92scevqi32EfQCwcDuCfWHKuCpQMpl8DiN-oWbY2pwYuW6d4u2urQR8TvD91OdsTsBOLuMXcZmunIIwiRn0XpsGEzjjlSX4eN2f59vegFPpc4pgU40BOJun5ONu3ZvHu86AasoRFquTjbL0SY8NMjD4f+Wa1oIxHOOszbSDwXA9BYVFOJS2ghkqJgPsxrIrjGrI9BAVEcNOOiGnOiHQkxfAQESq4QNUECCEmECrHxvaCQyqzqg2txsZw0AnkmHC4QQxDEOgt57nZDnaAAtAQ2jaAQlCHkIPzEeZdDcG5i7MMFqxuYI9RJnQghOFFgjXlSdECia7CEsy-D4v0TH6rOaUHrWhKtrwbLEfqWJ7ulIoviyK5bNMVKCHeRUqnVqnlV2VKrK1WCHnVJ7lSmUCMPJoYMYBi5QFpw6rByrGfsZqjqAA7uI2joOwjKOOOZwCFhO1yFAjIAr6YiMtY2kndllyJjdshxhdcKYc9zhSSdnFhBdOECB94F8Csz27R+MKRtxJ2DBYe2DEWYMFhdEaUSdPAcqyz3QDw-3UQIe3fixP2cRxF3VBY-2kxabDbBuF3U6DFiDFpF08Jph26QIFScFDfonZ2DaHUjEOMpxQvIpTL17YSDacaA4gENIML1sxdCrXQP2NgIvBQCrasnZhj2c9l9a2CIqgXciHDbLL8tsGc+KRtNOq63bx4XE75ukMhluG57gNmabHsNo41sK+RfAFnwdAdD9FzI6dSOU9lEa-LI7sBzdALASHtth84Wvu3rzGCHCBenQiUDF4ntyA386dg26UDZ2crZk5H0co62i7m+aDZV3C4Spzgat14MggAk36GlCXQ8-cEFflN3WvxX3gP1lHw9myd1TTU3qN8Czqft2c9a3IfzvZeXp-d+XG6DxvtMVzLIBy6HncSaXYSyIIp4Z-WgjqiIEeHImIXWQoFSG0BVig2-lAVY902BAVgULFmsC9oM1gZzYyDYpKmyAA) que les branchements sont corrects.


## Propriétés mathématiques de l'algèbre de Boole

On peut résumer ainsi ce qu'on a vu sur les booléens :

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

### Lois de Morgan 

- `not (a and b) = (not a) or  (not b)`
- `not (a or  c) = (not a) and (not b)`
