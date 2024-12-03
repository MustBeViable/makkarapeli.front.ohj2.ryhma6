from wsgiref.util import request_uri

from flask import Flask
from flask_cors import CORS
from Game.python.airport_selection_function import airportselection, current_coordinates
from Game.python.garbage_can import garbage_can, finnair_personnel, money_from_garbage, robber, hole_in_charge
from Game.python.search_of_kolo import kolo_search
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.makkara_sql_haku import search_makkara, search_makkara_id
from Game.python.sql_querys.money_function import update_player_money, fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import update_player_location, fetch_player_location
from Game.python.doubling_machine import tuplaus
from Game.python.game_texts import sausage_price
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch
from Game.python.sql_querys.top_5_score_fetch_query import print_all_players_top
from Game.python.taxfree import tax_free
app = Flask(__name__)

airports = {}

money_to_be_doubled = {}

times_doubled = [0,1]

@app.route('/airport/<ide>')
#Gives dictionaries within dictionary of 20 randomized airports based on location to user
def airport(ide):
    result = airportselection(ide)
    airports[ide] = result
    return result

@app.route('/airport_selected/<ide>/<airport_num>')
#Get users selected airport (frond end checks if he can afford) and updates player location. Also takes the fee here.
#User cannot change the values (i.e. prices), list is saved here. Returned result is just meant for checking does all go
#as planned
def airport_selected(ide, airport_num):
    result = airports[ide][airport_num]
    ariport_icao = result['ident']
    price = result['price']
    current_money = fetch_player_money(1)['money']
    spend = int(current_money) - int(price)
    update_player_money(spend, ide)
    update_player_location(ide, ariport_icao)
    return result

@app.route('/garbage/<ide>')
#when money found works now returns dictionary money as key and value is the random amount
def garbage(ide):
    value = garbage_can()
    if value == 'found_money':
        result = money_from_garbage()
        money_to_be_doubled[ide] = result
        #this check global list to be empty. List range is the logic for the doubling.
        if len(times_doubled) > 0:
            for i in range(len(times_doubled)):
                times_doubled.pop()
                i += 1
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

@app.route('/doubling/<ide>')

def doubling(ide):
    doubled_money = int(money_to_be_doubled[ide]['money'])
    print(doubled_money)
    times = len(times_doubled)
    print(times)
    new_money = tuplaus(doubled_money, times)
    money_to_be_doubled[ide]['money'] = new_money
    times_doubled.append(1)
    if new_money == 0:
        result = {'result': 'Hävisit tuplauksen'}
        return result
    else:
        result = {'result': new_money}
        return result

@app.route('/taxfree/<ide>')

def taxfree(ide):
    price = sausage_price
    result = {'value': price}
    result['name'] = search_makkara(ide)['name']
    return result

@app.route('/taxfree_buy/<ide>')
def taxfree_buy(ide):
    result = tax_free(fetch_player_money(ide)['money'], search_makkara_id(ide), ide)
    return result


@app.route('/hole_search/<ide>/<transportation>')
#Define variables in search_of_kolo function based on how frontend gives us info about transportation.
#Returns dictionary like: {'makkara': 'found'}
def hole_search(ide, transportation):
    result = kolo_search(ide, transportation)
    return result

@app.route('/player_money/<ide>')
#Return a dictionary like this {'money': '400'}.
def player_money(ide):
    result = fetch_player_money(ide)
    return result

@app.route('/player_location/<ide>')
#Returns player location as lat and long like this {'lattitude': '10', 'longitude': '2'}.
def player_location(ide):
    location = fetch_player_location(ide)['player_location']
    array = current_coordinates(location)
    result = {'lattitude': array[0][0], 'longitude': array[0][1]}
    return result

@app.route('/player_makkaras/<ide>')
def player_makkaras(ide):
    result = {'makkara_count': len(fetch_player_makkaras(ide))}
    return result

@app.route('/player_score/<ide>')
def player_score(ide):
    result = {'score': player_score_fetch(ide)}
    return result

@app.route('/top_5_all/')
def top_5():
    return print_all_players_top()


CORS(app)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)