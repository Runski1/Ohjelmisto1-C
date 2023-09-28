import mysql.connector
import geopy

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='root',
         password='rootwadap',
         autocommit=True
         )

def get_flight_route(player_id)
    cursor = connection.cursor()
    query1 = f"select player.current_pp, latitude_deg, longitude_deg from city inner join player on city.id = player.location where player.id = '{player_id}'"
    quert2 =     kaikki kaupungit
    result = cursor.fetchall()
