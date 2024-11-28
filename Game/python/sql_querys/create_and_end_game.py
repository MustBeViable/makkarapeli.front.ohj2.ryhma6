from Game.game_texts import yhteys

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