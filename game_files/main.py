from functions import *
from user_input_processor import *
# import os
from db_connection import connection
import time

new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    cursor = connection.cursor()
    print(format_database_for_new_game())

    player1_name = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1_name}.")
    time.sleep(0.3)
    sql = "INSERT INTO player SET screen_name = '" + player1_name + "';"
    cursor.execute(sql)
    player2_name = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2_name + "';"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2_name}")
    time.sleep(1)

    while True:
        player_table = get_player_data_as_list()
        for player in player_table:
            round_number = get_round_number()
            current_player = player_table[round_number - 1 % 2]
            is_lock = lock_check(str(current_player[0]))
            print(f"{current_player[1]} it is your turn!\n")
            time.sleep(1)

            if is_lock == "Not locked":
                printer(current_player[1], str(current_player[0]))  # printteri kutsu
                time.sleep(1)
                while True:
                    choice = input("\nWhat would you like to do: ")
                    user_input_processor(choice)
                    if choice == "fly" or choice == "help" or choice == "sail" or choice == "hike":
                    elif choice == "exit":
                        exit()
                    elix

                print(round_number)

                add_to_round_counter()

            elif is_lock > 0:
                printer(current_player[1], str(current_player[0]))
                lock_roll = dice_roll()
