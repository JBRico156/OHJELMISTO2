"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2"
jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

    Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
    Tämä tehdään kutsumalla kiihdytä-metodia.
    Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton
kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""

import random

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
        self.kuljettu_matka += kuljettu

matkat = [0]
autot = []
for i in range (1, 11):
    alku_nopeus = random.randint(100, 200)
    rekisteri = str(i)
    Kilpa_Auto = Auto("ABC-"+rekisteri, alku_nopeus, nopeus = 0, kuljettu_matka = 0)
    autot.append(Kilpa_Auto)

while max(matkat) < 10000:
    for auto in autot:
        muutos1 = random.randint(-10, 15)
        auto.kiihdytä(muutos1)
    for auto in autot:
        auto.kulje(1)
    for auto in autot:
        matkat.append(auto.kuljettu_matka)

for auto in autot:
    print(f"Auton rekisteri: {auto.rekisteritunnus}")
    print(f"Auton huippunopeus: {auto.huippunopeus}km/h")
    print(f"Auton nopeus: {auto.nopeus}km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka}km")
    print(" ")
