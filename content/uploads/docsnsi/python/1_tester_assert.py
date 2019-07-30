'''
title : Réaliser un jeu de test d'une fonction
author : qkzk
'''


def fibonacci(n):
    '''
    Liste des termes de la suite de Fibonacci de l'indice 0 à l'indice n inclus

    @param n: (int) l'indice maximal voulu
    @return: (list) la liste des termes
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


def tester_fibonacci():
    '''
    Teste certaines propriétés de la fonction Fibonacci

    return: None
    CU: lève une exception AssertionError si la fonction est mal programmée
    '''
    fib_10 = fibonacci(10)

    # longueur de la liste
    assert len(fib_10) == 11

    # différents résultats
    assert fibonacci(0) == [1]
    assert fibonacci(1) == [1, 1]
    assert fibonacci(5) == [1, 1, 2, 3, 5, 8]

    # ses éléments sont entiers
    for terme in fib_10:
        assert type(terme) == int

    # La propriété de récurrence
    assert fib_10[-3] + fib_10[-2] == fib_10[-1]

    # Valeur de retour dans les cas impossibles
    assert fibonacci(-1) == None
    assert fibonacci('a') == None
    assert fibonacci(3.14) == None


if __name__ == '__main__':
    tester_fibonacci()  # ne renvoit rien, tout va bien
