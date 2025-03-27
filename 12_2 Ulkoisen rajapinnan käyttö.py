
"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""


import json
import requests

api_key = "TÄHÄN API KOODI"
hakusana = input("Anna hakusana: ")

pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}&units=metric"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()

        lämpö = {json_vastaus['main']['temp']}
        lämpölista = [num for num in lämpö]
        kelvin = lämpölista[0] + 273.15

        print(f"Kaupunki: {json_vastaus['name']}")
        print(f"Säätila: {json_vastaus['weather'][0]['description']}")
        print(f"Lämpötila: {json_vastaus['main']['temp']} °C")
        print(f"Lämpötila: {kelvin} °K")
    else:
        print("Kaupungin tietoja ei löytynyt.")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa:", e)
