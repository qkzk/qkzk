def moyenne(valeurs):
    somme = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val
        nb_valeurs = nb_valeurs + 1

    return somme / nb_valeurs


print(moyenne([1, 2, 3]))  # renvoie 2.0


from math import sqrt


def ecart_type(valeurs):
    somme = 0
    somme_carres = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val
        somme_carres = somme_carres + val**2
        nb_valeurs = nb_valeurs + 1

    return sqrt(somme_carres / nb_valeurs - (somme / nb_valeurs) ** 2)


print(ecart_type([1, 2, 3]))  # 0.82


def proportion_dans_ab(valeurs, a, b):
    nb_dans_intervalle = 0
    nb_total = 0

    for val in valeurs:
        if a <= val and val <= b:
            nb_dans_intervalle = nb_dans_intervalle + 1
        nb_total = nb_total + 1
    return nb_dans_intervalle / nb_total


print(proportion_dans_ab([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2.5, 7.5))  # 0.5
