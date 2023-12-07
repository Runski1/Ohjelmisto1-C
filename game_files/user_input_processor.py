from functions import *
from db_connection import connection
from config import config
from colorama import Fore

cursor = connection.cursor()  # Voi jos osaisimme luokkia ja olioita, tätä ei tarvittaisi täällä

'''
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
            if city[1].lower() == parameter.lower():
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                remove_pp(city[4], current_player_id)  # vähennetään lennon hinta pelaajan rahoista
                # print("You begin your flight to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                print(f"You are now in {parameter}.\n")
                input("<Press ENTER to continue>")
                return False  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
        print("City doesn't exist or it is out of range.")  # tämä fix, ettei pelaaja menetä vuoroaan typolla
        return True
    else:
        print("Something is wrong here")
        return True
'''
'''
def travel_sail(parameter, player):
    # player-muuttujassa tuodaan koko vuorossa olevan pelaajan rivi tietokannasta
    current_player_id = str(player[0])  # pelaajan id stringinä
    available_cities = get_cities_in_range("boat", player)  # boat-parametri tätä funktiota varten
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])  # lambda-funktio järjestää etäisyyden mukaan
    if check_if_in_port(player) is False:
        print("You are not in a port city, thus you cannot sail.")
        print(f"The nearest port to your current location is in {sorted_available_cities[0][1]}.")
        return True
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
                input("<Press ENTER to continue>")
                return False
        print("City doesn't exist or it is out of range.")  # tämä fix, ettei pelaaja menetä vuoroaan typolla
        return True
    else:
        print("Something is wrong here")
        return True
'''
'''
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
            if city[1].lower() == parameter.lower():
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                # print("city dist: " + str(city[3]))
                set_lockstate(city[3], player[0], 0, "hike")
                print("You begin your hitchhike to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                input("<Press ENTER to continue>")
                return False  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
        print("City doesn't exist or it is out of range.")  # tämä fix, ettei pelaaja menetä vuoroaan typolla
        return True
    else:
        print("Something is wrong here")
        return True
'''
'''
def work(parameter, player):  # Tämä on oikeastaan vain placeholder-funktio, jolla voi generoida rahaa
    if parameter == "?":
        print("This should list all available jobs.")
        return True
    elif parameter == "do":
        print('You start working.')
        salary = random.randint(100, 500)
        add_pp(salary, player[0])
        return False
    else:
        return False
'''
'''
def search(player):
    set_searched(player[6])
    if is_city_bag_city(player):
        print('Congratulation you have found grandma`s lost luggage!!! Be fast and head back to Helsinki before anyone '
              ' else does!')
        input("Press Enter to continue: ")
        bag_found(player)
    else:
        item_name, item_value = item_randomizer()
        print(f'Nah! No grandma`s luggage in here! But you found {item_name} and it`s worth {item_value}')
        if item_value <= 0:  # Tällä hetkellä tietokannassa ei ole itemeitä mistä menettää rahaa. Voisi lisätä...? :)
            remove_pp(item_value, player[0])  # player 0 on id
        elif item_value >= 0:
            add_pp(item_value, player[0])
    input("<Press ENTER to continue>")
    return False
'''
'''
def hire(player):
    price_multiplier_dict = {
        "hire": config.get('config', 'HiringPrice')
    }
    price_hire = int(price_multiplier_dict["hire"])
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
                print('Congratulation you have found grandma`s lost luggage!!! Be fast and head '
                      'back to Helsinki before anyone else does!')
                # input("Press Enter to continue: ")
                bag_found(player)
            else:
                print("Nothing found from this city.")
        elif player[2] < price_hire:
            print("You dont have enough EP to hire detective.")
    elif yes_no == "n":
        print("You didnt hire a detective.")
    return True
'''

