from functions import *


def travel_fly(parameter):
    # Lentokohteen valinta ja kohteiden listaus
    current_player_id = get_player_data_as_list()[get_round_number() % 2][0]
    if parameter == "?":
        available_cities = get_cities_in_range("fly", current_player_id, 1)
        print("---Available cities where you can fly---\n")
        for key, value in available_cities:
            print(f"{key}: {value.2f} km away")
        print(f"Current PP: {current_pp[0]}")
        print(f"Location: {current_location[0][0]}")
        print(f"Lock state: {lock_status}")
        print("This should list all available cities where player can fly.")
    print("You begin your flight to " + parameter + ".")
    # Muuten funktion ajo suunnilleen:
    # Vaihda pelaajan sijainti=parametri
    # Vaihda pelaajan current_PP -= lennon hinta
    # Rollaa random event
    # Tulosta lennon päättyneen parametri-sijaintiin
    # next turn


def travel_sail(parameter):
    if parameter == "?":
        print("This should list all available cities where player can sail.")
    print('You start sailing to ' + parameter + '.')
    # Muuten funktion ajo suunnilleen:
    # Vaihda pelaajan sijainti=parametri
    # Vaihda pelaajan current_PP -= laivamatkan hinta
    # Rollaa random event
    # lockstate = laivamatkan kesto
    # tulosta "Olet matkalla xxxxx"
    # next turn


def travel_hitchhike(parameter):
    if parameter == "?":
        print("This should list all available cities where player can hitchhike.")
    print('You start hitchhiking to ' + parameter + '.')
    # Funktion ajo:
    # Laske etäisyys parametrina annettuun kaupunkiin
    # Etäisyydestä lockstaten total roll amount
    # Kutsu roll-funktiota ja addaa totaliin
    # next turn


def work(parameter):
    if parameter == "?":
        print("This should list all available jobs.")
    print('You start working.')
    print(parameter)
    # This function is a stub.
    # You can contribute to the function

def search():
    print("NOTE: Look up if player.location is also a bag_city")
    print("You search for grandma's suitcase, but it isn't here.")
    # Checkaa onko player.location bag_city
    # jos on, playeristä tulee laukunkantaja
        # player.location ei ole enää bag_city
        # Tulosta laukun löytyneen
        # next turn



def hire():
    print("NOTE: Look up if player.location is also a bag_city")
    print("You hire a local detective to look for your grandma's suitcase.")
    # Checkaa onko player.location bag_city
    # jos on, playeristä tulee laukunkantaja
    # player.location ei ole enää bag_city
    # Tulosta laukun löytyneen
    # Tämä ei päätä vuoroa


def manual(parameter):
    # manuaalia voisi laajentaa
    manual_dictionary = {
        'help': "[help] prints all available user commands.",
        'fly': "You can fly to another city with command [fly]. To show all available\n"
                "destinations and prices use [fly ?]. To start flying to the city of your choosing\n"
                "type [fly 'cityname'].\n"
                "Flying is the fastest form of travel and ",
        'sail': "You can sail to another city with command [sail]. To show all available\n"
                "destinations, prices and how many turns the trip will take, type [sail ?].\n"
                " To start sailing to the city of your choosing, type [sail 'cityname'].",
        'hike': "You can hitchhike to another city with command [hike]. Show all available destinations and \n"
                "an approximation on how many turns the trip will take with command [hike ?].\n"
                "To start hitchhiking to the city of your choosing, type [hike 'cityname'].\n"
                "You never know if strangers will let you in their car, so hitchhiking is luck-based.",
        'work': "This is a placeholder for work manual entry. Work has not been yet implemented to the game.",
        'search': "This is a placeholder for search manual entry",
        'exit': "[exit] will end the game running and hopefully save your progress.",
        'man': "You dirty bastard, trying to break me are you?"
        }
    print(manual_dictionary[parameter])


def help_function():
    # nykyisellään oleva manual.dictionaryn arvot voisi tulostua avainten kanssa
    print("You can use these commands:")
    for key in command_dictionary.keys():
        print(key)
    print("For more information about a certain command, type [man command].")


command_dictionary = {
    'help': help_function,
    'fly': travel_fly,
    'sail': travel_sail,
    'hike': travel_hitchhike,
    'work': work,
    'search': search,
    'hire': hire,
    'exit': exit,
    'man': manual
}
# Tuodaan käyttäjän kutsuttavat funktiot ajoa varten, ne on kirjoitettu eri fileen selkeyden takia.
commands_without_parameter = ["search", "hire", "help", "exit"]
# Koska osa funktioista kutsutaan parametrin kanssa, tämä väistää errorin käytettäessä listattuja funktioita


def user_input_processor(input_string):
    # Tämä funktio käsittelee käyttäjäsyötteen:
    # splittaa välilyönnistä listaksi
    input_as_list = input_string.split()
    # etsii listan ensimmäistä alkiota vastaavaa arvoa command_dictionarysta
    selected_function = command_dictionary[input_as_list[0]]
    # Jos käyttäjä ei antanut parametria:
    if len(input_as_list) < 2 and input_as_list[0] in commands_without_parameter:
        selected_function()
        # Kutsuu funktion ilman parametria
    elif len(input_as_list) == 2:
        selected_function(input_as_list[1])
        # kutsuu funktion käyttäen listan toista alkiota parametrina
    else:
        print("Bad parameters.")
        # Todennäköisesti parametri puuttuu tai niitä on annettu kaksi
# HUOM!! Jos importatussa pythonfilessä on jotain ajettavaa, se ajetaan automaattisesti importin yhteydessä.
