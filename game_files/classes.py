import random
import db_connection
import json


class Game:
    cursor = db_connection.connection.cursor()
    instances = []

    def __init__(self, game_name, player1_name, player2_name, round_number=0, bag_city=0):
        self.visited = ["16"]
        self.players = []
        self.game_name = game_name
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.round_counter = round_number
        self.bag_city = bag_city
        self.generate_bag()
        self.update_db()
        self.game_id = self.get_game_id(self.game_name)
        self.babymaker(self.player1_name, self.game_id)
        self.babymaker(self.player2_name, self.game_id)
        self.update_db()
        Game.instances.append(self)
        print(Game.instances)
        self.last_turn_rand_item = [None, None, None]

    def get_game_id(self, game_name):  # Pelin id saaminen koska olio luodaan ennen tietokantaan tallennusta
        sql = f"SELECT id FROM game WHERE name = '{game_name}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result[0][0]

    def update_db(self):  # Datan tallennus tietokantaan
        sql = f"SELECT name FROM game WHERE name = '{self.game_name}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if self.cursor.rowcount > 0:
            visited_json = json.dumps(self.visited)
            query = (f"UPDATE game SET round_counter = '{self.round_counter}', visited = '{visited_json}'"
                     f" WHERE name = '{self.game_name}'")
            self.cursor.execute(query)
            self.update_players()
        else:
            visited_json = json.dumps(self.visited)
            query = (f"INSERT INTO game (name, round_counter, bag_city, visited)"
                     f" VALUES('{self.game_name}', '{self.round_counter}', '{self.bag_city}', '{visited_json}')")
            self.cursor.execute(query)
            self.update_players()

    def update_players(self):
        for player in self.players:
            player.update_db()

    def babymaker(self, player, game_id):
        baby = Player(player, game_id)
        self.players.append(baby)
        return self

    def generate_bag(self):
        citys = []
        sql = f"SELECT id FROM city"
        Game.cursor.execute(sql)
        result = Game.cursor.fetchall()
        for city in result:
            citys.append(city[0])
        self.bag_city = random.choice(citys)

    def json_response(self):
        game_status = {
            "game": {
                "game_name": self.game_name,
                "round_counter": self.round_counter,
                "bag_city": self.bag_city,
                "visited": self.visited,
            },
            "players": {
                "player1": {
                    "player_id": self.players[0].id,
                    "screen_name": self.players[0].player_name,
                    "current_pp": self.players[0].money,
                    "lock_state": self.players[0].lock_state,
                    "prizeholder": self.players[0].prizeholder,
                    "total_dice": self.players[0].total_dice,
                    "location": self.players[0].location,
                    "game_id": self.players[0].game_id
                },
                "player2": {
                    "player_id": self.players[1].id,
                    "screen_name": self.players[1].player_name,
                    "current_pp": self.players[1].money,
                    "lock_state": self.players[1].lock_state,
                    "prizeholder": self.players[1].prizeholder,
                    "total_dice": self.players[1].total_dice,
                    "location": self.players[1].location,
                    "game_id": self.players[1].game_id
                },
                "last_turn_item": {
                    "string": self.last_turn_rand_item[0],
                    "value": self.last_turn_rand_item[1],
                    "player_id": self.last_turn_rand_item[2]
                }
            }
        }
        return game_status

    def load_game(self, game_data, player1, player2):  # Tallennetun pelin lataus tietokannasta
        game = Game(self.game_name, player1[1], player2[1])
        game.game = game_data[0][0]
        game.game_name = game_data[0][1]
        game.round_counter = game_data[0][2]
        game.bag_city = game_data[0][3]
        game.visited = json.loads(game_data[0][4])

        game.player1 = Player(player1[2], player1[7])
        game.player2 = Player(player2[2], player1[7])

        p1 = game.player1.set_player_data(player1)
        self.players.append(p1)
        p2 = game.player2.set_player_data(player2)
        self.players.append(p2)
        return self.json_response()

    @classmethod
    def get_classes(cls, game_name):
        return [inst for inst in cls.instances if inst.game_name == game_name]


class Player:
    player_instances = []

    def __init__(self, player_name, game_id, money=2000, location=16, lock_state=0, prizeholder=0, total_dice=0):
        self.player_name = player_name
        self.game_id = game_id
        self.money = money
        self.location = location
        self.lock_state = lock_state
        self.prizeholder = prizeholder
        self.total_dice = total_dice
        flag = self.check_if_exist()
        if not flag:
            query = (f"INSERT INTO player (screen_name, current_pp, lockstate, prizeholder,"
                     f" total_dice, location, game) VALUES ('{self.player_name}', '{self.money}', '{self.lock_state}',"
                     f" '{self.prizeholder}', '{self.total_dice}', '{self.location}', '{self.game_id}')")

            Game.cursor.execute(query)
            query = f"SELECT id FROM player WHERE screen_name = '{self.player_name}' AND game = '{self.game_id}'"
            Game.cursor.execute(query)
            result = Game.cursor.fetchall()
            self.id = result[0][0]

        else:
            sql = f"SELECT id FROM player WHERE screen_name = '{self.player_name}' AND game = {self.game_id}"
            Game.cursor.execute(sql)
            print("hello")
            result = Game.cursor.fetchone()
            print(result)
            self.id = result[0]
            self.update_db()
        Player.player_instances.append(self)

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
        return self

    def check_if_exist(self):
        sql = f"SELECT * FROM player WHERE game = '{self.game_id}'"
        Game.cursor.execute(sql)
        result = Game.cursor.fetchall()
        for row in result:
            if row[1] == self.player_name:
                return True

        return False

    @classmethod
    def get_players(cls, player_data):
        return [inst for inst in cls.player_instances if
                inst.player_name == player_data[1] and inst.game_id == player_data[7]]

    def get_cities_in_range(player):
        price_multiplier_dict = {
            "fly": config.get('config', 'FlyPriceMultiplier'),  # HUOM Nämä config-filestä tuodut on stringejä!
            "boat": config.get('config', 'BoatPriceMultiplier'),
            "hike": config.get('config', 'HikePriceMultiplier')
        }
        max_distance_dict = {
            "fly": config.get('config', 'MaxDistanceFly'),
            "boat": config.get('config', 'MaxDistanceBoat'),
            "hike": config.get('config', 'MaxDistanceHike')
        }
        travel_modes = ["fly", "boat", "hike"]
        sail_cities_in_range = []
        fly_cities_in_range = []
        hike_cities_in_range = []
        player_location = player[6]
        cities = get_city_data()
        boat_cities = get_ports(cities)
        player_coords = city_id_to_coords(player[6])
        player_pp = player[2]
        for mode in travel_modes:
            price_multiplier = float(price_multiplier_dict[mode])
            max_distance = int(max_distance_dict[mode])
            if mode == "boat":
                for city in boat_cities:
                    distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
                    price = distance_from_player * price_multiplier
                    if city[0] != player_location and distance_from_player <= max_distance and price <= player_pp:
                        sail_cities_in_range.append([city[0], city[1], city[2], distance_from_player, price, city[6]])
            else:
                for city in cities:
                    distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
                    price = distance_from_player * price_multiplier
                    if city[0] != player_location and distance_from_player <= max_distance and price <= player_pp:
                        if mode == "fly":
                            fly_cities_in_range.append(
                                [city[0], city[1], city[2], distance_from_player, price, city[6]])
                        elif mode == "hike":
                            hike_cities_in_range.append(
                                [city[0], city[1], city[2], distance_from_player, price, city[6]])
        return hike_cities_in_range, fly_cities_in_range, sail_cities_in_range