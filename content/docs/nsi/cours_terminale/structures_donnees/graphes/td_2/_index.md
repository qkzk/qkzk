---
title: "TD 2"
bookCollapseSection: true
weight: 11

---

pdf: [pour impression](/uploads/docnsitale/graphes/9_td_basique.pdf)

**Compétence :** _Savoir représenter une situation sous la forme d'un graphe._

# Exercice 1

On souhaite organiser un tournoi de football avec 4 équipes (numérotées de 1 à 4).
Chaque équipe rencontre une seule fois toutes les autres.

1. Représenter la situation sous la forme d'un graphe
2. Combien d'arêtes possède-t-il ? En déduire le nombre de matchs au total pour
    ce tournoi
3. Ce graphe est-il connexe ?
4. Ce graphe est-il complet ?

**Compétence :** _Savoir analyser une situation mise sous la forme d'un graphe._

# Exercice 2

Un club de tennis doit sélectionner deux joueurs parmi quatre pour représenter
le club à un tournoi national. Les quatre joueurs sont notés A, B, C et D.
Pour réaliser la séléction le club organise des matchs : chaque joueur rencontre
les trois autres :

_Règle :_ 

* Tout match gagné donne un point,
* Tout match perdu enlève un point.

Les joueurs sélectionnés sont les joueurs ayant obtenu le plus grand nombre
de points. On donne le résultat sous la forme d'un graphe orienté

![graph_000.svg](graph_000.svg)


Le sens de l'arc `A -> B` indique le joueur `A` a battu le joueur `B`

1. Donner le nombre de points de chaque joueur
2. En déduire les joueurs sélectionnés

# Exercice 3

Pour accéder à sa messagerie, Antoine a choisi un code qui doit être reconnu
par le graphe étiquetté suivant les sommets `1-2-3-4`. Une succession des lettres
constitue un code possible si ces lettres se succèdent sur un chemin du graphe
orienté ci-dessus en partant du sommet 1 et sortant au sommet 4.

![graph_001.svg](graph_001.svg)


1. Parmi les trois codes suivants, quels est (sont) le(s) code(s) reconnu(s)
    par le graphe.

    * SUCCES
    * SCENES
    * SUSPENS

2. Quelle est la taille du plus petit code possible ? Ce code est-il unique ?
3. Y a-t-il une taille maximale ?

**Compétence :** _Représenter sous la forme d'une matrice d'adjacence ou sous
la forme d'une liste d'adjacence._

# Exercice 4

On donne le graphe suivant :

![graph_002.svg](graph_002.svg)


1. Donner une représentation de ce graphe au moyen d'une liste d'adjacence.
2. Donner une représentation de ce graphe au moyen d'une matrice d'adjacence.

# Exercice 5

**Compétence :** _Représenter un graphe à partir d'une matrice d'adjacence ou à
partir d'une liste d'adjacence._

1. Donner le graphe associé à la matrice d'adjacence `A` ci-dessous :


    $$\left(\begin{matrix}
    0 & 0 & 1 & 0 & 0 & 0\\\
    1 & 0 & 0 & 1 & 0 & 0\\\
    1 & 1 & 0 & 0 & 1 & 0\\\ 
    0 & 0 & 1 & 0 & 0 & 0\\\ 
    0 & 0 & 0 & 0 & 0 & 1\\\ 
    0 & 0 & 1 & 0 & 0 & 1 
    \end{matrix}\right)$$

    **Note :** On notera les sommets `A, B, C, D, E` et `F`

2. Donner le multigraphe associé à la matrice d'adjacence `B` ci-dessous :

    $$\left(
    \begin{matrix}
    0 &  3 &  0 &  1\\\ 
    3 &  1 &  2 &  0\\\ 
    0 &  2 &  2 &  0\\\ 
    1 &  0 &  0 &  0 
    \end{matrix}
    \right)$$

    **Note :** On notera les sommets `A, B, C` et `D`

# Exercice 6

1. Donner le graphe associé à la liste des prédécesseurs ci-après ;

    | Sommet | Liste des prédécesseurs |
    |:------:|:-----------------------:|
    |   $A$  |         $(E, F)$        |
    |   $B$  |      $\varnothing$      |
    |   $C$  |         $(A, F)$        |
    |   $D$  |         $(D, F)$        |
    |   $E$  |      $\varnothing$      |
    |   $F$  |         $(B, c)$        |


2. Donner le graphe associé à la liste des voisins ci-après

    | Sommet | Liste des voisins |
    |:------:|:-----------------:|
    |   $A$  |    $(C, D, E)$    |
    |   $B$  |    $(C, D, E)$    |
    |   $C$  |    $(A, B, D)$    |
    |   $D$  |   $(A, B, C, E)$  |
    |   $E$  |    $(A, D, B)$    |

# Exercice 7 - Bilan

On considère un groupe de dix personnes présentes sur un réseau social,
le tableau suivant indique les paires de personnes qui ont une relation
d'amitié dans ce réseau social.

| $i$ | Amis de $i$ |
|-----|-------------|
| 1   | 3, 6, 7     |
| 2   | 6, 8        |
| 3   | 1, 6, 7     |
| 4   | 5, 10       |
| 5   | 4, 10       |
| 6   | 1, 2, 3, 7  |
| 7   | 1, 3, 6     |
| 8   | 2           |
| 9   |             |
| 10  | 4, 5        |

1. Représenter cette situation par un graphe dans lequel une arête montre
    le lien d'amitié.
2. Ce graphe est-il connexe ? Si non donner ses composantes connexes.
3. L'adage "les amis de nos amis sont nos amis" est-il vérifié ? Si non,
    que faudrait-il faire pour que ce le soit ?

