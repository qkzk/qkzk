---
title: "Probabilités & statistiques"
theme: "metropolis"
weight: 4
geometry: "margin=1.5cm"
header-includes: |
  \usepackage{tcolorbox}
  \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
  \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}
---



## Statistiques 


- [Script python accompagnant ce document](statistiques.py)
- [pdf](statistiques.pdf)

### Programme officiel
- Lire et comprendre une fonction Python renvoyant :
 - La moyenne.
 - L'écart type.
 - La proportion d'éléments appartenant à un intervalle donné.

### Moyenne 

Voici une fonction qui prend en entrée une série _non vide_ de valeurs (`list` de `int` ou `list` de `float`) et renvoie la moyenne des éléments.

On réalise la somme des éléments et on divise par leur nombre.

La fonction plante lorsqu'on l'utilise avec une liste vide.

```python 
def moyenne(valeurs):
    somme = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val 
        nb_valeurs = nb_valeurs + 1

    return somme / nb_valeurs

moyenne([1, 2, 3]) # renvoie 2.0
```

Cette fonction peut être considérablement réduite en utilisant les fonction `sum` et `len`.

### Écart-type

La fonction suivante calcule l'écart-type en utilisant la formule : $\delta(X) = \sqrt{E(X^2) - E(X)^2}$

```python 
from math import sqrt 

def ecart_type(valeurs):
    somme = 0
    somme_carres = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val
        somme_carres = somme_carres + val**2
        nb_valeurs = nb_valeurs + 1

    return sqrt(somme_carres / nb_valeurs - (somme / nb_valeurs) ** 2)

ecart_type([2, 4, 6, 8]) # 2.58
```

### Proportion d'éléments appartenant à un intervalle donné 

On dispose d'une série de valeurs et on souhaite connaître la proportion qui figure dans l'intervalle $[a;b]$

Voici une telle fonction :

```python 
def proportion_dans_ab(valeurs, a, b):
    nb_dans_intervalle = 0
    nb_total = 0

    for val in valeurs:
        if a <= val and val <= b:
            nb_dans_intervalle = nb_dans_intervalle + 1
        nb_total = nb_total + 1

    return nb_dans_intervalle / nb_total

proportion_dans_ab([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2.5, 7.5) # 0.5
```



## Probabilités

- [Script python accompagnant ce document](probabilites.py)
- [pdf](probabilites.pdf)

### Programme officiel



- Observer expérimentalement la loi des grands nombres.
- Simuler des échantillons aléatoires pour estimer des probabilités ou des proportions.
- Calculer des écarts entre fréquences observées et probabilités théoriques.

### Observer la loi des grands nombres 

Lorsqu'on réalise un grand nombre de fois la même expérience aléatoire (comme lancer un dé équilibré et regarder si on a obtenu un six), la fréquence des résultats obtenus s'approche de la probabilité théorique.

C'est la _loi des grands nombres_.

Voici une fonction qui simule un certain nombre de lancers de dés et donne la fréquence des six.

```python 
from random import randint 

def simuler_lancers(nb_lancers):
    nb_six = 0
    
    for i in range(nb_lancers):
        tirage = randint(1, 6)
        if tirage == 6:
            nb_six = nb_six + 1

    return nb_six / nb_lancers


simuler_lancers(1_000_000) ## s'approche de 1/6
```

### Simuler un échantillon aléatoire 

Afin de créer un échantillon aléatoire, on commence par simuler une expérience (n'importe laquelle) puis on la répète et on regroupe les résultats dans une liste.

Par exemple, pour simuler des notes entières entre 0 et 20 et créer un échantillon de 10 notes :

```python 
from random import randint 

def simuler_note():
    return randint(0, 20)

def creer_echantillon_note(taille):
    notes = []
    for i in range(taille):
        notes.append(simuler_note())

    return notes

creer_echantillon_note(10) # 10 notes entre 0 et 20
```

### Calculer des écarts entre fréquences observées et probabilités théoriques


Plus délicat.

L'idée est de comparer une situation _théorique_ décrite par les probabilités et une simulation de ce phénomène.

Considérons un lancer de dé équilibré et intéressons nous à la face obtenue.
C'est le modéle théorique.

L'univers $\Omega$ est $\{1, 2, 3, 4, 5, 6\}$

La loi :

| Face        | 1              | 2              | 3              | 4              | 5              | 6              |
|-------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Probabilité | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$

On simule une expérience aléatoire d'un tel lancer de dé et on regroupe toutes les valeurs dans une `list`. Ensuite on calcule l'espérance et l'écart-type de _l'écart_ entre le phénomène observé (les tirages)et le modèle théorique (les tirages).

Le code est trop long pour être intégré ici.
