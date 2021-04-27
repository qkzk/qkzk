---
author: qu3nt1n
date: 2017-06-14 12:55:50+00:00
draft: false
title: Domotique et raspberry pi
weight: 3
---




#### **Ce projet est TRÈS complexe. **




#### **Il n'est envisageable que si vous maitrisez deja l'electronique (un minimum), le raspberry, le réseau, Python et l'HTML.**


Deux raspberry (au moins), un serveur html, une console de contrôle.

Elle comporte plusieurs raspberry (ou arduino) contrôlant des capteurs / sorties (mouvement, distance, température, humidité, pression atmosphérique, photorésistance, servomoteur, camera, lecture de badge nfc, contrôle de relais etc.) qui communiquent avec un serveur.



1. Chaque raspberry fera donc tourner un ou deux scripts python et éventuellement motion (pour les cameras).
On peut découper le script ainsi : relevés locaux, communication via mqtt avec le serveur.
2. Le serveur est une autre machine (raspberry, serveur classique etc.) qui contient trois composants principaux :

  * un **broker** mqtt (= serveur mqtt) qui récupère les informations et les renvoie. Une fois installé correctement il n'y a plus rien à faire. Il récupère et transmet tout seul.
  * un serveur python qui récupère les informations transmises par le broker et les intègre à une base de donnée mySQL : **mqtt_to_sql.py**
  * un serveur html qui lit ces informations, les publie (graphiques, intégration de caméra, boutons, sliders, stream video de la camera) : **display_data.py
**Le tout sera donc présenté à l'aide d'un serveur html tournant en python avec flask. Il comportera au moins une page, idéalement une par composant.
Il sera possible d'afficher un graphe comportant les derniers relevés (crée en javascript)


3. un client html peut alors se connecter au serveur et lire/interagir avec les données.

