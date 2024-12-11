from Game.python.airport_selection_function import airportselection, current_coordinates
from Game.python.garbage_can import garbage_can, finnair_personnel, money_from_garbage, robber, hole_in_charge
from Game.python.search_of_kolo import kolo_search
from Game.python.sql_querys.country_code_for_flag import country_code_for_flag
from Game.python.sql_querys.fetch_player_makkaras import current_list_of_player_makkaras
from Game.python.sql_querys.game_logic_table import check_player_makkara_game, update_player_makkara_game
from Game.python.sql_querys.makkara_sql_haku import search_makkara, search_makkara_id
from Game.python.sql_querys.money_function import update_player_money
from Game.python.sql_querys.player_current_airport import player_current_airport_sql
from Game.python.sql_querys.player_location_fetch_and_update_querys import update_player_location, fetch_player_location
from Game.python.doubling_machine import tuplaus
from Game.python.game_texts import sausage_price
from Game.python.sql_querys.top_5_score_fetch_query import print_all_players_top
from Game.python.sql_querys.player_top_5_query import print_player_top5_list
from Game.python.taxfree import tax_free
from Game.python.choose_game import get_unfinished_playthrough
from Game.python.sign_in_up import sign_in_function, sign_up_function
from Game.python.sql_querys.create_and_end_game import create_game_safely
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.money_function import fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch
from flask import Flask, Response
from flask_cors import CORS
import json


app = Flask(__name__)


@app.route('/signin/<screen_name>')
def signin(screen_name):
    try:
        name_found = sign_in_function(screen_name)
        if not name_found:
            status_code = 404
            response_text = {
                'status': status_code,
                'message': 'Username not found.'
            }
        else:
            game_id = get_unfinished_playthrough(screen_name)
            status_code = 200
            response_text = {
                'status': status_code,
                'screen_name': screen_name,
                'unfinished_game': {}
            }
            print(game_id)
            if game_id:
                response_text['unfinished_game'] = {
                    'game_location': fetch_player_location_name(game_id)['name'],
                    'game_makkaras': len(fetch_player_makkaras(game_id)),
                    'game_score': player_score_fetch(game_id),
                    'game_money': fetch_player_money(game_id)['money']
                }
                print(response_text)
    except Exception as e:
        status_code = 500
        response_text = {
            'status': status_code,
            'message': str(e)
        }
    jsonresponse = json.dumps(response_text)
    return Response(response=jsonresponse, status=status_code, mimetype="application/json")


@app.route('/signup/<screen_name>', methods=['POST'])
def signup(screen_name):
    try:
        name_available = sign_up_function(screen_name)
        status_code = 404
        if not name_available:
            response_text = {
                'status': status_code,
                'message': 'Username is already taken.'
            }
        else:
            status_code = 200
            response_text = {
                'status': status_code,
                'screen_name': screen_name,
                'unfinished_game': {}
            }
    except Exception as e:
        status_code = 500
        response_text = {
            'status': status_code,
            'message': str(e)
        }
    jsonresponse = json.dumps(response_text)
    return Response(response=jsonresponse, status=status_code, mimetype="application/json")


@app.route('/start_game/<screen_name>/<new_game>')
def start_game(screen_name, new_game):
    """
    Starts the game.

    Parameters
    ----------
    screen_name : str
        The screen_name of the game.
    new_game : bool
        The divisor.

    Returns
    -------
    float
        The quotient of the division.
    """
    try:
        if new_game == 'true':
            game_id = create_game_safely(screen_name)
            status_code = 200
            response_text = {
                'status': status_code,
                'game_id': game_id
            }
        elif new_game == 'false':
            game_id = get_unfinished_playthrough(screen_name)
            status_code = 200
            response_text = {
                'status': status_code,
                'game_id': game_id
            }
        else:
            status_code = 404
            response_text = {
                'status': status_code,
                'message': 'Incorrect input.'
            }
    except Exception as e:
        status_code = 500
        response_text = {
            'status': status_code,
            'message': str(e)
        }
    jsonresponse = json.dumps(response_text)
    return Response(response=jsonresponse, status=status_code, mimetype="application/json")


airports = {}


def airport_cleaner(airport_dic):
    airport_dic = {}
    return airport_dic


money_to_be_doubled = {}

times_doubled = [0, 1]


@app.route('/airport/<ide>')
# Gives dictionaries within dictionary of 20 randomized airports based on location to user
def airport(ide):
    airport_cleaner(airports)
    result = airportselection(ide)
    airports[ide] = result
    return result


