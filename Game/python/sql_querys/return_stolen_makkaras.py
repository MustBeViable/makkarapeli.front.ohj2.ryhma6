from Game.game_texts import yhteys


def return_player_makkaras(id):

    """Returns makkaras from hole_in_charge to player, by making stolen=false"""

    sql = (f" UPDATE makkara_reached"
           f" SET stolen = false"
           f" where playthrough_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
