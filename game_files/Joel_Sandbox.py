from functions import *
from user_input_processor import user_input_processor
from db_connection import connection

def get_player_data_as_list():
#    cursor = connection.cursor()
    # SQL-kyselyllä kaikki player-taulusta
    sql = "SELECT * FROM player;"
    cursor.execute(sql)
    all_from_player_table = cursor.fetchall()
#    cursor.close()
    # Alustetaan lista
    all_from_player_table_as_list = []
    # Muutetaan kaikki data player-taulusta listaksi
    # Lista on muotoa [[1, pelaaja1_nimi, pelaaja2current_pp, etc][2, pelaaja2_nimi, pelaaja2current_pp, etc]]
    for i in range(len(all_from_player_table)):
        all_from_player_table_as_list.append(list(all_from_player_table[i]))
    return all_from_player_table_as_list

def get_city_data():
#    cursor = connection.cursor()
    sql = "SELECT * from city;"
    cursor.execute(sql)
    all_from_city = cursor.fetchall()
#    cursor.close()
    all_data_from_city_as_list = []
    for i in range(len(all_from_city)):
        all_data_from_city_as_list.append((list(all_from_city[i])))
    return all_data_from_city_as_list


def get_cities_in_range(travel_mode, player):
    price_multiplier_dict = {
        "fly": 1,
        "boat": 0.5,
        "hike": 0
    }
    max_distance_dict = {
        "fly": 9999999999,
        "boat": 1000,
        "hike": 1000
    }
    price_multiplier = price_multiplier_dict[travel_mode]
    max_distance = max_distance_dict[travel_mode]
    player_location = player[8]
    cities = get_city_data()
    if travel_mode == "boat":
        cities = get_ports(cities)
    player_coords = ((cities[player[8] - 1][3]), (cities[player[8] - 1][4]))
    player_pp = player[2]
    cities_in_range = []
    for city in cities:
        distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
        price = distance_from_player * price_multiplier
        if city[0] != player_location and (distance_from_player <= max_distance and
                                           price <= player_pp):
            cities_in_range.append([city[0], city[1], city[2], distance_from_player, price, city[6]])
    return cities_in_range

def travel_sail(parameter, player):
    # player-muuttujassa tuodaan koko vuorossa olevan pelaajan rivi tietokannasta
    current_player_id = str(player[0])  # pelaajan id stringinä
    available_cities = get_cities_in_range("boat", player)  # boat-parametri tätä funktiota varten
    sorted_available_cities = sorted(available_cities, key=lambda x: x[3])  # lambda-funktio järjestää etäisyyden mukaan
    # pienimmästä etäisyydestä suorimpaan listan saavuttettavissa olevista kaupungeista
    if parameter == "?":  # Tämä tulostaa pelaajalle saavutettavissa olevat kaupungit
        print("---Available cities where you can fly---\n")
        for city in sorted_available_cities:
            if city[5] == 1:  # if-else tulostaa visited tai not visited riippuen kaupungin tilasta
                visited_status = "visited"
            else:
                visited_status = "not visited"
            # printti muotoituna taulukkomaiseksi, aja funktio niin näet
            print(f"{city[1]:<15}: {city[2]:^25}: {city[3]} km : cost {city[4]:^6.0f} PP {visited_status:>15}")
        print(f"You have {get_current_pp(current_player_id)} PP.")  # viimeiseksi tuloste pelaajan rahamäärästä
        return True
        # koska tämän jälkeen pelaaja voi valita mihin lentää, tai tehdä muun toiminnon
    elif parameter != "?":  # käsittelee kohdekaupungiksi syötetyn parametrin
        for city in available_cities:
            if city[1].lower() == parameter:
                set_location(str(city[0]), current_player_id)  # vaihdetaan pelaajan sijainti
                remove_pp(city[4], current_player_id)  # vähennetään laivamatkan hinta pelaajan rahoista
                print("You begin your sail to " + parameter + ".")  # kuittaus onnistuneesta matkasta
                break  # kaupunkilooppi rikki kun kohdekaupunki on löytynyt
        return False
    else:
        print("Something is wrong here")
        return True
