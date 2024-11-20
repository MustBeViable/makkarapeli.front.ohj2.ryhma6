# 10% mahis finnair_personnel, 10% mahis kolovastaavalle, 10% mahis rosvolle, 10 % musta makkara, 60% mahis voittaa rahaa

import random

from Game.Game_ascii_art.finnair_ascii import finnair_ascii
from Game.Game_ascii_art.hole_in_charge_ascii import hole_in_charge_ascii
from Game.Game_ascii_art.money_found_garbage_can import happy_garbage_can
from Game.Game_ascii_art.robber_from_garbage_can import robber_2
from Game.game_texts import no, yes, yhteys, finnair_makkara, finnair_donation
from For_futher_development.secret_black_sausage import secret_black_sausage_chance, amount
from Game.doubling_machine import tuplataanko
from Game.sql_querys.fetch_player_makkaras import fetch_player_makkaras
from Game.sql_querys.money_function import update_player_money, fetch_player_money
from Game.sql_querys.score_fetch_and_score_update_querys import player_score_fetch, player_score_update


def robber(id, player_money):
    """robber reduces half of the player's money"""
    if player_money == 1:
        aft_rob = player_money - 1
        return aft_rob
    else:
        aft_rob = player_money * 0.5
        update_player_money(aft_rob, id)
    return aft_rob


def hole_in_charge(game_id):
    """This is hole in charge function and uses sql query from another file."""
    own_makkaras = fetch_player_makkaras(game_id)
    print("Törmäsit kolovastaavaan!")
    if len(own_makkaras) == 0:
        print("Tällä kertaa sinulla ei ollut makkaraa vietävänä.")
    else:
        # Devided by five (like 20%) and rounded down
        num_to_lose = len(own_makkaras) // 5

        # Varmistetaan, että vähintään yksi makkara otetaan
        if num_to_lose == 0 and len(own_makkaras) > 0:
            num_to_lose = 1

        # A random number of sausages (num_to_lose) is selected to remove
        lost_makkaras = random.sample(own_makkaras, num_to_lose)

        # The selected sausages are removed from original list and added to hole in charge's list
        for makkara in lost_makkaras:
            sql = (
                f"UPDATE makkara_reached SET stolen = True WHERE id IN (SELECT id FROM makkara_reached WHERE id = {makkara})")
            kursori = yhteys.cursor()
            kursori.execute(sql)
        print(
            f"Harmi makkaravarastosi kannalta, sillä kolovastaava vei sinulta makkaroita {len(lost_makkaras)} kpl.")
    return


def finnair_personnel(game_id):
    """Player can donate 500 euros and get rare sausage"""
    from Game.commands import input_in_section
    print(f"Finnairin ympäristöedustaja pyytää lahjoitusta. Sen arvo on {finnair_donation}€.")
    current_money = fetch_player_money(game_id)
    answer = input_in_section(game_id, f"Haluatko antaa lahjoituksen? Sinulla on tällä hetkellä {current_money}€. ({yes}/{no}): ").lower()

    while answer not in [yes, no]:
        answer = input_in_section(game_id, f"Älä änkytä!!! {yes}/{no}")

    if answer == yes:
        if current_money >= 500:
            print(
                f"Onnittelut hyvistä päätöksistä! Pitkäjänteisyytesi ja lahjoitustesi ansiosta olet saanut harvinaisen "
                f"makkaran, jota Kolovastaavakaan ei voi varastaa.")
            money = fetch_player_money(game_id)
            money -= finnair_donation
            update_player_money(money, game_id)
            score = player_score_fetch(game_id)
            score += finnair_makkara
            player_score_update(score, game_id)
        else:
            print("Rahat eivät riitä")
            return


def money_from_garbage():
    """This randomizes how much money you can get"""
    new_money = random.randint(200, 1000)
    return new_money


def garbage_can(game_id):
    """This is the main carbage can function, and it is checkng garbages with its all features (money found, robber,
    hole in charge, finnair personnel"""
    from Game.commands import input_in_section
    outcome = \
    random.choices(['found_money', 'robber', 'hole_in_charge', 'finnair_personnel'], weights=[70, 10, 10, 10], k=1)[0]
    if outcome == 'found_money':
        print(happy_garbage_can)
        new_money = money_from_garbage()
        print(f"Onneksi olkoon, löysit rahaa {new_money}€!")
        vastaus = input_in_section(game_id,
            f"Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan! Mitä vastaat?  ({yes}/{no}): ").lower()
        tuplataanko(vastaus, new_money, game_id)  # eliaksen tuplaus funktio
    elif outcome == 'robber':
        print(robber_2)
        current_money = fetch_player_money(game_id)
        if current_money > 0:
            print(
                f"Tulit ryöstetyksi! Rosvo vei merkittävän osan rahoistasi ja sinulle jäi {robber(game_id, current_money)} €.")
        else:
            print("Rosvo ei löytänyt ryöstettävää.")
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
        secret_black_sausage_chance(amount)  # saken mustamakkara funktio
    return



