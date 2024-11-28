from flask import Flask
from flask_cors import CORS
from Game.python.airport_selection_function import airportselection
from Game.python.garbage_can import garbage_can

app = Flask(__name__)

@app.route('/airport/<ide>')

def flight(ide):
    vastaus = airportselection(ide)
    return vastaus

@app.route('/garbage/<ide>')

def carbage(ide):
    vastaus = garbage_can(ide)
    return vastaus



CORS(app)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)