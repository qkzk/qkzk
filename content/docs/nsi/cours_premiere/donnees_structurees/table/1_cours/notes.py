"""
Exemple d'utilisation du module csv pour lire, manipuler et sauvegarder un fichier csv.

Avant la modification : "notes.csv"
Après la modifiacation : "notes_apres.csv"

"""

import csv
from typing import Callable


def charger(fichier: str) -> list:
    """Lit le contenu du fichier CSV dont le séparateur est ";"" et renvoie une liste de dict"""
    with open(fichier, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [dict(ligne) for ligne in reader]


def sauvegarder(fichier: str, tableau) -> None:
    """Enregistre un tableau au format CSV dans fichier. Le séparateur est ";" """
    with open(fichier, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=tableau[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(tableau)


def selectionner(tableau: list, critere: Callable) -> list:
    """
    Réalise la sélection des lignes du tableau qui vérifient le critère.

    `critere` est une fonction qui prend une ligne du tableau (un dict) et renvoie un booléen
    """
    return [ligne for ligne in tableau if critere(ligne)]


def est_bon_en_maths(ligne: dict) -> bool:
    """Vrai ssi l'étudiant a une note supérieure ou égale à 17 en maths"""
    return float(ligne["Mathématiques"]) >= 17


def projeter(tableau: list, champ: str) -> list:
    """Projete le tableau et extraie la colonne "champ" """
    return [ligne[champ] for ligne in tableau]


def exemple():
    # charger le contunu dans une liste de dictionnaires :
    tableau = charger("notes.csv")

    # combien d'élèves dans ce fichier ?
    print("Il y a ", len(tableau), "élèves dans le fichier")

    # sélectionner ceux qui ont 17+ en maths :
    bons_en_maths = selectionner(tableau, est_bon_en_maths)

    for ligne in bons_en_maths:
        print(ligne)

    # projeter le tableau pour obtenir la note d'info
    notes_d_info = projeter(tableau, "Informatique")

    # ce sont des `str`, faisons en des floats :
    notes_d_info = [float(note) for note in notes_d_info]
    print(notes_d_info)
    # maintenant on peut calculer la moyenne :
    print("moyenne d'info", sum(notes_d_info) / len(notes_d_info))

    # Théo Fernandes a triché en informatique, mettons lui 0 !
    for i in range(len(tableau)):
        # on trouve son indice dans le tableau
        ligne = tableau[i]
        if ligne["Prénom"] == "Théo" and ligne["Nom"] == "Fernandes":
            # avant
            print(ligne)
            ligne["Informatique"] = 0
            # on l'a trouvé, inutile de chercher plus loin.
            break

    # apres
    print(tableau[i])

    # sauvegarder dans un nouveau fichier
    sauvegarder("notes_apres.csv", tableau)


exemple()
