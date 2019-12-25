#add
def add(a,b):
    """
    >>> add(3,5)
    8
    >>> add(3,0)
    3
    >>> add(0,3)
    3
    """
    if (b == 0):
        return a
    else:
        return add(a+1,b-1)


# mult
def mult(a,b):
    """
    >>> mult(2,3)
    6
    >>> mult(2,0)
    0
    >>> mult(2,1)
    2
    """
    if (b == 0):
        return 0
    elif (b == 1):
        return a
    else:
        return a + mult(a, b-1)


# power
def power(a,b):
    """
    >>> power(2,3)
    8
    >>> power(2,0)
    1
    >>> power(3,1)
    3
    """
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a,b-1)


# algorithme d'Euclide
def euclide(a,b):
    """
    >>> euclide(15,3)
    3
    >>> euclide(15,7)
    1
    >>> euclide(32,56)
    8
    """
    if b == 0:
        return a
    else:
        return euclide (b, a % b)


# algorithme géométrique - Coloriage

# on suppose que sont définies :
def get_color(x,y):
    pass
def set_color(x,y,color):
    pass
BLACK = 'en noir'
WHITE = 'en blanc'
RED = 'en rouge'

def coloriage(x,y):
    # cas de base : point de la courbe  ou déjà colorié
    if get_color(x,y) == BLACK or get_color(x,y) == RED:
        pass
    else:
        # coloriage du point
        set_color(x,y,RED)
        # coloriage des 4 voisins
        coloriage(x+1,y)
        coloriage(x-1,y)
        coloriage(x,y+1)
        coloriage(x,y-1)


# palindrome
def is_palindrome(word):
    """
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("elle")
    True
    >>> is_palindrome("timoleon")
    False
    """
    l = len(word)
    if l <= 1:
        return True
    elif word[0] != word[l - 1]:
        return False
    else:
        return is_palindrome(word[1:l-1])


# Permutations des caractères
def list_permut_string(word):
    """
    return the list of all possible permutations of letters in word

    :param word: a word
    :type word: string
    :returns: *(list(string))* -- the list of all possible permutations of letters in word
    >>> list_permut_string("abc") == ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    True
    """
    if len(word) == 0:
        return [word]
    else:
        # insert the first letter of word in all the possible permutations of other letters of word
        return insert_letter_in_list(word[0], list_permut_string(word[1:]))

def insert_letter_in_list(letter,word_list):
    """
    return the list obtained by insertion of letter in all possible positions of words in word_list

    :param letter: the letter to insert
    :type letter: string of size 1
    :param word_list: a list of words
    :type word_list: list(string)
    :returns: *(list(string))* -- the list obtained by insertion of letter in all possible positions of words in word_list
    """
    if len(word_list) == 1:
        return insert_letter_in_word(letter,word_list[0])
    else:
        return insert_letter_in_word(letter,word_list[0]) + insert_letter_in_list(letter,word_list[1:])

def insert_letter_in_word(letter,word):
    """
    returns the list obtained by insertion of letter in all possible positions of word
    :param letter: the letter to insert
    :type letter: string of size 1
    :param word: a word
    :type word: string
    :returns: *(list(string))* -- the list obtained by insertion of letter in all possible positions of word
    """
    result = []
    l = len(word)
    for i in range(l+1):
        result.append(word[0:i]+letter+word[i:l])
    return result


