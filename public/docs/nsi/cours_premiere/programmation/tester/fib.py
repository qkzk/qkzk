def fibonacci(n):
    """
    Liste des termes de la suite de Fibonacci
      de l'indice 0 à l'indice n inclus

    @param n: (int) l'indice maximal voulu
    @return: (list) la liste des termes
    """
    if type(n) != int or n < 0:
        return None
    x = 1
    y = 1
    suite_fibonacci = [x]
    indice = 0
    while indice < n:
        x, y = y, x + y
        suite_fibonacci.append(x)
        indice += 1
    return suite_fibonacci
