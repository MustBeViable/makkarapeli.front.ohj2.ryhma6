import random

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
