from Game.python.sql_querys.makkara_sql_haku import search_makkara_score, search_amount_of_local_makkara, \
    search_amount_of_any_makkara, search_any_makkara_score

multiplier = 5

def count_local_makkara_score(game_id):
    """ Counts the score which the player will get when buying the local makkara.
    The score is reduced by a fifth each time the player buys the same makkara again
    until the score is a fifth of the original score."""
    default_score = search_makkara_score(game_id)
    amount = search_amount_of_local_makkara(game_id)
    score = max(default_score - (amount * (default_score // multiplier)), default_score // multiplier)
    return score

def count_makkara_score(game_id, makkara_id):
    """ Checks the score of a makkara given as parameter."""
    default_score = search_any_makkara_score(makkara_id)
    amount = search_amount_of_any_makkara(game_id, makkara_id)
    score = max(default_score - (amount * (default_score // multiplier)), default_score // multiplier)
    return score


"""
print(search_makkara_score(42))
print(count_makkara_score(42))
print(search_makkara_score(41))
print(count_makkara_score(41))
makkara_default_score = score_value_makkara
amount_of_makkara = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for default_score in makkara_default_score:
    print('\nUusi')
    for amount in amount_of_makkara:
        print(max(default_score - (amount * (default_score // 5)), default_score // 5))
"""