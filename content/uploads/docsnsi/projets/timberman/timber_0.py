###############################################################################
####################            IMPORTS                      ##################
###############################################################################

# pygame# librairie standard de python
from random import choice

import pygame
from pygame.locals import *


###############################################################################
####################            CONSTANTES                   ##################
###############################################################################

FENETRE_HAUTEUR = 600
FENETRE_LARGEUR = 600
FPS = 40  # 40 images par secondes

# couleurs
TEXTE_COULEUR = (255, 255, 255)  # blanc
FOND_COULEUR = (0, 0, 0)  # noir
OBJETS_COULEUR = (255, 127, 0)  # orangé
TIMBER_COULEUR = (0, 128, 255)  # bleu ciel

# constantes du bucheron
TIMBER_LARGEUR = 50
TIMBER_HAUTEUR = 60
TIMBER_GAUCHE = 0.5 * FENETRE_LARGEUR - 100
TIMBER_DROITE = 0.5 * FENETRE_LARGEUR + 100 - TIMBER_LARGEUR

# constantes des arbres
TRONC_LARGEUR = 50
TRONC_ABS = 0.5 * (FENETRE_LARGEUR - TRONC_LARGEUR)
TRONC_ORD = 0

BRANCHE_LARGEUR = 100
BRANCHE_HAUTEUR = 20
BRANCHE_DEPLACEMENT = 60

# l'abscisse de gauche des branches est de 175
BRANCHE_GAUCHE_ABS = 0.5*(FENETRE_LARGEUR - TRONC_LARGEUR) - BRANCHE_LARGEUR
# l'abscisse de droite des branches est de 325
BRANCHE_DROITE_ABS = 0.5*(FENETRE_LARGEUR + TRONC_LARGEUR)

# écoulement du temps
TEMPS_MAX = 5000  # 5 secondes
TEMPS_BONUS = 300  # 0.3 secondes
TEMPS_TICK = 0.3 * TEMPS_MAX / FPS

# données du chronomètre à l'écran
CHRONO_ABS = 350
CHRONO_ORD = 50
CHRONO_HAUTEUR = 25
CHRONO_LARGEUR = 150


################################################################################
#########################  DEBUT DU TRAVAIL             ########################
################################################################################


###############################################################################
####################            FONCTIONS                    ##################
###############################################################################


