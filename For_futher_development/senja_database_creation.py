from Game.game_creation_lists.iso_country_list import iso_country_list
from Game.game_creation_lists.makkaras_dictionary import makkaras_dictionary
from Game.game_creation_lists.score_value_makkara import score_value_makkara
from Game.game_texts import yhteys, start_location

start_score = 0
start_money = 2000
start_mustamakkara = 0
kursori = yhteys.cursor()

tables = ['makkara_reached', 'makkara', 'playthrough']
for table in tables:
    kursori.execute(f"DROP TABLE IF EXISTS {table}")
    print(f"dropped table {table}")

sql_playthrough1 = (f"DROP TABLE IF EXISTS playthrough;")
sql_playthrough2 = (f" CREATE TABLE IF NOT EXISTS playthrough ("
                    f" id           int NOT NULL AUTO_INCREMENT,"
                    f" score        int         DEFAULT {start_score},"
                    f" money        int         DEFAULT {start_money},"
                    f" screen_name  varchar(40),"
                    f" finished     boolean     DEFAULT false,"
                    f" mustamakkara int         DEFAULT 0,"
                    f" stolen_makkaras_iso_country varchar(40) DEFAULT NULL,"
                    f" player_location     varchar(40) DEFAULT '{start_location}',"
                    f" PRIMARY KEY (id),"
                    f" FOREIGN KEY (stolen_makkaras_iso_country)"
                    f" REFERENCES country(iso_country),"
                    f" FOREIGN KEY (player_location)"
                    f" REFERENCES airport(ident))"
                    f" ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci")

sql_makkara1 = (f" DROP TABLE IF EXISTS makkara;")
sql_makkara2 = (f" CREATE TABLE IF NOT EXISTS makkara ("
                f" id        int NOT NULL AUTO_INCREMENT,"
                f" name      varchar(255),"
                f" score     int,"
                f" country   varchar(255),"
                f" PRIMARY KEY (id),"
                f" FOREIGN KEY (country)"
                f" REFERENCES country(iso_country))"
                f" ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci")

sql_makkara_reached1 = (f" DROP TABLE IF EXISTS makkara_reached;")
sql_makkara_reached2 = (f" CREATE TABLE IF NOT EXISTS makkara_reached("
                        f" id            int NOT NULL AUTO_INCREMENT,"
                        f" stolen BOOLEAN DEFAULT false,"
                        f" playthrough_id       int,"
                        f" makkara_id    int,"
                        f" PRIMARY KEY (id),"
                        f" FOREIGN KEY (playthrough_id)"
                        f" REFERENCES playthrough(id) "
                        f" ON DELETE CASCADE"
                        f" ON UPDATE CASCADE,"
                        f" FOREIGN KEY (makkara_id)"
                        f" REFERENCES makkara(id)"
                        f" ON DELETE CASCADE"
                        f" ON UPDATE CASCADE)"
                        f" ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci")


def add_makkaras_to_table(makkara, country, score):
    sql = (f"INSERT INTO makkara (name, score, country) VALUES ('{makkara}', {score}, '{country}')")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
    for i in range(len(iso_country_list)):
        add_makkaras_to_table(list(makkaras_dictionary.values())[i], iso_country_list[i], score_value_makkara[i])


kursori.execute(sql_playthrough1)
kursori.execute(sql_playthrough2)
print("Playthrough luotiin.")

kursori.execute(sql_makkara1)
kursori.execute(sql_makkara2)
print("Makkara luotiin.")

kursori.execute(sql_makkara_reached1)
kursori.execute(sql_makkara_reached2)
print("Makkara_reached luotiin.")

for i in range(len(iso_country_list)):
    add_makkaras_to_table(list(makkaras_dictionary.values())[i], iso_country_list[i], score_value_makkara[i])
