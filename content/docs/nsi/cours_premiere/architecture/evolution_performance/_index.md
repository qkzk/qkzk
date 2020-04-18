---
title: Evolution des performances
author: David Roche
theme: metropolis
weight: 14
---


## Évolution des performances

Pendant des années, pour augmenter les performances des ordinateurs, les
constructeurs augmentaient la fréquence d'horloge des microprocesseurs :
la fréquence d'horloge d'un microprocesseur est liée à sa capacité
d'exécuter un nombre plus ou moins important d'instructions machines
par seconde.

Gordon Moore (ancien PDG d'Intel) a énoncé plusieurs "lois" qu'on peut résumer
ainsi :

**Loi de Moore : tous les 18 mois, le nombre de transistor par processeur double**

![loi de moore](https://upload.wikimedia.org/wikipedia/commons/a/a4/Loi_de_Moore.png)

Cette prédiction est restée vraie pendant des décennies mais s'est heurtée à
des problèmes physiques insolubles.

![fréquence CPU](/uploads/docsnsi/architecture/aqa/img/freq_cpu.jpg)

évolution de la fréquence d'horloge du CPU dans le temps

À partir de 2006 environ, la fréquence d'horloge a cessé d'augmenter, pourquoi ?

À cause d'une contrainte physique : en effet plus on augmente la
fréquence d'horloge d'un CPU, plus ce dernier chauffe. Il devenait
difficile de refroidir le CPU, les constructeurs de microprocesseurs
(principalement Intel et AMD) ont décidé d'adopter
une nouvelle tactique.

## Évolutions récentes des processeurs : de multiples coeurs.

Augmenter le nombre de cœurs présent sur un CPU ! M

ais qu'est qu'un cœur dans un
microprocesseur ? Dans un microprocesseur, un cœur est principalement
composé : d'une UAL, de registres (R0, R1\...) et d'une unité de
commande, un cœur est donc capable d'exécuter des programmes de façon
autonome. La technologie permettant de graver toujours plus de
transistors sur une surface donnée, il est donc possible, sur une même
puce, d'avoir plusieurs cœurs, alors qu'auparavant on trouvait un
seul cœur dans un CPU. Cette technologie a été implémentée dans les
ordinateurs grand public à partir de 2006. Aujourd'hui (en 2019) on
trouve sur le marché des CPU possédant jusqu'à 18 cœurs ! Même les
smartphones possèdent des microprocesseurs multicœurs : le Snapdragon
845 possède 8 cœurs.

## Programmes capables de s'exécuter sur de multiples cœurs.

On pourrait se dire que l'augmentation du nombre de cœurs entraîne
obligatoirement une augmentation des performances du CPU, en fait,
c'est plus que complexe que cela : pour une application qui n'aura pas
été conçue pour fonctionner avec un microprocesseur multicœur, le gain
de performance sera très faible, voir même nul.

En effet, la conception
d'applications capables de tirer profit d'un CPU multicœur demande la
mise en place de certaines techniques de programmation. Il faut aussi avoir
conscience que les différents cœurs d'un CPU doivent se "partager"
l'accès à la mémoire vive : quand un cœur travaille sur une certaine
zone de la RAM, cette même zone n'est pas accessible aux autres cœurs,
ce qui, bien évidemment va brider les performances. De plus, on trouve à
l'intérieur des microprocesseurs de la mémoire "ultrarapide" appelée
mémoire cache (il ne faut pas confondre mémoire cache et registres). Le
CPU peut stocker certaines données dans cette mémoire cache afin de
pouvoir y accéder très rapidement dans le futur.

La mémoire cache ayant un coup assez important, la quantité présente au sein
d'un CPU est assez limitée, les différents cœurs vont donc devoir se
partager cette mémoire cache, ce qui peut aussi provoquer des
ralentissements (en fait il existe plusieurs types de mémoire cache
appelés L1, L2 et L3, chaque cœur possède son propre cache L1, alors
que les caches L2 et L3 sont partagés par les différents cœurs).

------------------------------------------------------------------------
