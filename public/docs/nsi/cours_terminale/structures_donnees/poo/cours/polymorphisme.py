class Animal:
    """
    Classe de base `Animal` dont les autres animaux héritent.
    """

    def __init__(self, name):
        self.name = name

    def info(self):
        """Affiche une description générique"""
        print(f"je suis {self.name}")

    def move(self):
        """Affiche une action"""
        print("je bouge ...")


class Cat(Animal):
    """
    `Cat` hérite de `Animal`

    Dispose d'un constructeur particulier :
    """

    def __init__(self, name: str, age: int, taille: int):
        # on appelle le constructeur de la classe parente avec les parmaètres par défaut
        super().__init__(name)

        self.age = age
        self.taille = taille

    def info(self):
        """Redéfinition de la méthode."""
        print("je suis {self.name}")
        print(f" age {self.age}")
        print(f" taille {self.taille}")


def exemple():
    tom = Cat("Tom", 3, 20)
    # C'est la méthode de `Cat` qui est appelée
    tom.info()
    # Les instances de Cat disposent aussi de la méthode move
    tom.move()


exemple()
