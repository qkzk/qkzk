---
title: "Arbres - TD 2"
author: "qkzk"
weight: 3

---

### PDF : [pour impression](/uploads/docnsitale/arbres/td_arbres_fig.pdf)




**Compétence :** _Savoir décrire et caractériser un arbre ou un nœud._

# Exercice 1

On donne l'arbre suivant :

**arbre 1**


![graph_000.svg](graph_000.svg)


1. Déterminer pour cet arbre, sa racine, sa taille, sa hauteur, ses nœuds internes
    et ses feuilles
2. Pour le noeud 4, déterminer son père, ses frères, sa hauteur, sa profondeur.

# Exercice 2

On donne ci-dessous le tableau caractérisant un arbre :

| Noeud | Etiquette | Noeud du SAG | Noeud du SAD |
|:-----:|:---------:|:------------:|:------------:|
| 1     | `*`       | `2`          | `3`          |
| 2     | `+`       | `4`          | `5`          |
| 3     | `-`       | `6`          | `7`          |
| 4     | `3`       |              |              |
| 5     | `/`       | `8`          | `9`           |
| 6     | `8`       |              |              |
| 7     | `*`       | `10`         | `11`          |
| 8     | `4`       |              |              |
| 9     | `2`       |              |              |
| 10    | `2`       |              |              |
| 11    | `3`       |              |              |

1. Représenter l'arbre correspondant.
2. Quelle est la hauteur de cet arbre ?
3. Cet arbre est-il binaire, complet ?
4. Quel est le résultat de cette suite d'opérations mathématiques ?

**Compétence :** _Savoir évaluer quelques mesures sur les arbres binaires_

# Exercice 3

On donne l'arbre A suivant :

![graph_001.svg](graph_001.svg)


1. Calculer toutes les longueurs de cheminement.
2. En déduire toutes les profondeurs moyennes. On pourra essayer de les
    représenter sur l'arbre.

**Compétence :** _Identifier des situations nécessitant des structures de données
arborescentes._

# Exercice 4

On donne ci-dessous une liste aléatoire de 14 nombres entiers :

```
25 60 35 10 5 20 65 45 70 40 50 55 40 15
```

Construire (dans l'ordre de la liste) l'arbre binaire de recherche associé.

**Compétence :** _Savoir raisonner avec un type abstrait_

# Exercice 5

On donne la suite d'instructions suivantes :

```python
A = creer_arbre(2, creer_arbre_feuille(4), creer_arbre_feuille(3))
B = creer_arbre(5, creer_arbre_vide(4), creer_arbre_feuille(6))
C = creer_arbre(1, A, B)
```

1. Représenter la situation sous forme d'un arbre
2. Donner l'arbre correspondant à l'instruction :

    ```python
    T = SAD(C)
    ```

3. Quelle est la valeur retournée par l'instruction suivante :

    ```python
    r = racine(B)
    ```
