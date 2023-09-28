import functions, user_input_processor, mysql
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='game',
         password='pass',
         autocommit=True
         )




while True:

