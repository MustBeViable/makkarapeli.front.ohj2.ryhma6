from Game.python.sql_querys.fetch_player_makkaras import fetch_player_stolen_makkaras

def kolo_stolen_yes_no(game_id):
    stolen_amount=fetch_player_stolen_makkaras(game_id)
    if len(stolen_amount) == 0:
        result={"makkara":"not_stolen"}
        return result
    else:
        result = {"makkara": "stolen"}
        return result