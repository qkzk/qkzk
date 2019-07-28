---
author: qu3nt1n
date: 2017-04-09 16:54:56+00:00
draft: false
title: '10. Un jeu complet en pygame : dodger'

url: /
---

# DODGER


[article original](http://inventwithpython.com/chapter20.html) traduit par mes soins.

Voici un tutoriel permettant de créer un jeu complet à l'aide de Python (2.7) et pygame (1.9)

Il est nécessaire de disposer de connaissances sur Python et Pygame (import, init, blit, events) avant de l'aborder

_Pour ceux qui y étaient, ce jeu a servi de démonstration de travaux d'élèves lors des portes ouvertes du Lycée des Flandres en mars 2017. Il m'a semblé intéressant de le présenter._

Quelques-uns des thèmes abordés :



 	  * Le flag pygame.FULLSCREEN
 	  * Les variables "constates"  de Pygame pour les touches clavier
 	  * La méthode move_ip() Rect
 	  * La fonction pygame.mouse.set_pos()
 	  * Création de cheat codes cheat codes
 	  * Modifier le Dodger game



Dans ce tutoriel on utilise les notions de base du module Pygame pour créer un jeu graphique appelé Dodger.




Le jeu Dodger présente un joueur (player) qui doit éviter (to dodge) des méchant (baddies) qui lui tombent dessus depuis le haut de l'écran. Plus le joueur reste en vie longtemps, plus il augmente son score.




Pour l'amusement nous ajouterons aussi un mode de cheat : si le joueur maintient "x" les méchants ralentissent. S'il maintient "z" ils remontent.





## Revue des objets typiques de Pygame


Revoyons quelques types de données standard utilisés dans Pygame  :



 	  * pygame.Rect - Les objets Rect représentent un espace rectangulaire définis par une position et des dimensions.
La position est définie par l'attribut topleft (coin supérieur gauche) (ou les attributs topright, bottomleft, et bottomright). Ces attributs de coins sont des tuple d'entiers (X,Y). X et Y etant donc des coordonnées.
La dimension peut être définie par largeur et hauteur (width, height). Ce sont des entiers. Les objets Rect objects ont une méthode colliderect() permettant de vérifier s'ils se superposent à d'autres rectangles.
 	  * pygame.Surface - Les objets Surface sont des domaines de pixels de couleur. Ils représentent une image rectangulaire, tandis que les objets Rect ne représentent qu'un rectangle et une dimension. Les objets Surface ont une méthode blit() employée pour dessiner l'image d'une surface sur une autre surface. L'objet Surface renvoyé par la fonction pygame.display.set_mode() est particulier parce que tout ce qui est envoyé dessus est dessiné à l'écran quand pygame.display.update() est appelé.
 	  * pygame.event.Event - Le module pygame.event génère des objets Event dès que l'utilisateur utilise le clavier, la souris ou tout autre périphérique d'entrée (voir Computer vision & Python sur ce même site pour une utilisation de la webcam). La fonction pygame.event.get() renvoie une liste de ces événements objects. Vous pouvez vérifier quel type d'événement vous manipulez en consultant son attribut Type. QUIT, KEYDOWN, et MOUSEBUTTONUP sont des exemples d'événements.
 	  * pygame.font.Font - Le module pygame.font dispose du type de donnée Font qui représente la police utilisée par Pygame. Les paramètres à envoyer à  pygame.font.SysFont() sont une chaîne de caractère pour le nom et un entier pour la taille. Cependant il est courant d'envoyer None pour le nom afin d'employer la fonte par défaut.
 	  * pygame.time.Clock - L'objet Clock du module pygame.time permet de rendre nos jeux les plus rapides possibles. L'horloge dispose d'une méthode tick(), à laquelle nous passons le nombre de FPS (frame par seconde) auxquels nous voulons faire tourner le jeu. Plus les FPS sont élevées plus le jeu tourne rapidement.

Récupérez le code suivant et sauvegardez le dans un fichier _dodger.py. _Ce jeu requiert aussi quelques fichiers d'images et de sons disponibles.

Le [joueur](http://qkzk.xyz/docs/tutos/python/dodger/player.png), le [méchant](http://qkzk.xyz/docs/tutos/python/dodger/baddie.png), le [son gameover](http://qkzk.xyz/docs/tutos/python/dodger/gameover.wav), la [musique de fond](http://qkzk.xyz/docs/tutos/python/dodger/background.mid).

    
    #!/usr/bin/env python
    # coding=utf-8
    import pygame, random, sys
    from pygame.locals import *
    
    WINDOWWIDTH = 600
    WINDOWHEIGHT = 600
    TEXTCOLOR = (255, 255, 255)
    BACKGROUNDCOLOR = (0, 0, 0)
    FPS = 40
    BADDIEMINSIZE = 10
    BADDIEMAXSIZE = 40
    BADDIEMINSPEED = 1
    BADDIEMAXSPEED = 8
    ADDNEWBADDIERATE = 6
    PLAYERMOVERATE = 5
    
    def terminate():
        pygame.quit()
        sys.exit()
    
    def waitForPlayerToPressKey():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: # pressing escape quits
                        terminate()
                    return
    
    def playerHasHitBaddie(playerRect, baddies):
        for b in baddies:
            if playerRect.colliderect(b['rect']):
                return True
        return False
    
    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # set up pygame, the window, and the mouse cursor
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dodger')
    pygame.mouse.set_visible(False)
    
    # set up fonts
    font = pygame.font.SysFont(None, 48)
    
    # set up sounds
    gameOverSound = pygame.mixer.Sound('gameover.wav')
    pygame.mixer.music.load('background.mid')
    
    # set up images
    playerImage = pygame.image.load('player.png')
    playerRect = playerImage.get_rect()
    baddieImage = pygame.image.load('baddie.png')
    
    # show the "Start" screen
    drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    
    topScore = 0
    while True:
        # set up the start of the game
        baddies = []
        score = 0
        playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
        moveLeft = moveRight = moveUp = moveDown = False
        reverseCheat = slowCheat = False
        baddieAddCounter = 0
        pygame.mixer.music.play(-1, 0.0)
    
        while True: # the game loop runs while the game part is playing
            score += 1 # increase score
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
    
                if event.type == KEYDOWN:
                    if event.key == ord('z'):
                        reverseCheat = True
                    if event.key == ord('x'):
                        slowCheat = True
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == ord('w'):
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveUp = False
                        moveDown = True
    
                if event.type == KEYUP:
                    if event.key == ord('z'):
                        reverseCheat = False
                        score = 0
                    if event.key == ord('x'):
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                        terminate()
    
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False
    
                if event.type == MOUSEMOTION:
                        # If the mouse moves, move the player where the cursor is.
                        playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
    
            # Add new baddies at the top of the screen, if needed.
            if not reverseCheat and not slowCheat:
                baddieAddCounter += 1
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                }
    
                baddies.append(newBaddie)
    
            # Move the player around.
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                playerRect.move_ip(0, PLAYERMOVERATE)
    
            # Move the mouse cursor to match the player.
            pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)
    
            # Move the baddies down.
            for b in baddies:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif reverseCheat:
                    b['rect'].move_ip(0, -5)
                elif slowCheat:
                    b['rect'].move_ip(0, 1)
    
            # Delete baddies that have fallen past the bottom.
            for b in baddies[:]:
                if b['rect'].top > WINDOWHEIGHT:
                    baddies.remove(b)
    
            # Draw the game world on the window.
            windowSurface.fill(BACKGROUNDCOLOR)
    
            # Draw the score and top score.
            drawText('Score: %s' % (score), font, windowSurface, 10, 0)
            drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
    
            # Draw the player's rectangle
            windowSurface.blit(playerImage, playerRect)
    
            # Draw each baddie
            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])
    
            pygame.display.update()
    
            # Check if any of the baddies have hit the player.
            if playerHasHitBaddie(playerRect, baddies):
                if score > topScore:
                    topScore = score # set new top score
                break
    
            mainClock.tick(FPS)
    
        # Stop the game and show the "Game Over" screen.
        pygame.mixer.music.stop()
        gameOverSound.play()
    
        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()
    
        gameOverSound.stop()
    


