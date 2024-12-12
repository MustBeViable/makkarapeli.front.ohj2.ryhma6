from Game.python.count_makkara_score import count_makkara_score
from Game.python.game_texts import sausage_price
from Game.python.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update
from Game.python.sql_querys.makkara_taxfree_sql_update import add_makkara_reached
from Game.python.sql_querys.money_function import update_player_money, fetch_player_money

def tax_free(player_money, makkara_id, game_id):
    """Taxfree subtracts cost of money from player moneys and adds makkara from the country to
    players makkara_reached and adds makkaras score to players score"""
    if sausage_price <= player_money:
        add_makkara_reached(game_id, makkara_id)
        new_money = int(player_money) - sausage_price
        update_player_money(new_money, game_id)
        new_player_score = player_score_fetch(game_id) + count_makkara_score(game_id, makkara_id)
        player_score_update(new_player_score, game_id)
        result = {'makkara': 'ostettu'}
        return result
    elif sausage_price > player_money:
        result = {'makkara': 'Rahat eivät riitä makkaraan'}
        return result