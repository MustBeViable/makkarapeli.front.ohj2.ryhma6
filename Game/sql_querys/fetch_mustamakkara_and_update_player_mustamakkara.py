from Game.game_texts import yhteys


def fetch_mustamakkara(id):
    sql = (f" SELECT mustamakkara"
           f" FROM playthrough"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    current_mustamakkara = result[0][0]
    return current_mustamakkara

def mustamakkara_update(id, new_mustamakkara):
    sql = (f" UPDATE playthrough"
           f" SET mustamakkara = {new_mustamakkara}"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

