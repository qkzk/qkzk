"""
Simple jeu du morpion dans l'interpréteur Python.

Plus ou moins conforme au milieu d'année de première NSI. Pas trop de fioritures.

à exécuter avec : `python -i morpion.py`
"""


def jouer(morpion: list, ligne: int, colonne: int, symbole: str) -> bool:
    """
    Tente de jouer le symbole dans la case en question.
    Ne vérifie pas la validité de ligne, colonne et symbole.
    Suppose que l'utilisateur ne commet jamais d'erreur.

    Renvoie Vrai si le coup a pu être joué.
    """
    if morpion[ligne][colonne] == " ":
        morpion[ligne][colonne] = symbole
        return True
    return False


def ligne_gagnante(morpion: list, ligne: int) -> bool:
    """
    Vrai si et seulement si la ligne contient trois x ou trois o.
    Ne vérifie pas la validité de l'indice de ligne
    """
    if (
        morpion[ligne][0] == morpion[ligne][1] == morpion[ligne][2] == "x"
        or morpion[ligne][0] == morpion[ligne][1] == morpion[ligne][2] == "o"
    ):
        return True
    return False


def colonne_gagnante(morpion: list, colonne: int) -> bool:
    """
    Vrai si et seulement si la colonne contient trois x ou trois o.
    Ne vérifie pas la validité de l'indice de colonne
    """
    if (
        morpion[0][colonne] == morpion[1][colonne] == morpion[2][colonne] == "x"
        or morpion[0][colonne] == morpion[1][colonne] == morpion[2][colonne] == "o"
    ):
        return True
    return False


def diagonale_gagnante(morpion: list) -> bool:
    """
    Vrai si et seulement si l'une des diagonales contient trois x ou trois o.
    Ne vérifie pas la validité de l'indice de colonne
    """
    if (
        morpion[0][0] == morpion[1][1] == morpion[2][2] == "x"
        or morpion[0][0] == morpion[1][1] == morpion[2][2] == "o"
        or morpion[0][2] == morpion[1][1] == morpion[2][0] == "x"
        or morpion[0][2] == morpion[1][1] == morpion[2][0] == "o"
    ):
        return True
    return False


def est_gagnant(morpion) -> bool:
    """Vrai si et seulement la partie est gagnée."""
    for ligne in range(3):
        if ligne_gagnante(morpion, ligne):
            return True
    for colonne in range(3):
        if colonne_gagnante(morpion, colonne):
            return True
    if diagonale_gagnante(morpion):
        return True
    return False


def est_match_nul(morpion: list) -> bool:
    """Vrai si et seulement si aucune case n'est libre."""
    for ligne in range(3):
        for colonne in range(3):
            if morpion[ligne][colonne] == " ":
                return False
    return True


def est_termine(morpion: list) -> bool:
    """Vrai ssi la partie est gagnée ou est nulle."""
    return est_gagnant(morpion) or est_match_nul(morpion)


def afficher(morpion):
    """Affiche très simplement la grille dans la console"""
    print("-------")
    for ligne in morpion:
        print("|", end="")
        for symbole in ligne:
            print(symbole, end="|")
        print("\n-------")


def jouer_morpion() -> None:
    """
    Déroule une partie de morpion a deux joueurs dans l'interpréteur.
    S'arrête lorsque la partie est terminée.
    """
    morpion = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    joueur = "x"
    adversaire = "o"

    while not est_termine(morpion):
        print("Joueur: ", joueur)
        afficher(morpion)
        ligne = int(input("ligne ? : "))
        colonne = int(input("colonne ? : "))
        if jouer(morpion, ligne, colonne, joueur):
            if est_gagnant(morpion):
                afficher(morpion)
                print(joueur, "a gagné !")
            joueur, adversaire = adversaire, joueur
