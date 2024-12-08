from Game.python.sql_querys.create_and_end_game import create_game, finish_game_in_database, \
    fetch_unfinished_playthrough


def create_or_choose_game(screen_name, continue_game):
    """Checks if the given screen_name has an unfinished game.
    If they do, asks if they want to continue or create a new game.
    If they choose to continue, returns the id of that old game.
    If they decide to create a new game, or they don't have an unfinished game,
    creates a new game and returns its id. If they create a new game,
    the unfinished game will be marked as finished."""

    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    if len(unfinished_game_list) != 0:
        current_game_id = choose_old_or_new_game(screen_name, unfinished_game_list, continue_game)
    else:
        current_game_id = create_game(screen_name)
    return current_game_id


def choose_old_or_new_game(screen_name, unfinished_game_list, continue_game):
    """Asks the player if they want to continue their old game or start a new game
    and returns the id of the game. Creates a new game if needed and marks the old
    game as finished."""
    unfinished_game_id = unfinished_game_list[0][0]
    if continue_game:
        current_game_id = unfinished_game_id
    else:
        current_game_id = create_game(screen_name)
        finish_game_in_database(unfinished_game_id)
    return current_game_id


def get_unfinished_playthrough(screen_name):
    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    try:
        unfinished_game_id = unfinished_game_list[0][0]
    except IndexError:
        unfinished_game_id = None
    return unfinished_game_id


def create_game_safely(screen_name):
    """Creates a new game and finishes all unfinished games of the player.
    Returns the id of the created game."""
    unfinished_game_list = fetch_unfinished_playthrough(screen_name)
    if len(unfinished_game_list) != 0:
        for unfinished_game in unfinished_game_list:
            unfinished_game_id = unfinished_game[0]
            finish_game_in_database(unfinished_game_id)
    current_game_id = create_game(screen_name)
    return current_game_id
