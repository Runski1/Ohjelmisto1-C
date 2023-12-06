from functions import *
from user_input_processor import user_input_processor
from db_connection import connection
from end_game_event import helsinki_sysma
from intro import *
from tutorial import tutorial
import classes

#format_database_for_new_game()



while True:
    player_table = classes.g1.players
    for player in player_table:
        round_number = get_round_number()
        turn = True
        turn_skipper = False
        current_player = classes.g1.players[(round_number-1) % 2]
        is_lock = current_player.lock_state
        if current_player.prizeholder == 1 and current_player.location == 16 and is_lock == 0:
            helsinki_sysma(current_player.player_name)
            turn_skipper = True
        if not turn_skipper:
            print(f"\n{current_player.player_name} it is your turn!\n")
            if is_lock == 0:
                printer(current_player)
                while turn:
                    choice = input("\nWhat would you like to do: ")
                    turn = user_input_processor(choice, current_player)
                add_to_round_counter()
                classes.g1.add_to_db()
                current_player.update_db()
            if is_lock != 0:
                printer(current_player)
                print("\nYou are locked this round.")
                exit_backdoor = input("<Press ENTER to continue>")  # tätä exitiä
                if exit_backdoor == "exit":  # ei mainita missään, asensin tämän lähinnä devaukseen.
                    exit()
                lock_reduce(current_player)
                add_to_round_counter()
                classes.g1.add_to_db()
                current_player.update_db()
        if turn_skipper:
            add_to_round_counter()
            classes.g1.add_to_db()
            current_player.update_db()
