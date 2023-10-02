DROP DATABASE IF EXISTS kadonnut_testamentti;
CREATE DATABASE kadonnut_testamentti;
USE kadonnut_testamentti;

create table city
(
    id            int auto_increment
        primary key,
    name          varchar(50)          not null,
    country       varchar(50)          null,
    latitude_deg  float                null,
    longitude_deg float                null,
    bag_city      tinyint(1) default 0 null,
    visited       tinyint(1) default 0 null,
    port_city     tinyint(1)           null,
    constraint name
        unique (name)
);

create table player
(
    id             int auto_increment
        primary key,
    screen_name    varchar(25)          null,
    current_pp     int        default 2000 null,
    lockstate      int        default 0 null,
    prizeholder    tinyint(1) default 0 not null,
    real_prize     tinyint(1) default 0 not null,
    event_eligible tinyint(1) default 0 null,
    total_dice     int        default 0 null,
    location       int        default 16 not null,
    constraint player_city__fk
        foreign key (location) references city (id)
);

create table random_events
(
    id             int auto_increment
        primary key,
    fluff           varchar(255) null,
    roll_treshold  int          null,
    outcome_higher varchar(255) null,
    outcome_lower  varchar(255) null,
    location       int          null
);

create table location_tied
(
    city_id         int not null,
    random_event_id int not null,
    primary key (city_id, random_event_id),
    constraint location_tied_city__fk
        foreign key (city_id) references city (id),
    constraint location_tied_random_events__fk
        foreign key (random_event_id) references random_events (id)
);

create table round_counter
(
    counter int default 1 not null
);

INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (1, 'Tirana', 'Albania', 41.4147, 19.7206, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (2, 'Vienna', 'Austria', 48.1103, 16.5697, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (3, 'Sarajevo', 'Bosnia and Herzegovina', 43.8246, 18.3315, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (4, 'Brussels', 'Belgium', 50.9014, 4.48444, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (5, 'Sofia', 'Bulgaria', 42.6967, 23.4114, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (6, 'Minsk', 'Belarus', 53.8881, 28.04, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (7, 'Zurich', 'Switzerland', 47.4581, 8.54806, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (8, 'Prague', 'Czech Republic', 50.1008, 14.26, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (9, 'Berlin', 'Germany', 52.3514, 13.4939, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (10, 'Copenhagen', 'Denmark', 55.6179, 12.656, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (11, 'Algiers', 'Algeria', 36.691, 3.21541, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (12, 'Tallinn', 'Estonia', 59.4133, 24.8328, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (13, 'Cairo', 'Egypt', 30.1219, 31.4056, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (14, 'Gran Canaria Island', 'Canary islands', 27.9319, -15.3866, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (15, 'Madrid', 'Spain', 40.4719, -3.56264, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (16, 'Helsinki', 'Finland', 60.3172, 24.9633, 0, 1, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (17, 'Paris', 'France', 49.0128, 2.55, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (18, 'London', 'United Kingdom', 51.4706, -0.461941, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (19, 'Mestia', 'Georgia', 43.0536, 42.749, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (20, 'Athens', 'Greece', 37.9364, 23.9445, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (21, 'Zagreb', 'Croatia', 45.7429, 16.0688, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (22, 'Budapest', 'Hungary', 47.4298, 19.2611, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (23, 'Dublin', 'Ireland', 53.4213, -6.27007, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (24, 'Reykjavík', 'Iceland', 63.985, -22.6056, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (25, 'Rome', 'Italy', 41.8045, 12.252, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (26, 'Vilnius', 'Lithuania', 54.6341, 25.2858, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (27, 'Luxembourg', 'Luxembourg', 49.6233, 6.20444, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (28, 'Riga', 'Latvia', 56.9236, 23.9711, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (29, 'Tripoli', 'Libya', 32.6635, 13.159, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (30, 'Casablanca', 'Morocco', 33.3675, -7.58997, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (31, 'Chişinău', 'Moldova', 46.9277, 28.931, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (32, 'Podgorica', 'Montenegro', 42.3594, 19.2519, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (33, 'Skopje', 'North Macedonia', 41.9616, 21.6214, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (34, 'Valletta', 'Malta', 35.8575, 14.4775, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (35, 'Amsterdam', 'Netherlands', 52.3086, 4.76389, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (36, 'Oslo', 'Norway', 60.1939, 11.1004, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (37, 'Warsaw', 'Poland', 52.1657, 20.9671, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (38, 'Lisbon', 'Portugal', 38.7813, -9.13592, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (39, 'Bucharest', 'Romania', 44.5711, 26.085, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (40, 'Belgrade', 'Serbia', 44.8184, 20.3091, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (41, 'Stockholm', 'Sweden', 59.6519, 17.9186, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (42, 'Ljubljana', 'Slovenia', 46.2237, 14.4576, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (43, 'Bratislava', 'Slovakia', 48.1702, 17.2127, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (44, 'Domagnano', 'San Marino', 43.9489, 12.5114, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (45, 'Tunis', 'Tunisia', 36.851, 10.2272, 0, 0, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (46, 'Ankara', 'Turkey', 40.1281, 32.9951, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (47, 'Kiev', 'Ukraine', 50.345, 30.8947, 0, 0, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, bag_city, visited, port_city) VALUES (48, 'Prishtina', 'Kosovo', 42.5728, 21.0358, 0, 0, 0);
INSERT INTO kadonnut_testamentti.round_counter (counter) VALUES ('1');

INSERT INTO kadonnut_testamentti.random_events (fluff, roll_treshold, outcome_higher, outcome_lower) VALUES ('Misguided GPS: Your GPS leads you on a wild goose chase through narrow European streets. Roll over 7 to catch goose and get 200pp or lose 200 pp.', 7, 'You caught the pesky goose, get rewarded 200pp', 'Pesky goose got away, lose 200pp');
INSERT INTO kadonnut_testamentti.random_events (fluff) VALUES ('Street Performer Showdown: You challenge a talented street performer to a dance-off and impress the crowd. Gain 800 pp for your epic dance moves.');
INSERT INTO kadonnut_testamentti.random_events (fluff) VALUES ('Pickpocket Prank: You catch a pickpocket in the act and manage to retrieve your wallet, but not before they take a few euros. Lose 150pp for the experience.');
INSERT INTO kadonnut_testamentti.random_events (fluff) VALUES ('Airport Food Challenge: You participate in a competitive eating contest at the airport food court and emerge victorious. Gain 750 pp for your gastronomic achievement.');
INSERT INTO kadonnut_testamentti.random_events (fluff, roll_treshold, outcome_higher, outcome_lower) VALUES ('Lucky Penny Find: You spot a shiny penny on the airport floor. Roll a dice. On 2-8, its just a regular penny, and you gain 200pp. On 9-12 roll, it turns out to be a valuable collectors coin, and you gain 1000pp.', 9, 'You rolled over 9, rewarded 1000pp', 'You rolled under 9, penny was only worth 200pp');