from random import randint


def simuler_lancers(nb_lancers):
    nb_six = 0

    for i in range(nb_lancers):
        tirage = randint(1, 6)
        if tirage == 6:
            nb_six = nb_six + 1

    return nb_six / nb_lancers


print(simuler_lancers(1_000_000))  # s'approche de 1/6


from random import randint


def simuler_note():
    return randint(0, 20)


def creer_echantillon_note(taille):
    notes = []
    for i in range(taille):
        notes.append(simuler_note())

    return notes


print(creer_echantillon_note(10))

# copié depuis statsitiques.py
from math import sqrt


def calculer_moyenne(valeurs):
    somme = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val
        nb_valeurs = nb_valeurs + 1

    return somme / nb_valeurs


def calculer_ecart_type(valeurs):
    somme = 0
    somme_carres = 0
    nb_valeurs = 0

    for val in valeurs:
        somme = somme + val
        somme_carres = somme_carres + val**2
        nb_valeurs = nb_valeurs + 1

    return sqrt(somme_carres / nb_valeurs - (somme / nb_valeurs) ** 2)


from random import randint


def generer_tirages(nb_tirages):
    tirages = []
    for i in range(nb_tirages):
        lancer = randint(1, 6)
        tirages.append(lancer)
    return tirages


def calculer_effectifs(tirages):
    effectifs = [0, 0, 0, 0, 0, 0]
    for tirage in tirages:
        indice = tirage - 1
        effectifs[indice] = effectifs[indice] + 1
    return effectifs


def calculer_ecarts(effectifs):
    nb_tirages = sum(effectifs)
    proba = 1 / 6
    ecarts = []
    for effectif in effectifs:
        ecarts.append(effectif / nb_tirages - proba)
    return ecarts


def simuler_comparer():
    taille_simulation = [10, 100, 1000, 10_000, 100_000]
    for nb_tirages in taille_simulation:
        tirages = generer_tirages(nb_tirages)
        effectifs = calculer_effectifs(tirages)
        ecarts = calculer_ecarts(effectifs)
        moyenne = calculer_moyenne(tirages)
        ecart_type = calculer_ecart_type(tirages)
        print("\nsimulation...")
        print(nb_tirages, moyenne, ecart_type)
        print(effectifs)
        print(ecarts)


print("simuler et comparer")
simuler_comparer()
