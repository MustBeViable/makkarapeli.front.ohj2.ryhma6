from flask import Flask

from Game.python.sign_in_up import sign_in_function
from Game.python.sql_querys.create_and_end_game import fetch_unfinished_playthrough, create_game

app = Flask(__name__)
@app.route('/login/<screen_name>')
def signin(screen_name):
    name_found = sign_in_function(screen_name)
    if not name_found:
        return {'message': 'Username not found. Please try again.', 'status': 'not_found'}
    else:
        unfinished_game = fetch_unfinished_playthrough(screen_name)
        if not unfinished_game:
            new_game_id = create_game(screen_name)
            return {
                'message': 'New game created.',
                'status': 'new_game',
                'game_id': new_game_id
            }
        else: return {
                'message': 'Unfinished games found. Would you like to continue?',
                'status': 'unfinished_games',
                'unfinished_game': unfinished_game[0][0]
            }

@app.route('/login/<screen_name>/<old_or_new>')
def choose_game(screen_name):
    pass




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)