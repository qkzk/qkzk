---
title: "Boucles"
theme: "metropolis"
weight: 3
geometry: "margin=1.5cm"
header-includes: |
  \usepackage{tcolorbox}
  \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
  \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}
---

[pdf](./act_boucles.pdf)

# Boucles

On l'a vu mais rappelons :

- Une **boucle** permet de répéter plusieurs fois les mêmes instructions.
- Il existe deux manières d'écrire des boucles en Python :

  - bornées :

    ```python
    for i in range(4):
        print("j'ai ", i, " tomates")
    ```

    Qui affiche :

    ```
    j'ai 0 tomate
    j'ai 1 tomate
    j'ai 2 tomate
    j'ai 3 tomate
    ```

    `i` a pris pour valeur successives `0, 1, 2, 3`

  - non bornées

    ```python
    s = 0
    while s < 100:
        s = s + 30
    ```

    Cette boucle tourne jusqu'à ce que la condition `s < 100` ne soit plus vérifiée.
    Ainsi, `s` prend pour valeurs successives : `30, 60, 90, 120` et la boucle s'arrête.
    À la fin, `s` vaut 120.

# Réponses

## Éditeur

On travaillera dans l'éditeur de code `thonny` (dossier `Informatique` sur le bureau de votre
poste) ou sur la calculatrice si vous n'avez pas d'ordinateur ou dans `bashton`
(chercher `basthon` dans google).

## Réponse

Créer un fichier par exercice en le nommant correctement : `exo_1.py`, par exemple

Joindre vos réponse et faire `rendre le travail` quand vous avez terminé.

# Exercices

## Exo 1

Faire tourner sur feuille la boucle suivante :

```python
p = 1
i = 1
while p < 10:
    p = p * i
    i = i + 1
```

Indiquer les valeurs de `i` et de `p` après chaque tour.

Ensuite programmer et vérifier.

Que fait ce programme ?

## Exo 2

1.  a) Écrire le code de la fonction répète qui affiche N fois la chaîne de caractères mot.
    b) Écrire le code d’une instruction utilisant cette fonction pour afficher 10 fois le mot « Bravo ! ».
2.  a) Écrire le code de la fonction afficheTriangle qui affiche la lettre a une fois sur la première
    ligne, deux fois sur la deuxième et ainsi de suite jusqu’à la N-ième ligne.
    b) Écrire le code d’une instruction utilisant cette fonction pour afficher un triangle de 4 lignes avec
    la lettre « x ».
3.  Si c est une chaîne de caractères, on note `len(c)` le nombre de caractères qu’elle contient (sa
    longueur, length en anglais) et chaque caractère est numéroté à partir de 0 par un indice `i` : on les
    note `c[0], c[1], ... , c[len(c)-1]`.

    a) Écrire l’instruction qui permet d’afficher la troisième lettre de la chaîne de caractères mot.
    b) Écrire le code de la fonction compte qui renvoie le nombre de caractères `a` contenus dans la
    chaîne de caractères `mot`.
    c) Écrire le code d’une instruction utilisant cette fonction pour afficher le nombre de "a" contenus
    dans la phrase "Gare et rage sont deux anagrammes : ne pas confondre avec garage.".
    d) Même consigne pour afficher le nombre de 1 contenus dans l’écriture décimale de l’entier
    `123456789*987654321`. Donner ce nombre.

## Exo 3

a) Écrire le code de la fonction `alea2` qui renvoie deux entiers aléatoires compris entre 1 et 20
inclus.
b) Écrire le code de la fonction `alea2_distincts` qui renvoie deux entiers aléatoires différents
compris entre 1 et 20 inclus.
c) Écrire le code de la fonction `temps_pour_paire` qui renvoie le nombre d’essais nécessaires pour
obtenir deux entiers aléatoires successifs compris entre 1 et 20 inclus avec la fonction alea2.

d) Écrire le code de la fonction `moyenne_tpp` qui renvoie la moyenne des
nombres d’essais nécessaires pour obtenir deux entiers aléatoires successifs compris entre 1 et 20
inclus sur N expériences (c’est-à-dire si on exécute N fois la fonction temps_pour_paire).
e) Écrire le code d’une instruction pour afficher le résultat avec N=20000. Donner ce résultat.

## Exo 4

Écrire le code de la fonction `pgmi` qui renvoie le plus grand multiple de `a` inférieur ou égal à `b` à
l’aide d’une boucle.

## Exo 5

1.  a) Écrire le code de la fonction `nbre_diviseurs` qui renvoie le nombre de diviseurs entiers
    naturels d’un entier naturel non nul `n`.
    b) Écrire le code d’une instruction pour afficher le nombre de diviseurs de 24680. Donner ce
    nombre.
2.  Écrire le code de la fonction `est_premier` qui renvoie `True` si `N` est premier et `False` sinon.
3.  Écrire le code de la fonction `premier_supérieur` qui renvoie le plus petit entier naturel premier
    supérieur ou égal à un entier non nul N.
4.  a) Écrire le code de la fonction comptePremier qui renvoie le nombre d’entiers premiers compris
    entre deux entiers a et b inclus.
    b) Écrire le code d’une instruction pour afficher le nombre d’entiers premiers compris entre 2 et
    1000 inclus. Donner ce nombre.

## Exo 6

1.  On appelle carré tout entier naturel $n$ qui peut s’écrire $n = a^2$ où $a$ est un entier naturel.
    a) Écrire le code de la fonction compteCarrés qui renvoie le nombre de carrés compris entre deux entiers naturels a et b inclus sans utiliser la fonction sqrt.

    b) Soit un réel $x$.
    On appelle _partie entière_ de $x$ et on note le plus grand entier inférieur ou égal à ;

    il est codé `floor(x)`.
    On appelle _valeur entière_ par excès de $x$ et on note $\lceil x\rceil$ le plus petit entier supérieur ou égal à $x$;

    il est codé `ceil(x)`.

    Remarque. Il faut importer la bibliothèque `math` pour utiliser ces deux fonctions
    (`from math import *`).

    Démontrer que si $x$ et $y$ sont deux réels $x \leq y$ tels que alors le nombre d’entiers
    $n$ compris entre $x$ et $y$ est $\lceil y\rceil - \lceil x \rceil + 1$.

    c) Écrire le code de la fonction _compte_carres_ qui renvoie le nombre de carrés compris entre deux
    entiers naturels a et b inclus en utilisant les fonctions précédentes.

2.  On appelle somme de deux carrés tout entier naturel qui peut s’écrire $n=p^2+q^2$

    où $p$ et $q$ sont deux entiers naturels.
    a) Démontrer que si est une somme de deux carrés alors il peut s’écrire $n=p^2+q^2$ avec
    $0 \leq p \leq \sqrt{\frac{n}{2}} \leq q \leq \sqrt{n}$
    b) Écrire le code de la fonction `somme_carres` qui renvoie deux nombres et dont la somme des
    carrés est égale à un entier $N$ s’il est une somme de deux carrés et `(-1, -1)` sinon.
