---
title: "Boucles bornées"
bookCollapseSection: true
author: "qkzk"
weight: 2

---

## Boucles

{{< hint warning >}}
Une _boucle_ est un bloc de code qui est répété plusieurs fois.

On distingue deux types de boucles, les boucles _bornées_ (`for`) et les boucles _non bornées_ (`while`).

Lorsqu'on sait à l'avance combien de fois on souhaite répéter un bloc on emploie une boucle bornée sinon 
une boucle non bornée.
{{< /hint >}}


## Boucle bornée : `for`

En Python la boucle bornée s'écrit ainsi :

```python
for variable in collection:
    bloc_de_la_boucle

fin_de_la_boucle
```

Notez bien la syntaxe : `for ... in ... :`

`variable` est une variable qui va _parcourir_ `collection`, c'est à dire qu'elle prendra
toutes les valeurs de la collection.

Les collections peuvent être des `list`, `tuple`, `str` etc.

Voyons deux exemples :

Afficher toutes les lettres d'un mot :

```python
for lettre in "bonjour":
  print(lettre)

print("fini !")
```

L'exécution de ce programme affiche :


```
b
o
n
j
o
u
r
fini !
```

On réalise bien que `lettre` a pri pour valeurs successives les caractères
composant `mot` : `"b"`, `"o"` etc.


### Exercice 1

Écrire à l'aide d'une boucle un programme qui affiche _deux fois_ chaque lettre de votre prénom.

```
F 
F
r
r
a
a
n
n
k
k
```

{{< python title="Exercice 1: doubler les lettres" >}}
prenom = "Frank"
{{< /python >}}

## La fonction `range`

{{< hint warning >}}
La fonction `range` renvoie une collection d'entiers qu'on peut parcourir.
{{< /hint >}}

C'est une fonction avancée que nous allons étudier pas à pas :

### `range` avec un paramètre

```python
for nombre in range(10):
    print(nombre)

print("j'ai affiché les entiers de 0 à 9")
```

Dont l'exécution produit l'affichage :


```
0
1
2
...
9
j'ai affiché les entiers de 0 à 9
```

L'instruction `print(nombre)` a donc été exécutée 10 fois (il y a 10 entiers de 0 à 9)

Résumons :

{{< hint warning >}}
`range(n)` renvoie la collection des entiers de `0` inclu à `n` exclu.
{{< /hint >}}

On n'est pas tenu d'utiliser ce paramètre, par exemple pour afficher 20 fois "Allez les bleus !",
je peux l'écrire en 20 lignes :

```python
print("Allez les bleus !")
print("Allez les bleus !")
print("Allez les bleus !")
print("Allez les bleus !")
... # encore 16 lignes identiques...
```

ou en deux lignes :


```python
for k in range(20):
    print("Allez les bleus !")
```

C'est beaucoup plus lisible et on sait immédiatement combien de fois l'instruction sera répétée.

### Exercice 2


```
J'ai 0 ans
J'ai 1 ans
J'ai 2 ans
J'ai 3 ans
J'ai 4 ans
J'ai 5 ans
J'ai 6 ans
J'ai 7 ans
J'ai 8 ans
J'ai 9 ans
```

Produire l'affichage précédent jusqu'à votre age en deux lignes de code.

{{< python title="_La vieillesse est un naufrage_ - Charles de Gaulle" >}}
{{< /python >}}


### Exercice 3 - somme des entiers

Calculons la somme des entiers entre 0 et 100.

Bien sûr on pourrait l'écrire à la main :


```
somme = 0 + 1 + 2 + 3 + ... + 100
```

Une très longue ligne serait nécessaire mais rien d'impossible.

On peut aussi une variable `somme` et une boucle.


1. Rectifiez la cellulle suivante qui veut calculer $0 + 1 + 2 + 3 = 6$


    {{< python title="Somme des entiers" >}}
somme = 0
for entier in range(3):
    somme = somme + entier

