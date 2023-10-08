from colorama import Fore, Back, Style

from config import config





def tutorial():

    tutorial_text=print(
    f"{Fore.GREEN}Welcome to the tutorial of this game!\n"
    f"{Fore.GREEN}If you want more info about user commands type: {Fore.RED}          help\n"
    f"{Fore.GREEN}Fly to another city type:                       {Fore.RED}          fly\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','FlyPriceMultiplier') +" EP/km\n"
    f"{Fore.GREEN}Sail to another city type:                      {Fore.RED}          sail\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','BoatPriceMultiplier') + " EP/km\n"
    f"{Fore.GREEN}Hike to another city type:                      {Fore.RED}          hike\n"
    f"{Fore.GREEN}Money Charge: {Fore.BLUE}0 EP/km \n"
    f"{Fore.GREEN}Hire private detective to search luggage on airport type: {Fore.RED}hire\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','HiringPrice') +" EP\n"
    "\n"
    f"{Fore.GREEN}If you want to search luggage in current location type: {Fore.RED}  search\n"
    f"{Fore.GREEN}If you got better things to do type:            {Fore.RED}          exit\n"
    f"{Fore.GREEN}Add '{Fore.RED}?{Fore.GREEN}' after '{Fore.RED}fly{Fore.GREEN}' and '{Fore.RED}sail{Fore.GREEN}' "
    f"command and you will get list of available cities."+ Fore.RESET)
    return tutorial_text


def intro():
    import sys
    import time
    speed = 0.01# kirjoitusnopeus

    intro_email = ("\n"+Fore.BLUE+"It's the year 2043. Climate change and a three-decade-long inflation-deflation cycle have\n"
                   "scourged Europe. At the beginning of Paavo Väyrynen's third presidential term, the European\n"
                    "Union took action. The use of the Euro as a currency was abandoned, and all trade began to\n"
                    "be conducted with emission permits (EP). When Turkey and the North African countries adopted\n"
                    "the EU's economic and environmental reforms, they obtained full EU membership. For the first\n"
                    "time in history, the EU has expanded beyond the borders of Europe, thus becoming the New\n"
                    "European Union (NEU).\n\n\n")

    for letter in intro_email:
        sys.stdout.write(letter)
        sys.stdout.flush()  # Päivitä näyttö
        time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
    sys.stdout.write('\n')

    input(Fore.RED+"Press Enter to continue!")




    for _ in range(3):
        text = Fore.RESET+"One new email!"
        sys.stdout.write('\r' + text)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('One new email!\n')
    input(Fore.RED + "Press Enter to open email!")

    print(Fore.RESET+"From:  grandma <granny.betty@hotmale.com>\n" 
    "To     undisclosed recipients\n"
    "Subject\n\n")
    print("I'm finally back home from my adventure across NEU! It was quite a journey, and I'm grateful for\n"
    "the memories I've collected. Can't wait to catch up with you and share all the details.  It's nice to be\n"
    "back and sleep in my own bed and finally eat normal food. You know me, all those spices give me a headache\n"
    "and make my stomach upset.\n"
    "Oh, almost forgot! I cannot find my luggage anywhere! Im sure I had  it when I got to the airport in Prague.\n" 
    "Or was it Berlin? Or Casablanca? Anyway, it’s nothing too important, but my testament is there too.\n"
    "You know I like to keep it on me at all times, just in case.\n"
    "Love,\n"
    "Grandma\n")


    input(Fore.RED+"Press Enter to start the game!"+Fore.RESET)

    for _ in range(3):
        text = "Loading... "
        sys.stdout.write('\r' + text)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
        sys.stdout.flush()
        time.sleep(0.5)

    print("Loading complete!")
    intro_text = (Fore.GREEN +

    "          ▄▄▄▄▀ ▄  █ ▄███▄       █    ████▄    ▄▄▄▄▄      ▄▄▄▄▀        ▄▄▄▄▀ ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ██   █▀▄▀█ ▄███▄      ▄     ▄▄▄▄▀\n"
    "       ▀▀▀ █   █   █ █▀   ▀      █    █   █   █     ▀▄ ▀▀▀ █        ▀▀▀ █    █▀   ▀   █     ▀▄ ▀▀▀ █    █ █  █ █ █ █▀   ▀      █ ▀▀▀ █\n"
    "           █   ██▀▀█ ██▄▄        █    █   █ ▄  ▀▀▀▀▄       █            █    ██▄▄   ▄  ▀▀▀▀▄       █    █▄▄█ █ ▄ █ ██▄▄    ██   █    █\n"
    "          █    █   █ █▄   ▄▀     ███▄ ▀████  ▀▄▄▄▄▀       █            █     █▄   ▄▀ ▀▄▄▄▄▀       █     █  █ █   █ █▄   ▄▀ █ █  █   █\n"
    "         ▀        █  ▀███▀           ▀                   ▀            ▀      ▀███▀               ▀         █    █  ▀███▀   █  █ █  ▀\n"
    "                 ▀                                                                                        █    ▀           █   ██\n"
    "                                                                                                         ▀\n")


    # min_speed = 0.04  # Alin  kirjoitus nopeus
    # max_speed = 0.1   # Ylin kirjoitus nopeus
    for letter in intro_text:
        sys.stdout.write(letter)
        sys.stdout.flush()  # Päivitä näyttö
        time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
    sys.stdout.write('\n')


    intro_text2 = print(Fore.BLUE+
            "                   ______________________________________________________________________________"
            "___________________________\n"
            "                   |************************************"+Fore.GREEN+"Find grandma´s lost luggage"
                        +Fore.BLUE+"*****************************************|\n"
            "                   |**********"+Fore.GREEN+"This is a text based adventure game where you can make"
                                                        " your actions by typing them."+Fore.BLUE+"***********|\n"
            "                   |******************************************************************************"
                                                                                                  "************"
                                                                                                  "**************|\n"
            "                   |****************************************"+Fore.GREEN+"More info in tutorial!"
                        +Fore.BLUE+"******************************************|\n"
            "                   |____________________________________________________________________________"
                                   "____________________________|\n")
    return intro_text, intro_text2





if __name__ == "__main__":
    tutorial()
    intro()