def manual(parameter):
    manual_dictionary = {  # Manuaalientryt
        'help': f"{Fore.RED}help{Fore.GREEN} prints all available user commands.{Fore.RESET}",
        'fly': f"You can fly to another city with command{Fore.RED} fly{Fore.GREEN}. To show all available\n"
               f"destinations and prices use {Fore.RED}fly ?{Fore.GREEN}. To start flying to the city of your choosing\n"
               f"type {Fore.RED}fly '{Fore.GREEN}city_name{Fore.RED}'{Fore.GREEN}.\n"
               f"Flying is the fastest form of travel, but will cost you a lot of {Fore.BLUE}EP{Fore.GREEN}.{Fore.RESET}",
        'sail': f"{Fore.GREEN}You can sail to another city with command {Fore.RED}sail{Fore.GREEN}. To show all available\n"
                f"destinations, prices and how many turns the trip will take, type{Fore.RED} sail ?{Fore.GREEN}.\n"
                f" To start sailing to the city of your choosing, type{Fore.RED} sail '{Fore.GREEN}"
                f"city_name{Fore.RED}'{Fore.GREEN}.{Fore.RESET}",
        'hike': f"You can hitchhike to another city with command {Fore.RED}hike{Fore.GREEN}. Show all available "
                f"destinations and \n"
                f"an approximation on how many turns the trip will take with command{Fore.RED} hike ?{Fore.GREEN}.\n"
                f"To start hitchhiking to the city of your choosing, type {Fore.RED}hike '{Fore.GREEN}"
                f"city_name{Fore.RED}'{Fore.GREEN}.\n"
                f"You never know if strangers will let you in their car, so hitchhiking is luck-based.{Fore.RESET}",
        'hire': f"You can {Fore.RED}hire{Fore.GREEN} a private detective to search for grandma's suitcase"
                f". Hiring a detective will cost\n"
                f"you {Fore.BLUE}{config.get('config', 'HiringPrice')} "
                f"EP{Fore.GREEN}. If you hire one, you wont use your turn, but you "
                f"also cannot find any cool stuff you might \n"
                f"come by when searching yourself.{Fore.RESET}",
        'work': f"{Fore.GREEN}To work use the command {Fore.RED}work do {Fore.RESET}",
        'search': f"{Fore.GREEN}You can {Fore.RED}search{Fore.GREEN} for grandma's suitcase in your current location. Searching"
                  f" for yourself will\n"
                  f"also end your turn, but you can find lots of cool stuff when searching yourself. If you dont wish\n"
                  f"to use your turn to search, you can {Fore.RED}hire{Fore.GREEN} a private detective instead.{Fore.RESET}",
        'status': f"{Fore.GREEN}Prints you player status, it might be useful for ordinary human (it means you).{Fore.RESET}",
        'map':  f"{Fore.GREEN}Prints all cities, their visited status and distance from your sitting point to them.{Fore.RESET}",
        'exit': f"{Fore.RED}exit{Fore.GREEN} will end the game running and TOTALLY save your progress."
                f" ..For sure. I dare you to try.{Fore.RESET}",
        'man': f"{Fore.GREEN}Y{Fore.YELLOW}0{Fore.WHITE}u {Fore.RED}3{Fore.BLUE}1{Fore.GREEN}r{Fore.CYAN}7"
               f"{Fore.LIGHTYELLOW_EX}y {Fore.WHITE}B{Fore.GREEN}4{Fore.RED}5{Fore.MAGENTA}7{Fore.LIGHTRED_EX}a"
               f"{Fore.WHITE}R{Fore.LIGHTGREEN_EX}d{Fore.RED}, {Fore.GREEN}7{Fore.BLUE}r{Fore.RESET}Y{Fore.RED}1"
               f"{Fore.YELLOW}n{Fore.WHITE}g {Fore.RED}t{Fore.YELLOW}0 {Fore.RED}B{Fore.GREEN}r{Fore.BLUE}E"
               f"{Fore.WHITE}4{Fore.YELLOW}k {Fore.WHITE}m{Fore.RESET}E"f" {Fore.BLUE}4{Fore.YELLOW}r{Fore.RED}E "
               f"{Fore.GREEN}y{Fore.BLUE}0{Fore.WHITE}u{Fore.GREEN}?{Fore.RESET}"}  # have fun

    print(manual_dictionary[parameter])
    input("<Press ENTER to continue>")
    return True  # Lisätty perään ettei vuoro vaihdu jos käyttää man toimintoa.


