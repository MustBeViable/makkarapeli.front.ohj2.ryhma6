
import mysql.connector


yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='sakari',
         password='Possu2929',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
#Tää funktio hakee 20 random kenttää ja saa sen nimen, maan ja leveys/pituuspiirit geopyy varten
def airportselection():
    sql = (f" Select airport.name as name, country.name as country, ident "
           f" from airport, country "
           f" where country.iso_country = airport.iso_country"
           f" and airport.type = 'large_airport'"
           f" and airport.name not like 'CLICK%'"
           f" order by rand()"
           f" limit 20 ")
    #kursori = yhteys.cursor(dictionary=true), muuttaa tuplen sijasta dictionaryks. Eli lista, jonka sisällä dictionary
    #kantsii käyttä jos useampi select (vaikka select name, ident, id...) ja muuttamalla select arvoja ei muuta printtiä
    #näi voi callaa avaimilla mm result['name']
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    result = kursori.fetchall()
    #tää for loop käy jokaisen dictionaryn listan sisältä ja ajaa distance funktion (selvittää etäisyyttä ks. alempaa)
    # Kun se o saanu etäisyyden se lisää arvon avaimeen 'distance'.
    for i in range(len(result)):
        dist = distance(result[i]['ident'])
        result[i]['distance'] = dist
        #print(i + 1)
        #print(result[i]["name"])
        #print(distance(result[i]['name']))

    #tää luo uuden listan jossa lista on sortattu distance avaimella suuruus järjestykee (key=lambda lambda x määrittää
    # tavan millä järjestely tehdään. x['distance'] tarkoittaa, että jokaiselle alkion (tässä tapauksessa sanakirjan)
    # osalta otetaan. järjestelyavaimeksi sen 'distance'-arvo. X viittaayhtee sanakirjaan ja x['distance'] sen sanakirjan
    # distance avaimen arvoon.) "key=lambda tarjoaa joustavan ja yksinkertaisen tavan järjestää tai käsitellä listan
    # elementtejä räätälöidyn avaimen perusteella."
    result_sorted = sorted(result, key=lambda x: x['distance'])
    #tässä printtaan saadut tulokset uudesta listasta ja järjestän ne indeksi+1 perusteella, jotta saan tulosteen alkamaan
    # 1 ja päättymään 20. Enamurate lisää iterointiin indeksin, jossa sit käydään listan elementtejä läpi (jossa airport
    # on elementti) läpi i indeksin avulla. Samalla saadaan ulos elementin että indeksin. (1 sanakirja= erillisen
    # lentokentän nimi, maakoodi ja etäisyys avain/arvo pareina).
    print("Seuraavat lähdöt: (lennon nro, maa, lentokenttä, hinta (€):")
    price_multiplier = 50
    for i, airport in enumerate(result_sorted):
        #print(f"{i + 1}. {airport['name']}: ({airport['distance']:.1f} km)")
        print(f"{i + 1:17.0f}. {airport['country']}: {airport['name']}  ({price_multiplier + i  * price_multiplier}) €)")
    print(result_sorted)
    next_airport = int(input("Valitse haluamasi uusi lentokenttä syöttämällä sen järjestysluku: "))
    price = price_multiplier + next_airport * price_multiplier
    rahan_vahennus(price)
    next_airport = result_sorted[next_airport-1]["ident"]
    new_location = current_coordinates(next_airport)
    global location
    location = new_location
    return new_location

#tää funktio saa ylemmän funktion lentokenttien nimet ja laskee sen etäisyyden nykyiseen lentokenttään (käytin baselinenä
#nummelan lentokenttää. Ei tartte ku laittaa päivittää current_airport pelaajan nykyisee sijaintii.
def distance(next_place):
    from geopy import distance
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{next_place}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    #nummelan tilalle laitetaa se kenttä mis pelaaja o sil hetkel.
    current_airport = currne()
    #current_airport = (60.3339, 24.2964)

    dist = distance.distance(current_airport, result[0]).km
    #print(dist)
    return dist
airportselection()
def current_coordinates(chosen_ICAO):
    sql = (f" select latitude_deg, longitude_deg "
           f" from airport "
           f" where ident = '{chosen_ICAO}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    return result[0]
current_airport("EFNU")

locatio = current_coordinates("EFNU")