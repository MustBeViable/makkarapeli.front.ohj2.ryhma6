from Game.search_of_kolo import kolo_search
from Game.sql_querys.fetch_player_makkaras import fetch_player_stolen_makkaras


def check_if_any_stolen_makkara(game_id):
    """checks if player has over 0 makkaras and if has any makkaras, plays kolo_search funktio"""
    if len(fetch_player_stolen_makkaras(game_id))>0:
        kolo_search(game_id)
    else:
        print("Kololla ei ole sinulle mitään!")