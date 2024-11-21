from flask import Flask, request, Response
import json
from Game.airport_selection_function import airportselection

app = Flask(__name__)



@app.route('/airport/<ide>')
def flight(ide):
    vastaus = airportselection(ide)
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)