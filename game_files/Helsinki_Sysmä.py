from db_connection import connection

#after_end_game
def ending_check(helsinki_sysmä)
    cursor = connection.cursor()
    sql = ("SELECT PLAYER.id, PLAYER.location, PLAYER.prizeholder FROM player INNER JOIN city ON player.location = city.id "
           "WHERE city.NAME = 'Helsinki' and PLAYER.prizeholder= '1';")
    cursor.execute(sql)
    result = cursor.fetchall()

    if result[0][0:] == player: #Jos pelaajan id on listassa löytyneiden pelaajien id:en joukossa, joilla on pääpalkinto
        # niin loppu event käynnnistyy
        helsinki_sysmä()
    else:
        False
def helsinki_sysmä():
