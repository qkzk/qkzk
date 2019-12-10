---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Python 3 - Network Zero
weight: 4
---

# NetworkZero


_Cette brève présentation est une traduction de la page d'accueil de la_
_[documentation officielle](https://networkzero.readthedocs.io/en/latest/)_
_de la librairie._

## Introduction

NetworkZero facilite l'emploi de Python pour connecter des machines
entre elles à travers internet. Il est particulièrement conçu pour un
environnement classe ou club d'informatique où des programmes à faible durée de vie doivent se découvrir sur une même machine ou non doivent
se découvrir sans connaître les adresses IP ou les noms de domaine.

Il tourne sur Python 2.7 et Python 3.3+ et devrait fonctionner partout
où Python tourne. En particulier, il est testé automatiquement sur Windows, Mac et Linux et est utilisé sur les Raspberry Pi.

NetworkZero offre deux services principaux :

* Découvrerte automatique de programmes,
* Echanges d'objets Python entre les programmes,

## Que peut-il faire ?

N'importe quoi utilisant une machine ou un processus pour échanger à travers un réseau. Par exemple :

* Envoyer des commandes à un robet
* Envoyer des données d'un raspberry avec un capteur à un PC qui dessine et enregristre les données
* Montrer l'état d'un jeu partagé dans une fenêtre tout en envoyant les commandes d'un autre.

## Pouvez-vous montrer un exemple ?

[Machine or Process A]:

~~~python
import networkzero as nw0

address = nw0.advertise("hello")
while True:
    name = nw0.wait_for_message_from(address)
    nw0.send_reply_to(address, "Hello " + name)
~~~

[Machine or Process B and C and D ...]:

~~~python
import networkzero as nw0

hello = nw0.discover("hello")
reply = nw0.send_message_to(hello, "World!")
print(reply)
reply = nw0.send_message_to(hello, "Tim")
print(reply)
~~~

Cela fait tourner un service, rendu public sous le nom "hello" qui va repondre "Hello <name>" chaque fois que <name> lui est envoyé. Les autres machines ou processus découvrent le service et lui envoient leur noms, recevant un message d'accueuil en retour.

## En lire davantage :

* [utilisation](https://networkzero.readthedocs.io/en/latest/usage.html)
  * [introduction](https://networkzero.readthedocs.io/en/latest/usage.html#introduction)
  * [concepts](https://networkzero.readthedocs.io/en/latest/usage.html#concepts)
  * [exemples](https://networkzero.readthedocs.io/en/latest/usage.html#examples)
* [pour les enseignants](https://networkzero.readthedocs.io/en/latest/for-teachers.html)
  * [introduction](https://networkzero.readthedocs.io/en/latest/for-teachers.html#introduction)
  * [bénéfices](https://networkzero.readthedocs.io/en/latest/for-teachers.html#benefits)
  * [difficultés](https://networkzero.readthedocs.io/en/latest/for-teachers.html#difficulties)
* [pour les développeurs](https://networkzero.readthedocs.io/en/latest/for-developers.html)
  * [background](https://networkzero.readthedocs.io/en/latest/for-developers.html#background)
  * [services](https://networkzero.readthedocs.io/en/latest/for-developers.html#services)
  * [offre de base](https://networkzero.readthedocs.io/en/latest/for-developers.html#basic-offering)
  * [plus d'information](https://networkzero.readthedocs.io/en/latest/for-developers.html#more-information)
