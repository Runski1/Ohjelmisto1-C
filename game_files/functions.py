import random
import os
from db_connection import connection
from geopy.distance import geodesic
from math import floor
from config import config
cursor = connection.cursor()
# Testaan, auttaako cursorin tappaminen ja uudelleen luominen jokaisessa funktiossa
# mysql.connector.errors.DatabaseError: 2014 (HY000): Commands out of sync; you can't run this command now
# -erroriin


def dice_roll():
    dice_num = random.randint(2, 12)
    return dice_num


def get_current_pp(player_id):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    current_pp = result[0]  # queryn tulos tuplesta ulos
    return current_pp  # type(current_pp)=int


def add_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)  # int
    new_pp = current_pp + change_amount  # int
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"  # f-string koska int
    cursor.execute(query)
    return


def remove_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)
    new_pp = current_pp - change_amount
    query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"
    cursor.execute(query)
    return


def format_database_for_new_game():
    try:
        # current working dir
        cwd = os.getcwd()
        # avaa polusta script.sql, lukumuodossa, alias sql_file
        with open(cwd + "/create_game_db.sql", "r") as sql_file:
            sql_queries = sql_file.read().split(";")  # Lukee filen, splittaa ;-merkistä listaksi
        for sql_query in sql_queries:
            sql_query = sql_query.strip()  # Vedetään tyhjät (whitespacet) pois
            if sql_query:  # onko query tyhjä? -> FALSE
                cursor.execute(sql_query)
        connection.commit()  # varmistuscommit, tätä suositeltiin jossain
        return "Database formatting completed."
    except:  # Tämä on paska exception
        return ("Something went wrong with database formatting.\n"
                "Try to think of better exception rule")


def get_location(player_id):
    sql = (f"SELECT name FROM city INNER JOIN player ON city.id = player.location WHERE "
           f"player.id = '{player_id}'")  # player id tulee inttinä
    cursor.execute(sql)
    result = cursor.fetchone()
    location = result[0]  # location tuplesta ulos
    return location  # type(location)=str


def set_location(new_location, player_id):  # new location, player id tulee stringinä!
    sql = "UPDATE player SET location = '" + new_location + "' WHERE player.id = '" + player_id + "'"
    cursor.execute(sql)
    sql = "UPDATE city SET visited = 1 WHERE city.id = '" + new_location + "'"
    cursor.execute(sql)


def lock_check(player_id):  # Printer ei tarvitse tätä enää, tarvitseeko joku muu?
    sql = "SELECT lockstate FROM player"
    sql += " WHERE id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
#    cursor.close()
    lock_state = int(result[0][0])
    if lock_state == 0:
        return "Not locked"
    else:
        return lock_state


def printer(player):
    current_pp = int(player[2])
    current_location = get_location((str(player[0])))
    lock_status = int(player[3])
    print("---Player status---\n")
    print(f"Name: {player[1]}")
    print(f"Current PP: {current_pp}")
    print(f"Location: {current_location}")
    if player[4] > 0:
        print(f"Take your grandma's luggage back to her at Sysma!")
    else:
        print("Find your grandma's luggage.")
    if lock_status == 0:
        print("Lock state: not locked")
    else:
        print(f"Lock state: locked for {lock_status} turns")
    return True


def get_player_data_as_list():
    # SQL-kyselyllä kaikki player-taulusta
    sql = "SELECT * FROM player"
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


def get_round_number():
    sql = "SELECT counter FROM round_counter"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
#    cursor.close()
    return result


def add_to_round_counter():
    sql = "UPDATE round_counter SET counter = counter + 1"
    cursor.execute(sql)
#    cursor.close()


def get_city_data():
    sql = "SELECT * from city"
    cursor.execute(sql)
    all_from_city = cursor.fetchall()
#    cursor.close()
    all_data_from_city_as_list = []
    for i in range(len(all_from_city)):
        all_data_from_city_as_list.append((list(all_from_city[i])))
    return all_data_from_city_as_list


def get_ports(cities):
    port_cities = []
    for city in cities:
        if city[7] == 1:
            port_cities.append(city)
    return port_cities


def print_available_cities(travel_mode, city_list, player_id):
    if travel_mode == "fly":
        print("---Available cities where you can fly to---")
    elif travel_mode == "boat":
        print("---Available cities where you can sail to---")
    else:
        print("---Available cities where you can hitchhike to---")
    for city in city_list:
        if city[5] == 1:  # if-else tulostaa visited tai not visited riippuen kaupungin tilasta
            visited_status = "visited"
        else:
            visited_status = "not visited"
        # printti muotoituna taulukkomaiseksi, aja funktio niin näet
        print(f"{city[1]:<15}: {city[2]:^25}: {city[3]} km : cost {city[4]:^6.0f} PP {visited_status:>15}")
    print(f"You have {get_current_pp(player_id)} PP.")  # viimeiseksi tuloste pelaajan rahamäärästä


