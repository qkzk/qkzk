---
author: qu3nt1n
date: 2019-05-05 06:04:14+00:00
draft: false
title: Python 3 - 01 Les variables, les types
bookCollapseSection: true
weight: 1

---
# Consignes pour le suivi des cours

**Pour chacun des cours :**

1. Ouvrez l'éditeur Thonny.
2. Tapez chacune des commandes présentées et vérifiez son résultat.
3. Complétez votre script **resume_ch1.py** avec les nouvelles commandes
  apprises. C'est léquivalent d'une fiche de cours, prenez-en soin.
4. Déposez les dans votre drive, dans un dossier `NSI_nom_prenom`
    **que vous me partagez.**
5. Voici, par exemple, ce que vous pourriez noter dans le script

  ```python
  # Ch1 variables

  ## noms
  # minuscules > majuscules
  age = 17 # int
  print(age) # afficher la variable
  ...
  ```
---


**Pour chaque série d'exercice (à la fin des cours) :**

1. Réalisez les exercices dans un fichier bien nommé : **exo_ch1.py**

    Vous pouvez préférer les traiter un par un : **exo_ch1_01.py**
2. Vous pouvez les traiter **dans Thonny** ou dans **Colab**
3. Vous devez traiter tous les exercices **ayant 0 ou 1 étoile.**
4. Déposez les dans votre drive, dans le dossier `NSI_nom_prenom` **que vous m'avez partagé.**


---

## Chapitre 1 - Variables, types et opérateurs


Une variable est un espace mémoire dans lequel il est possible de stocker une valeur (une donnée).

Ouvrir Thonny dont le raccourci devrait être dans le dossier informatique :

<!-- ![idle_1](/uploads/uploads/2017/04/idle_1.png) -->
![idle_1](/uploads/docsnsi/python/thonny.jpg)



### 0- Noms de variables


Le nom d'une variable s'écrit avec des lettres (non accentuées), des chiffres ou bien l'underscore _
Le nom d'une variable ne doit pas commencer par un chiffre.

En langage Python, l'usage est de ne pas utiliser de lettres majuscules pour nommer les variables (celles-ci sont réservées pour nommer les classes).

Exemple : `age, mon_age, temperature1`

A éviter : `Age, AGE, MonAge, monAge, Temperature1`


### 1- Le type `int` (integer : nombres entiers)


Pour affecter (on dit aussi assigner) la valeur 17 à la variable nommée `age` :

```python
>>> age = 17
```

La fonction `print` affiche la valeur de la variable :

```python
>>> print(age)
17
```

La fonction `type()` retourne le type de la variable :

```python
>>> print(type(age))
<class 'int'>
```

`int` est le type des nombres entiers.

```python
>>> # ceci est un commentaire
>>> age = age + 1	# en plus court : age += 1
>>> print(age)
18
>>> age = age - 3	# en plus court : age -= 3
>>> print(age)
15
>>> age = age * 2		# en plus court : age *= 2
>>> print(age)
30
```


```python
>>> a = 6*3 - 20
>>> print(a)
-2
```


On peut afficher plusieurs élément sur une même ligne en les séparant d'une
virgule.

```python
>>> b = 25
>>> c = a + 2*b
>>> print(b, c)          # ne pas oublier la virgule
25 48
```

L'opérateur `//` donne la division entière :

```python
>>> 4 // 3  # 4 = 3 * 1 + reste
1
>>> tour = 450//360
>>> print(tour)
1
```

L'opérateur `%` donne le reste de la division (opération modulo) :

```python
>>> angle = 450 % 360
>>> print(angle)
90
```

L'opérateur `**` donne la puissance :

```python
>>> mo = 2 ** 20 # 2 puissance 20
>>> print(mo)
1048576
>>> racine2 = 2 ** 0.5 # 2 puissance 1/2
>>> print(racine2)
1.41421356237
```

**Opérations sur les nombres**

| Opération            | Opérateur |
|----------------------|-----------|
| addition             | `+`       |
| soustraction         | `-`       |
| produit              | `*`       |
| exposant             | `**`      |
| division réelle      | `/`       |
| division entière     | `//`      |
| reste de la division | `%`       |

### 2- Le type `float` (nombres en virgule flottante)



```python
>>> b = 17.0 	# le séparateur décimal est un point (et non une virgule)
>>> print(b)
17.0
>>> print(type(b))
<class 'float'>
```


