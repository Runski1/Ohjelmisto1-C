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

