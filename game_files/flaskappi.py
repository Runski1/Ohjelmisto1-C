# from game_files import user_input_processor
import classes
import functions
from flask import Flask, Response
import json
from db_connection import connection

server = Flask(__name__)


@server.route('/get_saveGame/<savegame>')
def get_savegame(savegame):
    cursor = connection.cursor()
    sql = f"SELECT * FROM game WHERE name = '{savegame}'"
    cursor.execute(sql)

    if cursor.rowcount > 0:
        game_data = cursor.fetchall()
        sql = f"SELECT * FROM player WHERE game = '{game_data[0][0]}'"
        cursor.execute(sql)
        players = cursor.fetchall()
        player1 = players[0]
        player2 = players[1]
        game = classes.Game(savegame, player1[1], player2[1])
        print(game.players)
        response_data = game.json_response()
        response = Response(response=json.dumps(response_data), status=200, mimetype='application/json')
        return response

    elif cursor.rowcount == 0:
        response_data = {"gameName": None}
        response = Response(response=json.dumps(response_data), status=200, mimetype='application/json')
        return response



#  else:


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
#   response_data = json.dumps(response_data)
#   response = Response(response=response_data, status=status_code, mimetype="application/json")

#   return response


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
        print()
        functions.work(game_id, player_id)
        functions.search(game_id, player_data)
        return game_name.json_response()


if __name__ == '__main__':
    server.run(use_reloader=True, host='127.0.0.1', port=3000)

    # testi ip
