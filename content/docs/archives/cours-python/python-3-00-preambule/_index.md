---
author: qu3nt1n
date: 2019-05-05 05:28:24+00:00
draft: false
title: Python 3 - 00 préambule
bookCollapseSection: true
weight: -1
---

## Préambule


En 1989, le hollandais **Guido van Rossum** commence le développement du langage de programmation Python.

Python est un langage **multi plateforme**, c'est-à-dire disponible sur plusieurs architectures (compatible PC, tablettes, smartphones, ordinateur low cost Raspberry Pi...) et systèmes d'exploitation (Windows, Linux, Mac, Android...).

Le langage Python est gratuit, sous **licence libre**.

C'est un des langages informatiques les plus populaires avec C, C++, C#, Objective-C, Java, PHP, JavaScript, Delphi, Visual Basic, Ruby et Perl ([liste non exhaustive](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html)).

Actuellement, Python en est à sa version 3.
Cependant, la version 2 est encore utilisée.

Attention : Python 2 n'est généralement pas compatible avec Python 3 !

Python est un langage interprété (on dit parfois : langage de script). Cela signifie que les commandes sont interprétées par le programme Python lui même avant d'être traitées par le processeur. Il est donc plus simple de développer en Python qu'en C ou en Java, par exemple.

La syntaxe de Python ne reprend pas la syntaxe la plus courante, dérivée du langage C.
Il faut donc un temps d'adaptation (assez court) pour commencer à développer en Python si on a déjà développé en C, Java etc. Le trajet inverse est similaire.


### Que peut-on faire avec Python ?


Beaucoup de choses !



