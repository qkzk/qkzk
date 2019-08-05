---
title: NN - partie 3
author: qu3nt1n
date: 2019-05-04 11:17:30+00:00
draft: false
type: docs
weight: 1
---

_Remarque - Août 2019 -_ Pour l'instant le développement de cette partie est en pause.

Le projet complet fonctionne mais est largement plus difficile que je ne l'avais imaginé.

Tant que je ne serai pas parvenu à un niveau de simplification acceptable, j'en resterai là.

---

# 3 - Classification de chiffres manuscrits à l'aide d'un réseau de neurones

L'objectif de cette partie est de vulgariser ce [long article de ML](http://adventuresinmachinelearning.com/neural-networks-tutorial/)

Cet article implémente un réseau de neurone depuis 0 après avoir expliqué la majorité des concepts sous-jacents. L'objectif est de résoudre un problème fondateur : la classification de chiffres écrits à la main.

Les articles et cours d'introduction au ML sont nombreux. Celui-là présente de nombreux avantages :

1. Il fonctionne (c'est important).
2. Les code est relativement clair et ordonné
3. Les données sont facilement accessibles
4. Il n'utilise pas énormément de librairies toute faite
5. Il contient une grande partie des explications mathématiques sur le sujet

Mais aussi quelques inconvénients majeurs pour mes objectifs :

1. Cela reste difficile...
2. et long,
3. Une partie de la magie est cachée dans l'emploi de `numpy` et `sklearn`
4. Les résultats ne sont pas immédiatement transposables... une fois les mécanismes compris, on écrit la même chose en quelques lignes dans une librairie dédiée.

### Voici ce que je suis parvenu à faire pour l'instant :

1. Reproduire le code et le faire fonctionner (c'est le point de départ)
2. Comprendre les maths qui sont derrière (sinon difficile de vous les expliquer...)
3. Enlever complètement la librairie `sklearn` pour détailler ce qu'elle fait. _Enlever `numpy` est_ possible _mais rendra le programme extrêmement lent... Les calculs devront être programmés à la main, sûrement avec des boucles partout et on devra sacrifier trop de choses pour terminer en un temps raisonnable._

et pas grand chose d'autre pour l'instant.

### Le projet à l'heure actuelle

Vous trouverez plus bas le résultat en l'état (sans relecture.)

Téléchargez les données, modifiez convenablement `DATAPATH` et cela devrait fonctionner.

Installez `numpy` avec `$ pip install numpy` si nécessaire.
---

Les données sont hébergées [ici](https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes)



Le code complet.

{{< gist qkzk 4c735dee6cd362febbd7abc555deb420 >}}


### TODOLIST

Que reste-t-il à accomplir ?

* Améliorer le code, le détailler, découper la backpropagation
* Traduire l'article, le découper en étapes raisonnables
* Transposer le code vers un notebook pour le rendre plus digeste et "non bloquant" : on doit pouvoir avancer sans rien comprendre d'une étape, les maths doivent être vaguement optionnelles
* déterminer les parties qui doivent-être réalisées par les élèves et celles que je vais donner
* Faire tout ça...
