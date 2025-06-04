---
title: "Partie 1"
bookCollapseSection: true
author: "qkzk"
date: ""
weight: 1

---

# Les fonctions


Une fonction est une portion de code qui peut être exécutée lorsqu'on en a besoin.

{{< hint warning >}}
Utiliser une fonction se fait en deux temps :

1. définition de la fonction,
2. appel de la fonction.

L'appel d'une fonction _renvoie_ toujours une valeur. Si aucune valeur
de retour n'est spécifiée, alors la fonction renvoie `None`.
{{< /hint >}}

## Exemples

On a déjà rencontré plusieurs fonctions, en particulier `len`. Cette fonction
renvoie (on dit parfois _retourne_) le nombre d'éléments d'une collection.

* la définition de la fonction `len` est faite par le programme Python lui même,
  nous n'avons pas à nous en charger.
* l'appel de la fonction se fait ainsi : `len(objet)`

Par exemple :

```python
>>> nom = "Raymond"
>>> len(nom)
7
```

On a aussi rencontré la fonction `print`. Cette fonction renvoie `None`
et affiche un objet dans la console.

```python
>>> valeur = print("Bonjour !")
Bonjour
>>> valeur == None
True
```

La librairie `random` propose de nombreuses fonctions. Nous allons en étudier
une :

```python
>>> import random
>>> dir(ranom)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__',
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
'__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp',
'_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512',
'_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn',
'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss',
'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate',
'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.randint)
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
```

Que lit-on ?

* la notation `randint(a, b)` nous indique que cette fonction nécessite deux
  _paramètres_.
* La ligne suivante nous indique que la fonction renvoie un entier aléatoire
  entre `a` et `b` inclus.

Sans surprise :

```python
>>> random.randint(3, 7)
5
>>> random.randint(3, 7)
3
>>> random.randint(3, 7)
4
>>> random.randint(3, 7)
5
```

```python
import random
print(help(random.randint))

for i in range(5):
    print(random.randint(3, 7))
```

Va produire l'affichage de 5 nombres aléatoires entre 3 et 7.

On pourrait résumer cette fonction à son type :

```python
random.randint(int, int) -> int
```

Elle prend deux entiers et renvoie un entier.

Nous allons apprendre à appeler, concevoir, documenter des fonctions.

Mais avant ça...

Que pourrait-on dire du type de `print` ?

{{< hint warning >}}
```python
print(any, any, any, ...) -> None
```

`print` accepte autant de paramètres qu'on le souhaite et renvoie `None`.

Le fait qu'elle affiche quelque chose dans la console est _un effet de bord_.
{{< /hint >}}


### Exercice 0

Relire les deux lignes précédentes jusqu'à ce que vous les connaissiez par coeur.

**J'insiste**. Vous aurez 250 occasions de me remercier durant l'année.


## Appeler une fonction

Appeler une fonction consiste à l'introduire dans une instruction en respectant
son _type_, c'est à dire ses paramètres d'entrée et de sortie.

Il convient donc de le connaître ! C'est à ça que sert l'aide de Python, à
écrire convenablement les appels des fonctions et des objets afin d'éviter
les erreurs.

### Exercice 1

1. Documentez-vous sur la fonction `random.choice`.
  Que fait-elle ? Quel est son type ?
2. Les instructions suivantes sont-elles valables ?

  ```python
  >>> import random
  >>> random.choice("salut")
  >>> random.choice(salut)
  >>> random.choice("s")
  >>> random.choice(12345)
  >>> random.choice("12345")
  ```

  {{< python title="random.choice">}}import random
print(help(random.choice))
  {{< /python >}}

## Définir une fonction

Avant de se lancer dans la syntaxe et ses subtilités : pourquoi aurait-on besoin
de définir une fonction ?

Dès qu'un morceau de code réalise une tâche spécifique ou dès qu'il est répété
plusieurs fois, on l'inclut dans une fonction.

Cela permet d'éviter de le recopier plusieurs fois (et donc d'avoir à le
modifier autant de fois lorsqu'on voudra l'_adapter_).

