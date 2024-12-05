from Game.python.game_texts import yhteys

def player_current_airport_sql(ide):
    sql = (f" SELECT airport.name as name, airport.iso_country as countrycode"
           f" FROM playthrough"
           f" JOIN airport ON playthrough.player_location = airport.ident"
           f" WHERE playthrough.id = {ide}")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    player_current_airport_info = kursori.fetchall()
    return player_current_airport_info[0]