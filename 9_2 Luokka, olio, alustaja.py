"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden
muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion
nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää."""

class Auto:

    Tehty = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, kiihdytys):
        self.nopeus += kiihdytys
        if kiihdytys <= 0 or kiihdytys > 0:
            if self.nopeus < 0:
                self.nopeus = 0
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
        return

Auto = Auto("ABC-123", 142)

Auto.kiihdytä(30)
Auto.kiihdytä(70)
Auto.kiihdytä(50)
print(f"{Auto.nopeus}km/h")
Auto.kiihdytä(-200)
print(f"{Auto.nopeus}km/h")





