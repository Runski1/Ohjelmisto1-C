from db_connection import connection

#after_end_game

cursor = connection.cursor()
sql = ("SELECT PLAYER.id, PLAYER.location, PLAYER.prizeholder FROM player INNER JOIN city ON player.location = city.id "
       "WHERE city.NAME = 'Helsinki';")
cursor.execute(sql)
result = cursor.fetchall()

if result[0][0:] == player: #Jos pelaajan id on listassa löytyneiden pelaajien id:en joukossa niin loppu event käynnnis
    # tyy
    helsinki_sysmä()

def helsinki_sysmä():
