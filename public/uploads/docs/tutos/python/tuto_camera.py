#!/usr/bin/env python
# coding=utf-8


# importer la camera dans pygame

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

# Capturer une simple image
'''
On ouvre la camera et on capture une frame comme une surface
de pygame.
On assume dans l'exemple suivant qu'il y a une camera à
/dev/video0 et on l'initialise en 640x480
La surface est ce que la camera voit quand get_image() est appelé
'''

# cam = pygame.camera.Camera("/dev/video0",(640,480))
# cam.start()
# image = cam.get_image()

# Lister les cameras connectees
'''
Et si on ne connait pas le chemin de la camera ?
On peut demander au module de fournir une liste de cameras
raccordées à l'ordi et d'initialiser la premiere de la liste
'''
# camlist = pygame.camera.list_cameras()
# if camlist:
#     cam = pygame.camera.Camera(camlist[0],(640,480))

# Utiliser les controles de la camera
'''
La plupart des cameras supportent les controles tels que
retourner l'image et changer sa luminosité.
set_controls() et get_controls() peuvent etre utilisés
à tout moment apres avoir utilise start()
'''

# cam.set_controls(hflip = True, vflip = False)
# print cam.get_controls()


# Capturing a Live Stream
'''
Le reste du tutoriel sera focalisé sur la capture d'un
stream en live d'images.
Pour cela, nous utiliserons la classe définie ci-dessous.
Comme décrit, nous allons seulement blit un stream de frames
issues de la camera sur l'ecran, ce qui montrera
la video en live.
C'est grosso-modo ce à quoi on s'attend, on boucle get_image(),
on blit sur la surface d'affichage et on la retourne.
Pour des raisons de performance, on demandera à la camera
d'utiliser toujours la meme surface.
'''
class Capture(object):
    def __init__(self):
        self.size = (640,480)
        # crée une suface d'affichage. comme tjrs dans pygame
        self.display = pygame.display.set_mode(self.size, 0)

        # on reprend ce qu'on a fait plus tot
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # on crée une surface sur laquelle capture. Pour des raisons
        # de performance, les dimensions sont celles de la surface
        # d'affichage
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # Vous pouvez délier les framerates de la camera et de l'application
        # vous pouvez vérifier si la camera a une image de prete.
        # Remarquez que cela fonctionne sur la majorite des cameras mais
        # certaines ne répondront jamais True.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # on blit l'objet sur la surface d'affichage. Simple !
        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # ferme proprement la camera
                    self.cam.stop()
                    going = False

            self.get_and_flip()





'''
Etant donné que get_image() est un appel bloquant cela peut
prendre un peu de temps sur une camera lente, cet
exemple utilise query_image() pour voir si la camera
est prête. Cela permet de séparer le framerate de votre jeu
de celui de la camera.
Si vous trouvez que votre camera ne supporte pas bien
les query_image(), c'est aussi possible d'avoir la camera
qui capture des images dans un thread à part,
pour environ le même gain de performance.
'''

# Computer Vision de base
'''
En utilisant la camera et les masques, pygame peut faire un peu
de computer vision
'''

# Colorspaces
'''
En initilisant une camera on peut définir un parametre optionnel
de couleur, avec 'RGB', 'YUV' et 'HSB' comme choix possibles.
'YUV' et 'HSB' sont plus utiles pour le computer vision car il est
plus facile de filtrer par couleur, ce que nous ferons plus bas dans
ce tutoriel.

'''
# pour tester remplacer self.cam = ... avec l'un des trois exemples ci-dessous
# self.cam = pygame.camera.Camera(self.clist[0], self.size, "RGB")
# self.cam = pygame.camera.Camera(self.clist[0], self.size, "YUV")
#  self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")

# Thresholding = filtrage par seuil

'''

En employant la fonction threshold du module transform on peut
isoler des objets de couleur dans une scene.
Dans l'exemple ci-dessous, on filtre l'arbre vert (en l'affichant) et
on rend le reste de l'image noir.
Lisez la référence à la fonction threshold pour plus de détails.
http://www.pygame.org/docs/ref/transform.html#pygame.transform.threshold
'''

# self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
# self.snapshot = self.cam.get_image(self.snapshot)
# pygame.transform.threshold(self.thresholded,self.snapshot,(0,255,0),(90,170,170),(0,0,0),2)

