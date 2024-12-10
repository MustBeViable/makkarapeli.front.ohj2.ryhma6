from flask import Flask, Response
import json
from Game.python.choose_game import get_unfinished_playthrough
from Game.python.sign_in_up import sign_in_function, sign_up_function
from Game.python.sql_querys.create_and_end_game import create_game_safely
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.money_function import fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)