def drawText(text, font, surface, x, y):
    '''
    Ecrit du texte à l'écran
    @param text: (str)
    @param font: (pygame.font)
    @param surface: (pygame.surface)
    @param x: (int) l'abscisse du coin supérieur gauche de la zone de texte
    @param y: (int) l'ordonnée du coin supérieur gauche de la zone de texte
    @return: (None)
    SE: écrit à l'écran
    '''
    # donnée complétement

    # permet d'ecrire
    textobj = font.render(text, 1, TEXTE_COULEUR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def chrono_dessiner(chrono, surface):
    '''dessine la barre du chronomètre à l'écran.
    Sa largeur est proportionnelle à la durée.

    @param chrono : (int) la durée à de la barre. Elle va représenter la durée
        totale
    @param surface : la fenêtre sur laquelle on écrit
    @return: (None)
    SE: dessine à l'écran
    '''

    # à écrire

    # calculer la largeur
    # créer l'objet rect du chrono
    # dessiner le chrono avec pygame.draw.rect
    pass


def timber_deplacer(direction):
    '''
    Retourne la nouvelle position et le nouvel objet rect du bucheron
    @param direction: (str) "gauche" ou "droite"
    @return : (Tuple (int, pygame.rect)) nouvelle position du bucheron
    '''

    # à compléter

    # nouvelle position selon qu'il aille à gauche ou droite
    timber_x = TIMBER_GAUCHE
    # on cree le rect du timber
    timber_rect = pygame.Rect(timber_x,
                              timber_y,
                              TIMBER_LARGEUR,
                              TIMBER_HAUTEUR)
    return timber_x, timber_rect


def timber_collision(timber_vivant):
    '''
    Détecte et réagit aux collisions entre le bucheron et les branches.
    Le bucheron ne peut toucher que la branche la plus basse
    Il gagne du temps s'il tape une branche
    On renvoit aussi une variable disant qu'il est vivant ou mort

    @param timber_vivant: (bool)
    @return : (bool) le score et l'état vivant/mort
    '''
    # à écrire
    timber_vivant = True
    # detection d'une collision
    # on ne peut toucher que la plus basse, inutile de lire les autres
    # on utilise la méthode colliderect entre de l'objet timber_rect
    # s'il y a collision, timber_vivant devient False
    return timber_vivant


def timber_bonus_temps(timber_chrono):
    '''
    Ajoute un bonus au temps en le limitant au maximum
    @param timber_chrono: (int)
    @return: (int)
    '''
    # à écrire
    # le chrono doit augmenter de la valeur bonus à chaque déplacement.
    # il ne peut dépasser TEMPS_MAX
    timber_chrono = TEMPS_MAX
    return timber_chrono


def timber_diminuer_chrono(timber_chrono, timber_vivant):
    '''
    Met à jour le chronomètre, il diminue d'un à chaque miliseconde.
    Le "temps" du jeu n'avance que 40 fois par seconde, on diminue le score
    de cette valeur
    Si le temps est écoulé, on tue le bucheron
    @param timber_chrono: (int) le temps restant
    @param timber_vivant: (bool)
    @return: (tuple (int, bool)) les nouveaux états
    '''
    # Donnée complètement
    # update le temps
    timber_chrono -= TEMPS_TICK
    if timber_chrono <= 0:
        # print("game over")
        timber_vivant = False
    return timber_chrono, timber_vivant


def arbre_dessiner():
    '''
    Dessine le tronc et les branches
    On parcourt le tableau des branches qu'on dessine une par une
    @return : (None)
    SE : dessine à l'écran
    '''
    # donnée complètement

    pygame.draw.rect(fenetre, OBJETS_COULEUR, tronc_rect)
    for branche in branches:
        # il serait plus pratique de les garder en mémoire et de les mettre
        # à jour
        branche_rect = pygame.Rect(branche[0],
                                   branche[1],
                                   BRANCHE_LARGEUR,
                                   BRANCHE_HAUTEUR)
        pygame.draw.rect(fenetre, OBJETS_COULEUR, branche_rect)


def arbre_deplacer(branche):
    '''
    Déplace les branche vers le bas
    Si la branche basse est sortie, on l'enlève et on ajoute une nouvelle
    en haut

    @param branche: (list) la liste des branches à l'écran
    @return: (list) la nouvelle liste des branches
    '''
    # partie à écrire :
    # toutes les branches doivent descendre d'un pas

    # la suite est complète, plus rien à faire ici
    if branches[0][1] >= FENETRE_HAUTEUR:
        # on enlève la branche sortie de l'écran
        branches.pop(0)
        # on choisit au hasard la nouvelle position de la branche
        nlle_abs = choice((BRANCHE_GAUCHE_ABS, BRANCHE_DROITE_ABS))
        branche = [nlle_abs, 0]
        branches.append(branche)
    # pour développer on affiche les branches
    print(branches)
    return branches


################################################################################
#########################  FIN DU TRAVAIL               ########################
################################################################################


# toute la suite est complète


################################################################################
#########################  INITIALISATION DU JEU        ########################
################################################################################
# arbre
tronc_rect = pygame.Rect(TRONC_ABS, TRONC_ORD, TRONC_LARGEUR, FENETRE_HAUTEUR)

branches = [[BRANCHE_DROITE_ABS, 0.66 * FENETRE_HAUTEUR],
            [BRANCHE_GAUCHE_ABS, 0.33 * FENETRE_HAUTEUR],
            [BRANCHE_DROITE_ABS, 0]]

##############################################################################
# timber

timber_x = TIMBER_GAUCHE  # position de gauche
timber_y = FENETRE_HAUTEUR - TIMBER_HAUTEUR  # il est pose au sol
timber_rect = pygame.Rect(timber_x, timber_y, TIMBER_LARGEUR,
                          TIMBER_HAUTEUR)  # le rect associe a timber
timber_chrono = TEMPS_MAX
timber_vivant = True
timber_a_tape = False
timber_score = 0

##############################################################################
# pygame

pygame.init()
pygame_clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((FENETRE_LARGEUR, FENETRE_HAUTEUR))
pygame.display.set_caption('Timber')

# taille et type de la fonte
font = pygame.font.SysFont(None, 48)

# on update une première fois pour afficher tous les éléments
pygame.display.update()

##############################################################################
# boucle infinie
while True:
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            elif event.key == K_LEFT:
                timber_x, timber_rect = timber_deplacer("gauche")
                timber_a_tape = True
                print("gauche")

            elif event.key == K_RIGHT:
                timber_x, timber_rect = timber_deplacer("droite")
                timber_a_tape = True
                print("droite")

    # Dessins
    # On remplit le fond
    fenetre.fill(FOND_COULEUR)

    # On dessine les scores
    drawText(str(timber_score),
             font,
             fenetre,
             0.15 * FENETRE_LARGEUR,
             0.1 * FENETRE_HAUTEUR)

    pygame.draw.rect(fenetre, OBJETS_COULEUR, tronc_rect)
    for branche in branches:
        branche_rect = pygame.Rect(branche[0],
                                   branche[1],
                                   BRANCHE_LARGEUR,
                                   BRANCHE_HAUTEUR)

        pygame.draw.rect(fenetre, OBJETS_COULEUR, branche_rect)
    pygame.draw.rect(fenetre, TIMBER_COULEUR, timber_rect)
    chrono_dessiner(timber_chrono, fenetre)

    # update
    timber_score += 1  #  augmente les scores
    if timber_a_tape:
        branches = arbre_deplacer(branches)  # fait descendre les branches
        timber_vivant = timber_collision(timber_vivant)
        timber_chrono = timber_bonus_temps(timber_chrono)
        # pour le tour suivant, la variable doit redevenir fausse
        timber_a_tape = False

    timber_chrono, timber_vivant = timber_diminuer_chrono(timber_chrono,
                                                          timber_vivant)
    if not timber_vivant:
        # si timber est mort, on arrête la boucle infinie
        break

    # pygame : tick, update
    pygame.display.update()
    pygame_clock.tick(FPS)

##############################################################################
# SORTIE DU JEU
# on arrive ici seulement si timber meurt...
fenetre.fill(FOND_COULEUR)
drawText(f'GAME OVER - {timber_score} points', font, fenetre,
         0.2 * FENETRE_LARGEUR, 0.3 * FENETRE_HAUTEUR)
pygame_clock.tick()
pygame.display.update()
print('GAME OVER')
print(f'Score : {timber_score}')
pygame.quit()
