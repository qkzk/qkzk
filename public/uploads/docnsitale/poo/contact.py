class Contact:
    def __init__(self, nom, prenom, telephone):
        self.__nom = nom
        self.__prenom = prenom
        self.__telephone = telephone

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_telephone(self):
        return self.__telephone

    @classmethod
    def depuis_dictionnaire(cls, dictionnaire):
        nom = dictionnaire["nom"]
        prenom = dictionnaire["prenom"]
        telephone = dictionnaire["telephone"]
        return cls(nom, prenom, telephone)

    def __repr__(self):
        return f'Contact("{self.get_nom()}", "{self.get_prenom()}", "{self.get_telephone()}")'


def exemple():
    robert = Contact("Duchmol", "Robert", "0678901234")   # directement

    dict_martin = {"nom": "Martin",
                   "prenom": "Patrick", "telephone": "0789012345"}
    martin = Contact.depuis_dictionnaire(dict_martin)

    assert isinstance(martin, Contact)
    assert martin.get_prenom() == "Patrick"

    print(robert)
    print(martin)
    print(dir(martin))


if __name__ == "__main__":
    exemple()
