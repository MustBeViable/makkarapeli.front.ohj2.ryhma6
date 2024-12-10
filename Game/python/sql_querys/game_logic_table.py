from Game.python.game_texts import yhteys

def update_player_makkara_game(action, id):

    """Updates player playthrough situation ie. if player have been at tax free it will be true"""

    sql = (f"UPDATE makkara_game SET {action} = true WHERE game_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    yhteys.commit()
    return

update_player_makkara_game('TaxFree', 1)