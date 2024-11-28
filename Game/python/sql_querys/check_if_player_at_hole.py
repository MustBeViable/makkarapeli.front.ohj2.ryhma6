from Game.game_texts import yhteys
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location

#Unfinished maybe coming next release
def country_where_hole(id):
    ICAO = fetch_player_location(id)
    sql = (f" SELECT country.name as name"
           f" FROM country"
           f" WHERE iso_country in ("
           f" SELECT iso_country"
           f" FROM airport"
           f" WHERE country.iso_country=airport.iso_country)")

def set_stolen_makkaras_location(id, ICAO):
    sql = (f" UPDATE playthrough"
           f" SET stolen_makkara_location = '{ICAO}'"
           f" WHERE id = {id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def check_if_player_at_stolen_makkaras_location(id):
    sql = (f" SELECT stolen_makkaras_location,"
           f" FROM playthrough"
           f" WHERE id = {id}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0][0]

