
"""Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit
pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys."""

class Hissi:

    def __init__(self, ylin = int):
        self.alin = 0
        self.sijainti = self.alin
        self.ylin = ylin

    def kerros_ylös(self, kerros):
        while self.sijainti < kerros:
            self.sijainti += 1
        print(f"Hissi on kerroksessa {self.sijainti}")

    def kerros_alas(self, kerros):
        while self.sijainti > kerros:
            self.sijainti -= 1
        print(f"Hissi on kerroksessa {self.sijainti}")

    def siirry_kerrokseen(self, siirry):
        if self.sijainti < siirry:
            while self.sijainti < siirry:
                Hissi.kerros_ylös(self, siirry)
            return
        if self.sijainti > siirry:
            while self.sijainti > siirry:
                Hissi.kerros_alas(self, 0)


class Talo:

    def __init__(self, alin_k = int, ylin_k = int, hissit = int):
        self.alin_k = alin_k
        self.hissit = hissit
        self.ylin_k = ylin_k
        self.talot = []
        luku = 0
        while luku < hissit:
            self.talot.append(Hissi(ylin_k))
            luku += 1

    def aja_hissiä(self, kohde, hissinumero):
        hissinumero -= 1
        matkustushissi = self.talot[hissinumero]
        matkustushissi.siirry_kerrokseen(kohde)

    def palohälytys(self):
        print("Palohälytys!")
        for hissi in self.talot:
            hissi.kerros_alas(0)

T = Talo(0, 10, 4)
T.aja_hissiä(4, 1)
T.aja_hissiä(7, 2)
T.aja_hissiä(2, 3)
T.aja_hissiä(10, 4)
print(" ")
T.palohälytys()








