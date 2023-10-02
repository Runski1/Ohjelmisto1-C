import random
import os
from db_connection import connection
from geopy.distance import geodesic
from math import floor

cursor = connection.cursor()
# Testaan, auttaako cursorin tappaminen ja uudelleen luominen jokaisessa funktiossa
# mysql.connector.errors.DatabaseError: 2014 (HY000): Commands out of sync; you can't run this command now
# -erroriin


def dice_roll():
    dice_num = random.randint(2, 12)
    return dice_num


def get_current_pp(player_id):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
  #  cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
#    cursor.close()
    return result


def add_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = current_pp + change_amount
 #   cursor = connection.cursor()
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor.execute(query)
 #   cursor.close()
    #    result = cursor.fetchone()
    #    print(result)
    return


def remove_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = current_pp - change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
#    cursor = connection.cursor()
    cursor.execute(query)
 #   cursor.close()
    return


def format_database_for_new_game():
    try:
 #       cursor = connection.cursor()
        # current working dir
        cwd = os.getcwd()
        # Itellä on tuo with open-syntaksi vähän ymmärryksen tavoittamattomissa
        with open(cwd + "/create_game_db.sql", "r") as sql_file:
            sql_queries = sql_file.read().split(";")  # Lukee filen, splittaa ;-merkistä listaksi
        for sql_query in sql_queries:
            sql_query = sql_query.strip()  # Vedetään tyhjät pois
            if sql_query:  # onko query tyhjä? -> FALSE
                cursor.execute(sql_query)
        connection.commit()
 #       cursor.close()
        return "Database formatting completed."
    except:
        return ("Something went wrong with database formatting.\n"
                "Try to think of better exception rule")


def get_location(player_id):
#    cursor = connection.cursor()
    sql = "SELECT name FROM city INNER JOIN player ON city.id = player.location"
    sql += " WHERE player.id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
#    cursor.close()
    return result


def set_location(new_location, player_id):
#    cursor = connection.cursor()
    sql = "UPDATE player SET location = '" + new_location + "' WHERE player.id = '" + player_id + "';"
    sql += "UPDATE city SET visited = 1 WHERE city.id = '" + new_location + "';"
    cursor.execute(sql)
#    cursor.close()


def lock_check(player_id):
#    cursor = connection.cursor()
    sql = "SELECT lockstate FROM player"
    sql += " WHERE id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
#    cursor.close()
    lock_state = int(result[0][0])
    if lock_state == 0:
        return "Not locked"
    else:
        return lock_state


def printer(name, player_id):
    current_pp = get_current_pp(player_id)
    current_location = get_location(player_id)
    lock_status = lock_check(player_id)
    print("---Player status---\n")
    print(f"Name: {name}")
    print(f"Current PP: {current_pp}")
    print(f"Location: {current_location[0][0]}")
    print(f"Lock state: {lock_status}")


def get_player_data_as_list():
#    cursor = connection.cursor()
    # SQL-kyselyllä kaikki player-taulusta
    sql = "SELECT * FROM player;"
    cursor.execute(sql)
    all_from_player_table = cursor.fetchall()
#    cursor.close()
    # Alustetaan lista
    all_from_player_table_as_list = []
    # Muutetaan kaikki data player-taulusta listaksi
    # Lista on muotoa [[1, pelaaja1_nimi, pelaaja2current_pp, etc][2, pelaaja2_nimi, pelaaja2current_pp, etc]]
    for i in range(len(all_from_player_table)):
        all_from_player_table_as_list.append(list(all_from_player_table[i]))
    return all_from_player_table_as_list


def get_round_number():
#    cursor = connection.cursor()
    sql = "SELECT counter FROM round_counter;"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
#    cursor.close()
    return result


def add_to_round_counter():
#    cursor = connection.cursor()
    sql = "UPDATE round_counter SET counter = counter + 1"
    cursor.execute(sql)
#    cursor.close()


def get_city_data():
#    cursor = connection.cursor()
    sql = "SELECT * from city;"
    cursor.execute(sql)
    all_from_city = cursor.fetchall()
#    cursor.close()
    all_data_from_city_as_list = []
    for i in range(len(all_from_city)):
        all_data_from_city_as_list.append((list(all_from_city[i])))
    return all_data_from_city_as_list

def get_ports(cities):
    port_cities = []
    for city in cities:
        if city[7] == 1:
            port_cities.append(city)
    return port_cities

def get_cities_in_range(travel_mode, player):
    price_multiplier_dict = {
        "fly": 1,
        "boat": 0.5,
        "hike": 0
    }
    max_distance_dict = {
        "fly": 9999999999,
        "boat": 1000,
        "hike": 1000
    }
    price_multiplier = price_multiplier_dict[travel_mode]
    max_distance = max_distance_dict[travel_mode]
    player_location = player[8]
    cities = get_city_data()
    if travel_mode == "boat":
        cities = get_ports(cities)
    player_coords = ((cities[player[8] - 1][3]), (cities[player[8] - 1][4]))
    player_pp = player[2]
    cities_in_range = []
    for city in cities:
        distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
        price = distance_from_player * price_multiplier
        if city[0] != player_location and (distance_from_player <= max_distance and
                                           price <= player_pp):
            cities_in_range.append([city[0], city[1], city[2], distance_from_player, price, city[6]])
    return cities_in_range

