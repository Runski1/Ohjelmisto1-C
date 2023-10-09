import random
import os
from db_connection import connection
import mysql.connector
from geopy.distance import geodesic
from math import floor
from config import config
from prize_found_event import end_game_email
from colorama import Fore
cursor = connection.cursor()

# Testaan, auttaako cursorin tappaminen ja uudelleen luominen jokaisessa funktiossa
# mysql.connector.errors.DatabaseError: 2014 (HY000): Commands out of sync; you can't run this command now
# -erroriin


def dice_roll():
    input("Press Enter to roll dice: ")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2
    print(f"You rolled: [{dice1}] and [{dice2}]")
    return dice_total


def get_current_pp(player_id):
    query = f"SELECT current_pp FROM player WHERE id='{player_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    current_pp = result[0]  # queryn tulos tuplesta ulos
    return current_pp  # type(current_pp)=int


def add_pp(change_amount, player_id):
    current_pp = get_current_pp(player_id)  # int
    new_pp = current_pp + change_amount  # int
    if new_pp > 0:  # tarkistus ettei eventti voi viedä poletteja nollan alapuolelle
        query = f"UPDATE player SET current_pp = '{new_pp}' WHERE id='{player_id}'"  # f-string koska int
        cursor.execute(query)

    else:
        sql = f"UPDATE player SET current_pp = 0 WHERE id = '{player_id}'"
        cursor.execute(sql)
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
    except mysql.connector.Error:  # Tämä ei ole enää paska exception
        return "Something went wrong with database formatting."


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


def set_searched(location):
    sql = f"UPDATE city SET visited = 1 WHERE city.id = '{location}'"
    cursor.execute(sql)


def lock_check(player_id):  # Printer ei tarvitse tätä enää, tarvitseeko joku muu?
    sql = "SELECT lockstate FROM player"
    sql += " WHERE id = '" + player_id + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    #    cursor.close()
    lock_state = int(result[0][0])
    return lock_state


def printer(player):
    current_pp = int(player[2])
    current_location = get_location((str(player[0])))
    lock_status = int(player[3])
    print("---Player status---\n")
    print(f"Name: {player[1]}")
    print(f"Current PP: {current_pp}")
    if player[3] == 0:
        print(f"Location: {current_location}")
    else:
        print(f"You're travelling to {current_location}.")
    if player[4] > 0:
        print(f"Take your grandma's luggage back to her at Sysma!")
    else:
        print("Find your grandma's luggage.")
    if lock_status == 0:
        print("You are free to do actions.")
    elif player[7] == 0:
        print(f"You are frozen and cannot do actions for {lock_status} turns.")
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
            visited_status = "searched"
        else:
            visited_status = "not searched"
        # printti muotoituna taulukkomaiseksi, aja funktio niin näet
        if visited_status == "searched":
            print(f"{Fore.RED}{city[1]:<15}{Fore.GREEN}: {city[2]:^25}: {Fore.BLUE}{city[3]:^7} km{Fore.GREEN} : cost "
                  f"{Fore.BLUE}{city[4]:^6.0f} EP {Fore.RED}{visited_status:>15}{Fore.RESET}")
        else:
            print(f"{Fore.RED}{city[1]:<15}{Fore.GREEN}: {city[2]:^25}: {Fore.BLUE}{city[3]:^7} km{Fore.GREEN} : cost "
                  f"{Fore.BLUE}{city[4]:^6.0f} EP {Fore.GREEN}{visited_status:>15}{Fore.RESET}")
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
        if city[0] != player_location and distance_from_player <= max_distance and price <= player_pp:
            cities_in_range.append([city[0], city[1], city[2], distance_from_player, price, city[6]])
    return cities_in_range


def lock_reduce(player):
    if int(player[7]) > 0:
        print(f"You need to roll {player[7]} more to reach your destination.")
        roll = dice_roll()
        sql = f"UPDATE player SET total_dice = total_dice - {roll} WHERE id = '{player[0]}'"
        if player[7] - roll > 0:
            print(f"You need to roll {player[7] -  roll} more next round.")
        else:
            print("You reached your destination! You can do actions next turn.")
            cursor.execute(sql)
            sql = f"UPDATE player SET lockstate = '0' WHERE id = '{player[0]}'"
            cursor.execute(sql)
    else:
        sql = f"UPDATE player SET lockstate = lockstate -1 WHERE id = '{player[0]}'"
        print("Player lock updated.")
    cursor.execute(sql)
    return


