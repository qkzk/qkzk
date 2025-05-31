"""
Dans ce script on travaille avec une image comportant 10 lignes et 7 colonnes.

Plutôt que de la représenter par des listes imbriquées, on la représente par une seule list où les éléments sont bout à bout.

Il suffit d'une fonction, connaissant les dimensions du tableau, pour accéder aux éléments comme s'ils étaient représentés en ligne.
"""

# On note les dimensions en majuscule pour indiquer au lecteur que ce sont des constantes qui ne varient pas.
LARGEUR = 7
HAUTEUR = 10


def indice(ligne: int, colonne: int):
    """calcule l'indice d'un pixel situé en ligne colonne dans un tableau"""
    return LARGEUR * ligne + colonne


def print_table(tableau: list) -> None:
    """Affiche les éléments de tableau en plusieurs lignes"""
    for ligne in range(HAUTEUR):
        for colonne in range(LARGEUR):
            print(tableau[indice(ligne, colonne)], end=" ")
        print()


def print_table2(tableau: list) -> None:
    """Affiche les éléments de tableau en plusieurs lignes avec des coordonnées autour"""
    print("    ", end="")
    for colonne in range(LARGEUR):
        print(f"{colonne} ", end=" ")
    print()
    for ligne in range(HAUTEUR):
        print(ligne, end="   ")
        for colonne in range(LARGEUR):
            print(f"{tableau[indice(ligne, colonne)]:2>}", end="  ")
        print()


def exemple():
    ascii_table = [chr(32 + i) for i in range(70)]
    print_table(ascii_table)
    print_table2(ascii_table)


exemple()
