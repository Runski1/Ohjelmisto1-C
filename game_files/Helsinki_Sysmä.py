"""from db_connection import connection

#after_end_game
def ending_check(helsinki_sysmä,player):
    cursor = connection.cursor()
    sql = ("SELECT player.id FROM player INNER JOIN city ON player.location = city.id "
           "WHERE city.name = 'Helsinki' and player.prizeholder= '1'")
    cursor.execute(sql)
    result = cursor.fetchall()

    if player in result: #Jos pelaajan id on listassa löytyneiden pelaajien id:en joukossa, joilla on pääpalkinto
        # niin loppu event käynnnistyy
        helsinki_sysmä()
    else:
        False
def helsinki_sysma(player_id):
    # this article is a stub. """