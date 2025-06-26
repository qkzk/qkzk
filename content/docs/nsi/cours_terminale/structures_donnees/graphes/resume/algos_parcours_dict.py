"""
Implémentation des algorithmes de parcours de graphes simple
cf [qkzk](https://qkzk.xyz/docs/nsi/cours_terminale/structures_donnees/graphes/cours_algo/)

Les graphes sont représentés par des dictionnaires.
On essaye d'éviter la construction des drapeaux qui nécessitent de connaître le graphe entier.
C'est toujours possible.
"""


def voisins(g: dict, s) -> list:
    """Renvoie la liste des voisins de s dans le graphe g"""
    return g[s]


def parcours_largeur(g: dict, source) -> list:
    """
    Réalise un parcours en largeur du graphe.
    Plutôt que d'utiliser les drapeaux qui nécessitent de connaître tout le graphe,
    on se contente d'entretenir une liste des sommets déjà enfilés.
    On n'enfile un voisin que s'il ne l'a pas déjà été.

    précondition: g est un graphe simple correctement construit.
    """
    file = [source]
    enfiles = [source]
    visites = []
    while file:
        courant = file.pop(0)
        for voisin in voisins(g, courant):
            if not voisin in enfiles:
                file.append(voisin)
                enfiles.append(voisin)
        visites.append(courant)

    return visites


def parcours_profondeur(g: dict, source) -> list:
    """
    Réalise un parcours en profondeur du graphe.
    Plutôt que d'utiliser les drapeaux qui nécessitent de connaître tout le graphe,
    on se contente d'entretenir une liste des sommets déjà empilés.
    On n'empile un voisin que s'il ne l'a pas déjà été.

    précondition: g est un graphe simple correctement construit.
    """
    pile = [source]
    empiles = [source]
    visites = []
    while pile:
        courant = pile.pop()
        for voisin in voisins(g, courant):
            if not voisin in empiles:
                pile.append(voisin)
                empiles.append(voisin)
        visites.append(courant)

    return visites


def construire_chemin(preds, source, dest):
    """
    Fabrique un chemin entre source et dest en remontant le dictionnaire des prédécesseurs : preds

    Précondition: le dictionnaire des prédécesseurs est valide.
    """
    chemin = [dest]
    courant = dest
    while not courant == source:
        courant = preds[courant]
        chemin.append(courant)

    return chemin[::-1]


def recherche_chemin(g: dict, source, dest) -> list:
    """
    Construit un chemin entre source et dest dans un graphe simple et connexe.

    Précondition : g est un graphe simple correctement construit et les sommets
        source et dest sont joignables
    """
    pile = [source]
    preds = {source: None}
    while pile:
        courant = pile.pop()
        for voisin in voisins(g, courant):
            if not voisin in preds:
                preds[voisin] = courant
                if voisin == dest:
                    break
                pile.append(voisin)
    return construire_chemin(preds, source, dest)


def contient_un_cycle(g: dict, source) -> bool:
    """
    Renvoie vrai si et seulement s'il y a un cycle dans le graphe g.
    Cette fois, on utilise les drapeaux. On pourrait s'en passer mais autant
    illustrer cette approche.

    Précondition: g est un graphe simple et connexe.
    """
    drapeaux = {sommet: -1 for sommet in g}
    pile = [source]
    drapeaux[source] = 0
    while pile:
        courant = pile.pop()
        drapeaux[courant] = 1
        for voisin in voisins(g, courant):
            if drapeaux[voisin] == 0:
                return True
            elif drapeaux[voisin] == -1:
                drapeaux[voisin] = 0
                pile.append(voisin)

    return False


def example():
    """Quelques graphes pour illustrer les parcours"""

    # fmt: off
    g1 = {
        "a": ["b", "c"],
        "b": ["c", "a"],
        "c": ["a", "b", "d"],
        "d": ["c"]
    }

    g2 = {
        0: [1, 2],
        1: [0, 2, 5],
        2: [0, 1, 3],
        3: [2, 4],
        4: [3],
        5: [1],
    }

    g3 = {
        0: [1, 2],
        1: [0, 5, 4],
        2: [0, 3, 4],
        3: [2],
        4: [1, 2],
        5: [1],
    }

    g4 = {
        0: [1, 2],
        1: [0, 5],
        2: [0, 3, 4],
        3: [2],
        4: [2],
        5: [1],
    }
    # fmt: on

    print(parcours_largeur(g1, "a"))
    print(g1)
    print(parcours_profondeur(g1, "a"))
    print(g1)
    print(parcours_largeur(g4, 0))
    print(g4)
    print(recherche_chemin(g2, 0, 4))
    print(g2)
    print(contient_un_cycle(g3, 0))
    print(g3)
    print(contient_un_cycle(g4, 0))
    print(g4)


if __name__ == "__main__":
    example()
