---
title: "Résumé court"
author: qkzk
theme: metropolis
geometry: margin=1.5cm
weight: 10000
header-includes: |
    \usepackage{tcolorbox}
    \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
    \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}

---

## Type constuits

Un type _construit_ est une collection d'objets. Python en propose trois : `list`, `tuple` et `dict`.

## Structures linéaires (éléments numérotés) : `list` et `tuple`

Une structure linéaire est composée d'un nombre fini _d'éléments numérotés_, accessibles par leur _indice_.

#### Mutabilité 

> Une structure de de donnée est mutable si elle peut évoluer.
> Concernant les types construits cela signifie qu'on peut ajouter, modifier
> ou supprimer des éléments de la structure

{{< columns >}}


### `tuple` : collection indexée non mutable

Les `tuple` sont des collections numérotées non mutables. Une fois crées, on ne peut changer leur contenu.

```python
>>> mon_tuple = (1, 2, 3)
>>> len(mon_tuple)
3
>>> mon_tuple[0]
1
>>> mon_tuple[-1] ## depuis la fin
3
>>> for elt in mon_tuple:
...     elt
1
2
3
>>> 3 in mon_tuple
True
>>> 4 in mon_tuple
False
>>> a, b, c = mon_tuple
>>> a
1
>>> c
3
```

Les `str` (chaînes de caractères) se comportent comme des `tuple`... de caractères.
<--->




### `list` : collection indexée mutable


Les `list` se manipulent comme des tuples _mutables_. Plus pratiques mais plus lentes que les `tuple`.

```python
>>> ma_liste = [1, 2, 3]
>>> len(ma_liste)
3
>>> ma_liste[0]
1
>>> ma_liste[-1] ## depuis la fin
3
>>> for elt in ma_liste:
...     elt
1
2
3
>>> 3 in ma_liste
True
>>> 4 in ma_liste
False
>>> a, b, c = ma_liste
>>> a
1
>>> c
3
```

{{< /columns >}}

### Mutabilité des `list`

```python
>>> ma_liste.append(4)
>>> ma_liste
[1, 2, 3, 4]
>>> del ma_liste[0]
>>> ma_liste
[2, 3, 4]
>>> ma_liste.pop()
4
>>> ma_liste
[2, 3]
```


## Dictionnaires : `cle` $\longrightarrow$ `valeur`

{{< columns >}}



Un `dict` associe des _clés_ à des _valeurs_. Pas d'indice mais mutables.


```python
>>> mon_dict = {'a': 1, 'b': 2}
>>> mon_dict['a']
1
>>> len(mon_dict)
2
>>> 'c' in mon_dict
False
>>> mon_dict['c'] = 3
>>> mon_dict
{'a': 1, 'b': 2, 'c': 3}
>>> del mon_dict['a']
>>> mon_dict
{'b': 2, 'c': 3}
```

<--->
### Trois manières d'itérer sur les `dict`\

```python
>>> for cle in mon_dict.keys():
... cle
'b'
'c'
>>> for valeur in mon_dict.values():
... valeur
2
3

>>> for cle, valeur in mon_dict.items():
... cle, valeur
'a', 2
'b', 3
```

{{< /columns >}}

## Types construits en Python : `list`, `tuple` et `dict`

Python utilise de nombreux types construits. Dans l'usage courant nous
rencontrons un des trois types cités ci-dessus


| Type              | `list`           | `tuple`         | `dict`              |
|-------------------|------------------|-----------------|---------------------|
| créer directement | `l=[1, 2, 3]`    | `t=(1, 2, 3)`   | `d={'a':1, 'b': 2}` |
| accéder           | `l[2] # 1`       | `t[2] ## 1`     | `d['a'] # 1`        |
| contient ?        | `2 in l  # True` | `2 in t # True` | `'a' in d  # True`  |
| mutable ?         | oui              | non             | oui                 |
| ajouter un élt.   | `l.append(4)`    | impossible      | `d['c'] = 3`        |
| supprimer un elt. | `del l[1]`       | impossible      | `del d['a']`        |

### Comment choisir ?

Le plus souvent : `list`

- regrouper des éléments de même nature : `tuple` ou `list` (si on doit les faire évoluer)
- associer un nom à des objets : `dict`
- savoir si un objet est dans une collection : `dict` (le plus rapide)
- itérer rapidement : `tuple`

