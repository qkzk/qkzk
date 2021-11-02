---
author: qu3nt1n
date: 2019-07-01 13:01:10+00:00
draft: false
title: Smart City
bookCollapseSection: true
weight: 9
---


# SmartCity : le lampadaire connecté

_Projet de réalisation d'un objet connecté et de son interface homme machine_

![smart city](https://images.itnewsinfo.com/lmi/articles/grande/000000065177.jpg)

## Présentation

La ville de Nantes est parmi les plus avancée en terme de nouvelles technologies
responsables.

Elle s'est récemment équipée de lampadaires connectés remplissant un triple
objectif :

* assurer la sécurité des habitants,
* limiter le gaspillage énergétique
* limiter la pollution lumineuse

L'objectif de ce projet est de réaliser un prototype complet remplissant le
cahier des charges.

## Lampadaire connecté

Plutôt que d'éclairer toute la nuit inutilement, le lampadaire connecté s'adapte
aux circonstances (luminosité, présence d'un piéton, horaire) pour décider
de s'allumer ou de s'éteindre.

## Principe du projet

Le but de ce projet est de réaliser un prototype de lampadaire connecté
utilisant un raspberry pi pour l'informatique embarquée, des capteurs
(luminosité, présence) et des relais pour les actionneurs.

L'ordinateur embarqué doit pouvoir être piloté sur place (via une console) et à
distance (via un serveur web) et doit régulièrement envoyer des messages avec
son état (bon fonctionnement, horaires d'allumage etc.)

En temps normal le lampadaire s'allume et s'éteint selon trois critères :

l'horaire (de 5h à 8h et de 20h à 0h), la luminosité ambiante et la présence
d'un piéton.

Certaines règles président sur d'autres (s'il fait jour, il est éteint) et
ces règles doivent pouvoir être ajustées à distance et sur place.

## Cahier des charges

![Candélabre connecté](https://atelier.bnpparibas/uploads/archives/_illustrations/2016/09/Bouygues%20Citybox.jpg)

### Objet connecté :

* ordinateur embarqué : RPI
* capteur de luminosité
* capteur de présence
* actionneurs (relais ?)
* éclairage via des leds (nous n'allons pas éclairer le lycée...)

### Maquette :

Une maquette physique d'une installation _peut_ être réalisée en :

* légo,
* modèle en carton,
* impression 3D...

### Logiciel de gestion

* Lit ses réglages dans une fichier de configuration et adapte son comportement,
* Possible de se connecter et d'exécuter un script Python qui demande à
  l'utilisateur un réglage et modifie le fichier de configuration,
* Un serveur web (Python + Flask) propose plusieurs pages
  * réglages modifiables
  * données des capteurs sur des courbes dans le temps
  * extraction de données des tables via un formulaire
* données (stockées dans une bdd sqlite3). Elle contient plusieurs tables
  présentant les allumages et extinctions ainsi que la raison. Les données des
  capteurs sont régulièrement enregistrées.


### Comportement du  lampadaire

![candelabres](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOPreVtU2RtuYy0wA2fjHNixRNuBPTSH7r4wMnMfDpZidxkOGc2w)

Les règles pour l'allumage et l'extinction varient selon 4 périodes dans le
temps :

* matin,
* journée,
* soir,
* nuit.

Pour simplifier la présentation nous allons supposer que le jour se lève à 6h
et qu'il fait nuit à 21h. Ces horaires seront adaptés selon la date.

* Allumage permanent : matin (5h - 8h) et soir (20h - 0h)
  * si la luminosité est bonne, le lampadaire peut retarder son allumage ou
  avancer son extinction
  * il peut sortir de son mode éteint si la luminosité diminue

* Nuit (0h - 5h)

  * réagit à la présence d'un piéton pour s'éclairer.
  * Éventuellement un lampadaire allumé peut communiquer avec ses voisins
    et éclairer une zone plus vaste (toute une rue, zone autour du piéton)

* Jour (5h - 20h)

  * le lampadaire est éteint.

## Extensions

Elles sont infinies...

![Extensions](https://i.pinimg.com/736x/61/6c/bf/616cbf5b768a6b2744f2207134cdb51d.jpg)

## Source

* [Vidéo](https://youtu.be/JC2VCzYAnC8?t=2159) ayant inspiré ce projet
* Article les SmartCities et [Nantes](https://leshorizons.net/2019/02/28/exemples-smart-city-france/)
