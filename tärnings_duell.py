from random import randint

class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.poäng = 0
        self.tärningresultat = 0


def kasta():
    return randint(1, 6)

def vinn_runda(resultat1, resultat2):
    if resultat1 > resultat2:
        spelare1.poäng += 1
        print(f"{spelare1.namn} fick en poäng")
    elif resultat1 < resultat2:
        spelare2.poäng += 1
        print(f"{spelare2.namn} fick en poäng")
    else:
        print("det blev lika")

spelare1 = Spelare("Anna")
spelare2 = Spelare("Erik")

spela = True

while spela:
    spelare1.tärningresultat = kasta()
    spelare2.tärningresultat = kasta()

    print(f"{spelare1.namn}: {spelare1.tärningresultat}")
    print(f"{spelare2.namn}: {spelare2.tärningresultat}")

    print("")

    vinn_runda(spelare1.tärningresultat, spelare2.tärningresultat)

    print("")

    if spelare1.poäng == 5:
        print(f"{spelare1.namn} vann!")
        spela = False
    elif spelare2.poäng == 5:
        print(f"{spelare2.namn} vann!")
        spela = False