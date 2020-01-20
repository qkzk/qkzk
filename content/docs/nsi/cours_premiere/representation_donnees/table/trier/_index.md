---
title: 'Tri dans une table'
author: 'qkzk'
date: '2019/12/22'
weight: 3
---

# 3. Trier une table selon une colonne

Heureusement, le programme est réaliste, on n'a pas besoin de créer les tris
nous mêmes.

_Une fonction de tri intégrée au système ou à une bibliothèque peut être utilisée_

Ouf !

## Trier selon un critère

### Critère de comparaison

Souvenons nous...

On peut trier les chaînes de caractères selon différents critères :

* ordre lexicographique : `['aaaa', 'bbb']`
* longueur : `['bbb', 'aaaa']`

Par exemple :

~~~python
>>> sorted(['aaaa', 'bbb']) # ordre lexicographique par défaut
['aaaa', 'bbb']
>>> sorted(['aaaa', 'bbb'], key=len) # longueur
['bbb', 'aaaa']
~~~

### Trier selon un critère arbitraire

On suppose avoir `liste_csv` qui comporte des enregistrements de la forme

~~~python
{'nom': 'Dupont', 'prenom': 'Robert', 'moyenne': '2.3'} # nul Robert, nul
~~~

attention, la moyenne n'est pas encore considérée comme un **nombre**, c'est
une chaîne de caractères !

~~~ python
>>> '2.3' > '18'
True
~~~

Comment trier les élèves selon leur moyenne (toujours pour coller, c'est ma
passion) ?

**Extrait de la [documentation](https://docs.python.org/fr/3.7/howto/sorting.html) :**

_Par exemple, voici une comparaison de texte insensible à la casse:_

~~~python
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
~~~

_La valeur du paramètre `key` devrait être une fonction qui prend un seul argument et renvoie une clef à utiliser à des fins de tri. Cette technique est rapide car la fonction clef est appelée exactement une seule fois pour chaque enregistrement en entrée._

_Un usage fréquent est de faire un tri sur des objets complexes en utilisant les indices des objets en tant que clef. Par exemple :_

~~~python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
~~~

On peut adapter à un dictionnaire sans problème :

~~~python
>>> dict_lyceens = [
...     {'prenom': 'jean', 'nom': 'dupont', 'moyenne': 15},
...     {'prenom': 'jak', 'nom': 'kage', 'moyenne': 12},
...     {'prenom': 'robert', 'nom': 'duchmol', 'moyenne': 10},
... ]
>>> sorted(dict_lyceens, key=lambda lyceen: lyceen["moyenne"])   # tri par moyenne
[{'prenom': 'robert', 'nom': 'duchmol', 'moyenne': 10},
{'prenom': 'jak', 'nom': 'kage', 'moyenne': 12},
{'prenom': 'jean', 'nom': 'dupont', 'moyenne': 15}]
~~~


### Rappel : fonction lambda

Une fonction lambda est une fonction `anonyme`

On la note ainsi : `lambda: entree: sortie`

Dans l'exemple ci-dessus, la fonction prend en entrée un `lyceen` et renvoie
sa moyenne : `lyceen['moyenne']`

Elle est équivalente à :

~~~python
def moyenne(lyceen):
  return lyceen["moyenne"]
~~~

On utilise une fonction lambda quand on ne se sert qu'une fois (par ligne).