Cela permet aussi de le _tester_ indépendamment et donc de s'assurer qu'il fait
ce qu'on attend de lui.

ce point peut sembler secondaire, pourquoi devrait-on "tester" le code. C'est
en fait fondamental.

Imaginons devoir manipuler des températures. Il existe deux unités de mesure
couramment employée : les degrés celcius et les Fahrenheit.

La conversion se fait à l'aide de la formule :

$$T_F = \dfrac{9}{5} \times T_C + 32$$


Bien sûr on pourrait faire :

```python
>>> 100.0 * 9.0 / 5.0 + 32.0
212.0
>>> 37.0 * 9.0 / 5.0 + 32.0
98.6
>>> 233.0 * 9.0 / 5.0 - 32.0
387.4
```

et convertir la température à l'aide de la formule. Même avec un copier-coller
cette approche est pénible... et dangereuse. 

Avez-vous repéré l'erreur dans les lignes précédentes ?

## Définition d'une fonction : syntaxe

{{< hint warning >}}
* On définit une fonction avec le mot clé `def` 
* après `def` on trouve le nom de la fonction,
* ensuite viennent ses paramètres entre des parenthèses,
* ensuite le symbole `:`
* Après `def` on trouve un bloc indenté contenant le corps de la fonction.
* La fonction s'arrête après le mot clé `return` qui indique ce qu'elle renvoie
  ou lorsque l'indentation revient au niveau précédent.
{{< /hint >}}


```python
def fahrenheit(degre_celcius):
  """
  Converti une temperature des degrés celcius 
  vers les Fahrenheit.
  """
  return degre_celcius * 9.0 / 5.0 + 32.0
```

On peut maintenant l'utiliser comme ceci :

```
>>> fahrenheit(100)
212.0
>>> fahrenheit(37)
98.6
```

La ligne `"""converti une temperature des degrés celcius vers les Fahrenheit"""`
appelée _docstring_ ou documentation est une chaîne de caractères pouvant
occuper plusieurs lignes.

On peut même consulter sa documentation :

```python
>>> help(fahrenheit)
Help on function fahrenheit in module __main__:

fahrenheit(degre_celsius)
    Converti une temperature des degrés celcius vers les Fahrenheit
```

Quelques recommandations importantes :

* chaque fois qu'on est amené à effectuer plusieurs manipulations similaires
  on crée une fonction,
* **une bonne fonction ne fait qu'une chose**,
* toutes vos fonctions doivent être documentées,
* on évite, autant que possible, les effets de bord.

```python
def fahrenheit(degre_celcius):
  """
  Converti une temperature des degrés celcius
  vers les Fahrenheit.
  """
  return degre_celcius * 9.0 / 5.0 + 32.0

help(fahrenheit)
print(fahrenheit(414))
print(fahrenheit(5))
```

```
Help on function fahrenheit in module __main__:

fahrenheit(degre_celcius)
    Converti une temperature des degrés celcius
    vers les Fahrenheit.

777.2
41.0
```

## Résumé : le mot clé `def`

{{< hint warning >}}
```python
def nom_de_la_fonction(parametre1, parametre2, parametre3, ...):
    """ Documentation qu'on peut écrire
    sur plusieurs lignes
    """
    bloc d instructions     # attention à l'indentation

    return resultat         # valeur de sortie 

arrive ici la déclaration est terminée
```
{{< /hint >}}

### Exercice 2 : écrire une fonction :

1. Écrire la définition d'une fonction : 

    * qui prend un paramètre appelé `prix_ht`,
    * qui renvoie le montant majoré de 20%,
    * appelée `prix_ttc`,
    * dont la documentation est : `"""Calcule la TVA"""`.

    On prendra garde à l'ordre !

    Voici ce qu'on doit obtenir en exécutant `help(prix_ttc)` :

    ```
    >>> help(prix_ttc)
    Help on function prix_ttc in module __main__:

    tva(prix_ht)
        Calcule le prix TTC
    ```

2. Calculez le prix TTC d'un article valant 150€, 10€
3. Que produit votre fonction lorsqu'on l'appelle avec les paramètres `"Mireille"`, `None` ? Expliquez.

