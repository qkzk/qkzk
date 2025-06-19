import os
from random import randint

import pgzrun


os.environ["SDL_VIDEO_CENTERED"] = "1"

TITLE = "Click to change color. Escape to quit"
WIDTH = 800
HEIGHT = 600


def color_to_hex(color: int) -> str:
    """Converti un entier représentant une couleur en sa notation hexa"""
    return f"#{color:>06x}".upper()


def random_color() -> int:
    """Renvoie une couleur RGB aléatoire sous forme d'entier"""
    color = randint(0, 0xFFFFFF)
    print(color_to_hex(color))
    return color


def random_color2() -> int:
    """La même chose mais un peu plus explicite. Ces deux fonctions sont équivalentes"""
    r = randint(0, 0xFF)
    g = randint(0, 0xFF)
    b = randint(0, 0xFF)
    color = (r << 16) + (g << 8) + b
    print(color_to_hex(color))
    return color


def update():
    """Quitte si on presse Q ou Escape"""
    checkkeys()


def draw():
    """Vide l'écran, colorie, écris la représentation de la couleur"""
    text_color = color_to_hex(color)
    screen.fill(text_color)
    draw_text_color(text_color)


def draw_text_color(text_color: str):
    """Ecris la couleur au format hexa au centre de l'écran"""
    screen.draw.text(
        text_color,
        center=(WIDTH // 2, HEIGHT // 2),
        color="white",
        ocolor="black",
        owidth=0.5,
        fontsize=64,
    )


def on_mouse_down():
    """Change la couleur quand on clique"""
    global color
    color = random_color()


def checkkeys():
    """Quitte si Q ou Escape sont pressées"""
    if keyboard[keys.Q] or keyboard[keys.ESCAPE]:
        exit()


color = random_color()

pgzrun.go()
