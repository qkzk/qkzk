---
title: "0 - Préambule"
bookCollapseSection: true
author: "qkzk"
weight: 1

---

pdf [pour impression](./preambule.pdf)


## Python

En 1989, le hollandais **Guido van Rossum** commence le développement de Python.

Python est un langage de programmation haut niveau, multiplateforme, interprété.


{{< tabs "description" >}}

{{< tab "Langage de haut niveau">}}
En interne la machine exécute une à une une séquence d'instruction qu'on peut
représenter par des mots simples comme "déplacer telle donnée vers tel registre",
"ajouter ce registre à celui-ci et l'enregistrer là" etc.

Ce langage est appelé _assembleur_ et c'est un langage _bas niveau_.

Bien que ces instructions soient lisibles par un humain, elles restent très
délicates à comprendre et il n'est pas simple d'écrire un programme en
assembleur.

Autre inconvénient majeur, chaque processeur dispose de son propre jeu
d'instruction. Un programme doit donc être réécrit pour fonctionner sur
un autre type de processeur !

Python est un langage _haut niveau_, cela signifie que ses instructions
ne dépendent pas de la machine sur laquelle on l'exécute.

Python est même considéré comme de _très_ haut niveau, la majorité
de la complexité est masquée à l'utilisateur. Cela rend le développement
de programme (et l'apprentissage de la programmation) plus rapide en Python.
{{< /tab >}}

{{< tab "Multiplateforme" >}}
Python fonctionne sur presque toutes les machines récentes : ordinateurs
sous windows, OSX, linux, téléphones sous android etc. Un programme Python
n'a pas a être réécrit pour passer d'une machine à l'autre.
{{< /tab >}}

{{< tab "Interprété" >}}
Lors de l'exécution d'un code Python, il est exécuté ligne par ligne
par un interpréteur. Il n'est pas compilé à l'avance pour être exécuté.
Ceci permet de disposer d'un _interpréteur_ auquel on peut passer
des commandes pour tester ses instructions.
{{< /tab >}}

{{< /tabs >}}

## Utilisation de Python

Python est utilisé par les développeurs professionnels pour remplir de nombreuses
tâches, en particulier les applications scientifiques et l'intelligence 
artificielle.

La facilité d'accès de Python rend ce langage attractif. On a vu ces dernières
années un essor formidable derrière Python, appuyé par le développement
d'outils facilitant les calculs scientifiques.

Python est aussi employé pour réaliser des serveurs webs à l'aide des bibliothèques
Django et Flask.


## Python 2 vs Python 3

Il existe deux versions majeures de Python : Python 2.7 (obsolète) et Python 3 (que nous utiliserons).

Elles sont très similaires mais les différences comptent.

Vous pouvez vérifier la version de Python en l'exécutant :

```bash
% python
Python 3.9.3 (default, Apr  8 2021, 23:35:02)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


## Installation de Python

### Au Lycée

Python 3 devrait être installé sur tous vos postes. Vous devriez trouver les
logiciels : _thonny_ et _sublime text 3_ qui permettent d'êcrire rapidement du
code Python.

La majorité des bibliothèques que nous utiliserons sont déjà présentes.


### Chez vous :

{{< tabs "uniqueid" >}}
{{< tab "MacOS" >}}
Je ne peux l'affirmer avec certitude mais il me semble que Python 3 est
installé sous OSX.
{{< /tab >}}
{{< tab "Linux" >}}
Python 3 est installé dans toutes les distributions grand public de Linux.
{{< /tab >}}
{{< tab "Windows" >}}
Sous Windows, pour installer Python avec l'**environnement de développement
IDLE**, il suffit de télécharger puis d'exécuter le fichier d'installation qui
se trouve sur le site officiel :
[https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)

Une fois installé, vous pouvez lancer IDLE en allant dans :
Démarrer → Programmes → Python → IDLE (Python GUI)

![idle_1](/uploads/uploads/2017/04/idle_1.png)
{{< /tab >}}
{{< /tabs >}}



## Outils pour développer


### Thonny

[Thonny](https://thonny.org/) est un éditeur de texte **spécifique** à Python.
(vous ne pouvez développer que du Python dans Thonny).

Au delà de ça, il est excellent pour les débutants.

Thonny intègre de nombreux outils : coloration syntaxique, auto complétion,
panneau de variables et d'appels de fonctions, débogueur, etc.

Regardez la [vidéo de présentation](https://youtu.be/nwIgxrXP-X4) (en anglais, hélas) et installez le chez vous.

## Code sur ce site et outils en ligne


### [Basthon](https://console.basthon.fr/)

Basthon est un site qui permet d'exécuter du Python dans le navigateur sans installer quoi que ce soit.

C'est insuffisant pour développer un programme complet mais c'est parfois très pratique.

### Sur mon site

Vous trouverez des blocs de code éditables et exécutables comme :

{{< python title="ce bloc est éditable et exécutable" >}}print("Hello, world!")
{{< /python >}}

Par contre, ce bloc de code est _statique_, vous ne pouvez que le lire :

```python
print("Hello, world!")
```


## Python sur la calculatrice Numworks

La calculatrice Numworks achetée en seconde permet d'exécuter du code Python.
Plus précisément elle intègre un éditeur et un interpréteur de micropython.
C'est une version de Python adaptée à l'informatique embarquée qui comporte
moins de librairies mais permet d'apprendre.

N'oublions pas [l'émulateur](https://www.numworks.com/fr/simulateur/) en ligne
et l'application mobile ([iOS](https://apps.apple.com/fr/app/calculatrice-numworks/id1456585807), [android](https://play.google.com/store/apps/details?id=com.numworks.calculator&hl=fr&gl=US)), très commodes.


