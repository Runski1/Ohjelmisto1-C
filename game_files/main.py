import functions
# from user_input_processor import manual
# import os
from db_connection import connection
import time

new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    cursor = connection.cursor()
    print(functions.format_database_for_new_game())
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
        for i in result:
            sql = "SELECT counter FROM round_counter;"
            cursor.execute(sql)
            result = cursor.fetchone()
            rounter = result[0]

            if rounter % 2 == 1:
                print(f"{player1[1]} it is your turn!\n")
                time.sleep(1)
                functions.printer(player1[1], str(player1[0]))
                time.sleep(1)
                choice_p1 = input(f"What would you like to do? ")
                sql = "UPDATE round_counter SET counter = counter + 1"
                cursor.execute(sql)

            elif rounter % 2 == 0:

                print(f"{player2_name} it is your turn!")
                time.sleep(1)
                functions.printer(player2_name, connection)
                choice_p2 = input("\nWhat would you like to do? ")
                sql = "UPDATE round_counter SET counter = counter + 1"
                cursor.execute(sql)
