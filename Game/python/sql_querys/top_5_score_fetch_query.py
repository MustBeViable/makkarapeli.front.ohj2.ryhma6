from Game.game_texts import yhteys


def print_all_players_top():
    sql = (f" SELECT screen_name, score"
           f" FROM playthrough")
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    result_sorted = sorted(result, key=lambda x: x['score'], reverse=True)
    print(f"Kaikkien pelaajien Top 5 tulokset: ")
    if len(result_sorted) < 5:
        for i in range(len(result_sorted)):
            print(f"{i + 1}. {result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f} pt")
    else:
        for i in range(5):
             print(f"{i + 1}. {result_sorted[i]['screen_name']}: {result_sorted[i]['score']:6.0f} pt")
    print("")
    return