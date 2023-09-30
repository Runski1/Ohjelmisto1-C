import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='game',
         password='pass',
         autocommit=True
         )



# force id(normaalisti tietokannasta)
current_player_id = 1
# force(range multiplier) (config)
flight_range_multiply = 1
# force travel mode (config)
chosen_travel_mode = 'hike'

print(get_cities_in_range(chosen_travel_mode, current_player_id, flight_range_multiply))
