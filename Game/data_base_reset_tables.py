from game_texts import yhteys

def table_remove(table):
    sql = "DROP TABLE {table} "
    kursori = yhteys.cursor()
    kursori.execute(sql.format(table=table))
    return

def drop_constraint(table, constraint):
    sql = (f" ALTER TABLE {table}"
           f" DROP CONSTRAINT {constraint}")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
#lisää listaa tablen nimi ku lisäät uuden tablen tietokantaa
test_list = ["makkara_reached", "makkara", "playthrough"]
'''
drop_constraint("playthrough", "FK_location")
drop_constraint("makkara_reached", "FK_makkara_id")
drop_constraint("makkara_reached", "FK_game_id")
drop_constraint("makkara", "FK_iso_country")
'''
for i in test_list:
    table_remove(table=i)
    print(i)