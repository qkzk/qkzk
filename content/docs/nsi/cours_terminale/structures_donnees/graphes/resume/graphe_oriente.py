"""
Implémentation d'une classe pour les graphes orientés qui hérite
des graphes simples

En plus des méthodes pour les graphes simples,
on peut obtenir la liste des successeurs et prédécesseurs d'un sommet.

Un exemple présente les méthodes.
"""

from pprint import pprint
from graphe_simple import Graphe


class GrapheOriente(Graphe):
    """
    Hérite des graphes simples toutes les méthodes.

    Deux méthodes nouvelles :

    * liste des prédécesseurs et successeurs

    Deux méthodes modifiées

    * ils sont construits comme "graphe orientés"
    * ajouter une arête n'ajoute que l'arête de a vers d, pas de d vers a.
    """

    def __init__(self):
        """Construit un graphe orienté vide"""
        super().__init__()
        self.oriente = True

    def ajouter_arete(self, d, a):
        """
        ajoute une arrête au graphe.
        @param d: (any) sommet de départ
        @param a: (any) sommet d'arrivée
        """
        if not d in self.sommets:
            self.sommets.append(d)
        if not a in self.sommets:
            self.sommets.append(a)

        if d not in self.aretes:
            self.aretes[d] = [a]
        else:
            self.aretes[d].append(a)

    def successeurs(self, d):
        """Retourne la list des successeurs d'un sommet d"""
        return self.voisins(d)

    def predecesseurs(self, a):
        """
        Retourne la list des prédécesseurs d'un sommet a

        Pour chaque sommet d, on cherche s'il existe l'arc d -> a
            si c'est le cas on l'ajoute à la liste.
        """
        return [d for d in self.aretes if a in self.aretes[d]]


def presenter_exemple():
    g = GrapheOriente()
    g.ajouter_arete("a", "b")
    g.ajouter_arete("a", "c")
    g.ajouter_arete("b", "c")
    g.ajouter_arete("b", "d")
    g.ajouter_arete("c", "e")
    g.ajouter_arete("d", "f")
    g.ajouter_arete("e", "f")
    g.ajouter_sommet("h")

    print(g.sont_adjacents("b", "e"))
    print(g.sont_adjacents("b", "f"))
    print(g.sont_adjacents("f", "e"))
    print(g.sont_adjacents("e", "f"))

    m_adj = g.matrice_adjacence()
    pprint(m_adj)

    l_adj = g.liste_adjacence()
    pprint(l_adj)

    mat = [[0, 1], [1, 0]]
    h = GrapheOriente.depuis_matrice_adjacence(mat)
    m = h.matrice_adjacence()
    assert mat == m

    dico = {
        "a": ["b", "c"],
        "b": ["c"],
    }

    k = GrapheOriente.depuis_dictionnaire_aretes(dico)
    pprint(k.matrice_adjacence())
    return k


if __name__ == "__main__":
    k = presenter_exemple()
