import random

from Game.python.sql_querys.money_function import fetch_player_money, update_player_money
from Game.python.sql_querys.return_stolen_makkaras import return_player_makkaras

taxi_price = 250
yango = 50

def kolo_search(game_id, transportation):

    """What happens when u search kolo"""
    #change variables in if check to match how frontend gives it to us

    if transportation == "taxi":
        return_player_makkaras(game_id)
        new_money = int(fetch_player_money(game_id)['money']) - taxi_price
        update_player_money(new_money, game_id)
        print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
        result = {'makkara': 'found'}
        return result

    elif transportation == "yango":
        chance = random.randint(1,2)
        if chance == 1:
            new_money= int(fetch_player_money(game_id)['money']) - 150 - yango
            update_player_money(new_money, game_id)
            print("Uber kuljettaja vei sinulta 100 euroa ja jätti sinut tienvarteen. Joudit tilaamaan taxin takaisin "
                  "lentokentälle, mikä maksoi 50 euroa.")
            result = {'makkara': 'not found also robbed'}
            return result

        else:
            new_money= int(fetch_player_money(game_id)['money']) -  yango
            update_player_money(new_money, game_id)
            return_player_makkaras(game_id)
            print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
            result = {'makkara': 'found'}
            return result


"""Vanha funktio alla lähes koskemattomana:
def kolo_search(game_id):

    'What happens when u search kolo' <- kommentti

    from Game.python.commands import input_in_section

    outside_airport = input_in_section(game_id, f"Kirjoita taxi jos haluat ottaa taxin ({taxi_price}€) tai"
                                                f" kirjoita uber jos haluat uberin (oikee yango, mut en jaksa muokkaa "
                                                f"sitä muuttujan nimee) ({yango}€).")
    while outside_airport != "taxi" and outside_airport != "uber":
        outside_airport = input_in_section(game_id, f"Kirjoita taxi jos haluat ottaa taxin ({taxi_price}€) tai "
                                                    f"kirjoita uber jos haluat uberin ({yango}€).")

    if outside_airport == "taxi":
        return_player_makkaras(game_id)
        new_money = fetch_player_money(game_id) - taxi_price
        update_player_money(new_money, game_id)
        print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
    elif outside_airport == "uber":
        mahdollisuus=random.randint(1,2)
        if mahdollisuus==1:
            new_money= fetch_player_money(game_id) - 150 - yango
            update_player_money(new_money, game_id)
            print("Uber kuljettaja vei sinulta 100 euroa ja jätti sinut tienvarteen. Joudit tilaamaan taxin takaisin "
                  "lentokentälle, mikä maksoi 50 euroa.")
        elif mahdollisuus!=1:
            return_player_makkaras(game_id)
            print("Löysit Kolovastaavan Kolon ja sait makkarasi takaisin! :)")
            return

"""