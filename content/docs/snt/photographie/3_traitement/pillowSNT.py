#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: `pillowSNT` module

:author: Académie de Lille _ Mieszczak Christophe
         Univ. Lille

:date: mars 2019

Interface simplifiée de manipulation d'images RVB.

"""

from PIL import Image


def ouvrir(chemin):
    """Renvoie l'image lue dans le fichier de nom `chemin`."""
    return Image.open(chemin)

def afficher(image):
    """Ouvre une fenêtre et affiche l'image."""
    image.show()

def sauver(image, chemin):
    """Sauvegarde l'image donnée dans le fichier de nom `chemin`."""
    image.save(chemin)


def filtrer(image, filtre):
    """L'image à laquelle la fonction `filtre()` a été appliquée à chaque pixel.

    La fonction `filtre()` accepte trois paramètres, `r`, `v`, et `b`.
    Elle renvoie les valeurs rvb du nouveau pixel.
    """
    nimg = Image.new("RGB", (image.size[0],image.size[1]))   # la nouvelle image
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, v, b = image.getpixel((x, y))
            nimg.putpixel((x, y), filtre(r, v, b))
    return nimg

def filtrer3x3(image,filtre3x3):
    """
    applique le filtre3x3 pour chaque pixel de l'image hors bordure
    """
    nimg = Image.new("RGB", (image.size[0],image.size[1]))   # la nouvelle image
    for x in range(1,image.size[0]-1):
        for y in range(1,image.size[1]-1):
            nimg.putpixel((x,y),filtre3x3(image.getpixel((x-1,y-1)),image.getpixel((x,y-1)),image.getpixel((x+1,y-1)),image.getpixel((x-1,y)),image.getpixel((x,y)),image.getpixel((x,y+1)),image.getpixel((x-1,y+1)),image.getpixel((x,y+1)),image.getpixel((x+1,y+1))))
    return nimg

#####################################exif##################

from PIL import ExifTags

def lireEXIF(image):
    """
    renvoie le dictionnaire des EXIF
    """
    exif = {
    ExifTags.TAGS[k]: v
    for k, v in image._getexif().items()
    if k in ExifTags.TAGS
    }
    return exif



