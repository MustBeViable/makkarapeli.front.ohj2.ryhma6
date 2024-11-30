# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 10 % musta makkara, 60% mahis voittaa rahaa

import random

from Game.python.Game_ascii_art.hole_in_charge_ascii import hole_in_charge_ascii
from Game.python.Game_ascii_art.money_found_garbage_can import happy_garbage_can
from Game.python.Game_ascii_art.robber_from_garbage_can import robber_2
from Game.python.game_texts import no, yes, yhteys, finnair_makkara, finnair_donation
from For_futher_development.secret_black_sausage import secret_black_sausage_chance, amount
from Game.python.doubling_machine import tuplataanko
from Game.python.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.python.sql_querys.money_function import update_player_money, fetch_player_money
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update


def robber(id):
    """robber reduces half of the player's money"""
    player_money = fetch_player_money(id)
    if player_money > 0:
        if player_money == 1:
            new_money = player_money - 1
            update_player_money(new_money, id)
            value = {'money': new_money}
            return value
        else:
            new_money = player_money * 0.5
            update_player_money(new_money, id)
            value = {'money': new_money}
            return value
    else:
        value = {'money': 'Ei ryöstettävää'}
        return value


def hole_in_charge(game_id):
    """This is hole in charge function and uses sql query from another file."""
    own_makkaras = fetch_player_makkaras(game_id)
    if len(own_makkaras) <= 0:
        answer = {'value': 'You have no makkaras. Hole_in_charge leaves defeated.'}
        return answer
    else:
        num_to_lose = len(own_makkaras) // 5

        if num_to_lose == 0:
            num_to_lose = 1

        # A random number of sausages (num_to_lose) is selected to remove
        lost_makkaras = random.sample(own_makkaras, num_to_lose)

        # The selected sausages are removed from original list and added to hole in charge's list
        for makkara in lost_makkaras:
            sql = (
                f"UPDATE makkara_reached SET stolen = True WHERE id IN (SELECT id FROM makkara_reached WHERE id = {makkara})")
            kursori = yhteys.cursor()
            kursori.execute(sql)
            result = {'makkaras_lost': {str(len(lost_makkaras))}}
            return result

def finnair_personnel(game_id, answer):
    """Player can donate 500 euros and get rare sausage"""
    current_money = fetch_player_money(game_id)
    if answer and current_money >= 500:
        money = fetch_player_money(game_id)
        money -= finnair_donation
        update_player_money(money, game_id)
        score = player_score_fetch(game_id)
        score += finnair_makkara
        player_score_update(score, game_id)
        result = {'answer': 'Sait maggaran :---D'}
        return result
    else:
        if current_money < 500:
            result = {'answer': 'Ei rahaa'}
            return result


def money_from_garbage():
    """This randomizes how much money you can get"""
    new_money = random.randint(200, 1000)
    value = {'money': new_money}
    return value


def garbage_can():
    """This is the main carbage can function, and it is checkng garbages with its all features (money found, robber,
    hole in charge, finnair personnel"""
    outcome = \
    random.choices(['found_money', 'robber', 'hole_in_charge', 'finnair_personnel'], weights=[70, 0, 0, 0], k=1)[0]
    return outcome