```python
>>> c = 14.0 / 3.0
>>> print(c)
4.66666666667
```


```python
>>> c = 14.0 // 3.0	# division entière
>>> print(c)
4.0
```

Attention : avec des nombres entiers, l'opérateur `/` renvoie généralement un flottant :

```python
>>> c = 14 / 3
>>> print(c)
4.666666666666667
```


Notation scientifique :

```python
>>> a = -1.784892e4
>>> print(a)
-17848.92
```



#### Les fonctions mathématiques


Pour utiliser les fonctions mathématiques, il faut commencer par importer le module `math` :

```python
>>> import math
```

On peut lister un paquet avec la fonction `dir()`

```python
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf',
'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
```

Pour appeler une fonction d'un module, la syntaxe est la suivante :
`module.fonction(arguments)`

Pour accéder à une donnée d'un module :
`module.data`

```python
>>> print(math.pi)		# donnée pi du module math (nombre pi)
3.14159265359
>>> print(math.sin(math.pi/4.0)) # fonction sin() du module math (sinus)
0.707106781187
>>> print(math.sqrt(2.0)) 	# fonction sqrt() du module math (racine carrée)
1.41421356237
>>> print(math.sqrt(-5.0))
Traceback (most recent call last):
    print(math.sqrt(-5.0))
ValueError: math domain error
>>> print(math.exp(-3.0)) 	# fonction exp() du module math (exponentielle)
0.0497870683679
>>> print(math.log(math.e)) 	# fonction log() du module math (logarithme népérien)
1.0
```



### 3- Le type `str` (string : chaîne de caractères)



```python
>>> nom = 'Dupont' 	# entre apostrophes
>>> print(nom)
Dupont
>>> print(type(nom))
<class 'str'>
>>> prenom = "Pierre" 	# on peut aussi utiliser les guillemets
>>> print(prenom)
Pierre
>>> print(nom, prenom) 	# ne pas oublier la virgule
Dupont Pierre
```

La concaténation désigne la mise bout à bout de plusieurs chaînes de caractères.
La concaténation utilise l'opérateur `+`

```python
>>> chaine = nom + prenom	# concaténation de deux chaînes de caractères
>>> print(chaine)
DupontPierre
>>> chaine = prenom + nom	# concaténation de deux chaînes de caractères
>>> print(chaine)
PierreDupont
>>> chaine = prenom + ' ' + nom
>>> print(chaine)
Pierre Dupont
>>> chaine = chaine + ' 18 ans'	# en plus court : chaine += ' 18 ans'
>>> print(chaine)
Pierre Dupont 18 ans
```

La fonction `len()` retourne la longueur (length) de la chaîne de caractères :


```python
>>> len("abc")
3
```


Indices et tranches (_index_ and _slices_ en anglais) :

```python
>>> print(chaine[0]) 	# premier caractère (indice 0)
P
>>> print(chaine[1])	# deuxième caractère (indice 1)
i
>>> print(chaine[1:4])	# slicing : cacatères d'indice 1, 2 et 3
ier
>>> print(chaine[2:])	# slicing : caractères d'indice supérieur à 2
erre Dupont 18 ans
>>> print(chaine[-1])	# dernier caractère (indice -1)
s
>>> print(chaine[-6:])	# slicing : depuis le sixième en partant de la fin
18 ans
```

En résumé :

```
lettre chaine          :   M   u   r   i   e   l
position depuis 0      :   0   1   2   3   4   5
position depuis la fin :  -6  -5  -4  -3  -2  -1
```


Attention aux apostrophes et guillemets dans les chaînes de caractères !

```python
>>> chaine = 'Aujourd'hui'
SyntaxError: invalid syntax
>>> chaine  = 'Aujourd\'hui'		# séquence d'échappement \'
>>> print(chaine)
Aujourd'hui
>>> chaine  = "Aujourd'hui"
>>> print(chaine)
Aujourd'hui
```



La séquence d'échappement `\n` représente un saut ligne :

```python
>>> chaine = 'Premiere ligne\nDeuxieme ligne'
>>> print(chaine)
Premiere ligne
Deuxieme ligne
```

Plus simplement, on peut utiliser les triples guillemets
(ou les triples apostrophes) pour encadrer une chaîne définie sur plusieurs
lignes :

```python
>>> chaine = """Premiere ligne
Deuxième ligne"""
>>> print(chaine)
Premiere ligne
Deuxieme ligne
```

