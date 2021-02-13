---
title: "le module Turtle"
weight: -2

---

Le module `Turtle` de [Python](https://docs.python.org/fr/3/library/turtle.html) permet de dessiner très simplement des figures.

Il est présent sur votre calculatrice Numworks, dans l'installation par défaut
de Python ainsi qu'en ligne, par exemple [ici](https://trinket.io/turtle).

Il est beaucoup plus difficile de le faire fonctionner dans Colab, aussi ce
petit projet ne l'utilisera pas.

# Méthodes courantes

Turtle permet de commander une tortue pour dessiner dans une figure.
On peut employer des commandes telles que `turtle.forward(...)` ou `turtle.right()`
qui déplacent la tortue. Les méthodes courantes sont:

| Méthode        | Paramètres     | Description                                                           |
|----------------|----------------|-----------------------------------------------------------------------|
| `Turtle`       | aucun          | Crée et renvoie un objet `Turtle`                                     |
| `forward()`    | `distance`     | Déplace la tortue vers l'avant de `distance`                          |
| `backward()`   | `distance`     | Déplace la tortue vers l'arrière de `distance`                        |
| `right()`      | `angle`        | Tourne la tortue dans le sens des aiguilles d'une montre              |
| `left()`       | `angle`        | Tourne la tortue dans le sens contraire des aiguilles d'une montre    |
| `penup()`      | aucun          | Lève le crayon de la tortue                                           |
| `pendown()`    | aucun          | Abaisse le crayon de la tortue                                        |
| `up()`         | aucun          | Lève le crayon de la tortue                                           |
| `down()`       | aucun          | Abaisse le crayon de la tortue                                        |
| `color()`      | nom de couleur | Change la couleur de la tortue                                        |
| `fillcolor()`  | nom de couleur | Change la couleur de remplissage d'un polygone                        |
| `heading()`    | aucun          | Renvoie la direction courante                                         |
| `position()`   | aucun          | Renvioe la position de la tortue                                      |
| `goto()`       | `x, y`         | Déplace la tortue vers la position `x, y`                             |
| `begin_fill()` | aucun          | Enregistre le premier point d'un polygone a remplir                   |
| `end_fill()`   | aucun          | Ferme le polygone et le remplit de la couleur courante                |
| `dot()`        | aucun          | Dessine un point à la position courante                               |
| `stamp()`      | aucun          | Dessine la forme de la tortue sur l'écran (_stamp_ = tampon)          |
| `shape()`      | `shapename`    | Change la forme de la tortue (`arrow`, `classic`, `turtle`, `circle`) |

# Dessiner avec `Turtle`

Pour utiliser les méthodes de `turtle`, il faut importer `turtle`.

1. Importer le module `turtle`
2. Créer et contrôler la tortue,
3. Dessiner avec les méthodes de la tortue,
4. Lancer `turtle.done()`


## Quelques exemples :

### Un carré

```python
import turtle
skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()
```

Résultat : ![carré](https://media.geeksforgeeks.org/wp-content/uploads/20201007233918/out.png)

On répète 4 fois la même séquence consistant à : avancer de 50 pixels, tourner
de 90 dans le sens des aiguilles d'une montre.

### Une étoie

```python
import turtle 
 
star = turtle.Turtle()
 
for i in range(50):
    star.forward(50)
    star.right(144)
     
turtle.done()
```

Résultat : ![Étoile](https://media.geeksforgeeks.org/wp-content/uploads/20201007234135/starrs.png)

### Hexagone

```python
import turtle 
polygon = turtle.Turtle()
 
num_sides = 6
side_length = 70
angle = 360.0 / num_sides 
 
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
turtle.done()
```

Résultat : ![hexagone](https://media.geeksforgeeks.org/wp-content/uploads/20201007234311/polly.png)

## Quelques figures plus spectaculaires

### Spirale

```python
import turtle   #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
 
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size-5
 
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
```

Voir [ici](https://trinket.io/turtle/4d11ecb3c2)

### Rosace

```python
import turtle

turtle.speed(0)
 
for i in range(80):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
```



### Rainbow Benzene

```python
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = Turtle()
screen = Screen()
screen.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
```

Voir [ici](https://trinket.io/turtle/0c31ae92f1)

## Figures fractales

Il est possible de construire assez simplement des fractales avec la tortue :

_Ces méthodes utilisent généralement des fonctions récursives qui ne seront
abordées qu'en terminale._

### Flocon de Koch

```python
from turtle import *
speed(0)
def koch(l,n):
    '''Fractacle de Koch'''
    if n<=0:
        forward(l)
    else:
        koch(l/3,n-1)
        left(60)
        koch(l/3,n-1)
        right(120)
        koch(l/3,n-1)
        left(60)
        koch(l/3,n-1)

def flocon(l,n):
    '''Flocon de Koch'''
    koch(l,n)
    right(120)
    koch(l,n)
    right(120)
    koch(l,n)
    
flocon(200, 3)
```

Voir [ici](https://trinket.io/turtle/504cb3fc09)

### Arbre Pythagoricien

```python
from turtle import *
angle = 30
speed(0)
color('#3f1905') # couleur du tronc

def arbre(n,longueur):
    if n==0:
        color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle) # tourne vers la gauche de angle degrés
        arbre(n-1,longueur*2/3)
        right(2*angle) # tourne vers la droite de angle degrés
        arbre(n-1,longueur*2/3)
        left(angle) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule

hideturtle() # cache la tortue
up() # lève le stylo
forward(100) # avance de 100
right(90) # tourne de 90 degrés vers la droite 
forward(300) # avance de 300 pixels
left(180) # fait un demi-tour
down() # pose le stylo
arbre(11, 400) # exécute la fonction
showturtle() # affiche la tortue
mainloop()
```

Voir [ici](https://trinket.io/turtle/fcd6a7a469)

### Courbe du dragon

Là on est très très loin du programme de NSI, mais le résultat mérite le détour.

```python
import turtle

def turn(i):
    left = (((i & -i) << 1) & i) != 0
    return 'L' if left else 'R'

def curve(iteration):
    return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])

turtle.hideturtle()
turtle.speed(0)
i = 1
while True:
    if turn(i) == 'L':
        turtle.circle(-4, 90, 36)
    else:
        turtle.circle(4, 90, 36)
    i += 1
```

Voici [ici](https://trinket.io/turtle/a6617f0826)


# Deux projets avec la tortue

Ces projets sont des tutoriels à suivre et qui peuvent vous inspirer.

## Suivre la station spatiale internationale

Pas à pas : suivre l'ISS et dessiner sa position.

Vous n'avez qu'à suivre les instructions [ici](https://projects.raspberrypi.org/fr-FR/projects/where-is-the-space-station)

## La course à la tortue

L'idée est simple : organiser une course aléatoire entre quelques tortues
et compter les points.

Le projet est entièrement détaillé, il suffit de suivre. Je n'ai pas
le courage de vous le traduire entièrement. Après, tout, vous êtes supposés
étudier l'anglais depuis la maternelle...

[Turtle race](https://www.futurelearn.com/info/courses/object-oriented-principles/0/steps/31480)
