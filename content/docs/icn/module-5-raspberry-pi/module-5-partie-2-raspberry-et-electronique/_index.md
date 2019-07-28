---
author: qu3nt1n
date: 2017-06-20 07:53:29+00:00
draft: false
title: 'partie 2 - Raspberry Pi et electronique : une introduction'


---

## L'électronique et le Raspberry Pi.




Le raspberry Pi permet **d’interagir physiquement avec l'extérieur**. Ceci est fait en utilisant le GPIO : General Purpose Input and Output (Entrées / sorties d'usage général).

Ce sont des ports d'entrée et de sortie couramment employés dans l’électronique. Ces ports sont souvent présents sur des machines et l'Arduino et le Raspberry Pi sont les premières cartes à vraiment les avoir démocratisés. Jusqu'ici il était préférable de maîtriser un minimum d'électronique avant de commencer à s'en servir. Ce n'est plus le cas. On peut maintenant inverser les rôles et découvrir l'électronique en créant des projets simples.

Cette présentation vise à vous familiariser avec le GPIO. Je pars du principe que vous ne connaissez rien ou presque à ce sujet et vais donc tâcher de exposer les grandes lignes.


### Présentation du GPIO.


Le GPIO des raspberry Pi 2, 3 et zero se présente sous la forme de 40 pins qui sont organisés de la même manière sur toutes ces cartes.

