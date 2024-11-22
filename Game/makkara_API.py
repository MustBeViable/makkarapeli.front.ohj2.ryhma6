from flask import Flask, request, Response
from flask_cors import CORS
import json
from Game.airport_selection_function import airportselection

app = Flask(__name__)

@app.route('/airport/<ide>')
def flight(ide):
    vastaus = airportselection(ide)
    return vastaus


CORS(app)

'''@app.route('/airport/<ide>')
def flight(ide):
    vastaus = airportselection(ide)
    return vastaus

CORS(app)'''

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)