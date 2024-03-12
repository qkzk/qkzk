'''
Implantation des dictionnaires en utilisant une table de hachage.

Objectif : accès aux valeurs en temps constant

On se limitera (pour l'instant) à 1024 éléments
'''


class DictionnaireHash:
    '''Implantation des dictionnaires utilisant une table de hachage'''

    TAILLE_MAX = 1024

    def __init__(self, collection=None):
        self.__cles_valeurs = [None] * self.TAILLE_MAX
        self.__longueur = 0
        if collection is not None:
            for cle, valeur in collection:
                self[cle] = valeur

    def __calculer_indice(self, cle):
        '''calcule l'indice d'un élément dans la liste `__cles_valeurs`'''
        return hash(cle) % self.TAILLE_MAX

    def est_vide(self):
        '''prédicat vrai ssi le dictionnaire est vide'''
        return len(self) == 0

    def __setitem__(self, cle, valeur):
        '''permet d'ajouter un élément avec 'd[cle] = valeur' '''
        indice = self.__calculer_indice(cle)
        self.__cles_valeurs[indice] = (cle, valeur)
        self.__longueur += 1

    def __getitem__(self, cle):
        '''permet d'accéder à un élément avec 'd[cle]' -> 'valeur' '''
        indice = self.__calculer_indice(cle)
        contenu = self.__cles_valeurs[indice]
        if contenu is not None:
            return contenu[1]
        raise KeyError(cle)

    def __repr__(self) -> str:
        '''renvoie une chaîne présentant le dictionnaire'''
        if self.est_vide():
            return 'DictionnaireHash()'
        elems = tuple((elt for elt in self.__cles_valeurs if elt is not None))
        return f'DictionnaireHash({elems})'

    def __iter__(self):
        '''permet d'itérer avec 'for cle in d' '''
        for elt in self.__cles_valeurs:
            if elt is not None:
                yield elt[0]

    def __delitem__(self, cle_recherchee):
        '''permet d'effacer une paire avec 'del d[cle] ' '''
        if self[cle_recherchee] is not None:
            indice = self.__calculer_indice(cle_recherchee)
            self.__cles_valeurs[indice] = None
            self.__longueur -= 1

    def values(self):
        '''renvoie un iterateur des valeurs'''
        return (elt[1] for elt in self.__cles_valeurs if elt is not None)

    def keys(self):
        '''renvoie un itérateur des clé'''
        return (elt[0] for elt in self.__cles_valeurs if elt is not None)

    def items(self):
        '''renvoie un itérateur des couples (clé, valeur)'''
        return (elt for elt in self.__cles_valeurs if elt is not None)

    def clear(self):
        '''vide le dictionnaire'''
        self.__longueur = 0
        self.__cles_valeurs = [None] * 1024

    def copy(self):
        '''retourne une copie du dictionnaire'''
        items = [elt for elt in self.__cles_valeurs if elt is not None]
        return DictionnaireHash(items)

    def get(self, cle):
        '''retourne la valeur de la clé si elle est contenue, None sinon'''
        return self[cle] if cle in self else None

    def __len__(self) -> int:
        '''renvoie la longueur du dictionnaire avec 'len(d)' '''
        return self.__longueur


def tester():
    d = DictionnaireHash()
    assert len(d) == 0
    d[1] = 2
    assert len(d) == 1
    assert d[1] == 2
    e = DictionnaireHash(((1, 2), (3, 4)))
    assert e[1] == 2
    assert e[3] == 4
    assert repr(e) == 'DictionnaireHash(((1, 2), (3, 4)))'
    assert len(e) == 2
    assert [(k, e[k]) for k in e] == [(1, 2), (3, 4)]
    assert [v for v in e.values()] == [2, 4]
    assert 1 in d
    del d[1]
    assert 1 not in d
    e.clear()
    assert len(e) == 0
    e = DictionnaireHash(((1, 2), (3, 4)))
    f = e.copy()
    assert repr(f) == 'DictionnaireHash(((1, 2), (3, 4)))'
    e[1] = 5
    assert repr(e) == 'DictionnaireHash(((1, 5), (3, 4)))'
    assert e.get(7) is None


if __name__ == "__main__":
    tester()
