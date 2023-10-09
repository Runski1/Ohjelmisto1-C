from colorama import Fore
from user_input_processor import manual, help_function
from config import config
flyprice = config.get("config", "FlyPriceMultiplier")
sailprice = config.get("config", "BoatPriceMultiplier")
flydistance = config.get("config", "MaxDistanceFly")
saildistance = config.get("config", "MaxDistanceBoat")
hikedistance = config.get("config", "MaxDistanceHike")
hiringPrice = config.get("config", "HiringPrice")


def tutorial_user_prompt():
    return input("What would you like to do: ").strip().lower()


def tutorial():
    text1 = f"""You control this game by typing commands and executing them by pressing ENTER. You can add parameters
for certain commands by seperating the command and the parameter with a space.
            
Try out a command now! Type {Fore.RED}man fly{Fore.RESET}"""

    print(text1)
    while True:
        if tutorial_user_prompt() == "man fly":
            manual("fly")
            break
        else:
            print("Oops. Looks like you made a typo. Try avoiding those, I'm quite a sensitive program.")

    text2 = f"""{Fore.GREEN}What you saw there was a manual entry of the command {Fore.RED}fly{Fore.GREEN}. There is a 
manual entry for every command you can use. Any time you wish, type {Fore.RED}man 'command_name'{Fore.GREEN}. To see all 
commands you can use, try out the {Fore.RED}help{Fore.GREEN} command!{Fore.RESET}"""
    print(text2)
    while True:
        if tutorial_user_prompt() == "help":
            help_function()
            break
        else:
            print(f"""{Fore.MAGENTA}Oops, you did it again
You played with my heart, got lost in the game
Oh, baby, baby
Oops, I think you're in love
That you're sent from above
You're not that innocent
Just.Stop.Please.{Fore.RESET}""")

    text3 = f"""{Fore.GREEN}Great! I think you got the hang of it. Let's move on to core mechanics. In case you missed
it, the goal in this game is to find your grandma's lost luggage, which she lost in some airport in the NEU.
You have to travel across different countries by hitchiking, sailing or flying. You can do that by using commands
{Fore.RED}hike, sail, fly{Fore.GREEN} respectively. Just add the name of the city you wish to travel to as parameter,
for example {Fore.RED}sail tallinn{Fore.GREEN}. To list all available cities you can travel to, use parameter {Fore.RED}?
{Fore.GREEN}For example, {Fore.RED}sail ?{Fore.GREEN} shows you a list of all cities you can sail to. If there is no port
in your location, that one will also tell you where is the nearest port.{Fore.RESET}"""

    text4 = f"""{Fore.GREEN}You can fly to every city you can afford to, there is no distance limit. Flying is very expensive though, so be careful!
You shouldn't spend all your money trying to find grandma's luggage, since you still have to return it back to her.
Sailing has a distance limit of {saildistance} km and hitchhiking {hikedistance} km.{Fore.RESET}"""

    text5 = f"""{Fore.GREEN}Flying costs {Fore.YELLOW}{flyprice} EP/km{Fore.GREEN} per kilometer, while sailing only {Fore.YELLOW}{sailprice} EP/km.
{Fore.GREEN}Hitchhiking is free *duh*, but it is the slowest form of travel, unless RNG-gods are with you. Sailing takes
some time, but unlike hitchhiking, its not random. Flying is instant!{Fore.RESET}"""

    text6 = f"""{Fore.GREEN}Once you get to new city, you should {Fore.RED} search{Fore.GREEN} for your grandma's luggage. Location of the luggage is
random, and there are a total of 48 cities in Lost Testament, so it might take a while. You'll use up your turn while
searching, but you can {Fore.RED}hire{Fore.GREEN} a detective to search for you. That'll cost you {hiringPrice} EP.
When you {Fore.RED}hire{Fore.GREEN} a detective you get to use your turn for travelling.

Remember:
{Fore.RED}help{Fore.GREEN} to show all commands
{Fore.RED}man command{Fore.GREEN}for manual entry of {Fore.RED}command{Fore.GREEN}
{Fore.RED}fly ?{Fore.GREEN}parameter "?" will show you a list of cities where you can travel to.
{Fore.RED}search{Fore.GREEN} to search for luggage. DONT FORGET TO SEARCH! It can be real pain in the ass to find the
luggage, if you visit a city but don't {Fore.RED}search{Fore.GREEN} there.


It's not dangerous to go alone in Lost Testament, so I will not give you anything.
Good luck!{Fore.RESET}
"""
    print(text3)
    input("<Press ENTER to continue>")
    print(text4)
    input("<Press ENTER to continue>")
    print(text5)
    input("<Press ENTER to continue>")
    print(text6)
    input("<Press ENTER to continue>")
if __name__ == "__main__":
    tutorial()

