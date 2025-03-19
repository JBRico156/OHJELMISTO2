"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
kasvattaa kuljetun matkan lukemaan 2090 km."""


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kuljettu_matka):
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


    def kulje(self, aika):
        kuljettu =  aika * self.nopeus
        Auto.kuljettu_matka += kuljettu


Auto = Auto("ABC-123", 142, nopeus = 0, kuljettu_matka = 0)


Auto.kiihdytä(50)
print(f"{Auto.nopeus}km/h")
Auto.kulje(5)
print(f"{Auto.kuljettu_matka}km")





