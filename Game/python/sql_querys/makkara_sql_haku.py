from Game.game_texts import yhteys
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location


def search_makkara(game_id):

    """Returns the name of the makkara in the location"""

    lokaatio=fetch_player_location(game_id)
    sql = (f"SELECT name "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")

    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["name"]


def search_makkara_id(game_id):

    """returns makkara_id in player location"""

    lokaatio=fetch_player_location(game_id)
    sql = (f"SELECT id "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")

    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["id"]



def search_makkara_score(game_id):

    """searches makkaras points from country where player in"""

    lokaatio=fetch_player_location(game_id)
    sql = (f"SELECT score "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["score"]
