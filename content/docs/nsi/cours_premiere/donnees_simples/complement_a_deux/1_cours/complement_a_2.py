def flip_bits_and_add_one(a: int, size: int) -> int:
    """
    Démarche du complément à 2 sur size bits :

    1. Echanger les bits d'un entier
    2. Ajouter 1
    3. Enlever les bits trop à gauche

    """
    # on crée un masque rempli de 1 : "11111111...1111"
    mask = (1 << size) - 1
    # 1. échanger tous les bits
    a ^= mask
    # 2. ajouter 1
    a += 1
    # 3. retirer les bits trop à gauche
    a &= mask

    return a


def comp2(n: int, size: int) -> str:
    """Renvoie le complément à 2 sur `size` bits de `n`"""
    if n >= 0:
        return bin(n)
    a = flip_bits_and_add_one(-n, size)
    return bin(a)


def read_comp2(bits: str, size: int) -> int:
    """Evalue la valeur d'un entier en complément à 2 sur size bits"""
    # retirer "0b" au début
    bits = bits.replace("0b", "")

    # s'il est positif, rien à faire
    if len(bits) < size or bits[0] == 0:
        return int(bits, 2)

    # convertir en entier, comme s'il était positif
    a = int(bits, 2)
    a = flip_bits_and_add_one(a, size)
    return -a


def table():
    """
    Dessine une table de valeurs du complément à 2 sur 8 bits.
    Profite de l'occasion pour tester toutes les valeurs.
    """
    for n in range(127, -129, -1):
        assert n == read_comp2(comp2(n, 8), 8)
        print(f"{n}\t{comp2(n, 8)}")


table()
