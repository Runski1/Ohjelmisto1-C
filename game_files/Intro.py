from colorama import Fore, Back, Style

from config import config

def tutorial():

    tutorial_text=print(
    f"{Fore.GREEN}Welcome to the tutorial of this game!\n"
    f"{Fore.GREEN}If you want more info about user commands type: {Fore.RED}          help\n"
    f"{Fore.GREEN}Fly to another city type:                       {Fore.RED}          fly\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','FlyPriceMultiplier') +"PP/km\n"
    f"{Fore.GREEN}Sail to another city type:                      {Fore.RED}          sail\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','BoatPriceMultiplier') + "PP/km\n"
    f"{Fore.GREEN}Hike to another city type:                      {Fore.RED}          hike\n"
    f"{Fore.GREEN}Money Charge: {Fore.BLUE}0 PP/km \n"
    f"{Fore.GREEN}Hire private detective to search luggage on airport type: {Fore.RED}hire\n"
    f"{Fore.GREEN}Money charge: {Fore.BLUE}"+ config.get('config','HiringPrice') +" PP\n"
    "\n"
    f"{Fore.GREEN}If you want to search luggage in current location type: {Fore.RED}  search\n"
    f"{Fore.GREEN}If you got better things to do type:            {Fore.RED}          exit\n")
    return tutorial_text




def intro():
    import sys
    import time

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

    speed = 0.0000001  # kirjoitusnopeus
    # min_speed = 0.04  # Alin  kirjoitus nopeus
    # max_speed = 0.1   # Ylin kirjoitus nopeus
    for letter in intro_text:
        sys.stdout.write(letter)
        sys.stdout.flush()  # Päivitä näyttö
        time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
        # Muuta nopeutta satunnaisesti
        # speed += random.uniform(-0.01, 0.01)  # Lisää tai vähennä nopeutta pienellä satunnaisella määrällä
        # speed = max(min_speed, min(speed, max_speed))  # rajoittaa nopeutta ettei ohjelma kaadu;DD
        # Lopuksi, jätä kursori paikalleen
    sys.stdout.write('\n')


    intro_text2 = print(Fore.BLUE+
            "                   _________________________________________________________________________________________________________\n"
            "                   |** Your grandma has returned from her trip to New-Europe and has noticed that she forgot her luggage  **|\n"
            "                   |*** at some airport, which she cannot remember. In her luggage, there is her precious testament that ***|\n"
            "                   |*** she's carrying with her just in case. Your goal is to track down grandma's lost luggage because  ***|\n"
            "                   |***** you may have the opportunity to get your name into the testament after returning it to her.  *****|\n"
            "                   |________________________________________________________________________________________________________|\n")

    return intro_text, intro_text2
intro()



user_input = input(f"{Fore.RED}Do you want to run tutorial for this game to get on track?(y/n)").lower()
if user_input == "y":
    tutorial()