![](https://docs.google.com/drawings/d/1yh0YsJq3fJedEdVh2gFhUGG2uveA1G_Ni7adSlxvHLI/pub?w=480&h=360)



## Quelques informations sur les technologies employées




### MQTT


La communication entre les raspberry / arduino et le serveur se fera à l'aide du protocole MQTT (qui encapsule le websocket et donc tcp : le réseau classique).
L'avantage de MQTT est immense : le serveur s'installe tout seul en ligne de commande et les tutoriels sont très simples. Une fois installé il ne nécessite AUCUNE interaction, AUCUN réglage. On peut s'abonner aux topic sans utiliser de script python et s'assurer que l'information lui parvient correctement. On peut simuler un envoi d'information en ligne de commande.
S'abonner, envoyer un message, réagir à un message sont les seules fonctions qu'il faut mettre en place. Elles sont déjà présentes dans les tutoriels python et fonctionnent parfaitement.

![](https://docs.google.com/drawings/d/1MCNtAM5uHbxD2hg8GElfghhRWlgru9VMOOPVm684Zpo/pub?w=480&h=360)


Le principe est le suivant.



1. Le **collecteur** (un script python sur le serveur - ou ailleurs) s'abonne à un **topic** (exemple temp) sur le broker. Notons simplement **MQTT SUB "temp".
Cette étape ne doit être faite qu'une seule fois.**
2. le **publieur** (un script python sur le raspberry ou autre) publie un message sur ce topic (temp) au **broker**. Notons **MQTT PUB "temp"** : 24 (il fait 24°C)
3. Le **broker** relaie cette information au **collecteur** intéressé par ce topic. **MQTT msg "temp" 24.
**Les prochains messages du topic "temp" seront envoyés de la même manière.

La transmission de l'information est assurée par le broker il n'y a rien d'autre à faire. MQTT fonctionne presque nativement sous linux et donc le raspberry et sous arduino.

On pourra envisager de faire transiter une information entre un arduino déconnecté du réseau et un raspberry via des modules nrf24l01+ qui utilisent des connections radio.


### **Raspberry  / Arduino**


Chaque raspberry / arduino permet simplement



* soit de relever une mesure et de la publier au broker en utilisant MQTT
* soit de streamer une vidéo de surveillance
* soit d'agir avec un composant (servo moteur à faire tourner, affichage LCD, allumage d'une led, activation d'un relais).



### Serveur web


Ainsi qu'il a été dit plus haut, deux scripts doivent être développés pour cette machine.



* Le collecteur qui s'abonne au broker mqtt, reçoit les infos et les stocke dans une bdd. Son travail est simple mais crucial.
* le serveur web qui récupère les infos depuis la bdd et les publie dans une page web
Celle-ci s'accompagne de graphiques crées en javascript permettant d'afficher les informations récupérées.
Des boutons permettant d'agir seront présentés. La pression de l'un d'eux enverra une information au broker. Le raspberry/arduino concerné devra réagir à cette action.



### SQLITE


C'est un système de gestion de base de donnée SQL. Disons simplement qu'il permet de stocker et de lire des données triées proprement. D'en relever une ou plusieurs simultanément et de créer des associations entre elles.
Nous n'exploiterons qu'une infime partie de ce que les bases de données proposent. SQLITE a été retenu pour ce projet car il est très documenté. Toutes les bases de données feraient l'affaire mais SQLITE réunit 2 qualités : il ne nécessite pas de réseau et il est très documenté.
Nous allons donc créer une table par type de mesure (température, humidité, pression, ouverture/fermeture d'un interrupteur...).
Un script Python va créer la base, la table et la remplir au fur et à mesure.

![](https://docs.google.com/drawings/d/1kDaEtT5TCSBqCZC-vfEZsrwY__ZvIfFa-z61pMlNmcM/pub?w=480&h=360)



### Flask


Il existe une foultitude de serveur html et flask est une solution minimaliste fonctionnant en Python, donc simple à prendre en main. Le principe est de créer un serveur et de lui décrire le contenu de chaque adresse possible.
Exemple : un client se connecte à la racine : "http://exemple.com/"
On lui envoie ce qui correspond à "/" qui est décrit dans le script. Par exemple le résultat d'une fonction qui affiche "Hello World!". Et voilà.

On peut bien sûr faire mieux et créer des modèles (templates).
Un modele est un fichier html classique comportant des balises {{ }} qui présentent des variables.

Le script python va donc faire 3 choses :



1. relever dans la bdd l'info nécessaire (Ex : la dernière température). Requete SQL (simplifiée) 'last temp' - reponse SQL date: '16:01', temp: '24'.
![](https://docs.google.com/drawings/d/11-8ANtjig7DWQXtY06OfVEzGaJqVq0-IOaxg8MC483g/pub?w=480&h=360)

2. l'intégrer dans le code html de la page (A 16h01 et la température était de 24°C )
3. envoyer cette info au client html qui verra alors :
A 16h01 et la température était de 24°C

Arrêtons ici la description de cette partie. Je ne détaille pas l'envoie d'un ordre depuis le client html.
Exemple : bouton "allumer la lumière". L'information circule alors dans l'autre sens. Depuis le serveur flask vers les raspberry / arduino qui contrôlent.


## Cahier des charges





1. Etablir un petit protocole de notation des informations. Ainsi vous pourrez ensuite simuler leur parcours et vous serez certain qu'elles seront interprétées correctement.
2. Mettre en place une simulation d'envoi d'information à un broker MQTT
3. Stocker des informations (factices ou réelles) dans une bdd sqlite après les avoir reçues du broker.
4. Flask. Afficher une page statique sans template. Créer un template statique. Créer un template utilisant une variable. Lire une info dans une variable et l'afficher sans template. Lire une info dans la bdd et l'afficher sans template. Lire une info dans la bdd et l'afficher dans un template.
5. Capteur RPI/Arduino. Envoyer une info via MQTT. Mettre en place l'envoi régulier d'un relevé au script qui stocke les données via MQTT.
A cette étape le projet sera complet mais minimaliste.
6. Graphique. Relever les 100 dernières températures et les afficher dans un graphique. Ajouter l'humidité sur le même graphique. Le rendu du graphique est réalisé par le client afin d'économiser les ressources, il est donc fait en javascript.
7. Donner des ordres au client via l'interface web.
8. Rendre l'interface présentable graphiquement avec du CSS.
