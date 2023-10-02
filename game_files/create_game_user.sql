DROP USER IF EXISTS 'game'@'localhost';
CREATE USER 'game'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON kadonnut_testamentti.* TO 'game'@'localhost';
FLUSH PRIVILEGES;
