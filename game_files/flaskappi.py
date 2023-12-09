import classes
import functions
from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)

server = Flask(__name__)
cursor = connection.cursor()


@server.route('/get_saveGame/<savegame>')
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
    return json_data


@server.route('/action/<game_id>/<player_id>/<action>/<target>')
def do_action(game_id, player_id, action, target):
    # getting the correct player
    cursor.execute(f"SELECT * FROM player WHERE game={game_id} AND id={player_id}")
    player_data = cursor.fetchone()
    game_name = functions.get_game_name(game_id)

    if action == "hike":
        functions.hitchhike(target, game_id, player_data)
        functions.search(game_id, player_data)
        return game_name.json_response()
    elif action == "sail":
        functions.sail(target, game_id, player_data)
        functions.search(game_id, player_data)
        return game_name.json_response()
    elif action == "fly":
        functions.fly(target, game_id, player_data)
        functions.search(game_id, player_data)
        return game_name.json_response()
    elif action == "work":
        functions.work(game_id, player_id)
        functions.search(game_id, player_data)
        return game_name.json_response()


if __name__ == '__main__':
    server.run(use_reloader=True, host='127.0.0.1', port=3000)
