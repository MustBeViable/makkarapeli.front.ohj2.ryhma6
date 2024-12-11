from Game.python.game_texts import yhteys

def update_player_makkara_game(id, action, done):

    """Updates player playthrough situation ie. if player have been at tax free it will be true"""

    sql = (f"UPDATE makkara_game SET {action} = {done} WHERE game_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)


def check_player_makkara_game(id):

    """Updates player playthrough situation ie. if player have been at tax free it will be true.
    Takes playthrough id as parameter and returns a dictionary
    {'game_id': 1, 'garbage': 0, 'taxfree': 0, 'airport': 0, 'hole_in_charge': 0}"""

    sql = (f" SELECT * "
           f" FROM makkara_game"
           f" WHERE game_id = '{id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]