On ne peut pas mélanger les serviettes et les torchons
(ici type `str` et type `int`) :

```python
>>> chaine = '17.45'
>>> print(type(chaine))
<class 'str'>
>>> chaine = chaine + 2
TypeError: cannot concatenate 'str' and 'int' objects
```

La fonction `float()` permet de convertir un type `str` en type `float`

```python
>>> nombre = float(chaine)
>>> print(nombre)
17.45
>>> print(type(nombre))
<class 'float'>
>>> nombre = nombre + 2		# en plus court : nombre += 2
>>> print(nombre)
19.45
```

Inversement, `str` transforme un nombre en chaîne de caractère :

```python
>>> a = 1
>>> b = str(a)
>>> type(b)
<class 'str'>
```

La fonction `input()` lance une invite de commande (en anglais : prompt)
pour saisir une chaîne de caractères.

```python
>>> # saisir une chaîne de caractères et valider avec la touche Enter
>>> chaine = input("Entrer un nombre : ")
Entrer un nombre : 14.56
>>> print(chaine)
14.56
>>> print(type(chaine))
<class 'str'>
>>> nombre = float(chaine)	# conversion de type
>>> print(nombre**2)
211.9936
```

En Python 3, le résultat de `input` est _toujours_ une chaîne de caractère.


### 4- Le type `list` (liste)


Une liste est une structure de données.
Le premier élément d'une liste possède l'indice (l'index) 0.
Dans une liste, on peut avoir des éléments de plusieurs types.

Les éléments d'une listes sont notés à l'aide des crochets `[ ... ]`

```python
>>> infoperso = ['Pierre', 'Dupont', 17, 1.75, 72.5]
>>> # infoperso est une liste
>>> type(infoperso)
<class 'list'>
>>> # infoperso contient 5 éléments de types str, str, int, float et float
>>> len(infoperso)
5
```

On accède aux éléments d'une liste par leur indice (un entier) : `ma_liste[indice]`

```python
>>> print('Prénom : ', infoperso[0])        # premier élément (indice 0)
Prénom :  Pierre
>>> print('Age : ', infoperso[2])           # le troisième élément a l'indice 2
Age :  17
>>> print('Taille : ', infoperso[3])        # le quatrième élément a l'indice 3
Taille :  1.75
>>> print('Masse : ', infoperso[-1])        # le dernier élément de la liste
```

La fonction `range()` crée un itérateur qui se comporte grossièrement comme une
liste d'entiers régulièrement espacés :

```python
>>> mon_range = range(10)
>>> print(mon_range)
range(0, 10)
>>> print(type(mon_range))
<class 'range'>
>>> ma_liste = list(mon_range)
>>> print(ma_liste)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(type(ma_liste))
<class 'list'>
```

`range(10)` : **10** nombres, à partir de **0**.

```python
>>> maliste = list(range(1, 10, 2))	# range(début, fin non comprise, pas)
>>> print(maliste)
[1, 3, 5, 7, 9]
>>> print(maliste[2])		# le troisième élément a l'indice 2
5
```




### 5- Le type `bool` (booléen)


Deux valeurs sont possibles : `True` et `False`


Ils permettent de faire des _tests_ en tout genre.

```python
>>> choix = True
>>> print(type(choix))
<class 'bool'>
```

Les opérateurs de comparaison :

| Comparaison       | Opérateur | Exemple  valant `True` | Exemple valant `False` |
|-------------------|-----------|------------------------|------------------------|
| égalité           | `==`      | `1 + 1 == 2`           | `1 + 1 == 2`           |
| différent         | `!=`      | `1 + 1 != 3`           | `1 + 1 != 2`           |
| supérieur         | `>`       | `3 > 2`                | `1 > 2`                |
| inférieur         | `<`       | `2 < 3`                | `2 < 1`                |
| supérieur ou égal | `>=`      | `2 + 2 >= len('1234')` | `2 >= 1`               |
| inférieur ou égal | `<=`      | `3 * 4 <= 4 * 4`       | `3 * 4 <= 2 * 4`       |

**Le résultat d'une comparaison est toujours un booléen.**

**ATTENTION :**

* Affecter avec 1 égal `a = 2`
* Comparer avec 2 égals `1 + 1 == 2`

```python
>>> b = 10
>>> b > 8
True
>>> b == 5
False
>>> b != 10
False
>>> 0 <= b <= 20
True
```

Les opérateurs logiques : `and, or, not`

* `not` est le _contraire de_ : `not True` vaut `False` et `not False` vaut `True`

    ```python
    >>> not (1 + 1 == 2)
    False
    ```

* `and` est un `ET` logique. En algorithmie il est souvent noté `&`
    Le résultat d'un ET est vrai si et seulement si les deux booléens sont
    vrais.

    `2 > 1 and 3 > 4` vaut `False`

* `or` est un `OU` logique. En algorithmie il est souvent noté `|`

    Le résultat d'un OU est vrai si l'un des deux (ou les deux) booléens sont
    vrais.

    `2 > 1 or 3 > 4` vaut True

```python
>>> note = 13.0
>>> mention_ab = note >= 12.0 and note < 14.0 # ou bien : mention_ab = 12.0 <= note < 14.0
>>> mention_ab
True
>>> not mention_ab
False
>>> note == 20.0 or note == 0.0
False
```

L'opérateur `in` s'utilise avec des chaînes (type `str`) ou des listes (type `list`) :

```python
>>> 1 in [1, 2, 3] # la liste contient-elle 1 ?
True
>>> 4 in [1, 2, 3] # la liste contient-elle 4 ?
False
>>> 'A' in 'Albert' # la chaîne 'A' figure-t-elle dans 'Albert' ?
True
>>> 'Aert' in 'Albert' # la chaîne 'Aert' figure-t-elle dans 'Albert' ?
False
```



### 6- Le type `dict` (dictionnaire)


Un dictionnaire stocke des données sous la forme **clé ⇒ valeur**.
Une clé est unique et n'est pas nécessairement un entier (comme c'est le cas de l'indice d'une liste).

