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

server = Flask(__name__)
CORS(server)


@server.route('action_input/<game_name>/<player>/<action>/<target>')
def input_processor(game_name, player, action, target):
    #Hae kannasta oikea peli
    #Valitse sen perusteella oikea pelaaja
    #????
    #profit

    if action == "hike":
        user_input_processor.travel_hitchhike(target, player)
    elif action == "sail":
        user_input_processor.travel_sail(target, player)
    elif action == "fly":
        user_input_processor.travel_fly(target, player)
    elif action == "work":
        user_input_processor.work("do",player)