class CaptureThresholded(object):
    def __init__(self):
        self.size = (640,480)
        # crée une suface d'affichage. comme tjrs dans pygame
        self.display = pygame.display.set_mode(self.size, 0)

        # on reprend ce qu'on a fait plus tot
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # on crée une surface sur laquelle capture. Pour des raisons
        # de performance, les dimensions sont celles de la surface
        # d'affichage
        self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # Vous pouvez délier les framerates de la camera et de l'application
        # vous pouvez vérifier si la camera a une image de prete.
        # Remarquez que cela fonctionne sur la majorite des cameras mais
        # certaines ne répondront jamais True.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
            self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
            pygame.transform.threshold(self.thresholded,self.snapshot,(255,255,0),(170,170,170),(0,0,0),2)
            # self.thresholded = self.cam.get_image(self.thresholded)



        # on blit l'objet sur la surface d'affichage. Simple !
        # self.display.blit(self.snapshot, (0,0))
        self.display.blit(self.thresholded, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # ferme proprement la camera
                    self.cam.stop()
                    going = False

            self.get_and_flip()




'''

Bien sur, ceci n'est utile que si vous connaissez déjà la couleur exacte
d'un objet que vous recherchez.
Pour éviter ce problème et rendre le filtrage par seuil utile dans
le monde réel, on a besoin d'une étape de calibrage où l'on identifie
la couleur d'un obet et où on l'utilise pour filtrer contre elle.
Nous allons utiliser la fonction average_color() du module transform
pour faire ça.
Un exemple de fonction de calibrage est fourni ci-dessous. Vous pouvez
la faire tourner en boucle jusqu'à avoir une couleur satisfaisante et
l'arrêter par un évenement comme une pression clavier.
La couleur dans la boite sera celle utilisée comme seuil.
Remarquez qu'on utilise les couleurs HSV

'''

# def calibrate(self):
#     # capture the image
#     self.snapshot = self.cam.get_image(self.snapshot)
#     # blit it to the display surface
#     self.display.blit(self.snapshot, (0,0))
#     # make a rect in the middle of the screen
#     crect = pygame.draw.rect(self.display, (255,0,0), (145,105,30,30), 4)
#     # get the average color of the area inside the rect
#     self.ccolor = pygame.transform.average_color(self.snapshot, crect)
#     # fill the upper left corner with that color
#     self.display.fill(self.ccolor, (0,0,50,50))
#     pygame.display.flip()

class CaptureCalibrate(object):
    def __init__(self):
        self.size = (640,480)
        # crée une suface d'affichage. comme tjrs dans pygame
        self.display = pygame.display.set_mode(self.size, 0)

        # on reprend ce qu'on a fait plus tot
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        # mode par defaut
        # self.cam = pygame.camera.Camera(self.clist[0], self.size)
        # RGB
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        # YUV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "YUV")
        # HSV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        print self.cam
        self.cam.start()

        # on crée une surface sur laquelle capture. Pour des raisons
        # de performance, les dimensions sont celles de la surface
        # d'affichage

        # capture initiale normale
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # Vous pouvez délier les framerates de la camera et de l'application
        # vous pouvez vérifier si la camera a une image de prete.
        # Remarquez que cela fonctionne sur la majorite des cameras mais
        # certaines ne répondront jamais True.
        if self.cam.query_image():

            # thresholded
            self.thresholded = pygame.surface.Surface(self.size, 0, self.display)

            # threshold recupéré pendant le calibrage
            pygame.transform.threshold(self.thresholded,self.snapshot,self.ccolor,(30,30,30),(0,0,0),2)

            # on blit l'objet sur la surface d'affichage. Simple !

            # thresholded
            self.display.blit(self.thresholded, (0,0))

            pygame.display.flip()

    def calibrate(self):
        # capture the image
        self.snapshot = self.cam.get_image(self.snapshot)
        # on la blit sur la display surface
        self.display.blit(self.snapshot, (0,0))
        # dessiner un rectangle au milieu de l'ecran
        crect = pygame.draw.rect(self.display, (255,0,0), (145,105,30,30), 4)
        # recupere la couleur moyenne de la zone dans le rectangle
        self.ccolor = pygame.transform.average_color(self.snapshot, crect)
        # rempli le coin superieur gauche de l'ecran avec cette couleur
        self.display.fill(self.ccolor, (0,0,50,50))
        pygame.display.flip()



    def main(self):

        going = True
        # calibrate
        # On calibre jusqu'à appuyer sur espace... tant qu'on n'appuie pas sur espace
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == KEYDOWN and e.key == K_SPACE:
                    going = False
            self.calibrate()

        # ensuite on affiche !
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # ferme proprement la camera
                    self.cam.stop()
                    going = False

            self.get_and_flip()


# Fond vert

# Vous pouvez utiliser la meme idee pour faire un fond vert/bleu, d'abord en en recuperant une image de fond et ensuite en filtrant par seuil contre elle. L'exemple ci dessous pointe d'abord la camera sur un mur blanc en couleur HSV


class CaptureGreenScreen(object):
    def __init__(self):
        self.size = (640,480)
        # crée une suface d'affichage. comme tjrs dans pygame
        self.display = pygame.display.set_mode(self.size, 0)

        # on reprend ce qu'on a fait plus tot
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        # mode par defaut
        # self.cam = pygame.camera.Camera(self.clist[0], self.size)
        # RGB
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        # YUV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "YUV")
        # HSV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        print self.cam
        self.cam.start()

        # on crée une surface sur laquelle capture. Pour des raisons
        # de performance, les dimensions sont celles de la surface
        # d'affichage

        # capture initiale normale
        self.background = pygame.surface.Surface(self.size, 0, self.display)
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.thresholded = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        # Vous pouvez délier les framerates de la camera et de l'application
        # vous pouvez vérifier si la camera a une image de prete.
        # Remarquez que cela fonctionne sur la majorite des cameras mais
        # certaines ne répondront jamais True.
        if self.cam.query_image():

            # thresholded
            self.snapshot = self.cam.get_image(self.snapshot)
            # self.thresholded = self.cam.get_image(self.thresholded)
            self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
            # self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
            # threshold recupéré pendant le calibrage
            pygame.transform.threshold(self.thresholded,self.snapshot,(0,255,0),(30,30,30),(0,0,0),1,self.background)


            # on blit l'objet sur la surface d'affichage. Simple !

        # thresholded
        self.display.blit(self.thresholded, (0,0))

        pygame.display.flip()

    def calibrate(self):
        # capture quelques images de fond
        bg = []
        for i in range(0,5):
          bg.append(self.cam.get_image(self.background))
        # prend la moyenne pour filtrer le bruit
        pygame.transform.average_surfaces(bg,self.background)
        # la blit sur la surface
        self.display.blit(self.background, (0,0))
        pygame.display.flip()



    def main(self):

        # on calibre d'abord l'image
        self.calibrate()

        # ensuite on affiche !
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # ferme proprement la camera
                    self.cam.stop()
                    going = False

            self.get_and_flip()

# Utiliser le module Mask

'''
Les exemples ci-dessus sont très bien si vous voulez simplement afficher
une image mais avec le module mask (http://www.pygame.org/docs/ref/mask.html#module-pygame.mask)
vous pouvez aussi utiliser la camera comme un périphérique de jeu.
Par exemple, en filtrant par seuil un objet particulier, on peut s'en servir
pour repérer la position d'un objet specifique et l'utiliser pour controler
un autre objet sur l'écran.
'''

class CaptureMask(object):
    def __init__(self):
        self.size = (640,480)
        # crée une suface d'affichage. comme tjrs dans pygame
        self.display = pygame.display.set_mode(self.size, 0)

        # on reprend ce qu'on a fait plus tot
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        # mode par defaut
        # self.cam = pygame.camera.Camera(self.clist[0], self.size)
        # RGB
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        # YUV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "YUV")
        # HSV
        # self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")
        print self.cam
        self.cam.start()

        # on crée une surface sur laquelle capture. Pour des raisons
        # de performance, les dimensions sont celles de la surface
        # d'affichage

        # capture initiale normale
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_and_flip(self):
        self.snapshot = self.cam.get_image(self.snapshot)
        # filtre contre la couleur obtenue plus tot
        mask = pygame.mask.from_threshold(self.snapshot, self.ccolor, (30, 30, 30))
        self.display.blit(self.snapshot,(0,0))
        # ne garde que le plus grand blob a l'ecran
        connected = mask.connected_component()
        # on s'assure que le blob est grand, afin de filtrer le bruit
        if mask.count() > 100:
            # trouve son centre
            coord = mask.centroid()
            # dessine un cercle de taille correspondant a celle du blob
            pygame.draw.circle(self.display, (0,255,0), coord, max(min(50,mask.count()/400),5))
        pygame.display.flip()

    def calibrate(self):
        # capture the image
        self.snapshot = self.cam.get_image(self.snapshot)
        # blit it to the display surface
        self.display.blit(self.snapshot, (0,0))
        # make a rect in the middle of the screen
        crect = pygame.draw.rect(self.display, (255,0,0), (145,105,30,30), 4)
        # get the average color of the area inside the rect
        self.ccolor = pygame.transform.average_color(self.snapshot, crect)
        # fill the upper left corner with that color
        self.display.fill(self.ccolor, (0,0,50,50))
        pygame.display.flip()



    def main(self):

        going = True
        # calibrate
        # On calibre jusqu'à appuyer sur espace... tant qu'on n'appuie pas sur espace
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == KEYDOWN and e.key == K_SPACE:
                    going = False
            self.calibrate()

        # ensuite on affiche !
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # ferme proprement la camera
                    self.cam.stop()
                    going = False

            self.get_and_flip()


# def get_and_flip(self):
#     self.snapshot = self.cam.get_image(self.snapshot)
#     # threshold against the color we got before
#     mask = pygame.mask.from_threshold(self.snapshot, self.ccolor, (30, 30, 30))
#     self.display.blit(self.snapshot,(0,0))
#     # keep only the largest blob of that color
#     connected = mask.connected_component()
#     # make sure the blob is big enough that it isn't just noise
#     if mask.count() > 100:
#         # find the center of the blob
#         coord = mask.centroid()
#         # draw a circle with size variable on the size of the blob
#         pygame.draw.circle(self.display, (0,255,0), coord, max(min(50,mask.count()/400),5))
#     pygame.display.flip()


'''
Ce ne sont que les exemples les plus simples. Vous pouvez suivre differents
objets de couleur à l'écran, déterminer les contours d'objets, gérer des
détections de collision entre le monde réel et un objet à l'écran,
déterminer les coins d'un objets pour manipuler plus précisément etc. Amusez vous bien !

'''
if __name__ == '__main__':
    # test des differentes classes
    # webcam = Capture()
    # webcam = CaptureThresholded()
    # webcam = CaptureCalibrate()
    # webcam = CaptureGreenScreen()
    webcam = CaptureMask()

    webcam.main()
