from typing import Any


def creer_vide() -> list:
    """Renvoie une pile vide"""


def empiler(pile, elt: Any) -> None:
    """Ajoute elt à la pile"""


def depiler(pile) -> Any:
    """
    Retire et renvoie le sommet de la pile.
    Plante si la pile est vide.
    """


def est_vide(pile) -> bool:
    """Vrai ssi la pile est vide"""


def longueur(pile) -> int:
    """Le nombre d'éléments de la pile"""


def sommet(pile) -> Any:
    """
    Permet de consulter le sommet de la pile.
    Ne modifie pas son contenu.
    Plante si la pile est vide.
    """


def test():
    pile = creer_vide()
    assert est_vide(pile)
    empiler(pile, 5)
    assert not est_vide(
        pile,
    )
    empiler(pile, 1)
    empiler(pile, 3)
    empiler(pile, 7)
    assert longueur(pile) == 4
    assert depiler(pile) == 7
    empiler(pile, 9)
    assert depiler(pile) == 9
    assert depiler(pile) == 3
    assert depiler(pile) == 1
    assert depiler(pile) == 5
    assert est_vide(pile)


if __name__ == "__main__":
    test()
