GET_ALL_BEERS_QUERY = "SELECT beer_id AS id, beer_name AS name, price FROM Beers;"
GET_BEER_BY_ID_QUERY = "SELECT beer_id AS id, beer_name AS name, price FROM Beers WHERE beer_id = %s;"
INSERT_BEER_QUERY = "INSERT INTO Beers (beer_name, price) VALUES (%s, %s);"

