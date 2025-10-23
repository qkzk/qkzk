---
title: "Plusieurs implantations d'une pile" 
author: qkzk
date: 2025-10-23
theme: metropolis
weight: 5
bookCollapseSection: true
geometry: "margin=1.5cm"
header-includes: |
    \usepackage{tcolorbox}
    \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
    \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}
---

# Implanter une pile utilisant le principe d'une liste

L'objectif de ce TP est d'implanter une pile.

On doit pouvoir :

* créer une pile vide,
* ajouter un élément,
* retirer un élément,
* tester si la pile est vide.


Ajoutons trois opérations :

* consulter le dernier élément entré (donc le prochain à sortir),
* mesurer la longueur,
* représenter dans l'interpréteur.


Nous allons utiliser la programmation objet
et la structure interne sera une liste chaînée.

Plusieurs approches sont possibles, en particulier :

* on peut ajouter en tête de la liste.
* on peut ajouter à la fin de la liste.

Nous allons employer la seconde approche.

**Compléter les extraits de code suivant**

## Version 1 : avec une classe


```python 
from typing import Any


class Pile:
    """Classe modélisant une pile"""

    def __init__(self):
        pass

    def empiler(self, elt: Any) -> None:
        """Ajoute elt à la pile"""
        pass

    def depiler(self) -> Any:
        """
        Retire et renvoie le sommet de la pile.
        Plante si la pile est vide.
        """
        pass

    def est_vide(self) -> bool:
        """Vrai ssi la pile est vide"""
        pass

    def longueur(self) -> int:
        """Le nombre d'éléments de la pile"""
        pass

    def sommet(self) -> Any:
        """
        Permet de consulter le sommet de la pile.
        Ne modifie pas son contenu.
        Plante si la pile est vide.
        """
        pass

    def __repr__(self) -> str:
        pass


def test():
    pile = Pile()
    assert pile.est_vide()
    pile.empiler(5)
    assert not pile.est_vide()
    pile.empiler(1)
    pile.empiler(3)
    pile.empiler(7)
    assert pile.longueur() == 4
    assert pile.depiler() == 7
    pile.empiler(9)
    assert pile.depiler() == 9
    assert pile.depiler() == 3
    assert pile.depiler() == 1
    assert pile.depiler() == 5
    assert pile.est_vide()


if __name__ == "__main__":
    test()
```

## Version 2 : avec des fonctions 

```python 
from typing import Any


def creer_vide() -> list:
    """Renvoie une pile vide"""


def empiler(pile, elt: Any) -> None:
    """Ajoute elt à la pile"""


def depiler(pile) -> Any:
    """
    Retire et renvoie le sommet de la pile.
    Plante si la pile est vide.
    """


def est_vide(pile) -> bool:
    """Vrai ssi la pile est vide"""


def longueur(pile) -> int:
    """Le nombre d'éléments de la pile"""


def sommet(pile) -> Any:
    """
    Permet de consulter le sommet de la pile.
    Ne modifie pas son contenu.
    Plante si la pile est vide.
    """


def test():
    pile = creer_vide()
    assert est_vide(pile)
    empiler(pile, 5)
    assert not est_vide(
        pile,
    )
    empiler(pile, 1)
    empiler(pile, 3)
    empiler(pile, 7)
    assert longueur(pile) == 4
    assert depiler(pile) == 7
    empiler(pile, 9)
    assert depiler(pile) == 9
    assert depiler(pile) == 3
    assert depiler(pile) == 1
    assert depiler(pile) == 5
    assert est_vide(pile)


if __name__ == "__main__":
    test()
```

## Version 3 en employant des cellules

Cette fois on emploie une cellule afin d'enregistrer la valeur. En y ajoutant un lien vers l'élément suivant, ces cellules modélisent des listes chaînées. 

L'interface pour l'utilisateur est totalement identique à la version avec des classes mais les coûts sont différents.

```python
from typing import Any


class Cellule:
    """Une cellule d'une pile"""

    def __init__(self, valeur, suivant):
        self.__valeur = valeur
        self.__suivant = suivant

    def valeur(self):
        """accesseur de la valeur"""
        return self.__valeur

    def suivant(self):
        """accesseur de la suite"""
        return self.__suivant


class Pile:
    """Classe modélisant une pile"""

    def __init__(self):
        pass

    def empiler(self, valeur: Any) -> None:
        """Ajoute valeur à la pile"""

    def depiler(self) -> Any:
        """
        Retire et renvoie le sommet de la pile.
        Plante si la pile est vide.
        """

    def est_vide(self) -> bool:
        """Vrai ssi la pile est vide"""

    def longueur(self) -> int:
        """Le nombre d'éléments de la pile"""

    def sommet(self) -> Any:
        """
        Permet de consulter le sommet de la pile.
        Ne modifie pas son contenu.
        Plante si la pile est vide.
        """

    def __repr__(self) -> str:
        pass


def test():
    pile = Pile()
    assert pile.est_vide()
    pile.empiler(5)
    assert not pile.est_vide()
    pile.empiler(1)
    pile.empiler(3)
    pile.empiler(7)
    assert pile.longueur() == 4
    assert pile.depiler() == 7
    pile.empiler(9)
    print(repr(pile))
    assert pile.depiler() == 9
    assert pile.depiler() == 3
    assert pile.depiler() == 1
    assert pile.depiler() == 5
    assert pile.est_vide()


if __name__ == "__main__":
    test()
```


