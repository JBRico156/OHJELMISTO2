
"""Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää
rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti."""


import json

import requests


pyyntö = "https://api.chucknorris.io/jokes/random"
try:

    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
