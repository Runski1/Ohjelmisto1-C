import random
import sys
import time
from db_connection import connection
cursor = connection.cursor()


def end_game_email():
    sql = "SELECT name FROM city WHERE bag_city = '1'"
    cursor.execute(sql)
    result = cursor.fetchall()
    luggage_amount = len(result)
    email_string = (f"Hey! This Jarmo from FunAir. We have found {luggage_amount} luggage(s) that matches with your "
                    f"lost one! Here is the list of airports where you can find it/them.")
    speed = 0.09  # kirjoitusnopeus
    min_speed = 0.1  # Alin  kirjoitus nopeus
    max_speed = 0.04   # Ylin kirjoitus nopeus
    for letter in email_string:
        sys.stdout.write(letter)
        sys.stdout.flush()  # Päivitä näyttö
        time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
    # Muuta nopeutta satunnaisesti
        speed += random.uniform(-0.03, 0.03)  # Lisää tai vähennä nopeutta pienellä satunnaisella määrällä
        speed = max(min_speed, min(speed, max_speed))  # rajoittaa nopeutta ettei ohjelma kaadu;DD
    # Lopuksi, jätä kursori paikalleen
    sys.stdout.write('\n')
    for city in result:
        print(city[0])


if __name__ == '__main__':
    end_game_email()
