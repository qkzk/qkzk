---
author: qu3nt1n
date: 2017-06-20 09:50:56+00:00
draft: false
title: partie 3 - Quelques montages électroniques simples


---

## Rapide présentation du kit.


Le kit de démarrage permet d'aborder l'électronique.

Il comporte des capteurs variés, des câbles mâle-mâle, des résistances, des leds, un servo-moteur et des boutons.

Afin de simplifier l'installation on commence par brancher le hat (chapeau) sur le raspberry. Ce n'est pas exactement le même modèle mais le branchement est identique :

![](https://cdn-shop.adafruit.com/1200x900/2327-10.jpg)


Ensuite on emploie directement les sorties du GPIO qui entourent le mini-breadboard central. Elles sont référencées à l'aide de la numérotation BCM (ou GPIO) disponible sur [pinout](https://fr.pinout.xyz/).

Les câbles mâle-mâle permettent de réaliser un montage.


## Sortie : une simple LED


Commençons par alimenter une LED. Nous allons utiliser la librairie **gpiozero.**




 	    1. **Installation de la librairie.**
Il est possible qu'elle soit déjà installée. Testons le en essayer de l'important dans Python.
Ouvrez Python et tapez : import gpiozero . Si vous ne voyez pas d'erreur la librairie est déjà installée et passez au 2.
Sinon :
Mettez à jour les paquets : sudo apt-get update
Et installez la librairie : sudo apt-get install python-gpiozero
Testez dans Python son import.
 	    2. ****Montage électronique.
![](https://leanpub.com/site_images/rpiintheclassroom/led-gpio17.png)
Souvenez vous que les leds sont **polarisées. **La longue broche vers le plus (pin 17) la courte vers le moins (ground).
On utilisera une résistance entre l'alimentation (pin 17) et la led. Celle-ci empêche la led de griller. Il n'est pas indispensable de s'en servir mais les leds sont fragiles.****On mesure la résistivité en Ohms. Plus c'est élevé, moins le courant circule. Ici on emploiera une résistance d'1 kilo Ohms, ressemblant à ça. Utilisez les couleurs des stries pour vous repérer.
![](https://www.pakwheels.com/forums/attachments/mechanical-electrical/334758-led-lovers-bike-cars-cfr-50jb-1r0.jpg)

 	    3. **Script
**Creez un fichier **testled.py **dans le dossier_ /home/pi _du raspberry pi.
Si vous êtes en ligne de commande vous pouvez utiliser l'éditeur de texte **nano. : **nano testled.py
Une fois votre code tapé (ou collé) vous pouvez quitter nano en utilisant le raccourci clavier : ctrl+x.
Pour sauvegarder confirmez "yes" ou "oui" selon la langue, pour fermer sans saugarder "no".
Puis entrez. Hop votre fichier est enregistré.
Voici le code :

    
    from gpiozero import LED
    from time import sleep
    
    led = LED(17)
    
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)


Examinons le en détail.
On comment par import la fonction LED de la librairie gpiozero. C'est la force de cette librairie, elle propose déjà des fonctions toutes faites comme allumer ou éteindre une led.
Ensuite on charge sleep qui permet de faire des pauses de certaines durées (en secondes).

On définit la variable **led** qui est raccordée au pin 17 (numérotation BCM, celle de votre hat).
On lance ensuite une boucle infinie qui va :

 	      * éclairer la led et faire une pause d'une seconde
 	      * éteindre la led et faire une pause d'une seconde

Puis recommencer. La led clignotte donc indéfiniment. Executez ce script avec Python depuis la console :
sudo python testled.py
 	    4. ****Evolutions****
Bien que ce montage soit simpliste il est possible de le faire évoluer grandement. Déjà en ajoutant des composants : d'autres leds pour créer des animations, des boutons pour les contrôler.
D'un point de vue logiciel : on peut intégrer d'autres fonctions à notre script comme relever ses mails et le faire réagir si un nouveau mail est reçu ou alors vérifier si quelqu'un est connecté à un réseau (un chat, une plateforme de jeu) et pouvoir facilement le rejoindre.




#### Gmail Checker


C'est un projet déjà complexe que je propose à ceux qui vont vite. Il n'est pas obligatoire.
Reprendre et adapter le tutoriel [d'adafruit](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview) au matériel disponible.

**Cahier des charges**




 	    * Réaliser un montage électronique avec deux leds (protégées par les résistances adéquates) raccordées sur des pins du GPIO
 	    * Créer un script python allumant la led verte et éteignant la led rouge si tous les messages sont lus et faisant le contraire s'il existe un message lu dans la boite de réception. _Remarquons que le projet est entièrement détaillé sur Adafruit... les adaptations sont très modiques et à la portée d'un singe savant... qui parlerait anglais.
Son objectif est donc de vous familiariser avec les tutoriels dédiés au raspberry d'[Adafruit](https://learn.adafruit.com/category/raspberry-pi)_




## Entrée : un bouton, sortie : une led


Reprenons le montage précédent, nous allons ajouter un bouton. Nous allons encore utiliser la librairie Python **gpiozero**, référez vous à la partie précédente pour son installation.



 	  1. ****Montage
![](https://github.com/RPi-Distro/python-gpiozero/blob/master/docs/images/led_button_bb.png?raw=true)
**** 

Utilisez la même resistance (1K Ohms) que précédemment. Vérifiez bien l'orientation de l'interrupteur. La led est toujours sur le pin 17 et l'interrupteur est sur le pin 3. Toujours avec les numérotations BCM.
 	  2. ****Script
****

    
    from gpiozero import LED, Button
    from signal import pause
    
    led = LED(17)
    button = Button(3)
    
    button.when_pressed = led.on
    button.when_released = led.off
    
    pause()
    




On ajoute cette fois la fonction pause de la librairie signal.
Elle permet d'interrompre le programme et d'éviter qu'il ne se ferme tout seul.
Remarquons qu'on définit le bouton comme la led grâce à son pin.

Les méthodes button.when_pressed et button.when_released définissent des actions à effectuer quand on presse le bouton ou qu'on le relâche.

Quand on presse, la led s'allume, quand on relâche elle s'éteint.

Enregistrez ce code dans un nouveau fichier : **test_button_led.py** et testez le.
 	  3. **Evolutions**
Elles sont nombreuses... On peut déjà remplacer le bouton par un [**interrupteur reed**](https://fr.wikipedia.org/wiki/Interrupteur_reed) qui, relié à un petit aimant, s'ouvre et se ferme quand on ouvre ou ferme une porte ! Vous avez déjà de quoi surveiller les entrées et sorties d'une pièce ou d'une armoire. Avec un minimum de modifications au script, vous pouvez envoyer une alerte par mail quand quelqu'un entre dans votre chambre. Il suffit de lancer le script avant de partir et hop.
Le pire est que ça fonctionne bien.



## Feu tricolore


Trois exemples de scripts sont présentés par gpiozero afin de contrôler quelques feux tricolores.

On les trouvera [ici](https://github.com/RPi-Distro/python-gpiozero/tree/master/docs/examples). Tout en bas : traffic_light_1.py etc.

Le montage est le suivant :

![](https://github.com/RPi-Distro/python-gpiozero/blob/master/docs/images/traffic_lights_bb.png?raw=true)


Testez les tous les trois.

**Consigne**

Ajoutez un bouton à ce montage. Utilisez les exemples précédents pour faire évoluer le feu à chaque pression du bouton.



 	  1. Au lancement du script les feux sont éteints
 	  2. Quand on presse le bouton le vert s'allume et reste allumé
 	  3. Quand on le presse à nouveau le jaune s'allume et le vert s'eteint, puis le rouge et le jaune s'éteint.
 	  4. Quand on presse une quatrième fois les feux s'éteignent et on peut recommencer.

Vous pouvez partir du dernier exemple qui est le plus explicite mais le premier fera l'affaire. Le second est le plus complexe à mes yeux.
