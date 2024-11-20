#Tää puuttu kokonaan nii ei tee sql hakua
from Game.game_texts import yhteys

#lisäsin toiset parametrit molempiin eli game_id, johon syötetään sen pelikerran id. Päivittää siis oikeita tietoja.
# Sama alempaa funktioon. Muutin myös tablen oikeaksi. SQL komento ei tarvitse ";" suorittaakseen oikein.
def add_money(amount, game_id):
    sql = (f"UPDATE playthrough SET money = {amount} WHERE id = '{game_id}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
#lisäsin tänne sen game_id parametrin jotta päivitetään aina oikeaa tietoa. Se tuo myös funktion sisällä add_money
# funktioon saman tiedon ja mulla toimi oikein toi nyt.
def use_money( game_id):
    sql = (f"SELECT money FROM playthrough WHERE id = '{game_id}'")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    player_money = result[0]['money']
    print(player_money)

    return

use_money(1)