```python
>>> personne = {'nom': 'Duchmol', 'prenom': 'Robert'}
>>> personne['nom']
'Duchmol'
>>> personne['prenom']
'Robert'
>>> type(personne)
<class 'dict'>
```

Les dictionnaires sont _mutables_, on peut leur ajouter des éléments :

```python
>>> personne['age'] = 42
>>> personne['age'
personne = {'nom': 'Duchmol', 'prenom': 'Robert', 'age': 42}
```



### 7- Autres types


Nous avons survolé les types les plus courants.
Il en existe bien d'autres :



* complex (nombres complexes, par exemple 1+2.5j)
* tuple (structure de données similaire aux listes mais _immuables_)
* set (structure de données sans répétition)
* file (fichiers)
* ...




### 8- Programmation Orientée Objet (POO)


Python est un langage de programmation **orienté objet** (comme les langages
C++, Java, PHP, Ruby...).
Une variable est en fait un **objet** d'une certaine **classe**.

Par exemple, la variable `amis` est un objet de la classe `list`.
On dit aussi que la variable `amis` est une **instance** de la classe `list`.

L'**instanciation** (action d'instancier) est la création d'un objet à partir
d'une classe (syntaxe : **NouvelObjet = NomdelaClasse(arguments)**) :

```python
>>> # instanciation de l'objet amis de la classe list
>>> amis = ['Nicolas', 'Julie']
>>> print(type(amis))
<class 'list'>
```

Une classe possède des fonctions que l'on appelle **méthodes** et des données
que l'on appelle **attributs**.

La méthode `append()` de la classe `list` ajoute un nouvel élément en fin
de liste :

```python
>>> # instanciation d'une liste vide
>>> amis = []			# ou bien : amis = list()
>>> amis.append('Nicolas')	# synthase générale : objet.méthode(arguments)
>>> amis
['Nicolas']
>>> amis.append('Julie')	# ou bien : amis = amis + ['Julie']
>>> amis
['Nicolas', 'Julie']
>>> amis.append('Pauline')
>>> amis
['Nicolas', 'Julie', 'Pauline']
```

La méthode `pop` de la classe liste renvoie le dernier de la liste et l'enlève
de celle-ci

```python
>>> ma_liste = [1, 2, 3]
>>> ma_liste.pop()
3
>>> ma_liste
[1, 2]
```

```python
>>> amis.sort()			# la méthode sort() trie les éléments en place.
>>> amis                # la liste est modifiée !!!
['Julie', 'Nicolas', 'Pauline']
```


```python
>>> amis.reverse()		# la méthode reverse() retourne une liste
>>> amis
['Pauline', 'Nicolas', 'Julie']
```

