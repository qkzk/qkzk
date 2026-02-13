import csv

TITANIC_CSV = "./titanic.csv"


def ouvrir(fichier: str) -> list:
    with open(fichier, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f, delimiter=",")
        return [dict(ligne) for ligne in lecteur]


enregistrements = ouvrir(TITANIC_CSV)

# Question 1
descripteurs = list(enregistrements[0].keys())
print("Les descripteurs sont:")
print(descripteurs)

# Question 2:
nb_passagers = len(enregistrements)
print(f"Il y avait {nb_passagers} passagers")

# Question 3:
projection_survived = [int(passager["Survived"]) for passager in enregistrements]
nb_survivants = sum(projection_survived)
print(f"{nb_survivants} ont survecu au nauffrage")

# Question 4:
fares = [float(passager["Fare"]) for passager in enregistrements]
chiffre_d_affaire = sum(fares)
print(f"Le voyage a rapporté {chiffre_d_affaire} aux organisateurs")

# Question 5:
nb_hommes = len([p for p in enregistrements if p["Sex"] == "male"])
nb_femmes = len([p for p in enregistrements if p["Sex"] == "female"])
nb_hommes_survivants = len(
    [p for p in enregistrements if p["Sex"] == "male" and p["Survived"] == "1"]
)
nb_femmes_survivantes = len(
    [p for p in enregistrements if p["Sex"] == "female" and p["Survived"] == "1"]
)

print(
    f"Le taux de survie chez les hommes est de {nb_hommes_survivants / nb_hommes:.2%} et chez les femmes {nb_femmes_survivantes / nb_femmes:.2%}"
)

# Question 6
classes = sorted(list(set(p["Pclass"] for p in enregistrements)))

tarifs_moyens = {
    classe: sum(float(p["Fare"]) for p in enregistrements if p["Pclass"] == classe)
    / len([p for p in enregistrements if p["Pclass"] == classe])
    for classe in classes
}
print("Les tarifs moyens de chaque classe sont :")
print(tarifs_moyens)

# Question 7
taux_survie_par_classe = {
    classe: len(
        [p for p in enregistrements if p["Pclass"] == classe and p["Survived"] == "1"]
    )
    / len([float(p["Fare"]) for p in enregistrements if p["Pclass"] == classe])
    for classe in classes
}
print("Le taux de survie de chaque classe est :")
for classe in classes:
    print(f"Classe {classe} : taux de survie {taux_survie_par_classe[classe]:.2%}")

# Question 8
ages = [
    {"nom": p["Name"], "age": float(p["Age"]), "survecu": p["Survived"] == "1"}
    for p in enregistrements
    if p["Age"] != ""
]

ages_survivants = [p for p in ages if p["survecu"]]
ages_decedes = [p for p in ages if not p["survecu"]]

ages_survivants.sort(key=lambda p: p["age"])
ages_decedes.sort(key=lambda p: p["age"])

jeune_survivant = ages_survivants[0]
vieux_survivant = ages_survivants[-1]
jeune_decede = ages_decedes[0]
vieux_decede = ages_decedes[-1]

print(
    f"Le plus jeune survivant est {jeune_survivant['nom']} agé de {jeune_survivant['age']}"
)
print(
    f"Le plus vieux survivant est {vieux_survivant['nom']} agé de {vieux_survivant['age']}"
)
print(f"Le plus jeune decede est {jeune_decede['nom']} agé de {jeune_decede['age']}")
print(f"Le plus vieux survivant est {vieux_decede['nom']} agé de {vieux_decede['age']}")

# Question 9
ratio = 90 * 7 / 2.10
tarifs = [float(p["Fare"]) for p in enregistrements]
tarif_eleve = max(tarifs)
tarif_moyen = sum(tarifs) / len(enregistrements)
tarif_eleve_2026 = tarif_eleve * ratio
tarif_moyen_2026 = tarif_moyen * ratio
print(f"Le tarif le plus élevé correspondrait à {tarif_eleve_2026:.2f} € de 2026")
print(f"Le tarif moyen correspondrait à {tarif_moyen_2026:.2f} € de 2026")
