import random
import sys
import time
from db_connection import connection


def end_game_email():
    cursor = connection.cursor()
    sql = "SELECT COUNT(id) FROM player;"
    cursor.execute(sql)
    result1 = cursor.fetchall()
    luggage_amount = result1[0][0] - 1
    email_string = (f"Hey! This Jarmo from FunAir. We have found {luggage_amount} luggage(s) that matches with your "
                    f"lost one! Here is the list of airports where you can find it/them.")
    speed = 0.09  # kirjoitusnopeus
    min_speed = 0.04  # Alin  kirjoitus nopeus
    max_speed = 0.1   # Ylin kirjoitus nopeus
    for letter in email_string:
        sys.stdout.write(letter)
        sys.stdout.flush()  # Päivitä näyttö
        time.sleep(speed)  # Käytä muuttujan "nopeus" arvoa odotusaikana
    # Muuta nopeutta satunnaisesti
        speed += random.uniform(-0.03, 0.03)  # Lisää tai vähennä nopeutta pienellä satunnaisella määrällä
        speed = max(min_speed, min(speed, max_speed))  # rajoittaa nopeutta ettei ohjelma kaadu;DD
    # Lopuksi, jätä kursori paikalleen
    sys.stdout.write('\n')

    sql = "SELECT NAME FROM city;"
    cursor.execute(sql)
    result2 = cursor.fetchall()

    # Sekoitetaan tulokset satunnaisessa järjestyksessä
    random.shuffle(result2)

    # Tulostetaan enintään result1 verran kaupunkien nimet
    for i, row in enumerate(result2):
        if i >= luggage_amount:
            break
        print(row[0])


end_game_email()