Voici ce que vous devriez voir (les sprites sont différents de ceux de la capture).
![](http://inventwithpython.com/chapter20_files/image002.jpg)



### Importer les modules



    
    #!/usr/bin/env python
    # coding=utf-8
    import pygame, random, sys
    from pygame.locals import *


Le jeu Dodger import les modules usuels après avoir défini l'encodage et l'environnement :pygame, random, sys, et pygame.locals. pygame.locals contient plusieurs variables utilisées par Pygame tels que les événements  (QUIT, KEYDOWN, etc.) et les touches du clavier (K_ESCAPE, etc.). En utilisant cette la syntaxe from pygame.locals import * syntax, vous pouvez simplement taper QUIT dans le code source au lieu de pygame.locals.QUIT.


### Réglage des variables Constantes



    
    WINDOWWIDTH = 600
    WINDOWHEIGHT = 600
    TEXTCOLOR = (255, 255, 255)
    BACKGROUNDCOLOR = (0, 0, 0)


Les constantes tapées entre les lignes 4 et 14 sont plus explicites que si l'on tapait directement les valeurs. Par exemple, windowSurface.fill(BACKGROUNDCOLOR) est plus facile à comprendre que windowSurface.fill((0, 0, 0)).


Vous pouvez les changer facilement dans le jeu et éditant le code source. En changeant WINDOWWIDTH à la ligne 4, vous le modifiez à toutes les lignes où il intervient WINDOWWIDTH. Si vous aviez tapé 600 à la place, vous devriez les changer toutes les fois où il intervient.









    
    FPS = 40




Le tick de l'horloge principale utilisée à la ligne 189 va ralentir le jeu suffisamment pour le rendre jouable. On envoie un entier à mainClock.tick() de façon à ce que le jeu sache combien de temps mettre en pause le programme. Cet entier est donc le nombre de FPS auquel on souhaite faire tourner le jeu.




Une "frame" est le dessin d'une image à l'écran pour une seule itération de la boucle du jeu. Vous pouvez régler le jeu à 40 FPS et toujours appeler mainClock.tick(FPS). Ensuite, en augmentant FPS, vous accélérez le jeu, en le diminuant vous ralentissez le jeu.




    
    BADDIEMINSIZE = 10
    BADDIEMAXSIZE = 40
    BADDIEMINSPEED = 1
    BADDIEMAXSPEED = 8
    ADDNEWBADDIERATE = 6




Les lignes 11 à 15 définissent d'autres constantes qui décrivent le comportement des méchants. Les dimensions des méchants seront comprises entre BADDIEMINSIZE et BADDIEMAXSIZE. Le rythmer auquel les méchants tombent de l'écran sera fixé entre BADDIEMINSPEED et BADDIEMAXSPEED pixels par itération de la boucle de jeu. Et un nouveau méchant sera ajouté toutes les ADDNEWBADDIERATE itérations.







    
    PLAYERMOVERATE = 5


PLAYERMOVERATE décrit le nombre de pixel que le jouer traverse à chaque itération. L'augmenter permet donc d'accélérer le joueur.


## Définir les fonctions




Plusieurs fonctions sont utilisées dans le jeu.




    
    def terminate():
        pygame.quit()
        sys.exit()


Pygame doit être quitté en appelant à la fois pygame.quit et sys.exit. On les ajoute donc tous les deux à une fonction  terminate qui sera appelée pour clore le jeu en une seule commande.

    
    def waitForPlayerToPressKey():
        while True:
            for event in pygame.event.get():


Parfois il est commode de pouvoir mettre en pause le jeu jusqu'à ce qu'un joueur presse une touche. Créer waitForPlayerToPressKey() et dans cette fonction, inclure une boucle infinie qui ne s'arrête (break) que lorsque qu'un événement KEYDOWN ou QUIT est enregistré. Au début de cette boucle, pygame.event.get() permet de définir la liste des événements en question.

    
    if event.type == QUIT:
        terminate()


Si le joueur a fermé la fenêtre quand le jeu est en pause, Pygame va générer un événement QUIT.

    
    if event.type == KEYDOWN:
         if event.key == K_ESCAPE: # pressing escape quits
             terminate()
              return


Même chose si la touche Escape du clavier est enregistrée parmi les événements clavier.

Si aucun QUIT ou KEYDOWN n'est enregistré, alors le code tourne en boucle. Cette boucle ne faisant rien, cela revient à mettre en pause tant qu'une touche n'est pas pressée.

    
    def playerHasHitBaddie(playerRect, baddies):
        for b in baddies:
            if playerRect.colliderect(b['rect']):
                return True
        return False


La fonction playerHasHitBaddie() va renvoyer True si le joueur a heurté l'un des méchants. Le parametre méchants est une liste de dictionnaires de méchants. Chacun de ces dictionnaire contient une clé 'rect' et la valeur de cette clé est un objet Rect qui représente la taille et la position du baddie.

playerRect est aussi un objet Rect. Ces objets ont une méthode colliderect() qui renvoie True si l'objet Rect a heurté celui envoyé en paramètre. Sinon coliiderect() va renvoyer False.

La boucle for de la ligne 33 tourne sur la liste des baddies et s'arrête dès que l'une des collisions est détectée. Si le code parcourt toute la liste sans passer à vrai, alors la fonction renvoie False.

    
    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


Quelques étapes doivent être accomplie pour écrire du texte à l'écran. Premièrement, la méthode render() appelée à la ligne 37 crée un objet Surface qui contient le texte et la police.
Ensuite on doit connaître la taille et la position de cet objet Surface. On peut obtenir définir cette position à l'aide d'un get_rect(). Ainsi l'objet Rect de la ligne 40 contient une copie de la taille et la hauteur définie par la surface. Ligne 41 on met à joueur la position du Rect en lui passant un tuple (x, y).
Enfin, ligne 42 on blit la Surface du textobj sur le textrect.

Ecrire du texte en pygame est plus complexe que d'appeler un simple print() néanmoins, en créant cette fonction, vous n'avez plus qu'à l'appeler une fois avec tous les paramètres pour le faire.


## Initialiser pygame et et définir la fenêtre.


Les constantes et les fonctions étant définies, il est possible de définir la fenêtre et l'horloge.

    
    pygame.init()
    mainClock = pygame.time.Clock()


La ligne 45 lance pygame avec l'appel à init(). La suivante défini l'horloge time.Clock() qui empêchera le jeu de tourner trop vite.

    
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    


Ligne 47 on crée une nouvelle Surface qui servira à définir la fenêtre affichée à l'écran. On emploie ici les dimensions crées plus haut. Remarquons qu'on ne passe qu'un seul argument à set_mode(), un tuple ! Les dimensions ne sont pas deux entiers mais un tuple les contenant.

    
    pygame.display.set_caption('Dodger')


On défini ici le titre du jeu, il apparaîtra en haut de l'écran.

    
    pygame.mouse.set_visible(False)
    


On cache le curseur de la souris. En effet, on se servira de la souris pour déplacer le joueur.


## Mode plein écran



    
     windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)


