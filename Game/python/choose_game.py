from Game.python.sql_querys.create_and_end_game import create_game, finish_game_in_database, \
    fetch_unfinished_playthrough

def get_unfinished_playthrough(screen_name):
    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    try:
        unfinished_game_id = unfinished_game_list[0][0]
    except IndexError:
        unfinished_game_id = None
    return unfinished_game_id