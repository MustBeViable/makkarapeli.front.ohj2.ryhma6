from Game.game_texts import yhteys

def add_makkara_reached(id, makkara):
    sql = (f" INSERT INTO makkara_reached (playthrough_id, makkara_id)"
           f" VALUES ({id}, {makkara})")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return