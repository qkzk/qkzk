---
author: qu3nt1n
date: 2019-05-05 06:34:34+00:00
draft: false
title: Python 3 - 03 Les boucles
weight: 3

---

# Chapitre 3 - Les boucles


Une boucle permet d'exécuter une portion de code plusieurs fois de suite.


# L'instruction `while`


![python_while](/uploads/uploads/2017/04/python_while.png)





## Syntaxe



```python
while expression:           # ne pas oublier le signe de ponctuation ':'
    bloc d instructions     # attention à l'indentation
# suite du programme
```

Si l'expression est vraie (`True`) le bloc d'instructions est exécuté, puis
l'expression est à nouveau évaluée.\
Le cycle continue jusqu'à ce que l'expression soit fausse (`False`).\
On passe alors à la suite du programme.


## Exemple : un script qui compte de 1 à 4



```python
# script Boucle1.py

# initialisation de la variable de comptage
compteur = 1
while compteur < 5:
    # ce bloc est exécuté tant que la condition (compteur < 5) est vraie
    print(compteur, compteur < 5)
    compteur += 1    # incrémentation du compteur, compteur = compteur + 1
print(compteur < 5)
print("Fin de la boucle")
```



    >>>
    1 True
    2 True
    3 True
    4 True
    False
    Fin de la boucle




## Table de multiplication par 8



```python
# script Boucle2.py

compteur = 1	# initialisation de la variable de comptage
while compteur <= 10:
    # ce bloc est exécuté tant que la condition (compteur <= 10) est vraie
    print(compteur, '* 8 =', compteur*8)
    compteur += 1    # incrémentation du compteur, compteur = compteur + 1
print("Et voilà !")
```



    >>>
    1 * 8 = 8
    2 * 8 = 16
    3 * 8 = 24
    4 * 8 = 32
    5 * 8 = 40
    6 * 8 = 48
    7 * 8 = 56
    8 * 8 = 64
    9 * 8 = 72
    10 * 8 = 80
    Et voilà !




## Affichage de l'heure courante



```python
# script Boucle3.py

import time     # importation du module time
quitter = 'n'   # initialisation
while quitter != 'o':
    # ce bloc est exécuté tant que la condition est vraie
    # strftime() est une fonction du module time
    print('Heure courante ', time.strftime('%H:%M:%S'))
    quitter = input("Voulez-vous quitter le programme (o/n) ? ")
print("A bientôt")
```



    >>>
    Heure courante  09:48:54
    Voulez-vous quitter le programme (o/n) ? n
    Heure courante  09:48:58
    Voulez-vous quitter le programme (o/n) ? o
    A bientôt

## Boucle infinie

Il arrive (accidentellement ou intentionnellement) qu'on entre dans une 
boucle _infinie_.

Sauriez-vous expliquer pourquoi cette boucle ne s'arrête pas ?

```python
n = 0
while n < 100:
    print(n)
```

Lorsqu'on exécute un script directement, on peut toujours l'arrêter
avec le raccourci clavier `CTRL + C`

Dans colab il peut cliquer sur le bouton carré "arrêter".





# L'instruction `for`




## Syntaxe


```python
for élément in séquence :
    bloc d instructions
# suite du programme
```




Les éléments de la séquence sont issus d'une chaîne de caractères ou bien d'une liste.


## Exemple avec une séquence de caractères



```python
# script Boucle4.py

chaine = 'Bonsoir'
for lettre in chaine:		# lettre est la variable d'itération
    print(lettre)
print("Fin de la boucle")
```

La variable `lettre` est initialisée avec le premier élément de la séquence (`'B'`).
Le bloc d'instructions est alors exécuté.
Puis la variable `lettre` est mise à jour avec le second élément de la
séquence (`'o'`) et le bloc d'instructions à nouveau exécuté...
Le bloc d'instructions est exécuté une dernière fois lorsqu'on arrive au
dernier élément de la séquence (`'r'`) :


    >>>
    B
    o
    n
    s
    o
    i
    r
    Fin de la boucle




## Exemple avec les éléments d'une liste



```python
# script Boucle5.py

maliste = ['Pierre', 67.5, 18]
for element in maliste:
    print(element)
print("Fin de la boucle")
```

Là, on affiche dans l'ordre les éléments de la liste :

```python
>>>
Pierre
67.5
18
Fin de la boucle
```



## Fonction `range()`


L'association avec la fonction `range()` est très utile pour créer des
séquences automatiques de nombres entiers :