print(somme)
    {{< /python >}}


2. Calculez ensuite la somme des entiers jusque 100.

_Remarque :_ Vous apprendrez cette année en mathématiques à calculer ces sommes directement avec une formule très efficace.

## `range` avec deux paramètres

{{< hint warning >}}
`range(debut, fin)` parcourt les entiers de `debut` inclu jusque `fin` exclu.
{{< /hint >}}

Par exemple `range(5, 10)` va parcourir les entiers : 5, 6, 7, 8, et 9. Mais pas 10.

### Exercice 4

Calculer la somme des entiers à trois chiffres (de 100 à 999) dans la cellule Python précédente.

## `range` avec trois paramètres

{{< hint warning >}}
`range(debut, fin, pas)`, on parcourt les entiers de `debut` inclu à `fin` exclu en avançant de `pas` en `pas` :
{{< /hint >}}


Collection des entiers pairs entre 100 et 199 : (100, 102, 104, ..., 198) : `range(100, 199, 2)`

### Exercice 5

1. Calculer la somme des entiers impairs entre 1000 et 10000.
2. Calculer la somme des entiers divisibles par 3 entre 1000 et 10000.
3. Calculer la somme des entiers qui se terminent par 7 entre 654 et 1 million.
4. Compter le nombre d'entiers se terminant par deux zéros plus petits qu'un milliard à l'aide d'une boucle.

_On utilisera la cellule python précédente_

## Combiner des blocs


Puisque l'indentation indique la structure d'un programme, on doit faire attention à la position qu'on donne à nos structures. 

Les deux programmes suivants ne font pas la même chose :


{{< python title="consécutifs ou imbriqués" >}}
nombre = 5
couleur = "bleu"

print("consécutifs")
if nombre > 10:
    couleur = "rouge"

for lettre in couleur:
    print(lettre)


print("imbriqués")
if nombre > 10:
    couleur = "rouge"

    for lettre in couleur:
        print(lettre)
{{< /python >}}

1. Dans le premier cas, la structure `for` est au niveau 0 d'indentation, elle sera exécutée
    dans tous les cas.

      Il affiche ligne par ligne les lettres du mot "bleu".

2. Dans le second cas, la structure `for` est _dans le if_, elle ne sera exécutée que si la
    condition est vraie.

  La condition est fausse et le bloc `if` n'est pas exécuté donc il ne se passe rien.

### Parcourir une collection, avec ou sans indice

Condisérons deux problèmes a priori similaire :

- pour un mot, compter les "a" qu'il contient.
- pour un mot, afficher les positions de _chaquee "a" qu'il contient.

Les deux se résolvent en parcourant chaque lettre du mot. Une boucle bornée permet de résoudre le problème.

Dans le premier on ne se soucie que de la lettre : `for lettre in mot:` convient.

Alors que dans le second, il faut _l'indice de la lettre_ : `for i in range(len(mot)):`

{{< python title="indice ou non" init="" >}}
mot = "abracadabra"

# compter les a 
total = 0
for lettre in mot:
    if lettre == "a":
        total = total + 1

print("Il y a", total, "a dans", mot)
print()

# indice des a 
for i in range(len(mot)):
    lettre = mot[i]
    if lettre == "a":
        print(mot, "contient un 'a' à l'indice", i)
{{< /python >}}

**Un problème qui se résout en parcourant une fois une collection avec une boucle bornée est un _parcours séquentiel_**

Vous rencontrerez énormément de parcours séquentiels en NSI alors essayez de retenir dès maintenant cette nuance, cela vous aidera grandement par la suite.

### Exercice 6

On considère la phrase suivante :

```python 
phrase = "je n'aime pas me lever le matin, je préfère dormir."
```

_On répondra aux questions dans la cellule de code plus bas._

