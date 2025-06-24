def est_vide(arbre):
    return len(arbre) == 0


def etiquette(arbre):
    return arbre[0]


def gauche(arbre):
    return arbre[1]


def droite(arbre):
    return arbre[2]


def taille(arbre):
    if est_vide(arbre):
        return 0
    return 1 + taille(gauche(arbre)) + taille(droite(arbre))


def hauteur(arbre):
    if est_vide(arbre):
        return -1
    return 1 + max(hauteur(gauche(arbre)), hauteur(droite(arbre)))


def exemple():
    ab = (
        5,
        (1, (), (3, (), ())),
        (9, (7, (), ()), (11, (), ())),
    )

    assert not est_vide(ab)
    assert etiquette(ab) == 5
    assert etiquette(gauche(ab)) == 1
    assert est_vide(gauche(gauche(ab)))
    assert taille(ab) == 6
    assert hauteur(ab) == 2


exemple()
