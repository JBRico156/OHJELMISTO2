
"""Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja
kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton
kaikki ominaisuudet."""


class Auto:

    Tehty = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka


Auto = Auto("ABC-123", "142 km/h")

print (f"Auton rekisteritunnus: {Auto.rekisteritunnus}, huippunopeus: {Auto.huippunopeus}, nykyinen nopeus: {Auto.nopeus}, kuljettu matka: {Auto.kuljettu_matka}" )