En changeant ainsi la ligne 47 on rend le jeu plein écran. La fenêtre est étendue jusqu'aux dimensions maximales de l'écran. Testez le jeu dans les deux modes pour bien comprendre son fonctionnement.

    
    # set up fonts
    font = pygame.font.SysFont(None, 48)


On défini un objet font en appelant font.SysFont. Le premier paramètre permet de la choisir et, en passant None, on choisit la police par défaut. Le second est sa taille.

    
    # set up sounds
    gameOverSound = pygame.mixer.Sound('gameover.wav')
    pygame.mixer.music.load('background.mid')


Ensuite on crée les objets sonores. Le premier est le son game over qui est appelé quand on perd.
Le second est la musique de fond qui est tourne en permanence. Il est possible de jouer n'importe quel .wav ou .mid dans le jeu.

Il est possible d'appeler mixer.Sound autant de fois que l'on souhaite mais mixer.music.load ne peut être appelée qu'une seule fois. Ces constructeurs ne renvoient rien.

    
    # set up images
    playerImage = pygame.image.load('player.png')
    playerRect = playerImage.get_rect()
    baddieImage = pygame.image.load('baddie.png')


On défini ici les images qui seront utilisées pour le joueur et les méchants. Tous les méchants ont la même image donc un seul fichier suffit.


