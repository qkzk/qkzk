---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: GPIO Zero
weight: 1
---


# GPIO Zero


_Cette brève présentation est une traduction de la page d'accueil de la [documentation officielle](https://gpiozero.readthedocs.io/en/stable/) de la librairie._

## GPIO Zero

**Attention : GPIO Zero est une librairie exclusive au Raspberry Pi.**

Elle permet d'utiliser facilement le raspberry pour utiliser des composants
électroniques de base (LED, bouton, servo moteur etc) via son interface GPIO.

La majorité des fonctions sont déjà développées et il suffit de réaliser
le montage.

## Usage

Des composants sont proposés pour permettre de démarrer l'informatique matérielle
sans accroc.

~~~python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
~~~

Avec très peu de code, vous pouvez facilement connecter des composants

~~~python
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()
~~~


Vous pouvez vous permettre de respecter des conventions de nommage
pour décrire vos objets et leurs intéractions :

~~~python
from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause

garden = LED(17)
motion = MotionSensor(4)
light = LightSensor(5)

garden.source = all_values(booleanized(light, 0, 0.1), motion)

pause()
~~~

La librairie comporte des des interfaces pour la majorité des composants
simples ainsi que pour des éléments plus complexes tels que des capteurs,
convertisseurs analogique / digital, LED RGB, kits robotiques et plus encore.

## Gestion des PINS

GPIO Zero tire parti de nombreuses librairies de manipulation des PINS telle que
RPi.GPIO et pigpio. Vous pouvez choisir quelle librairie utiliser, que ce soit
pour le script entier ou pour un composant particulier.

## Installation

GPIO Zero est installée par défaut sur les images bureau Raspbian
(ceux du lycée) disponible sur
[rapsberry.org](https://www.raspberry.org/download). Pour l'installer sur
raspbian lite ou un autre système d'exploitation, comme un PC utilisant
un GPIO à distance suivre [ce lien.](https://gpiozero.readthedocs.io/en/stable/installing.html)
