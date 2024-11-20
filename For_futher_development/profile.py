from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras, fetch_player_stolen_makkaras, \
    player_makkaras_amount
from Game.sql_querys.money_function import fetch_player_money
from Game.sql_querys.player_location_fetch_and_update_querys import fetch_player_location, fetch_player_location_name
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch


def show_profile(game_id):
    """This funktion shows player's profile"""
    print(f"Sijaintisi on tällä hetkellä lentokentällä: {fetch_player_location_name(game_id)}, ICAO: {fetch_player_location(game_id)}")
    print(f"Sinulla on rahaa {fetch_player_money(game_id)} euroa ja pisteitä {player_score_fetch(game_id)}.")
    #print(f"Sinun scoresi on {score_fetch(game_id)}")
    #show_makkarat = input("Jos haluat nähdä, paljonko sinulla on makkaroita, anna komento 'makkarani'.: ")
    print(f"Sinulla on yhteensä makkaroita: {player_makkaras_amount(game_id)} kpl.")
    #if show_makkarat == 'makkarani':
    """
        print(f"Kolovastaava viemät makkarat: {fetch_player_stolen_makkaras(game_id)}")
        print(f"Sinulla on {fetch_player_makkaras(game_id)}")

    if show_makkarat == 'makkarani':
        show_makkarat_dictionary = {f"{fetch_player_location_name(game_id)}", f"{fetch_player_makkaras(game_id)}"}
        #print(show_makkarat)
        """