```python
# script Boucle6.py
print(list(range(1, 5)))

for i in range(1, 5):
    print(i)
print("Fin de la boucle")
```



    >>>
    [1, 2, 3, 4]
    1
    2
    3
    4
    Fin de la boucle

### Syntaxe de `range()`

`range` avec 1 paramètre :

```python
range(fin)
```

*  entiers de 0 à `fin - 1`\
    `range(10)` comporte toujours 10 entiers...

`range` avec deux paramètres :

```python
range(debut, fin)
```

*    entiers depuis `debut` inclus jusque `b` exclu.\
    `range(4, 8)` : 4, 5, 6, 7

`range` avec trois paramètres :

```python
range(debut, fin, pas)
```

*    entiers depuis `debut` jusque `fin` (exclu) séparés de `pas`\
    `range(3, 11, 2)` : 3, 5, 7, 9

### Table de multiplication


La création d'une table de multiplication paraît plus simple avec une boucle `for` qu'avec une boucle `while` :

```python
# script Boucle7.py

for compteur in range(11):
    print(compteur, '* 9 =', compteur * 9)
print("Et voilà !")
```



    >>>
    0 * 9 = 0
    1 * 9 = 9
    2 * 9 = 18
    3 * 9 = 27
    4 * 9 = 36
    5 * 9 = 45
    6 * 9 = 54
    7 * 9 = 63
    8 * 9 = 72
    9 * 9 = 81
    10 * 9 = 90
    Et voilà !




## L'instruction `break`


L'instruction `break` provoque une sortie immédiate d'une boucle `while` ou
d'une boucle `for`.

Dans l'exemple suivant, l'expression `True` est toujours ... vraie : on a
une boucle sans fin.

L'instruction `break` est donc le seul moyen de sortir de la boucle.


#### Affichage de l'heure courante



```python
# script Boucle8.py

import time     # importation du module time
while True:
    # strftime() est une fonction du module time
    print('Heure courante ', time.strftime('%H:%M:%S'))
    quitter = input('Voulez-vous quitter le programme (o/n) ? ')
    if quitter == 'o':
        break
print("A bientôt")
```



    >>>
    Heure courante  14:25:12
    Voulez-vous quitter le programme (o/n) ? n
    Heure courante  14:25:20
    Voulez-vous quitter le programme (o/n) ? o
    A bientôt




## Astuce


Si vous connaissez le nombre de boucles à effectuer, utiliser une boucle `for`.
Autrement, utiliser une boucle `while`.


## Exercices


### Exercice 3.1 ★

Écrire un script qui affiche toutes les tables de multiplication (de 1 à 10).

### Exercice 3.2 ★

Écrire un script qui calcule la moyenne d'une série de notes depuis une liste.

Par exemple :
 
```python
notes = [5, 7, 9, 11]
```

Qui affiche :

```
moyenne : 8
```

### Exercice 3.3 ★

1. Avec une boucle `for`, écrire un script qui compte le nombre de lettres z
dans une chaîne de caractères.

    Par exemple :

    ```
    >>>
    Entrer la chaîne : Zinedine Zidane
    Résultat : 2
    ```

2. Faire la même chose, directement avec la méthode `count()` de la classe `str`.
Pour obtenir de l'aide sur cette méthode :

    ```python
    >>> help(str.count)
    ```

### Exercice 3.4 ★

Avec une boucle `while`, écrire un script qui affiche l'heure courante avec
une actualisation chaque seconde.

On utilisera la fonction `sleep()` du module `time`.

Pour obtenir de l'aide sur cette fonction :

```python
>>> import time
>>> help(time.sleep)
```

Par exemple :

```
>>> # Taper CTRL + C pour arrêter le programme.
>>>
Heure courante  12:40:59
Heure courante  12:41:00
Heure courante  12:41:01
Heure courante  12:41:02
KeyboardInterrupt
>>>
```

Remarque : forcer l'arrêt d'un programme avec CTRL + C est une mauvaise
pratique.
Nous verrons comment interrompre proprement un programme dans le chapitre
[Gestion des exceptions](/docs/nsi/cours-python/python-3-05-gestion-des-exceptions/).


### Exercice 3.5 ★

1. Écrire le script du jeu du plus ou moins suivant :

```
>>>
Le jeu consiste à deviner un nombre entre 1 et 100 :

--->   50
trop petit !
--->   75
trop petit !
--->   87
trop grand !
--->   81
trop petit !
--->   84
trop petit !
--->   85
Gagné en 6 coups !
```


Remarque : pour créer un nombre entier aléatoire entre 1 et 100 :

```python
import random
nombre = random.randint(1, 100)
```

2. Quelle est la stratégie la plus efficace ?

