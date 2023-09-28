import random
def dice_roll():
    dice_num = random.randint(2, 12)
<<<<<<< HEAD:game_files/functions.py
    return dice_num
=======
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
>>>>>>> b7cdff4664d557a4285cd38e431da1f0bd006f94:game_files/Functions.py
