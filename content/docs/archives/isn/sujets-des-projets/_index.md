---
author: qu3nt1n
date: 2016-07-01 12:56:59+00:00
draft: false
title: Sujets des mini projets - Liste des projets
bookCollapseSection: true
weight: 3
---







# Sujets des mini-projets 2019


![ZV3FWKD](/uploads/uploads/2016/07/ZV3FWKD-1024x768.jpg)










Le choix du mini-projet est déterminant pour la suite. Je ne vous laisserai pas aborder un projet final demandant du canvas si vous n'en n'avez jamais fait.



---


### Le score du Ping-Pong - html, javascript, éventuellement canvas - abordable


Dans une page html on affichera trois boutons (au moins) et le score détaillé d'une partie de ping-pong.
L'arbitre pourra, en appuyant sur un des boutons enregristrer un point marqué par un joueur. La gestion des sets et de la fin de partie sera prise en compte. L'arbitre pourra aussi remettre à zéro les scores.
Un état de la partie sera affiché indiquant aussi qui doit servir.
On enregristera le déroulé de la partie (l'ordre des points) dans un tableau afin d'afficher des statistiques (point marqué quand on sert etc.)
Extentions : on pourra indiquer le type de point : faute (nature ?), coup direct, ace etc.
On pourra, éventuellement, afficher des animations dans un canvas ou simplement avec des images.

---


### Pong - html, javascript, canvas - abordable


Canvas est un élément html5 qui permet d'afficher et de manipuler des images 2d ou 3d constituées de pixels manipulables en javascript.
Ce miniprojet vise à l'apprentissage du canvas en vue d'un projet final.

![](http://amigamuseum.emu-france.info/Fichiers/Biographie/images/pong/pong.gif)


Pong : le jeu historique et bien connu. 2 Raquettes défendant chacune un but (bords gauche et droit) se déplacent verticalement et font rebondir une balle. Celle-ci rebondit aussi sur les murs.
Il sera réalisé dans une page html contenant un canvas qui permet l'affichage et l'animation d'objets. On développera d'abord la version deux joueurs sur un même clavier (l'ordinateur ne joue pas). Un tutoriel presque complet est disponible [ici.](/docs/isn/isn-travaux-pratiques/4-programmation/4-12-tutoriel-pong-en-javascript/)La dernière partie (l'ordinateur joue contre vous) n'est pas détaillée dans ce tutoriel. On L'envisagera en deux temps : 1. Quelle ordonnée doit-il viser ? 2. Il se déplace étape par étape.
**Extension :** les niveaux de difficulté.


---


### Feu de forêt - html, javascript, canvas - assez difficile


Canvas est un élément html5 qui permet d'afficher et de manipuler des images 2d ou 3d constituées de pixels manipulables en javascript.
Ce miniprojet vise à l'apprentissage du canvas en vue d'un projet final.

Dans ce mini-projet vous allez réaliser un cadre contenant des blocs carrés pouvant prendre 4 états (vide, arbre vivant, arbre en feu, cendres).
A chaque étape, un arbre en feu enflamme ses voisins directs puis se consume et s'éteint (il devient de la cendre). C'est donc un réseau d'automates cellulaires. Le feu apparaît à gauche et se transmet donc de proche en proche. Après un nombre fini d'étapes, tous les arbres sont soit consumés soit toujours vivants.

Le programme demande une probabilité à l'utilisateur (entre 0 et 1) et génère aléatoirement la carte initiale où tous les arbres sont vivants. Le feu apparaît ensuite à partir de la gauche et se déplace en fonction des cellules qui l'entourent.

C'est un mini-projet ambitieux qui demande un investissement certain pour les novices. Il permettra d'aborder les projets les plus difficiles avec confiance.

[Projet](http://mathematice.fr/chapitre.php?menu=isn&num=12) similaire déjà réalisé en ISN.

---


### Réalisation d'une animation en p5js - html, javascript + p5js, canvas - moyen.






**p5js** est la librairie javascript adaptée de processing. Elle permet de réaliser très simplement des animations et du traitement de l'image à intégrer dans une page html ou un programme.
C'est une librairie dont la prise en main est simple mais qui s'avère très puissante.
Votre mini projet consiste à suivre les [activités](https://pixees.fr/informatiquelycee/p5_base_a1.html) réalisées par un collègue et ensuite à réaliser soit :

* (facile) une animation automatique présentant des bulles qui rebondissent les unes sur les autres en changeant de couleur.
* (moyen) du traitement vidéo depuis un flux vidéo récupéré par une webcam. A nouveau un tutoriel en deux parties ([1.](https://pixees.fr/informatiquelycee/p5_Img_a1.html) [2.](https://pixees.fr/informatiquelycee/p5_vid_a1.html)) est disponible.

L'objectif de ce mini-projet est la prise en main de p5js afin de réaliser **ensuite** un jeu vidéo complet en p5js. Les animations et transformations sont grandement simplifiées par p5js et votre projet final devra donc aller un peu plus loin qu'un simple jeu dans un canvas.

Remarquons que processing est à l'origine de deux autres projets majeurs que vous connaissez peut-être : **arduino** et **fritzing**.


---


### Prise en main et utilisation du Raspberry-Pi et découverte de Python


Micro ordinateur disposant de nombreux ports embarqués (usb, hdmi, jack, réseau etc.) le raspberry-pi est l'outil idéal pour commencer la programmation et l'electronique embarquée.

Durant ce mini projet vous apprendrez à vous en servir : installation d'un OS (raspbian), fonctions de base de linux, GPIO.

Le GPIO (General Purpose In and Out) : des broches raccordées à la carte mère permettant de capter ou transmettre un signal et permettant donc de communiquer avec l'extérieur.
Le raspberry Pi est un outil d'initiation à la programmation avec une visée électronique. Apprendre à diriger un objet ou à récupérer de l'information et la présenter.

**Objectifs indispensables pour le raspberry-pi** :

* Installation de l'OS
* Prise en main de linux et contrôle à distance depuis une autre machine réseau
* Intégration de capteurs et présentation dans une petite page web de leurs valeurs.
* Animation de quelques leds en fonction d'événements extérieurs

Afin de communiquer avec le GPIO l'apprentissage d'un nouveau langage est nécessaire et vous découvrirez donc Python.

**En parallèle vous devrez donc vous initier à Python.**
Les cours que vous allez suivre sont [ici](/docs/nsi/cours-python/_index.md). S'ils ne vous conviennent pas, de bonnes sources en français sont disponibles sur le site d'[OpenClassrooms](http://openclassrooms.com/courses/apprenez-a-programmer-en-python) (inscription nécessaire).

Ce mini projet est indispensable pour aborder un projet final demandant le Raspberry-Pi. Deux ou trois projets utilisant le raspberry Pi peuvent se dérouler en même temps. Pas plus.






## Contraintes des mini-projets.





Les mini-projets se font en groupe de 3. Aucun élève ne préparant de projet seul. Les groupes sont établis, gravés dans la roche et numérotés durant la première séance. Les mini projets sont à rendre un mois plus tard. Le projet concernant le Rpi ne pouvant être traité que trois fois.
Les documents seront partagés dès leur création via le drive, dans un dossier spécifique s'intitulant "Mini projet 2018 - groupe 3". Le code sera convenablement commenté. Les commentaires seront évalués.

Chaque élève créera un dossier projet dans google drive à l'aide de google docs et le partagera au professeur.

**Le dossier projet.
**Vos mini-projets seront accompagnés d'un dossier-projet. C'est un **document** réalisé à l'aide d'un **traitement de texte** (docs intégré dans google drive est parfait) et **exporté en .pdf**. Il doit **comporter 4 pages de contenu** (5 pour celui du projet final) hors annexe (votre code ira en annexe) et hors illustrations.
Vous y présentez le projet, son cahier des charges et vos réalisations. Les étapes intermédiaires (idées incorrectes, réalisations non abouties, ambitions démesurées) peuvent figurer mais ne peuvent constituer l'essentiel de votre travail. Vous pouvez aussi extraire quelques lignes pertinentes de code et les commenter en détail.
Le dossier projet sera évalué et constituera une partie de votre note.

**Les mini-projets constitueront l'essentiel de la note du deuxième trimestre.**







## Sujets des projets 2020 :


![](http://static.nautil.us/5779_7d3d5bcad324d3edc08e40738e663554.png)








* [Le compte est bon - Javascript- abordable](/docs/isn/sujets-des-projets/archives/le-compte-est-bon)
* [2048 - python + pygame ou javascript + canvas/p5js - abordable / intémédiaire](/docs/isn/sujets-des-projets/2048-projet)
* [ZagZig : JS, Canvas - intermédiaire](/docs/isn/sujets-des-projets/zagzig-js-canvas)
* [Jeu de la vie - Canvas - intermédiaire](/docs/isn/sujets-des-projets/jeu-de-la-vie)
* [Space orbit - p5js - intermédiaire](/docs/isn/sujets-des-projets/space-orbit)
* [Stack - html, js, canvas - difficile](/docs/isn/sujets-des-projets/stack)
* [Video Surveillance : Raspberry Pi, Python, Linux, Electronique - intermédiaire](/docs/isn/sujets-des-projets/video-surveillance-rpi-python)
* [Papy Panic : Raspberry Pi, Python, Linux, Electronique - assez difficile](/docs/isn/sujets-des-projets/papy-panic-rpi-python)
* [Domotique et raspberry Pi - très difficile](/docs/isn/sujets-des-projets/domotique-et-raspberry-pi)
* [Abelian Sandpile : automate cellulaire en Python (ou autre) - difficulté variable (peut monter très haut).](/docs/isn/sujets-des-projets/sandpiles)
* [Bowling Parallaxe : très sommaire, en fausse 3D et avec une gestion simplifiée des collisions. (intermédiaire - difficile)](/docs/isn/sujets-des-projets/bowling-paralaxe)
* [Bowling Elastique : une version apauvrie mais néanmoins intéressante du bowling. Extension vers le mouvement Brownien... (difficile)](/docs/isn/sujets-des-projets/bowling-elastique)
* [Othello (Reversi) : à deux joueurs (intermédiaire) et contre l'ordinateur (expert)](/docs/isn/sujets-des-projets/othello-reversi).
* [Rogulelike (difficile / expert)](/docs/isn/sujets-des-projets/rogulike)
* [Chemins Hamiltoniens sur les polyèdres (difficile / expert)](/docs/isn/sujets-des-projets/chemins_hamiltoniens_polyedres)
* [Labyrinthes (moyen / difficile) : générer et résoudre des labyrinthes](/docs/isn/sujets-des-projets/labyrinthe)
* [SmartCity : le lampadaire connecté](/docs/isn/sujets-des-projets/smartcity/)

D'autres projets sont possibles mais n'ont pas été décrits :

* **Bot telegram** : créer un bot contrôle a distance d'un raspberry pi OU jeu vidéo dans un channel - intéressabt mais aucune documentation en français. Le projet est vite fonctionnel mais nécessite trop d'outils à mes yeux.
* **Correcteur orthographique utilisant la distance de Leveinshtein.** Intéressant mais la difficulté n'est pas progressive. Une fois les premiers outils mis en place (distance, dictionnaire) la réalisation du correcteur est délicate.
* **Cryptographie** - passage en revue de méthodes célèbres ou étude exhaustive du chiffre de Vigenère. Demande un investissement certain. Envisageable pour qui a déjà quelques notions de Cryptographie ou souhaite progresser en mathématiques.<br>
Il est possible de traiter d'abord un mini-projet pour se familiariser, par exemple en suivant ces activités proposées aux élèves d'ICN première : [Code César, Substitution simple](/docs/icn/2-Cryptographie), [lexicométrie](/docs/icn/1-lexicometrie), [analyse fréquentielle](/docs/icn/3-casser-un-code-secret).<br>
De nombreuses extensions sont possibles : stéganographie (moyen), chiffrement asymétrique RSA (difficile), symétrique AES (expert). _Le chiffrement asymétrique couvre une grande partie du programme de la spécialité mathématiques de TS._
* **Hero Stick** - pour ceux qui ne connaîtraient pas, [une vidéo](https://www.youtube.com/watch?v=Ph0LxvHM_EQ). C'est plus difficile à développer qu'il n'y paraît.

D'autres idées en vrac :

* **Fourmis de Langton** : faisable
* **Fractales** : ensemble de Mandelbrodt (facile d'accès, plus délicat ensuite), Dragon Curve (moins facile mais très documenté),
* **PacMan** (version "perso" avec comportement simplifié des fantômes : abordable, version complète avec les comportements d'origine : plus délicat)
* **Logistic Map** : étude du comportement de suites récurrentes "simples" - la genèse du chaos.

[caption id="" align="alignleft" width="248"]![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/LogisticCobwebChaos.gif/220px-LogisticCobwebChaos.gif)
Les suites récurrentes réservent quelques surprises ![/caption]

[caption id="" align="alignleft" width="373"]![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Logistic_Bifurcation_map_High_Resolution.png/640px-Logistic_Bifurcation_map_High_Resolution.png)
Logistic Map[/caption]








##  Archives des sujets proposés les années précédentes :

Elles sont toutes disponibles en dépliant le dossier **isn/sujets-des-projets/archives**.

Il suffit de le déplier.
