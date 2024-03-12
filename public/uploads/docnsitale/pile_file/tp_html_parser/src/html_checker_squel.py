from stack import Stack
from myqueue import Queue
from html_parser1 import parse

def html_checker(s):
    """
    :param s: (str) un document html
    :return: (bool) True si `s` est bien formé, False sinon
    :CU: Aucune
    :Exemple:

    >>> html_checker("<!DOCTYPE html><html lang='fr'><div><p></p></div></html>")
    True
    >>> html_checker("<!DOCTYPE html><html lang='fr'><div></p></div><p></html>")
    False
    >>> html_checker("<!DOCTYPE html><html lang='fr'><div><p></p></div>")
    False
    """
    pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        # pas d'arguments sur la ligne de commande
        # on exécute les tests.
        import doctest
        doctest.testmod(verbose = True)
    else:
        # on considère que l'argument est le nom d'un fichier
        fname = sys.argv[1]
        try:
            with open(fname, 'r') as f:
                if html_checker(f.read()):
                    print("le fichier {} est un fichier html correct.".format(fname))
                else:
                    print("le fichier {} n'est pas un fichier html correct.".format(fname))
        except:
            print("Impossible de parser le fichier {}".format(fname))
