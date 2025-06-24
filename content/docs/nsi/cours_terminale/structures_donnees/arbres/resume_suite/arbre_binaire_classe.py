class ArbreBinaire:
    def __init__(self, etiquette=None, gauche=None, droite=None):
        self.__etiquette = etiquette
        self.__gauche = gauche
        self.__droite = droite

    def est_vide(self) -> bool:
        return (
            self.__etiquette is None and self.__gauche is None and self.__droite is None
        )

    def etiquette(self):
        assert not self.est_vide(), "L'arbre vide n'a pas d'etiquette"
        return self.__etiquette

    def gauche(self):
        assert not self.est_vide(), "L'arbre vide n'a pas de sous arbre gauche"
        return self.__gauche

    def droite(self):
        assert not self.est_vide(), "L'arbre vide n'a pas de sous arbre droit"
        return self.__droite

    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.gauche().taille() + self.droite().taille()

    def hauteur(self):
        if self.est_vide():
            return -1
        return 1 + max(self.gauche().hauteur(), self.droite().hauteur())

    def parcours_largeur(self):
        file = [self]
        res = []
        while file:
            courant = file.pop(0)
            if not courant.est_vide():
                res.append(courant.etiquette())
                file.append(courant.gauche())
                file.append(courant.droite())

        return res

    def parcours_prefixe(self, res=None):
        if res is None:
            res = []
        if self.est_vide():
            return []
        res.append(self.etiquette())
        self.gauche().parcours_prefixe(res)
        self.droite().parcours_prefixe(res)
        return res

    def parcours_infixe(self, res=None):
        if res is None:
            res = []
        if self.est_vide():
            return []
        self.gauche().parcours_infixe(res)
        res.append(self.etiquette())
        self.droite().parcours_infixe(res)
        return res

    def parcours_suffixe(self, res=None):
        if res is None:
            res = []
        if self.est_vide():
            return []
        self.gauche().parcours_suffixe(res)
        self.droite().parcours_suffixe(res)
        res.append(self.etiquette())
        return res


def exemple():
    VIDE = ArbreBinaire()
    assert VIDE.est_vide()
    a = ArbreBinaire(
        5,
        ArbreBinaire(1, VIDE, ArbreBinaire(3, VIDE, VIDE)),
        ArbreBinaire(9, ArbreBinaire(7, VIDE, VIDE), ArbreBinaire(11, VIDE, VIDE)),
    )
    assert a.taille() == 6
    assert VIDE.hauteur() == -1
    assert a.hauteur() == 2
    assert a.parcours_largeur() == [5, 1, 9, 3, 7, 11]
    assert a.parcours_prefixe() == [5, 1, 3, 9, 7, 11]
    assert a.parcours_infixe() == [1, 3, 5, 7, 9, 11]
    assert a.parcours_suffixe() == [3, 1, 7, 11, 9, 5]


exemple()
