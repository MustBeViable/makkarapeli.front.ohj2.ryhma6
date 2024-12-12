# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 10 % musta makkara, 60% mahis voittaa rahaa

import random

from Game.python.count_makkara_score import count_makkara_score
from Game.python.game_texts import no, yes, yhteys, finnair_makkara, finnair_donation
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.makkara_sql_haku import search_any_makkara_score, fetch_makkara_id_from_reached
from Game.python.sql_querys.money_function import update_player_money, fetch_player_money
from Game.python.sql_querys.return_stolen_makkaras import steal_makkara
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update


def robber(id):
    """robber reduces half of the player's money"""
    player_money = int(fetch_player_money(id)['money'])
    if player_money == 1:
        aft_rob = player_money - 1
        result = {'robber': f'{aft_rob}'}
        return result
    else:
        aft_rob = round(player_money * 0.5)
        update_player_money(aft_rob, id)
        result = {'robber': f'{aft_rob}'}
        return result


def hole_in_charge(game_id):
    """This is hole in charge function and uses sql query from another file."""
    own_makkaras = fetch_player_makkaras(game_id)
    print("Törmäsit kolovastaavaan!")
    if len(own_makkaras) == 0:
        result = {'answer': '0'}
        return result
    else:
        # Devided by five (like 20%) and rounded down
        num_to_lose = len(own_makkaras) // 5

        # Varmistetaan, että vähintään yksi makkara otetaan
        if num_to_lose == 0 and len(own_makkaras) > 0:
            num_to_lose = 1

        # A random number of sausages (num_to_lose) is selected to remove
        lost_makkaras = random.sample(own_makkaras, num_to_lose)

        # The selected sausages are removed from original list and added to hole in charge's list
        minus_score = 0
        for makkara in lost_makkaras:
            steal_makkara(makkara)
            makkara_id = fetch_makkara_id_from_reached(makkara)
            minus_score += count_makkara_score(game_id, makkara_id)
        new_score = player_score_fetch(game_id) - minus_score
        player_score_update(new_score, game_id)
        result = {'answer': f'{len(lost_makkaras)}'}
    return result


def finnair_personnel(game_id):
    """Player can donate 500 euros and get rare sausage"""
    print(f"Finnairin ympäristöedustaja pyytää lahjoitusta. Sen arvo on {finnair_donation}€.")
    current_money = fetch_player_money(game_id)['money']
    if int(current_money) >= 500:
        money = int(fetch_player_money(game_id)['money'])
        money -= finnair_donation
        update_player_money(money, game_id)
        score = player_score_fetch(game_id)
        score += finnair_makkara
        player_score_update(score, game_id)
        result = {'answer': 'makkara ostettu'}
        return result
    else:
        result = {'answer': 'ei rahaa'}
        return result


def money_from_garbage():
    """This randomizes how much money you can get"""
    new_money = random.randint(200, 1000)

    return new_money


def garbage_can(game_id):
    """This is the main carbage can function, and it is checkng garbages with its all features (money found, robber,
    hole in charge, finnair personnel"""
    from Game.python.commands import input_in_section
    outcome = \
    random.choices(['found_money', 'robber', 'hole_in_charge', 'finnair_personnel'], weights=[25, 25, 25, 25], k=1)[0]
    return outcome