@app.route('/airport_selected/<ide>/<airport_num>')
# Get users selected airport (frond end checks if he can afford) and updates player location. Also takes the fee here.
# User cannot change the values (i.e. prices), list is saved here. Returned result is just meant for checking does all go
# as planned
def airport_selected(ide, airport_num):
    result = airports[ide][airport_num]
    ariport_icao = result['ident']
    price = result['price']
    current_money = fetch_player_money(ide)['money']
    spend = int(current_money) - int(price)
    update_player_money(spend, ide)
    update_player_location(ide, ariport_icao)
    return result


@app.route('/garbage/<ide>')
# when money found works now returns dictionary money as key and value is the random amount
def garbage(ide):
    value = garbage_can(ide)
    if value == 'found_money':
        won_money = money_from_garbage()
        money_to_be_doubled[ide] = won_money
        # this check global list to be empty. List range is the logic for the doubling.
        if len(times_doubled) > 0:
            for i in range(len(times_doubled)):
                times_doubled.pop()
                i += 1
        print(money_to_be_doubled)
        result = {'player_found_money': won_money}
        return result
    elif value == 'hole_in_charge':
        result = hole_in_charge(ide)
        return result
    elif value == 'finnair_personnel':
        # check later how it will be implemented to frontend
        result = {'value': 'Finnair_personel happened'}
        return result
    elif value == 'robber':
        result = robber(ide)
        return result


@app.route('/finnair/<ide>')
def finnair(ide):
    # Javascript need to check the player input.
    # Returns dictionary like this {'answer': 'Ei rahaa'}
    result = finnair_personnel(ide)
    return result


@app.route('/doubling/<ide>')
# returns how much player won
def doubling(ide):
    doubled_money = money_to_be_doubled[ide]
    times = len(times_doubled)
    new_money = tuplaus(doubled_money, times)
    money_to_be_doubled[ide] = new_money
    times_doubled.append(1)
    if new_money == 0:
        result = {'result': '0'}
        return result
    else:
        result = {'result': new_money}
        return result


@app.route('/save_money/<ide>')
def save_money(ide):
    player_new_money = int(money_to_be_doubled[ide]) + int(fetch_player_money(ide)['money'])
    update_player_money(player_new_money, ide)
    money_to_be_doubled[ide] = '0'
    return {'money': 'saved'}


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
# Define variables in search_of_kolo function based on how frontend gives us info about transportation.
# Returns dictionary like: {'makkara': 'found'}
def hole_search(ide, transportation):
    result = kolo_search(ide, transportation)
    return result


@app.route('/player_money/<ide>')
# Return a dictionary like this {'money': '400'}.
def player_money(ide):
    result = fetch_player_money(ide)
    return result


@app.route('/player_location/<ide>')
# Returns player location as lat and long like this {'lattitude': '10', 'longitude': '2'}.
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


@app.route('/top_5_player/<ide>')
def top_5_player(ide):
    return print_player_top5_list(ide)


@app.route('/player_location_for_flag/<ide>')
def player_location_for_flag(ide):
    return country_code_for_flag(ide)


@app.route('/player_current_airport/<ide>')
def player_current_airport(ide):
    return player_current_airport_sql(ide)


@app.route('/player_current_makkara_list/<ide>')
# return every player unique sausage and sausage count
def player_current_makkara_list(ide):
    return current_list_of_player_makkaras(ide)


@app.route('/check_status/<ide>/<section>')
# return every player unique sausage and sausage count
def check_satus(ide, section):
    try:
        status_dict = check_player_makkara_game(ide)
        if not all(section in status_dict for sec in ('game_id', 'garbage', 'taxfree', 'airport', 'hole_in_charge')):
            status_code = 404
            response_text = {
                'status': status_code,
                'message': 'Error in api call.'
            }
        else:
            status_code = 200
            response_text = {
                'status': status_code,
                'section_status': status_dict[section]
            }
    except Exception as e:
        status_code = 500
        response_text = {
            'status': status_code,
            'message': str(e)
        }
    jsonresponse = json.dumps(response_text)
    return Response(response=jsonresponse, status=status_code, mimetype="application/json")

@app.route('/update_status/<ide>/<section>/<done>')
# return every player unique sausage and sausage count
def check_section_satus(ide, section, done):
    """
       Parameters
       ide : int, The ide of the game.
       section : str, The section of the game to be updated
       done : str, 'true' or 'false'
       Returns status code and message (success or error)
       """
    try:
        update_player_makkara_game(ide, section, done)
        status_code = 200
        response_text = {
            'status': status_code,
            'message': 'Success.'
        }
    except Exception as e:
        status_code = 500
        response_text = {
            'status': status_code,
            'message': str(e)
        }
    jsonresponse = json.dumps(response_text)
    return Response(response=jsonresponse, status=status_code, mimetype="application/json")

CORS(app)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
