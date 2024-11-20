from Game.game_texts import yhteys


def player_score_fetch(id):
    sql = (f" SELECT score"
           f" FROM playthrough"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    current_score = result[0][0]
    return current_score

def player_score_update(new_score, id):
    sql = (f" UPDATE playthrough"
           f" SET score = {new_score}"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return