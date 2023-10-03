
import threading
import sys
import time

def loading_text_animation(text, iterations, delay):
    for _ in range(iterations):
        sys.stdout.write('\r' + text)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
        sys.stdout.flush()
        time.sleep(delay)

loading_text = "Loading... "
iterations = 3  # Number of times to flicker
delay = 0.5  # Time in seconds for each flicker

loading_text_animation(loading_text, iterations, delay)
print("Loading complete!")
def intro():
    intro_text = (

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


    return intro_text


intro_text2 = (
                            "                   _________________________________________________________________________________________________________\n"
                            "                   |** Your grandma has returned from her trip to New-Europe and has noticed that she forgot her luggage  **|\n"
                            "                   |*** at some airport, which she cannot remember. In her luggage, there is her precious testament that ***|\n"
                            "                   |*** she's carrying with her just in case. Your goal is to track down grandma's lost luggage because  ***|\n"
                            "                   |***** you may have the opportunity to get your name into the testament after returning it to her.  *****|\n"
                            "                   |________________________________________________________________________________________________________|\n")



intro()
print(intro_text2)



#def tutorial():
    #print("This is text")



