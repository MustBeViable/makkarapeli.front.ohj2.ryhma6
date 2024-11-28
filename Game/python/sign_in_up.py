from Game.python.game_texts import cancel_command, sign_up, sign_in, give_screen_name_str, sign_in_or_up_str
from Game.python.sql_querys.create_and_end_game import fetch_all_screen_names

def sign_in_function(name):
    """Ask the player for a screen name. \n
    Returns False if the name is not found, True if the screen name exists."""
    if name not in fetch_all_screen_names():
        return False
    else:
        return True

def sign_up_function(name):
    """Asks the player for a screen name.\n
    Returns the given name."""
    if name in fetch_all_screen_names():
        return {name: False}
    else:
        return {name: True}