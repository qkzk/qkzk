from random import randint


def nim():
    allumettes = 15
    while allumettes > 1:
        print(f"Il reste {allumettes} allumettes")
        a_retirer = int(input("Combien retirer (1, 2, 3) ? "))
        if a_retirer >= min(allumettes, 4) or a_retirer <= 0:
            continue
        allumettes -= a_retirer
        print(f"Il reste {allumettes} allumettes.")
        if allumettes == 1:
            print("Bravo, vous avez gagné !\n")
            return
        print("L'ordinateur joue !")
        ordi = randint(1, min(3, allumettes - 1))
        print(f"L'ordinateur retire {ordi} allumettes")
        if allumettes == 1:
            print("Dommage, l'ordinateur a gagné !\n")
            return


if __name__ == "__main__":
    while True:
        nim()
