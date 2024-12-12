from Game.python.game_texts import yhteys


def return_player_makkaras(id):

    """Returns makkaras from hole_in_charge to player, by making stolen=false"""

    sql = (f" UPDATE makkara_reached"
           f" SET stolen = false"
           f" where playthrough_id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def steal_makkara(makkara):
    """Takes makkara_reached id, sets it to stolen=true"""
    sql = (f"UPDATE makkara_reached "
           f"SET stolen = True "
           f"WHERE id = {makkara}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return