from Game.python.game_texts import yhteys

def print_player_top5_list(ide):
    sql1 = (f" SELECT screen_name"
           f" FROM playthrough"
           f" WHERE id = {ide}")
    kursori1 = yhteys.cursor(dictionary=True)
    kursori1.execute(sql1)
    result = kursori1.fetchall()
    screen_name = result[0]['screen_name']
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough"
           f" WHERE screen_name = '{screen_name}'")
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
