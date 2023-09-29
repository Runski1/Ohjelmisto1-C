import random
import os
# Matias kävi lisäämässä funktioihin sql_connection-parametrit siinä toiveissa että connectionin voi muodostaa vain
# mainissa ja kantaa sieltä minne tarvitseekaan


def dice_roll():
    dice_num = random.randint(2, 12)
    return dice_num


def get_current_pp(player_id, sql_connection):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
    cursor = sql_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
#    print(result)
    return result


def add_pp(change_amount, player_id, sql_connection):
    current_pp = get_current_pp(player_id, sql_connection)
    new_pp = int(current_pp[0]) + change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor = sql_connection.cursor()
    cursor.execute(query)
#    result = cursor.fetchone()
#    print(result)
    return


def remove_pp(change_amount, player_id, sql_connection):
    current_pp = get_current_pp(player_id, sql_connection)
    new_pp = int(current_pp[0]) - change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor = sql_connection.cursor()
    cursor.execute(query)
#    result = cursor.fetchone()
#    print(result)
    return

def format_database_for_new_game(sql_connection):
    try:
        # current working dir
        cwd = os.getcwd()
        # Itellä on tuo with open-syntaksi vähän ymmärryksen tavoittamattomissa
        with open(cwd + "/create_game_db.sql", "r") as sql_file:
            sql_queries = sql_file.read().split(";")  # Lukee filen, splittaa ;-merkistä listaksi
        cursor = sql_connection.cursor()
        for sql_query in sql_queries:
            sql_query = sql_query.strip()  # Vedetään tyhjät pois
            if sql_query:  # onko query tyhjä? -> FALSE
                cursor.execute(sql_query)
        sql_connection.commit()
        return "Database formatting completed."
    except:
        return "Something went wrong with database formatting."

