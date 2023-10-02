from functions import *
import user_input_processor
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

def travel_sail(parameter, player):
    current_player_id = str(player[0])
    available_cities = get_cities_in_range("sail", player)
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
    print('You start sailing to ' + parameter + '.')


