"""
title: planification des taĉhes
author: chatGPT & qkzk
date: 2023/02/23


Résolution gloutonne et exhaustive du problème de planification des tâches.

Dans tout le script les tâches sont représentées par des tuples, et une liste 
est fournie.

Par exemple :

taches = [
    ("A", 9.5, 10.5),
    ("B", 10.5, 11.5),
    ("C", 11.0, 12.0),
    ("D", 11.5, 12.5),
    ("E", 12.0, 13.0),
    ("F", 12.5, 13.5),
    ("G", 13.0, 14.0),
]
"""


import itertools


def planification_taches(taches: list[tuple]) -> list[tuple]:
    """
    Recherche gloutonne de la solution au problème de planification des tâches
    """
    # Tri des tâches par ordre croissant de fin de la tâche
    taches_triees = sorted(taches, key=lambda x: x[2])

    # Création de la liste de tâches planifiées
    taches_planifiees = []

    # Définition de la fin de la dernière tâche planifiée
    fin_derniere_tache = -1

    # Parcours des tâches triées par ordre croissant de fin de la tâche
    for tache in taches_triees:
        # Si la tâche peut être planifiée avant la fin de la dernière tâche planifiée
        if tache[1] >= fin_derniere_tache:
            taches_planifiees.append(tache)
            fin_derniere_tache = tache[2]

    return taches_planifiees


def duree_totale_taches(taches: list[tuple]) -> float:
    """
    Renvoie la durée totale d'une liste de tâches supposées compatibles
    entre elles.
    """
    # Initialiser les variables de durée totale et fin de la dernière tâche
    duree_totale = 0

    # Parcourir chaque tâche
    for tache in taches:
        # Ajouter la durée de la tâche à la durée totale
        duree_totale += tache[2] - tache[1]

    return duree_totale


def presenter_taches(taches: list[tuple]):
    """
    Affiche une liste de tâches, supposées compatibles et la durée totale.
    """
    print("Tâches planifiées :")
    for tache in taches:
        print(f"{tache[0]} : début {tache[1]}, fin {tache[2]}")

    print(f"Durée totale {duree_totale_taches(taches)}")
    print()


def planification_taches_exhaustif(taches: list[tuple]):
    """
    Recherche exhaustive d'une solution optimale
    """
    # Générer toutes les permutations possibles de la liste de tâches
    permutations = itertools.permutations(taches)

    # Initialiser les variables de la meilleure solution trouvée
    meilleur_planification = None
    meilleur_duree_totale = -float("inf")

    # Parcourir chaque permutation possible
    for permutation in permutations:
        # Vérifier si la permutation est valide (pas de chevauchement de tâches)
        duree_totale = 0
        fin_derniere_tache = 0
        valide = True
        for tache in permutation:
            if tache[1] < fin_derniere_tache:
                valide = False
                break
            duree_totale += tache[2] - tache[1]
            fin_derniere_tache = tache[1]

        # Si la permutation est valide et donne une durée totale plus courte
        # que la meilleure solution actuelle
        if valide and duree_totale > meilleur_duree_totale:
            meilleur_planification = permutation
            meilleur_duree_totale = duree_totale

    return meilleur_planification


def test_planification_taches():
    """
    Exemple de tâches à planifier
    """
    taches = [
        ("A", 9.5, 10.5),
        ("B", 10.5, 11.5),
        ("C", 11.0, 12.0),
        ("D", 11.5, 12.5),
        ("E", 12.0, 13.0),
        ("F", 12.5, 13.5),
        ("G", 13.0, 14.0),
    ]

    # Affichage des tâches à planifier
    print("Tâches à planifier :")
    for tache in taches:
        print(f"{tache[0]} : début {tache[1]}, fin {tache[2]}")
    print()

    # Planification des tâches
    taches_gloutonnes = planification_taches(taches)

    # Affichage des tâches planifiées
    print("Solution gloutonne")
    presenter_taches(taches_gloutonnes)

    taches_opti = planification_taches_exhaustif(taches)
    # Affichage des tâches planifiées
    print("Solution exhaustive")
    presenter_taches(taches_opti)


if __name__ == "__main__":
    test_planification_taches()
