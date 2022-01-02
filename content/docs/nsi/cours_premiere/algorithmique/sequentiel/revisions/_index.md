---
title: "Révisions"
theme: metropolis
weight: 3

---

[pdf](./ds3_revisions.pdf)

# Parcours séquentiels et tableaux

1. On considère la fonction suivante :

    ```python
    def minimum(tab: list) -> int:
        """Renvoie le plus petit élément de tab"""
        mini = tab[0]
        for elt in tab:
            if elt ...
                  ...
        return ...
    ```

    1. Compléter la fonction
    2. On considère `tab = [3, 2, 4, 5, 1]`. Quel donner la valeur `elt` après chaque tour de la
        boucle lorsqu'on exécute `minimum(tab)`.
    3. Qu'est-ce qu'un **invariant** de boucle ? Qu'un **variant** de boucle ?
    4. Dans quel type de boucle peut-on se passer d'un variant ? Pourquoi ?
    5. Proposer un invariant de la boucle de la fonction `minimum`

5. On a enregistré une image noir et blanc dans un tableau à deux dimensions `image`.

    Le noir est modélisé par la valeur 0 et le blanc par la valeur 1.

    ```python
    image = [ 
        [1, 0, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
    ]
    ```

    a. Quelle est la valeur de `image[1][2]` ?
    b. Quelle instruction saisir pour modifier la dernière ligne et la remplacer par `[1, 1, 0, 0]` ?
    c. Écrire le code d'une fonction `negatif` qui prend en paramètre un tableau à 2 dimensions
        représentant une image et renvoie son négatif.

        En voici un exemple d'utilisation :

        ```python
        >>> negatif(image)
        [
            [0, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 0],
        ]
        ```

        Attention, votre fonction doit accepter des images de toutes dimensions pas seulement 4x4.

