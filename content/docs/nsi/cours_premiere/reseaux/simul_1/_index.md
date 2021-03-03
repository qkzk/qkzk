---
title: Simulation réseau
author: David Roche
weight: 5
---

### pdf : [pour impression](/uploads/docsnsi/reseau/nsi_prem_simReseau1.pdf)

Après la théorie, passons maintenant à la pratique. Il est un peu
difficile de mettre en place un réseau pour effectuer quelques tests. À
la place, nous allons utiliser un simulateur de réseau. Il existe
différents types de simulateurs : du plus simple au plus
"professionnel". Nous allons utiliser un simulateur relativement
simple à prendre en main, mais suffisamment performant :
[Filius](http://www.lernsoftware-filius.de/Herunterladen) (la page web
est en allemand, mais le logiciel est disponible en anglais).

Avant de visionner une petite vidéo qui devrait vous aider à prendre en
main Filius, quelques petites indications

Nous allons utiliser deux commandes dans la vidéo :

-   "ipconfig" qui permet de connaitre la configuration réseau de la
    machine (adresse IP, adresse MAC\...) sur laquelle est exécutée
    cette commande ("ipconfig" est une véritable commande sous Windows
    de Microsoft, sous les systèmes de type Unix (Linux ou macOS par
    exemple), la commande équivalente est "ifconfig")
-   "ping" qui permet d'envoyer des paquets de données d'une machine
    A vers une machine B. Si la commande est exécutée sur la machine A,
    le "ping" devra être suivi par l'adresse IP de la machine B (par
    exemple, si l'adresse IP de B est "192.168.0.2", on aura "ping
    192.168.0.2")

Autre chose à retenir, vous allez peut-être apercevoir dans cette vidéo
un "netmask" (masque de réseau en français), vous devez juste savoir
que :

-   pour une adresse du type a.b.c.d/8, on a un netmask qui est
    "255.0.0.0"
-   pour une adresse du type a.b.c.d/16, on a un netmask qui est
    "255.255.0.0"
-   pour une adresse du type a.b.c.d/24, on a un netmask qui est
    "255.255.255.0"

Vous pouvez maintenant visionner la vidéo (n'hésitez pas à aller sur
YouTube pour un meilleur confort de lecture).

Lien vers la [vidéo](https://youtu.be/nzuRSOwdF5I)

#### À faire vous-même 1

En utilisant le logiciel Filius, créez un réseau de 4 machines (M1, M2,
M3 et M4). L'adresse IP de la machine M1 est "192.168.1.1",
choisissez les adresses IP des machines M2, M3 et M4.

Effectuez un "ipconfig" sur la machine "M1" afin de vérifier son
adresse IP et de déterminer son adresse MAC (adresse physique)

Effectuez un "ping" de la machine M2 vers la machine M4.

#### À faire vous-même 2

Visionner les vidéos "filius 2" à "filius 4" et reproduire les manipulations
présentées.

* [filius 2](https://www.youtube.com/watch?v=xyK6ThdQeR0)
* [filius 3](https://www.youtube.com/watch?v=K3GGmiLwB6U)
* [filius 4](https://www.youtube.com/watch?v=EZp_TLGVyv0)
