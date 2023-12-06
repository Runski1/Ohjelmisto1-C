from game_files import classes
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
    sql_result = {"gameName": 'testgame', 'players': {'player1': 'ville', 'player2': 'jari'}}
    if savegame == 'testgame':
        response_data = sql_result
        status_code = 200

    else:
        response_data = {"gameName":"not found"}
        status_code = 200
        # classes.Game(sql_result['gameName'], sql_result['players'])


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
    game.add_to_db()
    json_data = game.json_response()
    cursor = connection.cursor()
    cursor.execute()
    connection.commit()
    cursor.close()


@server.route('/action/<savedGame>/<playername>/<action>/<target>')
def do_action(gamename, player_id, action, target):
    cursor = connection.cursor()
    cursor.execute(f"select name, playerName from savedGames where name = '{name}'")
    sql_result = cursor.fetchone()
    #kesken


if __name__ == '__main__':
    server.run(use_reloader=True, host='127.0.0.2', port=3000)

    #testi ip
