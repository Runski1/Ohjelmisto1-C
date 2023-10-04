from db_connection import connection

#after_end_game

cursor = connection.cursor()
sql = "SELECT id, location, prizeholder from player where prizeholder='1';"
cursor.execute(sql)
result = cursor.fetchall()



if result[1] == "Helsinki" and result[0] == player:
    helsinki_sysmä()
#if player location == helsinki and prizeholder ==1
def helsinki_sysmä():
