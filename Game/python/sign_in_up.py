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
    Returns True if the name is available, returns False if it's not."""
    if name in fetch_all_screen_names():
        return False
    else:
        return True