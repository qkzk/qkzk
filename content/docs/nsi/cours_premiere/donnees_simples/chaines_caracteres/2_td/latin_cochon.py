CONSONNES = "BCDFGHJKLMNPQRSTVWXZ"


def mot_latin_cochon(mot: str) -> str:
    if mot[0] in CONSONNES:
        mot_encode = mot[1:] + mot[0] + "UM"
    else:
        mot_encode = mot
    return mot_encode


def phrase_latin_cochon(phrase: str) -> str:
    mots = phrase.split(" ")
    nouvelle_phrase = " ".join([mot_latin_cochon(mot) for mot in mots])
    return nouvelle_phrase


def mot_latin_cochon2(mot: str) -> str:
    """Version sans slice"""
    if mot[0] in CONSONNES:
        mot_encode = ""
        for indice in range(1, len(mot)):
            mot_encode = mot_encode + mot[indice]
        mot_encode = mot_encode + mot[0]
        mot_encode = mot_encode + "UM"
    else:
        mot_encode = mot
    return mot_encode


def phrase_latin_cochon2(phrase: str) -> str:
    """Version sans join ou split"""
    phrase_encodee = ""
    courant = ""
    for indice in range(len(phrase)):
        if phrase[indice] != " ":
            courant = courant + phrase[indice]
        else:
            mot_encode = mot_latin_cochon2(courant)
            phrase_encodee = phrase_encodee + mot_encode + " "
            courant = ""
    # ne pas oublier le dernier mot...
    mot_encode = mot_latin_cochon2(courant)
    phrase_encodee = phrase_encodee + mot_encode

    return phrase_encodee


print(mot_latin_cochon("VITRE"))
print(phrase_latin_cochon("LA VITRE MENACE DE TOMBER"))

print(mot_latin_cochon2("VITRE"))
print(phrase_latin_cochon2("LA VITRE MENACE DE TOMBER"))
