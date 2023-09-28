import functions
import user_input_processor
import os
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         # database='kadonnut_testamentti',
         user='game',
         password='pass',
         autocommit=True
         )
new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    print(functions.format_database_for_new_game(connection))
else:
    # TÄMÄ VAIN YHTEYSTESTI
    cursor = connection.cursor()
    cursor.execute("USE kadonnut_testamentti;")
    cursor.execute("SELECT * FROM city;")
    print(cursor.fetchall())
