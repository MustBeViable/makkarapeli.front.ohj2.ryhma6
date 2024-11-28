# All the commands that the user can give.
import mysql.connector

yes = "k"
no = "e"
approve = "n"
cancel_command = "palaa"
continue_old_game_command = "j"
create_new_game_command = "u"
sign_up = "uusi"
sign_in = "kirjaudu"

start_money = 1000
start_score = 0
start_mustamakkara = 0
start_location = "EFNU"
sausage_price = 100
finnair_makkara = 69420
finnair_donation = 500
price_multiplier = 50

# Basic commands
commands_command = "komennot"
help_command = "ohje"
money_command = "bank"
makkaras_command = "makkarat"
score_command = "pisteet"
profile_command = "profiili"
hole_command = "kolo"
top_command = "top"
give_up_command = "luovuta"
end_command = "lopeta"

# Dictionary of commands that are normally available and their help texts.
command_and_helptext = {
    commands_command: "Näyttää peruskomennot.",
    help_command: "Näyttää ohjeen.",
    money_command: "Näyttää omat rahasi.",
    makkaras_command: "Näyttää omat makkarasi.",
    score_command: "Näyttää pisteesi.",
    profile_command: "Näyttää sijaintisi, rahasi, pisteesi ja makkaroidesi määrän.",
    hole_command: "Mikäli Kolovastaava on vienyt makkaroitasi, voit etsiä koloa.",
    top_command: "Näyttää omien peliesi sekä kaikkien pelaajien top-listat.",
    give_up_command: "Lopettaa pelin. Luovuttamisen jälkeen et voi enää jatkaa kyseistä pelikertaa.",
    end_command: "Sulkee pelin. Edistymisen tallentuu automaattisesti ja voit palata jatkamaan peliä profiilistasi."
}

# Game texts.

give_screen_name_str = f'Anna käyttäjänimi. Voit palata takaisin kirjoittamalla "{cancel_command}".\n'
sign_in_or_up_str = f'Kirjoita "{sign_in}" jos haluat kirjautua sisään. Kirjoita "{sign_up}" jos haluat luoda uuden käyttäjätunnuksen.\n'

not_command_str = (' ei  ole komento. '
                   'Komennolla "komennot" näet kaikki peruskomennot. ')

game_instruction_str = (f'PELIN OHJE\n'
                        f'Sinulta kysytään kysymys. Kirjoita konsoliin haluamasi vastaus ja paina enter. '
                        f'Voit kirjoittaa myös jonkin peruskomennoista (katso alta).\n')

game_goal_str = (f'PELIN TAVOITE\n'
                 f'Pelin tavoite on kerätä mahdollisimman paljon makkaroita ja siten kerryttää pistesaalista.\n'
                 f'Makkaroita voi ostaa lentokenttien Tax free -myymälöistä. Kullakin maalla on oma makkaransa.\n'
                 f'Erilaisista makkaroista saa eri määrän pisteitä.\n'
                 f'Peli päättyy, kun sinulla ei ole enää rahaa ostaa lentolippua.'
                 f'Edistymisesi tallentuu automaattisesti.\n')

# String of commands and what they do
commands_str = f'PERUSKOMENNOT\n'

for com in command_and_helptext.keys():
    commands_str += f'{com}: {command_and_helptext[com]}\n'

# Combines all instructions to one manual.
give_help_str = (f"\n"
                 f"{game_instruction_str}\n"
                 f"{commands_str}\n"
                 f"{game_goal_str}")

garbage_can_question = f"Haluatko kaivaa roskista? ({yes}/{no})"
tax_free_question = f"Haluatko vierailla Tax Free -myymälässä? ({yes}/{no})"

airport_selection_question = f"Kävelet kohti lipunmyyntiautomaattia. Kirjoita {approve} nähdäksesi lähtevät lennot."

money_is_zero_str = "Rahasi loppuivat!"
no_money_for_flight_str = "Rahasi eivät riitä enää lentämiseen. "

yhteys = mysql.connector.connect(
         host='localhost',
         port=3306,
         database='flight_game',
         user='kolovastaava',
         password='kolovastaava',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

