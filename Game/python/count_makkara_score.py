from Game.python.sql_querys.makkara_sql_haku import search_makkara_score, search_amount_of_local_makkara, \
    search_amount_of_any_makkara, search_any_makkara_score

multiplier = 3

def count_local_makkara_score(game_id):
    """ Counts the score which the player will get when buying the local makkara.
    The score is reduced by a quarter each time the player buys the same makkara again
    until the score is 0."""
    default_score = search_makkara_score(game_id)
    amount = search_amount_of_local_makkara(game_id)
    score = max(default_score - default_score / multiplier * amount, 0)
    return score

def count_makkara_score(game_id, makkara_id):
    """ Checks the score of a makkara given as parameter."""
    default_score = search_any_makkara_score(makkara_id)
    amount = search_amount_of_any_makkara(game_id, makkara_id)
    score = max(default_score - default_score / multiplier * amount, 0)
    return score