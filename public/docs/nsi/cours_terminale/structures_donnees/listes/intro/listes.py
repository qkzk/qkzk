class Liste:
    def __init__(self, *args):
        if len(args) == 0:
            self.__tete = None
            self.__queue = None
        else:
            self.__tete = args[0]
            self.__queue = args[1]

    def tete(self):
        return self.__tete

    def queue(self):
        return self.__queue

    def est_vide(self):
        return self.__tete is None and self.__queue is None

    def __len__(self):
        if self.est_vide():
            return 0
        return 1 + len(self.queue())

    def acceder(self, indice: int):
        if indice == 0:
            return self.tete()
        return self.queue.acceder(indice - 1)

    def __repr__(self):
        if self.est_vide():
            return "[ ]"
        return f"({self.tete()}, {self.queue()})"


def test():
    e = Liste()
    assert e.est_vide()
    assert len(e) == 0
    d = Liste("d", e)
    assert not d.est_vide()
    assert d.tete() == "d"
    assert d.queue() is e
    c = Liste("c", d)
    assert len(c) == 2
    b = Liste("b", c)
    a = Liste("a", b)
    assert len(a) == 4
    assert a.tete() == "a"
    assert a.queue().queue().queue() is d

    print(a)


if __name__ == "__main__":
    test()
