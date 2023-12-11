import classes
import functions
from flask import Flask, Response
import json
import mysql.connector
from flask_cors import CORS

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)

server = Flask(__name__)
CORS(server)
cursor = connection.cursor()


@server.route('/get_saveGame/<savegame>/')
def get_savegame(savegame):
    sql = f"SELECT * FROM game WHERE name = '{savegame}'"
    cursor.execute(sql)
    cursor.fetchall()
    if cursor.rowcount > 0:
        game_inst = classes.Game.get_classes(savegame)
        return game_inst[0].json_response()
    elif cursor.rowcount == 0:
        response_data = {"gameName": None}
        response = Response(response=json.dumps(response_data), status=200, mimetype='application/json')
        return response


@server.route('/add_player/<gamename>/<player1>/<player2>/')
def create_game(gamename, player1, player2):
    game = classes.Game(gamename, player1, player2)
    data = game.json_response()
    json_data = json.dumps(data, default=vars)
    response = Response(json_data, status=200, mimetype='application/json')
    return response


@server.route('/action/<game_name>/<player_id>/<action>/<target>/')
def do_action(game_name, player_id, action, target):
    # getting the correct player
    game_id = functions.get_game_id(game_name)
    # game_name = functions.get_game_name(game_id)
    game_inst = classes.Game.get_classes(game_name)
    cursor.execute(f"SELECT * FROM player WHERE game={game_id} AND id={player_id}")
    player_data = cursor.fetchone()

    if action == "hike":
        functions.hitchhike(target, game_id, player_data)
        functions.search(game_id, player_data, target)
        functions.add_to_round_counter(game_id)
        return game_inst[0].json_response()
    elif action == "sail":
        functions.sail(target, game_id, player_data)
        functions.search(game_id, player_data, target)
        functions.add_to_round_counter(game_id)
        return game_inst[0].json_response()
    elif action == "fly":
        functions.fly(target, game_id, player_data)
        functions.search(game_id, player_data, target)
        functions.add_to_round_counter(game_id)
        classes.Player.get_players(player_data)
        return game_inst[0].json_response()
    elif action == "work":
        functions.work(game_id, player_data)
        # functions.search(game_id, player_data)
        functions.add_to_round_counter(game_id)
        return game_inst[0].json_response()
    elif action == "test":
        functions.bag_found(game_id, player_data)
        return game_inst[0].json_response()

    @server.route('/end_game/<game>/')  # Loppuun pelatun pelin tyhjennys tietokannasta
    def nuke_me_papi(game):
        print(game)
        print("Uuuhh Nuke me PAPI!")
        sql = f"SELECT * FROM game WHERE name = '{game}'"
        cursor.execute(sql)
        game_data = cursor.fetchone()
        print(game_data)
        sql = f"DELETE FROM player WHERE game = '{game_data[0]}'"
        cursor.execute(sql)
        sql = f"DELETE FROM game WHERE id = '{game_data[0]}'"
        cursor.execute(sql)
        response = {
            "endlife": "Game removed from the universe"
        }
        return Response(json.dumps(response), status=200, mimetype='application/json')

if __name__ == '__main__':
    query = "SELECT * FROM game"
    cursor.execute(query)
    gametable = cursor.fetchall()
    for row in gametable:
        game_id = row[0]
        game_name = row[1]
        round_counter = row[2]
        bag_city = row[3]
        visited = json.loads(row[4].replace("'", "\""))
        query = f"SELECT * FROM player WHERE game = {game_id}"
        cursor.execute(query)
        players = cursor.fetchall()
        playernames = []
        for player in players:
            player_screen_name = player[1]
            player_game = player[6]
            playernames.append(player_screen_name)
        classes.Game(game_name, playernames[0], playernames[1], round_counter, bag_city, visited, game_id)
    server.run(use_reloader=True, host='127.0.0.2', port=3000)
    # (self, game_name, player1_name, player2_name, round_counter=0, bag_city=0, visited=None, game_id=0)
