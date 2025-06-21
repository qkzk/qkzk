import csv


def charger(fichier: str) -> list:
    """Charge un fichier csv, renvoie une list de dict"""
    with open(fichier, encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        lines = [dict(line) for line in reader]
    return lines


def selectionner(contenu: list, champ: str, valeur: str):
    """Enregistrements de contenu pour lesquels champ=valeur"""
    return [ligne for ligne in contenu if ligne[champ] == valeur]


def projeter(contenu: list, champ: str) -> list:
    """Valeurs de 'champ' pour chaque enregistrement de contenu"""
    return [ligne[champ] for ligne in contenu]


def sauvegarder(fichier: str, contenu: list, champs: list):
    """Sauvegarde un fichier au format csv. Les fieldnames doivent correspondre"""
    with open(fichier, "w", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(contenu)


def exemple():
    # Les employés de Calcutta
    fichier1 = "employees.csv"
    contenu1 = charger(fichier1)
    print(contenu1)
    coe = selectionner(contenu1, "Branch", "COE")
    print(coe)
    names = projeter(contenu1, "Name")
    print(names)

    # Les employés de Paris
    fichier2 = "employees2.csv"
    contenu2 = charger(fichier2)

    # On fusionne tous les employés
    # exactement les mêmes champs dans les 2 contenus !
    contenu_fusion = contenu1 + contenu2
    champs = ["Name", "Branch", "Year", "CGPA"]

    fichier3 = "employees_fusion.csv"
    sauvegarder(fichier3, contenu_fusion, champs)

    # La "branch" IT après la fusion
    it_fusion = selectionner(contenu_fusion, "Branch", "IT")
    print(it_fusion)
    fichier4 = "it_fusion.csv"
    sauvegarder(fichier4, it_fusion, champs)

    # ATTENTION, pour faire des calculs, il faut penser à convertir en nombre !!!
    # anciennete_moyenne = sum(projeter(contenu_fusion, "Year")) / len(contenu_fusion)
    # Provoque une erreur "TypeError", les "Year" ont pour valeur des `str` !!!
    ages = [int(age) for age in projeter(contenu_fusion, "Year")]
    print(ages)  # des int
    anciennete_moyenne = sum(ages) / len(ages)
    print(anciennete_moyenne)


exemple()
