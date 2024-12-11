from Game.python.game_texts import yhteys
from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location


def search_makkara(game_id):

    """Returns the name of the makkara in the location"""

    lokaatio=fetch_player_location(game_id)['player_location']
    sql = (f"SELECT name "
           f"FROM makkara "
           f"WHERE country in("
           f"select iso_country from country where iso_country in("
           f"select iso_country from airport where ident in("
           f"select player_location from playthrough where player_location='{lokaatio}')))")

    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]


def search_makkara_id(game_id):

    """returns makkara_id in player location"""

    lokaatio=fetch_player_location(game_id)['player_location']
    print(lokaatio)
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

    lokaatio=fetch_player_location(game_id)['player_location']
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


def search_amount_of_local_makkara(game_id):
    """ Checks in which country the player is,
    and fetches the amount of that country's makkaras the player has bought.
    Returns the amount as int.
    """
    local_makkara = search_makkara_id(game_id)
    sql = (f"SELECT COUNT(makkara_id) "
           f"FROM makkara_reached "
           f"WHERE playthrough_id = {game_id} "
           f" AND makkara_id = {local_makkara}")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]['COUNT(makkara_id)']


def search_amount_of_any_makkara(game_id, makkara_id):
    """ Fetches the amount of the given country's makkaras the player has bought.
    Returns the amount as int.
    """
    sql = (f"SELECT COUNT(makkara_id) "
           f"FROM makkara_reached "
           f"WHERE playthrough_id = {game_id} "
           f" AND makkara_id = {makkara_id}")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]['COUNT(makkara_id)']


def search_any_makkara_score(game_id, makkara_id):

    """Fetches makkaras points from country given as a parameter"""

    sql = (f"SELECT score "
           f"FROM makkara "
           f"WHERE makkara_id = {makkara_id}")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]["score"]