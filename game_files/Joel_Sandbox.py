from functions import *
from user_input_processor import user_input_processor
from db_connection import connection
def dice_roll():
    dice_num = random.randint(2, 12)
    return dice_num

def get_current_pp(player_id):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
#    print(result)
    return result
def add_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = int(current_pp[0]) + change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor = connection.cursor()
    cursor.execute(query)
#    result = cursor.fetchone()
#    print(result)
    return

def remove_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = int(current_pp[0]) - change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor = connection.cursor()
    cursor.execute(query)
#    result = cursor.fetchone()
#    print(result)
    return

def update_city_status(city_id):
    query = f"UPDATE city SET visited='1' WHERE id='{city_id}'"
    cursor = connection.cursor()
    cursor.execute(query)
    return

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

def travel_sail(parameter, player):
    current_player_id = str(player[0])
    available_cities = get_cities_in_range("boat", player)
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])
    if parameter == "?":
        print("---Available cities where you can sail---\n")
        for city in sorted_available_cities:
            if city[5] == 1:
                visited_status = "visited"
            else:
                visited_status = "not visited"
            print(f"{city[1]:<15}: {city[2]:^25}: {city[3]} km : cost {city[4]:^6.0f} PP {visited_status:>15}")
        user_input_processor(input(f"{player[1]}: "), player)
    elif parameter != "?":
        for city in available_cities:
            if city[1].lower() == parameter:
                set_location(str(city[0]), current_player_id)
                remove_pp(city[4], current_player_id)
                print('You start sailing to ' + parameter + '.')
                break
    else:
        print("Something is wrong here")


