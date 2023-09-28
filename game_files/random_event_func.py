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


def event_randomizer():
    sql = "SELECT COUNT(*)"
    sql += " FROM random_events GROUP BY fluff;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            len_events = row[0]
    rand_test = random.randint(1, 6)

    if rand_test % 2 == 1:
        print("Nothing happened!")
    elif rand_test % 2 == 0:
        randomized_num = random.randint(1, len_events)
        sql = "SELECT fluff FROM random_events"
        sql += " WHERE id = '" + str(randomized_num) + "';"
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            return result


lol = event_randomizer()
for i in lol:
    print(i)
