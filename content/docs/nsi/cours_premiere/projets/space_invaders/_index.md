---
title:
    pgzero invaders
author:
  qkzk
date:
  2020-01-18
weight:
  100
---

# Space Invaders - Pygame Zero

Rares sont ceux à n'avoir jamais joué à Space Invaders et, pour beaucoup,
c'est leur première expérience avec les jeux-videos.

Le format "Space Invaders" demande quelques techniques de programmation
pour fonctionner. Pendant un certain temps, certains programmeurs ont appris
de nouveaux langages en se forçant à y écrire un space invaders. C'est un bon
exercice pour découvrir la syntaxe et les fonctions d'un langage.

Ce tutoriel sera découpé en deux parties :

* Dans la première on construit une version de base du jeu Invaders avec des
  aliens, des lasers, des bases de défense et un score.

* La seconde partie ajoutera les éléments supplémentaires de la version des bornes
  d'arcades des années 70.

## Débuter la programmation d'un invaders avec Pygame Zero

Pygame Zero est une librairie de fonctions pour Pygame qui simplifie
considérablement le développement d'un jeu. Si vous ne connaissez pas Pygame
Zero, ce n'est pas grâve. Mais commencez par lire cette [introduction](http://qkzk.xyz/docs/nsi/cours-python/libraries_faciles/pygame_zero/).

Cette introduction vous présente la manière de créer un programme Pygame Zero
élémentaire aussi nous pouvons débuter immédiatement. Nous aurons besoin de
quelques images pour les éléments du jeu - vous pouvez les dessiner vous-mêmes
ou récupérer les nôtres depuis GitHub. Les dimensions par défaut de la fenêtre
de Pygame Zero sont 800 pixels de large pour 600 pixels de haut, ce qui convient
à notre jeu aussi nous n'avons pas besoin de définir `WIDTH` ou `HEIGHT`.

## Débuter le tutoriel