# Conversion des nombres romains
VALEUR_ROMAIN = { 'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
def romain_to_arabe(nombre):
    '''
    >>> romain_to_arabe('X') ==  10
    True
    >>> romain_to_arabe('XCI') == 91
    True
    >>> romain_to_arabe('MMXIX') == 2019
    True
    '''
    if nombre == '':
        return 0
    if len(nombre) == 1:
        return VALEUR_ROMAIN[nombre[0]]
    elif VALEUR_ROMAIN[nombre[0]] < VALEUR_ROMAIN[nombre[1]]:
        return VALEUR_ROMAIN[nombre[1]] - VALEUR_ROMAIN[nombre[0]]\
            + romain_to_arabe(nombre[2:])
    else:
        return VALEUR_ROMAIN[nombre[0]] + romain_to_arabe(nombre[1:])

# version récursive terminale
def romain_to_arabe_term(nombre, acc = 0):
    '''
    >>> romain_to_arabe_term('X') ==  10
    True
    >>> romain_to_arabe_term('XCI') == 91
    True
    >>> romain_to_arabe_term('MMXIX') == 2019
    True
    '''
    if nombre == '':
        return acc
    if len(nombre) == 1:
        return acc + VALEUR_ROMAIN[nombre[0]]
    elif VALEUR_ROMAIN[nombre[0]] < VALEUR_ROMAIN[nombre[1]]:
        return romain_to_arabe_term(nombre[2:] , acc + VALEUR_ROMAIN[nombre[1]] - VALEUR_ROMAIN[nombre[0]])
    else:
        return romain_to_arabe_term(nombre[1:], acc + VALEUR_ROMAIN[nombre[0]] )



# Algorithmes sur les listes récursives

# on suppose donc que l'on ne dispose que des fonctions
LISTE_VIDE = []
def cree_liste(tete, reste):
    return [tete] + reste
def tete(liste):
    return liste[0]
def reste(liste):
    return liste[1:]
# on peut donc définir le prédicat
def est_vide(liste):
    return liste == LISTE_VIDE


# somme des éléments
def sum_list(number_list):
    """
    >>> sum_list([1,2,3]) == 6
    True
    """
    if est_vide(number_list) :
        return 0
    else:
        return tete(number_list) + sum_list(reste(number_list))


# dernier élément
def last(liste):
    """
    >>> last([1,2,3])  == 3
    True
    """
    if est_vide(reste(liste)):
        return tete(liste)
    else:
        return last(reste(liste))


# concaténation de listes
def concat(liste1, liste2):
    '''
    >>> l1 = [1,2]
    >>> l2 = [3,4]
    >>> concat(l1,l2) == [1,2,3,4]
    True
    >>> concat(LISTE_VIDE,l1) == [1,2]
    True
    >>> concat(l1, LISTE_VIDE) == [1,2]
    True
    '''
    if est_vide(liste1):
        return liste2
    else:
        return cree_liste(tete(liste1),
                          concat(reste(liste1),liste2))


# appliquer une fonction à tous les éléments d'une liste
def map(f, liste):
    '''
    >>> map(len, ['a', '', 'abc']) == [ 1, 0, 3 ]
    True
    '''
    if est_vide(liste):
        return LISTE_VIDE
    else:
        return cree_liste( f(tete(liste)),
                           map(f, reste(liste) ) )


# mélange de deux listes
def shuffle(liste1, liste2):
    '''
    >>> shuffle([1,5,3],[8,2,6,9,7]) == [1,8,5,2,3,6,9,7]
    True
    >>> shuffle([1,5,3,9,7],[8,2,6]) == [1,8,5,2,3,6,9,7]
    True
    '''
    if est_vide(liste1):
        return liste2
    elif est_vide(liste2):
        return liste1
    else:
        tete1 = tete(liste1)
        tete2 = tete(liste2)
        reste_shuffle = shuffle(reste(liste1), reste(liste2))
        return cree_liste( tete1,
                           cree_liste( tete2, reste_shuffle ) )


# tours de Hanoi
'''
idée récursive :
pour déplacer n disques d'une tour de départ vers une tour d'arrivée :
il faut déplacer (n-1) disques de départ vers une 3ème tour,
on peut ensuite déplacer 1 seul disque de départ vers arrivée (qui est vide donc c'est possible)
il reste alors à déplacer (n-1) disques de la 3ème tour vers la tour d'arrivée.
Pour déplacer n disques il faut donc pouvoir déplacer (n-1) disques.
Quand on a qu'un seul disque on sait le déplacer sans problème, c'est le cas de base.
'''


'''
On représente chaque disque par un nombre correspondant à sa taille
On représente les tours par des listes de disques, l'ordre de la liste correspond à l'empilement des disques de bas en haut.
Les trois tours sont rangés dans une liste.
'''
def hanoi(n):
    '''
    Résoud le problème de Hanoï pour n disque
    @param {int} le nombre de disqus initial
    '''
    tours = init(n)
    deplacer_n_disques(n, 0 , 2, tours)

def init(n):
    '''
    crée la liste des 3 tours, la première contient les n disques empilés du plus grand au plus petit
    '''
    return [ [(n-i) for i in range(n) ] , [] , [] ]

def deplacer_n_disques(n, depart, arrivee, tours):
    '''
    deplace n disques de la tour depart à la tour arrivee (en rspectant les contraintes de Hanoï)
    les tours sont mémomriées dans tours et repérées par leur indice (depart et arrivee)
    '''
    if n == 1 :
        deplacer_1_disque(depart, arrivee, tours)
    else :
        intermediaire = troisieme_tour(depart, arrivee)
        deplacer_n_disques(n-1, depart, intermediaire, tours)
        deplacer_1_disque(depart, arrivee, tours)
        deplacer_n_disques(n-1, intermediaire, arrivee, tours)

def troisieme_tour(premiere, deuxieme):
    '''
    fournit l'indice de la troisieme tour connaissant les deux autres indices
    '''
    return 3 - (premiere+deuxieme)

def deplacer_1_disque(depart, arrivee, tours):
    '''
    deplace 1 seul disque de la tour depart à la tour arrivee
    les tours sont mémomriées dans tours et repérées par leur indice (depart et arrivee)
    affiche le déplacement effectué
    '''
    disque = depiler(tours[depart])
    empiler(tours[arrivee], disque)
    affiche_deplacemene(disque, depart, arrivee, tours)

def affiche_deplacemene(disque, depart, arrivee, tours):
    '''
    affichage du déplacement du disque
    '''
    print("disque {0} : {1} -> {2} | {3[0]} - {3[1]} - {3[2]} ".format(disque, depart+1, arrivee+1, tours))

def depiler(tour):
    '''
    retire et renvoie le disque au sommet de la tour, la tour est modifiée
    '''
    return tour.pop()
def empiler(tour, disque):
    '''
    ajoute le disque fourni au sommet de la tour, la tour est modifiée
    '''
    tour.append(disque)

# pour essayer :
#hanoi(4)




# tri par insertion
'''
trier par insertion c'est insérer le premier élément de  la liste dans la liste des autres éléments triée
'''
def inserer(e, liste_triee):
    '''
    '''
    if est_vide(liste_triee) :
        return [e]
    elif e < tete(liste_triee):
        return [e] + liste_triee
    else:
        return [liste_triee[0]] + inserer(e, reste(liste_triee))

def tri_insertion(liste):
    '''
    >>> tri_insertion([2,1,4,3]) == [1,2,3,4]
    True
    '''
    if est_vide(liste):
        return liste
    else:
        return inserer(tete(liste),
                       tri_insertion(reste(liste)))


# liste permutations (identique aux chaines évidemment)

def list_permut_list(list):
    """
    return the list of all possible permutations of elements in list

    :param list: a list
    :type list: list
    :returns: *(list(list))* -- the list of all possible permutations of elements in list
    >>> list_permut_list(["tim", "o", "leon"]) == [['tim', 'o', 'leon'], ['o', 'tim', 'leon'], ['o', 'leon', 'tim'], ['tim', 'leon', 'o'], ['leon', 'tim', 'o'], ['leon', 'o', 'tim']]
    True
    """
    if len(list) == 0:
        return [list]
    else:
        # insert the first element of list in all the possible permutations of other lists of list
        return insert_element_in_all_lists(list[0], list_permut_list(list[1:]))


def insert_element_in_all_lists(element,list_list):
    """
    return the list obtained by insertion of element in all possible positions of lists in list_list

    :param element: the element to insert
    :type element: any
    :param list_list: a list of lists
    :type list_list: list(list)
    :returns: *(list(list))* -- the list obtained by insertion of element in all possible positions of lists in list_list
    """
    if len(list_list) == 1:
        return insert_element_in_list(element,list_list[0])
    else:
        return insert_element_in_list(element,list_list[0]) + insert_element_in_all_lists(element,list_list[1:])

def insert_element_in_list(element,list):
    """
    returns the list obtained by insertion of element in all possible positions of list
    :param element: the element to insert
    :type element: any
    :param list: a list
    :type list: list
    :returns: *(list(list))* -- the list obtained by insertion of element in all possible positions of list
    """
    result = []
    l = len(list)
    for i in range(l+1):
        result.append(list[0:i]+[element]+list[i:l])
    return result



# rencontres de championnat
def rencontres(joueurs):
    '''
    >>> rencontres([1,2,3,4]) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    True
    '''
    if len(joueurs) <= 1:
        return []
    else:
        rencontres_avec_premier_joueur = un_contre_les_autres(joueurs[0], joueurs[1:])
        rencontre_des_autres_entre_eux = rencontres(joueurs[1:])
        return rencontres_avec_premier_joueur + rencontre_des_autres_entre_eux

def un_contre_les_autres(joueur, autres):
    '''
    renvoie la liste de tous les couples possibles de joueur avec chacune des éléments de autres
    >>> un_contre_les_autres(1,[2,3,4]) == [(1, 2), (1, 3), (1, 4)]
    True
    '''
    return [ (joueur, adversaire) for adversaire in autres ]


# OURS CAGE

import dico


def distance(word1,word2):
    """
    return the distance between two given words, ie. the number of different characters.
    Positions of characters do not matter.
    @param {string} word1  a word
    @param {string} word2 a word
    @return {int}  number of different charcaters between two words
    CU : words must be of same length
    >>> distance("bonjour", "bonjour")
    0
    >>> distance("bonjour", "bbojura")
    2
    >>> distance("bonjour", "boajour")
    1
    >>> distance("bonjour", "xxxxxxx")
    7
    """
    if len(word1) != len(word2):
        raise Exception("words must be of same length")
    word1Char = list(word1)
    word2Char = list(word2)
    word1Char.sort()
    word2Char.sort()
    index_in_word1 = 0
    index_in_word2 = 0
    max_len = len(word1)
    result = max_len
    while index_in_word1 < max_len  and index_in_word2 < max_len :
        if word1Char[index_in_word1] < word2Char[index_in_word2]:
            index_in_word1 = index_in_word1 + 1
        elif word2Char[index_in_word2] < word1Char[index_in_word1]:
            index_in_word2 = index_in_word2 + 1
        elif word1Char[index_in_word1] == word2Char[index_in_word2]:
            index_in_word2 = index_in_word2 + 1
            index_in_word1 = index_in_word1 + 1
            result = result - 1
    return result

def neighbourList(word):
    """
    return the list of words in DICO  that are at distance 1 from  word
    @param {string}  word : the word
    @return {list(string)} list  of words from DICO at distance 1 from word
    """
    result = []
    for element in dico.DICO:
        if distance(word,element) == 1:
            result.append(element)
    return result

'''
idée récursive :
pour [trouver un chemin] de start vers end
on cherche à faire un pas, vers un des voisins de start,
    il reste alors à [trouver un chemin] de ce voisin vers end,   ( <= récursivité ici)
        sans repasser par un mot déjà rencontré
        si on atteint end, on a trouvé un chemin
        sinon si on ne trouve par de tel chemin (plus de mot) on est dans un impasse
    il faut alors essayer avec un autre voisin
    s'il n'y a plus de voisin candidat, alors on n'a pas de solution
'''
def solve(start,end):
    """
    """
    def _solve(end,seen,candidates):
        """
        cherche un chemin jusque end, seen sont les mots déjà rencontrés, candidates sont les successeurs possibles du mot courant
        @return {(boolean, list)} : première composante est False si pas de solution ,
                                si elle vaut True, la liste du chemin de résolution est dans la seconde composante
        """
        if candidates == []:
            return False, []
        elif end in candidates:
            return True, [end]
        else:
            start = candidates[0]
            seen.append(start)
            neighbours = neighbourList(start)
            nextCandidates = [ word for word in neighbours if not word in seen]
            success, solution = _solve(end, seen, nextCandidates)
            if success :
                return True, [start] + solution
            else:
                return _solve(end,seen,candidates[1:])

    status, liste = _solve(end,[],[start])
    if status:
        return liste
    else:
        return None

#print ( solve('ours', 'cage') )

#von koch
import turtle


def vonkoch(l,n):
    """
    """
    _init_turtle(-350,0)
    _draw_vonkoch(l,n)
    turtle.showturtle()

def vonkoch_flake(l,n):
    """
    """
    _init_turtle(-350,200)
    for _ in range(3):
        _draw_vonkoch(l,n)
        turtle.right(120)

def _init_turtle(x,y):
    """
    """
    turtle.speed("fastest")
    turtle.clearscreen()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.hideturtle()

def _draw_vonkoch(l,n):
    """
    """
    if n == 0:
        turtle.forward(l)
    else:
        _draw_vonkoch(l/3,n-1)
        turtle.left(60)
        _draw_vonkoch(l/3,n-1)
        turtle.right(120)
        _draw_vonkoch(l/3,n-1)
        turtle.left(60)
        _draw_vonkoch(l/3,n-1)


def test_von_koch(n):
    vonkoch_flake(300,n)
    turtle.exitonclick()
# pour tester
#test_von_koch(3)






if __name__ == '__main__':
    import doctest
    doctest.testmod ()

    test_von_koch(10)
