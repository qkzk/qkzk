def syracuse(u):
    '''
    Renvoie le terme suivant u d'une suite de syracuse
    
    :param u: (int) entier quelconque
    :return: (int)
    :CU: aucune
    
    >>> syracuse(0)
    0
    >>> syracuse(3)
    10
    >>> syracuse(50)
    25
    '''
    if u % 2 == 0:
        res = u // 2
    else:
        res = 3 * u + 1
    return res


def terme_syracuse(a, n):
    u = a
    for _ in range(n):
        u = syracuse(u)
    return u


def atterissage_syracuse(a):
    n = 0
    u = a
    while u != 1:
        u = syracuse(u)
        n += 1
    return n