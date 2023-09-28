import functions
import user_input_processor
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='game',
         password='pass',
         autocommit=True
         )
