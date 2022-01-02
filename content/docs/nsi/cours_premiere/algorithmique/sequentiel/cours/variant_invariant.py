def puissance(a: int, n: int) -> int:
    """Renvoie le nombre a exposant n."""

    p = 1

    while n > 0:
        if n % 2 == 0:
            a = a * a
            n = n // 2
        else:
            p = p * a
            n = n - 1
    return p

def somme(tableau: list) -> int:
    """Renvoie la somme du tableau"""
    s = 0
    for x in tableau:
        s = s + x
    return s

def division_par_soustraction(a: int, b: int) -> tuple:
    """
    Renvoie (q, r) tels que a = b * q + r et r < b
    @param a: (int) a >= 0
    @param b: (int) b > 0
    @return: (int, int) (q, r) tels que a = b * q + r et r < b
    """
    r = a
    q = 0

    while r >= b:
        r = r - b
        q = q + 1

    return q, r


def test():
    """Teste la validité des fonctions"""

    for i in range(10):
        assert puissance(3, i) == 3 ** i

    for tableau in [list(range(n)) for n in range(20)]:
        assert somme(tableau) == sum(tableau)

    for a in range(1, 10):
        for b in range(1, a):
            assert division_par_soustraction(a, b) == divmod(a, b)


if __name__ == "__main__":
    test()
