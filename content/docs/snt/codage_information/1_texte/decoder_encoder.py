    """
title: Encodage et décodage d'un message texte en ASCII.
author: qkzk
date: 2024/08/20
"""


def lire_message_a_encoder() -> str:
    """Lit et renvoie le message à encoder"""

    message = input(
        "Veuillez taper votre message. Il ne doit contenir que des caractères ASCII (pas d'accents) : "
    )
    return message


def construit_encodage(message: str) -> str:
    encodage = ""
    for lettre in message:
        code = ord(lettre)
        if code > 127:
            print(f"Votre message contient le caractère {lettre} qui n'est pas ASCII.")
            print("Recommençons...")
            return ""
        encodage += bin(code)[2:].zfill(8)
        encodage += " "
    return encodage


def encoder():
    """Lit et encode un message depuis l'entrée standard. L'affiche dans la sortie standard."""
    message = lire_message_a_encoder()
    encodage = construit_encodage(message)
    if len(encodage) == 0:
        return
    print("Votre message encodé est : ")
    print(encodage)


def lire_message_a_decoder() -> str:
    """Lit un message dans l'entrée standard, le nettoie et le renvoie."""
    message = input(
        "Veuillez taper un code binaire. Il ne doit contenir que des 0, 1 ou espaces : "
    )
    message = message.strip().replace(" ", "")
    return message


def decode_message(message: str) -> str:
    """Decode un message reçu et le renvoie."""
    nb_bloc = len(message) // 8 + 1
    decodage = ""
    for indice in range(nb_bloc):
        bloc = message[8 * indice : 8 * (indice + 1)]
        if len(bloc) == 0:
            continue
        lettre = chr(int(bloc, 2))
        decodage += lettre
    return decodage


def decoder():
    """Lit et decode un message reçu dans l'entrée standard et l'affiche dans la sortie standard."""
    message = lire_message_a_decoder()
    vide = message.replace("0", "").replace("1", "")
    if len(vide) > 0:
        print(
            f"Votre message contient les caractères {vide} qui ne sont ni 0, 1 ou espace."
        )
        print("Recommençons...")
        return
    decodage = decode_message(message)
    print(decodage)


def main():
    while True:
        reponse = input(
            "Voulez-vous encoder (Oui), décoder (Non) un message ou quitter (Q) ? : "
        )
        debut = reponse[0]
        if debut in "qQ":
            print("Au revoir !")
            return
        elif debut in "oOyYeE":
            encoder()
        else:
            decoder()


if __name__ == "__main__":
    main()
