---
title: "Booléens : TD"
author: "qkzk"
weight: 2

---

### pdf : [pour impression](/uploads/docsnsi/booleens/booleen_cours.pdf)

# Objectifs

* Construire la table de vérité d'une expression booléenne relativement simple.
* Évaluer et construire des expressions booléennes en Python

# Exercice 1

Construire la table de vérité de l'expression : `a OU (NON b)`

# Exercice 2

Construire la table de vérité de l'expression : `NON a et (b ou c)`

# Exercice 3

Construire la table de vérité de l'expression : `(a et NON b) ou (NON a et b)`

# Exercice 4

Construire la table de vérité de l'expression : `(a OU b) ET (a OU c)`

# Exercice 5

Trouver une expression équivalente à `a et b` construite uniquement à partir
des opérateurs `NON` et `ou`

On vérifiera à l'aide d'une table de vérité.

# Exercice 6

Trouver une expression équivalente à `a OU b` construite uniquement à partir
des opérateurs `NON` et `et`

On vérifiera à l'aide d'une table de vérité.

# Exercice 7

Donner la valeur des expressions booléennes suivantes :

```python
(1 > 2) and (3 < 5)
((4 - 7) >= 2) or (2 != 1 + 1)
a = 223
b = 455
a != (b // 2)
```

# Exercice 8

insérer le minimum de parenthèses dans les expressions suivantes pour
les égalités soient correctes

```python
2 + 3 * 5 + 4 == 21
5 + 2 * 3 + 4 == 25
4 + 5 * 2 + 3 == 29
```


# Exercice 9

La clé de vérification utilisée en France pour les numéros de sécurité sociale
est égal à 97 moins le résidu modulo 97 du nombre formé par les autres chiffres
: c'est-à-dire que la clé est l'unique entier entre 01 et 97 tel que la somme
de la clé avec le reste du numéro fasse un entier divisible par 97.

Nous allons traduire ceci en Python

1. Voici le numéro de sécurité sociale de JP : `1 81 10 59 340 223`.
    Calculer sa clé de sécurité à l'aide d'une calculatrice.
2. Proposer une expression de la clé de sécurité.
3. Écrire cette expression en Python en supposant que le numéro est noté `numero`

    ```python
    numero = 1811059340223
    cle = ???
    ```

4. Proposer une expression booléenne qui soit vraie si `cle` est bien
    la clé de sécurité de `numero` et fausse sinon.

