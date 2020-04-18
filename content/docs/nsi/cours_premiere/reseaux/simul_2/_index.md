---
title: Simulation réseau 2
author: David Roche
weight: 6
---


### pdf : [pour impression](/uploads/docsnsi/reseau/nsi_prem_simReseau2.pdf)

#### À faire vous-même 1

En utilisant Filius, nous allons maintenant mettre en place un serveur
Web afin de pouvoir faire des requêtes HTTP. Il sera possible
d'analyser les données échangées entre les machines grâce à l'outil
"data exchange". Pour afficher cet outil, il suffit de faire un clic
droit sur la machine concernée et de choisir "show data exchange".
Commencez par visionner la vidéo ci-dessous :

Lien vers [la vidéo](https://youtu.be/fY2yiRXMdS8)

Une fois la vidéo visionnée, en utilisant le logiciel Filius, mettez en
place un réseau composé de 2 clients et d'un serveur Web, créez ensuite
une page HTML toute simple et activez le serveur Web (comme indiqué dans
la vidéo). Choisissez un client et par l'intermédiaire d'un navigateur
Web (que vous aurez au préalable installé sur le client), effectuez une
requête HTTP. Analysez les données échangées entre le client et le
serveur à l'aide de l'outil "data exchange".

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
