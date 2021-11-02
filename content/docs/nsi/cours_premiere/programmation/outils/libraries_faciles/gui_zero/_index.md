---
author: qkzk
date: 2019-12-10 07:08:58+00:00
draft: false
title: Gui Zero
bookCollapseSection: true
weight: 3
---

# Guizero


_Cette brève présentation est une traduction de la page d'accueil de la_
_[documentation officielle](https://lawsie.github.io/guizero/about/)_
_de la librairie._

## Qu'est ce que guizero ?

guizero est une librairie Python 3 permettant de créer de simples
interfaces graphiques (GUI).

Elle est conçue pour permettre aux débutants de créer rapidement et
facilement des interfaces graphiques pour leurs programmes.

![guizero](https://lawsie.github.io/guizero/images/have-a-go.png)

~~~python
from guizero import App, Text, PushButton

app = App(title="guizero")

intro = Text(app, text="Have a go with guizero and see what you can create.")
ok = PushButton(app, text="Ok")

app.display()
~~~

## Objectifs

L'objectif de guizero est rendre la conception d'interfaces graphiques
rapide, accessible et compréhensibles aux débutants.

* Fonctionne avec la librairie standard Tkinter (inutile d'installer d'autres librairies).
* Permet d'abstraire les détails que les débutants trouvent difficile
  d'accès (comme les objets `StringVar()` de Tkinter).
* Des Widgets nommés pour permettre aux débutants de construire un modèle mental.
* Suffisemment flexible pour être employée dans un projet de lycée et néanmoins utilisable à l'école primaire.
* Documentation compréhensible et accessible riche d'exemples.
* Fournit des messages d'erreurs utilisables et compréhensibles.

## Installation

Il existe de nombreuses méthodes d'installation. La plus intéressante au lycée est celle qui évite les droits d'administrateurs.

Il suffit de télécharger et de dézipper un fichier pour [installer guizero](## easy install).

## Easy install

1. Rendez-vous sur le [dépot guizero](https://github.com/lawsie/guizero)
2. Cliquez sur l'icone verte "Clone or download" et ensuite "download zip"

    ![easy install](https://lawsie.github.io/guizero/images/download-zip.png)
3. Ouvrez le fichier zip.
4. Ouvrez le dossier `guizero-master` et copiez le dossier `guizero` dans votre dossier principal

    ![zip](https://lawsie.github.io/guizero/images/copy-guizero-annotated.png)
5. Et voilà ! Quand vous créez vos scripts assurez-vous de les enregistrer dans votre dossier principal.

## Installation avec pip

### Windows

1. Dans une fenêtre de commande (touche windows, cmd, entrée, clic droit, "ouvrir avec les droits d'administrateur", si nécessaire demander à un administrateur de taper ses identifiants)
2. Taper cette commande et pressez entrée :

    `pip3 install guizero`

    Si vous êtes derriere un proxy, demandez à votre adminstrateur son adresse et utiliser :

    `pip3 install --proxy http://ip.proxy:port guizero`

    ![pip](https://lawsie.github.io/guizero/images/windows_pip_install.gif)
