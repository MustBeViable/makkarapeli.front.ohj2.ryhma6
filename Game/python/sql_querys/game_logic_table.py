from Game.python.game_texts import yhteys

def update_player_makkara_game(action, id):

    """Updates player playthrough situation ie. if player have been at tax free it will be true"""

    sql = (f"UPDATE makkara_game SET {action} = true WHERE game_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    yhteys.commit()

def check_player_makkara_game(id):

    """Updates player playthrough situation ie. if player have been at tax free it will be true"""

    sql = (f" SELECT * "
           f" FROM makkara_game"
           f" WHERE game_id = '{id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    yhteys.commit()
    result = kursori.fetchall()
    return result[0]

print(check_player_makkara_game(1))