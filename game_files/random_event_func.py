import mysql.connector
import random

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)

cursor = connection.cursor()


# funktio joka laskee montako eventtiä on yhteensä
# sen jälkeen arpoo tuleeko eventti
# jos tulee arpoo eventin tietokannasta ja palauttaa sen
# jos ei printtaa jotain

def event_randomizer():
    sql = "SELECT COUNT(id) FROM random_events;"
    cursor.execute(sql)
    result = cursor.fetchall()
    len_events = 0
    if cursor.rowcount > 0:
        for row in result:
            len_events = row[0]
    rand_test = random.randint(1, 6)

    if rand_test % 2 == 1:
        print("No eventos for you m8!")
        return
    elif rand_test % 2 == 0:
        randomized_num = random.randint(1, len_events)
        sql = "SELECT fluff FROM random_events WHERE id = '" + str(randomized_num) + "';"
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            return result

