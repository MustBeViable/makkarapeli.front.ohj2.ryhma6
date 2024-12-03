from Game.python.game_texts import yhteys


def print_all_players_top():
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    result_sorted = sorted(result, key=lambda x: x['score'], reverse=True)
    if len(result_sorted) < 5:
        return result_sorted
    else:
        top_5 = {}
        for i in range(5):
             top_5[i+1] = result_sorted[i]
        return top_5

print(print_all_players_top())