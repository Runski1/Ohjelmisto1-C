from db_connection import connection

#after_end_game
'''def ending_check(helsinki_sysmä,player)
    cursor = connection.cursor()
    #tarkistaa onko nykyisellä pelaajalla laukku
    sql = ("SELECT player.id FROM player INNER JOIN city ON player.location = city.id
           "WHERE city.name = 'Helsinki' and player.prizeholder= '1'")
    cursor.execute(sql)
    result = cursor.fetchall()

    if player in result: #Jos pelaajan id on listassa löytyneiden pelaajien id:en joukossa, joilla on pääpalkinto
        # niin loppu event käynnnistyy
        helsinki_sysmä()
    else:
        False'''


import sys
import time
def helsinki_sysma():
    print("You have arrived to Helsinki! Your grandma lives in Sysmä, so you have to order Dungo-driver to get there.")
    calling_text = [".", "..", "...", "...."]
    for _ in range(2):
        for text in calling_text:

            sys.stdout.write('\r'"Calling"+ text)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(text) + '\r')  # Hide the text
            sys.stdout.flush()
            time.sleep(0.5)


helsinki_sysma()

    #dice_roll()