def help_function():
    help_dictionary = {
        'help': "shows you all commands you can use",
        'man': f"[man {Fore.RED}'{Fore.GREEN}command{Fore.RED}'{Fore.GREEN}] prints you the manual entry for "
               f"certain command.",
        'status': "Prints your player status",
        'map': "Prints distance to all cities and if they have been visited or not.",
        'fly': "travel with an airplane, (or fly yourself, however you want to imagine it)",
        'sail': "it might seem slow, but trust me, you'll travel with a cruise ship and not an actual sailboat",
        'hike': "hitchhike your way around the NEU. Devs tell its safe, don't worry.",
        'work': "The Pinnacle of Procrastination, to be implemented",
        'search': "search for your grandma's luggage.",
        'hire': "hires a private detective to search for yourself. basically spend money to save one turn",
        'exit': "Crash your game on purpose and without error messages. *chuckle* Also might save your progress."
    }
    max_key_length = max(len(key) for key in help_dictionary.keys())
    print("Here is a list of all the available commands.")
    for key, value in help_dictionary.items():
        print(f"{Fore.RED}{key:<{max_key_length}} : {Fore.GREEN}{value}{Fore.RESET}")
    print(f"For more information about a certain command, type {Fore.RED}man "
          f"'{Fore.RESET}command{Fore.RED}'{Fore.RESET}.")
    input("<Press ENTER to continue>")
    return True  # nämä pitävät pelaajan vuoron päällä main loopissa


command_dictionary = {  # pelaajan komennot
    'help': help_function,
    'man': manual,
    'status': printer,
    'map': print_city_status,
    #'fly': travel_fly,
    #'sail': travel_sail,
    #'hike': travel_hitchhike,
    # 'work': work,
    'search': search,
    # 'hire': hire,
    'exit': exit
}
commands_without_parameter = ["status", "map", "search", "hire", "help", "exit"]


def user_input_processor(input_string, current_player):
    # Tämä funktio käsittelee käyttäjäsyötteen:
    # splittaa välilyönnistä listaksi
    try:
        if input_string == "":
            return True
        input_as_list = input_string.lower().strip().split()
        # etsii listan ensimmäistä alkiota vastaavaa arvoa command_dictionarysta
        try:
            selected_function = command_dictionary[input_as_list[0]]
        except KeyError:
            print("Command not found. Enter [help] for list of available commands.")
            return True
        # Jos käyttäjä ei antanut parametria:
        if len(input_as_list) < 2 and input_as_list[0] in commands_without_parameter:
            if selected_function is help_function or selected_function is exit:
                return selected_function()
            else:
                return selected_function(current_player)
        elif len(input_as_list) == 2:
            try:
                if selected_function is manual:
                    return selected_function(input_as_list[1])
                # kutsuu funktion käyttäen listan toista alkiota parametrina
                return selected_function(input_as_list[1], current_player)
            except TypeError or KeyError:  # TypeError laukeaa tässä yleensä, jos syöttää parametrin liikaa
                print("Oops, looks like you might have had a parameter where it doesnt belong.")
                return True
        else:
            print("Didn't pay any attention to tutorial did you? Use only one parameter for command of your choice.")
            return True
    except ValueError or IndexError or KeyError or TypeError:  # eipä ole ainakaan bare except :)
        print("I cant be bothered to explain exactly HOW things went wrong here. It might have been ValueError, might\n"
              "have been TypeError. Most likely it wasn't KeyError, but who knows? Only thing I know for sure is that\n"
              "you somehow managed to avoid ALL of my exception rules. Just type what you're asked, please...")
        return True
