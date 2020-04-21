---
title: Travaux pratiques
author: qkzk
weight: 2
---

### pdf : [pour impression](/uploads/docnsitale/recursivite/pdf/3_td.pdf)

# Programmer les exercices sur la récursivité.

Je ne reprends pas tous les énoncés.

Ils sont disponibles [ici](../td) et [là](/uploads/docnsitale/recursivite/pdf/2_exo-recursivite.pdf)

## Exercices directs

_Ils ne demandent pas de revoir toutes les notions_

1. somme, produit, puissance, (Euclide ?)
2. coloriage de pixels
3. palindrome

## Exercices classiques

_plus difficiles_

4. chiffres romains (difficile)
5. listes récursives (donner les fonctions de base)

    Dans cet exercice on utilisera des listes Python

    MAIS on doit se limiter aux fonctions suivantes :

    ```python
    # on suppose donc que l'on ne dispose que des fonctions
    LISTE_VIDE = []
    def cree_liste(tete, reste):
        return [tete] + reste

    def tete(liste):
        return liste[0]

    def reste(liste):
        return liste[1:]

    # on peut donc définir le prédicat
    def est_vide(liste):
        return liste == LISTE_VIDE
    ```

    * `somme`, `last`, `concat`, `map`,
    * (`shuffle` difficile)

7. tour de Hanoï avec exemples

## Exercices d'approfondissement

8. tri par insertion
9. permutations
10. rencontres du championnat
11. ours en cage
