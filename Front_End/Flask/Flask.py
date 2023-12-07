from game_files import user_input_processor
from game_files import classes
from game_files import functions
from flask import Flask, Response, Request
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


@server.route('/get_saveGame/<savegame>')
def get_savegame(savegame):
    cursor = connection.cursor()
    sql_result = {"gameName": 'testgame', 'players': {'player1': 'ville', 'player2': 'jari'}}
    sql = f"SELECT name FROM game WHERE name = '{savegame}'"
    cursor.execute(sql)
    if cursor.rowcount == 0:
        response_data = {"gameName": None}
        response = Response(response=json.dumps(response_data), status=200, mimetype='application/json')
        return response
    else:
        game_data = cursor.fetchall()
        sql = f"SELECT * FROM player WHERE game = '{functions.id_to_name()}'"
    if savegame == 'testgame':
        response_data = sql_result
        status_code = 200




    else:


    # '''cursor = connection.cursor()
    # cursor.execute(f"select name, playerName from savedGames where name = '{savegame}'")
    # sql_result = cursor.fetchone()
    # if sql_result:
    #     response_data = {"gameName": f'{sql_result[0]}', "players": [f'{sql_result[1]}']}
    #     status_code = 200
    # else:
    #     cursor.execute("INSERT INTO savedGames (name) VALUES (%s)", (savegame,))
    #     response_data = {"gameName": "not found"}
    #     status_code = 400'''
    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=status_code, mimetype="application/json")

    return response


@server.route('/add_player/<gamename>/<player1>/<player2>/')
def create_game(gamename, player1, player2):
    game = classes.Game(gamename, player1, player2)
    game.update_db()
    json_data = game.json_response()
    connection.commit()


@server.route('/action/<game_id>/<player_id>/<action>/<target>')
def do_action(game_id, player_id, action, target):
    cursor = connection.cursor()
    # getting the correct player

    cursor.execute(f"SELECT * FROM player WHERE (game={game_id} AND id={player_id})")
    player_data = cursor.fetchall()

    # muunnetaan target cityn id nimeksi
    city_name = functions.id_to_name(target)

    # tarkistetaan on pelaajalla rahaa matkaan

    if action == "hike":
        user_input_processor.travel_hitchhike(city_name, player_id)
        return False
    elif action == "sail":
        user_input_processor.travel_sail(city_name, player_id)
        return False
    elif action == "fly":
        user_input_processor.travel_fly(city_name, player_id)
        return False
    elif action == "work":
        user_input_processor.work("do", player_id)
        return False


if __name__ == '__main__':
    server.run(use_reloader=True, host='127.0.0.2', port=3000)

    # testi ip
