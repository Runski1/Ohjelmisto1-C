from functions import *
# from user_input_processor import manual
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
    sql = "INSERT INTO player SET screen_name = '" + player1_name + "'"
    cursor.execute(sql)
    player2_name = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2_name + "'"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2_name}.")
    time.sleep(1)

    while True:
        player_table = get_player_data_as_list()
        for player in player_table:  # iteroi joka pelaajan läpi vuorollaan
            round_number = get_round_number()
            current_player = player_table[round_number-1 % 2] #lisäsin -1 että saadaan peli aloittamaan pelaaja1:stä
        # Muuttujaan current player tallennetaan siis vuorossa olevan pelaajan tiedot listana: [id, screen_name etc.]
            print(f"{current_player[1]} it is your turn!\n")
            time.sleep(1)
            printer(current_player[1], str(current_player[0]))  # Tämä on Miron printterikutsu
            time.sleep(1)
            choice_p1 = manual()  # choice_p1 tulee kutsumaan user_input_processorin, mutta atm
            if choice_p1 == "exit":  # lisäsin siihen vain while loopin breakkausta varten exitin
                exit()
            print(round_number)  # tämä testaamista varten seuraa vuoronumeroa
            add_to_round_counter()
