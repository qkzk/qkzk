---
author: qu3nt1n
date: 2019-05-05 07:23:34+00:00
draft: false
title: Python 3 - 12 Créer un programme exécutable avec Py2exe
bookCollapseSection: true
weight: 12

---

#### Attention !
L'extension Py2exe ne fonction que pour la version 2 de Python, sous Windows.
Pour la version 3, il existe des solutions comme cx_freeze






L'extension **Py2exe** permet de convertir un script Python en un programme exécutable (uniquement pour le système d'exploitation Windows).
Ce programme exécutable (fichier avec l'extension .exe) peut ensuite être lancé sur un ordinateur où Python n'est pas installé.


### Téléchargement et installation de Py2exe


Il faut un ordinateur avec Windows et Python déjà installé (attention : Py2exe ne supporte pas la version 3 de Python).

Le programme d'installation de Py2exe est disponible ici :

[Py 2 exe : site officiel](http://www.py2exe.org/)

Une fois téléchargé ([ici](https://pypi.org/project/py2exe/#files), choisir la version pour windows 64 à moins que vous ayez un PC très ancien, alors prendre windows 32), il suffit d'exécuter ce fichier pour installer Py2exe.


### Utilisation de Py2exe


A titre d'exemple, voici le script d'un jeu de puissance 4 :

[jeu_puissance4.py](http://fsincere.free.fr/isn/python/script/jeu_puissance4.py)

![](http://fsincere.free.fr/isn/python/picto/jeu_puissance4.png)


Télécharger et enregistrer ce script dans le répertoire où est installé Python (chez moi, c'est le répertoire C:\Python27).

Créer le script `setup.py` :


    # setup.py
    from distutils.core import setup
    import py2exe

    setup(windows=["jeu_puissance4.py"])


Enregistrer le script `setup.py` dans le répertoire courant de Python.


#### Remarques





* si vous voulez disposer de la console en plus de l'interface graphique (GUI), remplacer `setup(windows=["jeu_puissance4.py"])` par `setup(console=["jeu_puissance4.py"])`
* pour traiter plusieurs scripts en même temps, il suffit de compléter la liste :
`setup(windows=["jeu_puissance4.py","script2.py","script3.py"])`

Ouvrir l'interpréteur de commande de Windows (Démarrer → Exécuter → cmd)

Placez-vous dans le répertoire courant de Python (commande `cd` : change directory) :


    > cd C:\Python27


puis lancer Py2exe :


    > python setup.py py2exe


Un sous répertoire nommé `dist` est créé (chez moi C:\Python27\dist).
Il contient le fichier exécutable `jeu_puissance4.exe` ainsi que toutes les ressources nécessaires à un fonctionnement autonome (`python27.dll library.zip`...).

Vous pouvez maintenant copier le répertoire complet `dist` et le distribuer vers des ordinateurs qui ne possèdent pas Python.
Le programme se lancera en exécutant le fichier `jeu_puissance4.exe`.

Notez que le code source Python (jeu_puissance4.py) n'est plus visible (comme c'est le cas pour des programmes compilés avec des langages de programmation comme C ou C++).
Cet aspect est intéressant pour un enseignant qui veut montrer un projet de programme, sans pour autant dévoiler le code source à ses étudiants...
Py2exe est donc un moyen de fermer le code source (stratégie commerciale des logiciels propriétaires).


### Webographie





* [www.py2exe.org](http://www.py2exe.org/)
* [inventwithpython.com](http://inventwithpython.com/appendixc.html)



### Applications similaires


Dans la même catégorie de logiciels que Py2exe, on peut citer :



 	  * [cx_Freeze](http://cx-freeze.sourceforge.net/) (pour Python 2 et 3)
 	  * [py2app (pour Mac OS)](http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html)






Source : [Fabrice Sincère](http://fsincere.free.fr/isn/python/cours_python_py2exe.php) - [Contenu sous licence CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/fr/)
