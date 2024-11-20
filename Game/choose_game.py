from Game.game_texts import continue_old_game_command, create_new_game_command
from Game.sql_querys.create_and_end_game import create_game, finish_game_in_database, fetch_unfinished_playthrough
from Game.sql_querys.fetch_player_makkaras import player_makkaras_amount
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location_name
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch

def continue_or_new_str(game_id):
    """'Haluatko jatkaa keskeneräistä pelikertaasi?
       (sijainti: location
       pisteitä: score
       makkaroita: n kpl)
       Jos aloitat uuden peli, edellinen pelisi päättyy.
        Jos haluat jatkaa, paina {old}. Jos haluat aloittaa uuden pelin, paina {new}.'"""
    text = (f"Haluatko jatkaa keskeneräistä pelikertaasi? "
            f"(sijainti: {fetch_player_location_name(game_id)}, "
            f"pisteitä: {player_score_fetch(game_id)}, "
            f"makkaroita: {player_makkaras_amount(game_id)} kpl)\n"
            f"Jos aloitat uuden peli, edellinen pelisi päättyy, etkä voi enää jatkaa sitä.\n"
            f"Jos haluat jatkaa, paina {continue_old_game_command}. Jos haluat aloittaa uuden pelin, paina {create_new_game_command}. ")
    return text

no_unfinished_game = "Luodaan sinulle uusi peli."

def create_or_choose_game(screen_name):
    """Checks if the given screen_name has an unfinished game.
    If they do, asks if they want to continue or create a new game.
    If they choose to continue, returns the id of that old game.
    If they decide to create a new game, or they don't have an unfinished game,
    creates a new game and returns its id. If they create a new game,
    the unfinished game will be marked as finished."""

    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    if len(unfinished_game_list) != 0:
        current_game_id = choose_old_or_new_game(screen_name, unfinished_game_list)
    else:
        print(no_unfinished_game)
        current_game_id = create_game(screen_name)
    return current_game_id

def choose_old_or_new_game(screen_name, unfinished_game_list):
    """Asks the player if they want to continue their old game or start a new game
    and returns the id of the game. Creates a new game if needed and marks the old
    game as finished."""
    current_game_id = None
    unfinished_game_id = unfinished_game_list[0][0]
    user_input = input(continue_or_new_str(unfinished_game_id)).lower().strip()
    while user_input not in [continue_old_game_command, create_new_game_command]:
        user_input = input(continue_or_new_str(unfinished_game_id)).lower().strip()
    if user_input == continue_old_game_command:
        current_game_id = unfinished_game_id
    if user_input == create_new_game_command:
        current_game_id = create_game(screen_name)
        finish_game_in_database(unfinished_game_id)
    return current_game_id