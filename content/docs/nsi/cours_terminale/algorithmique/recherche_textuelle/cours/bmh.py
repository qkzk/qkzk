__title__ = "Algorithme de Boyer-Moore-Horspool"
__author__ = "qkzk"
__date__ = "2020/03/14"
from string import ascii_lowercase as lettres

__doc__ = """
titre:  {0}
auteur: {1}
date:   {2}

Implémentation de la version présentée dans Éléments d'algorithmique
    par Beauquier Bestel Chrétienne

[pdf](http://www-igm.univ-mlv.fr/~berstel/Elements/Elements.pdf)

L'algorithme de BMH est une simplification de l'algorithme complet
de Boyer Moore.

Il se révèle néanmoins efficace parce qu'il limite déjà considérablement
le nombre de comparaison.

L'implémentation ci-dessous est une simple transcription en Python de
l'algorithme présenté.

La seule difficulté réside en le changement d'indice à opérer.

Un jeu de tests est ajouté ainsi qu'un mode présentation qui permet
d'afficher les décalages succéssifs.


""".format(
    __title__, __author__, __date__
)


def derniere_occurence(motif, caracteres=None):
    """
    Retourne un dictionnaire des dernières occurences pour
    un motif donné
    chaque lettre parmi les lettres choisies se voit attribuée la distance
    jusqu'à sa dernière apparition dans le motif.
    Si elle n'apparait pas dans le motif, la valeur est la longueur du motif

    @param motif: (str)
    @param caracteres: (str) chaîne contenant les caracteres acceptés
    @return: (dict) le dictionnaire des dernières occurences
    """
    if caracteres is None:
        caracteres = lettres
    taille_motif = len(motif)
    dict_derniere_occurence = {lettre: taille_motif for lettre in caracteres}
    for i in range(taille_motif - 1):
        dict_derniere_occurence[motif[i]] = taille_motif - 1 - i
    return dict_derniere_occurence


def boyer_moore_horspool(motif, texte, caracteres=None, verbose=False):
    """
    Retourne le tableau des occurences du motif dans le texte.
    Une occurence est un indice à partir du quel on trouve le motif dans le
    texte
    Utilise l'algorithme de Boyer-Moore-Horspool
    @param motif, texte: (str)
    @param caracteres: (str) chaîne contenant les caracteres acceptés
    @param verbose: (bool) si vrai, on affiche les étapes successivess
    @return: (list) liste d'entiers
    """
    # si aucune table de caracteres n'est fournie, on utilise les lettres
    # minuscules
    if verbose:
        print(
            """
        Boyer-Moore-Horspool

Recherche du motif {}
dans le texte      {}
        """.format(
                motif, texte
            )
        )
    if caracteres is None:
        caracteres = lettres
    # on génère le dictionnaire des dernières occurences
    dict_derniere_occurence = derniere_occurence(motif, caracteres=caracteres)
    if verbose:
        print(dict_derniere_occurence, "\n\n")

    taille_motif = len(motif)
    taille_texte = len(texte)
    occurences = []  # contiendra les occurences rencontrées

    j = 0  # on commence au dernier caractère du motif
    while j <= taille_texte - taille_motif:  # tant qu'on n'a pas parcouru le texte
        if verbose:
            print(texte)
            print("." * j + motif)
        i = taille_motif - 1  # on initialise à la position finale du motif
        while i >= 0 and texte[j + i] == motif[i]:
            # tant qu'il y a correspondance ou qu'on n'a pas fini
            i -= 1  # on recule d'un caractere
        if i == -1:
            # arrivé à 0, toutes les lettres correspondent et on a trouve
            occurences.append(j)  # attention, j compte depuis la fin
            j += 1  # on cherche à la position suivante
            if verbose:
                print("OCCURENCE position {}\n\n".format(j))
        else:
            # ici on peut avancer de la distance correspondant à la lettre
            indice_non_corresp = j + i
            avancer = dict_derniere_occurence[texte[indice_non_corresp]]

            if verbose:
                print(" " * ((indice_non_corresp)) + "^")
                print(
                    "Non correspondance entre {} et {} position {} - avancer de {}".format(
                        texte[indice_non_corresp],
                        motif[i - 1],
                        indice_non_corresp,
                        avancer,
                    )
                )
                # input()
                print()
                print()
            j += avancer
    return occurences


def presenter():
    """
    Présente l'algorithme dans la console
    """
    texte = "aabbbababacaabbabaaababab"
    motif = "aababab"
    verbose = True
    boyer_moore_horspool(motif, texte, verbose=verbose, caracteres="abc")

    texte = "lunalinaluna" * 2
    motif = "alun"
    verbose = True
    boyer_moore_horspool(motif, texte, verbose=verbose, caracteres="ailnu")


def tester():
    """
    Teste la validité de l'implémentation.
    Lève une exception si le résultat ne correspond pas.
    """
    motifs_textes = [
        ("aababab", "aabbbababacaabbabaaababab", 1),
        ("alun", "lunalinaluna" * 2, 3),
    ]
    for motif, texte, nb_solution in motifs_textes:
        bmh = boyer_moore_horspool(motif, texte, verbose=False)
        for indice in bmh:
            assert len(bmh) == nb_solution, bmh
            assert texte[indice : indice + len(motif)] == motif


if __name__ == "__main__":
    tester()
    presenter()
