
import csv


def depuis_csv(fichier):
    with open(fichier, 'r') as contenu_csv:
        lecteur = csv.DictReader(contenu_csv)
        return [dict(ligne) for ligne in lecteur]


def vers_csv(nom: str, ordre: list) -> None:
    with open(nom + '.csv', 'w') as fichier:
        dic = csv.DictWriter(fichier, fieldnames=ordre)
        table = eval(nom)
        dic.writeheader()  # pour la 1ere lire, celle des attributs
        for ligne in table:
            dic.writerow(ligne)  # ajoute les lignes de la table
    return None