Après avoir récupéré les images [ici](https://github.com/qkzk/data_colab/raw/master/nsi/prog/space_invaders/images/images.zip),
décompressez les dans un dossier `images`

À la racine, créez un fichier `invaders.py`. Voici votre arborescence :

~~~
├── images
│   ├── alien1b.png
│   ├── alien1.png
│   ├── background.png
│   ├── base1.png
│   ├── explosion1.png
│   ├── explosion2.png
│   ├── explosion3.png
│   ├── explosion4.png
│   ├── explosion5.png
│   ├── laser1.png
│   ├── laser2.png
│   └── player.png
└── invaders.py
~~~

Et le contenu du fichier `invaders.py`

[invaders_00.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_00.py)

~~~python
import pgzrun

def draw():
    pass

def update():
    pass


pgzrun.go()
~~~

Tout ce que nous ferons maintenant est d'écrire dans le fichier `invaders.py`

Ouvrez une commande windows, naviguez jusqu'à votre dossier et exécutez
votre fichier `python3 invaders.py`

Vous devriez voir une fenêtre noire de 800x600 pixels.

## Pygame zero vs pygame

Résumons en quelques mots le principe de Pygame zero

Pygame Zero se charge d'une grande partie du code "pénible" de pygame.

J'entends par là qu'il suffit de définir proprement deux fonctions pour
disposer d'un jeu complet.

Ces fonctions sont `draw()`, `update()`

* `draw` contient l'ordre dans lequel les éléments doivent être dessinés
    à chaque tour de la boucle
* `update` contient les mises à jour à chaque tour de la boucle. Événéments
  clavier, collisions, nouveaux élément à l'écran etc.

## Le joueur

Commençons par dessiner le vaisseau du joueur à l'écran. Si on appelle
notre image `player.png` on peut créer l'Actor en haut du code avec
`player = Actor("player", (400, 550))`

Nous voudrons certainement quelque chose de plus intéressant qu'une simple
fenêtre noire, aussi nous pouvons ajouter un fond à notre fonction `draw()`.
Si nous la dessinons en premier, tout ce qui suit sera dessiné par dessus.
Nous pouvons le dessiner en utilisant la fonction `blit()` en écrivant

~~~python
screen.blit('background', (0, 0))
~~~

cela suppose d'avoir appelé notre fond : `background.png`. Ajoutons
`player.draw()` juste après pour faire apparaître le joueur.

**Voici votre code complet à l'issue de cette étape :**

[invaders_01.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_01.py)


## Déplacer le vaisseau du joueur

Le vaisseau du joueur doit répondre aux pressions des touches du clavier donc
nous allons utiliser l'objet clavier de Pygame Zero pour vérifier si certaines
touches ont été pressées. Créeons d'abord une nouvelle fonction pour s'occuper
de ces entrées. Appelons la `checkKeys` et nous devons l'appeler depuis notre
fonction `update`.

Dans la fonction `checkKeys` on a besoin de rendre globale la variable `player`.
En effet, celle-ci est définie _en dehors_ de la fonction et Python nous
empechera de la modifier autrement.

Ensuite on teste si la touche `left` est pressée avec `if keyboard.left:`
et, si `player.x > 40` alors `player.x -= 5`

On ajoute un code similaire pour l'autre direction.

Vérifiez que votre vaisseau se déplace maintenant correctement.

**Voici le code complet à l'issue de cette étape :**

[invaders_02.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_02.py)


## Un concept d'alien

Nous voulons maintenant créer une formation d'aliens. Vous pouvez les disposer
comme vous le souhaitez mais nous allons utiliser trois lignes de six aliens.
Nous diposons d'une image appelée `alien.png` et pouvons créer un `Actor` pour
chaque alien, nous l'ajouterons à un tableau de manière à les parcourir
facilement pour réaliser des actions sur chaque alien. Pour créer les Actors,
nous utilisons un peu de mathématiques pour définir les coordonnées $x$ et $y$
initiales. Il est bienvenue de créer une fonction pour initialiser les aliens,
appelons la `initAliens`. Parce que nous aurons besoin de définir d'autres
objets, profitons-en pour créer une fonction `init()` depuis laquelle
nous appelerons toutes les autres fonctions de réglage.

Voilà comment procéder :

1. Créez la fonction `init` si elle n'existe pas déjà.\
    Dans cette fonction, appelez `initAliens()`
2. Créez la fonction `initAliens`.\
    Elle contient :
    1. la déclaration de la variable aliens comme globale : `global aliens`
    2. l'initialisation de la liste `aliens = []`
    3. la boucle qui crée les éléments, pour l'instant :

        ~~~python
        for a in range(18):
          pass
        ~~~

## Un peu de mathématiques

Pour placer correctement nos aliens et les créer comme acteurs, on a crée une
liste : `aliens = []` et réalisé une boucle : `for a in range(18):`, mais
celle-ci ne fait rien pour l'instant.

Dans cette boucle nous allons créer chaque acteur et l'ajouter à la liste.

Les abscisses commencent à 210 et sont espacés de 80. Chaque ligne contient
6 aliens donc, les $x$ sont : $210 + (a \% 6) \times 80$

Les ordonnées commencent à 100 et sont espacées de 60. Chaque ligne commence
à 60. Donc les $y$ sont $100 + (a // 6) * 64$

Revenons un instant sur cette histoire de division et de reste :

Le quatrième (0, 1, 2, 3) alien est situé à la ligne 0 et colonne 3.

Donc pour `a=3` on obtient `a % 6 = 3` et `a // 6 = 0`, puis pour $x, y$ :

$210 + 3 \times 80 = 450$ et $100 + 0 = 100$.

Pour `a = 17`, on obtient : `17 % 6 = 5` et `17 // 6 = 2`, le dernier élément
de la ligne numéro 2.

Ses coordonnées sont alors `(210 + (a % 6) * 80, 100 + (a // 6) * 64)
(610, 228) = (610, 228)`

Utiliser le modulo et le reste permet de stocker un tableau 2D dans une seule
liste. On dit qu'on a _linéarisé_ le tableau.

Afin de voir vos aliens (pour l'instant immobiles) ajoutez une boucle à
votre fonction `draw` :

~~~python
def draw():
  ...
  for alien in aliens:
      alien.draw()
~~~

**Attention, cette boucle sera bientôt supprimée**

Et voici le code complet à cette étape.

[invaders_03.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_03.py)


## Croire aux choses étranges

Après ce titre obscur, nous allons introduire l'idée selon laquel l'alien a un
état. En effet, dans Pygame Zero, chaque `Actor` dispose de variables d'état
qu'on peut modifier. Ce sont les _attributs_ de cet objet. Nous reviendrons
sur la manière un peu plus tard.

Il est temps maintenant de dessiner proprement nos aliens. Ajoutez une fonction
`drawAlien` qui contient les deux lignes ajoutées à `draw` et appelez la depuis
`draw`. Vos aliens se dessinent comme avant.

## Les aliens arrivent !

Nous allons créer une fonction que nous allons appeler depuis notre fonction
`update` et qui s'occupe de ce qui doit arriver aux aliens. Appelons la
`updateAliens`. Nous ne voulons pas les déplacer à chaque rafraichissement de
l'image (ils se déplaceraient beaucoup trop vite !) donc nous allons utiliser
un compteur appelé `moveCounter` et l'incrémenter à chaque appel de `update`.

S'il dépasse une certaine valeur (`moveDelay`), nous remettons le compteur à
zéro et appelons `updateAliens`

La fonction `updateAliens` va calculer leur déplacement en $x$ et $y$
pour les déplacer en avant et en arrière le long des lignes et vers le bas
quand ils arrivent au bord.

Voici ce que contienent les fonctions modifiées à cette étape :

~~~python
def updateAliens():
    global aliens
    pass

def update():
    global moveCounter
    checkKeys()
    moveCounter += 1
    if moveCounter == moveDelay:
        moveCounter = 0
        updateAliens()

def init():
    global moveDelay, moveCounter, moveSequence
    initAliens()
    moveDelay = 30
    moveCounter = 0
    moveSequence = 0
~~~

Remarquez aussi qu'on ajoute une variable globale `moveSequence` dont on
va parler immédiatement.

**Le code complet à cette étape :**

[invaders_04.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_04.py)


## Mettre les aliens à jour

Pour déterminer où les aliens devraient se déplacer, nous allons compter de 0 à 40.
De 0 à 9, ils se déplacent à gauche. À 10 ils se déplacent vers le bas.
De 11 à 29, ils se déplacent à droite. En 30 ils descendent.
De 31 à 40, ils se déplacent à gauche.

Comptez les pas et vous réaliserez qu'ils partent bien du milieu et serpentent
jusqu'en bas.

Lisez le code ci-dessous pour comprendre comment faire. Cette fonction est
délicate et je ne la détaillerai pas complètement.

Remarquez qu'on utilise une fonction `animate` de pygame_zero pour rendre
le déplacement fluide. On ajoute aussi une bascule entre leurs images pour
changer les pattes.

Pensez à jouter `from random import randint` tout en haut pour utiliser
la fonction `randint`

~~~python
def updateAliens():
    global moveSequence, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30:
        movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 50
    if moveSequence > 10 and moveSequence < 30:
        movex = 15
    for alien in aliens:
        animate(alien, pos=(alien.x + movex, alien.y + movey),
                duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            alien.image = "alien1"
        else:
            alien.image = "alien1b"
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0
~~~



## All your base are belong to us

Maintenant nous allons construire nos défenses. Il y a plusieurs problèmes
à contourner. En particulier, nous aimerions construire les bases avec `Actor`
mais il n'existe pas de méthode pour "clip" un `Actor` quand il est affiché.
Clip est un terme qui désigne le fait de ne dessiner qu'une partie d'une image.
C'est une méthode dont on a besoin pour réduire la taille des bases quand elles
sont touchées par le laser un alien.
Nous allons devoir ajouter une méthode à `Actor` comme nous avons ajouté
les attributs plus tôt. (méthode = fonction d'un objet particulier).

## Construire les bases

Nous allons créer trois bases qui seront faites de trois acteurs chacune. Si
nous voulons afficher l'image complète (base1.png), nous devons créer une liste
d'acteurs de base et afficher chaque acteur avec un code du style `base.draw()`.
Ce que nous allons faire est d'ajouter une variable à la base pour l'afficher
à la hauteur voulue. Nous devons aussi écrire une nouvelle fonction pour
dessiner la base selon cette variable de hauteur.

Lisez le code suivant pour comprendre la manière dont cette nouvelle fonction
est écrite et ajoutée à la variable hauteur. Cela signifie qu'on peut appeler
cette fonction pour chaque acteur d'une base avec `base.drawClipped`.

~~~python

def drawClipped(self):
    screen.surface.blit(self._surf, (self.x - 32, self.y-self.height + 30),
                        (0, 0, 64, self.height))

def initBases():
    global bases
    bases = []
    bc = 0
    for b in range(3):
        for p in range(3):
            bases.append(Actor("base1", midbottom=(150+(b*200)+(p*40), 520)))
            bases[bc].drawClipped = drawClipped.__get__(bases[bc])
            bases[bc].height = 60
            bc += 1

def drawBases():
    for base in bases:
        base.drawClipped()
~~~


**Le code complet à l'issue de cette étape :**

[invaders_05.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_05.py)


## Est-ce que je peux tirer sur quelque chose maintenant ?

Ajoutons des lasers pour en faire un jeu de tir. Nous devons tirer des lasers
depuis notre vaisseau et depuis les aliens. Nous allons cependant les conserver
tous dans une même liste. Quand nous créeons un laser et l'ajoutons à la liste
`lasers`, nous pouvons donner à son `Actor` un type. Dans ce cas, nous créeons
le type 0 pour les lasers du joueur et le type 1 pour les lasers des aliens.
Nous devons aussi ajouter une variable d'état. La création et la mise à jour
des lasers est similaire à celle des éléments déjà crées. Le code ci-dessous
montre les fonctions que nous utilisons.

## Faire fonctionner les lasers

Vous pouvez voir dans le code ci-dessous que l'on crée un laser du le joueur
en ajoutant une vérification pour la touche `SPACE` depuis la fonction
`checkKeys`. Nous utilisons le laser bleu (`laser2.png`) pour le joueur.
Une fois que le nouveau laser est dans notre liste de lasers, il sera dessiné
à l'écran si nous appelons la fonction `drawLasers` depuis la fonction `draw`.
Dans notre fonction `updateLasers` nous parcourons la liste des lasers et
vérifions le type de chaque laser. Si c'est un laser de type 1 (joueur), on
déplace le laser vers le haut de l'écran et vérifions s'il touche quelque chose.
Remarquez les appels à une fonction `listCleanup` dont nous parlerons plus tard.

Pensez à ajouter une variable `DIFFICULTY = 1` tout en haut juste après les
imports ainsi qu'à appeler les fonctions nouvellement crées.

~~~python
def checkKeys():
    global player, lasers
    ... # ici la partie déjà saisie de checkKeys
    if keyboard.space:
        l = len(lasers)
        lasers.append(Actor("laser2", (player.x,player.y-32)))
        lasers[l].status = 0
        lasers[l].type = 1

def drawLasers():
    for l in range(len(lasers)): lasers[l].draw()

def updateLasers():
    global lasers, aliens
    for l in range(len(lasers)):
        if lasers[l].type == 0:
            lasers[l].y += (2*DIFFICULTY)
            checkLaserHit(l)
            if lasers[l].y > 600: lasers[l].status = 1
        if lasers[l].type == 1:
            lasers[l].y -= 5
            checkPlayerLaserHit(l)
            if lasers[l].y < 10: lasers[l].status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)
~~~


**Code complet à cette étape :**

[invaders_06.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_06.py)


## Collisions

Commençons par `checkPlayerLaserHit`. Nous pouvons détecter si un laser a touché
un alien en parcourant le tableau des aliens et vérifiant avec la fonction
`Actor` : `collidepoint((laser.x, laser.y))` pour voir si une collision a eu
lieu. Si un alien a été touché, c'est là que nos variables d'état entrent en
jeu. Plutôt que de retirer le laser et l'alien de leur listes, nous leur donnons
un drapeau "à effacer". Cela évite des soucis lors des boucles qui parcourent
ces listes, sans quoi il va manquer des éléments dans les listes et nous aurons
des erreurs. Nous leur donnons donc un drapeau et les effaçons après avec
`listCleanup`.


![flow de space invaders](https://rpi-magazines.s3-eu-west-1.amazonaws.com/magpi/legacy-assets/2018/10/Space-Invaders-Flow.jpg)

## Nettoyer le désordre

La fonction `listCleanup` crée une nouvelle liste et parcourt les listes
qu'on lui passe. Elle n'ajoute chaque élément que s'il a un état à 0.
Cette nouvelle liste est alors renvoyée et utilisée ensuite.
Maintenant qu'on a un système pour un type de laser, on peut facilement
l'adapter pour les lasers de nos aliens. On peut créer les lasers des aliens
de la même manière mais, au lieu de les déclancher quand on presse espace,
on les tire à des intervalles aléatoires avec `if randint(0,5) == 0: ...` quand
on met à jour notre liste d'aliens.
On leur donne alors le type 0 plutôt que 1 et on les déplace vers le bas
dans notre fonction `updateLasers`

Voici ce qu'on peut ajouter à `updateAliens`

~~~python
def updateAliens():
    global moveSequence, moveDelay
    ...
    for alien in aliens:
        ...
        if randint(0, 5) == 0:
            lasers.append(Actor("laser1", (alien.x, alien.y)))
            lasers[len(lasers)-1].status = 0
            lasers[len(lasers)-1].type = 0
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0
~~~

## Assurer les arrières

Pour l'instant on ne s'est pas soucié de ce qui se passe quand un laser touche
une des bases. Parce que nous changeons la hauteur de l'acteur des bases, la
détection de collision ne nous donnera pas le résultat escompté. Nous devons
donc écrire une autre fonction pour vérifier une collision sur l'acteur de base.
Notre nouvelle fonction `collideLaser()` va vérifier les coordonnées du laser
et celles de la base en tenant compte de la hauteur de la base. Ensuite on
attache la nouvelle fonction à la base quand elle est créée. On peut employer
la nouvelle fonction `collideLaser()` pour vérifier le joueur et l'alien du
laser et retirer le laser s'il est touché. Si c'est la base qui est touchée,
on réduit sa hauteur.

**Code complet à cette étape :**

[invaders_07](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_07.py)


## Un peu trop de lasers

On remarque vite que les aliens tirent trop vite... mais cela est contré
parce que notre vaisseau peut tirer en continu tant que la touche espace est
enfoncée. Non seulement c'est trop facile mais en plus cela ralenti le jeu.
Nous devons établir des limites à la vitesse de tir et nous pouvons le faire en
utilisant un autre objet natif de Pygame Zero : l'horloge. Si on ajoute une
variable `laserActive` à notre Actor joueur  et le passons à 0, on peut
appeler `clock.schedule(makeLaserActive, 1.0)` pour appeler la fonction
`makeLaserActive` après une seconde.

## Je suis touché !

Nous devons regarder ce qui se produit quand le vaisseau est touché par un
laser. Pour cela nous allons créer une animation utilisant plusieurs frames.
On dispose de cinq images d'explosion à ajouter à une une liste, avec notre
image de vaisse "normal" et à attacher à notre acteur de joueur. Nous
allons pour cela importer le module de maths et, à chaque cycle on écrit :
`player.image = player.images[math.floor(player.status/6)]` ce qui affiche
l'image normale si l'état est à 0. Si on règle cet état à 1 quand le vaisseau
est touché, on peut commencer l'animation. Dans la fonction `update`, on ajoute
`if player.status > 0: player.status += 1`. Au fur et à mesure que les valeurs
augmentent, cela va dessiner la séquence de frames l'une après l'autre.

## Initialisation

Cela peut sembler étrange de ne s'occuper de l'initialisation qu'à la fin du
tutoriel mais nous avons ajouté et modifié des éléments à la structure de notre
jeu régulièrement et ce n'est que maintenant qu'on peut vraiment mesurer quelles
sont les données à régler avant que le jeu ne commence. Plus tôt nous avons
crée une fonction `init` qu'on peut appeler pour lancer le jeu. On peut aussi
l'appeler pour reset tous les éléments et redémarrer le jeu.
Si on inclut tous les éléments abordés plus haut, cela donne quelque chose comme

~~~python
def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initAliens()
    initBases()
    moveCounter = moveSequence = player.status = score = player.laserCountdown = 0
    lasers = []
    moveDelay = 30
    player.images = ["player","explosion1","explosion2", "explosion3","explosion4","explosion5"]
    player.laserActive = 1
~~~

**Code complet du jeu à cette étape :**

[invaders_08.py](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_08.py)

## Ils arrivent trop vite !

Il reste quelques détails à ajuster dans cette première partie.
Nous pouvous régler la difficulté (en haut du code) et l'utiliser dans différents
élément du jeu. Nous devrions aussi ajouter un score, en ajoutant 1000 à une
variable globale `score` chaque fois qu'un alien est touché et ensuite
l'afficher en haut à droite de l'écran à l'aide de la fonction `draw`.
Quad le jeu se termine (le joeur à été touché ou tous les aliens sont morts),
on devrait afficher un message adapté.

La version suivante (pas encore traduite, disponible en anglais ici) ajoutera
les niveaux, les vies, les sons, les aliens bonus et un tableau des scores.

![Game Over pour l'instant](https://rpi-magazines.s3-eu-west-1.amazonaws.com/magpi/legacy-assets/2018/10/Coding-Space-Invaders.jpg)

**Ci-dessous le code complet à cette étape.**

[invaders_09](https://github.com/qkzk/data_colab/blob/master/nsi/prog/space_invaders/invaders_09.py)
~~~python
import pgzrun
import math
from random import randint

player = Actor("player", (400, 550))
DIFFICULTY = 1


def draw():
    screen.blit('background', (0, 0))
    player.image = player.images[math.floor(player.status/6)]
    player.draw()
    drawLasers()
    drawAlien()
    drawBases()
    screen.draw.text(str(score), topright=(780, 10), owidth=0.5,
                     ocolor=(255, 255, 255), color=(0, 64, 255), fontsize=60)
    if player.status >= 30:
        screen.draw.text("GAME OVER\nPress Enter to play again",
                         center=(400, 300), owidth=0.5, ocolor=(255, 255, 255),
                         color=(255, 64, 0), fontsize=60)
    if len(aliens) == 0:
        screen.draw.text("YOU WON!\nPress Enter to play again",
                         center=(400, 300), owidth=0.5, ocolor=(255, 255, 255),
                         color=(255, 64, 0), fontsize=60)


def drawAlien():
    for alien in aliens:
        alien.draw()


def updateAliens():
    global moveSequence, lasers, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30:
        movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 50
    if moveSequence > 10 and moveSequence < 30:
        movex = 15
    for alien in aliens:
        animate(alien, pos=(alien.x + movex, alien.y + movey),
                duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            alien.image = "alien1"
        else:
            alien.image = "alien1b"
            if randint(0, 5) == 0:
                lasers.append(Actor("laser1", (alien.x, alien.y)))
                lasers[len(lasers)-1].status = 0
                lasers[len(lasers)-1].type = 0
        if alien.y > player.y and player.status == 0:
            player.status = 1
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0


def update():
    global moveCounter, player
    if player.status < 30 and len(aliens) > 0:
        checkKeys()
        updateLasers()
        moveCounter += 1
        if moveCounter == moveDelay:
            moveCounter = 0
            updateAliens()
        if player.status > 0:
            player.status += 1
    else:
        if keyboard.RETURN:
            init()


def drawClipped(self):
    screen.surface.blit(self._surf, (self.x - 32, self.y-self.height + 30),
                        (0, 0, 64, self.height))


def initBases():
    global bases
    bases = []
    bc = 0
    for b in range(3):
        for p in range(3):
            bases.append(Actor("base1", midbottom=(150+(b*200)+(p*40), 520)))
            bases[bc].drawClipped = drawClipped.__get__(bases[bc])
            bases[bc].collideLaser = collideLaser.__get__(bases[bc])
            bases[bc].height = 60
            bc += 1


def drawBases():
    for base in bases:
        base.drawClipped()


def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initAliens()
    initBases()
    moveCounter = 0
    moveSequence = 0
    player.status = 0
    score = 0
    player.laserCountdown = 0
    lasers = []
    moveDelay = 30
    player.images = ["player", "explosion1", "explosion2",
                     "explosion3", "explosion4", "explosion5"]
    player.laserActive = 1


def initAliens():
    global aliens
    aliens = []
    for a in range(18):
        aliens.append(Actor('alien1',
                            (210 + (a % 6) * 80, 100 + (a // 6) * 64)))
        aliens[a].status = 0


def checkKeys():
    global player, lasers
    if keyboard.left and player.x > 40:
        player.x -= 5
    if keyboard.right and player.x < 760:
        player.x += 5
    if keyboard.space:
        if player.laserActive == 1:
            player.laserActive = 0
            clock.schedule(makeLaserActive, 1.0)
            l = len(lasers)
            lasers.append(Actor("laser2", (player.x, player.y-32)))
            lasers[l].status = 0
            lasers[l].type = 1


def makeLaserActive():
    global player
    player.laserActive = 1


def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()


def updateLasers():
    global lasers, aliens
    for laser in lasers:
        if laser.type == 0:
            laser.y += (2*DIFFICULTY)
            checkLaserHit(laser)
            if laser.y > 600:
                laser.status = 1
        if laser.type == 1:
            laser.y -= 5
            checkPlayerLaserHit(laser)
            if laser.y < 10:
                laser.status = 1
    lasers = listCleanup(lasers)
    aliens = listCleanup(aliens)


def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )


def listCleanup(l):
    newList = []
    for i in l:
        if i.status == 0:
            newList.append(i)
    return newList


def checkPlayerLaserHit(l):
    global score
    for b in bases:
        if b.collideLaser(l):
            l.status = 1
    for a in aliens:
        if a.collidepoint((l.x, l.y)):
            l.status = 1
            a.status = 1
            score += 1000


def checkLaserHit(l):
    global player
    if player.collidepoint((l.x, l.y)):
        player.status = 1
        l.status = 1
    for b in bases:
        if b.collideLaser(l):
            b.height -= 10
            l.status = 1


init()
pgzrun.go()
~~~

## Conclusion

Ce projet est tiré du magazine en ligne dédié au Raspberry Pi : [MagPi](https://magpi.raspberrypi.org/) numéro [74](https://magpi.raspberrypi.org/issues/74) (cette version) et
numéro [75](https://magpi.raspberrypi.org/issues/75) (version complète).
