from Game.game_texts import yhteys


def fetch_unique_makkara_score(id):
    sql = (f" SELECT score"
           f" from makkara"
           f" where id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    makkara_score = result[0][0]
    return makkara_score

