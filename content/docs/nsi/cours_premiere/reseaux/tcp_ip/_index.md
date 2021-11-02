---
title: Protocoles TCP et IP
bookCollapseSection: true
author: David Roche
weight: 2
---

### pdf : [ce document, pour impression](/uploads/docsnsi/reseau/nsi_prem_tcpip.pdf) - [fiche de révision](/uploads/docsnsi/reseau/16_protocoles_tcp_ip.pdf)

Pour communiquer ensemble, 2 ordinateurs en réseau doivent utiliser des
règles communes, l'ensemble de ces règles qui permettent à 2
ordinateurs de communiquer ensemble s'appelle un protocole.

Il existe de nombreux protocoles réseau, nous allons en étudier 2 : le
protocole TCP et le protocole IP. Ces 2 protocoles sont tellement liés
l'un à l'autre que l'on parle souvent du protocole TCP/IP.

Avant d'entrer dans le vif du sujet, un peu d'histoire :

La DARPA (Defense Advanced Research Projects Agency) voit le jour en
1958, cette agence gouvernementale américaine a pour but de veiller à la
constante suprématie des États unis en matière technologique et
scientifique. En 1962 la DARPA soutient le projet du professeur
Licklider qui a pour but de mettre en réseau les ordinateurs des
universités américaines afin que ces dernières puissent échanger des
informations plus rapidement (même à des milliers de kilomètres de
distance). En 1968, ARPAnet, 1er réseau informatique à grande échelle de
l'histoire voit le jour. Le 29 octobre 1969, le 1er message (le mot
"login") est envoyé depuis l'université de Californie à Los Angeles
vers l'université de Stanford via le réseau ARPAnet (les 2 universités
sont environ distantes de 500 Km). C'est un demi-succès, puisque seules
les lettres "l" et "o" arriveront à bon port. En 1972, 23
ordinateurs sont connectés à ARPAnet (on trouve même des ordinateurs en
dehors des États unis). En parallèle au projet ARPAnet, d'autres
réseaux voient le jour, problème, ils utilisent des protocoles de
communication hétéroclite (UUCP, NCP ou encore X.25) et 2 ordinateurs
appartenant à 2 réseaux différents sont incapables de communiquer entre
eux puisqu'ils n'utilisent les mêmes protocoles. En 1974 Vint Cerf et
Bob Khan vont mettre au point le protocole TCP qui sera très rapidement
couplé au protocole IP pour donner TCP/IP. TCP/IP, grâce à sa
simplicité, va très rapidement s'imposer comme un standard : les
différents réseaux (ARPAnet et les autres) vont adopter TCP/IP. Cette
adoption va permettre d'interconnecter tous ces réseaux (2 machines
appartenant à 2 réseaux différents vont pouvoir communiquer grâce à
cette interconnexion). Internet était né (le terme Internet vient de
"internetting" qui signifie "Connexion entre plusieurs réseaux").
TCP/IP est donc au coeur d'Internet, voilà pourquoi aujourd'hui, la
plupart des machines utilisent TCP/IP.

Après ce petit rappel historique, essayons de comprendre le principe de
base des protocoles TCP (Transmission Control Protocol) et IP (Internet
Protocol)

Quand un ordinateur A "désire" envoyer des données à un ordinateur B,
l'ordinateur A "utilise" le protocole TCP pour mettre en forme les
données à envoyer.

Ensuite le protocole IP prend le relai et utilise les données mises en
forme par le protocole TCP afin de créer des paquets des données. Après
quelques autres opérations qui ne seront pas évoquées ici, les paquets
de données pourront commencer leur voyage sur le réseau jusqu'à
l'ordinateur B. Il est important de bien comprendre que le protocole IP
"encapsule" les données issues du protocole TCP afin de constituer des
paquets de données.

![](/uploads/docsnsi/reseau/img/TCP_IP_1.jpg)

Une fois arrivées à destination (ordinateur B), les données sont
"désencapsulées" : on récupère les données TCP contenues dans les
paquets afin de pouvoir les utiliser.

![](/uploads/docsnsi/reseau/img/TCP_IP_2.jpg)

Le protocole IP s'occupe uniquement de faire arriver à destination les
paquets en utilisant l'adresse IP de l'ordinateur de destination. Les
adresses IP de l'ordinateur de départ (ordinateur A) et de
l'ordinateur destination (ordinateur B) sont ajoutées aux paquets de
données.

![](/uploads/docsnsi/reseau/img/TCP_IP_3.jpg)

Le protocole TCP permet de s'assurer qu'un paquet est bien arrivé à
destination. En effet quand l'ordinateur B reçoit un paquet de données
en provenance de l'ordinateur A, l'ordinateur B envoie un accusé de
réception à l'ordinateur A (un peu dans le genre "OK, j'ai bien reçu
le paquet"). Si l'ordinateur A ne reçoit pas cet accusé de réception
en provenance de B, après un temps prédéfini, l'ordinateur A renverra
le paquet de données vers l'ordinateur B.

Nous pouvons donc résumer le processus d'envoi d'un paquet de données
comme suit :

![](/uploads/docsnsi/reseau/img/TCP_IP_4.png)

À noter qu'il existe aussi le protocole UDP qui ressemble beaucoup au
protocole TCP. La grande différence entre UDP et TCP est que le
protocole UDP ne gère pas les accusés de réception. Les échanges de
données avec UDP sont donc moins fiables qu'avec TCP (un paquet
"perdu" est définitivement "perdu" et ne sera pas renvoyé) mais
beaucoup plus rapides (puisqu' il n'y a pas d'accusé de réception à
transmettre). UDP est donc très souvent utilisé pour les échanges de
données qui doivent être rapides, mais où la perte d'un paquet de
données de temps en temps n'est pas un gros problème (par exemple le
streaming vidéo).

Il est très important de bien comprendre que TCP/IP repose sur la notion
de paquets de données. Si par exemple on désire envoyer un fichier (son,
photo, vidéo ou texte, peu importe, dans tous les cas on envoie une
succession de bits) en utilisant TCP/IP, les données qui constituent ce
fichier ne seront pas envoyées d'un seul tenant, ces données vont être
"découpées" en plusieurs morceaux et chaque morceau sera envoyé dans
un paquet différent. Une fois tous les paquets arrivés à destination, le
fichier d'origine pourra être reconstitué. Pour aller d'un ordinateur
A à un ordinateur B, les différents paquets contenant les données qui
constituent notre fichier, ne passeront pas forcement par la même route
(cette notion de route sera abordée plus tard), ils pourront emprunter
des chemins très différents : en exagérant à peine, pour faire le trajet
Paris-Los Angeles, certains paquets pourront passer par l'atlantique
alors que d'autres passeront par le pacifique. Si un des paquets
n'arrive pas à destination, le fichier ne pourra pas être reconstitué,
le paquet "perdu" devra être renvoyé par l'émetteur (voir le système
d'accusé de réception décrit ci-dessus).

![](/uploads/docsnsi/reseau/img/nsi_prem_tcpip_1.png)
