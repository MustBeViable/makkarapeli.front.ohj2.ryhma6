import time

from Game.Game_ascii_art.airplane_up import airplane_up
from Game.commands import input_in_section
from Game.sql_querys.money_function import fetch_player_money, update_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, update_player_location, \
    fetch_player_location_name
from game_texts import yhteys, price_multiplier

def check_player_input(game_id):
    """This function tests if player have given right input."""
    next_location = input_in_section(game_id,
        "Valitse haluamasi uusi lentokenttä syöttämällä sen järjestysluku(älä syötä yli 20 tai 0 tai pienempi): ")
    while next_location is not int and next_location not in range(1,21):
        try:
            next_location = int(next_location)
        except:
            next_location = input_in_section(game_id,
                "Syötit väärin! Valitse uudelleen haluamasi uusi lentokenttä syöttämällä sen järjestysluku: ")
            continue
        else:
            next_location = int(next_location)
        while next_location not in range(1, 21):
            next_location = input_in_section(game_id,
                "Syötit väärin! Valitse uudelleen haluamasi uusi lentokenttä syöttämällä sen järjestysluku: ")
            break
    return next_location

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
    player_current_ident = current_coordinates(player_ident)
    for i in range(len(list_of_airport_dictionaries)):
        dist = distance(list_of_airport_dictionaries[i]['ident'], player_current_ident)
        list_of_airport_dictionaries[i]['distance'] = dist
    #This sorts list of airport dictionaries by the distance from nearest to furthest.
    list_of_airport_dictionaries_sorted_by_distance = sorted(list_of_airport_dictionaries, key=lambda x: x['distance'])
    #Enumerate adds index to the list and uses it as index "i" while airport calls same dictionary's right value.
    money = fetch_player_money(game_id)
    print("Seuraavat lähdöt: (lennon nro, maa, lentokenttä, hinta (€):")
    for i, airport in enumerate(list_of_airport_dictionaries_sorted_by_distance):
        print(f"{i + 1:17.0f}. {airport['country']}: {airport['name']}  ({price_multiplier + i  * price_multiplier}) €)")
    print(f"Sinulla on {money}€. ")
    next_location = check_player_input(game_id)
    while money < next_location*price_multiplier:
        print("Rahasi ei riitä tälle kentälle.")
        next_location = check_player_input(game_id)
    next_airport = list_of_airport_dictionaries_sorted_by_distance[next_location-1]["ident"]
    price = (next_location)*price_multiplier
    money -= price
    update_player_money(money, game_id)
    update_player_location(game_id, next_airport)
    location_name = fetch_player_location_name(game_id)
    print(airplane_up)
    time.sleep(2)
    print(f"Saavuit lentokentälle {location_name}.")
    return next_airport

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
