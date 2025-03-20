

"""Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja
autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

    -tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
     kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
    -tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
    -kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
     Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen
auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa
tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne
tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt."""

import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        kuljettu = aika * self.nopeus
        self.kuljettu_matka += kuljettu

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistuvat_autot = osallistuvat_autot
        self.kulunut_aika = 0

    def tunti_kuluu(self):
        while not self.kilpailu_ohi():
            for auto in self.osallistuvat_autot:
                muutos1 = random.randint(-10, 15)
                auto.kiihdytä(muutos1)

            for auto in self.osallistuvat_autot:
                auto.kulje(1)
            self.kulunut_aika += 1
            if self.kulunut_aika % 10 == 0:
                self.tulosta_tilanne()
        self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for auto in self.osallistuvat_autot:
            print(f"Auton rekisteri: {auto.rekisteritunnus}")
            print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
            print(f"Auton nopeus: {auto.nopeus} km/h")
            print(f"Kuljettu matka: {auto.kuljettu_matka:.2f} km")
            print(" ")

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.kilpailun_pituus for auto in self.osallistuvat_autot)

osallistuvat_autot = []
for i in range(1, 11):
    alku_nopeus = random.randint(100, 200)
    rekisteri = str(i)
    Kilpa_Auto = Auto("ABC-" + rekisteri, alku_nopeus)
    osallistuvat_autot.append(Kilpa_Auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, osallistuvat_autot)
kilpailu.tunti_kuluu()
print("Kilpailu jatkuu!\n")
kilpailu.tulosta_tilanne()
print("Kilpailu on päättynyt!")


