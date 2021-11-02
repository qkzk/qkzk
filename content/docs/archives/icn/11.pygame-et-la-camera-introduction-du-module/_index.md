---
author: qu3nt1n
date: 2017-04-09 09:25:22+00:00
draft: false
title: '11. Pygame et la camera : introduction du module'
bookCollapseSection: true

weight: 11
---

<table rules="none" width="638" style="height: 122px;" class="docinfo docutils field-list" frame="void" >
<tbody valign="top" >
<tr class="field-odd field" >
Author:

<td class="field-body" >by Nirav Patel
</td>
</tr>
<tr class="field-even field" >
Contact:

<td class="field-body" >[nrp@eclecti.cc](mailto:nrp%40eclecti.cc)
</td>
</tr>
<tr class="field-odd field" >
Tradution:

<td class="field-body" >par qkzk
</td>
</tr>
</tbody>
</table>
[Lien vers l'article original](http://www.pygame.org/docs/tut/CameraIntro.html)


## Introduction




#### Remarques préliminaires :





 	  1. ** **Ce tutoriel est difficile, il demande de régulièrement mettre à jour un script Python et, pour cela, il faut parfaitement comprendre ce qu'il fait. Voilà pourquoi une solution complète est disponible à la fin de cet article. Vous pouvez tout à fait l'utiliser en première lecture ; comprenez bien que vous ne parviendrez pas à dépasser ce tutoriel si vous n'en faites pas parfaitement l'acquisition.
 	  2. Il fonctionne sous LINUX et donc pas directement sur vos PC WINDOWS. Il faut donc l'utiliser sur un raspberry pi équipé D'UNE CAMERA... sur lequel Pygame est installé.
 	  3. Ce tutoriel utilise **Pygame**. Il est inutile d'espérer le comprendre si vous n'avez jamais rien fait dans Pygame. Les manipulations élémentaires (display, window, blit, events etc.) doivent être comprises.
 	  4. Pygame 1.9 supporte la gestion des camera, vous permettant de capturer des images fixes, de regarder des vidéos en live et de faire un peu de computer vision. Ce tutoriel va présenter ces situations et fournir des exemples de code sur lesquels appuyer vos jeux et applications. Vous pouvez vous appuyer sur [`reference documentation`](http://www.pygame.org/docs/ref/camera.html#module-pygame.camera) pour l'API complète.
**Remarque : **Dans Pygame 1.9, le module camera fournit une utilisation native de la camera pour celles qui utilisent v4l2 dans Linux. Certaines autres plateformes sont supportées en via Videocapture ou OpenCV, mais ce guide va se concentrer sur l'utilisation native. La plupart des exemples vont fonctionner sur d'autres plateformes, mais certains outils comme les contrôles ne fonctionneront plus. Ce module est aussi qualifié **D'EXPERIMENTAL**, signifiant qu'il peut évoluer dans les versions ultérieures.



### Import et Init




    import pygame
    import pygame.camera
    from pygame.locals import *

    pygame.init()
    pygame.camera.init()


Le module camera est optionnel, il doit donc être importé et initialisé manuellement de cette manière.


### Capture d'une simple image


Commençons par le cas le plus simple, on ouvre la camera et on capture une frame comme une surface de pygame.
On assume dans l'exemple suivant qu'il y a une camera à /dev/video0 et on l'initialise en 640x480
La surface est ce que la camera voit quand get_image() est appelé


    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    image = cam.get_image()




#### Lister les cameras connectées


Et si on ne connait pas le chemin de la camera ? On peut demander au module de fournir une liste de cameras raccordées à l'ordi et d'initialiser la première de la liste.


    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0],(640,480))




#### Utiliser les contrôles de la camera


La plupart des cameras supportent les contrôles tels que retourner l'image et changer sa luminosité.
set_controls() et get_controls() peuvent etre utilisés à tout moment après avoir utilisé start().


    cam.set_controls(hflip = True, vflip = False)
    print cam.get_controls()




### Capturer un Stream en live


Le reste du tutoriel sera focalisé sur la capture d'un stream en live d'images.
Pour cela, nous utiliserons la classe définie ci-dessous. Comme décrit, nous allons seulement blit un stream de frames issues de la camera sur l'écran, ce qui montrera la vidéo en live.
C'est grosso-modo ce à quoi on s'attend, on boucle get_image(), on blit sur la surface d'affichage et on la retourne.
Pour des raisons de performance, on demandera à la camera d'utiliser toujours la même surface.


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


