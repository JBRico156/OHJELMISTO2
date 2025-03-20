
"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän
kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista
tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""

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


T = Talo(0, 10, 4)
T.aja_hissiä(4, 1)
T.aja_hissiä(7, 2)
T.aja_hissiä(2, 3)
T.aja_hissiä(10, 4)







