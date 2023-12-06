import functions
from db_connection import connection


class Game:
    visited = []
    players = []
    cursor = connection.cursor()

    def __init__(self, game_name, player1_name, player2_name, round_number=0, bag_city=0, player1="", player2=""):
        self.game_name = game_name
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.round_counter = round_number
        self.bag_city = bag_city
        self.babymaker()
        self.add_to_db()
        self.player1 = player1
        self.player2 = player2

    def add_to_db(self):
        self.bag_city = functions.generate_main_bag()
        query = (f"INSERT INTO game (name, round_counter, bag_city, visited)"
                 f" VALUES('{self.game_name}', '{self.round_counter}', '{self.bag_city}', '{Game.visited}')")
        self.cursor.execute(query)

    def babymaker(self):
        self.player1 = Player(self.player1_name)
        self.players.append(self.player1)
        self.player2 = Player(self.player2_name)
        self.players.append(self.player2)


class Player:

    def __init__(self, player_name, money=2000, location=16, bag=0, lock_state=0, prizeholder=0, total_dice=0):
        self.id = id
        self.player_name = player_name
        self.money = money
        self.location = location
        self.bag = bag
        self.lock_state = lock_state
        self.prizeholder = prizeholder
        self.total_dice = total_dice

        query = (f"INSERT INTO player (screen_name, current_pp, lockstate, prizeholder,"
                 f" total_dice, location) VALUES ('{self.player_name}', '{self.money}', '{self.lock_state}',"
                 f" '{self.prizeholder}', '{self.total_dice}', '{self.location}')")

        Game.cursor.execute(query)

    def update_db(self):
        query = f"SELECT id FROM player"
        Game.cursor.execute(query)
        result = Game.cursor.fetchall()
        self.id = result[0]

        sql = f"UPDATE player SET current_pp = '{self.money}' WHERE id = '{self.id}'"
        Game.cursor.execute(sql)
        sql = f"UPDATE player SET lockstate = '{self.lock_state}' WHERE id = '{self.id}'"
        Game.cursor.execute(sql)
        sql = f"UPDATE player SET prizeholder = '{self.prizeholder}' WHERE id = '{self.id}'"
        Game.cursor.execute(sql)
        sql = f"UPDATE player SET total_dice = '{self.total_dice}' WHERE id = '{self.id}'"
        Game.cursor.execute(sql)
        sql = f"UPDATE player SET location = '{self.location}' WHERE id = '{self.id}'"
        Game.cursor.execute(sql)


g1 = Game("hoi", "tatti", "taavi")
