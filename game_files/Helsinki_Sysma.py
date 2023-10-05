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
def helsinki_sysma():
    print(f"{Fore.BLUE}You have arrived to Helsinki! Your grandma lives in Sysmä, so you have to order Dungo-driver to get there.")
    calling_text = [".", "..", "...", "...."]
    for _ in range(2):
        for text in calling_text:

            sys.stdout.write('\r'f"{Fore.RED}Calling"+ text)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
            sys.stdout.flush()
            time.sleep(0.5)
            input(f"{Fore.BLUE}You reached Dungo-driver! Roll dice while waiting him to arrive!{Fore.RED} Press enter!{Fore.BLUE}")
            num_roll = dice_roll()
            print(f"{Fore.GREEN}{num_roll}")
            input(f"{Fore.BLUE}You have to guide route for your loyal Dungo-driver. If you get same number you rolled before\n"
            f"you will get finally back to your lovely grandma and you get your name on testament! {Fore.RED}Press enter!")
            num_roll2 = dice_roll()
            print(f"{Fore.GREEN}{num_roll2}")
            lost_cities = ("Lohja","Korso","Kerava","Jyväskylä","Pieksämäki","Mellunmäki","Itäkeskus")


            time.sleep(1.0)
            if num_roll == num_roll2:
                print(f"{Fore.YELLOW}
                f"                                      /$$$$$$                                                     /$$               /$$             /$$     /$$\n"                 
                f"                                     /$$__  $$                                                   | $$              | $$            | $$    |__/\n"                
                f"                                    | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$\n"                 
                f"                                    | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$ /$$_____/\n"                
                f"                                    | $$|_  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$\n"                
                f"                                    | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$      /$$__  $$  | $$ /$$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$ \____  $$\n"                 
                f"                                    |  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/\n"                
                f"                                     \______/  \______/ |__/  |__/ \____  $$|__/      \_______/   \___/   \______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|_______/\n"                 
                f"                                                                   /$$  \ $$\n"                
                f"                                                                  |  $$$$$$/\n"                 
                f"                                                                   \______/\n"                
                f"                                     /$$ /$$ /$$ /$$     /$$                        /$$                                                                             /$$ /$$ /$$\n"                 
                f"                                    | $$| $$| $$|  $$   /$$/                       | $$                                                                            | $$| $$| $$\n"                
                f"                                    | $$| $$| $$ \  $$ /$$//$$$$$$  /$$   /$$      | $$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$        /$$  /$$  /$$  /$$$$$$  /$$$$$$$ | $$| $$| $$\n"                
                f"                                    | $$| $$| $$  \  $$$$//$$__  $$| $$  | $$      | $$__  $$ |____  $$|  $$  /$$//$$__  $$      | $$ | $$ | $$ /$$__  $$| $$__  $$| $$| $$| $$\n"                
                f"                                    |__/|__/|__/   \  $$/| $$  \ $$| $$  | $$      | $$  \ $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$ | $$ | $$| $$  \ $$| $$  \ $$|__/|__/|__/\n"                 
                f"                                                    | $$ | $$  | $$| $$  | $$      | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      | $$ | $$ | $$| $$  | $$| $$  | $$\n"                 
                f"                                     /$$ /$$ /$$    | $$ |  $$$$$$/|  $$$$$$/      | $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$      |  $$$$$/$$$$/|  $$$$$$/| $$  | $$ /$$ /$$ /$$\n"                
                f"                                    |__/|__/|__/    |__/  \______/  \______/       |__/  |__/ \_______/    \_/    \_______/       \_____/\___/  \______/ |__/  |__/|__/|__/|__/\n"
                f"                                                                                                                                                                                                  \n\n\n\n"
                                                                                                                                                                                                                  
                                                                                                                                                                                                                                 
                f" /$$$$$$$$ /$$                       /$$           /$$                           /$$   /$$                                                   /$$\n"                
                f"|__  $$__/| $$                      |__/          | $$                          |__/  | $$                                                  |__/                                                 \n"                 
                f"   | $$   | $$$$$$$   /$$$$$$        /$$ /$$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$        /$$  /$$$$$$$       /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$\n"
                f"   | $$   | $$__  $$ /$$__  $$      | $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$|_  $$_/   |____  $$| $$__  $$ /$$_____/ /$$__  $$      | $$ /$$_____/      | $$  | $$ /$$__  $$| $$  | $$ /$$__  $$ /$$_____/\n"
                f"   | $$   | $$  \ $$| $$$$$$$$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/| $$  | $$      /$$$$$$$| $$  \ $$| $$      | $$$$$$$$      | $$|  $$$$$$       | $$  | $$| $$  \ $$| $$  | $$| $$  \__/|  $$$$$$\n" 
                f"   | $$   | $$  | $$| $$_____/      | $$| $$  | $$| $$  | $$| $$_____/| $$      | $$  | $$ /$$ /$$__  $$| $$  | $$| $$      | $$_____/      | $$ \____  $$      | $$  | $$| $$  | $$| $$  | $$| $$       \____  $$\n"
                f"   | $$   | $$  | $$|  $$$$$$$      | $$| $$  | $$| $$  | $$|  $$$$$$$| $$      | $$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$      | $$ /$$$$$$$/      |  $$$$$$$|  $$$$$$/|  $$$$$$/| $$       /$$$$$$$/\n"
                f"   |__/   |__/  |__/ \_______/      |__/|__/  |__/|__/  |__/ \_______/|__/      |__/   \___/   \_______/|__/  |__/ \_______/ \_______/      |__/|_______/        \____  $$ \______/  \______/ |__/      |_______/\n" 
                f"                                                                                                                                                                 /$$  | $$\n"                                        
                f"                                                                                                                                                                |  $$$$$$/\n"                                        
                f"                                                                                                                                                                \______/\n")












            else:
                print(f"{Fore.BLUE}Your not so loyal Dungo-driver got lost despite of your guiding:´(\n"
                      f"You have arrived to {Fore.YELLOW}{random.choice(lost_cities)}\n\n"
                    f"{Fore.RED}You get angry and your driver gets you back to Helsinki!!!")









