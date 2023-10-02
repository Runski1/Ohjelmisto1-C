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
result = cursor.fetchall()
luggage_amount = result[0][0] - 1
end_game_email = f"Hey! This Jarmo from FunAir. We have found {luggage_amount}: luggage(s) that matches with your lost one! Here is the list of airports where you can find it/them."

for letter in end_game_email:
    sys.stdout.write(letter)
    sys.stdout.flush()  # Päivitä näyttö
    time.sleep(0.05)     # Odota 0.1 sekuntia ennen seuraavaa kirjainta

# Lopuksi, jätä kursori paikalleen
sys.stdout.write('\n')