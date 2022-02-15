---
title: "TP: Simulation 2"
author: "David Roche"
date: "2022/02/15"
theme: "metropolis"
weight: 22
bookCollapseSection: true

---

### [pdf](./tp_reseau_2.pdf)



En utilisant Filius, nous allons maintenant mettre en place un serveur
Web afin de pouvoir faire des requêtes HTTP. Il sera possible
d'analyser les données échangées entre les machines grâce à l'outil
"data exchange". Pour afficher cet outil, il suffit de faire un clic
droit sur la machine concernée et de choisir "show data exchange".

## À faire vous-même 1

Commencez par visionner la vidéo ci-dessous :

Lien vers [la vidéo](https://youtu.be/fY2yiRXMdS8)

## À faire vous-même 2

Une fois la vidéo visionnée, en utilisant le logiciel Filius :

1. mettez en place un réseau composé de 2 clients et d'un serveur Web,
2. créez ensuite une page HTML toute simple et activez le serveur Web (comme
   indiqué dans la vidéo). 
3. Choisissez un client et par l'intermédiaire d'un navigateur Web (que vous
   aurez au préalable installé sur le client), effectuez une requête HTTP. 
4. Analysez les données échangées entre le client et le serveur à l'aide de
   l'outil "data exchange".



Comme vous pouvez le constater on retrouve :

-   le protocole TCP au niveau de la couche "Transport" ("ACK"
    signifie acknowledgement, ce sont les accusés de réception aussi
    appelés acquittement)
-   le protocole HTTP au niveau de la couche "Application" (en
    cliquant sur les requêtes et réponses HTTP on retrouve ce que l'on
    a vu précédemment dans le cours "Protocole HTTP")
-   le protocole ARP qui permet de trouver une adresse MAC à partir
    d'une adresse IP (l'échange entre les 2 machines commence
    d'ailleurs avec ce protocole ARP, sinon, impossible d'envoyer les
    trames)

On notera que les trames et les paquets IP ne sont pas directement
visibles avec cet outil "data exchange" : il faut cliquer sur une
ligne "TCP" pour "voir" les couches "Internet" et "accès
réseau".
