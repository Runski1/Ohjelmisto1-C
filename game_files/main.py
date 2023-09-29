import mysql.connector
import functions
import user_input_processor
import game_formatting



connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)
new_game_selection = input("Start new game (Y/N)").lower()
cursor = connection.cursor()
if new_game_selection == "y":
    print(functions.format_database_for_new_game(connection))
    cursor = connection.cursor()
    player1 = input("Nickname player 1: ")
    print(f"Player 1 is now known as {player1}.")
    sql = "INSERT INTO player SET screen_name = '" + player1 + "';"
    cursor.execute(sql)
    player2 = input("Nickname player 2: ")
    sql = "INSERT INTO player SET screen_name = '" + player2 + "';"
    print(f"Player 2 is now known as {player2}")
    cursor.execute(sql)