## Afficher l'écran de démarrage


Quand le jeu se lance, on affiche son nom à l'écran. On souhaite aussi expliquer à l'utilisateur comment jouer. Cet écran sert à donner le temps à l'utilisateur de se préparer.

    
    # show the "Start" screen
    drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()


On appelle le drawText avec 5 arguments :



 	  1. le string contenant le texte
 	  2. la police
 	  3. la surface sur laquelle écrire
 	  4. l'abscisse x
 	  5. l'ordonnée y

Cela peut sembler beaucoup mais souvenons nous de la définition de drawText un peu plus haut. Elle demandait bien ces paramètres. Ce type d'appel simplifie grandement le code.

La fonction waitForPlayerToPressKey() va mettre le jeu en pause jusqu'à ce que l'utilisateur presse un touche pour le lancer.


## Lancement du mode de jeu



    
    topScore = 0
    while True:


Le meilleur score est stocké dans une variable.
On lance ensuite une boucle infinie qui va décrire une partie complète. A chaque défaite, on retourne ligne 71. Techniquement, ce n'est donc pas la boucle infinie du jeu.

    
    # set up the start of the game
    baddies = []
    score = 0


A chaque partie on initialise la liste des méchants et le score de la partie en cours.
La variable baddies est une liste dont chaque élément est un dictionnaire. Ils contiennent les clés suivantes :



 	  * 'rect' : l'objet Rect qui décrit où il se situe et quelle est sa taille
 	  * 'speed' : la vitesse du mechant. Entier qui décrit le nombre de pixels franchis entre chaque frame
 	  * 'surface' : La surface sur laquelle on dessine l'image agrandie ou diminuée du méchant. Cet objet Surface est blitté sur la surface renvoyée par pygame.display.set_mode().


    
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)


