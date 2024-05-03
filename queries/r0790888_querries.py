GET_DELIVERY_RECORDS_QUERY = "SELECT * FROM delivery WHERE dilivery_id = ?"
GET_LOCATION_DELIVERY_RECORDS_QUERY = "SLECT * FROM delivery where location_name = ?"
INSERT_DELIVERY_RECORD_QUERY = "INSERT INTO delivery (delivery_id, location_name, location_address, delivery_date, product_name, product_count)"