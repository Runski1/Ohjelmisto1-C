import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kadonnut_testamentti',
    user='game',
    password='pass',
    autocommit=True
)

server = Flask(__name__)
@server.route('/game_files/savedgames/<savegame>')
def get saveGame(savegame):
    cursor = connection.cursor()
    cursor.execute(f"")

if __name__ == '__main__':
    server.run(use_reloader = True, host = '127.0.0.1',port = 3000)