1. À l'aide d'une boucle et d'une condition, produire l'affichage suivant :

    _Ce sont les voyelles de la phrase_


    ```
    e est une voyelle
    a est une voyelle
    i est une voyelle
    e est une voyelle
    a est une voyelle
    e est une voyelle
    e est une voyelle
    e est une voyelle
    e est une voyelle
    a est une voyelle
    i est une voyelle
    e est une voyelle
    e est une voyelle
    o est une voyelle
    i est une voyelle
    ```


2. Intégrer les voyelles accentuées.

3. Compléter l'affichage précédent en affichant aussi les consonnes et la ponctuation : 

    ```
    j n'est pas une voyelle
    e est une voyelle
      n'est pas une voyelle
    n n'est pas une voyelle
    ' n'est pas une voyelle
    a est une voyelle
    i est une voyelle
    m n'est pas une voyelle
    e est une voyelle
      n'est pas une voyelle
    p n'est pas une voyelle
    a est une voyelle
    s n'est pas une voyelle
      n'est pas une voyelle
    m n'est pas une voyelle
    e est une voyelle
      n'est pas une voyelle
    l n'est pas une voyelle
    e est une voyelle
    ...
    ```

{{< python title="Cellule de l'exo 6" >}}
voyelles = "aeiouy"
phrase = "je n'aime pas me lever le matin, je préfère dormir."


{{< /python >}}


### Exercice 7

1. En utilisant `for` et une condition bien placée, comptez les voyelles dans un mot.

    Testez avec les mots "table", "exercice", "bonjour"

    {{< python title="voyelles" >}}
mot1 = "table"
mot2 = "exercice"
mot3 = "bonjour"
mot4 = "ordinateur"

voyelles = "aeiouy
    {{< /python >}}


2. Comptez cette fois les consonnes d'un mot sans accent ni tiret ni apostrophe comme `ordinateur`.

### Exercice 8 - table de multiplication

1. `nombre = 5`. En une ligne supplémentaire écrire :

      `4 * 5 = 20`

      Le nombre 20 doit être obtenu par opération.

      Rappel : `print(1, "abc", 2 * 3)` produit l'affichage :

     ```
     1 abc 6
     ```

2. Utiliser ce principe pour écrire la table de 4.

      ```
      4 * 0 = 0
      4 * 1 = 4
      4 * 2 = 8
      4 * 3 = 12
      4 * 4 = 16
      4 * 5 = 20
      4 * 6 = 24
      4 * 7 = 28
      4 * 8 = 32
      4 * 9 = 36
      4 * 10 = 40
      ```

3. En utilisant deux boucles _imbriquées_ (l'une **dans** l'autre), afficher
  les tables de multiplications des entiers de 0 à 10 inclu.

{{< python title="Python est malin, il a appris ses tables">}}
{{< /python >}}

### Exercice 9 - Mini challenge : somme des nombres impairs.

Avez vous remarqué que $1 + 3 = 2^2$ ? 

Mais ce n'est pas tout, $1 + 3 + 5 = 9 = 3^2$ !

Que dire de $1 + 3 + 5 + 7 = 16 = 4^2$ ?

Oh !

1. Vérifiez cette relation pour la somme des 100 premiers nombres impairs.
2. Faites la vérification dans une boucle pour _chaque somme intermédiaire_.

    La relation est vraie, donc n'affichez rien si elle est juste et un message si elle fausse.

{{< python title="Somme des impairs" init="" >}}
print(1 + 3 == 2 ** 2)
{{< /python >}}

{{< expand "" "..." >}}
```python
# On initialise la somme à 0
somme = 0
# On itère de 1 à 99
for i in range(1, 100):
    # on ajoute à somme le nombre impair suivant, il est de la forme 2 * i - 1
    somme = somme + (2 * i - 1)
    # testons s'il est le carré de i 
    if somme != i ** 2:
        # en cas d'échec, on affiche et on arrête la boucle
        print(i)
        break
print("ça marche :)")
```
{{< /expand >}}


