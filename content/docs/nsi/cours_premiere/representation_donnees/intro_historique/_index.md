---
title:
- Introduction et historique
weight: 1
---



## pdf pour [impression](/uploads/docsnsi/donnees_qkzk_img/intro_historique_print.pdf) et [diaporama](/uploads/docsnsi/donnees_qkzk_img/intro_historique_slides.pdf)

# Comment stocker des informations dans une machine ?

## Une idée relativement récente



* Machine **à calculer** : Antiquité
* Machine pour **stocker de l'information** : XVIIIeme siècle.


## Historique sommaire

En 1725 on voit l'apparition des cartes perforées : feuilles de papier rigides sur lesquelles sont disposés des trous qui symbolisent des données.

On stockait, par exemple, les plans de conception de tricot jacquard

### ![Métier jacquard](/uploads/docsnsi/donnees_qkzk_img/metier_jacquard.jpg){width=60%}


## Technologies modernes


* _l'électromagnétisme_ (aimants) et de la mécanique (ça tourne): bande,
  cassette, disquette et disques durs pour le stockage.

* _de l'électronique pure_ pour la mémoire vive et la mémoire flash. $10^4$ fois plus rapide...

## Mémoire vive vs mémoire morte

* _mémoire vive_ RAM : non persistante. Perdue sans alimentation.
* _mémoire morte_ ROM : persistante. Écrite une fois, ne peut qu'être lue.
* _mémoire de masse_ : persistante. Sert au stockage. Réinscriptible.

Pourquoi utiliser la mémoire vive si on peut la perdre ? Parce que c'est plus
(beaucoup) rapide !

## Objectifs

Optimiser à la fois _l'espace en mémoire_ et _les temps d'accès_.

### ![Bandes de stockage](/uploads/docsnsi/donnees_qkzk_img/Computer_tapes.jpg){width=400px}

## Mémoire flash

Depuis 30 ans : mémoire flash, plus rapide, sans élément mécanique, peu gourmande en énergie mais coûteuse.


### ![Carte SD](/uploads/docsnsi/donnees_qkzk_img/sdcard.jpg){width=150px} ![Disque dur SSD](/uploads/docsnsi/donnees_qkzk_img/ssd.png){width=250px}

## Pyramide de la mémoire

On peut résumer ainsi :

* Rapide = coûteux = limité en espace
* Lent = économique = vaste en espace

## Pyramide de la mémoire

### ![Pyramide de la mémoire](/uploads/docsnsi/donnees_qkzk_img/PyramideMem.gif)

## Données : deux unités de mesure

Nous avons 10 doigts et comptons avec 10 chiffres.

En informatique on emploie un autre système pour représenter les nombres :

### les bits 0 et 1 et les octets

* 1 _bit_ : 0 ou 1. Unité minimale de symbole b, parfois bit.

* 1 _octet_ : paquet de _8 bits_. Symbole B (anglais pour Byte) ou o.

  1 octet peut donc représenter $2^8 = 256$ valeurs distinctes.

Pourquoi deux unités ? Parce que

Attention aux confusions !

## Données : ordre de grandeur

Préfixe   long               $10^n$      Exemple
-------   ----------         --------    --------------------------------------
kilo      milliers           $10^3$      $3,5$ kb = $3500$ bits
mega      millions           $10^6$      $1$ Mb = 1 million de bits = 125 kB
giga      milliards          $10^9$
téra      billions           $10^{12}$   $1$ TB = $8 \times 10 ^{12}$ b
péta      billiards          $10^{15}$



## Quelques exemples

| Objet                  	| Espace mémoire                                   	|
|------------------------	|--------------------------------------------------	|
| 1 lettre               	| 7 bits en ASCII                                  	|
| 1 page de texte        	| $3 \times 10^4$ bits                             	|
| Disquette 3.5"         	| $1,44$ MB = $1,2 \times 10^7$ bits               	|
| Disque dur en 1980     	| $20$ MB = $1,6 \times 10^8$ bits                 	|
| Bdd du WDCC            	| $5000$ TB = $4 \times 10^{16}$ bits              	|
| Trafic internet (2016) 	| $1.56\times 10^9$ TB= $1,25 \times 10^{22}$ bits 	|
| 1 gramme d'ADN         	| $1,8 \times 10^{22}$ bits                        	|

# Nombres en informatique.

## Pourquoi les bits de données ?

Partons de ce qu'on sait faire :

* On sait construire de très petits transistors.
* On sait les concentrer sur une petite surface.
* L'amélioration des technologies permet de concentrer l'information et la puissance de calcul.

Par exemple :

* 1971 : 2300 transistors dans un processeur 4004.
* 2014 : 2,6 milliards dans un core i7 d'intel.


Le choix d'utiliser l'électronique pour stocker l'information est une
_conséquence_ de notre capacité à calculer avec des portes logiques.

![Intel C4004 - 1971](/uploads/docsnsi/donnees_qkzk_img/Intel_C4004.jpg)
