---
title: ressources
bookCollapseSection: true
author: qkzk
date: 2017-06-22 08:47:43+00:00
draft: false
weight: 6
---



# Programmes officiels de la NSI

1. [première](https://cache.media.education.gouv.fr/file/SP1-MEN-22-1-2019/26/8/spe633_annexe_1063268.pdf)
2. [terminale](https://cache.media.education.gouv.fr/file/SPE8_MENJ_25_7_2019/93/3/spe247_annexe_1158933.pdf)
3. [document d'accompagnement](https://eduscol.education.fr/cid144156/nsi-bac-2021.html#lien1)


# Logiciels et outils employés

## Un éditeur de texte parmi :

* [Thonny](https://thonny.org/) Thonny est un éditeur de texte adapté aux débutants. Il ne fonctionne que pour Python.
* [Atom](https://atom.io/) Éditeur de texte développé javascript par github. Très extensible, il fonctionne sur toutes les plateformes. C'est celui que j'utilise.
* [Sublime Text](http://www.sublimetext.com/) Editeur de texte complet et multi plateformes (windows, osx, linux). C'est un freemium : l'acheter débloque de nouvelles fonctions (peu utiles).
* [Visual Studio](https://code.visualstudio.com/). Le petit chouchou actuel. Très puissant.

Citons ceux qui ont du succès : [PyCharm](https://www.jetbrains.com/pycharm/) et [vim](https://www.vim.org/)

## Outils en ligne

* [Google Drive](https://drive.google.com) Cloud de google, disposant d'une suite bureautique intégrée et de versions pour toutes les plateformes.
* [Google Classroom](https://classroom.google.com) Si tout se passe comme prévu, vous devriez déjà avoir un compte et être familier.
* [Colab](https://colab.research.google.com/) Python en ligne dans google drive. Jupyter Notebook sans devoir administrer un serveur.
* [repl.it](https://repl.it/) pour développer en ligne dans tous les langages. À nouveau, vous devriez en avoir entendu parler...
* [github](https://github.com/) est le dépôt git le plus populaire. On y trouve énormément de projets dont linux, python, node.js, react...


## Python

* [python](https://www.python.org/) le site officiel
* [dépôt python](https://github.com/python/cpython) sur github. Si vous voulez voir l'envers du décor.
* [Pypi](https://pypi.org/) là où sont hebergés les paquets installés ave `pip install ...`


### Librairies python pratiques

Toutes sont accessibles dans pip.

* [pygame](https://www.pygame.org/news) : la librairie jeux vidéos la plus couramment employée sous python,
* [pygame zero](https://pygame-zero.readthedocs.io/en/stable/index.html) : la version "accessible" de cette même librairie,
* [network zero](https://networkzero.readthedocs.io/) : le réseau pour les débutants,
* [gui zero](https://lawsie.github.io/guizero/) : créer des fenêtres jolies et facilement,
* [gpio zero](https://gpiozero.readthedocs.io/en/stable/installing.html) : manipuler facilement le gpio d'un raspberry pi,
* [flask](https://flask.palletsprojects.com/) permet de créer des sites web. La référence Python pour les microservices. Permet de créer une page "hello world!" mais est aussi utilisé par Netflix, reddit, Lyft, le MIT et Zalando...
* [matplotlib](https://matplotlib.org/) : dessiner des figures scientifiques,
* [numpy](https://numpy.org/) : calcul numériques de précision,
* [les outils google](https://developers.google.com/) : pour contrôler à peu près tout ce qu'ils proposent (gmail, calendar, classroom etc.)
* [selenium](https://selenium-python.readthedocs.io/) permet de piloter le navigateur depuis Python "clic ici, remplit tel champ, charge telle page". Permet d'automatiser le contrôle.
* [l'api discord](https://discordpy.readthedocs.io/en/latest/api.html) pour créer des bots Discord,
* [l'api telegram](https://python-telegram-bot.org/) pour créer des bots Telegram,
* [l'api twitter](https://python-twitter.readthedocs.io/en/latest/) pour créer des bots Twitter,


## D'autres logiciels

Les outils réseau

1. [Filius](http://www.lernsoftware-filius.de/Herunterladen) est un simulateur réseau facile d'accès. (utilisez google trad si vous ne comprenez pas l'allemand)
2. [Cisco Packet Tracer](https://www.netacad.com/fr/courses/packet-tracer/introduction-packet-tracer) La même chose mais pour les professionnels. Beaucoup plus puissant. Le maîtriser complètement suffit à trouver du travail.
3. [Wireshark](https://www.wireshark.org/) est un analyseur de paquets réseau. Libre et gratuit.

Divers

* [sqlite](https://www.sqlite.org/index.html) implémente une bdd SQL stockée dans des fichiers. Très pratique et facile d'accès. Directement intégrée à Python.
* [sqlite browser](https://sqlitebrowser.org/) permet de manipuler ces bdd dans un environnement fenétré.
* [sqlite tutorial](https://www.sqlitetutorial.net/) présente toutes les commandes de sqlite avec des exemples faciles à comprendre. Très commode.

## Ref cards

* [unix](/uploads/docsnsi/pdf/unix-refcard.pdf)
* [Python 3](https://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html)
* [js](https://htmlcheatsheet.com/js/)

# Références en français


* [OpenClassRooms](http://fr.openclassrooms.com/informatique/cours/dynamisez-vos-sites-web-avec-javascript) : LA référence en français, complète et didactique (anciennement : site du zéro).
* [France IOI](http://www.france-ioi.org/algo/chapters.php) : Site d'entrainement à la programmation et à l'algorithmique. De nombreux cours et exercices interactifs dans plusieurs langages (Python, C, C++, Python, Java, CAML etc.)
* [Le manuel de référence, édité par l'INRIA.](/uploads/docs/livreISN.pdf) Il est mis à votre disposition gratuitement mais son usage est protégé. Un [mirroir](https://wiki.inria.fr/wikis/sciencinfolycee/images/7/73/Informatique_et_Sciences_du_Num%C3%A9rique_-_Sp%C3%A9cialit%C3%A9_ISN_en_Terminale_S.pdf) sur le site de l'INRIA.
* Vous souhaitez découvrir linux ? Lisez [cette introduction](http://raspbian-france.fr/decouvrir-linux-cours-introduction-debutants/) et regardez les slides.  Une distribution populaire, facile d'accès et entièrement libre : [Ubuntu](http://www.ubuntu.com/). Une [communauté](http://ubuntu-fr.org/) d'utilisateurs avec des ressources en français.
* [Apprendre à programmer avec Python 3](https://inforef.be/swi/download/apprendre_python3_5.pdf). Le livre recommandé par l'université de Lille et écrit par Gérard Swinnen.

# Raspberry pi

* [Raspbian France](http://raspbian-france.fr/) : tutoriels, actualités autour du système d'exploitation raspbian - en français



# Where is Brian ?


Le vrai langage de l'informatique n'est ni C++ ni Python mais l'anglais... Aussi :

### Les références à lire

* [StackOverflow](https://stackoverflow.com/) : Pourquoi ça marche pas quand je fais ça ? Tapez le en anglais dans google et vous arriverez sans doute ici... Toutes vos incompréhensions ont une réponse et elle se trouve sur stackoverflow.
* [GitHub](https://github.com) : Des tonnes de projets et de logiciels entièrement accessibles. Devenu incontournable, même les éditeurs les plus fermés s'y sont mis.
* [Code Academy](http://www.codecademy.com/tracks/javascript) : des exercices accessibles et de difficulté croissante pour s'initier à Javascript. Seul problème : tout est en anglais.
* [W3 Schools](https://www.w3schools.com/) : référence sur les langages du web. Toutes les commandes sont illustrées. Un tour de force. Idéal pour débugguer du javascript.
* [MDN](https://developer.mozilla.org/fr/docs/Web/Reference) la référence de Mozilla pour html, css et javascript.
* [AdaFruit](https://www.adafruit.com/) : un vendeur d’électronique très complet qui propose trois tonnes de tutoriels en tout genre pour le Raspberry Pi ou l'Arduino.
* SoloLean : application mobile d'apprentissage comportant des tutoriels etc. Disponible sur [googleplay](https://play.google.com/store/apps/developer?id=SoloLearn) et [l'apple store](https://itunes.apple.com/us/developer/sololearn-inc/id933957049).
* [WordPress.org](https://Wordpress.org) : à intégrer dans un site PHP pour le rendre ultra fonctionnel et esthétique en quelques (dizaines) d'heures.
* [WordPress.com](https://fr.wordpress.com) : la même chose mais déjà hébergé, installé et très simplifié...


## Les chaînes youtube de qualité

Youtube propose énormément de cours et tutoriels sur Python et l'informatique.

Vous trouverez bien sûr de nombreuses références en français, mais je n'en regarde pas. Voici celles que j'apprécie particulièrement.

* [The coding train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw) : surtout du processing (java) et p5js (javascript). Énormément de projets très accessibles et une énergie incroyable. La meilleure chaîne youtube sur informatique.
* [Engineer Man](https://www.youtube.com/channel/UCrUL8K81R4VBzm-KOYwrcxQ). D'un niveau plus relevé, il s'attaque à tout. Les formats sont courts et vont droit au but. D'une excellente qualité.
* [Computerphile](https://www.youtube.com/user/Computerphile) est une des chaînes d'un vaste groupe visant à vulgariser les sciences (mathématiques, physique, chimie, astronomie, informatique). Les formats sont courts mais d'excellente qualité. Attention ce ne sont pas des cours à proprement parler.
* [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) un développeur Python très jeune qui passe en revue les fonctionnalités principales. Format souvent courts mais variés.
* [Ben Eater](https://www.youtube.com/channel/UCS0N5baNlQWJCUrhCEo8WlA) a réalisé de nombreux projets souvent axés sur l'electronique et l'informatique "bas niveau". Il a notamment construit un ordinateur 8 bits complet sur un breadboard. Mais pas que !
* [Kalle Hallden](https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ) propose des vidéos plus "inspirantes" que réellement éducatives. Néanmoins il regorge d'idées et il expose sa mnière de penser.
* [Corey Schafer](https://www.youtube.com/user/schafer5/about) propose un pannel très vaste de cours sur Python et l'informatique en général. Je n'ai pas beaucoup suivi mais les avis sont excellents.
* [kite](https://www.youtube.com/channel/UCxVRDu9ujwOrmDxu72V3ujQ/playlists) est un outil de complétion automatique pour Python à intégrer dans un éditeur avancé (sublim, atom, vscode, vim). Ils proposent de nombreuses vidéos de qualité.

---

# D'autres trucs

* [Rust Python](/python) est une version de python écrite en Rust et compilée en web assembly.
  Pour faire simple, c'est Python dans le navigateur écrit dans un langage rapide et sûr.
  Je n'en suis pas un contributeur.
* [Reversi](/reversi) est une version du jeu reversi / othello écrite en Rust, compilée en web assembly.
  Il tourne assez vite et me bat sans difficulté :) Ça, par contre, c'est de moi.

# About


## D'où proviennent ces cours ?


* La majorité d'entre eux sont originaux,
* d'autres proviennent des enseignements que j'ai reçu à l'université de Lille lors des formations animées par le [FIL](http://fil.univ-lille1.fr/), ou durant le DIU.
* Certains sont inspirés de sources glanées sur internet... (StackOverFlow, Reddit, W3 Schools, OpenClassRooms etc.)
* Certains projets proviennent d'autres collègues enseignant aussi l'informatique.

Dans tous les cas ils étaient libres de droits ou sous une licence permettant l'usage aux enseignants. Merci à leurs concepteurs.

## Est-ce que je peux m'en servir ?

* Si vous enseignez, faîtes en ce que vous voulez.
* Si c'est pour un usage commercial, la réponse est non.

## Comment est fait le site ?

* Dans sa version 2019, le contenu est tapé en en [markdown](https://fr.wikipedia.org/wiki/Markdown) et le site est crée avec [HUGO](https://gohugo.io/). Le thème est [hugo-book](https://themes.gohugo.io/hugo-book/). Il est hébergé sur une [github page](https://pages.github.com/).
* Les précédentes versions étaient en Wordpress (joli mais lourdingue).
* Auparavant c'était du html / js pur hebergé chez free.

## Ça marche pas, y'a un bug là...

Merci de me contacter en publiant une issue sur le dépôt [github](https://github.com/qkzk/qkzk.github.io) de mon site.

## Je trouve ça formidable blablabla

Vous pouvez m'envoyer des bitcoins à cette adresse : _1Dzd4GqasicwsVoyBhHayZTCYQ8HnVdiSd_

Ou si vous préférez Ethereum... : _0xa6288d3cc9bB4FFFB5637f04b54b902916446D75_
