'''connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='kadonnut_testamentti',
         user='game',
         password='pass',
         autocommit=True
         )
'''
import sys
import time

teksti = "Tervetuloa Python-kirjain kerrallaan!"

for kirjain in teksti:
    sys.stdout.write(kirjain)
    sys.stdout.flush()  # Päivitä näyttö
    time.sleep(0.05)     # Odota 0.1 sekuntia ennen seuraavaa kirjainta

# Lopuksi, jätä kursori paikalleen
sys.stdout.write('\n')