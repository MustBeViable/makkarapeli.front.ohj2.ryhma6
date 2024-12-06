from Game.python.game_texts import yhteys

def country_code_for_flag(ide):
    sql = (f" SELECT airport.iso_country as country_code_for_flag"
           f" FROM playthrough"
           f" JOIN airport ON playthrough.player_location = airport.ident"
           f" WHERE playthrough.id = {ide}")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    country_code = kursori.fetchall()
    return country_code[0]