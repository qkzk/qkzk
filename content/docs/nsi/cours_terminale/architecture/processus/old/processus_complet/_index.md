---
subtitle: "Ordonnancement des processus"
weight: 1

---


# Les processus

**Objectifs**

Pour permettre le fonctionnement d'un ordinateur, de nombreuses tâches ou
applications doivent être exécutées simultanément, par le système
d'exploitation et les différents utilisateurs.

Notons aussi qu'une même application (programme) doit pouvoir s'exécuter
plusieurs fois simultanément (par plusieurs utilisateurs par exemple), ou que
plusieurs applications doivent pouvoir accéder à un même périphérique sans
conflit.

Pour permettre cela, le système d'exploitation génère de nombreux processus,
puis gère leur exécution.

**Concept :**

> Un processus est un programme en cours d'exécution.
>
> Les notions de programme et de processus sont différentes : le même programme
> exécuté plusieurs fois (dans le temps ou par plusieurs utilisateurs
> simultanément) générera plusieurs processus.

Chaque processus possède en mémoire les instructions à exécuter et ses données.

## L'ordonnancement

Le système d'exploitation doit permettre à toutes les applications et tous 
les utilisateurs de travailler en même temps, c'est-à-dire donner l'impression
à chacun qu'il est seul à utiliser l'ordinateur et ses ressources physiques.
Cette gestion complexe des processus est réalisée par une partie spécifique
du noyau : **l'ordonnanceur.**

**Concept :**

> Comme une ressource (le processeur ou un périphérique) ne peut pas être
> partagée, c'est son temps d'utilisation qui va l'être ; le temps d'utilisation
> d'une ressource est partagé en intervalles très courts, pendant lesquels
> l'ordonnanceur l'alloue à un seul utilisateur.


L'ordonnanceur permet :

* de minimiser le temps de traitement du processus d'un utilisateur
* de garantir l'équité entre les différents utilisateurs
* d'optimiser l'utilisation de la ressource
* d'éviter les blocages.

Plusieurs algorithmes d'ordonnancement sont possibles, parmi les plus répandus
nous pouvons citer :

* le **tourniquet** : la ressource est affectée à chaque processus à tour
    de rôle. Pour l'exécuation simultanée des processus, c'est la rapidité
    de ce tour qui va donner l'impression à chaque utilisateur que son processus
    est seul à utiliser le processeur. Cette méthode ancienne a les avantages
    de sa simplicité, de sa rapidité de gestion et de sa robustesse.

    * Processus 1 : `z` instructions à réaliser
    * Processus 2 : `y` instructions à réaliser
    * Processus 3 : `t` instructions à réaliser

        Imaginons que `z < y < t`

    | Exécution par le microprocesseur            |
    |---------------------------------------------|
    | P1. instruction 1                           |
    | P2. instruction 1                           |
    | P3. instruction 1                           |
    | P1. instruction 2                           |
    | P2. instruction 2                           |
    | P3. instruction 2                           |
    | ...                                         |
    | P1. instruction `z`                         |
    | P2. instruction `z`                         |
    | P3. instruction `z`                         |
    | ...     (P1 a fini, P2 et P3 continuent...) |
    | P2. instruction `y`                         |
    | P3. instruction `y`                         |
    | ...     (P2 a fini, P3 continue...)         |
    | ...                                         |
    | P3. instruction `t`                         |

* La mise en place d'un système de **priorités** : l'ordre d'affectation
    de la ressource sera alors fonction de la priorité de la tâche. Cette
    méthode est très équitable, mais définition du niveau de priorité de la
    tâche doit être objective.

* La gestion du **premier entré, premier sorti** (FIFO : _First In, First Out_).
    L'exemple le plus évident de cet algorithme est la file d'impression des
    documents sur une imprimante.
* L'algorithme du "**plus court d'abord**" : très efficace pour satisfaire
    au mieux les utilisateurs, mais il n'est pas toujours simple d'évaluer
    le temps d'exécution d'une tâche avant son début.

Parallélement à l'évolution des performances des microprocesseurs,
l'ordonnancement est aussi un moyen d'amélioration de la rapidité de traitement :
des algorithmes récents, de plus en plus complexes ont est proposés.

# Les interblocages

Nous avons dits précédemment que des processus peuvent avoir besoin de la
même ressource.

Dans de nombreuses situations, deux processus (ou davantage) peuvent souhaiter
accéder à la même donnée sur le disque dur :

* Les deux processus ont uniquement besoin de lire la donnée : celle-ci est
    alors partagée, sans problème complexe.
* Les deux processus ont besoin de la donnée de manière exclusive, pour la
    modifier, par exemple.
* Les deux processus ont besoin de communiquer entre eux : l'un doit attendre
    un résultat de l'autre.

**Exemple 1**

Deux processus P1 et P2 ont tous les deux besoin de la même donnée D pour la
modifier, c'est-à-dire de manière exclusive. Le premier à y accéder est P1,
D lui est alloué par le système d'exploitation. Lorsque P2 souhaite accéder à
D, la ressource n'est pas disponible : P2 est alors bloqué jusqu'à la fin de
l'utilisation de D par P1.

**Exemple 2**

Deux processus P1 et P2 ont tous les besoin de deux données, D1 et D2.\
Chaque processus bloque une donnée et doit attendre d'avoir accès à la seconde
pour se terminer et les libérer.

Si la chronologie est la suivante :

* P1 bloque D1
* P2 bloque D2
* P1 attend D2
* P2 attend D1

Alors aucun des deux processus ne pourra avancer. C'est **l'interblocage**.
Rien ne pourra avancer sans une intervention extérieure.

Face à cette problématique la plupart des systèmes d'exploitation ont choisir
de ne pas essayer d'éviter les interblocages mais de les détecter s'ils
surviennent et de les solutionner.


