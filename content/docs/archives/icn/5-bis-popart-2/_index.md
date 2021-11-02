---
author: qu3nt1n
date: 2018-03-01 12:39:17+00:00
draft: false
title: 05. bis - popart
bookCollapseSection: true
weight: 5

---

Vous connaissez sans doute le popart et Andy Wahrol.

[caption id="" align="alignnone" width="800"]![](http://p6.storage.canalblog.com/61/16/119589/64652366.jpg)
Portraits de Mao réalisé par Andy Wahrol en 1972[/caption]

Nous allons réaliser un script créant automatiquement des portraits popart similaire en Python.

Vous pouvez tout à fait obtenir ce résultat en manipulant vous même les images dans photofiltre. Par exemple, voici le [travail d'un enfant de 8 ans](https://www.youtube.com/watch?v=UVLDYdYULSw). J'imagine donc que vous y parviendrez.

Ce petit projet nécessite d'avoir suivi la partie précédente et d'avoir compris la manipulation d'images avec PIL, la librairie Python spécialisée dans l'imagerie matricielle.

![](http://cdn02.cdn.justjared.com/wp-content/uploads/headlines/2018/01/gal-gadot-oscars-snub.jpg)


![](data:image/jpeg;base64,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)


Voici les deux portraits dont nous allons partir. La beauté de ces actrices n'est pas le seul critère de choix. Le contraste marqué, les fonds de couleur unie sont importants. Aussi, ces images sont carrées.

Voici un descriptif assez sommaire des consignes.

On dispose de plusieurs images de départ dans un dossier source et d'un dictionnaire de palette au format suivant. Il peut contenir autant de palettes que l'on veut. Chaque palette contient trois couleurs (ou plus - l'important est qu'elles aient toutes le même nombre de couleurs).

~~~python
palettes = [
{"title":"romuald", "colors": ["#9944FF", "#3300AA", "#00AAFF"]},
{"title":"roland", "colors": ["#000000", "#00AAA6", "#00E3A2"]}
]
~~~

Pour chaque palette, on ouvre l'image qu'on converti avec PIL en niveaux de gris (grayscale).

On crée une nouvelle image vide : un tableau vide.
Pour chaque pixel de l'image de départ, on détermine la couleur de la palette à l'aide de seuils prédéfinis sur tous les pixels. On colle cette couleur dans le tableau de la nouvelle image.

On enregistre ce résultat en précisant dans le nom de fichier le titre de la palette employée.

Voilà ! Vous devriez obtenir autant d'images que de palettes x images de départ. J'ai simplement collé les images correspondantes pour recréer le cadre initial.

![gal_gadot](/uploads/uploads/2018/03/gal_gadot.png)
![sarah_gadon](/uploads/uploads/2018/03/sarah_gadon.png)


Si vous n'arrivez à rien, voici un tutoriel à compléter. Je n'ai enlevé qu'une dizaine de lignes.

~~~python
#!/usr/bin/env python
# coding=utf-8

'''
Voici le fichier de départ de votre projet.
Les étapes sont entièrement détaillées, il n'y a plus qu'à écrire le code
Inutile d'essayer de le faire tourner, il ne fonctionne pas encore

Tout ce qui doit être complété est présenté par trois points : ...
'''

# Librairies dont on aura besoin
# manipuler des fichiers dans PIL
from PIL.Image import open, new
# manipuler récuperer une couleur au format rgb
from PIL.ImageColor import getrgb
# convertir en niveaux de gris
from PIL.ImageOps import grayscale
# manipuler des fichiers
import os


# VARIABLES
# le dossier de départ
inputdir = '...'

# le dossier d'arrivée
outputdir= '...'

# les palettes de couleurs
# vous pouvez les modifier pour des résultats plus ou moins réussis
# Préférez des images très contrastées
# Il est possible d'ajouter autant de palettes que l'on veut
palettes = [
{"title":"romuald", "colors": ["#9944FF", "#3300AA", "#00AAFF"]},
{"title":"raymond", "colors": ["#690042", "#BD9700","#BDB491" ]},
{"title":"roland", "colors": ["#000000", "#00AAA6", "#00E3A2"]},
{"title":"reynald", "colors": ["#000000", "#57C0B9", "#57C0B9" ]} # il n'y a que 2 couleurs
]

# FONCTIONS
def colorfun(pixels, colors):
    # realise la conversion depuis une image grayscale vers le popart
    new_pixels = [] # tableau des nouveaux pixels
    for pixel in pixels: # on itere dans les pixels du tableau
        # pixel est un nombre entre 0 = noir et 255 = blanc
        if pixel < 85: # premier seuil, sombre
            color = getrgb(colors[0])
        elif ...: # second seuil, intermédiaire
            color = ...
        else: # troisième seuil, clair
            ...


        new_pixels.append(...) # on cole le pixel dans le tableau
    return ... # on renvoie le nouveau tableau des pixels


# si le dossier de sortie n'existe pas, on le crée
if not os.path.exists(outputdir):
    os.mkdir(outputdir)


# LA BOUCLE
for palette in palettes: # on itère dans les palettes

    for file in os.listdir(inputdir): # pour chaque fichier de la source
        (file_basename, file_extension)=os.path.splitext(file) # on separe le nom du fichier de son extension

        print 'processing %s' % file_basename # affichage console
        output_name = file_basename + '_' + palette['title']  + file_extension # on crée le nom du futur fichier contenant le titre de la palette

        colors = ... # on récupère la palette des couleurs
        img = open(os.path.join(inputdir, file)) # on ouvre le fichier source
        pixels = grayscale(img).getdata() # qu'on converti en grayscale avec PIL pour en récupérer les données
        img2 = new(img.mode, img.size,) # on crée une nouvelle image vide
        img2.putdata( ... ) # où on colle les nouveaux pixels renvoyés par colorfun
        img2.save(os.path.join(outputdir, output_name)) # on sauvegarde

        # # idem en couleurs inversées
        # colors.reverse()
~~~
