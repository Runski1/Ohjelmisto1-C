import classes
import functions
import user_input_processor
import mysql.connector
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

cursor = connection.cursor()

server = Flask(__name__)
CORS(server)

def id_to_name(city_id):
    sql = f"SELECT name from city WHERE id={city_id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result[0])
    #return result[1]

def player_selector(game_id):
    sql = f'SELECT * FROM player WHERE game={game_id}'
    cursor.execute(sql)
    player_list = cursor.fetchall()
    print(player_list)
    return


@server.route('/action_input/<game_name>/<player>/<action>/<target>')
def input_processor(game_name, player, action, target):
    # Hae kannasta oikea peli
    # Valitse sen perusteella oikea pelaaja
    # ????
    # profit

    if action == "hike":
        user_input_processor.travel_hitchhike(target, player)
    elif action == "sail":
        user_input_processor.travel_sail(target, player)
    elif action == "fly":
        user_input_processor.travel_fly(target, player)
    elif action == "work":
        user_input_processor.work("do", player)


player_selector(1)
id_to_name(1)
