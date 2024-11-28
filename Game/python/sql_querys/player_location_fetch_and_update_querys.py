from Game.game_texts import yhteys


def fetch_player_location(id):
    sql = (f" SELECT player_location"
           f" FROM playthrough"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    current_location = result[0][0]

    return current_location

def update_player_location(id, new_location):
    sql = (f" UPDATE playthrough"
           f" SET player_location = '{new_location}'"
           f" WHERE id = '{id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def fetch_player_location_name(id):
    sql = (f" SELECT airport.name"
           f" FROM airport"
           f" WHERE ident = ("
           f"   SELECT player_location"
           f"   FROM playthrough"
           f"   WHERE id ='{id}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    current_location_name = result[0][0]
    return current_location_name