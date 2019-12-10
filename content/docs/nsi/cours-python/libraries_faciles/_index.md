---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Python 3 - Librairies faciles d'emploi
weight: 15
---

# Présentation de quelques librairies faciles à employer

## GPIO Zero

**Attention : GPIO Zero est une librairie exclusive au Raspberry Pi.**

Elle permet d'utiliser facilement le raspberry pour utiliser des composants
électroniques de base (LED, bouton, servo moteur etc) via son interface GPIO.

La majorité des fonctions sont déjà développées et il suffit de réaliser
le montage.

## Pygame Zero

Pygame Zero vise à simplifier le développement d'un jeu vidéo sous pygame.
Elle permet de s'affranchir de nombreuses contraintes telles que la création
de la fenêtre et des objets propres à Pygame.

De loin elle ressemble beaucoup à ce qui existe en java (processing)
et en javascript (p5js).

## GUI Zero

GUI Zero permet de créer très simplement des fenêtres et une interface
graphique. Elle permet de se concentrer sur ce que souhaite réaliser le
développeur sans devoir créer à la main tous les éléments relatifs aux
fenêtre.

## Network Zero

Cette librairie permet de faire communiquer différents processus Python
présents sur plusieurs machines. Elle a des limitations (le réseau doit
être configuré simplement etc.) mais permet d'éviter d'avoir trop à se
battre avec l'interface.

## paho-mqtt

mqtt, pour Mosquitto, est un protocole de communication entre machines reposant
sur un modèle simple : un serveur (broker) auquel se connectent des clients.
Le client envoie un message au client avec un sujet spécifique (topic), le
broker diffuse le sujet à tous les clients abonnés à ce sujet.

Elle est optimisée pour l'IOT et très peu gourmande en ressources.

MQTT n'est pas spécifique à Python et existe sous UNIX, Windows, sous forme
de libriarie pour tous les langages modernes etc.

C'est un standard de l'industrie.