def get_cities_in_range(travel_mode, player):
    price_multiplier_dict = {
        "fly": config.get('config', 'FlyPriceMultiplier'),  # HUOM Nämä config-filestä tuodut on stringejä!
        "boat": config.get('config', 'BoatPriceMultiplier'),
        "hike": config.get('config', 'HikePriceMultiplier')
    }
    max_distance_dict = {
        "fly": config.get('config', 'MaxDistanceFly'),
        "boat": config.get('config', 'MaxDistanceBoat'),
        "hike": config.get('config', 'MaxDistanceHike')
    }
    price_multiplier = float(price_multiplier_dict[travel_mode])
    max_distance = int(max_distance_dict[travel_mode])
    player_location = player[8]
    cities = get_city_data()
    player_coords = ((cities[player[8] - 1][3]), (cities[player[8] - 1][4]))
    if travel_mode == "boat":
        cities = get_ports(cities)
    player_pp = player[2]
    cities_in_range = []
    for city in cities:
        distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
        price = distance_from_player * price_multiplier
        if city[0] != player_location and (distance_from_player <= max_distance and
                                           price <= player_pp):
            cities_in_range.append([city[0], city[1], city[2], distance_from_player, price, city[6]])
    return cities_in_range


def lock_reduce(player):
    sql = f"UPDATE player SET lockstate = lockstate -1 WHERE id = '{player[0]}'"
    cursor.execute(sql)
    print("Player lock updated.")
    return


def event_randomizer(player):

    event_multiplier = float(config.get('config', 'RandomEventChance'))
    rand_test = random.uniform(0, 1)
    # Haetaan kaikkien eventtien määrä ja kokeillaan tuleeko eventtiä vai ei
    sql = "SELECT COUNT(id) FROM random_events"
    cursor.execute(sql)
    events_sum = cursor.fetchall()
    playerid = str(player[0])
    # jos eventtiä ei tule tulostetaan allaoleva
    if rand_test > event_multiplier:
        print("No events for you this time.")
        return False
    # jos eventti tulee, haetaan arpomalla eventti kaikkien eventtien joukosta ja käsitellään sitä
    # niin että outcom_high jaetaan splitillä kahteen osaan ja outcome_lower jaetaan kahteen osaan
    # sekä tallennetaan fluff teksi muuttujaksi.
    elif rand_test < event_multiplier:
        randomized_num = random.randint(1, events_sum[0][0])
        sql = f"SELECT * FROM random_events WHERE id = {randomized_num}"
        cursor.execute(sql)
        rand_event = cursor.fetchall()
        outcome_h = rand_event[0][3].split(",")
        outcome_l = rand_event[0][4].split(",")
        fluff = rand_event[0][1]
        # kokeillaan tuleeko pelaaja ryöstetyksi menettäen kaikki pp:nsä
        # ja tyhjennetään pelaajalta kaikki pp:t
        if outcome_h[0] == "robbed":
            print(fluff)
            remove_pp(player[2], player[0])
            print(f"You have no PP.")
            if int(outcome_h[1]) > 0:
                # Tähän lockstate
                print(f"Your lockstate updates to + {outcome_h[1]}.")
                return False

            return True
        # jossei pelaajalta ryöstetä kaikkea omaisuutta ruvetaan tutkimaan erinäisiä vaihtoehtoja mitä
        # eventistä tulee
        else:
            if rand_event[0][2] == 0:
                print(fluff)
                sql = f"UPDATE player SET current_pp = current_pp {outcome_h[0]} WHERE id = '{playerid}'"
                cursor.execute(sql)
                print(f"\nYour pp updates to {outcome_h[0]}.")
                if int(outcome_h[1]) > 0:
                    sql = f"UPDATE player SET lockstate = lockstate + {outcome_h[1]} WHERE id = '{playerid}'"
                    cursor.execute(sql)
                    print(f"Your lockstate updated + {outcome_h[1]}.")
                    return False
                else:
                    return True
            # jos eventissä pitää heittää noppaa heitetään sitä pelaajan avustuksella
            # sen jälkeen testataan onko nopan heitto tarpeeksi iso roll_treshold sarakkeen määräämän arvon perusteella
            elif rand_event[0][2] > 0:
                print(fluff)
                print(f"\nYou need to roll at least {rand_event[0][2]}.")
                input("Press Enter to roll dice: ")
                roll = dice_roll()
                print(f"\nYou rolled {roll}.")
                # jos isompi tai yhtä iso, tehdään näin
                if roll >= rand_event[0][2]:
                    sql = f"UPDATE player SET current_pp = current_pp {outcome_h[0]} WHERE id = '{playerid}'"
                    cursor.execute(sql)
                    print(f"Your pp updates {outcome_h[0]}.")
                    if int(outcome_h[1]) > 0:
                        sql = f"UPDATE player SET lockstate = lockstate + {outcome_h[1]} WHERE id = '{playerid}'"
                        cursor.execute(sql)
                        print(f"Your lockstate updates + {outcome_h[1]}.")
                        return False
                    else:
                        return True
                # jos pienempi tehdään näin
                elif roll < rand_event[0][2]:
                    sql = f"UPDATE player SET current_pp = current_pp {str(outcome_l[0])} WHERE id = '{playerid}'"
                    cursor.execute(sql)
                    print(f"Your pp updates {outcome_l[1]}.")
                    if int(outcome_l[1]) > 0:
                        sql = f"UPDATE player SET lockstate = lockstate + {str(outcome_l[1])} WHERE id = '{playerid}'"
                        cursor.execute(sql)
                        print(f"Your lockstate updates + {outcome_l[1]}.")
                        return False
                    else:
                        return True
                # jos suurempi tehdään näin
                elif roll > rand_event[0][2]:
                    sql = f"UPDATE player SET current_pp = current_pp {str(outcome_h[0])} WHERE id = '{playerid}'"
                    cursor.execute(sql)
                    print(f"Your pp updates {outcome_h[0]}.")
                    if int(outcome_h[1]) > 0:
                        sql = f"UPDATE player SET lockstate = + {str(outcome_h[1])} WHERE id = '{playerid}'"
                        cursor.execute(sql)
                        print(f"Your lockstate updates + {outcome_h[1]}.")
                        return False
                    else:
                        return True


