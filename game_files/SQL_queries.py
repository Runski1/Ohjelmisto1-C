import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='root',
         password='rootwadap',
         autocommit=True
         )

def get_route(travel_mode,player_id,multiply):
    cursor = connection.cursor()
    query1 = (f"select player.current_pp,latitude_deg,longitude_deg from city inner join player on "
              f"city.id = player.location where player.id = '{player_id}'")
    query2 = f"select name,latitude_deg , longitude_deg from city group by name"
    query3 = f"select name,latitude_deg , longitude_deg from city where port_city = '1' group by name"

    if travel_mode == 'boat':
        query2 = query3


    cursor.execute(query1)
    player_data = cursor.fetchall()
    available_range = player_data[0][0] * multiply
    # laskee pelaajan maksimi rangen annetulla kertoimella ja nykyisellä rahan määrällä



    # hakee kaikki kaupungit pelialueelta

    cursor.execute(query2)
    city_data = cursor.fetchall()

    #pelaajan sijainti
    player_location = (player_data[0][1],player_data[0][2])

    city_in_range=[]


    #Käy läpi kaupungit ja tarkistaa voiko pelaaja matukstaa sinne
    for city in city_data:
        city_name = city[0]
        latitude_deg = city[1]
        longitude_deg = city[2]
        city_location = (latitude_deg,longitude_deg)
        distance = geodesic(player_location, city_location).kilometers

        # testaa onko kaupunki saavutettavan matkan päässä, jos on niin se lisätään listaan
        if travel_mode == 'boat' or  'hike' and distance <=1000 and distance <= available_range:
            city_in_range.append(city_name)
        elif distance <= available_range:
            city_in_range.append(city_name)
    result = city_in_range

    return result
#force id(normaalisti tietokannasta
player_id= 1
#multiplieri configista
flight_range_multiply = 1
travel_mode = 'hike'

print(get_route(travel_mode, player_id,flight_range_multiply))





