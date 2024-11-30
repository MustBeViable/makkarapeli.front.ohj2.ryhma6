from flask import Flask

from Game.python.choose_game import get_unfinished_playthrough, create_game_safely
from Game.python.sign_in_up import sign_in_function, sign_up_function
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.money_function import fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/signin/<screen_name>')
def signin(screen_name):
    try:
        name_found = sign_in_function(screen_name)
        if not name_found:
            response = {
                'status': '404',
                'message': 'Username not found.'
            }
        else:
            game_id = get_unfinished_playthrough(screen_name)
            response = {
                'status': '200',
                'screen_name': screen_name,
                'unfinished_game': {}
            }
            print(game_id)
            if game_id:
                response['unfinished_game'] = {
                    'game_location': fetch_player_location(game_id),
                    'game_makkaras': len(fetch_player_makkaras(game_id)),
                    'game_score': player_score_fetch(game_id),
                    'game_money': fetch_player_money(game_id)
                }

    except Exception as e:
        response = {
            'status': '500',
            'message': str(e)
        }
    return response


@app.route('/signup/<screen_name>')
def signup(screen_name):
    try:
        name_available = sign_up_function(screen_name)
        if not name_available:
            response = {
                'status': '404',
                'message': 'Username is already taken.'
            }
        else:
            response = {
                'status': '200',
                'screen_name': screen_name,
                'unfinished_game': {}
            }
    except Exception as e:
        response = {
            'status': '500',
            'message': str(e)
        }
    return response

@app.route('/choose_game/<screen_name>/<new_game>')
def choose_game(screen_name, new_game):
    try:
        if new_game == 'true':
            game_id = create_game_safely(screen_name)
            response = {
                'status': '200',
                'game_id': game_id
            }
        elif new_game == 'false':
            game_id = get_unfinished_playthrough(screen_name)
            response = {
                'status': '200',
                'game_id': game_id
            }
        else:
            response = {
                'status': '404',
                'message': 'Incorrect input.'
            }
    except Exception as e:
        response = {
            'status': '500',
            'message': str(e)
        }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)