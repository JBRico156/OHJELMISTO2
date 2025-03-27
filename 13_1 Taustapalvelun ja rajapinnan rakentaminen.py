
"""Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}."""

from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    try:
        luku = int(luku)

        isprime = ""

        if luku <= 1:
            isprime = "false"
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                isprime = "false"
            else:
                isprime = "true"

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku": luku,
            "isprime": isprime

        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
