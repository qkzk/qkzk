import random

from PIL import Image, ImageDraw

Pixel = tuple[int, int]

# Couleurs pastel prédéfinies
PASTEL_COLORS = [
    (255, 179, 186),  # rose pastel
    (186, 255, 201),  # vert pastel
    (186, 225, 255),  # bleu pastel
    (255, 255, 186),  # jaune pastel
]


def generate_colored_blocks(n: int) -> Image.Image:
    """
    Génère une image carrée de taille n x n remplie de gros carrés de couleur pastel.

    L'image est divisée en une grille de gros blocs (entre 3 et 6 par ligne),
    chaque bloc étant coloré aléatoirement parmi 4 couleurs pastel.
    """
    # Crée une image blanche
    img = Image.new("RGB", (n, n), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Choisit aléatoirement une taille de grille (3 à 6 blocs par ligne)
    grid_size = random.randint(3, 6)
    block_size = n // grid_size

    for row in range(grid_size):
        for col in range(grid_size):
            color = random.choice(PASTEL_COLORS)
            x0 = col * block_size
            y0 = row * block_size
            x1 = x0 + block_size
            y1 = y0 + block_size
            draw.rectangle([x0, y0, x1, y1], fill=color)

    return img


def echange2pix(img: Image.Image, pixel1: Pixel, pixel2: Pixel) -> None:
    """Echange les pixels"""
    couleur0 = img.getpixel(pixel1)
    couleur1 = img.getpixel(pixel2)
    img.putpixel(pixel1, couleur1)
    img.putpixel(pixel2, couleur0)


def rotation4pix(
    img: Image.Image, pixel0: Pixel, pixel1: Pixel, pixel2: Pixel, pixel3: Pixel
) -> None:
    """Rotation d'un quart de tour de 4 pixels"""
    echange2pix(img, pixel0, pixel1)
    echange2pix(img, pixel1, pixel2)
    echange2pix(img, pixel2, pixel3)


def rotation_quart_simple(img: Image.Image) -> None:
    """Rotation itérative d'un quart de tour"""
    assert img.size[0] == img.size[1]
    n = img.size[0]
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            ri = (n - 1) - i
            rj = (n - 1) - j
            rotation4pix(img, (i, j), (rj, i), (ri, rj), (j, ri))


def echange_quadrant(
    img: Image.Image, pixel0: Pixel, pixel1: Pixel, width: int
) -> None:
    x0, y0 = pixel0
    x1, y1 = pixel1
    for i in range(width):
        for j in range(width):
            echange2pix(img, (x0 + i, y0 + j), (x1 + i, y1 + j))


def rotation_quart_rec_inner(img: Image.Image, pixel: Pixel, width: int) -> None:
    """Fonction récursive utilisée en interne pour tourner une image d'un quart de tour."""
    if width <= 1:
        return
    x, y = pixel
    n = width // 2
    # fmt:off
    rotation_quart_rec_inner(img, (x,         y), n)
    rotation_quart_rec_inner(img, (x + n,     y), n)
    rotation_quart_rec_inner(img, (x + n, y + n), n)
    rotation_quart_rec_inner(img, (x,     y + n), n)
    echange_quadrant(img, (x,         y), (x + n,     y), n)
    echange_quadrant(img, (x + n,     y), (x + n, y + n), n)
    echange_quadrant(img, (x + n, y + n), (x,     y + n), n)
    # fmt:on


def rotation_quart_rec(img: Image.Image) -> None:
    """Rotation récursive utilisant diviser pour régner."""
    assert img.size[0] == img.size[1]
    rotation_quart_rec_inner(img, (0, 0), img.size[0])


def generate():
    """Génère une image aléatoire et carré, de taille 400px, sauvagardée dans 'pastel_blocks.png'"""
    img = generate_colored_blocks(400)
    img.show()
    img.save("pastel_blocks.png")


def exemple():
    # generate()

    img = Image.open("pastel_blocks.png")
    img.show("Original")

    from time import time

    start = time()
    rotation_quart_simple(img)
    end = time()
    print(f"rotation simple. Taille {img.size} durée {end - start:.3f} secondes")
    img.show("Rotation simple")

    img = Image.open("pastel_blocks.png")
    start = time()
    rotation_quart_rec(img)
    end = time()
    img.show("Rotation recursive")
    print(f"rotation rec. Taille {img.size} durée {end - start:.3f} secondes")
    # vraiment nul, c'est bcp plus long (0.252s vs 1.682s)


if __name__ == "__main__":
    exemple()
