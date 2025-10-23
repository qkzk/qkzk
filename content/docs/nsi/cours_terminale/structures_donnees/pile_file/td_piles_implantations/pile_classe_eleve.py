from typing import Any


class Pile:
    """Classe modélisant une pile"""

    def __init__(self):
        pass

    def empiler(self, elt: Any) -> None:
        """Ajoute elt à la pile"""
        pass

    def depiler(self) -> Any:
        """
        Retire et renvoie le sommet de la pile.
        Plante si la pile est vide.
        """
        pass

    def est_vide(self) -> bool:
        """Vrai ssi la pile est vide"""
        pass

    def longueur(self) -> int:
        """Le nombre d'éléments de la pile"""
        pass

    def sommet(self) -> Any:
        """
        Permet de consulter le sommet de la pile.
        Ne modifie pas son contenu.
        Plante si la pile est vide.
        """
        pass

    def __repr__(self) -> str:
        pass


def test():
    pile = Pile()
    assert pile.est_vide()
    pile.empiler(5)
    assert not pile.est_vide()
    pile.empiler(1)
    pile.empiler(3)
    pile.empiler(7)
    assert pile.longueur() == 4
    assert pile.depiler() == 7
    pile.empiler(9)
    assert pile.depiler() == 9
    assert pile.depiler() == 3
    assert pile.depiler() == 1
    assert pile.depiler() == 5
    assert pile.est_vide()


if __name__ == "__main__":
    test()
