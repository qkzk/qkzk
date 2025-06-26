"""
Implémentation d'une classe pour les graphes simples.

On peut en hériter pour créer d'autres graphes.

Se construisent par étape (ils sont mutables MAIS pas implémenté la suppression)
Ils peuvent aussi se construire avec une matrice d'adjacence ou
un dictionnaire pour les sommets.

Un exemple présente les méthodes.
"""

from pprint import pprint


class Graphe:
    """
    Graphes non orientés et non pondérés

    Trois modes de constructions :
    * Créer et graphe vide et ajouter des sommets ou des arêtes
    * Depuis une matrice d'adjacence (les sommets sont numérotés à partir de 0)
    * Depuis un dictionnaire des arêtes.

    On peut aussi :

    * obtenir la matrice d'adjacence,
    * savoir si un graphe est orienté ou non,
    * obtenir les sommets et les arêtes,
    * obtenir les voisins d'un sommet,
    """

    def __init__(self):
        """Construit un graphe simple vide"""
        self.oriente = False
        self.sommets = []
        self.aretes = {}
        self.matrice = None

    def est_vide(self):
        """Vrai ssi le graphe n'a aucun sommet"""
        return len(self.sommets) == 0

    def est_simple(self):
        """Vrai si le graphe est simple. Avec un test pour l'héritage"""
        return not self.oriente

    def est_oriente(self):
        """Vrai si le graphe est orienté. Avec un test pour l'héritage"""
        return self.oriente

    def ajouter_sommet(self, s):
        """Ajoute un sommet au graphe s'il n'y figure pas déjà"""
        if not s in self.sommets:
            self.sommets.append(s)

    def ajouter_arete(self, d, a):
        """
        Ajoute une arrête au graphe.
        Pour les graphes simples, il ajoute en fait deux arêtes :
        de a vers d, de d vers a
        """
        if not d in self.sommets:
            self.sommets.append(d)
        if not a in self.sommets:
            self.sommets.append(a)

        if d not in self.aretes:
            self.aretes[d] = [a]
        else:
            self.aretes[d].append(a)
        if a not in self.aretes:
            self.aretes[a] = [d]
        else:
            self.aretes[a].append(d)

    def sont_adjacents(self, d, a):
        """Vrai ssi les sommets d et a sont connectés par une arrête."""
        return d in self.aretes and a in self.aretes[d]

    def voisins(self, d):
        """Retourne la liste des voisins d'un sommet d du graphe"""
        if not d in self.aretes:
            return []
        return self.aretes[d]

    def matrice_adjacence(self):
        """
        Crée (si ce n'est pas déjà fait ou si le graphe a changé depuis)
        la matrice d'adjacence et la retourne
        @return: (list) double liste carrée : la matrice d'adjacence
        """
        nb_sommets = len(self.sommets)
        if self.matrice is None or len(self.matrice) != nb_sommets:
            self.matrice = [[0] * nb_sommets for _ in range(nb_sommets)]
            for i, d in enumerate(self.sommets):
                for j, a in enumerate(self.sommets):
                    self.matrice[i][j] = 1 if self.sont_adjacents(d, a) else 0
        return self.matrice

    def liste_adjacence(self):
        """Retourne le dictionnaire des arêtes. Les noms sont mal choisis
        mais en Python d'après son concepteur, utiliser une table de hashage
        est optimal"""
        return self.aretes

    @classmethod
    def depuis_matrice_adjacence(cls, matrice):
        """
        Retourne un Graphe crée depuis sa matrice d'adjacence

        @param matrice: (list) une matrice carrée
        @return: (Graphe) le graphe qui a cette matrice d'adjacence
        """
        if not isinstance(matrice, list):
            raise ValueError("La matrice doit être un objet list")
        if len(matrice) > 0 and len(matrice) != len(matrice[0]):
            raise ValueError("La matrice doit être carrée")
        g = cls()
        for source, ligne in enumerate(matrice):
            for destination, arete_presente in enumerate(ligne):
                if arete_presente == 1:
                    g.ajouter_arete(source, destination)
        return g

    @classmethod
    def depuis_dictionnaire_aretes(cls, dico_aretes):
        """
        Retourne un graphe formé à partir du dictionnaire des sommets

        @param dico_aretes: (dict) le dictionnaire des arêtes
            de la forme sommet: liste de arêtes
        @return: (Graphe) le graphe qui a ces arêtes.
        """
        g = cls()
        for source, voisins in dico_aretes.items():
            for destination in voisins:
                g.ajouter_arete(source, destination)
        return g


def presenter_exemple():
    g = Graphe()
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

    print(g.voisins("a"))

    m_adj = g.matrice_adjacence()
    pprint(m_adj)
    print()

    l_adj = g.liste_adjacence()
    pprint(l_adj)

    mat = [[0, 1], [1, 0]]
    h = Graphe.depuis_matrice_adjacence(mat)
    m = h.matrice_adjacence()
    assert mat == m

    dico = {
        "a": ["b", "c"],
        "b": ["c"],
    }

    k = Graphe.depuis_dictionnaire_aretes(dico)
    pprint(k.matrice_adjacence())


if __name__ == "__main__":
    presenter_exemple()
