from functions import *
from db_connection import connection
from config import config

cursor = connection.cursor()


def find_city_index(city_name, city_list):
    for index, city_data in enumerate(city_list):
        if city_data[1] == city_name:
            return index


def travel_fly(parameter, player):
    # player-muuttujassa tuodaan koko vuorossa olevan pelaajan rivi tietokannasta
    current_player_id = str(player[0])  # pelaajan id stringinä
    available_cities = get_cities_in_range("fly", player)  # fly-parametri tätä funktiota varten
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])  # lambda-funktio järjestää etäisyyden mukaan
    # pienimmästä etäisyydestä suorimpaan listan saavuttettavissa olevista kaupungeista
    if parameter == "?":  # Tämä tulostaa pelaajalle saavutettavissa olevat kaupungit
        print_available_cities("fly", sorted_available_cities, current_player_id)
        return True  # koska tämän jälkeen pelaaja voi valita mihin lentää, tai tehdä muun toiminnon
    elif parameter != "?":  # käsittelee kohdekaupungiksi syötetyn parametrin
        for city in available_cities:
            if city[1].lower() == parameter:
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                remove_pp(city[4], current_player_id)  # vähennetään lennon hinta pelaajan rahoista
                print("You begin your flight to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                input("<Press ENTER to continue>")
                print(f"You are now in {parameter}.\n")
                event_randomizer(player)
                return False  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
    else:
        print("Something is wrong here")
        return True


def travel_sail(parameter, player):
    # player-muuttujassa tuodaan koko vuorossa olevan pelaajan rivi tietokannasta
    current_player_id = str(player[0])  # pelaajan id stringinä
    available_cities = get_cities_in_range("boat", player)  # boat-parametri tätä funktiota varten
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])  # lambda-funktio järjestää etäisyyden mukaan
    # pienimmästä etäisyydestä suorimpaan listan saavuttettavissa olevista kaupungeista
    if parameter == "?":  # Tämä tulostaa pelaajalle saavutettavissa olevat kaupungit
        print_available_cities("boat", sorted_available_cities, current_player_id)
        return True  # koska tämän jälkeen pelaaja voi valita mihin lentää, tai tehdä muun toiminnon
    elif parameter != "?":  # käsittelee kohdekaupungiksi syötetyn parametrin
        for city in available_cities:
            if city[1].lower() == parameter:
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                remove_pp(city[4], current_player_id)  # vähennetään laivamatkan hinta pelaajan rahoista
                set_lockstate(city[3], player[0], 0, "sail")
                print("You begin sailing to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                event_randomizer(player)
                input("<Press ENTER to continue>")
                break
        return False  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
    else:
        print("Something is wrong here")
        return True


def travel_hitchhike(parameter, player):
    # player-muuttujassa tuodaan koko vuorossa olevan pelaajan rivi tietokannasta
    current_player_id = str(player[0])  # pelaajan id stringinä
    available_cities = get_cities_in_range("hike", player)  # hike-parametri tätä funktiota varten
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])  # lambda-funktio järjestää etäisyyden mukaan
    # pienimmästä etäisyydestä suorimpaan listan saavuttettavissa olevista kaupungeista
    if parameter == "?":  # Tämä tulostaa pelaajalle saavutettavissa olevat kaupungit
        print_available_cities("hike", sorted_available_cities, current_player_id)
        return True  # koska tämän jälkeen pelaaja voi valita mihin lentää, tai tehdä muun toiminnon
    elif parameter != "?":  # käsittelee kohdekaupungiksi syötetyn parametrin
        for city in available_cities:
            if city[1].lower() == parameter:
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                print("city dist: " + str(city[3]))
                set_lockstate(city[3], player[0], 0, "hike")
                print("You begin your hitchhike to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                event_randomizer(player)
                input("<Press ENTER to continue>")
                return False  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
    else:
        print("Something is wrong here")
        return True


def work(parameter, player):
    if parameter == "?":
        print("This should list all available jobs.")
        return True
    print('You start working.')
    print(parameter)
    return False
    # This function is a stub.
    # You can contribute to the function


def search(player):
    sql = (f"SELECT bag_city FROM city inner join player on "
           f"city.id = player.location and player.screen_name = '{player[1]}'")
    cursor.execute(sql)
    result = cursor.fetchall()
    if result[0][0] == 1:
        print('Congratulation you have found grandma`s lost luggage!!! Be fast and head back to Helsinki before anyone '
              ' else does!')
    else:
        item_name, item_value = item_randomizer()
        print(f'Nah! No grandma`s luggage in here! But you found {item_name} and it`s worth {item_value}')
        if item_value <= 0:  # Tällä hetkellä tietokannassa ei ole itemeitä mistä menettää rahaa. Voisi lisätä...? :)
            remove_pp(item_value, player[0])  # player 0 on id
        elif item_value >= 0:
            add_pp(item_value, player[0])
    input("<Press ENTER to continue>")
    return False


def hire(player):
    price_multiplier_dict = {
        "hire": config.get('config', 'HiringPrice')
    }
    price_hire = int(price_multiplier_dict["hire"])
    player_id = str(player[0])
    print(f"You hire a local detective to look for your grandma's suitcase. Cost is {price_hire}.")
    yes_no = input("Do you want to hire a detective? y/n: ")
    if yes_no == "y":
        player_location = str(player[8])
        if player[2] > price_hire:
            remove_pp(price_hire, player[0])
            sql = "SELECT bag_city FROM city INNER JOIN player ON city.id = player.location"
            sql += f" WHERE player.location = '{player_location}'"
            cursor.execute(sql)
            result = list(cursor.fetchall())
            if result[0] == 1:
                sql = f"UPDATE player SET prizeholder = 1 WHERE id = '{player_id}'"
                cursor.execute(sql)
                print("You found grandmas luggage!")

            else:
                print("Nothing found from this city.")

        elif player[2] < price_hire:
            print("You dont have enough pp to hire detective.")

    elif yes_no == "n":
        print("You didnt hire a detective.")
    return True


def manual(parameter, player):
    # manuaalia voisi laajentaa
    manual_dictionary = {
        'help': "[help] prints all available user commands.",
        'fly': "You can fly to another city with command [fly]. To show all available\n"
               "destinations and prices use [fly ?]. To start flying to the city of your choosing\n"
               "type [fly 'city_name'].\n"
               "Flying is the fastest form of travel and ",
        'sail': "You can sail to another city with command [sail]. To show all available\n"
                "destinations, prices and how many turns the trip will take, type [sail ?].\n"
                " To start sailing to the city of your choosing, type [sail 'city_name'].",
        'hike': "You can hitchhike to another city with command [hike]. Show all available destinations and \n"
                "an approximation on how many turns the trip will take with command [hike ?].\n"
                "To start hitchhiking to the city of your choosing, type [hike 'city_name'].\n"
                "You never know if strangers will let you in their car, so hitchhiking is luck-based.",
        'hire': "You can [hire] a private detective to search for grandma's suitcase. Hiring a detective will cost\n"
                "you " + config.get('config', 'HiringPrice') + " PP. If you hire one, you wont use your turn, but you "
                                                               "also cannot find any cool stuff you might \n"
                                                               "come by when searching yourself.",
        'work': "This is a placeholder for work manual entry. Work has not been yet implemented to the game.",
        'search': "You can [search] for grandma's suitcase in your current location. Searching for yourself will\n"
                  "also end your turn, but you can find lots of cool stuff when searching yourself. If you dont wish\n"
                  "to use your turn to search, you can [hire] a private detective instead.",
        'exit': "[exit] will end the game running and hopefully save your progress.",
        'man': "You dirty bastard, trying to break me are you?"
    }
    print(manual_dictionary[parameter])
    input("<Press ENTER to continue>")
    return True  # Lisätty perään ettei vuoro vaihdu jos käyttää man toimintoa.


def help_function(player):
    # nykyisellään oleva manual.dictionaryn arvot voisi tulostua avainten kanssa
    print("You can use these commands:")
    for key in command_dictionary.keys():
        print(key)
    print("For more information about a certain command, type [man 'command'].")
    return True


command_dictionary = {
    'help': help_function,
    'status': printer,
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
commands_without_parameter = ["status", "search", "hire", "help", "exit"]


# Koska osa funktioista kutsutaan parametrin kanssa, tämä väistää errorin käytettäessä listattuja funktioita


def user_input_processor(input_string, current_player):
    # Tämä funktio käsittelee käyttäjäsyötteen:
    # splittaa välilyönnistä listaksi
    input_as_list = input_string.lower().strip().split()
    # etsii listan ensimmäistä alkiota vastaavaa arvoa command_dictionarysta
    selected_function = command_dictionary[input_as_list[0]]
    # Jos käyttäjä ei antanut parametria:
    if len(input_as_list) < 2 and input_as_list[0] in commands_without_parameter:
        return selected_function(current_player)
        # Kutsuu funktion ilman parametria
    elif len(input_as_list) == 2:
        return selected_function(input_as_list[1], current_player)
        # kutsuu funktion käyttäen listan toista alkiota parametrina
    else:
        print("Bad parameters.")
        return True
        # Todennäköisesti parametri puuttuu tai niitä on annettu kaksi
# HUOM!! Jos importatussa pythonfilessä on jotain ajettavaa, se ajetaan automaattisesti importin yhteydessä.
