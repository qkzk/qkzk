---
author: qu3nt1n
date: 2017-01-19 17:33:18+00:00
draft: false
title: 'Internet of Objects : IoT'
bookCollapseSection: true
weight: 101

---

Brouillon rapide




# L'internet des Objets




Révolution ou mirage ? Les objets arrivent sur internet et il est maintenant possible pour tout un chacun de contrôler de nombreuses fonctions de son domicile depuis internet.

Le principe est le suivant : un objet (caméra, thermostat, cafetière, volet électrique etc.) est muni d'un ordinateur mignature ou simplement d'un micro contrôleur avancé intégré dans un réseau local.
Généralement un ordinateur du domicile contrôle ces différents objets et publie leurs états à la fois localement et online.

Les objets sont commandés par cette machine en fonction de scripts automatisés (pour maintenir la température entre certaines valeurs quand un des téléphones portables est raccordé au wifi par exemple) ou de manière active (pour commander l'ouverture d'un portail depuis son véhicule et désactiver l'alarme).

Il est tout à fait possible de réaliser soi même de tels serveurs mais cela demande un niveau de compétence avancé et il vaut mieux commencer par la partie amusante : les objets eux mêmes.


## Exemple de plateforme IO : Adafruit IO


Adafruit conçoit et vend des objets connectés munis de capteurs ou de leds en tout genre. Ceux-ci s'intègrent généralement à un écosystème plus vaste (compatible raspberry, aduino, beaglebone, feather). Chaque objet s'accompagne d'une librairie de programmes développés par adafruit et qui facilitent le développement par l'utilisateur.



 Ils proposent aussi une plateforme IO qui réunit plusieurs avantages :
 Elle est gratuite (tant qu'à faire)
 Elle est - relativement - simple d'emploi. Un minimum de Python suffit, par exemple
 Elle s'intègre bien à leurs produits (là aussi, on s'y attendait)
 Adafruit propose des tutoriels assez clairs pour commencer à développer et utilisant des objets courants

Découvrir Adafruit IO

[




 Your browser does not support the video tag.

 __
](/assets/24612)



## Par où commencer ?


Survoler ces quatre tutoriels de présentation : [Addafruit IO Basics](https://learn.adafruit.com/series/adafruit-io-basics).

Ensuite vous pouvez, dans un même dashboard, intégrer une camera, un bouton permettant d'allumer un led, un affichage d'une valeur numérique (simulant, par exemple une température)



Quelques petits projets pour prendre les choses en main



 	  1. Bouton sur Ada IO qui allume un led
Il deviendra notre système d'ouverture de volets roulants, de porte de garage ou autre...
 	  2. Etat d'un bouton poussoir : chaque fois qu'on presse un bouton fermant un circuit, l'état est reflété sur Ada IO.

On l'intégrera dans un système d'alerte d'ouverture de porte. Un aimant posé à une porte ferme un circuit électrique quand la porte est close. A son ouverture, le circuit est ouvert. L'information est transmise à Ada IO qui affiche donc quand quelqu'un est entré.
 	  3. Afficher une valeur numérique sur Ada IO. Dans un premier temps un simple input python fera l'affaire. A chaque saisie par l'utilisateur, celle-ci apparaît sur adaIO.
A terme, cela deviendra notre affichage de température intérieure
 	  4. Camera avec détection de mouvements. Une camera (webcam ou raspberry) diffuse un stream local et envoie des images à AdaIO. cf [Adafruit NoIO Camera](https://learn.adafruit.com/cloud-cam-connected-raspberry-pi-security-camera/pi-camera-setup?view=all)



## Des alertes mails


Intégrer à vos scripts Python des systèmes d'alerte par mail écrivant à l'aide d'une adresse gmail à cette même adresse (je vous conseille d'en créer une à l'occasion plutôt que d'employer la votre - c'est moins dangereux pour vos données personnelles et moins pénible à débugguer si vous envoyez 200 mails par mégarde...).
Par exemple : à chaque pression du bouton, chaque fois que la valeur numérique saisie (penser : température) sort d'une fourchette préétablie.


## Vers un système de Domotique


Vos projets sont incomplets tant qu'ils ne sont pas capables d'être contrôles sans un ordinateur. Le gros morceau sera donc de développer une interface simple permettant d'afficher et de contrôler vos appareils.

_to be continued..._
