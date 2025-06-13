"""

def a():
    b()


def b():
    a()


a()
"""

"""

def inf():
    while True:
        yield 1


for x in inf():
    pass  # Boucle infinie sans "while"
"""

from itertools import count

for x in count():
    pass  # Pareil