* du calcul scientifique (librairie [`NumPy`](http://www.numpy.org/))
* des graphiques (librairie [`matplotlib`](http://matplotlib.org/))
* du traitement du son, de la synthèse vocale (librairie `eSpeak`)
* du traitement d'image (librairie [`PIL`](http://www.pythonware.com/products/pil)), de la vision artificielle par caméra (framework [`SimpleCV`](http://simplecv.org/))
* de la bio-informatique (librairie [`Biopython`](http://biopython.org/wiki/Main_Page))
* des applications avec interface graphique GUI (librairies [`Tkinter`](http://fsincere.free.fr/isn/python/cours_python_tkinter.php), [`PyQt`](http://www.riverbankcomputing.co.uk/software/pyqt/intro), [`wxPython`](http://www.wxpython.org/), [`PyGTK`](http://www.pygtk.org/)...)
* des jeux vidéo en 2D (librairie [`Pygame`](http://fsincere.free.fr/isn/python/cours_python_pygame.php))
* des applications multi-touch (framework [`kivy`](http://kivy.org/) pour tablette et smartphone à écran tactile)
* des applications Web (serveur Web [`Zope`](http://www.zope.org/) ; frameworks Web [`Flask`](http://flask.pocoo.org/), [`Django`](http://www.django-fr.org/))
* interfacer des systèmes de gestion de base de données (librairie [`MySQLdb`](http://mysql-python.sourceforge.net/MySQLdb.html)...)
* des applications réseau (framework [`Twisted`](http://twistedmatrix.com/trac))
* communiquer avec des ports série RS232 (librairie [`PySerial`](http://pyserial.sourceforge.net/)), en Bluetooth (librairie [`pybluez`](https://code.google.com/p/pybluez))...
* ...

Des **dizaines de milliers** de librairies sont disponibles sur le dépôt officiel [`PyPI`](https://pypi.python.org/pypi).


### Installation




#### Au LYCEE des FLANDRES


Par défaut, Python 3.7 **devrait** être installé sur vos machines. Si une autre version de Python existe (par exemple 2.7 ou 3.4) ce n'est pas forcement gênant. La majorité des instructions sont identiques et il n'est pas toujours indispensable de mettre à jour. Pour débuter ce cours vous pouvez utiliser la version existante.
Il arrive souvent que les raccourcis du menu démarrer n'apparaissent pas. Il faut alors chercher à partir de la racine du disque dur principal **c:\** pour localiser Python... N'étant pas maître des installations, je ne peux rien y faire.

D'autre part nous utiliserons souvent des outils en ligne permettant de travailler directement dans le navigateur et simplifiant considérablement l'échange de documents : [repl.it](https://repl.it)  et [google colab](https://colab.research.google.com/).


#### Sous Windows -- à la maison.


Sous Windows, pour installer Python avec l'**environnement de développement IDLE**, il suffit de télécharger puis d'exécuter le fichier d'installation qui se trouve sur le site officiel :
[https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)

Une fois installé, vous pouvez lancer IDLE en allant dans :
Démarrer → Programmes → Python → IDLE (Python GUI)

![idle_1](/uploads/uploads/2017/04/idle_1.png)



#### Sous Linux


Python 3 est pré-installé sur la plupart des distributions Linux.


#### SOUS MAC OSX


Je n'ai pas de Mac donc c'est à prendre avec des pincettes...

À ma connaissance, Python 2 a longtemps été installé sur OSX. Python 3 devrait être la version présente sur les distributions les plus récentes.

Cependant d'après [ce que je lis](https://hdrapin.com/2017/03/04/installer-python-sur-mac/) il suffit d'utiliser le gestionnaire de paquets HomeBrew :

~~~bash
$ brew install python3
~~~

[caption id="" align="aligncenter" width="820"]![](https://hdrapin.files.wordpress.com/2016/11/image-022.png?w=820)
L'installation de Python avec HomeBrew (c)[/caption]

#### Thonny

[Thonny](https://thonny.org/) est un éditeur de texte spécifique à Python. Vous ne pouvez développer que du Python dans Thonny. Au delà de ça, il est excellent pour les débutants.

Thonny intègre de nombreux outils : coloration syntaxique, auto complétion, panneau de variables et d'appels de fonctions, débogueur, etc.

Regardez la vidéo de présentation (en anglais, hélas) et installez le chez vous.


#### IDLE


IDLE est l'environnement de développement intégré (IDE en anglais : Integrated Development Environment) proposé par Python.
IDLE propose un certain nombre d'outils :



* un éditeur de texte (pour écrire le programme)
* un interpréteur (pour exécuter le programme)
* un débogueur (pour tester le programme)

Il existe d'autres IDE multilangage comme :

* [Sublime Text](https://www.sublimetext.com/),
* [Atom](https://atom.io/),
* [VS Code](https://code.visualstudio.com/),
* [Spyder](https://pypi.python.org/pypi/spyder) ...




### Scripts


Un programme est une séquence d'instructions.
Dans le cas d'un programme en langage Python, on parle souvent de **script Python**.

Un script se présente sous la forme d'un fichier texte avec l'extension **.py**


#### Jeu de puissance 4


Voici un exemple de script Python :

[jeu_puissance4.py](http://fsincere.free.fr/isn/python/script/jeu_puissance4.py)

Enregistrer ce script sur votre bureau.

Ouvrir IDLE :
Démarrer → Programmes → Python → IDLE (Python GUI)
File → Open → jeu_puissance4.py
L'éditeur de texte s'ouvre avec le code source du script (environ 1000 lignes de code, soit plusieurs dizaines d'heures de travail pour un développeur expérimenté) :

![idle_2](/uploads/uploads/2017/04/idle_2.png)


Pour exécuter le script : Run → Run module (ou touche F5)

A vous de jouer !

![jeu_puissance4](/uploads/uploads/2017/04/jeu_puissance4.png)



## Python et les caractères accentués


Par défaut, Python 2 ne gère pas les caractères accentués dans les scripts. La version 3 de python résout ce problème en autorisant la majorité des caractères courant. Cependant, évitez d'utiliser des variables contenant des caractères spéciaux, réservez les aux chaînes de caractères.

~~~python
>>> é
  File "<stdin>", line 1
    é
    ^
SyntaxError: invalid syntax
~~~


On prendra donc soin, d'insérer en haut de chaque script (par exemple : **exemple.py**) l'encodage suivant :

~~~python
# coding=utf-8
~~~


Oui, il est précédé d'un # et donc paraît être un commentaire mais les premières lignes sont interprétées comme des réglages.

On trouvera souvent le préambule suivant :

~~~python
#!/usr/bin/env python
# coding=utf-8
~~~

ou `#! /usr/bin/python` . Cette première ligne, appelée SHEBANG, permet au système d'exploitation linux de reconnaître un script exécutable.

De manière générale, on recommande d'éviter les accents, cédilles etc. dans les codes sources. C'est parfois impossible, aussi doivent-ils être traités avec prudence en définissant un encodage.


## Python et l'indentation


En Python la structure d'un programme est **définie par son indentation**. Ce sont les espaces qui séparent le bord gauche de l'éditeur du début de l'instruction.

~~~python
if 2>1:
    print("bravo !")
~~~

Le print précédent est indenté par 4 espaces. C'est le format standard d'indentation. On trouvera parfois des variantes telle qu'une tabulation, 2 espaces, 3 espaces...
On veillera donc à se méfier des copier coller hâtifs en Python. Si l'indentation n'est pas la même entre la source et la destination, le programme va renvoyer une erreur.

Que se passe-t-il si on n'indente pas ?

~~~python
>>> if 2>1:
... print("bla")
  File "<stdin>", line 2
    print "bla"
        ^
IndentationError: expected an indented block
~~~

Python renvoie une erreur.



Vous pouvez maintenant poursuivre votre découverte.
