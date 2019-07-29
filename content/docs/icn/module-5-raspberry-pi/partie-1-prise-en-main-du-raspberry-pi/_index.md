---
author: qu3nt1n
date: 2017-06-20 13:41:39+00:00
draft: false
title: partie 1 - Prise en main du raspberry pi


---

# 1. Présentation du Raspberry Pi


![](http://apprendre-python.com/images/raspberry-pi.png)

Les passionnés de bidouillage informatique seront un moment où un autre confrontés à un article parlant du **raspberry pi**.


## Qu'est-ce qu'un raspberry pi?


Le **raspberry pi** est un _nano ordinateur_, c'est à dire qu'il est _aussi grand qu'une carte de crédit_.
Le projet est assez récent: 2012 et près de 5 millions de cartes ont été vendues.


![Raspberry pi 2](http://apprendre-python.com/images/raspberry-pi-2.jpg)



Le **rapsberry pi** a été conçu par David Braben, un créateur de jeux vidéos. Le **nano ordinateur** est vendu nu ou accompagné d'un kit d'initiation à l'électronique, il est uniquement composé d'une carte mère.
Comme vous pouvez le voir, il ne dispose pas de périphériques (clavier, souris, écran) et pas non plus de stockage de masse (disque dur).
Le prix du modèle (le B+) et d'environ **30 euros**. Le **raspberry pi** est alimenté par un câble USB, il consomme donc très peu d'énergie.

Listons les avantages de ce nano ordinateur:



 prix faible (30 euros)
 très faible consommation
 totalement silencieux
 environnement linux, donc Geek friendly - mais aussi windows 10 IoT (Internet of Things) ou Android.
 4 ports USB
 1 sortie HDMI
 1 port réseau RJ45
 des OS lui sont dédiés
 beaucoup d'outils pour démarrer rapidement
 grande communauté
 des ports GPIO !

Les inconvénients

 Trop lent pour un usage exclusif, même pour faire de la bureautique.

Remarquons qu'il fait tourner sans problème des scripts domotiques ou d'anciens jeux vidéos - disons jusqu'au 16 bits inclus (SuperNES, Megadrive).


## Caractéristiques raspberry pi modèle B+





 CPU 700Mhz ARM
 mémoire 512Mo
 4 ports USB
 sortie vidéo HDMI
 carte réseau
 17x GPIO



## Caractéristiques améliorées raspberry pi modèle 2





 CPU 900 MHz quadricœur ARM Cortex-A7
 mémoire 1Go
 OS Ubuntu Core et Windows 10

_Remarque : Depuis l'achat par le lycée de quelques raspberry d'autres modèles sont sortis : le raspberry pi 3 (plus puissant, mêmes dimensions) et le raspberry pi zero (5$ !!! format très compact mais, nécessite de la soudure pour utiliser certains ports.)_


## Connectique fournie avec la boite :


On trouve aussi :



 une alimentation micro USB,
 une carte micro SD préformatée avec raspbian (à ce jour l'installation devrait être complète pour toutes les cartes)
 un adaptateur micro SD vers SD (la grande carte SD)
 un petit cable RJ45 pour le connecter au réseau du lycée (à ce jour tous les raspberry dont je dispose sont autorisés sur le réseau du lycée)
 un cable vidéo (hdmi + adaptateur dvi ou dvi + adaptateur hdmi)
 un cable USB/micro USB pour l'alimenter depuis un port USB
 Un boitier de protection pour le raspberry

Au lycée nous proposons généralement deux boîtes : les transparentes se contentes de ce qui est cité plus haut. Les noires s'accompagnent d'un kit d'électronique dont nous ferons la découverte plus tard.

Il nous manque donc :

 un clavier USB
 une souris USB
 un écran DVI

Il faudra donc employer le clavier USB la souris USB et l'écran DVI de la salle.


## GPIO ??


**General Purpose Input Output** : entrées et sorties d'utilisation générale. Ce sont les broches en haut de l'image. Le GPIO fournit des accès entre l'extérieur et le raspberry Pi. Au niveau le plus simple on peut les considérer comme des interrupteur que vous pouvez ouvrir ou fermer (Input) ou que le raspberry peut ouvrir ou fermer (Output). Les autres pins servent à alimenter un composant électronique ou sont des masses (terre).
Remarquons que le raspberry intègre aussi d'être relié à des composants électroniques avancés technologies : SPI, PWM, I2C, OneWire... Nous n'entrerons pas dans le détail.
Ce dont** il ne dispose pas** (nativement) est d'entrée/sortie analogique. Impossible de lire une tension ou une résistance, impossible de faire varier une tension.
On utilisera alors un convertisseur analogique / digital ou plutôt une carte Arduino.


### Mais pour quoi faire ?


Vous pouvez programmer les pins pour interagir avec le monde réel.
Les inputs peuvent provenir d'un capteur ou d'un signal provenant d'un autre ordinateur, d'un objet, d'un composant électronique.  Les sorties peuvent faire à peu près n'importe quoi (éclairer une LED, envoyer un signal ou des données à un autre composant...). Si le raspberry est connecté à un réseau, vous pouvez contrôler les objets qui lui sont raccordés depuis n'importe où et ces objets peuvent renvoyer des données. Le contrôle et la connexion d'objets physiques à travers internet est un monde vaste et très intéressant et le raspberry Pi est l'outil idéal pour aborder cet univers. Il existe de nombreux exemples [ici](http://www.raspberrypi.org/blog/) (en anglais) ou [ici](http://raspbian-france.fr/tutoriels/).

L'objectif de cette introduction n'est pas de vous faire travailler avec les ports GPIO... mais de vous donner envie de le faire ! On va tout d'abord apprendre à utiliser le raspberry Pi et découvrir Linux à travers des projets très simples. Si vous éprouvez de l'intérêt alors...



---



Les présentations étant faites, passons aux choses sérieuses.


# 2. Prise en main





 	  1. Insérer la carte micro SD dans le raspberry, on fera attention au sens,
 	  2. brancher la connectique nécessaire : réseau (vers la fiche murale), clavier, souris, vidéo (vers l'écran lol)
 	  3. alimenter **en dernier** sur une prise murale

Si tout s'est déroulé comme prévu le raspberry devrait booter sous **raspbian** et vous afficher soit un bureau classique, soit une console de commande dans laquelle vous identifier.
Les identifiants par défaut sont : **login : pi ; mdp : raspberry   **

La première chose à faire est de vérifier l'état de la connexion réseau. Ouvrir une fenêtre de commande (Terminal) si vous êtes sur le bureau et saisir la commande :
_Si vous êtes en mode texte, tapez simplement la commande suivante :_

    
    ifconfig


Valider avec entrée.
Vous devriez voir apparaître beaucoup d'information concernant la connexion réseau du raspberry, en particulier son **adresse IP** du style : **"176.92.0.34"** .  **Notez la.**

Selon toute vraisemblance, l'adresse ip ne change pas sur le réseau du Lycée. Celui-ci est configuré de façon à toujours donner à chaque machine la même adresse. Parfois cela n'est pas possible malheureusement.

Ensuite, on va s'assurer qu'il communique bien avec l'extérieur. Saisissez la commande suivante :

    
    ping google.com


Le raspberry va alors envoyer une requette "ping" à l'adresse google.com. Pour faire cela il doit d'abord TROUVER le domaine google.com... Et c'est un serveur DNS (domain name server) qui va lui indiquer l'adresse IP de google.com. Une fois l'adresse résolue (216.58.213.142) elle sera transcrite et il enverra sa requête. Google est configuré pour répondre aux pings (certains serveurs ne l'autorisent pas, pour des questions de sécurité) et google.com va renvoyer une réponse (Pong !). Quand celle-ci sera parvenue jusqu'à nous, le raspberry affichera le temps écoulé en millisecondes et recommencera.
Cette latence est indiquée pour chaque ping, ligne par ligne.
Cette commande s’exécute indéfiniment et il faut l'interrompre avec le raccourci clavier CTRL + C

_Remarque : Cette petite manipulation est le B-A-BA du diagnostic réseau quand vous n'arrivez plus à accéder à internet ou à une machine de votre réseau local. Elle est réalisable sous windows, seulement la commande ifconfig s'appelle ipconfig sous windows._


## 2.1 Raspbian : L'environnement graphique et la fenêtre de commande


Le système d'exploitation installé sur la carte SD est une distribution **Linux** appelée **Raspbian**. C'est une variante de Debian adaptée au raspberry Pi et qui gère donc nativement tout son matériel.

Raspbian propose de nombreux outils et logiciels pré installés que je vais vous demander de découvrir.

Par défaut, raspbian démarre en mode texte (la fenêtre de commande). Si c'est le cas, lancez l'environnement fenêtré avec la commande :

    
    startx


Vous disposez donc d'une demi-heure pour faire le tour des logiciels (et jeux !) installés sur le raspberry. Dépêchez vous !


#### RETOUR SUR LA FENÊTRE DE COMMANDE.


Linux désigne toute une gamme de systèmes d'exploitation respectant de grands principes. Leur architecture est similaire et on y trouve toujours une fenêtre de commande (généralement le logiciel qui la contrôle est **bash**). Lancez la fenêtre de commande avec l'application **Terminal**

Vous trouverez [ici](http://raspberrypis.net/les-commandes-linux-les-plus-utiles-pour-son-raspberry-pi/) une liste non exhaustive des commandes qui permettent de comprendre le fonctionnement d'un système d'exploitation sous linux. Il n'est pas question de toutes les tester ici. Retenez déjà **ls ** qui permet de lister le contenu d'un répertoire, **ifconfig** pour le réseau et **man** pour obtenir de l'information sur une commande (par exemple : **man ls**)

Pour manipuler les fichiers et dossiers : cd permet de changer de répertoire, move de déplacer un fichier ou un dossier.

Par défaut un seul utilisateur est crée, son nom est rapsberry. Les fichiers personnels de cet utilisateur sont dans le dossier /home/raspberry/ dans lequel vous êtes quand vous ouvrez le terminal. Si vous avez lancé le terminal depuis le bureau, vous serez peut-être sur /home/raspberry/Desktop

Déplacez vous avec **cd** jusqu'au bureau, listez en le contenu avec **ls** et remarquez les couleurs employées pour chaque type de fichier et dossier.

L'utilisateur raspberry est un **Administrateur** du système. Cela signifie qu'il peut faire ce qu'il veut de la machine, y compris en détruire totalement le système de fichier en quelques commandes. Voilà qui semble très dangereux... Mais rassurez vous.

D'abord il est possible de créer autant d'utilisateur que l'on veut et de leur donner autant de pouvoir que l'on veut. Un compte invité aura typiquement le droit d'écrire dans son répertoire et d’exécuter les commandes de base (navigateur etc.) dans un environnement protégé.

Un super utilisateur (ou administrateur) n'est en fait qu'un utilisateur normal **sauf** s'il demande **explicitement** au système d’exécuter une commande puissante. Il faut donc vraiment le vouloir pour tout saccager.

Néanmoins, retenez le, les commandes que vous saisissez dans la ligne de commande peuvent avoir des répercussions sur le bon fonctionnement du système.


## 2.2 Vous connecter sur le raspberry en SSH


SSH est à la fois un protocole et un programme. Il sert à se connecter sur une machine distante à travers un réseau et à la contrôler en ligne de commande. SSH est totalement sécurisé et il est quasi impossible de pirater une transmission entre un client et un serveur.

Ici, le serveur est le raspberry et le client la machine windows. C'est important !

Par défaut le serveur SSH est activé sur votre raspberry et tout ce que vous avez à faire est :



 	  1. de vous assurer qu'il est bien connecté au réseau du lycée (nous l'avons déjà fait).
 	  2. De relever son adresse ip (déjà fait)
 	  3. **De vous connecter depuis un autre ordinateur :**
Depuis une machine windows il faut installer [Putty](http://www.putty.org/).
Télécharger putty.exe sur votre PC (s'il n'y est pas déjà) et lancez le directement.


_`putty.exe` (the SSH and Telnet client itself)_




_32-bit: [`putty.exe`](https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe)_

![](https://www.raspberrypi.org/documentation/remote-access/ssh/images/ssh-win-config.png)
Tapez l'adresse ip du raspberry (ifconfig...) dans Host Name, cliquez sur SSH et cliquez sur Open.
Putty lance alors un terminal dans lequel il se connecte au raspberry.

Vous devriez arriver sur une invite de commande vous proposer de vous identifier :
login : pi , password : raspberry.

Pour clore la connexion il suffit de fermer le terminal.
Une fois la connexion réussie vous obtiendrez :

![](https://www.raspberrypi.org/documentation/remote-access/ssh/images/ssh-win-window.png)


Et voilà ! vous avez accès au raspberry, EN MODE TEXTE, depuis une autre machine...

**Avantages** : inutile de brancher des périphériques : clavier, souris, écrans ne sont pas indispensables. (seuls le réseau et l'alimentation demeurrent indispensables)
**Inconvénients** : pas d'environnement graphique. SSH ne gère que le texte... et l'adresse ip du raspberry peut avoir changer la prochaine fois que vous vous connecterez... Il faudra peut-être recommencer.

C'est bien beau d'accéder à une machine... mais pourquoi faire ? Bah ! Tout ce qu'on veut !

Admettons que votre raspberry contrôle une caméra avec capteur de mouvement.
Chaque fois que vous rencontrez un problème durant la configuration ou l'entretien vous pouvez vous assurer du bon fonctionnement des différents modules (la caméra, le capteur de mouvement, le serveur web sur lequel vous transmettez les images, le fichier dans lequel vous enregistrez toute l'activité etc.)

C'est déjà très élaboré... Si votre raspberry contrôle un simple serveur web, vous pouvez l'administrer à distance via le SSH

Retenez aussi que Putty risque de planter si vous éteignez le raspberry. Putty ne peut comprendre ce vous faites au raspberry, si vous lui envoyez une commande pour le redémarrer ( **sudo reboot** ) la connexion sera coupée et vous devrez fermer la fenêtre, relancer Putty et vous reconnecter... mais l'ip aura peut-être changé entre temps ! C'est la vie.



---





### Et maintenant ? Le GPIO !


Tous les projets n'utilisant pas le GPIO seront similaires : installer le logiciel, le configurer et éventuellement brancher un périphérique USB. Un peu de programmation Python si nécessaire et le tour est joué.

Si vous êtes tentés par le GPIO c'est une autre histoire !



 [tutoriel](https://espaceraspberryfrancais.shost.ca/Debuter-sur-Raspberry-Francais/Cr%C3%A9er-un-programme-Python-Raspberry-Francais/) de présentation du GPIO et des connecteurs de base : leds, boutons, Python.
 [tutoriel](https://www.youtube.com/watch?v=iGrH3jHWijw) vidéo en français (accent québécois en bonus) : trois leds, un bouton, un peu de Python. Si vous trouvez qu'il a une voix marrante : [ici](https://www.youtube.com/watch?v=6uhs-gw-NRA) pour découvrir ses idées de projet et voir sa tête. Presque tous sont réalistes, d'ailleurs.

Le b-a-ba du GPIO ne demande pas beaucoup de connaissance, mais plus vous avancez, plus il faut maîtriser la programmation... Ensuite vient le matériel et donc deux facteurs : la connaissance de l’électronique et l'achat du matériel.

Dans quel ordre aborder le GPIO ?

 	  1. allumer une led depuis un script python.
 	  2. afficher un message à l'écran quand vous appuyez sur un bouton (via un script python).
 	  3. envoyer un mail quand vous pressez un bouton.
 	  4. allumer une led quand vous recevez un mail.
 	  5. MOTION ! Le programme le plus abouti pour faire de la caméra du raspberry pi une caméra de surveillance. Configurer motion pour qu'il streame vers l'extérieur (sera bloqué depuis le lycée).
 	  6. Des capteurs ! Température, pression, humidité + serveur web = station météo.
 	  7. Les différents projets proposés aux terminales ISN : [jeu portable](http://qkzk.xyz/?page_id=478), [caméra de surveillance](http://qkzk.xyz/?page_id=62), [panic button](http://qkzk.xyz/?page_id=66)
 	  8. Créer une timelapse box qu'on dépose 24 heures et qui filme seule le passage du temps. Un peu de poésie.
![time-lapse-2_4972189_GIFSoup.com](/uploads/uploads/2016/07/time-lapse-2_4972189_GIFSoup.com_.gif)


Bon ne rêvez pas vous n'avez pas l'appareil photo qu'il faut pour réaliser une vidéo pareille.



---





## 3. Premier projets : KODI, station d'émulation


**CES DEUX PROJETS SONT A ENVISAGER SI DISPOSEZ CHEZ VOUS DE VOTRE PROPRE RAPSBERRY.**
** AU LYCEE ILS SONT TROP LONGS POUR NOS COURTES SEANCES.**

On peut se servir du raspberry comme lecteur vidéo de vidéos partagées sur un réseau ou stockées sur une clé usb, éventuellement un disque externe. Tout ça grâce à **Kodi** !


## KODI


![](https://lh5.googleusercontent.com/-z3JQRNhH124/AAAAAAAAAAI/AAAAAAAAAek/WaUEO7Dn79c/s0-c-k-no-ns/photo.jpg)


KODI (anciennement XBMC) est un média center développé à l'origine pour la première XBOX. Il permet donc de lire des vidéos, des sons et d'autres médias (flux vidéos depuis internet, podcast etc.) depuis une interface prévue pour être intuitive et manipulable avec toute sorte de périphériques (télécommande, manette, clavier, souris etc.). Raspberry + Kodi = l'équivalent du menu médias de votre PS4 / Xbox One pour 30€. En plus vous l'aurez "fait vous même" (enfin, installé vous même...).

Nous allons profiter de cette étape pour présenter la démarche générale d'installation d'un programme sur la majorité des distributions linux : le système des **dépôts** et la commande **apt-get**. L'installation d'un nouveau logiciel sur une distribution linux se fait en deux temps : on s'assure que les librairies sont à jour, on installe le logiciel.
Trois variantes de la même commande "apt-get" remplissent ces fonctions.


#### METTRE À JOUR LE SYSTÈME


_Cette étape n'est pas systématique. Il faut le faire régulièrement, peut-être tous les mois, pour éviter tout problème de compatibilité entre différentes librairies._
Commençons par le plus important... Mettre à jour le raspberry Pi :
Exécutez l'une après l'autre les commandes suivantes dans un terminal, après vous être assuré que vous êtes bien connecté à internet.

**Attention, prévoir du temps devant soi...**

    
    sudo apt-get update
    sudo apt-get upgrade


Détaillons ce qu'elles font :
**sudo : **donne à l'utilisateur courant les droits de super-utilisateur pour effectuer la commande qui suit (**s**uper **u**ser **do**es). ici apt-get qui manipule le système de fichiers, ce qu'un utilisateur normal ne peut pas faire.
**apt-get** est la commande qui gère les paquets systèmes à travers un **dépôt**.
**update** : Récupère la liste la plus récentes des paquets installés sur la machine.
Reprenons : sudo apt-get update = en tant qu'administrateur, synchronise la liste des paquets avec celle du dépôt (s'il te plait).
**upgrade** : Installe la version la plus récente des paquets présents sur la machine. Il est fort probable qu'apt-get vous demande l'autorisation d'utiliser plus d'espace disque pour mettre à jour certaines librairies. Répondez oui.

Ces deux commandes vous assurent donc de disposer des versions les plus récentes de tous les paquets installés sur votre système.

Une fois que vous avez récupéré la main :


#### INSTALLER KODI



    
    sudo apt-get install kodi


Se passe de commentaire, on installe le paquet kodi à partir du dépôt. Votre raspberry devrait télécharger et installer kodi. Et voilà, c'est déjà terminé.

De manière générale c'est ainsi qu'on installe un nouveau logiciel sur linux. Inutile de farfouiller internet, cliquer cent fois, décompresser, confirmer 30 fois, créer un raccourci au bon endroit et que sais-je.

_Et pour désinstaller ? sudo apt-get remove kody . Ne le faites pas maintenant..._


#### OPTIMISATION DE KODI


_Raspbian n'est pas le seul système d'exploitation développé pour le raspberry. Kodi est disponible dans une version plus récente et mieux optimisée sur d'autres systèmes. Si ce projet vous intéresse je vous conseille donc d'acquérir une autre carte SD dédiée à Kodi sur laquelle vous installerez [la bonne distribution](http://kodi.wiki/view/HOW-TO:Install_Kodi_on_Raspberry_Pi). La marche à suivre est généralement la même mais le résultat est optimal._

Quelques réglages sont à faire pour optimiser kodi sur raspbian et résoudre quelques problèmes potentiels ; notre objectif n'étant que de tester, je vous laisse le soin de lire [ce tutoriel](https://www.raspberrypi.org/forums/viewtopic.php?t=99866) si ça vous intéresse.


#### TESTER ET TRANSFÉRER DES FICHIERS


Etant donné que votre carte sd ne comporte aucun film pour tester, vous trouverez [ici](http://www.stephaniequinn.com/Music/Handel%20-%20Entrance%20of%20the%20Queen%20of%20Sheba.mp3) un mp3 et [ici](http://samples.mplayerhq.hu/avi/samsung_crap_bug742.avi) un film de tailles raisonnables. Téléchargez les sur le PC.

Raspbian lance, par défaut, un serveur SFTP : secure file transfer protocol (transfert sécurisé de fichiers).
Il suffit donc de se connecter au raspberry depuis un autre ordinateur avec un client FTP, gérant le SFTP tel que** FileZilla** (qui devrait déjà être installé sur votre PC, sinon faîtes le).

Hôte : l'ip du raspberry, identifiant : pi, mot de passe : raspberry (vous devriez avoir deviné) port : **22** (ftp non sécurisé 21, sftp sécurisé 22)

Vous pourrez alors transférer vos fichiers sur le raspberry ! Déplacer vos fichiers depuis la fenêtre de gauche (le PC sur lequel vous êtes) vers la fenêtre de droite (le raspberry) dans le dossier medias (/home/pi/media).

_Remarque : Il est aussi possible d'employer une clé usb mais nous allons tester le sftp_

Pour lancer kodi, si le raccourci n’apparaît pas sur le bureau, tapez kodi-standalone dans la console.

Une fois dans kodi, vidéos, dossiers, ajouter le dossiers médias (/home/pi/medias).
Vous pouvez alors ouvrir ce dossier et y trouver votre vidéo. Recommencer pour le mp3 si vous voulez tester.

Et voilà, vous disposez d'un serveur média capable d'explorer votre réseau local, de streamer des vidéos depuis internet ou depuis votre box, de lire en hd etc.

C'est aussi simple que ça !

Une fois ces tests effectués pensez à le désinstaller : sudo apt-get remove kodi.


## Station d'émulation


Retropie est un projet visant à faire du raspberry Pi une station d'émulation compatible avec une trentaine de console. Il utilise EmulationStation, un logiciel multiplateforme (linux, windows etc.) qui, justement, émule les consoles.

L'inconvénient majeur de Retropie est qu'il ne fonctionne pas bien sous raspbian. Il est donc conseillé de formater une carte micro SD uniquement pour retropie. Si vous avez une carte microSD avec au moins 8go, il est possible de tester... chez vous. Au lycée les téléchargements seront trop longs et l'intérêt modeste. Vous trouverez [ici](https://hiob.fr/configurer-retropie/) un tutoriel en français à ce propos
