def tri_select(tab: list) -> None:
    """
    Effectue un tri par sélection de tab.
    Modifie `tab` en place.
    Ne renvoie rien
    """
    for i in range(len(tab) - 1):
        mini = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[mini]:
                mini = j
        tab[i], tab[mini] = tab[mini], tab[i]


def tri_insertion(tab: list) -> None:
    """
    Effectue un tri par insertion de tab.
    Modifie `tab` en place.
    Ne renvoie rien.

    Version très peu efficace qui réalise beaucoup d'échanges inutiles.
    Sera améliorée en TP.
    """
    for i in range(len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j - 1]:
            tab[j], tab[j - 1] = tab[j - 1], tab[j]
            j -= 1


def tri_insertion_ameliore(tab: list) -> None:
    """
    Effectue un tri par insertion de tab.
    Modifie `tab` en place.
    Ne renvoie rien.

    Version très peu efficace qui réalise beaucoup d'échanges inutiles.
    Sera améliorée en TP.
    """
    for i in range(len(tab)):
        j = i
        val = tab[j]
        while j > 0 and val < tab[j - 1]:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = val


def tableau_aleatoire(taille: int, elem_max: int) -> list:
    """
    Renvoie un tableau aléatoire d'entiers entre 1 et `elem_max` inclu contenant `taille` éléments.
    """
    from random import randint

    return [randint(1, elem_max) for _ in range(taille)]


def est_trie(tab: list) -> bool:
    """Vrai ssi `tab` est trié par ordre croissant."""
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True


def test():
    """Teste les fonctions de tri."""

    assert est_trie([1])
    assert est_trie([])
    assert est_trie([1, 2, 3])
    assert not est_trie([3, 2, 1])
    assert not est_trie([3, 1, 2])

    tab = [3, 1, 5]
    tri_select(tab)
    assert est_trie(tab)

    for _ in range(100):
        tab = tableau_aleatoire(10, 10)
        tri_select(tab)
        assert est_trie(tab)

    tab = [3, 1, 5]
    tri_insertion(tab)
    assert est_trie(tab)

    for _ in range(100):
        tab = tableau_aleatoire(10, 10)
        tri_insertion(tab)
        assert est_trie(tab)

    tab = [3, 1, 5]
    tri_insertion_ameliore(tab)
    assert est_trie(tab)

    for _ in range(100):
        tab = tableau_aleatoire(10, 10)
        tri_insertion_ameliore(tab)
        assert est_trie(tab)


if __name__ == "__main__":
    test()
