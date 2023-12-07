import random
import db_connection
import json


class Game:
    players = []
    cursor = db_connection.connection.cursor()

    def __init__(self, game_name, player1_name, player2_name, round_number=0, bag_city=0):
        self.game_name = game_name
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.round_counter = round_number
        self.bag_city = bag_city
        self.update_db()
        self.game_id = self.get_game_id(self.game_name)
        self.player1 = self.babymaker(self.player1_name, self.game_id)
        self.player2 = self.babymaker(self.player2_name, self.game_id)
        self.visited = []
        self.players = []
        self.update_db()

    def get_game_id(self, game_name):
        sql = f"SELECT id FROM game WHERE name = '{game_name}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result[0]

    def update_db(self):
        self.bag_city = self.generate_bag()
        visited_json = json.dumps(self.visited)
        query = (f"INSERT INTO game (name, round_counter, bag_city, visited)"
                 f" VALUES('{self.game_name}', '{self.round_counter}', '{self.bag_city}', '{visited_json}')")
        self.cursor.execute(query)

        for player in self.players:
            player.update_db()

    def babymaker(self, player, game_id):
        baby = Player(player, game_id)
        self.players.append(baby)
        return baby

    def generate_bag(self):
        city_id = []
        sql = f"SELECT id FROM city"
        Game.cursor.execute(sql)
        result = Game.cursor.fetchall()
        for city in result:
            city_id.append(city[0])
        return random.choice(city_id)

    def json_response(self):
        game_status = {
            "game": {
                "game_name": self.game_name,
                "round_counter": self.round_counter,
                "bag_city": self.bag_city,
                "visited": self.visited
            },
            "players": {
                "player1": self.player1,
                "player2": self.player2
            }
        }
        game_json = json.dumps(game_status)
        return game_json

    def load_game(self, game_data, player1, player2):
        game = Game(self.game_name, player1[1], player2[1])
        game.game_id = game_data[0][0]
        game.game_name = game_data[0][1]
        game.round_counter = game_data[0][2]
        game.bag_city = game_data[0][3]
        game.visited = json.loads(game_data[0][4])

        game.player1 = Player(player1[2], player1[7])
        game.player2 = Player(player2[2], player1[7])

        game.player1.set_player_data(player1)
        game.player2.set_player_data(player2)
        return game


class Player:

    def __init__(self, player_name, game_id, money=2000, location=16, bag=0, lock_state=0, prizeholder=0, total_dice=0):
        self.player_name = player_name
        self.game_id = game_id
        self.money = money
        self.location = location
        self.bag = bag
        self.lock_state = lock_state
        self.prizeholder = prizeholder
        self.total_dice = total_dice

        query = (f"INSERT INTO player (screen_name, current_pp, lockstate, prizeholder,"
                 f" total_dice, location, game) VALUES ('{self.player_name}', '{self.money}', '{self.lock_state}',"
                 f" '{self.prizeholder}', '{self.total_dice}', '{self.location}'), '{self.game_id}'")

        Game.cursor.execute(query)
        query = f"SELECT id FROM player WHERE screen_name = '{self.player_name}'"
        Game.cursor.execute(query)
        result = Game.cursor.fetchall()
        self.id = result[0]

    def update_db(self):
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

    def set_player_data(self, data):
        self.id = data[0]
        self.player_name = data[1]
        self.money = data[2]
        self.lock_state = data[3]
        self.prizeholder = data[4]
        self.total_dice = [5]
        self.location = data[6]
        self.game_id = data[7]
        Game.players.append(self)
