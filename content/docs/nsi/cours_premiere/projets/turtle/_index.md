---
title: "le module Turtle"
bookCollapseSection: true
weight: -2

---

Le module `Turtle` de [Python](https://docs.python.org/fr/3/library/turtle.html) permet de dessiner très simplement des figures.

Il est présent sur votre calculatrice Numworks, dans l'installation par défaut
de Python ainsi qu'en ligne, par exemple [ici](https://coddy.tech/embed-editor?lang=python&code=ZnJvbSB0dXJ0bGUgaW1wb3J0ICoKCmZvciBpIGluIHJhbmdlKDQpOgogICAgZm9yd2FyZCgxMDApCiAgICBsZWZ0KDkwKQo).

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

Résultat : ![carré](/docs/nsi/cours_premiere/projets/turtle/img/0.png)

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

Résultat : ![Étoile](/docs/nsi/cours_premiere/projets/turtle/img/1.png)

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

Résultat : ![hexagone](/docs/nsi/cours_premiere/projets/turtle/img/2.png)

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

Voir [ici](https://coddy.tech/embed-editor?lang=python&code=aW1wb3J0IHR1cnRsZSAgICNPdXRzaWRlX0luCnduID0gdHVydGxlLlNjcmVlbigpCnduLmJnY29sb3IoImxpZ2h0IGdyZWVuIikKc2trID0gdHVydGxlLlR1cnRsZSgpCnNray5jb2xvcigiYmx1ZSIpCiAKZGVmIHNxcmZ1bmMoc2l6ZSk6CiAgICBmb3IgaSBpbiByYW5nZSg0KToKICAgICAgICBza2suZmQoc2l6ZSkKICAgICAgICBza2subGVmdCg5MCkKICAgICAgICBzaXplID0gc2l6ZS01CiAKc3FyZnVuYygxNDYpCnNxcmZ1bmMoMTI2KQpzcXJmdW5jKDEwNikKc3FyZnVuYyg4NikKc3FyZnVuYyg2NikKc3FyZnVuYyg0NikKc3FyZnVuYygyNikK)

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

Voir [ici](https://coddy.tech/embed-editor?lang=python&code=ZnJvbSB0dXJ0bGUgaW1wb3J0ICoKY29sb3JzID0gWydyZWQnLCAncHVycGxlJywgJ2JsdWUnLCAnZ3JlZW4nLCAnb3JhbmdlJywgJ3llbGxvdyddCnQgPSBUdXJ0bGUoKQpzY3JlZW4gPSBTY3JlZW4oKQpzY3JlZW4uYmdjb2xvcignYmxhY2snKQpmb3IgeCBpbiByYW5nZSgzNjApOgogICAgdC5wZW5jb2xvcihjb2xvcnNbeCU2XSkKICAgIHQud2lkdGgoeC8xMDAgKyAxKQogICAgdC5mb3J3YXJkKHgpCiAgICB0LmxlZnQoNTkpCg)

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

Voir [ici](https://coddy.tech/embed-editor?lang=python&code=ZnJvbSB0dXJ0bGUgaW1wb3J0ICoKc3BlZWQoMCkKZGVmIGtvY2gobCxuKToKICAgICcnJ0ZyYWN0YWNsZSBkZSBLb2NoJycnCiAgICBpZiBuPD0wOgogICAgICAgIGZvcndhcmQobCkKICAgIGVsc2U6CiAgICAgICAga29jaChsLzMsbi0xKQogICAgICAgIGxlZnQoNjApCiAgICAgICAga29jaChsLzMsbi0xKQogICAgICAgIHJpZ2h0KDEyMCkKICAgICAgICBrb2NoKGwvMyxuLTEpCiAgICAgICAgbGVmdCg2MCkKICAgICAgICBrb2NoKGwvMyxuLTEpCgpkZWYgZmxvY29uKGwsbik6CiAgICAnJydGbG9jb24gZGUgS29jaCcnJwogICAga29jaChsLG4pCiAgICByaWdodCgxMjApCiAgICBrb2NoKGwsbikKICAgIHJpZ2h0KDEyMCkKICAgIGtvY2gobCxuKQogICAgCmZsb2NvbigyMDAsIDMpCg)

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

Voir [ici](https://coddy.tech/embed-editor?lang=python&code=ZnJvbSB0dXJ0bGUgaW1wb3J0ICoKYW5nbGUgPSAzMApzcGVlZCgwKQpjb2xvcignIzNmMTkwNScpICMgY291bGV1ciBkdSB0cm9uYwoKZGVmIGFyYnJlKG4sbG9uZ3VldXIpOgogICAgaWYgbj09MDoKICAgICAgICBjb2xvcignZ3JlZW4nKQogICAgICAgIGZvcndhcmQobG9uZ3VldXIpICMgYXZhbmNlCiAgICAgICAgYmFja3dhcmQobG9uZ3VldXIpICMgcmVjdWxlCiAgICAgICAgY29sb3IoJyMzZjE5MDUnKQogICAgZWxzZToKICAgICAgICB3aWR0aChuKQogICAgICAgIGZvcndhcmQobG9uZ3VldXIvMykgI2F2YW5jZQogICAgICAgIGxlZnQoYW5nbGUpICMgdG91cm5lIHZlcnMgbGEgZ2F1Y2hlIGRlIGFuZ2xlIGRlZ3LDqXMKICAgICAgICBhcmJyZShuLTEsbG9uZ3VldXIqMi8zKQogICAgICAgIHJpZ2h0KDIqYW5nbGUpICMgdG91cm5lIHZlcnMgbGEgZHJvaXRlIGRlIGFuZ2xlIGRlZ3LDqXMKICAgICAgICBhcmJyZShuLTEsbG9uZ3VldXIqMi8zKQogICAgICAgIGxlZnQoYW5nbGUpICMgdG91cm5lIHZlcnMgbGEgZ2F1Y2hlIGRlIGFuZ2xlIGRlZ3LDqXMKICAgICAgICBiYWNrd2FyZChsb25ndWV1ci8zKSAjIHJlY3VsZQoKaGlkZXR1cnRsZSgpICMgY2FjaGUgbGEgdG9ydHVlCnVwKCkgIyBsw6h2ZSBsZSBzdHlsbwpmb3J3YXJkKDEwMCkgIyBhdmFuY2UgZGUgMTAwCnJpZ2h0KDkwKSAjIHRvdXJuZSBkZSA5MCBkZWdyw6lzIHZlcnMgbGEgZHJvaXRlIApmb3J3YXJkKDMwMCkgIyBhdmFuY2UgZGUgMzAwIHBpeGVscwpsZWZ0KDE4MCkgIyBmYWl0IHVuIGRlbWktdG91cgpkb3duKCkgIyBwb3NlIGxlIHN0eWxvCmFyYnJlKDExLCA0MDApICMgZXjDqWN1dGUgbGEgZm9uY3Rpb24Kc2hvd3R1cnRsZSgpICMgYWZmaWNoZSBsYSB0b3J0dWUKbWFpbmxvb3AoKQo)

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
