from Game.game_texts import sausage_price, yes, no
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update
from sql_querys.makkara_taxfree_sql_update import add_makkara_reached
from sql_querys.makkara_sql_haku import search_makkara, search_makkara_id, search_makkara_score
from sql_querys.money_function import update_player_money, fetch_player_money

def taxfree(player_money, makkara_id, game_id):
    """Taxfree subtracts cost of money from player moneys and adds makkara from the country to
    players makkara_reached and adds makkaras score to players score"""
    if sausage_price <= fetch_player_money(game_id):
        makkara_name = search_makkara(game_id)
        add_makkara_reached(game_id, makkara_id)
        new_money = player_money - sausage_price
        update_player_money(new_money, game_id)
        new_player_score = player_score_fetch(game_id) + search_makkara_score(game_id)
        player_score_update(new_player_score, game_id)
        print(f"Ostit makkaran {makkara_name} ja se maksoi {sausage_price} euroa. Sinulla on nyt {new_money} €.")
    elif sausage_price > player_money:
        print("Rahat eivät riittäneet. Mene töihin!!!!")
        return

# Asking do you want to buy makkara from taxfree
def yes_no_taxfree(game_id):
    """Asks player if he wants to buy airport specific makkara."""
    from Game.commands import input_in_section
    print(f"Sinulla on {fetch_player_money(game_id)}€ rahaa. Taxfreestä löytyi hieno {search_makkara(game_id)}"
          f" ja se maksaa {sausage_price}€.")
    taxfree_answer = input_in_section(game_id, f"Haluatko ostaa makkaran? ({yes}/{no})")
    while taxfree_answer not in [yes, no]:
        taxfree_answer = input_in_section(game_id, f"Haluatko ostaa makkaran? ({yes}/{no})")

    if taxfree_answer == yes:
        taxfree(fetch_player_money(game_id), search_makkara_id(game_id), game_id)

# taxfree(player_money, makkara_ID)
# taxfree(fetch_player_money(game_id), search_makkara_id())
# print(player_score_fetch(game_id))