def syracuse(u):
    '''
    renvoie le terme suivant u dans une suite de Syracuse
    
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
        res = 3*u + 1
    return res

def terme_syracuse(a, n):
    '''
    renvoie le terme d'indice n de la suite de Syracuse de terme initial a
    
    :param a: (int) terme initial de la suite de Syracuse envisagée
    :param n: (int) indice du terme souhaité
    :return: (int)
    :CU: n >= 0
    
    >>> terme_syracuse(0, 10)
    0
    >>> terme_syracuse(10, 0)
    10
    >>> terme_syracuse(10, 1)
    5
    >>> terme_syracuse(10, 2)
    16
    '''
    u = a
    for i in range(n):
        u = syracuse(u)
    return u

def atterrissage_syracuse(a):
    '''
    renvoie l'indice du terme d'«atterrissage» de la suite de Syracuse
    de terme initial a
    
    :param a: (int) terme initial d'une suite de Syracuse
    :return: (int) premier indice n tel que u_n = 1
    :CU: a > 0
    
    >>> atterrissage_syracuse(1)
    0
    >>> atterrissage_syracuse(2)
    1
    >>> atterrissage_syracuse(3)
    7
    '''
    n = 0
    u = a
    while u != 1:
        u = syracuse(u)
        n = n + 1
    return n
