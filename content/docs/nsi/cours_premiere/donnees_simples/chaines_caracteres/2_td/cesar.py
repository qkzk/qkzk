def cesar(texte_clair: str) -> str:
    """
    Encode un texte avec la méthode de chiffrement de César et la clé 3
    texte_clair doit être écrit en MAJUSCULES : BONJOUR

    ord("A"): encodage du A
    ord(lettre) - ord("A") : écart entre la lettre et A
    ord(lettre) - ord("A") + 3 : écart entre la lettre et A + 3
    ... % 26 : tourne pour les dernière lettre
    ... + ord("A") : encodage de la nouvelle lettre en ASCII
    chr(...) la nouvelle lettre elle-même
    """
    a = ord("A")
    encode = ""
    for lettre in texte_clair:
        encode += chr((ord(lettre) - a + 3) % 26 + a)
    return encode


def decesar(texte_encode: str) -> str:
    """
    Décode un texte avec la méthode de chiffrement de César et la clé 3
    texte_encode doit être écrit en MAJUSCULES : BONJOUR
    """
    a = ord("A")
    encode = ""
    for lettre in texte_encode:
        encode += chr((ord(lettre) - a - 3) % 26 + a)
    return encode


def exemple():
    texte = "BONJOUR"
    chiffre = cesar(texte)
    dechiffre = decesar(chiffre)

    print(texte, chiffre, dechiffre)


if __name__ == "__main__":
    exemple()
