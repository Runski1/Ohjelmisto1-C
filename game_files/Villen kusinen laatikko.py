import random
import sys
import time
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='game',
         password='pass',
         autocommit=True
         )




cursor = connection.cursor()
sql = "SELECT COUNT(id) FROM player;"
cursor.execute(sql)
result1 = cursor.fetchall()
luggage_amount = result1[0][0] - 1
end_game_email = f"Hey! This Jarmo from FunAir. We have found {luggage_amount}: luggage(s) that matches with your lost one! Here is the list of airports where you can find it/them."
speed = 0.08 #kirjoitus nopeus
min_speed = 0.04  # Alin  kirjoitus nopeus
max_speed = 0.1   # Ylin kirjoitus nopeus
for letter in end_game_email:
    sys.stdout.write(letter)
    sys.stdout.flush()  # Päivitä näyttö
    time.sleep(speed)     # Käytä muuttujan "nopeus" arvoa odotusaikana
# Muuta nopeutta satunnaisesti
    speed += random.uniform(-0.01, 0.01)  # Lisää tai vähennä nopeutta pienellä satunnaisella määrällä
    speed = max(min_speed, min(speed, max_speed))
# Lopuksi, jätä kursori paikalleen
sys.stdout.write('\n')

sql = "SELECT NAME FROM city where visited ='0';"
cursor.execute(sql)
result2 = cursor.fetchall()

# Sekoitetaan tulokset satunnaisessa järjestyksessä
random.shuffle(result2)

# Tulostetaan enintään result1 verran kaupunkien nimet
for i, row in enumerate(result2):
    if i >= luggage_amount:
        break
    print(row[0])











