
"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi
metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi
päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään
haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen."""



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

h = Hissi(15)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)



