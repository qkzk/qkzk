'''
title : Réaliser un jeu de test d'une fonction
author : qkzk
'''


def fibonacci(n):
    '''
    Liste des termes de la suite de Fibonacci de l'indice 0 à l'indice n inclus

    @param n: (int) l'indice maximal voulu
    @return: (list) la liste des termes

    >>> fib_10 = fibonacci(10)

    >>> len(fib_10)
    11

    # différents résultats
    >>> fibonacci(0)
    [1]
    >>> fibonacci(1)
    [1, 1]
    >>> fibonacci(5)
    [1, 1, 2, 3, 5, 8]

    # ses éléments sont entiers
    >>> for terme in fib_10:
    ...    type(terme) == int
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    True

    # La propriété de récurrence
    >>> fib_10[-3] + fib_10[-2] == fib_10[-1]
    True

    # Valeur de retour dans les cas impossibles
    >>> fibonacci(-1)

    >>> fibonacci('a')

    >>> fibonacci(3.14)
    '''
    if type(n) != int or n < 0:
        return
    x = 1
    y = 1
    suite_fibonacci = [x]
    indice = 0
    while indice < n:
        x, y = y, x + y
        suite_fibonacci.append(x)
        indice += 1
    return suite_fibonacci


def Fonction_mal_testee():
    '''
    Simple fonction qui echoue
    >>> Fonction_mal_testee()
    3
    '''
    return 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # s'il ne se passe rien, les tests sont justes.
