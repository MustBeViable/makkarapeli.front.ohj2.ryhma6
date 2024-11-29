from wsgiref.util import request_uri

from flask import Flask
from flask_cors import CORS
from Game.python.airport_selection_function import airportselection
from Game.python.garbage_can import garbage_can, finnair_personnel, money_from_garbage, robber, hole_in_charge
from Game.python.sql_querys.money_function import update_player_money, fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import update_player_location, fetch_player_location
import json,tempfile
app = Flask(__name__)

airports = {}

@app.route('/airport/<ide>')
#Gives dictionaries within dictionary of 20 randomized airports based on location to user
def airport(ide):
    result = airportselection(ide)
    airports[ide] = result
    return result

@app.route('/garbage/<ide>')
#when money found works now returns dictionary money as key and value is the random amount
def garbage(ide):
    value = garbage_can()
    if value == 'found_money':
        result = money_from_garbage()
        return result
    elif value == 'hole_in_charge':
        result = hole_in_charge(ide)
        return result
    elif value == 'finnair_personnel':
        #check later how it will be implemented to frontend
        result = {'value': 'Finnair_personel happened'}
        return result
    elif value == 'robber':
        result = robber(ide)
        return result


@app.route('/finnair/<ide>/<answer>')

def finnair(ide, answer):
#Javascript need to check the player input. Only true state will go through (if check)
#Returns dictionary like this {'answer': 'Ei rahaa'}
    if answer == 'true':
        result = finnair_personnel(ide, answer)
        return result

@app.route('/airport_selected/<ide>/<airport_num>')
#Get users selected airport (frond end checks if he can afford) and updates player location. Also takes the fee here.
#User cannot change the values (ie. prices), list is saved here. Returned result is just meant for checking does all go
#as planned
def airport_selected(ide, airport_num):
    result = airports[ide][airport_num]
    ariport_icao = result['ident']
    price = result['price']
    spend = int(fetch_player_money(1)) - int(price)
    update_player_money(spend, ide)
    update_player_location(ide, ariport_icao)
    return result


CORS(app)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

'''    
    update_player_location(ide, icao)
    result = fetch_player_location(ide)
    
        tfile=result
    config = {}
    json.dump(config, tfile)'''