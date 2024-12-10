
from Game.python.game_texts import yhteys



def update_player_money(amount, game_id):

    """Updates player money, parametreina new money amount and game_id"""

    sql = (f"UPDATE playthrough SET money = {amount} WHERE id = '{game_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return



def fetch_player_money(playthrough_id):

    """Fetches player moneys from database and returns a dictionary like: {'money': '500'}"""

    sql = (f"SELECT money FROM playthrough WHERE id = '{playthrough_id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    player_money = result[0]
    return player_money

