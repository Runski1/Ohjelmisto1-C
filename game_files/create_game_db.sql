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
    port_city     tinyint(1)           null
);

create table game
(
    id            int auto_increment
        primary key,
    name          varchar(255)  null,
    round_counter int default 0 null,
    bag_city      int           null,
    visited       varchar(255)  null
);


create table player
(
    id             int auto_increment
        primary key,
    screen_name    varchar(25)             null,
    current_pp     int        default 2000 null,
    lockstate      int        default 0    null,
    prizeholder    tinyint(1) default 0    not null,
    total_dice     int        default 0    null,
    location       int        default 16   not null,
    game           int                     null,
    constraint player__id_fk
        foreign key (game) references game (id),
    constraint player_city__fk
        foreign key (location) references city (id)
);



create table random_items
(
    id                  int auto_increment
    primary key,
    item_description    varchar(255)  not null,
    value               float not null
);

INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (1, 'Tirana', 'Albania', 41.4147, 19.7206, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (2, 'Vienna', 'Austria', 48.1103, 16.5697, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (3, 'Sarajevo', 'Bosnia and Herzegovina', 43.8246, 18.3315, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (4, 'Brussels', 'Belgium', 50.9014, 4.48444, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (5, 'Sofia', 'Bulgaria', 42.6967, 23.4114, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (6, 'Minsk', 'Belarus', 53.8881, 28.04, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (7, 'Zurich', 'Switzerland', 47.4581, 8.54806, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (8, 'Prague', 'Czech Republic', 50.1008, 14.26, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (9, 'Berlin', 'Germany', 52.3514, 13.4939, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (10, 'Copenhagen', 'Denmark', 55.6179, 12.656, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (11, 'Algiers', 'Algeria', 36.691, 3.21541, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (12, 'Tallinn', 'Estonia', 59.4133, 24.8328, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (13, 'Cairo', 'Egypt', 30.1219, 31.4056, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (14, 'Gran-Canaria', 'Canary islands', 27.9319, -15.3866, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (15, 'Madrid', 'Spain', 40.4719, -3.56264, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (16, 'Helsinki', 'Finland', 60.3172, 24.9633, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (17, 'Paris', 'France', 49.0128, 2.55, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (18, 'London', 'United Kingdom', 51.4706, -0.461941, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (19, 'Mestia', 'Georgia', 43.0536, 42.749, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (20, 'Athens', 'Greece', 37.9364, 23.9445, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (21, 'Zagreb', 'Croatia', 45.7429, 16.0688, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (22, 'Budapest', 'Hungary', 47.4298, 19.2611, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (23, 'Dublin', 'Ireland', 53.4213, -6.27007, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (24, 'Reykjavik', 'Iceland', 63.985, -22.6056, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (25, 'Rome', 'Italy', 41.8045, 12.252, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (26, 'Vilnius', 'Lithuania', 54.6341, 25.2858, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (27, 'Luxembourg', 'Luxembourg', 49.6233, 6.20444, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (28, 'Riga', 'Latvia', 56.9236, 23.9711, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (29, 'Tripoli', 'Libya', 32.6635, 13.159, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (30, 'Casablanca', 'Morocco', 33.3675, -7.58997, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (31, 'Chisinau', 'Moldova', 46.9277, 28.931, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (32, 'Podgorica', 'Montenegro', 42.3594, 19.2519, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (33, 'Skopje', 'North Macedonia', 41.9616, 21.6214, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (34, 'Valletta', 'Malta', 35.8575, 14.4775, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (35, 'Amsterdam', 'Netherlands', 52.3086, 4.76389, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (36, 'Oslo', 'Norway', 60.1939, 11.1004, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (37, 'Warsaw', 'Poland', 52.1657, 20.9671, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (38, 'Lisbon', 'Portugal', 38.7813, -9.13592, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (39, 'Bucharest', 'Romania', 44.5711, 26.085, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (40, 'Belgrade', 'Serbia', 44.8184, 20.3091, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (41, 'Stockholm', 'Sweden', 59.6519, 17.9186, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (42, 'Ljubljana', 'Slovenia', 46.2237, 14.4576, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (43, 'Bratislava', 'Slovakia', 48.1702, 17.2127, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (44, 'Domagnano', 'San Marino', 43.9489, 12.5114, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (45, 'Tunis', 'Tunisia', 36.851, 10.2272, 1);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (46, 'Ankara', 'Turkey', 40.1281, 32.9951, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (47, 'Kiev', 'Ukraine', 50.345, 30.8947, 0);
INSERT INTO kadonnut_testamentti.city (id, name, country, latitude_deg, longitude_deg, port_city) VALUES (48, 'Prishtina', 'Kosovo', 42.5728, 21.0358, 0);


INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (1, 'one dirty sock', 0);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (7, 'Inflatable Necktie', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (9, 'Funny Hat with Propeller', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (15, 'Rubber Chicken', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (24, 'Silly String', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (28, 'Fake Mustache', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (30, 'Rubber Duck', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (32, 'Fake Passport with Silly Name', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (35, 'Silly String Confetti', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (37, 'Funny Face Mask', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (40, 'Silly Straw', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (42, 'Funny Boarding Pass', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (45, 'Fake Airport Security Badge', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (47, 'Silly String Silly String', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (57, 'Sunglasses Case', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (61, 'Razor', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (67, 'Tissues', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (69, 'Hand Sanitizer', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (70, 'Wet Wipes', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (74, 'Hair Gel', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (75, 'Face Mask', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (80, 'Shoe Polish Kit', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (81, 'Stain Remover Pen', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (82, 'Stylus Pen', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (84, 'Lint Roller', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (87, 'Clock', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (90, 'Travel Socks', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (92, 'Travel Towel', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (93, 'Umbrella', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (95, 'Gloves', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (99, 'Belt', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (100, 'Travel Pouch', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (106, 'Toothbrush', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (112, 'Razor', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (113, 'Shaving Cream', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (120, 'Scrub Brush', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (124, 'Clothesline', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (131, 'Packing Cubes', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (133, 'Neck Pillow', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (140, 'Playing Cards', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (143, 'Sudoku Book', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (148, 'Watercolor Set', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (154, 'Golf Putter', 10);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (2, 'Luggage Tag', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (17, 'Sleeping Mask', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (22, 'Funny T-Shirt', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (29, 'Mini Fan', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (33, 'Travel-sized Playing Cards', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (39, 'Sunglasses with Built-in Straw', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (43, 'Travel-sized Kazoo', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (46, 'Travel-sized Magic 8-Ball', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (48, 'Travel-sized Slinky', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (50, 'Travel-sized Rubber Band Shooter', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (63, 'Dental Floss', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (158, 'Travel Volleyball', 30);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (18, 'Funny Socks', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (34, 'Airplane-shaped Bottle Opener', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (41, 'Travel-sized Bubbles', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (96, 'Scarf', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (103, 'Pillowcase', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (114, 'Aftershave', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (121, 'Laundry Bag', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (123, 'Clothespins', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (125, 'Sewing Kit', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (128, 'Trash Bags', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (136, 'Earbuds', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (144, 'Crossword Puzzle Book', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (147, 'Colored Pencils', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (152, 'Jump Rope', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (156, 'Travel Soccer Ball', 50);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (11, 'Socks with Toes', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (31, 'Funny Travel Mug', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (36, 'Travel-sized Jenga', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (44, 'Chia Pet Travel Companion', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (66, 'Mouthwash', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (77, 'Luggage Scale', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (108, 'Hairdryer', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (115, 'Cologne', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (117, 'Lotion', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (130, 'Compression Bags', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (137, 'Headphones', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (139, 'Multi-tool', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (142, 'Travel Backgammon', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (151, 'Resistance Bands', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (155, 'Travel Frisbee', 70);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (49, 'Funny Travel-themed Stickers', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (64, 'Nail Clippers', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (71, 'Lip Balm', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (73, 'Sewing Kit', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (85, 'Folding Mirror', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (91, 'Travel Slippers', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (104, 'Eye Mask', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (105, 'Ear Plugs', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (107, 'Comb', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (119, 'Bath Sponge', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (126, 'Safety Pins', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (127, 'Ziplock Bags', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (129, 'Clothes Folder', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (132, 'Shoe Bags', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (134, 'Eye Pillow', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (135, 'Sleep Mask', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (145, ' Word Search Book', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (146, 'Coloring Book', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (149, 'Sketchbook', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (159, 'Beach Ball', 76);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (83, 'Collapsible Cup', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (88, 'Travel Pillow', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (94, 'Hat', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (101, 'Organizer', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (109, 'Straightener', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (116, 'Perfume', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (118, 'Body Wash', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (122, 'Laundry Detergent', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (141, 'Chess Set', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (150, 'Yoga Mat', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (153, 'Tennis Racket', 90);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (10, 'Travel Blanket', 100);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (16, 'Laptop Charger', 100);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (12, 'Hand Sanitizer', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (21, 'Invisible Ink Pen', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (23, 'Travel Sudoku Book', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (25, 'Frisbee', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (27, 'Travel-sized Umbrella', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (38, 'Travel-sized Connect Four', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (52, 'Toothpaste', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (62, 'Hairbrush', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (68, 'Soap', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (79, 'Umbrella', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (86, 'Mug', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (89, 'Travel Blanket', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (110, 'Curling Iron', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (111, 'Flat Iron', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (138, 'Travel Power Strip', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (157, 'Football', 110);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (3, 'Passport', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (5, 'Neck Pillow', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (8, 'Travel Pillow', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (19, 'Travel Guidebook', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (26, 'Travel Scrabble', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (53, 'Reusable Water Bottle', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (55, 'Shampoo', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (58, 'Deodorant', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (60, 'Sunscreen', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (72, 'First Aid Kit', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (76, 'Insect Repellent', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (78, 'Travel Iron', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (97, 'Backpack', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (98, 'Wallet', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (102, 'Adaptor', 150);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (4, 'Sunglasses', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (13, 'Travel Journal', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (14, 'Snorkel and Flippers', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (20, 'Binoculars', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (54, 'E-reader', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (59, 'Body Lotion', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (65, 'Portable Power Bank', 190);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (6, 'Noise-Canceling Headphones', 340);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (56, 'Spare Phone Charger', 435);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (162, 'Platinum Toilet Paper Roll', 650);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (167, 'Jet-Powered Skateboard', 650);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (166, 'The Laughter Generator 9000', 700);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (163, 'Rocket-Powered Slippers', 770);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (160, 'Golden Banana Phone', 800);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (164, 'Infinite Chocolate Bar', 980);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (51, 'Laughing Gas Inhaler', 1000);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (161, 'Diamond-Studded Umbrella', 1000);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (165, 'Eternal Fortune Cookie', 1100);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (169, 'Unicorn-Powered Car', 1200);
INSERT INTO kadonnut_testamentti.random_items (id, item_description, value) VALUES (168, 'Time-Traveling Toaster', 2000);

INSERT INTO kadonnut_testamentti.game (id, name, round_counter, bag_city, visited) VALUES (1,'test', 0, 32, '["16"]');
INSERT INTO kadonnut_testamentti.player (id, screen_name, current_pp, lockstate, prizeholder, total_dice, location, game) VALUES (1, 'Alan', 2000, 0, 0, 0, 16, 1);
INSERT INTO kadonnut_testamentti.player (id, screen_name, current_pp, lockstate, prizeholder, total_dice, location, game) VALUES (2, 'Turing', 2000, 0, 0, 0, 16, 1);