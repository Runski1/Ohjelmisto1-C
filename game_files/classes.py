from db_connection import connection
import functions


class Game:
    visited = []
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
        bag_city = functions.generate_main_bag()

        query = (f"INSERT INTO game (name, round_counter, bag_city, visited)"
                 f" VALUES('{self.game_name}', '{self.round_counter}', '{bag_city}', '{Game.visited}')")
        self.cursor.execute(query)

    def babymaker(self):
        player1 = Player(self.player1_name)
        player2 = Player(self.player2_name)
        self.players.append(player1)
        self.players.append(player2)


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