La méthode `lower()` de la classe `str` retourne la chaîne de caractères en casse minuscule :



## Exercices


### Exercice 1.1 ☆

Afficher la taille en octets et en bits d'un fichier de 536 ko.

_On donne : 1 ko (1 kilooctet) = 1000 octets et 1 octet = 8 bits_

### Exercice 1.2

Les amis de Robert sont Marcel, Frank et Marie.

1. Créer la `liste` de ses amis. 
2. Robert a rencontré son voisin Raoul. Ajoutez son nouvel ami à la liste sans
    créer de nouvelle liste.
3. Ils ont respectivement 36 ans, 22 ans, 27 ans et 28 ans. Créer le
    dictionnaire de leurs âges respectifs.
4. C'est l'anniversaire de Marcel. Augmentez son âge d'un an.
4. Robert et Franck se sont brouillés. Supprimez Franck de la liste des amis et
    du dictionnaire des âges.

    ```python
    >>> ma_liste = ['a', 'b', 'c']
    >>> del ma_liste[1]             # supprime l'élément d'indice 1
    >>> ma_liste
    ['a', 'c']
    ```
    


### Exercice 1.3 ★

Le numéro de sécurité sociale est constitué de 13 chiffres auquels s'ajoute
la clé de contrôle à 2 chiffres.

Exemple : 1 89 11 26 108 268 91

La clé de contrôle est calculée par la formule :

97 - (numéro de sécurité sociale modulo 97)

Donc ici :

```python
>>> chiffres = 1891126108268    # sans les deux derniers chiffres !
>>> cle = 97 - (chiffres % 97)  # modulo = reste de la division entière
91
>>>
```

Robert a tenté de frauder chez le médecin. Il a donné les informations
suivantes :

"Mon numéro de sécurité sociale est 1 57 10 21 122 350 11"

1. Expliquez pourquoi il a reçu une convocation au commissariat de police.
2. La variable `secu` contient un entier (`int`) constitué des 13 chiffres et de la clé.

    a. Comment extraire les 13 chiffres du numéro depuis la variable `secu` ?

    b. Comment extraire la clé de contrôle constituée des deux derniers chiffres ?

    c. Proposez une expression booléenne qui vérifie la clé de
        contrôle.

    <!--
    >>> cle = secu % 100
    >>> numero = secu // 100
    >>> cle == (97 - (numero % 97))
    -->

### Exercice 1.3 ★

1. Afficher la valeur numérique de $\sqrt{4,63 - 15/16}$ à l'aide du module `math`
2. Le prof. de maths qui sommeille en moi vous rappelle que :

    $x^{0.5} = \sqrt{x}$ pour tout $x \geq 0$.\
    Retouvez le résultat précédent sans utiliser la librairie `math`.


### Exercice 1.4 ★

À partir des deux variables `prenom` et `nom`, afficher
les initiales (par exemple LM pour Léa Martin).

Rappel : 

```python
>>> prenom = 'David'
>>> prenom[0]
'D'
>>> prenom[1]
'a'
```


### Exercice 1.5 ★☆

L'identifiant d'accès au réseau du lycée est construit de
la manière suivante : initiale du prénom puis les 8 premiers caractères du nom (le tout en minuscule).

Exemple : Alexandre Lecouturier → alecoutur.\
À partir des deux variables `prenom` et `nom`, construire l'identifiant.

### Exercice 1.6 ★★

On donne un extrait des logins d'accès au réseau du lycée :


    alecoutur  Huz4
    lmartin    monty
    fsincere   gnugpl


1) Créer une variable de type `dict` qui contient les couples
identifiant - mot de passe ci-dessus.

2) La saisie du login fournit deux variables `identifiant` et `motdepasse` :
une pour l'identifiant et l'autre pour le mot de passe.

Construire une variable booléenne qui donne `True` en cas d'identification
correcte, et `False` dans le cas contraire :

* lmartin monty → True
* alecoutur fqsdf → False
* martin monty → False (ce cas est plus compliqué à traiter)


### QCM


[QCM sur les types int, float et str](http://fabrice.sincere.free.fr/qcm/qcm.php?nom=qcm_python3x_1)

Source : [Fabrice Sincère](http://fsincere.free.fr/isn/python/cours_python_ch1.php) - [Contenu sous licence CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/fr/)
