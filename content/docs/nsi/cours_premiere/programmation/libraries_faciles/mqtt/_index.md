---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Paho Mqtt
weight: 5
---

# Paho MQTT


_Cette brève présentation est une traduction de la page d'accueil de la_
_[documentation officielle](https://pypi.org/project/paho-mqtt/)_
_de la librairie._


Parmi tous les projets présentés, Paho MQTT est le seul d'usage professionnel. Le niveau requis est légèrement supérieur (mais pas tant que ça).

## Mosquitto


mqtt, pour Mosquitto, est un protocole de communication entre machines reposant
sur un modèle simple : un serveur (broker) auquel se connectent des clients.
Le client envoie un message au client avec un sujet spécifique (topic), le
broker diffuse le sujet à tous les clients abonnés à ce sujet.

Elle est optimisée pour l'IOT et très peu gourmande en ressources.

MQTT n'est pas spécifique à Python et existe sous UNIX, Windows, sous forme
de libriarie pour tous les langages modernes etc.

C'est un standard de l'industrie.

## Introduction

La librairie Paho-MQTT, développée par Eclipse, propose un client qui permet à des applications de se connecter à un broker MQTT (**qu'il faut créer séparément en quelques commandes**) pour publier des messages et s'abonner à des topics afin de recevoir les messages publiés.  Il propose aussi des fonctions simples facilitant la publication de messages à un serveur MQTT.

## Installation

La dernière version stable de la librairie est disponible dans PyPi et peut être installée via :

~~~bash
$ pip install paho-mqtt
~~~

ou, dans un environnement virtuel (hp nsi)  `virtualenv`:

~~~bash
virtualenv paho-mqtt
source paho-mqtt/bin/activate
pip install paho-mqtt
~~~

## Débuter

Voici un exemple très simple qui se à l'arbre du topic $SYS et affiche les messages reçus :

~~~python
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
~~~
