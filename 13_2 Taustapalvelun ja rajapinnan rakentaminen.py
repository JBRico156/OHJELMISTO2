
"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}."""

from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jan',
         password='KevytSalasana2',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    try:
        sql = f"SELECT name, ident, iso_country, municipality FROM airport where ident='{ICAO}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        Name = tulos[0][0]
        ICAOKOODI = tulos[0][1]
        Municipality = tulos[0][3]

        tilakoodi = 200
        vastaus = {"ICAO": ICAOKOODI,
                   "Name": Name,
                   "Municipality": Municipality
                   }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO-koodi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen osoite"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
