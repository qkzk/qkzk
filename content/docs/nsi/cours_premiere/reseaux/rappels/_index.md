---
title: "Rappels"
author: "David Roche"
date: "2022/02/15"
theme: "metropolis"
weight: 1
bookCollapseSection: true

---

[pdf](./reseau_rappels.pdf)


## Rappels : Introduction au réseau

_Ce qu’il faut retenir de seconde_

### Réseaux

Des ordinateurs sont dits “en réseaux” quand ils sont capables de communiquer
entre eux soit par l'intermédiaire d’un câble (ex : câble Ethernet avec
prises RJ45) ou d’une connexion radio (ex : Wifi).\
Pour relier plus de 2 ordinateurs, il est nécessaire d’utiliser un switch

### IP : _Internet Protocol_, les adresses

Pour identifier un ordinateur sur un réseau, on utilise _généralement_ une **adresse IP**. 
Les adresses IP sont de la forme : "a.b.c.d", avec a, b, c et d compris entre 0
et 255 (a, b, c et d sont codés sur 1 octet). Ce format est appelé IPv4. Nous en verrons
un autre cette année : IPv6.

Une partie de l’adresse IP permet d’identifier le réseau auquel appartient la
machine et l’autre partie de l’adresse IP permet d’identifier la machine sur
ce réseau 

Exemple : soit l’adresse IP d’un ordinateur : 192.168.3.1/24,
192.168.3 correspond à la partie réseau de l’adresse IP et 1 correspond à la
partie machine de l’adresse IP

### Adresse réseau

Toutes les machines appartenant au même réseau devront posséder la même
adresse réseau (sinon elles ne pourront pas communiquer ensemble, même si
elles sont bien physiquement reliées).

les adresses IP (a.b.c.d) n’ont forcément pas les parties a, b et c
consacrées à l’identification du réseau et la partie d consacrées à
l’identification des machines sur le réseau : on ajoute à l'adresse IP un "/"
suivi d'un nombre, généralement 8, 16 ou 24

* si ce nombre est 8 (exemple : 192.168.2.1/8), cela signifie que pour une
 adresse a.b.c.d/8, la partie a est consacrée à l'adresse réseau, le reste
 (b, c, d) est consacré à la partie machine de l'adresse IP. On aura donc
 une adresse réseau de la forme a.0.0.0

* si ce nombre est 16 (exemple : 192.168.2.1/16), cela signifie que pour
 une adresse a.b.c.d/16, les parties a et b sont consacrées à l'adresse
 réseau, le reste (c, d) est consacré à la partie machine de l'adresse IP.
 On aura donc une adresse réseau de la forme a.b.0.0

 * si ce nombre est 24
 (exemple : 192.168.2.1/24), cela signifie que pour une adresse
 a.b.c.d/24, les parties a, b et c sont consacrées à l'adresse réseau, le
 reste (d) est consacré à la partie machine de l'adresse IP. On aura donc
 une adresse réseau de la forme a.b.c.0

### Routeurs

Certaines machines sont connectées à plusieurs réseaux et réalisent un
pont entre ces réseaux. On les appelle des _routeurs_.

Chez vous ou au lycée, vous disposez d'un _réseau local_ au sein duquel les
machines peuvent communiquer directement.

Accéder à internet -- qui est à l'extérieur de votre réseau local -- nécessite
de passer par un routeur. Chez vous, c'est généralement la box internet
qui fait office de routeur (réseau local + internet), de switch (plusieurs prises RJ45)
et de borne wifi.

### DNS

Il existe un protocole appelé DNS qui fait le lien entre un domaine (`impots.gouv.fr`)
et une adresse IP (`145.242.11.100`). Certaines machines sur internet accomplissent ce rôle.
Cela nous évite d'avoir à retenir des adresses IP, c'est comme une liste de contacts.


