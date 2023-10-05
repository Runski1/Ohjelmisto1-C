from db_connection import connection
from colorama import Fore, Back, Style
import random
from functions import dice_roll
#after_end_game
'''def ending_check(helsinki_sysmä,player)
    cursor = connection.cursor()
    #tarkistaa onko nykyisellä pelaajalla laukku
    sql = ("SELECT player.id FROM player INNER JOIN city ON player.location = city.id
           "WHERE city.name = 'Helsinki' and player.prizeholder= '1'")
    cursor.execute(sql)
    result = cursor.fetchall()

    if player in result: #Jos pelaajan id on listassa löytyneiden pelaajien id:en joukossa, joilla on pääpalkinto
        # niin loppu event käynnnistyy
        helsinki_sysmä()
    else:
        False'''


import sys
import time
def helsinki_sysma(player):
    print(f"{Fore.BLUE}{player} you have arrived in Helsinki! Your grandma lives in Sysmä, so you have to order a Dungo-driver to get there.")
    calling_text = [".", "..", "...", "...."]
    for _ in range(2):
        for text in calling_text:
            sys.stdout.write('\r'f"{Fore.RED}Calling"+ text)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
            sys.stdout.flush()
    time.sleep(0.5)
    input(f"{Fore.BLUE}You reached the Dungo-driver! Roll the dice while waiting for him to arrive!{Fore.RED} Press enter!")
    num_roll = dice_roll()
    print(f"{Fore.GREEN}{num_roll}")
    input(f"{Fore.BLUE}You have to guide the route for your loyal Dungo-driver. If you get the same number you rolled before,\n" 
    f"you will finally get back to your lovely grandma, and you'll get your name on the testament!{Fore.RED} Press enter!")
    num_roll2 = dice_roll()
    print(f"{Fore.GREEN}{num_roll2}")
    lost_cities = ("Lohja","Korso","Kerava","Jyväskylä","Pieksämäki","Mellunmäki","Itäkeskus")


    time.sleep(1.0)
    if num_roll == num_roll2:
        victory = (f"                                            {Fore.BLUE}!!!!!!!{Fore.LIGHTYELLOW_EX}****{Fore.RED}{player} OMG YOU MADE IT{Fore.LIGHTYELLOW_EX}**** {Fore.BLUE}!!!!!!!\n"
                   f"                                      {Fore.BLUE}!!!!!!!{Fore.LIGHTYELLOW_EX}****{Fore.RED}Your name i$ now on te$tament {Fore.LIGHTYELLOW_EX}**** {Fore.BLUE}!!!!!!!\n")

        victory2 =  ("\n\n\n\n\n\n\n\n\n"
                    "  /$$$$$$                                                     /$$               /$$             /$$     /$$\n"
                    " /$$__  $$                                                   | $$              | $$            | $$    |__/\n"                
                    "| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$\n"                 
                    "| $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$ /$$_____/\n"                
                    "| $$|_  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$\n"                
                    "| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$      /$$__  $$  | $$ /$$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$ \____  $$\n"                 
                    "|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/\n"                
                    "\______/  \______/ |__/  |__/ \____  $$|__/      \_______/   \___/   \______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|_______/\n"                 
                    "                              /$$  \ $$\n"                
                    "                              |  $$$$$$/\n"                 
                    "                               \______/\n"                
                        " /$$ /$$ /$$ /$$     /$$                        /$$                                                                             /$$ /$$ /$$\n"                 
                        "| $$| $$| $$|  $$   /$$/                       | $$                                                                            | $$| $$| $$\n"                
                        "| $$| $$| $$ \  $$ /$$//$$$$$$  /$$   /$$      | $$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$        /$$  /$$  /$$  /$$$$$$  /$$$$$$$ | $$| $$| $$\n"                
                        "| $$| $$| $$  \  $$$$//$$__  $$| $$  | $$      | $$__  $$ |____  $$|  $$  /$$//$$__  $$      | $$ | $$ | $$ /$$__  $$| $$__  $$| $$| $$| $$\n"                
                        "|__/|__/|__/   \  $$/| $$  \ $$| $$  | $$      | $$  \ $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$ | $$ | $$| $$  \ $$| $$  \ $$|__/|__/|__/\n"                 
                        "                | $$ | $$  | $$| $$  | $$      | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      | $$ | $$ | $$| $$  | $$| $$  | $$\n"                 
                        " /$$ /$$ /$$    | $$ |  $$$$$$/|  $$$$$$/      | $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$      |  $$$$$/$$$$/|  $$$$$$/| $$  | $$ /$$ /$$ /$$\n"                
                        "|__/|__/|__/    |__/  \______/  \______/       |__/  |__/ \_______/    \_/    \_______/       \_____/\___/  \______/ |__/  |__/|__/|__/|__/\n\n\n\n\n\n\n")

        for _ in range(5):  # Toista vilkutus 5 kertaa
            sys.stdout.write(Fore.LIGHTYELLOW_EX + victory2)  # Tulosta koko teksti
            sys.stdout.flush()
            time.sleep(0.5)  # Odota ennen seuraavaa vilkkumisen vaihetta
        time.sleep(1.0)
        print(victory)

    else:
        print(f"{Fore.BLUE}Your not so loyal Dungo-driver got lost despite of your guiding:´(\n"
        f"You have arrived to {Fore.YELLOW}{random.choice(lost_cities)}\n\n"
        f"{Fore.RED}You get angry and your driver gets you back to Helsinki!!!")

player = "Ville"

helsinki_sysma(player)





