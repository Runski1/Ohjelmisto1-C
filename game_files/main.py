from functions import *
# from user_input_processor import manual
# import os
from db_connection import connection
from user_input_processor import user_input_processor
import time

new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    cursor = connection.cursor()
    print(format_database_for_new_game())

    player1_name = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1_name}.")
    time.sleep(1)
    sql = "INSERT INTO player SET screen_name = '" + player1_name + "';"
    cursor.execute(sql)
    player2_name = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2_name + "';"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2_name}.")
    time.sleep(1)

while True:
    player_table = get_player_data_as_list()  # player_table on lista pelaajien riveistä, kts functions.py
    for player in player_table:  # iteroi joka pelaajan läpi vuorollaan
        round_number = get_round_number()  # haetaan round_counter-taulun arvo vuorossa olevan pelaajan
        # määrittämiseen
        # allaoleva toimii vain kahdella pelaajalla atm (modulo 2), mutta se on helposti muutettavissa useammalle
        # pelaajalle
        current_player = player_table[(round_number - 1) % 2]
        # Muuttujaan current player tallennetaan siis vuorossa olevan pelaajan tiedot listana: [id, screen_name etc.]
        print(f"{current_player[1]} it is your turn!\n")  # indeksi 1 viittaa screen_nameen
        time.sleep(1)
        printer(current_player[1], str(current_player[0]))  # Tämä on Miron printterikutsu
        time.sleep(1)
        user_input_string = input(f"{current_player[1]}: ")
        user_input_processor(user_input_string, current_player)
        print(round_number)  # tämä testaamista varten seuraa vuoronumeroa
        add_to_round_counter()
