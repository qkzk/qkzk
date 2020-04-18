---
title: Créer une clé Linux
author: qkzk
theme: metropolis
weight: 2
# mainfont: Noto Sans CJK JP
---

# Utiliser Linux

Le programme de NSI demande à ce que vous utilisiez un système libre.

Le plus couramment utilisé étant Linux, c'est celui qui a été choisi pour vous.
Il existe de nombreuses possibiités pour utiliser Linux au Lycée et l'une
d'entre elle est la clé **Freeduc Jbart.**

# Clé Linux : Freeduc Jbart

Le Lycée Jean Bart à Dunkerque propose une clé USB qui permet de mettre en
oeuvre tous les éléments du programme de NSI concernant les systèmes
d'exploitation et les logiciels libres.

Elle utilise la distribution **debian** et l'environnement de bureau **cinnamon**

![debian et cinnamon](https://philippe.scoffoni.net/wp-content/uploads/2015/04/S%C3%A9lection_0123.png)

## Créer la clé.

La démarche est entièrement détaillée [ici](https://usb.freeduc.org/freeduc-usb/freeduc-jbart/index.fr.html)

**Résumé depuis une machine Linux**

1. Disposer d'une clé USB d'au moins 16 GB. De préférence en USB3 pour gagner beaucoup de temps
2. Brancher la clé usb
3. `df` devrait afficher la clé sur `/dev/sdb`. Sinon ouvrir un gestionnaire de fenêtre et repérer la clé.

  Si elle n'apparait toujours pas, essayer `$ sudo gparted` pour repérer la clé.

4. Télécharger la version "légère" (3 GB) de la clé : **live-image-amd64.hybrid.iso**
5. Copier avec dd le contenu sur la clé : `$ sudo dd if=live-image-amd64.hybrid.iso of=/dev/sdX status=progress bs=4M oflag=dsync`
    où on remplace `X` par l'adresse de la clé

6. Utiliser fdisk pour créer une partition de persistence :

  1. `$ sudo fdisk /dev/sdX`
  2. nouvelle partition `n`. Suivre les instructions par défaut.
  3. écrire : `w` - sinon rien n'est enregistré sur la clé.
  4. vérifier (fdisk, p, q)

7. Formater la partition de persistence :

  `$ sudo mkfs -t ext4 -L persistence /dev/sdX3`

8. Créer un fichier `persistence.conf` contenant `/ union` sur la machine locale
9. Copier le fichier sur la partition de persistence :

  `$ sudo cp persistence.conf /run/media/robert/persistence/`

  Si la clé n'est pas montée, la monter avec un gestionnaire de fichiers.
10. Si possible, copier le paquet debian de google chrome (rechercher google chrome, télécharger .deb)
10. Effacer les autres fichiers éventuels de cette partition :

  1. `$ cd /run/media/robert/persistence`
  2. `$ ls`
  3. `sudo rm -rf lost+found`

## Booter sur la clé

C'est variable selon les systèmes mais il faut toujousr s'assurer qu'on peut
démarrer depuis une clé usb dans le bios. Certains bios remettent ce paramètre
à une valeur par défaut dès que la clé est retiré.

Pour booter sur la clé :

1. brancher la clé
2. rebooter et, dans le bios, activer le boot sur la clé.

## Tester la persistence

La clé n'est fournie qu'avec des logiciels libres. On peut installer google chrome pour tester.

1. arrivé sur la clé, repérer le paquet debian dans /run/live/persistence/sdb3 et l'installer

    `$ sudo dpkg -i /run/live/persistence/sdb3/google TAB`

2. Si le paquet n'a pas pu être copié, il faut le télecharger et l'installer

    activer le wifi si nécessaire. Se connecter au réseau.
3. lancer firefox et chercher `google chrome`.
4. suivre le premier lien, télécharger, enregistrer sur le disque.
5. installer le paquet debian de google chrome :

    `$ sudo dpkg -i Téléchargement/google-chrome... (TAB)`
6. Tester : `$ google-chrome`
8. **rebooter**. Google chrome doit toujours être présent.

## Utiliser la clé.

Se référer au TP "découverte le linux" et aux résumés fournis.

## Dupliquer sa clé

Il est possible de **dupliquer** la partie "programmes" de la clé
(sans la persistence) avec l'outil fourni directement dans la distribution : **live clone**

Il reste ensuite à activer la persitence (voir plus haut).
