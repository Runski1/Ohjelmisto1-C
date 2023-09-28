import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='viimeinen_testamentti',
         user='root',
         password='rootwadap',
         autocommit=True
         )

def get_flight_route(player_id)
    cursor = connection.cursor()
    cursor.execute(f"select current_PP.player, latitude.city,longitude.city FROM player, city where player.id = '{player_id}' group by type")
    result = cursor.fetchall()  # hakee ensimmäisen tulosrivin