Le site de référence (à mes yeux) pour explorer les possibilités du GPIO est [pinout.xyz](https://fr.pinout.xyz/). Entièrement traduit en français il propose les trois numérotations (!) courantes.

Commençons par regarder le raspberry et apprendre à se repérer. Ouvrez le site [pinout.xyz](https://fr.pinout.xyz/) et réduisez les dimensions de la fenêtre afin de lire ce document en même temps.

![Raspberry_Pi_2_Model_B_v1.1_top_new](http://qkzk.xyz/wp-content/uploads/2017/06/Raspberry_Pi_2_Model_B_v1.1_top_new-683x1024.jpg)


Voici l'orientation du raspberry permettant le mieux de se repérer. Le pin physique numéro 1 est celui en haut à gauche. Le 2 est à sa droite et on continue ainsi de suite. Toute la colonne de gauche est impaire (1, 3, 5 etc.) et celle de droite paire (2, 4, 6). **Quel est le numéro physique du dernier pin en bas à gauche ?**

Cette numérotation, physique, n'est pas celle que vous rencontrerez le plus souvent. Il en existe deux autres : **BCM** numbering (parfois référence en GPIO numbering) et **WiringPi** numbering.


### Quel est le rôle des pins ?


On peut découper les fonctions du GPIO en 5 grandes catégories.



 	  1. Les pins **d'alimentation**. On en compte quatre : deux pins en 3.3 volts et deux pins en 5 volts. **Repérez les sur le raspberry.**
Remarquons que les pins en 3.3V sont limités à 50 mA : de quoi alimenter quelques petits composants. Pas assez pour faire tourner un moteur.
Les pins en 5 v sont directement raccordés à l'alimentation du raspberry. Il faut donc faire très attention si on s'en sert. Il est d'ailleurs possible d'alimenter le raspberry lui même en employant ces pins.
 	  2. Les **GROUNDS**. Souvent référencés en GND ou Masse pour les docs en français. Ils permettent de fermer un circuit électrique. L'alimentation électrique d'un composant nécessite toujours un circuit fermé
![](https://upload.wikimedia.org/wikipedia/commons/b/b4/Ohm%27s_Law_with_Voltage_source_TeX.svg)

C'est un peu plus compliqué en réalité mais disons que le courant circule du "plus" vers le "moins". Dans le montage ci-dessous le plus serait un pin 3.3v du rapsberry et le moins un des grounds.
L'alimentation est symbolisée par le rond à gauche, et le R à droite représente une résistance. Ce montage electrique est grosso modo celui d'un radiateur électrique ou d'un grille pain ! Ajoutons une led et voici un premier montage. Vous le réaliserez bientôt.
![](https://www.raspberrypi.org/learning/robot-antenna/images/gpio.png)

Le "truc" rouge est une LED, c'est d'une diode électroluminescente (yeah). Elle est orientée - comme une pile, on dit qu'elle est polarisée - et on se repère facilement ainsi : la tige courte part vers le moins (ground), la tige longue vers le plus (3.3 V).
L'espèce d'haltère marron est une résistance (qui protège la LED). On peut connaître la résistivité de celle-ci en repérant les stries colorées qu'elle présente. On trouve facilement sur internet les correspondances entre couleur et valeur.
Ce montage n'a aucun intérêt : la LED s'allume, point.Les grounds sont tous raccordés entre eux, on peut les échanger à notre convenance.
**Combien le rapsberry comporte-t-il de ground ? Comptez les sur pinout.xyz.**
Astuce : si vous cliquez sur un ground, les autres s'affichent aussi  !
Les autres pins ont trois fonctions possibles.
 	  3. Les **Sorties** "standard". Tous les autres pins peuvent peuvent émettre un courant à notre convenance. La tension est alors +3.3V et l'intensité maximale celle du +3.3V soit 50 mA.
![](https://leanpub.com/site_images/rpiintheclassroom/led-gpio17.png)

Ce montage est déjà plus intéressant ! Le + est ici le pin noté (GP17), sa numérotation physique est 11. On peut allumer (à l'aide d'un petit programme) ou éteindre la LED quand ça nous chante.
Si vous réalisez ce montage sans rien programmer il ne se passera rien ! Par défaut tous les pins sont en mode "entrée".
![](http://akshaim.in/4DIAC/images/Chapter_3/Pi_Blink.gif)

 	  4. Entrée "standard". Ils peuvent recevoir un signal digital et donc servir de lecteur d'interrupteur. Dans un programme on aura donc une commande d'écoute sur un des pins et, lorsqu'un signal est reçu, on pourra l'interpréter.
Voici, par exemple, un simple bouton raccordé en entrée.
Remarquons qu'on alimente le bouton en +3.3 V. D'après ce qu'on a dit plus haut concernant les circuits électriques cela signifie que le pin d'entrée est vu comme une masse.
![](http://www.scratchmypi.co.uk/wp-content/uploads/2014/05/pushuppi_bb-1024x959.png)
_Le grand rectangle blanc au centre de l'image est un **breadboard.
**Il est découpé en 4 parties similaires. Les traits verticaux tout à gauche et à droite sont reliés entre eux. On relie généralement l'alimentation sur le rouge, la masse sur le bleu._
_La partie centrale fonctionne différemment. Les LIGNES horizontales sont reliées entre elles. Ce qui permet la connexion du circuit que vous voyez.
_
 	  5. Les autres fonctions sont, pour l'instant, toutes regroupées dans cette catégorie. Disons simplement que tous les pins (sauf alimentations et masses) peut être des entrées et sorties standard mais seuls certains peuvent servir aux autres fonctions.
Ces fonctions permettent de réaliser des montages beaucoup plus complexes : alimentation de moteur, lecture de valeurs (température renvoyée par un capteur), gestion d'un écran à cristaux liquides etc.
Parmi ces fonctions citons :
**I2C** qui permet de connecter de nombreux périphériques à l'aide de 4 broches seulement (pin 3 et 5 pour les données et l'horloge, une masse et une alimentation).
![grove-lcd-rgb_bb](http://qkzk.xyz/wp-content/uploads/2017/06/grove-lcd-rgb_bb-1024x695.png)

_Un écran à cristaux liquides RGB raccordés à un raspberry. La "logique" électronique de cet écran est 5V il faut donc l'alimenter en 5V (fil rouge). Les informations (fils blanc et jaune) transitent par un convertisseur de niveau logique (le carré rouge) (à gauche 3.3V, à droite 5V). Le circuit est complété par une masse (fil noir) qui transite elle aussi par le convertisseur.
Ajoutons un capteur d'humidité et de température et voilà ce qu'on peut réaliser :
![](https://32414320wji53mwwch1u68ce-wpengine.netdna-ssl.com/wp-content/uploads/2014/08/GrovePi_Home_Weather_Station_display.jpg)
_
Evoquons aussi **SPI** qui permet de réaliser de multiples liaisons séries (pour connecter un Arduino ou un microcontrôleur).
D'autre standards de l'électronique sont incorporés mais ce n'est pas notre but que de les présenter tous ici.
Si ces technologies vous intéressent elles sont présentées sur pinout.xyz



### Est-ce aussi bien qu'un Arduino ?


Le concept est différent ! Un arduino ne fait que de l'électronique et il la fait mieux qu'un raspberry. En effet l'arduino n'est pas un ordinateur, pas de système d'exploitation, pas de clavier, souris, caméra. Pas de jeux etc.
L'arduino propose aussi nativement de la lecture **analogique : il peut mesurer une tension, une résistivité etc.**
Pour faire cela avec un raspberry il faut une puce supplémentaire.
D'autre part, l'arduino est plus fiable que le raspberry. Ce n'est pas son objectif mais l'arduino pourrait être employé dans l'industrie. Une fois correctement programmé il tourne indéfiniment et fait exactement ce qu'on attend de lui.
Le raspberry est plus complexe et peut planter ou ramer comme n'importe quel ordinateur.
Enfin, bien qu'il existe un raspberry zero à 5€, il est difficile de se le procurer sans devoir acheter un pack complet qui coûte vite 25€... et il faut encore souder etc.
L'arduino mini se trouve à 1.50€ sur des sites grands publics. Vous aurez alors un "remake" totalement identique fabriqué en Chine. C'est légal, je vous l'assure.


### Comment cela fonctionne-t-il ?


Des variantes existent mais grosso-mode toutes reprennent le même principe.



 	  1. On réalise un montage électronique en s'aidant d'un schéma (ou alors on en invente un !)
 	  2. On installe éventuellement une librairie propre à un langage de programmation (Python, C etc.) et on se documente un peu sur son fonctionnement
 	  3. On écrit un programme dans ce langage, on le lance et hop, le tour est joué.

La majorité des projets disponibles sur internet proposent le montage électronique et le code qui les accompagne. Les plus aboutis peuvent rarement être reproduits à l'identique : il faut exactement le même matériel et les mêmes installations...


### Les librairies les plus courantes


La libraire historique est **[RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO). **C'est une librairie Python installée par défaut dans raspbian. Elle est assez simple et puissante. Vous trouverez des tonnes de scripts l'utilisant.
Il convient d'apprendre à s'en servir, au moins de manière rudimentaire.
Elle n'est pas toujours intuitive mais permet de comprendre assez bien ce qui se passe.

Ensuite vint **[WiringPi](http://wiringpi.com/).** C'est une librairie très puissante qui gère toutes les possibilités du GPIO. Développée en C elle fonctionne directement dans le shell (la console). Des adaptations au langage Python sont proposées mais méfiance, certaines sont incompatibles avec vos programmes.
On la réservera à des projets avancés (moteurs en particulier).

Une nouveauté : **[gpioZero](https://gpiozero.readthedocs.io/en/stable/). **Développée dans l'optique de simplifier la découverte de l'électronique elle est assez puissante et TRES SIMPLE d'emploi.

    
    from gpiozero import LED
    from time import sleep
    
    led = LED(17)
    
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)


Et hop vous avez une led qui clignote toutes les secondes. Les autres recettes proposées sur gpioZero sont du même ordre : simples et lisibles. Nous allons en découvrir quelques unes.

Enfin, certains fabricants d'électronique proposent leurs propres librairies. Citons [Adafruit](https://www.adafruit.com/) qui publie aussi une tonne de tutoriels et une plateforme dédiée à l'IoT (internet des objets, domotique etc.) mais aussi [Sparkfun](https://www.sparkfun.com/) ou [Grove](http://wiki.seeed.cc/Grove_System/).

Nous allons maintenant réaliser quelques montages utilisant les composants présents dans le kit de démarrage.