Le rect du joueur. Il est positionné par son coin topleft au centre (horizontal) et en bas (vertical). Sa position est un tuple, souvenons nous.
D'autre pas, les coordonnées dans pygame sont : x vers la droite, y vers le bas.

    
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0


Les variables de mouvement du joueur sont toutes initialisées à False. Les deux cheatmode aussi.
Le compteur de méchant est réinitialisé à 0.
Ce compteur augmente de 1 à chaque tour et, quand il vaut ADDNEWBADDIERATE un nouveau méchant est ajouté à l'écran et on réinitialise le compteur à 0.

    
    pygame.mixer.music.play(-1, 0.0)


La musique de fond est lancée ligne 79 en appelant mixer.music.play(). Le premier argument, -1, indique le nombre de fois où elle doit se répéter (-1 : à l'infini).
Le second est un réel (float) qui indique à quelle seconde de la musique vous souhaitez qu'elle commence, 0.0 : du début.


## La boucle de jeu


Le jeu tourne indéfiniment en mettant à jour l'état du monde (position du joueur, des méchants, gestion des événements, dessin des objets). Ceci se déroulant des dizaines de fois par seconde, on obtient une illusion de temps réel.

    
    while True: # the game loop runs while the game part is playing
        score += 1 # increase score


On lance la boucle infinie et on augmente de 1 le score à chaque tour.
Elle ne s'arrêtera que lorsqu'on va perdre ou quitter la partie.


## Gestion des événements


Il y a 4 types d'événements que le programme va gérer : QUIT, KEYDOWN, KEYUP et MOUSEMOTION

    
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()


Ligne 84 est le début du gestionnaire d'événements. Il appelle pygmae.event.get() qui renvoie une liste d'objets Event. Chaque objet est un événement s'étant déroulé depuis le dernier appel à cette fonction. Le code va d'abord comparer le type d'événements et ensuite gérer l'événement en fonction.
Si le type d'événement est QUIT on sort du jeu.

    
    if event.type == KEYDOWN:
        if event.key == ord('z'):
            reverseCheat = True


Si le type d'événement est KEYDOWN, le joueur a enfoncé une touche. L'événement clavier a aussi une clé qui lui est attribuée et qui correspond à la touche pressée. La fonction ord() renvoie la valeur de la touche.
Par exemple, ligne 89 la touche 'z' est enfoncée, alors on passe la valeur reverseCheat à true.

    
    if event.key == K_LEFT or event.key == ord('a'):
        moveRight = False
        moveLeft = True


Les lignes 93 à 104 présentent les déplacements clavier. Remarquons qu'on peut presser à chaque fois deux touches, WASD ou les flèches. Celles-ci n'ont pas de valeur ordinale mais une valeur constante définie par pygame.locals.
D'autre part chaque déplacement change deux variables : moveRight passe à faux et moveLeft à vrai. Les deux déplacements étant incompatibles.
Voici une table présentant les valeurs des touches du clavier.
<table cellpadding="0" cellspacing="0" style="border-collapse: collapse; border: none;" border="1" class="MsoNormalTable" >
<tbody >
<tr >

<td style="border-top: double windowtext 1.5pt; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Pygame Constant Variable



</td>

<td style="border-top: double windowtext 1.5pt; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Keyboard Key



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border-top: double windowtext 1.5pt; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Pygame Constant Variable



</td>

<td style="border-top: double windowtext 1.5pt; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Keyboard Key



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_LEFT



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Left arrow



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_HOME



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Home



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_RIGHT



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Right arrow



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_END



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


End



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_UP



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Up arrow



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_PAGEUP



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


PgUp



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_DOWN



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Down arrow



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_PAGEDOWN



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


PgDn



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_ESCAPE



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Esc



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F1



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F1



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_BACKSPACE



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Backspace



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F2



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F2



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_TAB



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Tab



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F3



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F3



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_RETURN



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Return or Enter



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F4



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F4



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_SPACE



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Space bar



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F5



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F5



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_DELETE



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Del



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F6



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F6



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_LSHIFT



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Left Shift



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F7



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F7



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_RSHIFT



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Right Shift



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F8



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F8



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_LCTRL



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Left Ctrl



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F9



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F9



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_RCTRL



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Right Ctrl



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F10



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F10



</td>
</tr>
<tr >

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_LALT



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Left Alt



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F11



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F11



</td>
</tr>
<tr >

<td style="border: none; border-bottom: double windowtext 1.5pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_RALT



</td>

<td style="border: none; border-bottom: double windowtext 1.5pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


Right Alt



</td>

<td style="border: none; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >
</td>

<td style="border: none; border-bottom: double windowtext 1.5pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


K_F12



</td>

<td style="border: none; border-bottom: double windowtext 1.5pt; padding: 0in 5.4pt 0in 5.4pt;" valign="top" >


F12



</td>
</tr>
</tbody>
</table>

    
    if event.type == KEYUP:
        if event.key == ord('z'):
            reverseCheat = False
            score = 0


L'événement KEYUP est crée à chaque fois que le joueur relache une touche. Ils disposent d'un numéro de touche identiques à ceux de KEYDOWN.
On arrête alors les déplacements et les cheat code en passant les valeurs à False.


## La méthode move_ip()



    
    if event.type == MOUSEMOTION:
            # If the mouse moves, move the player where the cursor is.
            playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)
    


