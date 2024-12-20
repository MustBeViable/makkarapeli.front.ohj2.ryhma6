import random

from Game.python.count_makkara_score import count_makkara_score
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_stolen_makkaras
from Game.python.sql_querys.makkara_sql_haku import fetch_makkara_id_from_reached
from Game.python.sql_querys.money_function import fetch_player_money, update_player_money
from Game.python.sql_querys.return_stolen_makkaras import return_player_makkaras
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update

taxi_price = 300
yango = 50

def kolo_search(game_id, transportation):

    """What happens when u search kolo"""
    #change variables in if check to match how frontend gives it to us

    if transportation == "taxi":
        return_stolen_score(game_id)
        return_player_makkaras(game_id)
        new_money = int(fetch_player_money(game_id)['money']) - taxi_price
        update_player_money(new_money, game_id)
        result = {'makkara': 'found'}
        return result

    elif transportation == "yango":
        chance = random.randint(1,2)
        if chance == 1:
            new_money= int(fetch_player_money(game_id)['money']) - taxi_price - yango
            update_player_money(new_money, game_id)
            result = {'makkara': 'not found also robbed'}
            return result

        else:
            return_stolen_score(game_id)
            new_money= int(fetch_player_money(game_id)['money']) -  yango
            update_player_money(new_money, game_id)
            return_player_makkaras(game_id)
            result = {'makkara': 'found'}
            return result


def return_stolen_score(game_id):
    plus_score = 0
    lost_makkaras = fetch_player_stolen_makkaras(game_id)
    for makkara in lost_makkaras:
        makkara_id = fetch_makkara_id_from_reached(makkara)
        plus_score += count_makkara_score(game_id, makkara_id)
    new_score = player_score_fetch(game_id) + plus_score
    player_score_update(new_score, game_id)