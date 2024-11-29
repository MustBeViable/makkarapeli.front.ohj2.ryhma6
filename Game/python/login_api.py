from flask import Flask

from Game.python.sign_in_up import sign_in_function, sign_up_function
from Game.python.sql_querys.create_and_end_game import fetch_unfinished_playthrough, create_game
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.money_function import fetch_player_money
from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch

app = Flask(__name__)


@app.route('/signin/<screen_name>')
def signin(screen_name):
    name_found = sign_in_function(screen_name)
    if not name_found:
        response = {
            'status': '404',
            'message': 'Käyttäjätunnusta ei löytynyt.'
        }
    else:
        game_id = fetch_unfinished_playthrough(screen_name)
        response = {
            'status': '200',
            'screen_name': screen_name,
            'unfinished_game': {}
        }
        if game_id:
            response['unfinished_game'] = {
                'game_location': fetch_player_location(game_id),
                'game_makkaras': fetch_player_makkaras(game_id),
                'game_score': player_score_fetch(game_id),
                'game_money': fetch_player_money(game_id)
            }
    return response

@app.route('/signup/<screen_name>')
def signup(screen_name):
    name_available = sign_up_function(screen_name)
    if not name_available:
        response = {
            'status': '404',
            'message': 'Käyttäjätunnus on jo käytössä.'
        }
    else:
        response = {
            'status': '200',
            'screen_name': screen_name,
            'unfinished_game': {}
        }
    return response

@app.route('/login/<screen_name>/<new_game>')
def choose_game(screen_name, new_game):
    if new_game:
        game_id = create_game(screen_name)
    else:
        game_id = fetch_unfinished_playthrough(screen_name)
    return game_id


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)