On gère ainsi les événements souris. On ne s'occupe que du déplacement de la souris, pas des boutons.

MOUSEMOTION est généré dès que la souris est déplacée. Ces événements ont aussi un attribut pos pour la position de la souris. C'est un tuple (X,Y) de coordonnées. On déplace alors le joueur à ces coordonnées.

La méthode move_ip() des objets Rect va déplacer la position du Rect horizontalement ou verticalement par un certain nombre de pixels.
Par exemple move_ip(10,20) va déplacer le Rect de 10 en abs et 20 en ordonnée. le "ip" signifie "in place". C'est parce que la méthode change le Rect lui même plutôt que de renvoyer un nouveau Rect. Il existe aussi une méthode move qui renvoie un nouveau Rect situé à la nouvelle position.

    
    # Add new baddies at the top of the screen, if needed.
    if not reverseCheat and not slowCheat:
        baddieAddCounter += 1


On augmente le compteur de baddies de 1 à chaque tour. Ceci ne se produit que si l'on n'est pas en mode cheat.

    
    if baddieAddCounter == ADDNEWBADDIERATE:
        baddieAddCounter = 0
        baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
        newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
        }


Quand le compteur baddieAddCounter arrive à la valeur ADDNEWBADDIERATE, il est temps d'ajouter un méchant à l'écran.
On tire au hasard avec random.randint( ) un entier entre les bornes BADDIEMINSIZE et BADDIEMAXSIZE représentant sa taille.
On crée ensuite le dictionnaire newBaddie = { } contenant les clés 'rect', 'speed' et 'surface'. Rect contient la taille et la position. L'abscisse de la position est aléatoire entre 0 et la taille de l'écran moins la taille du baddie, l'ordonnée est choisie de façon à ce qu'il semble entrer dans l'écran tout en haut. Les dimensions sont égales car le méchant est carré.
La vitesse est aléatoire entre les constantes définies plus haut : BADDIEMINSPEED et BADDIEMAXSPEED
La surface est définie de la même manière que celle du joueur.

    
    baddies.append(newBaddie)


