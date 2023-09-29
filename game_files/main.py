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
    cursor = connection.cursor()
    print(functions.format_database_for_new_game(connection))
    player1 = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1}.")
    sql = "INSERT INTO player SET screen_name = '" + player1 + "';"
    cursor.execute(sql)
    player2 = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2 + "';"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2}")
    run = True

    while run:


else:
    # TÄMÄ VAIN YHTEYSTESTI
    cursor = connection.cursor()
    cursor.execute("USE kadonnut_testamentti;")
    cursor.execute("SELECT * FROM city;")
    print(cursor.fetchall())
