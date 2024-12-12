Tässä tiedostossa esitellään pelin toiminta, tunnetut bugit ja jatkokehitysideat.

Ennen pelin käynnistämistä ensimmmäisen kerran tietokanta täytyy päivittää ajantasalle. 
Tietokannan pohjan saa luotua, kun uuteen tietokantaan tuo tiedoston lp.sql (kurssillaa saatu skripti).
Tämän jälkeen Game.game_texts-tiedostoon yhteys-muuttujaan täytyy vaihtaa juuri luodun tietokannan nimi, oma käyttäjätunnus ja salasana.
Puuttuvat taulut saa luotua tietokantaan ajamalla data_base_creation.py-tiedoston.

Peli ajetaan ajamalla api.py tiedosto. Html on tidostossa main_html.
Peliä pelataan selaimessa.

Aika ei riittänyt aivan kaiken tekemiseksi täydelliseksi ja siksi pelissä on kehitettävää.
Tiedossa olevat ongelmat/parannusehdotukset:

1. Lentokentän valinta ei kerro käyttäjälle, että käyttäjällä ei ole varaa lentää valittuun kohteeseen. Taxfree ei kerro, että pelaajalla ei ole varaa makkaraan.
2. Macille sopiva tietokannan luontiskripti on piilossa.
   Korjattaisiin lisäämällä data_base_creationin luontiskriptiin komennot, jotka korjaavat komennot Macille sopiviksi.
   Vaihtoehtoisesti voitaisiin korjata siirtämällä database_creation_senja Game-repoon ja sitä käytettäisiin oletuksena.
3. JavaScriptissä on testiprinttejä. Ne eivät sinänsä häiritse, mutta koodi olisi siistimpää ilman.


Esiprojektin jälkeen ehdimme korjata/toteuttaa seuraavat esiprojektista puuttuneet ominaisuudet:
1. Kun kolovastaava vie tai palauttaa makkaroita, käyttäjän pisteet eivät muuttuneet. Nyt pisteet vähenevät, kun kolovastaava vie makkaroita ja palaavat takaisin, kun kolo löytyy.
2. Tietyn maan makkarasta saa enemmän pisteitä, kun sen ostaa ensimmäisen kerran. Parin ostokerran jälkeen pisteitä ei saa ollenkaan.
