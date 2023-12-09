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
    game_data = cursor.fetchall()

    if cursor.rowcount > 0:
        sql = f"SELECT * FROM player WHERE game = '{game_data[0][0]}'"
        cursor.execute(sql)
        players = cursor.fetchall()
        player1 = players[0]
        player2 = players[1]
        game = classes.Game(savegame, player1[1], player2[1])
        response_data = game.json_response()
        response = Response(response=json.dumps(response_data, default=vars), status=200, mimetype='application/json')
        return response

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
        functions.work(game_id, player_id)
        # functions.search(game_id, player_data)
        functions.add_to_round_counter(game_id)
        return game_inst[0].json_response()
    elif action == "test":
        functions.bag_found(game_id, player_data)
        return game_inst[0].json_response()


if __name__ == '__main__':
    server.run(use_reloader=False, host='127.0.0.1', port=3000)