3. Question bonus : Montrer que l'on peut deviner un nombre en 7 coups maximum.

Bibliographie : [La dichotomie](http://fr.wikipedia.org/wiki/Dichotomie)

Remarque : l'algorithme de Dichotomie est au programme de première NSI.

### Exercice 3.6 - Robert le rentier

Robert a placé 1000 € à la banque. Voici comment les opérations qui sont
réalisées sur son compte :

1. Chaque année les intérêts s'élèvent à 2% du capital durant l'année précédente.
    Ils sont ajoutés automatiquement à son capital.
3. Chaque année, Robert ajoute 200 € à son capital.

Exemple : 

| Date       | Capital | Remarque                |
|------------|---------|-------------------------|
| 2019/01/01 | 1000    | investissement initial  |
| 2020/01/01 | 1220    | 1000 + 2% de 1000 + 200 |
| 2021/01/01 | 1444.4  | 1220 + 2% de 1220 + 200 |

1. Écrire une boucle qui calcule le capital de Robert à l'issue des 10
    prochaines années.
2. Robert prendra sa retraite quand il aura 120 000 € de côté. Combien d'années
    devra-t-il encore travailler ?

### Exercice 3.7 - Geralt kiffe ses cheveux.

![](https://s-media-cache-ak0.pinimg.com/736x/9c/04/96/9c0496717e938a311f4ed1286fc11f4f.jpg)


Pour ne pas être dérangé dans ses aventures il décide de les couper chaque fois qu'ils font plus de 40 cm. Ce matin Geralt a coupé ses cheveux et ils mesurent 17 cm. Chaque jour la longueur de ses cheveux augmente d'un pour cent (leur longueur est multipliée par 1.01).

Écrire un script qui affiche dans combien de jours Geralt devra couper ses cheveux.

**Les exercices suivants sont nécessitent quelques aptitudes en mathématiques...**

### Exercice 3.8 ★★

Écrire un script qui donne l'évolution de la suite convergente :

$u_{n+1} = \dfrac{u_n}{2} + \dfrac{1}{u_n}$

Par exemple :


    >>>
    Valeur initiale ? 20
    Jusqu'à quel rang ? 10
    0 20.0
    1 10.05
    2 5.12450248756
    3 2.75739213842
    4 1.74135758045
    5 1.44494338196
    6 1.41454033013
    7 1.41421360012
    8 1.41421356237
    9 1.41421356237
    10 1.41421356237
    >>>

---

### Exercice 3.9 ★★ - Code de César

En cryptographie, le code de César est une technique de chiffrement
élémentaire qui consiste à décaler une lettre de 3 rangs vers la droite :

```
A → D

B → E

...

Z → C
```


1. Ecrire le script de ce codage.
Par exemple :

```
>>> Message à coder ? abcdefghijklmnopqrstuvwxyz
defghijklmnopqrstuvwxyzabc

>>> Message à coder ? Monty Python's Flying Circus
prqwb sbwkrq'v ioblqj flufxv
```

On pourra utiliser la chaîne `'abcdefghijklmnopqrstuvwxyz'` et la méthode
`find()` de la classe `str`.
Pour obtenir de l'aide sur cette méthode :

```
>>> help(str.find)
```

2. Ecrire le script du décodage.
Par exemple :

```
>>> Message à décoder ? prqwb sbwkrq'v ioblqj flufxv
monty python's flying circus
```



### Exercice 3.11 ★★ - Fraction continue infinie

Estimer la valeur numérique de la fraction continue suivante :

![formule_fraction_continue](/uploads/uploads/2017/04/formule_fraction_continue.png)




Comparer avec la valeur exacte : $\dfrac{1 + \sqrt{5}}{2}$

### Exercice 3.12

1. ★ Ecrire un script qui détermine si un nombre entier est premier ou pas.

2. **Rappel :** un nombre **premier** est un entier naturel qui n'a que deux diviseurs : 1 et lui même.
    Ex : 3 est premier mais 6 ne l'est pas car 2*3=6.
    Par exemple :

    ```
    >>>
    Nombre ? 17
    17 est un nombre premier
    ```

3. ★★★ Ecrire un script qui décompose un nombre entier en un produit de facteurs premiers.

    ```
    >>>
    Nombre à décomposer ? 2142
    2142 = 2 * 3 * 3 * 7 * 17
    ```



### QCM


[QCM sur les boucles](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_loop)



Source : [Fabrice Sincère](http://fsincere.free.fr/isn/python/cours_python_ch3.php) - [Contenu sous licence CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/fr/)
