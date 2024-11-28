import mysql.connector

from Game.game_creation_lists.all_lists_etc import iso_country_list, makkaras_dictionary, score_value_makkara
from Game.game_texts import start_score, start_money, start_mustamakkara, start_location, yhteys

'''yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='kolovastaava',
         password='kolovastaava',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
'''


#Tehty toimimaan mun tietokantaan, eli pitäs lisätä funktio mikä antaa oikeudet aina kun pelataan eri koneella
# (eli pitää luoda funktio joka luo käyttäjän, hakee tietokannan ja antaa oikeudet). Toi kannattaa tarkistaa opelta
# onko tarpeellista. Se luo tablen, jonka jälkee se tekee joukon, mihin lisään jo tietokannassa olevat makkarat. Sen
# jälkee se lisää samaa joukkoon makkarat listasta. Tää estää duplikaatit.

#Tiedossa oleva ongelma: Jostai syystä aina uudestaa ajaessa lisää yhden luvun 0, 1, 2, 3...

#tämän koodin tomiakseen pitää antaa KAIKKI oikeudet tehdä muutoksia flight_game databasee
#esim käyttäen tietokantaa nimeltä flight_game "GRANT ALL ON flight_game.* TO (käyttäjänimi)@localhost;" Ja sit
#"flush privileges"

def table_check(table_name):
    sql = (f"show tables;")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    check_list = []
    for i in range(len(result)):
        check_list.append(result[i][0])
    if table_name in check_list:
        value = 1
    else:
        value = 0
    return value

#Luo käyttäjälle makkara tablen. Toimii vain jos käyttäjälle on annettu luvat. Ohjeet ylempänä.
def create_table_makkara():
    sql = (f" CREATE TABLE makkara (id int NOT NULL auto_increment,"
           f" name VARCHAR(255),"
           f" score int,"
           f" country varchar(255),"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def add_makkaras_to_table(makkara, country, score):
    sql = (f"INSERT INTO makkara (name, score, country) VALUES ('{makkara}', {score}, '{country}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


def create_makkara_reached():
    sql = (f" CREATE TABLE makkara_reached (id int NOT NULL auto_increment,"
           f" stolen BOOLEAN DEFAULT FALSE,"
           f" playthrough_id int,"
           f" makkara_id int,"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def create_playthrough(score, money, mustamakkara, location):
    sql = (f" CREATE TABLE playthrough (id int NOT NULL auto_increment,"
           f" score int DEFAULT {score},"
           f" money int DEFAULT {money},"
           f" screen_name VARCHAR(255),"
           f" finished BOOLEAN DEFAULT FALSE,"
           f" mustamakkara int DEFAULT {mustamakkara},"
           f" stolen_makkaras_iso_country VARCHAR(255) DEFAULT NULL,"
           f" player_location varchar(40) DEFAULT '{location}',"
           f" primary key (id))")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def foreign_keys_makkara_reached():
    sql = (f" ALTER TABLE makkara_reached"
           f" ADD CONSTRAINT FK_playthrough_id FOREIGN KEY (playthrough_id) REFERENCES playthrough(id),"
           f" ADD CONSTRAINT FK_makkara_id foreign key (makkara_id) references makkara(id)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
#Constraintin lisäämällä teet elämästä huomattavasti helpompaa kun poistat FK yhdistelmiä. Nimi voi olla muute hankala
def foreign_keys_playthrough():
    sql = (f" ALTER TABLE playthrough "
           f" ADD CONSTRAINT FK_location"
           f" FOREIGN KEY (player_location) REFERENCES airport(ident),"
           f" ADD CONSTRAINT FK_hole_airport"
           f" FOREIGN KEY (stolen_makkaras_iso_country) REFERENCES country(iso_country)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def foreign_keys_makkara():
    sql = (f" ALTER TABLE makkara"
           f" ADD CONSTRAINT FK_iso_country"
           f" FOREIGN KEY (country) REFERENCES country(iso_country)")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return


makkara = "makkara"
test1 = table_check(makkara)
#final_test arvoksi taululuontien määrä
final_test = 3
if test1 == 0:
    create_table_makkara()
    for i in range(len(iso_country_list)):
        add_makkaras_to_table(list(makkaras_dictionary.values())[i],iso_country_list[i],score_value_makkara[i])
    final_test -= 1
    print("t1")
    print(final_test)
makkara_reached = "makkara_reached"

test2 = table_check(makkara_reached)
if test2 == 0:
    create_makkara_reached()
    final_test -= 1
    print("t2")
    print(final_test)
playthrough = "playthrough"
test3 = table_check(playthrough)

if test3 == 0:
    create_playthrough(start_score, start_money, start_mustamakkara, start_location)
    final_test -= 1
    print("t3")
    print(final_test)

if final_test == 0:
    foreign_keys_makkara_reached()
    print("fk makkara reached tehty")
    foreign_keys_playthrough()
    print("fk playthrough tehty")
    foreign_keys_makkara()
    print("fk makkara tehty")