On ajoute ensuite ce nouveau baddie à la liste comme précédemment.


## Le déplacement du joueur



    
    if moveLeft and playerRect.left > 0:
        playerRect.move_ip(-1 * PLAYERMOVERATE, 0)


Les quatre variables de déplacement (moveLeft etc.) sont définies comme vraies ou fausses par les événements clavier. Si le joueur bouge vers la gauche et que son abscisse est positive, il devrait se déplacer.
C'est ce qu'on fait à l'aide de move_ip.

On se déplace selon la vitesse PLAYERMOVERATE définie plus haut. -1*PLAYERMOVERATE est donc la version négative de l'entier en question.

On défini de la même manière les autres déplacements.


## La fonction pygame.mouse.set_pos()



    
    # Move the mouse cursor to match the player.
    pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)


On déplace le curseur à la même position que le joueur en passant à cette fonction les coordonnées : playerRect.centerx et playerRect.centery.
En particulier le curseur sera toujours au centre du Rect du joueur.

    
    # Move the baddies down.
    for b in baddies:
        if not reverseCheat and not slowCheat:
            b['rect'].move_ip(0, b['speed'])


On boucle dans la liste des baddies.
Python permet de boucler directement dans une liste sans effort.
Si les cheatmode ne sont pas activés alors le méchant va se déplacer vers le bas.


## Les cheatmode



    
    elif reverseCheat:
        b['rect'].move_ip(0, -5)
    elif slowCheat:
        b['rect'].move_ip(0, 1)


On fait reculer les monstres ou on les ralenti si selon le cheatmode activé.


## Retirer les méchants



    
    # Delete baddies that have fallen past the bottom.
    for b in baddies[:]:
        if b['rect'].top > WINDOWHEIGHT:
            baddies.remove(b)


Les méchants qui arrivent en bas de l'écran sont simplement retirés de la liste qui les contient.
Attention cependant, il faut s'assurer de ne pas modifier la liste elle même alors qu'on la parcourt. On réalise d'abord une copie de la liste et ensuite on modifie la liste originale. Ceci nous assure que la boucle ne va rencontrer aucune erreur.

Cette copie est réalisée en écrivant baddies[:]
b['rect'] récupère la valeur de la clé 'rect' de l'élément b de la liste. b['rect'].top est donc le haut de cet élément.

On compare ensuite le haut de l'élément Rect à la taille de l'écran et, s'il est supérieur on retire le baddie de la liste.


## Dessiner la fenêtre


Tous les éléments étant à jour, il est temps de dessiner la fenêtre.

La fenêtre étant rafraîchie plusieurs fois par seconde, cela rend les animations fluides.

Les éléments sont dessinés **LES UNS AU DESSUS DES AUTRES. On commence donc par le fond**

    
    # Draw the game world on the window.
    windowSurface.fill(BACKGROUNDCOLOR)


