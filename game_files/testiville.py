from  db_connection import connection

def search(player):
    cursor = connection.cursor()
    sql = (f"SELECT bag_city FROM CITY inner join player "
           f"on city.id = player.location and player.screen_name = '{player}';")
    cursor.execute(sql)
    result = cursor.fetchall()
    if result[0] == 1:
        print('Congratulation you have found grandma`s lost luggage!!! Be fast and head back to Helsinki before anyone '
              ' else does!')
    else:
        item_name, item_value = item_randomizer()
        print(f'Nah! No grandma`s luggage in here! But you found {item_name} and it`s worth {item_value}')
        if item_value <= 0:
            remove_pp(item_value, player[0]) #player 0 on id
        elif item_value >=0:
            add_pp(item_value, player[0])
    return False
player=1
print(search(player))