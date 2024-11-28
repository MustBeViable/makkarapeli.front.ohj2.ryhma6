from Game.game_texts import yhteys


def fetch_player_screen_name(game_id):
    """Fetches the screen name in the playthrough."""
    sql = (f" SELECT screen_name"
           f" FROM playthrough"
           f" where id = '{game_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0][0]