def item_randomizer():
    item_id_roll = str(random.randint(1, 169))
    sql = f"SELECT item_description, value FROM random_items WHERE id='" + item_id_roll + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    item_name, item_value = result[0]  # tuple unpacker
    return item_name, int(item_value)  # Nämä ovat n. 95% pelkkää arvotonta paskaa

def determine_travel_lock_amount(distance, travel_type):
    if travel_type == "hike":
        if distance <= 300:
            travel_lock_amount = 1
            travel_lock_amount += random.randint(0, 2)
        if distance <= 600:
            travel_lock_amount = 1
            travel_lock_amount += random.randint(2, 3)
        if distance <= 1000:
            travel_lock_amount = 2
            travel_lock_amount += random.randint(2, 3)
    elif travel_type == "sail":
        if distance <= 300:
            travel_lock_amount = random.randint(1, 2)
        if distance <= 600:
            travel_lock_amount = 1
            travel_lock_amount += random.randint(1, 2)
        if distance <= 1000:
            travel_lock_amount = 1
            travel_lock_amount += random.randint(2, 3)
    return travel_lock_amount

def set_lockstate(distance, player_id, counter, travel_type):
    if distance != 0:
        lock_amount = determine_travel_lock_amount(distance, travel_type)
    if counter != 0:
        lock_amount = counter
        print(lock_amount)
    print("lock amount: " + str(lock_amount))
    query = f"UPDATE player SET lockstate = '{lock_amount}' WHERE id = '{player_id}'"
    cursor.execute(query)
    return


def get_not_visited_city_ids():
    sql = "SELECT id FROM city WHERE visited = '0'"
    cursor.execute(sql)
    cities = cursor.fetchall()
    result = []
    for city in cities:
        result.append(city[0])
    return result


def generate_main_bag():
    not_visited_cities = get_not_visited_city_ids()
    random_city = random.choice(not_visited_cities)
    sql = f"UPDATE city SET bag_city = 1 WHERE id = '{random_city}'"
    cursor.execute(sql)


def generate_additional_bags():
    not_visited_cities = get_not_visited_city_ids()
    playercount = len(get_player_data_as_list())
    random_cities = random.sample(not_visited_cities, playercount)
    for city_id in random_cities:
        sql = f"UPDATE city SET bag_city = 1 WHERE id = '{city_id}'"
        cursor.execute(sql)

