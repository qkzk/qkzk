TAILLE = 1024


def hacher(chaine: str) -> int:
    """Fonction de hachage simple mais lamentable"""
    total = 0
    for lettre in chaine:
        total ^= ord(lettre)
    return total % TAILLE


class DictSimple:
    """Table d'association utilisant une table de hachage bof bof. Ne gère pas les collisions"""

    def __init__(self):
        self.items = [None] * 1024
        self.__longueur = 0

    def set(self, cle: str, valeur):
        indice = hacher(cle)
        if self.items[indice] is None:
            self.__longueur += 1
        self.items[indice] = (cle, valeur)

    def __lire_interne(self, cle: str):
        indice = hacher(cle)
        items = self.items[indice]
        if items is None:
            raise KeyError(cle)
        return indice, items

    def get(self, cle: str):
        _, items = self.__lire_interne(cle)
        return items[1]

    def effacer(self, cle: str):
        indice, _ = self.__lire_interne(cle)
        self.items[indice] = None
        self.__longueur -= 1

    def longueur(self) -> int:
        return self.__longueur

    def __repr__(self) -> str:
        rep = "{"
        for indice in range(TAILLE):
            paire = self.items[indice]
            if paire is not None:
                cle, valeur = paire
                rep += f"({cle}, {valeur}), "
        rep = rep.rstrip(", ")
        rep += "}"
        return rep


def exemple():
    d = DictSimple()
    d.set("a", 1)
    d.set("b", 2)
    d.set("c", 3)
    assert d.get("a") == 1
    d.set("a", 4)
    assert d.get("a") == 4
    assert d.longueur() == 3
    d.effacer("b")
    assert d.longueur() == 2
    print(d)
    assert repr(d) == "{(a, 4), (c, 3)}"


exemple()
