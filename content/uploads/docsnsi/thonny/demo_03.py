def syracuse(u):
    '''
    Renvoie le terme suivant u d'une suite de syracuse
    
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