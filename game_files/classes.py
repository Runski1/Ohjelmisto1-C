import mysql.connector
from db_connection import connection
import functions

class Game:
    players = []
    cursor = connection.cursor()

    def __init__(self, game_name, player1, player2, round_number=0):
        self.game_name = game_name
        self.player1_name = player1
        self.player2_name = player2
        self.round_counter = round_number
        self.babymaker()
        self.add_to_db()


    def add_to_db(self):
        functions.generate_main_bag()

        query = (f"INSERT INTO Game(game_name, round_counter, bag_city, searched)"
                 f" VALUES('{self.game_name}', '{self.round_counter}', '{bag_city}', '{searched}')")
        self.cursor.execute(query)



    def babymaker(self):
        self.players.append(Player(self.player1_name))
        self.players.append(Player(self.player2_name))


class Player:

    def __init__(self, player_name, money=2000, location=16, bag=0, lock_state=0):
        self.player_name = player_name
        self.money = money
        self.location = location
        self.bag = bag
        self.lock_state = lock_state
        query = f"INSERT INTO"