{{< python title="prix TTC" >}}



{{< /python >}}

### Exercice 3 : documentation

Pour chaque fonction définie ci-dessous :

1. Indiquer son type d'entrée et de sortie
2. A-t-elle un effet de bord ?
3. Compléter sa documentation et proposer un nom plus adapté

{{< python title="fonctions" >}}
def ma_fonction():
  ''' '''
  return 3


def seconde_fonction(nombre):
  ''' '''
  return 5 * nombre


def troisieme_fonction(nom):
  ''' '''
  print("Bonjour", nom)
{{< /python >}}

### Exercice 4 : dé à $n$ faces

La fonction suivante simule le lancer d'un dé à six faces :



{{< python title="lancer un dé" >}}import random


def lancer_un_de():
    '''Renvoie un entier aléatoire entre 1 et 6'''
    valeur = random.randint(1, 6)
    return valeur

print(lancer_un_de())
{{< /python >}}

On l'exécute ainsi :


```python
>>> lancer_un_de()
3
>>> lancer_un_de()
6
```

Adapter la fonction pour qu'elle accepte un paramètre, le nombre de faces du dé.

On souhaite pouvoir l'utiliser ainsi :

```python
>>> lancer_un_de(20)
14
>>> lancer_un_de(10)
7
```

## Syntaxe complète et documentation complète

Voici une expression mathématiques : $f(x) = 2x + 1$

On peut la traduire simplement en :

```python
def f(x):
    return 2 * x + 1
```

Ce n'est pas très lisible et l'aide ne va pas nous apporter grand chose.

Donnons lui un nom explicite

```python
def image_de_f(x):
    return 2 * x + 1
```

Ajoutons sa documentation

```python
def image_de_f(x):
    """Renvoie l'image de x par f(x) = 2x + 1"""
    return 2 * x + 1
```

On peut aussi ajouter des _indications de type_, ce n'est pas obligatoire mais
c'est pratique !

```python
def image_de_f(x: float) -> float:
    '''Renvoie l'image de x par f(x) = 2x + 1'''
    return 2 * x + 1
```

Remarquez la syntaxe : 

* dans les parenthèses on met `x: float` c'est le type du paramètre `x`,
* derrnière les parenthèses on met : `-> float` c'est le type de sortie.

On peut indiquer aussi les types dans la documentation :


```python
def image_de_f(x: float) -> float:
    '''
    Renvoie l'image de x par f(x) = 2x + 1
    
    @param x: (float) l'antécédent
    @return:  (float) l'image
    '''
    return 2 * x + 1
```

et maintenant :

```python
>>> image_de_f(31)
63
>>> help(image_de_f)
Help on function image_fonction in module __main__:

image_de_f(x: float) -> float
    Renvoie l'image de x par f(x) = 2x + 1
    @param x: (float) l'antécédent
    @return:  (float) l'image
```


### Exercice 5 : code d'une fonction

Pour chaque question :

* on donnera le code complet avec documentation et indication de type.
* on écrira un exemple.


```python
def compte_les_a(mot: str) -> int:
    """
    Renvoie le nombre de `a` dans `mot`.

    @param mot: (str) un mot formé de lettres.
    @return: (int) le nombre de `a`
    """
    nombre_de_a = 0
    for lettre in mot:
        if lettre == "a":
            nombre_de_a = nombre_de_a + 1
    return nombre_de_a

mot = "abracadabra"
print(f"{mot} comporte {compte_les_a(mot)} a")
```

{{< python title="Réponses exo 5">}}
{{< /python >}}


1. Écrire une fonction qui calcule l'image par $f(x) = x^2 - 2x + 3$

2. Les fonctions peuvent accepter plusieurs paramètres d'entrée. Écrire 
  une fonction qui prend trois paramètres entiers et renvoie leur somme.

    ```python
    >>> somme_de_trois_nombres(1, 2, 3)
    6
    ```

3. `contient_un_z` accepte une chaîne de caractère en paramètre d'entrée
    et renvoie un booléen. Il est vrai si la chaîne reçue contient la lettre `z`

