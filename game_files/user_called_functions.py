
def travel_fly(parameter):
    # Lentokohteen valinta ja kohteiden listaus
    if parameter == "?":
        # Kutsu mahdollisten lentokohteiden lista tässä
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
        'fly': "[fly] lets you choose flight destination. To show all available\n"
                "destinations, use [fly ?]. Start flying to city of your choosing\n"
                "use [fly city], where city is the name of your chosen city.",
        'sail': "[sail] lets you choose flight destination. To show all available\n"
                "destinations, use [sail ?]. Start sailing to city of your choosing\n"
                "use [sail city], where city is the name of your chosen city.",
        'hike': "This is a placeholder for hike manual entry.",
        'work': "This is a placeholder for work manual entry.",
        'search': "This is a placeholder for search manual entry",
        'exit': "[exit] Stop the game running and hopefully save your progress.",
        'man': "You dirty bastard, trying to break me are you?"
        }
    print(manual_dictionary[parameter])


def help_function():
    # nykyisellään oleva manual.dictionaryn arvot voisi tulostua avainten kanssa
    print("You can use these commands:")
    for key in command_dictionary.keys():
        print(key)
    print("For more information about a command, write 'man command'")


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