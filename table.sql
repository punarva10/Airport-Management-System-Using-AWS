CREATE TABLE IF NOT EXISTS airlines_type
(
at_id int(11) NOT NULL, 
at_name varchar(255) NOT NULL,
PRIMARY KEY(at_id)
);

CREATE TABLE IF NOT EXISTS route(
route_id int (11) NOT NULL, 
route_from_city varchar (255) NOT NULL,
route_to_city varchar (255) NOT NULL, 
route_economy_fare varchar (255) NOT NULL, 
route_business_fare varchar (255) NOT NULL,
PRIMARY KEY(route_id)
);

CREATE TABLE IF NOT EXISTS airlines (
airlines_id int(11) NOT NULL, 
airlines_at_id int(11) NOT NULL, 
r_id int(11) NOT NULL, 
airlines_name varchar (255) NOT NULL, 
airlines_from varchar (255) NOT NULL,
airlines_to varchar (255) NOT NULL,
airlines_total_distance varchar (255) NOT NULL,
airlines_travel_time varchar (255) NOT NULL, 
airlines_departure varchar (255) NOT NULL, 
airlines_arrival varchar (255) NOT NULL, 
fare float(11)
PRIMARY KEY(airlines_id),
FOREIGN KEY (airlines_at_id) REFERENCES airlines_type(at_id),
FOREIGN KEY (r_id) REFERENCES route(route_id)
);

CREATE TABLE IF NOT EXISTS passenger(
passenger_id int (11) NOT NULL, 
passenger_type varchar (255) NOT NULL, 
passenger_name varchar (255) NOT NULL, 
passenger_gender varchar (255) NOT NULL, 
passenger_age varchar (255) NOT NULL,
passenger_seat_no varchar (255) NOT NULL,
PRIMARY KEY(passenger_id)
);

CREATE TABLE IF NOT EXISTS city(
city_id int(10) UNSIGNED NOT NULL,
city_name varchar (45) NOT NULL,
PRIMARY KEY(city_id)
);

CREATE TABLE IF NOT EXISTS booking(
booking_id int (11) NOT NULL,
b_airlines_id int(11) NOT NULL,
p_id int(11) NOT NULL,
source_id int(10) UNSIGNED NOT NULL,
dest_id int(10) UNSIGNED NOT NULL,
booking_date varchar (255) NOT NULL,
booking_total_fare float(11), 
booking_journey_date varchar (255) NOT NULL, 
booking_seat_type varchar (255) NOT NULL, 
booking_status varchar (255) NOT NULL DEFAULT 0,
PRIMARY KEY(booking_id),
FOREIGN KEY (b_airlines_id) REFERENCES airlines(airlines_id),
FOREIGN KEY (source_id) REFERENCES city(city_id),
FOREIGN KEY (dest_id) REFERENCES city(city_id),
FOREIGN KEY (p_id) REFERENCES passenger(passenger_id)
);






