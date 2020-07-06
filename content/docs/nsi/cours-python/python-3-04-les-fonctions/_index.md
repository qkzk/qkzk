---
author: qu3nt1n
date: 2019-05-05 06:41:30+00:00
draft: false
title: Python 3 - 04 Les fonctions
weight: 4

---

Nous avons déjà vu beaucoup de fonctions : `print(), type(), len(), input(), range()`...
Ce sont des fonctions pré-définies ([built-in functions](http://docs.python.org/3/library/functions.html)).
Nous avons aussi la possibilité de créer nos propres fonctions.


## Intérêt des fonctions


Une fonction est une portion de code que l'on peut appeler au besoin (c'est une sorte de sous-programme).

L'utilisation des fonctions évite des redondances dans le code : on obtient ainsi des programmes plus courts et plus lisibles.

Par exemple, nous avons besoin de convertir à plusieurs reprises des degrés Celsius en degrés Fahrenheit :

```python
>>> 100.0 * 9.0 / 5.0 + 32.0
212.0
>>> 37.0 * 9.0 / 5.0 + 32.0
98.6
>>> 233.0 * 9.0 / 5.0 + 32.0
451.4
```

La même chose en utilisant une fonction :

```python
>>> def fahrenheit(degre_celsius):
...     """ Conversion degré Celsius en degré Fahrenheit """
...     return degre_celsius * 9.0 / 5.0 + 32.0
...
>>> fahrenheit(100)
212.0
>>> fahrenheit(37)
98.6
>>> temperature = 233
>>> fahrenheit(temperature)
451.4
```

## Principe des fonctions 

Chaque fois qu'on sera amené à effectuer plusieurs manipulations similaires,
on créera une fonction pour éviter les copiers collers.


Une bonne fonction _ne fait qu'une chose_.

Elle prend des paramètres en entrée et retourne une valeur de sortie.

C'est tout ce qu'elle doit faire !



# L'instruction `def`




## Syntaxe


```python
def nom_de_la_fonction(parametre1, parametre2, parametre3, ...):
    """ Documentation
    qu'on peut écrire
    sur plusieurs lignes
    """

    bloc d instructions     # attention à l'indentation

    return resultat         # valeur de sortie 

```



### Exemple n°1



```python
# script Fonction1.py

def mapremierefonction():	# cette fonction n'a pas de paramètre
    """ Cette fonction affiche 'Bonjour' """
    print("Bonjour")
    return			# cette fonction ne retourne rien ('None')
				# l'instruction return est ici facultative
```

Une fois la fonction définie, nous pouvons l'appeler :

```python
>>> mapremierefonction()	# ne pas oublier les parenthèses ()
Bonjour
```


L'accès à la documentation se fait avec la fonction pré-définie `help()` :

```python
>>> help(mapremierefonction)	# affichage de la documentation
    Help on function mapremierefonction in module __main__:

    mapremierefonction()
        Cette fonction affiche 'Bonjour'
```




### Exemple n°2


La fonction suivante simule le comportement d'un dé à 6 faces.
Pour cela, on utilise la fonction `randint()` du module [`random`](http://docs.python.org/3/library/random.html?highlight=random#random).


```python
# script Fonction2.py
import random

def tirage_de():
    """ Retourne un nombre entier aléatoire entre 1 et 6 """
    valeur = random.randint(1, 6)
    return valeur
```


```python
>>> tirage_de()
3
>>> tirage_de()
6
```




### Exemple n°3


Voici une fonction qui calcule l'image par la fonction $f(x) = 2x + 1$.

```python
def image_fonction(x):
    return 2 * x + 1
```

On ajoute maintenant sa documentation :



```python
def image_fonction(x):
    '''
    Calcule l'image par la fonction
    @param x: (float)
    @return: (float)
    '''
    return 2 * x + 1
```

On peut aussi préciser les _types_ d'entrée et de sortie :

```python
def image_fonction(x: float) -> float:
    '''
    Calcule l'image par la fonction
    @param x: (float)
    @return: (float)
    '''
    return 2 * x + 1
```

On peut alors l'exécuter ou afficher son aide :

```python
>>> image_fonction(31)
63
>>> help(image_fonction)
Help on function image_fonction in module __main__:

image_fonction(x: float) -> float
    Calcule l'image par la fonction
    @param x: (float)
    @return: (float)
```



### Exemple n°4


Une fonction avec deux paramètres :


```python
# script Fonction4.py

# définition de fonction
def tirage_de2(valeur_min, valeur_max):
    """ Retourne un nombre entier aléatoire entre valeur_min et valeur_max """
    import random
    return random.randint(valeur_min, valeur_max)

# début du programme
for i in range(5):
    print(tirage_de2(1, 10)) 	# appel de la fonction avec les arguments 1 et 10
```



    >>>
    6
    7
    1
    10
    2
    >>>

A faire :

1. Compléter la documentation de la fonction :
    précisez le type des paramètres d'entrée et de la valeur de sortie.
2. Ajouter les types au squelette de la fonction comme dans l'exemple 3.


### Exemple n°5


Une fonction qui retourne une liste :


```python
# script Fonction5.py

# définition de fonction
def tirage_plusieurs_de(nombretirage):
    """ Retourne une liste de nombres entiers aléatoires entre 1 et 6 """
    import random
    resultat = [random.randint(1, 6) for i in range(nombretirage)]	# compréhension de listes (Cf. annexe)
    return resultat
```

On l'exécute pour tirer 10 dés : 

```python
>>> tirage_plusieurs_de(10)
[4, 1, 3, 3, 2, 1, 6, 6, 2, 5]
```

**A faire :**

1. Compléter la documentation de la fonction :
    précisez le type des paramètres d'entrée et de la valeur de sortie.
2. Ajouter les types au squelette de la fonction comme dans l'exemple 3.


### Exemple n°6


Une fonction qui détermine si un entier est pair.
Il peut y avoir plusieurs instructions `return` dans une fonction.
L'instruction `return` provoque le retour immédiat de la fonction.


```python
# script Fonction6.py

# définition de fonction
def est_pair(nombre):
    """ Retourne True si et seulement si 'nombre' est pair """
    if nombre % 2 == 0:   # L'opérateur % donne le reste d'une division
        return True
    else:
        return False
```

Et on l'exécute :


**A faire :**

1. Compléter la documentation de la fonction :
    précisez le type des paramètres d'entrée et de la valeur de sortie.
2. Ajouter les types au squelette de la fonction comme dans l'exemple 3.

### Amélioration de cette fonction :

Examinons le code de la fonction :

L'instruction `nombre % 2 == 0` retourne une valeur _booléenne_.

Si elle est vraie... on retourne True et si elle est fausse... on return False.

On peut donc simplifier la fonction ainsi :

```python
def est_pair(nombre):
    """ Retourne True si et seulement si 'nombre' est pair """
    return nombre % 2 == 0
```

Et le code ne fait plus qu'une ligne !

# Portée de variables : variables globales et locales


La _portée d'une variable_ est l'endroit du programme où on peut accéder à la variable.

Observons le script suivant :

```python
a = 10		# variable globale au programme

def mafonction():
    a = 20	# variable locale à la fonction
    return a
```



    >>> a               # nous sommmes dans l'espace global du programme
    10
    >>> mafonction()    # nous sommes dans l'espace local de la fonction
    20
    >>> a               # de retour dans l'espace global
    10


Nous avons deux variables différentes qui portent le même nom `a`

Une variable `a` de valeur 20 est créée dans la fonction : c'est une _variable locale_ à la fonction.
Elle est détruite dès que l'on sort de la fonction.


Maintenant, changeons légèrement le contenu :


```python
a = 10		# variable globale au programme

def mafonction():
    return a
```

Lorsqu'on exécute le script on obtient :

```
>>> a
10
>>> mafonction()
10
```


## `global`


L'instruction `global` rend une variable globale :

```python
a = 10		# variable globale

def mafonction():
    global a	# la variable est maintenant globale
    a = 20
    print(a)
    return
```


```
    >>> print(a)
    10
    >>> mafonction()
    20
    >>> print(a)
    20
```

Remarque : il est préférable d'éviter l'utilisation de l'instruction `global`
car c'est une source d'erreurs (on peut ainsi modifier le contenu d'une variable
globale en croyant agir sur une variable locale).
La sagesse recommande donc de suivre la règle suivante :



* ne jamais affecter dans un bloc de code local une variable de même nom
    qu'une variable globale



# Annexe : la compréhension de listes


La _compréhension de listes_ est une structure syntaxique disponible dans un
certain nombre de langages de programmation, dont Python.

C'est une manière de créer efficacement des listes.

Revenons sur l'exemple vu dans le script `Fonction5.py` :

```python
resultat = [random.randint(1, 6) for i in range(10)]
```

`resultat` contient 10 objets (`for ... range(10)`) qui sont tous obtenus par
le même appel (`random.randint(1, 6)`).



    >>> print(resultat)
    [3, 1, 5, 6, 4, 2, 1, 1, 3, 1]






## Autre exemple : liste de carrés



```python
carres = [i*i for i in range(11)]
```

qui contient :
```python
>>> print(carres)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

1. Que changer pour générer la liste des 100 premiers carrés (de 0 à 99) ?
2. Et pour les cubes ?




La compréhension de listes évite donc d'écrire le code "classique" suivant :

```python
carres = []
for i in range(11):
  carres.append(i * i)
```

## Liste par compréhension avec un filtre

On peut générer une liste par compréhension avec la syntaxe suivante :

```python
[objet for element in sequence if condition]
```


On obtient alors la liste de `objet` qui **respectent la condition.**

On _filtre_ la liste directement durant sa création.

_Exemple :_

```python
mes_carres = [x ** 2 for x in range(10) if x % 2 == 0]
```

Liste des carrés des entiers de 0 à 9 qui sont pairs.

```python
>>> mes_carres
[0, 4, 16, 36, 64]
```

### Autre exemple

Voici les noms des élèves : 

```python
eleves = ['Jean', 'Pauline', 'Francis', 'Mathilde', 'Louise']
```

Et tous ceux qui contiennent un `a` dans leur nom :

```python
eleve_avec_a = [nom for nom in eleves if 'a' in nom]
```

qui contient :

```python
>>> eleve_avec_a
['Jean', 'Pauline', 'Francis', 'Mathilde']
```

Maintenant ceux qui ont un prénom assez long :

```python
noms_longs = [nom for nom in eleves if len(nom) > 6]
```

qui contient :

```python
>>> noms_longs = ['Pauline', 'Francis', 'Mathilde']
```

# Exercices


## Exercice 4.1 ☆

1.  Ecrire une fonction `carre()` qui retourne le carré d'un nombre :

    ```python
    >>> carre(11.11111)
    123.4567654321
    ```

2. Avec une boucle `while` et la fonction `carre()`, écrire un script qui
    affiche le carré des nombres entiers de 1 à 100 :

    ```python
    >>>
    1^2 = 1
    2^2 = 4
    3^2 = 9
    ...
    99^2 = 9801
    100^2 = 10000
    Fin du programme
    ```

## Exercice 4.2 ☆

Ecrire une fonction qui retourne l'aire de la surface d'un disque de rayon R.

```python
from math import pi
```

Exemple :

```python
>>> airedisque(2.5)
19.6349540849
```

## Exercice 4.3

Écrire une fonction qui prend deux chaînes de caractères et retourne la plus
courte des deux :

```python
>>> plus_court("abc", "abcd")
'abc'
>>> plus_court("abcd", "ab")
'ab'
```


## Exercice 4.4 ★


1.  Ecrire une fonction qui retourne la factorielle d'un nombre entier N.

    On rappelle que :

    * factorielle de $N$ est noté $N!$
    * Par convention, $0!=1$
    * $N! = 1\times 2\times \ldots \times (N-1)\times N$
    * Par exemple : $3! = 1 \times 2 \times 3 = 6$
    * $1! = 1$


    Exemple :

    ```python
    >>> factorielle(50)
    30414093201713378043612608166064768844377641568960512000000000000
    ```


2. Comparez avec le résultat de la fonction [`factorial()`](http://docs.python.org/3/library/math.html) du module `math`.


## Exercice 4.5 ★

Ecrire une fonction qui retourne une carte (au hasard) d'un jeu de Poker à 52 cartes.
On utilisera la fonction `choice()` ou `randint()` du module `random`.
On donne :

```python
ListeCarte = ['2s', '2h', '2d', '2c', '3s', '3h', '3d', '3c',
              '4s', '4h', '4d', '4c', '5s', '5h', '5d', '5c',
              '6s', '6h', '6d', '6c', '7s', '7h', '7d', '7c',
              '8s', '8h', '8d', '8c', '9s', '9h', '9d', '9c',
              'Ts', 'Th', 'Td', 'Tc', 'Js', 'Jh', 'Jd', 'Jc',
              'Qs', 'Qh', 'Qd', 'Qc', 'Ks', 'Kh', 'Kd', 'Kc',
              'As', 'Ah', 'Ad', 'Ac']
```


```python
>>> tiragecarte()
7s
>>> tiragecarte()
Kd
```

## Exercice 4.4 ★

1. A l'aide de la fonction `randint()` du module `random`, écrire une fonction
    qui retourne un mot de passe de longueur N (chiffres, lettres minuscules ou majuscules).
    On donne :

    ```python
    chaine = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'`
    ```

    ```python
    >>> password(10)
    'mHVeC5rs8P'
    >>> password(6)
    'PYthoN'
    ```

2.  Reprendre la question 1) avec la fonction `choice()` du module `random`.
    Pour obtenir de l'aide sur cette fonction :

    ```python
    >>> import random
    >>> help(random.choice)
    ```

3.  Quel est le nombre de combinaisons possibles ?



---

## Exercice 4.6 ★★

1) Ecrire une fonction qui retourne une liste de N cartes **différentes** d'un jeu de Poker à 52 cartes.
Noter qu'une fonction peut appeler une fonction : on peut donc réutiliser la fonction `tiragecarte()` de l'exercice précédent.
Exemple :

```python
>>> print(tirage_n_carte(2))
    ['As', 'Ah']
>>> print(tirage_n_carte(25))
    ['Jc', 'Jh', 'Tc', '2d', '3h', 'Qc', '8d', '7c', 'As', 'Td', '8h', '9c', 'Ad', 'Qh',
    'Kc', '6s', '5h', 'Qd', 'Kh', '9h', '5d', 'Js', 'Ks', '5c', 'Th']
```




2) Simplifier le script avec la fonction `shuffle()` ou `sample()` du module `random`.

## Exercice 4.7 ★★

Ecrire une fonction qui retourne une grille de numéros du jeu Euro Millions.
On utilisera la fonction `sample()` du module `random`.

![euromillions](/uploads/uploads/2017/04/euromillions.png)



    >>> print(euromillions())
    [37, 23, 9, 11, 49, 2, 11]
    >>> print(euromillions())
    [16, 32, 8, 30, 40, 6, 4]


---

## Exercice 4.8 - listes par compréhension

On condidère les notes suivantes :

```python
notes = [13, 14, 8, 14, 12, 20, 10, 4, 18, 11, 12, 19, 8, 4, 19]
```
1. Créer, par compréhension la liste notes inférieures à 12 parmi celles-ci.
2. Créer, par compréhension la liste des notes impaires.
3. Les notes doivent toutes être baissées d'un point. Créer la nouvelle liste 
    par compréhension.

---

## Exercice 4.9 ★★

1) Ecrire une fonction qui retourne la valeur de la fonction mathématique `f(x)= 27x3 -27x2 -18x +8` :


    >>> print(f(0), f(1), f(0.5), f(0.25), f(0.375))
    8.0 -10.0 -4.375 2.234375 -1.123046875


2) On se propose de chercher les zéros de cette fonction par la [méthode de dichotomie](http://fr.wikipedia.org/wiki/Dichotomie).
Ecrire le script correspondant.


    >>>
    Recherche d'un zéro dans l'intervalle [a,b]
    a? 0
    b? 1
    Précision ? 1e-12
    0.5
    0.25
    0.375
    0.3125
    0.34375
    0.328125
    0.3359375
    0.33203125
    0.333984375
    0.3330078125
    0.33349609375
    0.333251953125
    ...
    ...
    0.333333333333
    >>>


3) Chercher tous les zéros de cette fonction.

Annexe : représentation graphique de la fonction `f(x)= 27x3 -27x2 -18x +8` (graphique réalisé avec la librairie [matplotlib](http://matplotlib.org/examples/pylab_examples/axes_props.html) de Python)

![fonction_matplotlib](/uploads/uploads/2017/04/fonction_matplotlib.png)



### QCM


[QCM sur les fonctions](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python_function)

Source : [Fabrice Sincère](http://fsincere.free.fr/isn/python/cours_python_ch4.php) - [Contenu sous licence CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/fr/)
