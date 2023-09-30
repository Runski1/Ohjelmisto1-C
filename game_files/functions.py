import random
import os
from db_connection import connection
from geopy.distance import geodesic
cursor = connection.cursor()
# Matias kävi lisäämässä funktioihin sql_connection-parametrit siinä toiveissa että connectionin voi muodostaa vain
# mainissa ja kantaa sieltä minne tarvitseekaan


def dice_roll():
    dice_num = random.randint(2, 12)
    return dice_num


def get_current_pp(player_id):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    #    print(result)
    return result


def add_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = int(current_pp[0]) + change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor.execute(query)
    #    result = cursor.fetchone()
    #    print(result)
    return


def remove_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = int(current_pp[0]) - change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor.execute(query)
    #    result = cursor.fetchone()
    #    print(result)
    return


def format_database_for_new_game():
    try:
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
        return "Database formatting completed."
    except:
        return ("Something went wrong with database formatting.\n"
                "Try to think of better exception rule")


def get_location(player_id):
    sql = "SELECT name FROM city INNER JOIN player ON city.id = player.location"
    sql += " WHERE player.id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def lock_check(player_id):
    sql = "SELECT lockstate FROM player"
    sql += " WHERE id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    lock_state = int(result[0][0])
    if lock_state == 0:
        return "Not locked"
    else:
        return lock_state


def printer(name, player_id):
    current_pp = list(get_current_pp(player_id))
    current_location = get_location(player_id)
    lock_status = lock_check(player_id)
    print("---Player status---\n")
    print(f"Name: {name}")
    print(f"Current PP: {current_pp[0]}")
    print(f"Location: {current_location[0][0]}")
    print(f"Lock state: {lock_status}")


def get_player_data_as_list():
    # SQL-kyselyllä kaikki player-taulusta
    sql = "SELECT * FROM player;"
    cursor.execute(sql)
    all_from_player_table = cursor.fetchall()
    # Alustetaan lista
    all_from_player_table_as_list = []
    # Muutetaan kaikki data player-taulusta listaksi
    # Lista on muotoa [[1, pelaaja1_nimi, pelaaja2current_pp, etc][2, pelaaja2_nimi, pelaaja2current_pp, etc]]
    for i in range(len(all_from_player_table)):
        all_from_player_table_as_list.append(list(all_from_player_table[i]))
    return all_from_player_table_as_list


def get_round_number():
    sql = "SELECT counter FROM round_counter;"
    cursor.execute(sql)
    return cursor.fetchone()[0]


def add_to_round_counter():
    sql = "UPDATE round_counter SET counter = counter + 1"
    cursor.execute(sql)


def get_cities_in_range(travel_mode, player_id, multiply):
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
    # pelaajan sijainti
    player_location = (player_data[0][1], player_data[0][2])
    city_in_range = {}  # sanakirja kaupungeista ja etäisyydestä pelaajaan
    # Käy läpi kaupungit ja tarkistaa voiko pelaaja matkustaa sinne
    for city in city_data:
        city_name = city[0]
        latitude_deg = city[1]
        longitude_deg = city[2]
        city_location = (latitude_deg, longitude_deg)
        distance = geodesic(player_location, city_location).kilometers
        # testaa onko kaupunki saavutettavan matkan päässä, jos on niin se lisätään listaan
        if travel_mode == 'boat' or 'hike' and distance <= 1000 and distance <= available_range:
            city_in_range[city_name] = distance
        elif distance <= available_range:
            city_in_range[city_name] = distance
    result = city_in_range
    return result
