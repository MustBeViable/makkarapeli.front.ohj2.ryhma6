from Game.game_texts import cancel_command, sign_up, sign_in, give_screen_name_str, sign_in_or_up_str
from Game.sql_querys.create_and_end_game import fetch_all_screen_names

# Asks the player if they want to sign in or sign up until they give one of those answers.
def ask_sign_in_or_up():
    """ Asks the player if they want to sign in or sign up.\n
    Returns the screen name of the player."""
    answer = input(sign_in_or_up_str).lower().strip()
    if answer == sign_in:
        name = sign_in_function()
    elif answer == sign_up:
        name = sign_up_function()
    else:
        name = ask_sign_in_or_up()
    return name

# Asks the player for a screen name and accepts it, if it has previous games.
# If the player cancels, they can choose again if they want to sign in or sign up.
def sign_in_function():
    """Ask the player for a screen name and returns the given name."""
    name = input(give_screen_name_str).lower().strip()
    while name not in fetch_all_screen_names() and name != cancel_command:
        print(f'Käyttäjätunnusta "{name}" ei löydy.')
        name = input(give_screen_name_str).lower().strip()
    if name == cancel_command:
        name = ask_sign_in_or_up()
    return name

# Asks the player for a screen name and accepts it, if it doesn't have previous games.
# If the player cancels, they can choose again if they want to sign in or sign up.
def sign_up_function():
    """Asks the player for a screen name.\n
    Returns the given name."""
    name = input(give_screen_name_str).lower()
    while name in fetch_all_screen_names() and name != cancel_command:
        name = input(f'Käyttäjätunnus "{name}" on jo käytössä. Valitse toinen nimi.\n').lower().strip()
    if name == cancel_command:
        name = ask_sign_in_or_up()
    return name