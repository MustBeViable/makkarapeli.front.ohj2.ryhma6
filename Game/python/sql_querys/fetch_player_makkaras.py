from Game.python.game_texts import yhteys

#Luo listan pelaajan makkaroista joita pelaajalla on. Parametri on pelaajan uniikki id.
def fetch_player_makkaras(id):
    sql = (f" SELECT id"
           f" FROM makkara_reached"
           f" where playthrough_id = '{id}'"
           f" and stolen = False")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras

def fetch_player_stolen_makkaras(id):
    sql = (f" SELECT id"
           f" FROM makkara_reached"
           f" where playthrough_id = '{id}'"
           f" and stolen = True")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    player_makkaras = []
    for i in range(len(result)):
        player_makkaras.append(result[i][0])
    return player_makkaras

def player_makkaras_amount(id):
    """Returns the amount of makkaras the player has."""
    amount = len(fetch_player_makkaras(id))
    return amount

def current_list_of_player_makkaras(id):
    """Returns every unique sausage name"""
    sql = (f" SELECT makkara.name as name,"
           f" COUNT(makkara_reached.id) AS count"
           f" FROM makkara"
           f" JOIN makkara_reached ON makkara.id = makkara_reached.makkara_id"
           f" JOIN playthrough ON makkara_reached.playthrough_id = playthrough.id"
           f" WHERE playthrough.id = '{id}'"
           f" GROUP BY makkara.name")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result

def current_list_of_player_makkaras_count(id):
    sql = (f" SELECT count(makkara.name) as count"
           f" FROM makkara"
           f" JOIN makkara_reached ON makkara.id = makkara_reached.makkara_id"
           f" JOIN playthrough ON makkara_reached.playthrough_id = playthrough.id"
           f" WHERE playthrough.id = '{id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result