4. `contient_la_lettre` accepte _deux_ paramètres d'entrée, des chaînes,
    elle renvoie vraie si le second paramètre (une lettre) est présent dans
    le premier.

5. `longueur` simule le comportement de `len` pour les chaînes de caracètres.

    C'est évident mais je le précise, vous n'avez pas le droit d'utiliser `len` !

6. `factorielle` renvoie le produit des entiers jusqu'au paramètre `n`, un entier
  plus grand que 0. 

    ```python
    >>> factorielle(5)
    120
    ```

    Complément: Modifier la fonction pour respecter la définition mathématique:
      `factorielle(0) == 1`

7. `plus_grand_des_deux` prend deux paramètres entiers et renvoie le plus grand
  des deux.

### Exercice 6 : mini challenge

Reprendre le dernier exercice (équations du second degré) de la partie "Conditions" et écrire une fonction `resoudre_trinome` qui prend trois paramètres et renvoie les racines de celui-ci.

Votre fonction renvoie toujours un `tuple` qui contient 0, 1 ou deux valeurs approchées des racines.


```python 
>>> resoudre_trinome(1, 2, 1) # x^2 + 2x + 1 = 0 => x=-1
(-1.0,)
>>> resoudre_trinome(1, 2, 2) # x^2 + 2x + 2 = 0 => pas de sol 
()
>>> resoudre_trinome(1, 2, 0) # x^2 + 2x = 0 => x=0 ou x = -2
(-2.0, 0.0)
```

{{< expand "" "..." >}}
```python
def resoudre_trinome(a: float, b: float, c: float) -> tuple:
    """Renvoie les solutions réelles de ax^2+bx+c = 0 dans un tuple"""
    delta = b ** 2 - 4 * a * c 
    if delta < 0:
        # on renvoie un tuple vide
        return ()
    elif delta == 0:
        # attention ici on doit renvoyer un tuple d'un seul élément,
        # il faut ajouter une virgule avant de fermer la parenthèse
        return (-b / (2 * a), )
    else:
        return ((-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a))


print(resoudre_trinome(1, 2, 1))
print(resoudre_trinome(1, 2, 2))
print(resoudre_trinome(1, 2, 0))
```
{{< /expand >}}

### Exercice 7 : mini challenge

1. Écrire une fonction `indice_du_min` qui prend un tableau `tab` non vide et renvoie _l'indice_ de son élément minimal

    ```python 
    >>> indice_du_min([1, 0, 3, 2, 9])
    1
    >>> indice_du_min([1, 3, 5, 7])
    0
    ```

2. Les voyelles c'est has been. Maintenant je n'écris plus que les consonnes ! Cmprs ?

    Écrire une foncion `filtre_voyelle` qui reçoit un mot en minuscule et renvoie sa version sans voyelle 
    
    ```python 
    voyelles = "aeiouy"
    ```

    Exemple :

    ```python 
    >>> filtre_voyelle("compris")
    "cmprs"
    >>> filtre_voyelle("abcde")
    "bcd"
    ```

  {{< expand "" "..." >}}
  ```python
  VOYELLES = "aeiouy"

  def filtre_voyelle(mot: str) -> str:
      nouveau = ""
      for lettre in mot:
          if lettre not in VOYELLES:
              nouveau = nouveau + lettre 

      return nouveau 

  print(filtre_voyelle("compris"))
  print(filtre_voyelle("abcdefghijklmnopqrstuvwxyz"))
  ```
  {{< /expand >}}

3. Écrire une fonction `est_trie` qui reçoit un tableau d'entiers et renvoie un booléen valant vrai si et seulement si les éléments du tableau sont triés par ordre croissant.

    ```python 
    >>> est_trie([1, 3, 2])
    False
    >>> est_trie([1, 2, 3])
    True
    ```

  {{< expand "" "..." >}}
  ```python 
  def est_trie(tab: list) -> bool:
      """Vrai ssi le tableau est trié par ordre croissant"""
      for i in range(len(tab) - 1):
          if tab[i] > tab[i + 1]:
              return False 
      return True 

  print(est_trie([1, 2, 3]))
  print(est_trie([1, 3, 2]))
  ```
  {{< /expand >}}
