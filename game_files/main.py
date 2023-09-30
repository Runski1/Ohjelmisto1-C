import functions
from user_input_processor import manual
import os
import mysql.connector
import time

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    #database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)
new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    cursor = connection.cursor()
    print(functions.format_database_for_new_game(connection))
    sql = "INSERT INTO round_counter (counter) VALUES ('1');"
    cursor.execute(sql)

    player1_name = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1_name}.")
    time.sleep(1)
    sql = "INSERT INTO player SET screen_name = '" + player1_name + "';"
    cursor.execute(sql)
    player2_name = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2_name + "';"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2_name}")
    time.sleep(1)

    while True:
        sql = "SELECT * FROM player;"
        cursor.execute(sql)
        result = cursor.fetchall()
        player1 = list(result[0])
        player2 = list(result[1])
        for i in player1, player2:
            sql = "SELECT counter FROM round_counter;"
            cursor.execute(sql)
            result = cursor.fetchone()
            rounter = result[0]

            if rounter % 2 == 1:
                sql = "SELECT id FROM player"
                sql += " WHERE screen_name = '"+player1_name+"';"
                cursor.execute(sql)
                result = cursor.fetchall()
                player1_id = int(result[0][0])
                choice = input(f"{player1_name} it is your turn!")
                time.sleep(1)
                functions.printer(player1_name, player1_id, connection)
                choice_p1 = input(f"What would you like to do? ")
                sql = "UPDATE round_counter SET counter = counter + 1"
                cursor.execute(sql)

            elif rounter % 2 == 0:

                print(f"{player2_name} it is your turn!")
                time.sleep(1)
                functions.printer(player2_name, connection)
                choice_p2 = input("What would you like to do? ")
                sql = "UPDATE round_counter SET counter = counter + 1"
                cursor.execute(sql)




else:
    # TÄMÄ VAIN YHTEYSTESTI

    cursor = connection.cursor()
    cursor.execute("USE kadonnut_testamentti;")
    cursor.execute("SELECT * FROM city;")
    print(cursor.fetchall())
