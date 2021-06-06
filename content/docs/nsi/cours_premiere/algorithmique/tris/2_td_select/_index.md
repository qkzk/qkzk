---
title: "TD - tri sélection"
weight: 2

---

### PDF : [Pour impression](./2_tris_td.pdf)

## Exercice 1

1. Faire tourner l'algorithme du tri par sélection présenté en cours sur le tableau `[5, 7, 3, 1, 9]`
2. Combien de comparaisons sont nécessaires pour trier ce tableau ?
3. Recommencer avec le tableau déjà trié `[1, 3, 5, 7, 9]`.
4. Gagne-t-on quelque chose à partir d'un tableau déjà trié ?

## Exercice 2

1. Proposer une version avec des indices, en langage naturel du tri par sélection.
2. Faire tourner votre version sur le tableau `[5, 7, 3, 1, 9]`
    
    Compléter le tableau suivant, on écrivant les éléments triés et non triés
    après chaque tour de la boucle principale.

    | Étape | Partie triée | Partie non triée  |
    |-------|--------------|-------------------|
    | 1     | `[]`         | `[5, 7, 3, 1, 9]` |
    | 2     |              |                   |
    |       |              |                   |
    |       |              |                   |
    |       |              |                   |
    |       |              |                   |
    |       |              |                   |
    |       |              |                   |

## Exercice 3 - Vérifier qu'un tableau est trié

On dispose d'un tableau de nombres, on souhaite vérifier s'il est trié par ordre
croissant.


```
Fonction est_triee(t: tableau de nombres)
    n: longueur du tableau
    est_trié = vrai

    Pour i allant de 0 à longueur - 2 faire

      si t[i] > t[i + 1] alors
          est_trie = faux
    renvoyer est_trie
```

1. Quelle est la signature de cette fonction ? Préciser le type de sa variable
  de retour.
2. Traduire cette fonction en Python.
3. La programmer et vérifier sur quelques exemples sa validité.
4. La boucle de la fonction parcourt toujours l'intégralité du tableau.

    a. Proposer un exemple pour lequel il n'est pas nécessaire de parcourir
        tout le tableau pour savoir qu'il n'est pas trié.
    b. Proposer une amélioration du coût de la fonction.
