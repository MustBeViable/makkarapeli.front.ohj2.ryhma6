import random

from Game.python.commands import input_in_section
from Game.python.game_texts import yes, no
from Game.python.sql_querys.money_function import fetch_player_money, update_player_money

def tuplaus(amount, times_player_have_doubled):
    """This function randomizes a number from 1 to 100 and checks if it's more than 50. If it is player wins.
    It reduces chances to win by every new doubling situation. If player wins it doubles the money, if he loses it returns 0"""
    luckynumber = random.randint(1, 100)
    player_number = luckynumber - (times_player_have_doubled * 5)
    casinos_number = 100 - luckynumber + (times_player_have_doubled * 5)
    if player_number >= casinos_number:
        amount = amount * 2
        return amount
    else:
        amount = 0
        return amount

def tuplataanko(answer, winnings, game_id):
    """This function asks does player wants to double his money and also checks that they do not have any money left."""
    times_player_have_doubled = 0
    current_money = fetch_player_money(game_id)
    while answer == yes and winnings > 0:
        if answer == yes:
            winnings = tuplaus(winnings, times_player_have_doubled)
            times_player_have_doubled += 1
            if winnings > 0:
                answer = input_in_section(game_id, f"Roskiksen keiju tarjoaa mahdollisuuden tuplata tämän rahan."
                    f" Mitä vastaat? ({yes}/{no}): ").lower()
            else:
                break
    current_money += winnings
    update_player_money(current_money ,game_id)
    print(f"Sinulla on tällä hetkellä rahaa {current_money}€.")