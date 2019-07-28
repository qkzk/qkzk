---
author: qu3nt1n
date: 2016-07-01 13:26:56+00:00
draft: false
title: Vidéo Surveillance (RPI, Python)
weight: 12
---

# Raspberry : Camera




### Projet de base


Avant de commencer cette description, un petit rappel à la [loi](https://www.service-public.fr/particuliers/vosdroits/F2517) :
**_ L'installation de caméras par (...) des personnes de droit privé (...) n'est possible sur la voie publique ou dans des lieux ou bâtiments ouverts au public qu'après obtention d'une autorisation préalable._**

Dans ce projet vous utiliserez le raspberry et sa caméra pour surveiller automatiquement un lieu.

![camera-module](http://qkzk.xyz/wp-content/uploads/2016/07/camera-module-300x169.png)

Des événements peuvent déclencher la surveillances et l'enregristrement des données : détection de mouvement, signal émis à distance.

![mounted_sm](http://qkzk.xyz/wp-content/uploads/2016/07/mounted_sm-300x235.jpg)


Il sera possible d'afficher sur un autre ordinateur ce que voit la caméra en temps réel.
Le tout sera piloté par un script python qui se chargera au lancement.
On pourra aussi commander au raspberry la prise de timelapse.


### Cahier des charges





 	  * Utiliser le rapsberry convenablement, installation, raccordements...
 	  * Raccorder sa caméra, prendre une photo, filmer, exporter les données automatiquement
 	  * Controle du raspberry à distance via ssh
A cette étape le raspberry doit être accessible sans écran, uniquement via le réseau en SSH. Vous devez être capable d'y transférer vos fichiers au fur et à mesure.
 	  * Envoyer un ordre au raspberry et le faire exécuter un script Python
 	  * Envoyer un ordre : prendre une photo, l'exporter
 	  * Envoyer un ordre : filmer, arrêter, encoder, exporter.
 	  * Utiliser le capteur de mouvement
 	  * Créer un timelapse
 	  * Mettre de l'ordre dans tout ça...



### Extensions





 	  * Créer un boitier imprimé en 3D pour le raspberry et sa caméra. Hors de mon champ d'action.
 	  * Visiophone (difficile).
 	  * Piège caméra d'observation d'oiseaux (alimentation externe, déclencheur automatique, transfert via wifi etc.).



### Un autre exemple de projet : Console de jeu Donkey Kong


Déjà fait trois fois, un peu marre perso...
