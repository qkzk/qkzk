---
author: qu3nt1n
date: 2016-07-01 13:29:12+00:00
draft: false
title: Papy Panic (RPI, Python)
weight: 7
---

# Raspberry : Panic Button




### Projet de base


Dans ce projet vous utliserez le raspberry pi afin de créer un bouton d'alerte pour les séniors.

Le senior garde sur lui une radiocommande équipée d'un bouton qu'il presse en cas de danger (chute dont il ne parvient pas se relever).
Cette radiocommande émet un signal capté par un recepteur radio connecté au raspberry Pi.
Celui-ci affichera alors l'information (leds, signal sonore etc.) et altera les secours via internet (ou autre)

![rpiModel-A](http://qkzk.xyz/wp-content/uploads/2016/07/rpiModel-A-300x208.jpg)
Ce projet a pour but d'explorer les possibilités du raspberry Pi en terme de domotique. Il peut-être adapté selon les besoins.



Des connaissances en electronique sont indispensables, voilà pourquoi il est réservé aux élèves faisant S.I. Il faudra sans doute se rapprocher d'un enseignant de S.I. pour obtenir un peu d'aide.



C'est à mes yeux un projet difficile. Quand je l'ai terminé la première fois c'était pour un usage personnel et j'étais certain de ne jamais le proposer aux élèves.



Le matériel du projet est donc composé :



* Du raspberry
* D'une [ commande radio](https://www.adafruit.com/products/1392) style bip de garage






Your browser does not support the video tag.




* D'un [récepteur radio](https://www.adafruit.com/products/1096) :
![1096-05](http://qkzk.xyz/wp-content/uploads/2016/07/1096-05-300x225.jpg)

* De la connectique nécessaire pour connecter tout ce beau monde et afficher des infomations (breadboard, jumpers, boutons, leds).



### Cahier des charges





* Utiliser le rapsberry convenablement, installation, raccordements
* Utiliser le gpio pour afficher une information via une led
* Presser un bouton, allumer une led (sans transition par le raspberry)
* Presser un bouton, déclencer un événement dans un script sur le raspberry, allumer une led
* Lancer un script automatiquement, le programmer sous windows, le transmettre au rapsberry
* Dessiner puis réaliser le circuit électronique reliant le raspberry et le récepteur radio
A cette étape le raspberry doit être accessible sans écran, uniquement via le réseau en SSH. Vous devez être capable d'y transférer vos fichiers au fur et à mesure.
* Connecter le recepteur radio au raspberry, lui transmettre un signal
* Ecrire le script qui écoute l'événément et transmet les informations
* Envoi automatique de mails (ou autre) via Python, déclenchés par le clavier
* Idem, déclenchés par un bouton
* Idem, par la radio
* Mettre de l'ordre dans tout ça...






### Extensions








* Créer une boitier de protection de tous les éléments en impression 3D (Hors de mon champ d'action...).
* Utiliser le raspberry à d'autres fins : récupérer la météo et l'afficher, afficher le contenu d'un calendrier, rappeler qu'il faut prendre des médicaments sur un écran etc.
