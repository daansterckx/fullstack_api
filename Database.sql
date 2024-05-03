DROP DATABASE if exists brewery_database;
CREATE DATABASE brewery_database;

USE brewery_database;

CREATE TABLE Beers (
    beer_id INT AUTO_INCREMENT PRIMARY KEY,
    beer_name VARCHAR(255) NOT NULL,
    price float NOT NULL
);
CREATE TABLE Tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(255) NOT NULL,
    description TEXT,
    tour_date DATETIME NOT NULL,
    max_attendees INT NOT NULL
);