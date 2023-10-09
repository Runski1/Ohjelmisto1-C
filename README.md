## Asennus

ajakaa create_game_user.sql omaan tietokantaanne
**HUOM: se droppaa käyttäjän nimeltä "game" ja luo uuden tilalle**

Pythonkoodi alustaa tietokannan (*Ohjelmisto1-C/game_files/functions.py* -tiedoston funktio *format_database_for_new_game()*)
**Droppaa tietokannan nimeltä "kadonnut_testamentti" ja luo uuden tilalle**
sitä teiltä tuskin löytyy, mutta ajattelin huomauttaa

### Tarvittavat paketit

Koodimme käyttää colorama, mysql-connector-python ja geopy -paketteja ja python3.9 -versiota.
Noilla samoilla nimillä löytyy jos asentaa komentoriviä käyttäen pip:llä.
Jos ajatte ohjelman pycharmissa, värit eivät välttämättä tulostu kuten on suunniteltu, jos käytössä on jokin erikseen ladattu tyylipaketti.

### Muuta
create_game_db.sql-tiedoston tulee olla samassa kansiossa kuin functions.py-tiedoston jotta tietokannan alustusfunktio toimii
Ohjelma käynnistyy ajamalla main.py
