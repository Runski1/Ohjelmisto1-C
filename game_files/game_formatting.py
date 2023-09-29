def format_database_for_new_game(sql_connection):
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
    # Tämä alla oleva on vain testi toimiiko DB
    query = "SELECT * FROM city;"
    cursor.execute(query)
    return cursor.fetchall()


def format(sql_connection):
format_database_for_new_game()