Etant donné que get_image() est un appel bloquant cela peut prendre un peu de temps sur une camera lente, cet exemple utilise query_image() pour voir si la camera est prête. Cela permet de séparer le framerate de votre jeu de celui de la camera. Si vous trouvez que votre camera ne supporte pas bien
les query_image(), c'est aussi possible d'avoir la capture d'images de la camera dans un thread séparé,
pour environ le même gain de performance.


### Computer Vision de base


En utilisant la camera et les masques, pygame peut faire un peu de computer vision.


#### Colorspaces


En initialisant une camera on peut définir un paramètre optionnel de couleur, avec 'RGB', 'YUV' et 'HSB' comme choix possibles.

'YUV' et 'HSB' sont plus utiles pour le computer vision car il est plus facile de filtrer par couleur, ce que nous ferons plus bas dans ce tutoriel.


    self.cam = pygame.camera.Camera(self.clist[0], self.size, "RGB")



![](http://www.pygame.org/docs/_images/camera_rgb.jpg)



    self.cam = pygame.camera.Camera(self.clist[0], self.size, "YUV")



![](http://www.pygame.org/docs/_images/camera_yuv.jpg)



     self.cam = pygame.camera.Camera(self.clist[0], self.size, "HSV")



![](http://www.pygame.org/docs/_images/camera_hsv.jpg)



#### Thresholding = filtrage par seuil


En employant la fonction threshold du module transform on peut isoler des objets de couleur dans une scène. Dans l'exemple ci-dessous, on filtre l'arbre vert (en l'affichant) et on rend le reste de l'image noir. Lisez la référence à la fonction threshold pour plus de détails. [`threshold function`](http://www.pygame.org/docs/ref/transform.html#pygame.transform.threshold).


    self.thresholded = pygame.surface.Surface(self.size, 0, self.display)
    self.snapshot = self.cam.get_image(self.snapshot)
    pygame.transform.threshold(self.thresholded,self.snapshot,(0,255,0),(90,170,170),(0,0,0),2)



![](http://www.pygame.org/docs/_images/camera_thresholded.jpg)


Bien sur, ceci n'est utile que si vous connaissez déjà la couleur exacte d'un objet que vous recherchez.
Pour éviter ce problème et rendre le filtrage par seuil utile dans le monde réel, on a besoin d'une étape de calibrage où l'on identifie la couleur d'un objet et où on l'utilise pour filtrer contre elle.
Nous allons utiliser la fonction average_color() du module transform pour faire ça. Un exemple de fonction de calibrage est fourni ci-dessous. Vous pouvez la faire tourner en boucle jusqu'à avoir une couleur satisfaisante et l'arrêter par un événement comme une pression clavier. La couleur dans la boite sera celle utilisée comme seuil. Remarquez qu'on utilise les couleurs HSV.


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


![](http://www.pygame.org/docs/_images/camera_average.jpg)



    # threshold recupéré pendant le calibrage
    pygame.transform.threshold(self.thresholded,self.snapshot,self.ccolor,(30,30,30),(0,0,0),2)


![](http://www.pygame.org/docs/_images/camera_thresh.jpg)


Vous pouvez utiliser la meme idee pour faire un fond vert/bleu, d'abord en en recuperant une image de fond et ensuite en filtrant par seuil contre elle. L'exemple ci dessous pointe d'abord la camera sur un mur blanc en couleur HSV.


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


![](http://www.pygame.org/docs/_images/camera_background.jpg)



    pygame.transform.threshold(self.thresholded,self.snapshot,(0,255,0),(30,30,30),(0,0,0),1,self.background)


![](http://www.pygame.org/docs/_images/camera_green.jpg)



#### Utiliser le module Mask


Les exemples ci-dessus sont très bien si vous voulez simplement afficher une image mais avec le
[`mask module`](http://www.pygame.org/docs/ref/mask.html#module-pygame.mask), vous pouvez aussi utiliser la camera comme un périphérique de jeu.
Par exemple, en filtrant par seuil un objet particulier, on peut s'en servir pour repérer la position d'un objet spécifique et l'utiliser pour contrôler un autre objet sur l'écran.


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


![](http://www.pygame.org/docs/_images/camera_mask.jpg)


Ce ne sont que les exemples les plus simples. Vous pouvez suivre différents objets de couleur à l'écran, déterminer les contours d'objets, gérer des détections de collision entre le monde réel et un objet à l'écran, déterminer les coins d'un objets pour manipuler plus précisément etc. Amusez vous bien !

[Solution complète](http://qkzk.xyz/?page_id=869)
