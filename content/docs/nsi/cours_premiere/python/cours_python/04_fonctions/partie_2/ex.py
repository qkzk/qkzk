MOIS = (
    ("janvier", 31),
    ("février", 28),
    ("mars", 31),
    ("avril", 30),
    ("mai", 31),
    ("juin", 30),
    ("juillet", 31),
    ("aout", 31),
    ("septembre", 30),
    ("octobre", 31),
    ("novembre", 30),
    ("décembre", 31),
)


def calculer_mois(jour: int):
    jours_ecoules = 0
    mois = MOIS[0][0]
    for i in range(len(MOIS)):
        mois, nb_jours = MOIS[i]
        jours_ecoules += nb_jours
        if jours_ecoules >= jour:
            break
    return mois


assert calculer_mois(1) == "janvier"
assert calculer_mois(31 + 1) == "février"
assert calculer_mois(31 + 27) == "février"
assert calculer_mois(31 + 28 + 31) == "mars"
assert calculer_mois(31 + 28 + 31 + 1) == "avril"
assert calculer_mois(364 - 32) == "novembre"
assert calculer_mois(364) == "décembre"