def event_randomizer(player):
    event_multiplier = float(config.get('config', 'RandomEventChance'))
    rand_test = random.uniform(0, 1)
    # Haetaan kaikkien eventtien määrä ja kokeillaan tuleeko eventtiä vai ei
    sql = "SELECT COUNT(id) FROM random_events"
    cursor.execute(sql)
    events_sum = cursor.fetchall()
    playerid = player[0]
    # jos eventtiä ei tule tulostetaan allaoleva
    if rand_test > event_multiplier:
        # print("No events for you this time.")
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
            input("<Press ENTER to continue>")
            remove_pp(player[2], player[0])
            print(f"Your EP is gone.")
            if int(outcome_h[1]) > 0:
                set_lockstate(0, player[0], outcome_h[1], "diggoo")
                print(f"You cannot do actions for {outcome_h[1]} turns.")
                return False
            else:
                return True
        # jossei pelaajalta ryöstetä kaikkea omaisuutta ruvetaan tutkimaan erinäisiä vaihtoehtoja mitä
        # eventistä tulee
        else:
            # jos eventissä pitää heittää noppaa heitetään sitä pelaajan avustuksella
            # sen jälkeen testataan onko nopan heitto tarpeeksi iso roll_treshold sarakkeen määräämän arvon perusteella
            if rand_event[0][2] >= 0:
                print(fluff)
                input("<Press ENTER to continue>")
            roll = random.randint(2, 12)
            if rand_event[0][2] > 0:
                print(f"\nYou need to roll at least {rand_event[0][2]}.")
                roll = dice_roll()
            # jos isompi tai yhtä iso, tehdään näin
            if roll >= rand_event[0][2]:
                add_pp(int(outcome_h[0]), int(playerid))
                print(f"Your EP changes {outcome_h[0]}.")
                if int(outcome_h[1]) > 0:
                    set_lockstate(0, playerid, outcome_h[1], "diggoo")
                    print(f"You are frozen for {outcome_h[1]} turns.")
                    # Pelaaja voi ylikirjoittaa tämän lockin heittämällä hitchhike-noppaa
                    return False
                else:
                    return True
            # jos pienempi tehdään näin
            elif roll < rand_event[0][2]:
                add_pp(int(outcome_l[0]), int(playerid))  # perkeleen duplicatet, en äkkiseltään keksi miten välttyisi
                print(f"Your EP changes {outcome_l[0]}.")
                if int(outcome_l[1]) > 0:
                    set_lockstate(0, playerid, outcome_l[1], "diggoo")
                    print(f"You are frozen for {outcome_l[1]} turns.")
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


def determine_travel_lock_amount(distance, travel_type, player_id):
    if travel_type == "hike":
        travel_lock_amount = 999
        required_dice = int(distance) * float(config.get('config', 'HikeDistanceMultiplier'))
        sql = f"UPDATE player SET total_dice = '{required_dice}' WHERE id = {int(player_id)}"
        cursor.execute(sql)
    else:  # travel_type == "sail":
        travel_lock_amount = int(floor(int(distance) * float(config.get('config', 'BoatDistanceMultiplier'))))

    return travel_lock_amount


def set_lockstate(distance, player_id, counter, travel_type):
    query = f"SELECT lockstate FROM player WHERE id = '{player_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    lock_amount = result[0]
    if int(distance) != 0:
        lock_amount = determine_travel_lock_amount(distance, travel_type, player_id)
    if counter != 0:
        lock_amount = int(lock_amount) + int(counter)
    # print("lock amount: " + str(lock_amount))
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
    player_count = len(get_player_data_as_list())
    random_cities = random.sample(not_visited_cities, player_count - 1)
    for city_id in random_cities:
        sql = f"UPDATE city SET bag_city = 1 WHERE id = '{city_id}'"
        cursor.execute(sql)


def check_if_in_port(player):
    query = f"SELECT id FROM city WHERE port_city = '1'"
    cursor.execute(query)
    result = cursor.fetchall()
    lista = []
    for city in result:
        lista.append(city[0])
    if player[8] in lista:
        return True
    else:
        return False


def bag_found(player):
    query = f"SELECT COUNT(*) FROM player WHERE prizeholder = '1'"
    cursor.execute(query)
    bagman = cursor.fetchone()
    query = f"UPDATE player SET prizeholder = 1 WHERE id ='{player[0]}'"
    cursor.execute(query)
    query = f"UPDATE city SET bag_city = 0 WHERE id ='{player[8]}'"
    cursor.execute(query)
    if bagman[0] == 0:
        generate_additional_bags()
        end_game_email()


def is_city_bag_city(player):
    sql = (f"SELECT bag_city FROM city inner join player on "
           f"city.id = player.location and player.screen_name = '{player[1]}'")
    cursor.execute(sql)
    result = cursor.fetchall()
    if result[0][0] == 1:
        return True
    else:
        return False


def print_city_status(player):
    cities = get_city_data()
    player_coords = ((cities[player[8] - 1][3]), (cities[player[8] - 1][4]))
    for city in cities:
        distance_from_player = floor(geodesic(player_coords, ((city[3]), (city[4]))).km)
        city.append(distance_from_player)
    sorted_city = sorted(cities, key=lambda x: x[8])
    for city in sorted_city:
        if city[6] == 1:
            visited_status = "searched"
        else:
            visited_status = "not searched"
        # printti muotoituna taulukkomaiseksi, aja funktio niin näet
        if visited_status == "searched":
            print(f"{Fore.RED}{city[1]:<15}{Fore.GREEN}: {city[2]:^25}: {Fore.BLUE}{city[8]:^7} km{Fore.GREEN} : "
                  f"{Fore.RED}{visited_status:>15}{Fore.RESET}")
        else:
            print(f"{Fore.RED}{city[1]:<15}{Fore.GREEN}: {city[2]:^25}: {Fore.BLUE}{city[8]:^7} km{Fore.GREEN} : "
                  f"{visited_status:>15}{Fore.RESET}")


if __name__ == "__main__":
    pass
