---
author: qu3nt1n
date: 2017-06-20 11:53:32+00:00
draft: false
title: partie 4 - d'autres composants classiques


---

Cette page concentre quelques présentation d'emploi de composants électroniques. Chaque fois que cela est possible on emploiera la librairie **gpioZero. **


## Sorties




### piezo buzzer


Commençons par un simple buzzer. Les buzzers sont composés d'une lame d'un matériel particulier : il est piezo-électrique. Cela signifie qu'il vibre lorsqu'un courant électrique le parcourt. La majorité des haut-parleurs fonctionnent sur un principe différent, ils sont électro-magnétiques. Une membrane vibre en contact d'un champ magnétique.
Remarquons qu'on peut aussi utiliser les matériaux piezo électriques autrement : ils émettent du courant quand on les presse ! Cela permet de détecter une vibration, une pression. On parle alors de piezo-switch et le boitier du raspberry en propose un.



 	  1. **montage**![](https://www.raspberrypi.org/learning/physical-computing-with-python/images/buzzer-circuit.png)

 	  2. **script**

    
    from gpiozero import Buzzer
    
    bz = Buzzer(17)
    bz.on()


Et voilà. Comme d'habitude, créez un fichier **test_buzzer.py**, copier le script et sauvegardez le.
Exécutez le avec sudo python test_buzzer.py
 	  3. **évolutions****
**Je vous renvoie à la documentation de gpioZero pour tester les autres fonctions proposées. Vous devriez avoir compris son fonctionnement à cette étape.On trouvera aussi un projet plus amusant utilisant la librairie wiringPi. Il permet de [jouer la musique de Dark Vador](http://www.instructables.com/id/Playing-the-Imperial-March-From-Star-Wars-on-Raspb/) sur commande... Il est beaucoup plus avancé mais si vous voulez faire de la musique avec cet engin, pourquoi pas.



## Capteurs




### Distance : HC-SR04


Les capteurs de distance(*) utilisent deux pins du GPIO : un pour le _trigger (déclancheur,** **_noté TRIG sur le capteur) et un pour l'_echo (ECHO sur le capteur). _Attention, ils fonctionnent et émettent du 5V qui va très certainement endommager votre raspberry. Il faut donc d'abord réaliser un pont diviseur de tension avant de l'alimenter.

**Montage**



 	  1. Relier le GND du capteur vers un ground du raspberry
 	  2. Relier le TRIG vers un pin du raspberry (BCM 23)
 	  3. Relier une résistance 330 Ohms depuis le pin ECHO du capteur vers un pin du GPIO (BCM 24)
 	  4. Relier une résistance 470 Ohms depuis le ground du raspberry vers le pin ECHO. Cela forme alors un [pont diviseur de tension](https://fr.wikipedia.org/wiki/Diviseur_de_tension). Le signal reçu par le raspberry sera du 3.3V (environ).
 	  5. Enfin, relier le VCC du capteur vers un pin 5V du raspberry.

![](https://raw.githubusercontent.com/fivdi/pigpio/master/example/distance-hc-sr04.png)


Le **script** suivant va périodiquement renvoyer la distance mesurée par le capteur en cm.

    
    from gpiozero import DistanceSensor
    from time import sleep
    
    sensor = DistanceSensor(echo=24, trigger=23)
    while True:
        print('Distance: ', sensor.distance * 100)
        sleep(1)


(*) _Les capteurs hc-sr04 ne mesurent pas de distance en réalité mais une durée. Ils émettent un ultra-son qui rebondit sur les objets proches. En mesurant le temps entre l'émission et son écho on peut estimer la distance. Il suffit de connaître la vitesse du son dans l'air (environ 330 m/s à température ambiante)._

**Evolutions. **Elles sont sans fin. On trouve ces capteurs dans la majorité des projets de robotique grand public. Au dessus des roues avant d'un robot ils lui permettent de repérer les obstacles proches...


### Mouvement : PIR


Les capteurs de mouvement qu'on trouve facilement sont généralement des [PIR](https://en.wikipedia.org/wiki/Passive_infrared_sensor). Ce sont des capteurs infrarouge qui détectent l'émission de rayonnement infrarouge dans un angle devant eux. Tous les objets émettent du rayonnement électromagnétique (la longueur d'onde de ce rayonnement dépend de la température de l'objet. Un métal rougeoie quand on le chauffe beaucoup, le rayonnement n'est plus infrarouge mais visible.) et ces capteurs détectent les variations de ce rayonnement. Ils envoient alors un signal dont la durée est ajustable. Leur sensibilité l'est aussi. Ce sont les composants de base des détecteurs de mouvement qu'on trouve dans les lieux publics afin d'économiser l'énergie.

![](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/04/PIR.jpg)


**Montage**

![](https://raspberry-pi.developpez.com/cours-tutoriels/capteur/mag-pi-utiliser-port-gpio/partie-1-detection-mouvement/images/CablagePIR5.PNG)


Un PIR typique dispose d'un petit circuit imprimé avec trois pins : VCC, OUT et GND. VCC doit être relié au 5V du raspberry, le GND à l'un des grounds et enfin OUT à n'importe quel pin. Ici on emploiera le pin 7 de la numérotation BCM

Le programme suivant va imprimer du texte à chaque fois qu'un mouvement est détecté.

    
    from gpiozero import MotionSensor
    
    pir = MotionSensor(7)
    pir.wait_for_motion()
    print("Motion detected!")


Vous pouvez ajuster deux paramètres à l'aide des potentiomètres situés sous le capteur : la sensibilité et la durée d'émission.

Le montage suivant illustre ces réglages. Le potentiomètre "time" (gauche sur le plan) ajuste la durée, en tournant dans le sens des aiguilles d'une montre on l'augmente.
Le potentiomètre "sens" (droite sur le plan) ajuste la sensibilité. Elle augmente quand on tourne dans le sens des aiguilles d'une montre.

Des jumpers permettent parfois de changer de mode entre "H" : _non rettrigered_ et "L" : _rettrigered_.

![PIR_simple_test_bb](http://qkzk.xyz/wp-content/uploads/2017/06/PIR_simple_test_bb-1024x913.png)


Il ne nécessite aucun script Python pour fonctionner ! Et se contente d'éclairer la LED (protégée par une resistance 220 Ohms) quand un mouvement est détecté. Le raspberry ne sert ici que d'alimentation 5V mais puisque c'est ce que nous avons sous la main...

Les usages sont très nombreux et je préfère vous laisser chercher des projets les employant que de vous en décrire un sommaire. Retenez qu'avec ce capteur, une camera et un interrupteur reed on peut complètement surveiller l'entrée d'une pièce.


### Luminosité : Photorésistance


Une photorésistance (LDR) est un composant électronique donc la résistivité varie en fonction de la lumière qu'il reçoit : plus celle-ci est élevée, plus la résistivité baisse.

![](https://upload.wikimedia.org/wikipedia/commons/4/4e/LDR07_Light-dependent_CdS_photoresistor.jpg)


On en trouve beaucoup et les applications sont nombreuses :

_(Extrait de[ Wikipédia](https://fr.wikipedia.org/wiki/Photor%C3%A9sistance#Avantages))_



 Les détecteurs de flammes qui sont des photorésistances à détection d’infrarouges ou d’UV. À savoir que seule une forte fumée cause une inhibition du capteur UV et que la foudre ou une soudure peut le déclencher accidentellement. Pour la photorésistance à infrarouges, la présence de vapeur d’eau atténue fortement sa sensibilité.
 Les détecteurs de présence se déclinent sous deux principes différents. Un premier détectant l’augmentation du flux induit par la présence d’un corps dans le champ (principalement des capteurs à infrarouges), le second détectant la diminution du flux induit par l’ombre du corps présent dans le champ du capteur qui est plus limité que celui à infrarouges (détection dans le visible et capteur LDR plus directif).
 Les récepteurs infrarouges permettent de faire communiquer deux appareils sans contact. L’un des appareils possède un émetteur infrarouge et le second la photorésistance.
 Les détecteurs à UV qui permettent de mettre en évidence toute source d’UV et ainsi asservir la source ou détecter une fuite par exemple.
 L’allumage des lumières lorsque la luminosité diminue (éclairage public ou domestique).
 La mesure de la luminosité extérieure dans les appareils photographiques ou les ordinateurs.

Ils ont de nombreux avantages (coût faible, sensibilité élevée etc.) mais tout autant d'inconvénients (dont le principal à mes yeux est la non linéarité de la résistivité en fonction de l'entrée).

Par essence, le Raspberry Pi n'est pas prévu pour fonctionner avec des tels capteurs ! Les pins du raspberry Pi sont tous DIGITAUX. Cela signifie qu'ils renvoient "ON" s'ils détectent une tension supérieure à 2.5V et "OFF" sinon. Pas d'entre deux, pas de "mesure" précise.

On ne pourra donc utiliser directement le LDR sur un Raspberry Pi sans passer par un montage électronique.

Certains montages élaborés nécessitent quelques composants faisant justement ce travail de conversion ANALOGIQUE (qui peut varier dans le temps) vers DIGITAL (0 ou 1).

Voici le plus simple que j'ai pu trouver. Ce n'est pas le plus courant... mais il fonctionne bien !

![](https://gpiozero.readthedocs.io/en/stable/_images/light_sensor_bb.svg)


Le composant cylindrique est un condensateur 1µF (1 microFarad - cette valeur est importante !), le LDR est le petit bitogno gris, noir et rouge.

**Attention : ce type de condensateur est souvent POLARISE. Le pôle négatif est marqué d'une bande argentée le long du condensateur est sa broche est plus courte. Il va vers le ground.**

Ce montage allume une LED si de la lumière est détectée par le LDR et l'éteint sinon.


##### **Les scripts Python :**


Afficher "Light" ou "Dark" dans la console.







    
    from gpiozero import LightSensor
    
    sensor = LightSensor(18)
    
    while True:
        sensor.wait_for_light()
        print("It's light! :)")
        sensor.wait_for_dark()
        print("It's dark :(")








Executer une fonction quand la lumière change (ici qui illumine la LED).







    
    from gpiozero import LightSensor, LED
    from signal import pause
    
    sensor = LightSensor(18)
    led = LED(16)
    
    sensor.when_dark = led.on
    sensor.when_light = led.off
    
    pause()








**Sources** : le [script](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor) lui même, quelques [explications](https://gpiozero.readthedocs.io/en/stable/api_input.html#light-sensor-ldr) concernant le montage.

La lecture des sources du gpiozero est intéressante, ne serait-ce que pour réaliser à quel point il simplifie la mise en place de boutons, de leds etc.

_Un grand merci aux collèges de S.I. Christophe B. et Yann L-G. pour m'avoir expliqué en détail le fonctionnement de ce montage qui me renvoyait vingt ans en arrière durant ma prépa :)_

Ce montage n'est pas le plus couramment employé. On préfère lire la résistivité à l'aide d'un convertisseur analogique-digital et obtenir une valeur précise. Un Arduino est donc bien meilleur pour ce type de capteur.


### Humidité et température : DHT22


A nouveau, gpioZero ne propose pas de librairie spécifique pour ce capteur. Remarquons qu'il existe d'autres capteurs jouant le même rôle, celui-ci est simplement celui dont je dispose (l'ayant mis en place chez moi) : On est le 20 juin et il fait 32 degrés. J'ai mis des glaçons sous le panier du chat parce qu'il a l'air mal en point. BREF.

Les capteurs DHT11 et DHT22 fonctionnent sur le même principe :

_Le DHT22 est un capteur de température et humidité simple et peu couteux. Il utilise un capteur d'humidité à capacitance et un thermistor pour mesurer l'air ambiant et renvoie un signal digital sur le pin data. Il est plutôt simple d'usage mais requiert un timing précis pour relever les données. Le seul soucis de ce capteur est qu'il ne peut publier ses donnée que toutes les 2 secondes. (cf Adafruit)_

Cette fois je vous renvoie carrément[ à la librairie](https://github.com/adafruit/Adafruit_Python_DHT) d'Adafruit. Vous devriez avoir compris le principe.



 	  1. On l'installe (lisez la page d'accueil)
 	  2. On monte le capteur et teste le script. Les liens sont dans **[examples](https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/simpletest.py).**



##### Montage


![](http://www.manuel-esteban.com/wp-content/uploads/2013/04/Raspberry-et-DHT22_bb.jpg)


Les branchements sont les suivants :



 Le Pin 1 de la sonde va vers l’alim 3,3V du Raspberry
 Le Pin 2 va vers un pin du Raspberry Pi (le pin 4 dans mon exemple).
 Le Pin 3 … ne sert à rien ![:)](http://www.manuel-esteban.com/wp-includes/images/smilies/icon_smile.gif)

 Le Pin 4 va vers le Ground du Raspberry Pi
 Une resistance (de 4700 ohm à 10K Ohm) se branche entre le pin 2 et l’alim (à connecter en premier, avant la sortie vers le pin 4 du raspberry pi).



##### Software


Les outils Adafruit ont été déplacés sur github et consistent maintenant en une librairie C que nous devrons utiliser dans un script python.

Récupérons les sources et compilons la bibliothèque DHT.







    
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git
    cd Adafruit_Python_DHT
    sudo apt-get update
    sudo apt-get install build-essential python-dev python-openssl
    sudo python setup.py install







Une fois terminé et pour tester cela, on exécute la commande suivante (pour un  DHT11) , un DHT 22 sera interrogé par Adafruit_DHT 22 XX, XX étant le numéro du GPIO concerné.









    
    cd examples
    sudo ./AdafruitDHT.py 22 4
    Temp=23.0* Humidity=37.0%













_Vous ne devriez pas être concerné par le problème suivant mais sait-on jamais..._




Attention : le message d’erreur ci-dessous indique que le mode « device-tree » n’est pas activé sur le Raspberry.






    
    Traceback (most recent call last):
    File "./AdafruitDHT.py", line 41, in &lt;module&gt;
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    File "build/bdist.linux-armv7l/egg/Adafruit_DHT/common.py", line 90, in read_retry
    File "build/bdist.linux-armv7l/egg/Adafruit_DHT/common.py", line 77, in read
    File "build/bdist.linux-armv7l/egg/Adafruit_DHT/Raspberry_Pi_2.py", line 34, in read
    RuntimeError: Error accessing GPIO.










Tapez sudo raspi-config puis dans le point 8 « Advanced Options », faites un « Enable Device Tree » et **rebootez**.










Vérifiez que tout fonctionne avec : sudo ./AdafruitDHT.py 22 4











Le 22 étant le type de DHT que vous avez (11 ,22 ou 2302) et 4 le numéro du GPIO que vous avez câblé.

OK tout est bon on a température et humidité !


##### **Evolutions.**


Adafruit propose un tutoriel permettant d'[updater une page google drive](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview) afin de créer une base de donnée de température et tracer des courbes simplement. Pourquoi pas.

De façon moins rudimentaire un joli projet consiste à stocker les données dans une base de donnée SQlite et les afficher dans une page web (qui demande alors un petit serveur web). C'est tout à fait faisable et les effets peuvent-être bluffants. (Je trouve).

![download](http://qkzk.xyz/wp-content/uploads/2017/06/download.png)


Puisque je vous dis qu'il fait trop chaud, vous me croyez maintenant ?






### Servo moteur




##### Présentation


Le moteur inclus dans le Starter Kit est un petit servomoteur de modélisme. Il n'est pas conçu pour des applications nécessitant une très grande force (tirer un char d'un kg...), mais il est possible de contrôler précisément la rotation de l'axe, entre 0 et 180°. Il sert généralement à orienter les roues d'un véhicule. Il existe des servomoteurs à rotation continue, qui permettent de régler la vitesse de rotation de l'axe.

**Les servomoteurs sont contrôlés par des impulsions de durée variable. Seuls deux pins du raspberry 2 (un seul sur le modèle 1) en sont capables sans passer par le système d'exploitation : les pins 12 et 18 (notation PWM).
Remarque : gpioZero contourne ce problème !**


##### Principe


La position d'un servomoteur est donnée par la durée d'une pulsation. Le servomoteur attend des pulsations tous les 20 millisecondes environ. Si cette pulsation est "high" pendant 1 milliseconde, l'angle sera à zéro. Si cette pulsation dure 1,5 millisecondes, il sera au centre. Si elle dure 2 millisecondes, il sera à 180 degrés.

![servo](https://cdn-learn.adafruit.com/assets/assets/000/003/496/medium640/learn_raspberry_pi_servos.png?1396797327)


[gpioZero](http://gpiozero.readthedocs.io/en/stable/api_output.html#servo) propose une panoplie complète pour manipuler un servomoteur. Son avantage sur d'autres librairies similaires est ENORME, on peut utiliser n'importe quel pin du raspberry.

**Montage**

Reliez l'alimentation 5V du rasperry au câble rouge du servo ; le ground du raspberry au câble marron du servo et, par exemple, le câble jaune au pin 17 (bcm).

**Programme
**

Le programme suivant va déplacer le servo entre ses positions minimales, centrales et maximales en faisant des pauses entre chaque étape.

    
    from gpiozero import Servo
    from time import sleep
    
    servo = Servo(17)
    while True:
        servo.min()
        sleep(1)
        servo.mid()
        sleep(1)
        servo.max()
        sleep(1)









D'autres exemples sont disponibles chez gpio zero pour le manipuler plus finement.

**Projets**




 	    * Utiliser un servo pour orienter une camera dans une direction, tournant régulièrement et offrant un angle plus
large.
 	    * Créer un pan/tilt en attachant deux servos moteurs. On pourra ainsi orienter la caméra dans beaucoup plus de directions.
![](http://www.robotshop.com/media/catalog/product/cache/1/image/900x900/9df78eab33525d08d6e5fb8d27136e95/s/e/servocity-spt50-sub-micro-pan-tilt-kit-hs55-servos-1_1.jpg)

 	    * Toujours avec un pan tilt, cette fois remplacer la caméra par un laser... et vous pouvez créer un script qui oriente vise des points aléatoires au sol pour amuser votre chat. J'ai dû mettre une LED à la place du laser mais vous comprenez le principe.
**Attention : les lasers sont dangereux, ils peuvent détruire les cellules de la rétine et rendre aveugle. Soyez prudent, cela arrive plus vite que vous ne le pensez peut-être.**


![laserCat_bb](http://qkzk.xyz/wp-content/uploads/2017/06/laserCat_bb-1024x787.png)


Le projet complet [en action](https://learn.adafruit.com/raspberry-pi-wifi-controlled-cat-laser-toy/overview).





