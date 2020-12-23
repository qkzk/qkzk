#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'qkzk'
__date_creation__ = '2020/04/24'
__doc__ = """
:mod:`parcours` module
:author: {:s}
:creation date: {:s}
:last revision:


Implémente et teste les parcours en largeur, prefixe, infixe, suffixe
sur la classe BinaryTree
""".format(__author__, __date_creation__)


import binary_tree as bt

VIDE = bt.BinaryTree()


def feuille(data):
    return bt.BinaryTree(data, VIDE, VIDE)


def parcours_largeur(arbre):
    '''
    Retourne les sommets d'un arbre binaire parcouru en largeur
    @param arbre: (BinaryTree)
    @return: (list) les feuilles, parcourues dans largeur.
    '''
    fifo = []
    visites = []
    fifo.append(arbre)

    while fifo != []:
        arbre = fifo.pop(0)
        if not arbre.is_empty():
            visites.append(arbre.get_data())
            fifo += [arbre.get_left_subtree(), arbre.get_right_subtree()]
    return visites


def parcours_profondeur(arbre, ordre="prefixe"):
    '''
    Retourne les sommets d'un arbres binaires parcouru en profondeur
    dans un ordre particulier
    @param arbre: (BinaryTree)
    @keyword ordre: (str) parmi (prefixe, infixe, suffixe)
    @return: (list) les sommets dans l'ordre visité
    '''
    procedures = {
        "prefixe": parcourir_prefixe,
        "infixe": parcourir_infixe,
        "suffixe": parcourir_suffixe,
    }
    procedure = procedures[ordre]
    visites = []
    procedure(arbre, visites=visites)
    return visites


def parcourir_prefixe(arbre, visites):
    '''
    Procédure qui modifie le tableau visites transmis.
    Le remplit avec les sommets dans l'ordre prefixe
    Récursive, elle s'appelle deux fois (pour chaque fils)

    @param arbre: (BinaryTree)
    @SE: modifie le tableau visites
    '''
    if not arbre.is_empty():
        visites.append(arbre.get_data())
        if not arbre.get_left_subtree().is_empty():
            parcourir_prefixe(arbre.get_left_subtree(), visites)
        if not arbre.get_right_subtree().is_empty():
            parcourir_prefixe(arbre.get_right_subtree(), visites)


def parcourir_infixe(arbre, visites):
    '''
    Procédure qui modifie le tableau visites transmis.
    Le remplit avec les sommets dans l'ordre infixe
    Récursive, elle s'appelle deux fois (pour chaque fils)

    @param arbre: (BinaryTree)
    @SE: modifie le tableau visites
    '''
    if not arbre.is_empty():
        if not arbre.get_left_subtree().is_empty():
            parcourir_infixe(arbre.get_left_subtree(), visites)
        visites.append(arbre.get_data())
        if not arbre.get_right_subtree().is_empty():
            parcourir_infixe(arbre.get_right_subtree(), visites)


def parcourir_suffixe(arbre, visites):
    '''
    Procédure qui modifie le tableau visites transmis.
    Le remplit avec les sommets dans l'ordre suffixe
    Récursive, elle s'appelle deux fois (pour chaque fils)

    @param arbre: (BinaryTree)
    @SE: modifie le tableau visites
    '''
    if not arbre.is_empty():
        if not arbre.get_left_subtree().is_empty():
            parcourir_suffixe(arbre.get_left_subtree(), visites)
        if not arbre.get_right_subtree().is_empty():
            parcourir_suffixe(arbre.get_right_subtree(), visites)
        visites.append(arbre.get_data())


def profondeur_pile(arbre):
    '''
    Retourne les sommets d'un arbre binaire parcouru en profondeur

    N'utilise pas de récursion mais simplement une pile
    Attention, on ajoute d'abord le fils droit, ensuite le gauche.
    On obtient un parcours prefixe.

    @param arbre: (BinaryTree)
    @return: (list) les feuilles, parcourues dans l'ordre prefixe.
    '''
    lifo = []
    visites = []
    lifo.append(arbre)

    while lifo != []:
        arbre = lifo.pop()
        if not arbre.is_empty():
            visites.append(arbre.get_data())
            lifo += [arbre.get_right_subtree(), arbre.get_left_subtree(), ]
    return visites


def infixe(arbre):
    '''
    Réalise un parcours infixe de l'arbre.
    N'utilise pas de procédure externe. On ajoute simplement les listes
    produites dans un certain ordre.
    L'algorithme est récursif.

    @param arbre: (BinaryTree)
    @return: (list) Les étiquettes, dans l'ordre demandé
    '''
    if arbre.is_empty():
        return []
    return infixe(arbre.get_left_subtree()) + \
        [arbre.get_data()] + \
        infixe(arbre.get_right_subtree())


def prefixe(arbre):
    '''
    Réalise un parcours prefixe de l'arbre.
    N'utilise pas de procédure externe. On ajoute simplement les listes
    produites dans un certain ordre.
    L'algorithme est récursif.

    @param arbre: (BinaryTree)
    @return: (list) Les étiquettes, dans l'ordre demandé
    '''
    if arbre.is_empty():
        return []
    return [arbre.get_data()] + \
        prefixe(arbre.get_left_subtree()) + \
        prefixe(arbre.get_right_subtree())


def suffixe(arbre):
    '''
    Réalise un parcours suffixe de l'arbre.
    N'utilise pas de procédure externe. On ajoute simplement les listes
    produites dans un certain ordre.
    L'algorithme est récursif.

    @param arbre: (BinaryTree)
    @return: (list) Les étiquettes, dans l'ordre demandé
    '''
    if arbre.is_empty():
        return []
    return suffixe(arbre.get_left_subtree()) + \
        suffixe(arbre.get_right_subtree()) + \
        [arbre.get_data()]


def tester_tlm():
    arbre_abcdefg = bt.BinaryTree(
        "a",
        bt.BinaryTree(
            "b",
            feuille("d"),
            feuille("e"),
        ),
        bt.BinaryTree(
            "c",
            feuille("f"),
            feuille("g")
        )
    )
    # arbre_abcdefg.show()

    # parcours largeur
    visites = parcours_largeur(arbre_abcdefg)
    assert visites == list('abcdefg')
    assert parcours_largeur(VIDE) == []

    # parcours en profondeur
    assert parcours_profondeur(arbre_abcdefg,
                               ordre="prefixe") == list('abdecfg')

    assert parcours_profondeur(arbre_abcdefg,
                               ordre="infixe") == list('dbeafcg')

    assert parcours_profondeur(arbre_abcdefg,
                               ordre="suffixe") == list('debfgca')

    # profondeur pile
    assert profondeur_pile(arbre_abcdefg) == list('abdecfg')

    # prefixe, infixe, suffixe
    assert prefixe(arbre_abcdefg) == list('abdecfg')
    assert infixe(arbre_abcdefg) == list('dbeafcg')
    assert suffixe(arbre_abcdefg) == list('debfgca')


if __name__ == '__main__':
    tester_tlm()
