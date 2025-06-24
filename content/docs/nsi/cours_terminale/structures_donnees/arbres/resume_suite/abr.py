class ABR:
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

    def contient(self, val) -> bool:
        if self.est_vide():
            return False
        e = self.etiquette()
        if e == val:
            return True
        elif e > val:
            return self.gauche().contient(val)
        else:
            return self.droite().contient(val)

    def inserer(self, val):
        if self.est_vide():
            self.__etiquette = val
            self.__gauche = ABR()
            self.__droite = ABR()
        elif self.etiquette() >= val:
            self.gauche().inserer(val)
        else:
            self.droite().inserer(val)

    def est_abr(self) -> bool:
        return est_trie(self.parcours_infixe())

    def plus_petit(self):
        if self.est_vide():
            raise ValueError("L'arbre vide n'a pas de plus petit élément")
        if self.gauche().est_vide():
            return self.etiquette()
        return self.gauche().plus_petit()


def est_trie(tab: list) -> bool:
    if len(tab) == 0:
        return True
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True


def exemple():
    VIDE = ABR()
    assert VIDE.est_vide()
    assert VIDE.hauteur() == -1
    assert VIDE.taille() == 0

    a = ABR(
        5,
        ABR(1, ABR(), ABR(3, ABR(), ABR())),
        ABR(9, ABR(7, ABR(), ABR()), ABR(11, ABR(), ABR())),
    )
    assert a.taille() == 6
    assert a.hauteur() == 2

    assert a.parcours_largeur() == [5, 1, 9, 3, 7, 11]
    assert a.parcours_prefixe() == [5, 1, 3, 9, 7, 11]
    assert a.parcours_infixe() == [1, 3, 5, 7, 9, 11]
    assert a.parcours_suffixe() == [3, 1, 7, 11, 9, 5]

    assert a.est_abr()

    for val in [1, 3, 5, 7, 9, 11]:
        assert a.contient(val)
    for val in [0, 2, 4, 6, 8, 10, 12]:
        assert not a.contient(val)

    a.inserer(0)
    assert a.contient(0)
    assert a.taille() == 7
    assert a.est_abr()

    a.inserer(4)
    assert a.contient(4)
    assert a.taille() == 8
    assert a.est_abr()


exemple()
