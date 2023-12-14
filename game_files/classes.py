import random
import db_connection
import json
from geopy.distance import geodesic
from math import floor
from config import config


class Game:
    cursor = db_connection.connection.cursor()
    instances = []

    def __init__(self, game_name, player1_name, player2_name, round_counter=0, bag_city=0, visited=None, game_id=0):
        if visited is None:
            self.visited = ["16"]
        else:
            self.visited = visited
        self.players = []
        self.game_name = game_name
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.round_counter = round_counter
        self.bag_city = bag_city
        self.game_id = game_id
        if self.game_id == 0:
            self.generate_bag()
            self.update_db()
    #        self.game_id = self.get_game_id(self.game_name)
        self.babymaker(self.player1_name, self.game_id)
        self.babymaker(self.player2_name, self.game_id)
        self.update_db()
        Game.instances.append(self)
        self.last_turn_income = [None, None, None, None]

    def get_game_id(self, game_name):  # Pelin id saaminen koska olio luodaan ennen tietokantaan tallennusta
        sql = f"SELECT id FROM game WHERE name = %s"
        self.cursor.execute(sql, (game_name,))
        result = self.cursor.fetchall()
        return result[0][0]

    def update_db(self):  # Datan tallennus tietokantaan
        sql = f"SELECT * FROM game WHERE name = %s"
        self.cursor.execute(sql, (self.game_name,))
        data = self.cursor.fetchone()
        if self.cursor.rowcount > 0:
            self.round_counter = data[2]
            visited_json = json.dumps(data[4].replace("'", "\""))
            query = (f"UPDATE game SET round_counter = {data[2]}, visited = {visited_json}"
                     f" WHERE name = %s")
            self.cursor.execute(query, (self.game_name,))
            self.update_players()
        else:
            visited_json = json.dumps(self.visited)
            query = (f"INSERT INTO game (name, round_counter, bag_city, visited)"
                     f" VALUES(%s, '{self.round_counter}', '{self.bag_city}', '{visited_json}')")
            self.cursor.execute(query, (self.game_name,))
            self.game_id = self.get_game_id(self.game_name)
            self.update_players()

    def update_players(self):
        for player in self.players:
            sql = f"SELECT * FROM player WHERE screen_name = %s AND game = '{self.game_id}'"
            self.cursor.execute(sql, (player.player_name,))
            data = self.cursor.fetchone()
            if self.cursor.rowcount > 0:
                player.set_player_data(data)
            else:
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
        self.players[0].get_cities_in_range()
        self.players[1].get_cities_in_range()
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
                    "game_id": self.players[0].game_id,
                    "cities_in_range": {
                        "hike": self.players[0].hike_cities_in_range,
                        "fly": self.players[0].fly_cities_in_range,
                        "sail": self.players[0].sail_cities_in_range
                    }
                },
                "player2": {
                    "player_id": self.players[1].id,
                    "screen_name": self.players[1].player_name,
                    "current_pp": self.players[1].money,
                    "lock_state": self.players[1].lock_state,
                    "prizeholder": self.players[1].prizeholder,
                    "total_dice": self.players[1].total_dice,
                    "location": self.players[1].location,
                    "game_id": self.players[1].game_id,
                    "cities_in_range": {
                        "hike": self.players[1].hike_cities_in_range,
                        "fly": self.players[1].fly_cities_in_range,
                        "sail": self.players[1].sail_cities_in_range
                    }
                },
                "last_turn_item": {
                    "string": self.last_turn_income[0],
                    "value": self.last_turn_income[1],
                    "player_id": self.last_turn_income[2],
                    "work_salary": self.last_turn_income[3]
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
                     f" total_dice, location, game) VALUES (%s, '{self.money}', '{self.lock_state}',"
                     f" '{self.prizeholder}', '{self.total_dice}', '{self.location}', '{self.game_id}')")

            Game.cursor.execute(query, (self.player_name,))
            query = f"SELECT id FROM player WHERE screen_name = %s AND game = '{self.game_id}'"
            Game.cursor.execute(query, (self.player_name,))
            result = Game.cursor.fetchall()
            self.id = result[0][0]

        elif flag:
            sql = f"SELECT * FROM player WHERE screen_name = %s AND game = {self.game_id}"
            Game.cursor.execute(sql, (self.player_name,))
            result = Game.cursor.fetchone()
            self.id = result[0]
            self.set_player_data(result)
        self.hike_cities_in_range = []
        self.fly_cities_in_range = []
        self.sail_cities_in_range = []
        self.get_cities_in_range()
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

    def get_cities_in_range(self):
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
        player_location = self.location
        cities = self.get_city_data()
        boat_cities = self.get_ports(cities)
        player_coords = self.city_id_to_coords()
        player_pp = self.money
        for mode in travel_modes:
            price_multiplier = float(price_multiplier_dict[mode])
            max_distance = int(max_distance_dict[mode])
            if mode == "boat":
                for city in boat_cities:
                    distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
                    price = floor(distance_from_player * price_multiplier)
                    if city[0] != player_location and distance_from_player <= max_distance and price <= player_pp:
                        sail_cities_in_range.append([city[0], city[1], city[2], distance_from_player, price])
            else:
                for city in cities:
                    distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
                    price = floor(distance_from_player * price_multiplier)
                    if city[0] != player_location and distance_from_player <= max_distance and price <= player_pp:
                        if mode == "fly":
                            fly_cities_in_range.append(
                                [city[0], city[1], city[2], distance_from_player, price])
                        elif mode == "hike":
                            hike_cities_in_range.append(
                                [city[0], city[1], city[2], distance_from_player, price])

        self.hike_cities_in_range = hike_cities_in_range
        self.fly_cities_in_range = fly_cities_in_range
        self.sail_cities_in_range = sail_cities_in_range

    def get_city_data(self):
        sql = "SELECT * from city"
        Game.cursor.execute(sql)
        all_from_city = Game.cursor.fetchall()
        all_data_from_city_as_list = []
        for i in range(len(all_from_city)):
            all_data_from_city_as_list.append((list(all_from_city[i])))
        return all_data_from_city_as_list

    def get_ports(self, cities):
        port_cities = []
        for city in cities:
            if city[5] == 1:
                port_cities.append(city)
        return port_cities

    def city_id_to_coords(self):
        sql = f"SELECT latitude_deg, longitude_deg FROM city WHERE id={self.location}"
        Game.cursor.execute(sql)
        coords = Game.cursor.fetchone()
        return coords
