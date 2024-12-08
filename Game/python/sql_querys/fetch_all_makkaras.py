from Game.python.game_texts import yhteys


def fetch_all_makkaras():
    """Returns a list of all makkara ids"""
    sql = (f" SELECT id"
           f" FROM makkara")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    makkaras = []
    for i in range(len(result)):
        makkaras.append(result[i][0])
    return makkaras