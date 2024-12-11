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