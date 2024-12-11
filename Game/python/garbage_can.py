# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 10 % musta makkara, 60% mahis voittaa rahaa

import random

from Game.python.Game_ascii_art.finnair_ascii import finnair_ascii
from Game.python.Game_ascii_art.hole_in_charge_ascii import hole_in_charge_ascii
from Game.python.Game_ascii_art.money_found_garbage_can import happy_garbage_can
from Game.python.Game_ascii_art.robber_from_garbage_can import robber_2
from Game.python.count_makkara_score import count_makkara_score
from Game.python.game_texts import no, yes, yhteys, finnair_makkara, finnair_donation
from For_futher_development.secret_black_sausage import secret_black_sausage_chance, amount
from Game.python.doubling_machine import tuplataanko
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
        aft_rob = player_money * 0.5
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
        player_score_update(game_id, new_score)
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



"""
    if outcome == 'found_money':
        new_money = money_from_garbage()
        tuplataanko(vastaus, new_money, game_id)  # eliaksen tuplaus funktio
    elif outcome == 'robber':
        current_money = int(fetch_player_money(game_id)['money'])
        if current_money > 0:
            left = robber(game_id, current_money)
            result = {'money_left': left}
            return result
        else:
            result = {'answer': 'ei ryöstettävää'}
            return result
    elif outcome == 'hole_in_charge':
        print(hole_in_charge_ascii)
        hole_in_charge(game_id)
    elif outcome == 'finnair_personnel':
        print(finnair_ascii)
        print("Terve, olen Finnairin ympäristöedustaja. Meillä on palvelu,\n"
              "jolla voit kompensoida lentopäästöjäsi. Voit lahjoittaa haluamasi\nmäärän rahaa, ja me annamme sinulle "
              "vastineeksi harvinaisen makkaran.")
        finnair_personnel(game_id)
    elif outcome == secret_black_sausage_chance:
        secret_black_sausage_chance(amount)  # saken mustamakkara funktio"""