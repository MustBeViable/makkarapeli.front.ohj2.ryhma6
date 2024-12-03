from Game.python.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, update_player_location
from game_texts import yhteys, price_multiplier

def airportselection(game_id):
    """Fetch 20 random airports, which will be sorted by distance to player"""
    sql = (f" Select airport.name as name, country.name as country, ident "
           f" from airport, country "
           f" where country.iso_country = airport.iso_country"
           f" and airport.type = 'large_airport'"
           f" and airport.name not like 'CLICK%'"
           f" order by rand()"
           f" limit 20 ")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    list_of_airport_dictionaries = kursori.fetchall()
    #This for loop goes through all the randomly chosen airports one at the time and adds distance airports
    # to the dictionary
    player_ident = fetch_player_location(game_id)
    player_current_ident = current_coordinates(player_ident['player_location'])
    for i in range(len(list_of_airport_dictionaries)):
        dist = distance(list_of_airport_dictionaries[i]['ident'], player_current_ident)
        list_of_airport_dictionaries[i]['distance'] = dist
    #This sorts list of airport dictionaries by the distance from nearest to furthest.
    list_of_airport_dictionaries_sorted_by_distance = sorted(list_of_airport_dictionaries, key=lambda x: x['distance'])
    for i in range(len(list_of_airport_dictionaries_sorted_by_distance)):
        list_of_airport_dictionaries_sorted_by_distance[i]['number'] = f"{i + 1}"
        list_of_airport_dictionaries_sorted_by_distance[i]['price'] = f"{price_multiplier + i * price_multiplier}"
    dictionary_of_dictionarys_airport = {}
    for i in range(len(list_of_airport_dictionaries_sorted_by_distance)):
        dictionary_of_dictionarys_airport[f'{i+1}'] = list_of_airport_dictionaries_sorted_by_distance[i]
    return dictionary_of_dictionarys_airport

def distance(next_place, icao):
    """Check distance of airports one at the time. Returns player's distance to that airport."""
    from geopy import distance
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{next_place}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    dist = distance.distance(icao, result[0]).km
    return dist

def current_coordinates(IDENT):
    """Fetch coordinates of airport, where player is currently. Returns those coordinates."""
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{IDENT}'")

    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result