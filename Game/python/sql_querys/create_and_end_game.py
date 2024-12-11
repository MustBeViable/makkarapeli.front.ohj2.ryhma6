from Game.python.game_texts import yhteys

def sql_executed(sql_text):
    kursori = yhteys.cursor()
    kursori.execute(sql_text)
    result = kursori.fetchall()
    return result

def create_game(screen_name):
    """Creates the game to the database with given screen name. Returns the id of the new game."""
    sql_create = (f"INSERT INTO playthrough (screen_name) VALUES ('{screen_name}')")
    sql_executed(sql_create)
    sql_id = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND finished = false ORDER BY id DESC")
    sql_executed(sql_id)
    new_id = sql_executed(sql_id)[0][0]
    sql_create_status = (f"INSERT INTO makkara_game (game_id) VALUES ({new_id})")
    sql_executed(sql_create_status)
    return new_id

def finish_game_in_database(finish_id):
    """Marks the game with the given id as finished in the databased."""
    sql = (f"UPDATE playthrough SET finished = true WHERE id = '{finish_id}'")
    sql_executed(sql)
    return

def fetch_unfinished_playthrough(screen_name):
    """Fetches and returns a list of ids of unfinished playthroughs of the player.
    Returns an empty list if there are no unfinished playthroughs."""
    sql = (f"SELECT id FROM playthrough WHERE screen_name = '{screen_name}' AND finished = false")
    unfinished_game_list = sql_executed(sql)
    return unfinished_game_list

def fetch_all_screen_names():
    """Returns each screen name once."""
    sql = (f"select distinct screen_name from playthrough;")
    screen_names_list = sql_executed(sql)
    fine_screen_name_list = []
    for name in screen_names_list:
        fine_screen_name_list.append(name[0])
    return fine_screen_name_list

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