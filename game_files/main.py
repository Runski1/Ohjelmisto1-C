from functions import *
from user_input_processor import user_input_processor
from db_connection import connection
from Helsinki_Sysma import helsinki_sysma

new_game_selection = input("Start new game (Y/N)").lower()
if new_game_selection == "y":
    cursor = connection.cursor()
    print(format_database_for_new_game())
    player1_name = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1_name}.")
    sql = "INSERT INTO player SET screen_name = '" + player1_name + "'"
    cursor.execute(sql)
    player2_name = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2_name + "'"
    cursor.execute(sql)
    print(f"Player 2 is now known as {player2_name}")
    generate_main_bag()

while True:
    player_table = get_player_data_as_list()
    for player in player_table:
        turn = True
        round_number = get_round_number()
        current_player = player_table[(round_number-1) % 2]
        if current_player[4] == 1 and current_player[8] == 16:
            helsinki_sysma(current_player[1])
        is_lock = lock_check(str(current_player[0]))
        print(f"\n{current_player[1]} it is your turn!\n")
        if is_lock == "Not locked":
            printer(current_player)
            while turn:  # HUOM!!!! TÄMÄ LOOP EI TULOSTA PELAAJAN TILAA UUDESTAAN, PITÄISIKÖ ANTAA PELAAJAN KUTSUA
                choice = input("\nWhat would you like to do: ")
                turn = user_input_processor(choice, current_player)
            add_to_round_counter()

        elif is_lock > 0:
            printer(current_player)
            exit_backdoor = input("\nYou are locked this round. (Press enter to continue: ")  # tätä exit-vaihtoehtoa
            if exit_backdoor == "exit":  # ei kerrota missään, asensin tämän lähinnä devaukseen.
                exit()
            lock_reduce(current_player)
            add_to_round_counter()
            continue
