Tässä tiedostossa esitellään pelin toiminta, tunnetut bugit ja jatkokehitysideat.

Ennen pelin käynnistämistä ensimmmäisen kerran tietokanta täytyy päivittää ajantasalle. 
Tietokannan pohjan saa luotua, kun uuteen tietokantaan tuo tiedoston lp.sql (kurssillaa saatu skripti).
Tämän jälkeen Game.game_texts-tiedostoon yhteys-muuttujaan täytyy vaihtaa juuri luodun tietokannan nimi, oma käyttäjätunnus ja salasana.
Puuttuvat taulut saa luotua tietokantaan ajamalla data_base_creation.py-tiedoston.

Peli ajetaan ajamalla api.py tiedosto. Html on tidostossa main_html.
Peliä pelataan selaimessa.

Aika ei riittänyt aivan kaiken tekemään täydelliseksi ja siksi pelissä on kehitettävää.
Tiedossa olevat bugit ja ongelmat:
1. Kaikkia funktioita ja koodia ei ole kommentoitu.
2. Macille sopiva tietokannan luontiskripti on piilossa.
   Korjattaisiin lisäämällä data_base_creationin luontiskriptiin komennot, jotka korjaavat komennot Macille sopiviksi.
   Vaihtoehtoisesti voitaisiin korjata siirtämällä database_creation_senja Game-repoon ja sitä käytettäisiin oletuksena.
3. Lentokentän valintanapit eivät kerro käyttäjälle, että käyttäjällä ei ole varaa lentää.


Esiprojektin jälkeen ehdimme korjata/toteuttaa seuraavat esiprojektista puuttuneet ominaisuudet:
1. Kun kolovastaava vie tai palauttaa makkaroita, käyttäjän pisteet eivät muutu. Pisteiden tulisi vähentyä makkaroiden lähtemisen myötä.
   Korjataan lisäämällä pelaajan pisteiden päivitys funktioihin, jotka päivittävät pelaajan makkaroiden stolen-tilan muutosta.
2. Tietyn maan makkarasta saa enemmän pisteitä, kun sen ostaa ensimmäisen kerran.
