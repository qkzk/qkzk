__doc__ = '''
Dictionnaire en Python

Que peut-on faire avec un dictionnaire ?
'''

# 1. Créer un dictionnaire :

# vide

d1 = {}
d2 = dict()

# Avec des clés et valeurs

d3 = {'cle': 'valeur'}
# avec le nom de la classe, on doit passer un tuple contenant des tuples
d4 = dict((('cle1', 'valeur1'), ('cle2', 'valeur2')))

assert d4['cle1'] == 'valeur1'
assert d4['cle2'] == 'valeur2'

# 2. Accéder à un élément

assert d3['cle'] == 'valeur'
assert d3.get('cle') == 'valeur'
# si la clé n'est pas présente, la méthode get renvoie None
assert d3.get('bonjour') is None

try:
    d3["bonjour"]
except KeyError as e:
    # si la clé n'est pas présente, la notation d[cle] lève une exception KeyError"
    pass

# 3. ajouter un élément

d3["bonjour"] = "aurevoir"

# la notation d[cle] = valeur appelle la méthode d.__setitem__(cle, valeur)
d3.__setitem__("1", "2")

assert d3["bonjour"] == "aurevoir"
# la notation d[cle] appelle d.__getitem__(cle)
assert d3.__getitem__("1") == "2"

# itérer sans préciser : sur les clés
print()
for cle in d3:
    print("clé:", cle, " - valeur: ", d3[cle])

# itérer sur les clés
print()
for cle in d3.keys():
    print("clé:", cle, " - valeur: ", d3[cle])

# itérer sur les valeurs
print()
for valeur in d3.values():
    print("valeur: ", valeur)

# itérer sur les couples clés, valeurs
print()
for cle, valeur in d3.items():
    print("clé:", cle, " - valeur: ", valeur)

# 4. Contient

assert "1" in d3
assert not 1 in d3

# 5. Longueur, comparaison

assert len(d4) == 2
assert d4 == {'cle1': 'valeur1', 'cle2': 'valeur2'}

# 6. Nettoyer, copier

d4.clear()  # vide le dictionnaire
assert d4 == {}

d5 = d3.copy()

assert d3 == d5      # ils contiennent les mêmes éléments...
assert d3 is not d5  # mais sont des objets différents en mémoire

print("d3 et d5 sont des objets différents", id(d3), id(d5))