On vient donc d'effacer tous les éléments précédents.

Souvenons nous que l'objet Surface de windowSurface est une surface particuliere renvoyée par pygame.display.set_mode(). Ainsi, tout ce qui est dessiné sur cette surface apparaîtra à l'écran une fois pygame.display.update() appelé.


## Dessiner le score



    
    # Draw the score and top score.
    drawText('Score: %s' % (score), font, windowSurface, 10, 0)
    drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)


On affiche le texte du score et du meilleur score dans le coin de l'écran. 'Score: %s' % (score) est un formatage particulier d'une chaîne de caractère qui va remplacer %s par la valeur contenu dans le tuple (score). On aura donc :

'Score : 172' si la variable score vaut 172.

On les dessine aux coordonnées données en dernier paramètres : respectivement 10, 0 et 10, 40.


## Dessiner le joueur



    
    # Draw the player's rectangle
    windowSurface.blit(playerImage, playerRect)


Les informations du joueur sont stockées dans deux variables : playerImage (son sprite) et playerRect (position et dimension). La méthode blit() dessine l'image playerImage sur la surface windowSurface aux positions de playerRect() et selon ses dimensions.


## Dessiner les méchants



    
    # Draw each baddie
    for b in baddies:
        windowSurface.blit(b['surface'], b['rect'])


On fait de même pour chaque méchant de la liste. On récupère depuis le dictionnaire b les éléments 'surface' et 'rect' qu'on envoie à blit.


## Mise à jour de la fenêtre



    
    pygame.display.update()


On dessine enfin cette surface sur celle de l'écran et tous les éléments vont apparaître.


## Détection des collisions


A cette étape toutes les données sont dessinées à l'écran. Il ne reste plus qu'à détecter les collisions entre le joueur et les méchants.

    
    # Check if any of the baddies have hit the player.
    if playerHasHitBaddie(playerRect, baddies):
        if score > topScore:
            topScore = score # set new top score
        break


On appelle la fonction définie plus haut pour tester la collision entre le joueur et les méchants.
La partie est alors terminée et on va mettre à jour le meilleur score si le score actuel l'a dépassé.

Enfin on arrête la boucle de la partie avec un break.

On revient alors à la boucle contenant le déroulé du jeu.

Si aucune collision n'est détectée on arrive alors ligne 191

    
    mainClock.tick(FPS)


Pour empêcher l'ordinateur d'aller le plus vite possible dans la boucle de jeu (ce qui irait trop vite pour le joueur) on met en pause brièvement. mainClock.tick(FPS) assure que 40 tour de boucles sont effectués par seconde.


## Game Over



    
    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()


Quand le joueur perd, on arrive à la ligne 193 (on est alors sorti de la boucle depuis le break ligne 189). On joue alors le son gameover et on arrête la musique.

    
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()


On affiche ensuite le texte proposant de rejouer et on met l'écran à jour.

On entre ensuite en pause jusqu'à ce qu'il presse une touche ligne 200.

    
    gameOverSound.stop()


Selon le temps que le joueur aura mis à presser une touche, le son gameover peut ne pas être terminé. On arrête le son dès que la fonction waitForPlayerToPressKey() est terminée pour s'en assurer.


## Modifier le jeu Dodger


Voilà notre jeu graphique réalisé. Vous pouvez le trouver trop difficile ou trop facile... Mais il est simple de l'éditer pour changer ses paramètres. En effet il suffit de régler la vitesse dans les constantes initiales.

Par exemple, pour le ralentir, il suffit de passer FPS à 20 pour qu'il aille deux fois moins vite... Mais votre joueur aussi ira deux fois moins vite !
Si vous ne souhaitez que ralentir les méchants, changez leur vitesse maximale BADDIEMAXSPEED.

Trop facile ? Augmentez la vitesse minimale des baddie sans toucher au FPS. etc.

Moins de méchants, mais plus gros : augmentez le nombre de tours avant qu'un méchant n'apparaisse et leur taille minimale.


Le jeu restera essentiellement le même mais ses paramètres peuvent être adapté selon votre volonté.
