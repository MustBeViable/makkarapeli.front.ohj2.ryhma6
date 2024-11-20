import random

from Game.sql_querys.money_function import fetch_player_money, update_player_money
from Game.sql_querys.return_stolen_makkaras import return_player_makkaras

taxi_price = 150
uber_price = 1

def kolo_search(game_id):

    """What happens when u search kolo"""

    from Game.commands import input_in_section

    outside_airport = input_in_section(game_id, f"Kirjoita taxi jos haluat ottaa taxin ({taxi_price}€) tai kirjoita uber jos haluat uberin ({uber_price}€).")
    while outside_airport != "taxi" and outside_airport != "uber":
        outside_airport = input_in_section(game_id, f"Kirjoita taxi jos haluat ottaa taxin ({taxi_price}€) tai kirjoita uber jos haluat uberin ({uber_price}€).")

    if outside_airport == "taxi":
        return_player_makkaras(game_id)
        new_money = fetch_player_money(game_id) - taxi_price
        update_player_money(new_money, game_id)
        print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
    elif outside_airport == "uber":
        mahdollisuus=random.randint(1,2)
        if mahdollisuus==1:
            new_money=fetch_player_money(game_id)-150-uber_price
            update_player_money(new_money, game_id)
            print("Uber kuljettaja vei sinulta 100 euroa ja jätti sinut tienvarteen. Joudit tilaamaan taxin takaisin lentokentälle, mikä maksoi 50 euroa.")
        elif mahdollisuus!=1:
            return_player_makkaras(game_id)
            print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
            return
