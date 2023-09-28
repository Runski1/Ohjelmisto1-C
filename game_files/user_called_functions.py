def travel_fly(parameter):
    if parameter == "?":
        print("This should list all available cities where player can fly.")
    print("You begin your flight to " + parameter + ".")


def travel_sail(parameter):
    if parameter == "?":
        print("This should list all available cities where player can sail.")
    print('You start sailing to ' + parameter + '.')


def travel_hitchhike(parameter):
    if parameter == "?":
        print("This should list all available cities where player can hitchhike.")
    print('You start hitchhiking to ' + parameter + '.')


def work(parameter):
    if parameter == "?":
        print("This should list all available jobs.")
    print('You start working.')
    print(parameter)


def search():
    print("NOTE: Look up if player.location is also a bag_city")
    print("You search for grandma's suitcase, but it isn't here.")


def hire():
    print("NOTE: Look up if player.location is also a bag_city")
    print("You hire a local detective to look for your grandma's suitcase.")


def manual(parameter):
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