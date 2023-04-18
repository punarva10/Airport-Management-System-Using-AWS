-- Inserting values into airlines_type table
INSERT INTO airlines_type VALUES (001, "Commercial");
INSERT INTO airlines_type VALUES (002, "Business Jets");
INSERT INTO airlines_type VALUES (003, "Cargo");
INSERT INTO airlines_type VALUES (004, "Private Plane");
INSERT INTO airlines_type VALUES (005, "Sailplanes");
INSERT INTO airlines_type VALUES (006, "Sport Planes");

-- Inserting values into route table
INSERT INTO route VALUES (111, "Delhi", "Bangalore", "₹5500","₹10000");
INSERT INTO route VALUES (112, "Bangalore", "Mangalore", "₹1500","₹3000");
INSERT INTO route VALUES (113, "Chennai", "Kolkata", "₹5000","₹9000");
INSERT INTO route VALUES (114, "Mumbai", "Bangalore", "₹3500","5500");
INSERT INTO route VALUES (115, "Singapore", "Bangalore", "₹14000","20000");
INSERT INTO route VALUES (116, "Singapore", "Kolkata", "₹14500","20500");
INSERT INTO route VALUES (117, "Mangalore", "Chennai", "₹2000","3000");
INSERT INTO route VALUES (118, "Mangalore", "Mumbai", "₹1000","2000");
INSERT INTO route VALUES (119, "Bangalore", "Mumbai", "₹2200","4000");
INSERT INTO route VALUES (120, "Bangalore", "Delhi", "₹6500","9000");
INSERT INTO route VALUES (123, "Mumbai", "Ranchi", "₹3500","4500");
INSERT INTO route VALUES (121, "Delhi", "Singapore", "₹7500","9500");
INSERT INTO route VALUES (122, "Mumbai", "Mangalore", "₹1550","2200");

-- Inserting values into airlines table
INSERT INTO airlines VALUES (5000, 001, 111, "Vistara","Delhi","Bangalore", "2175 KM", "2hrs 45mins","02:00","04:45",4500);
INSERT INTO airlines VALUES (5001, 002, 115, "Singapore Airlines","Singapore", "Bangalore", "3170 KM", "4hrs 15mins", "00:00","04:15",14000);
INSERT INTO airlines VALUES (5002, 003, 113, "GoAir", "Chennai", "Kolkata", "1662 KM", "2hrs 30mins", "14:00","16:30",5000);
INSERT INTO airlines VALUES (5003, 001, 114, "AkasaAir", "Bangalore", "Rajkot", "1900 KM", "2hrs 00mins", "13:00","15:00",3500);
INSERT INTO airlines VALUES (5004, 001, 114, "AkasaAir", "Bangalore", "Rajkot", "1900 KM", "2hrs 00mins", "13:00","15:00");
INSERT INTO airlines VALUES (5009, 001, 111, "IndiGo", "Delhi", "Bangalore", "2175 KM", "2hrs 45mins", "16:00","18:45",4500);
INSERT INTO airlines VALUES (5008, 004, 111, "Spicejet", "Delhi", "Bangalore", "2175 KM", "2hrs 45mins", "14:00","16:45",4900);
INSERT INTO airlines VALUES (5007, 005, 111, "Vistara", "Delhi", "Bangalore", "2175 KM", "2hrs 45mins", "13:00","15:00",4950);
INSERT INTO airlines VALUES (5011, 001, 123, "Vistara", "Mumbai", "Ranchi", "2075 KM", "2hrs 00mins", "20:00","22:00",3500);
INSERT INTO airlines VALUES (5010, 005, 121, "DHL", "Delhi", "Singapore", "2475 KM", "4hrs 45mins", "11:00","15:45",0);
INSERT INTO airlines VALUES (5012, 001, 122, "Vistara", "Mumbai", "Mangalore", "1111 KM", "1hrs 15mins", "09:00","10:15",1550);


-- Insert values into passenger table 
INSERT INTO passenger VALUES (2050, "Regular", "Kruthi Shetty", "Female", "20 Y/o", "33 A");
INSERT INTO passenger VALUES (2051, "Senior Citizen", "Saraswati Shetty", "Female", "75 Y/o", "16 B");
INSERT INTO passenger VALUES (2052, "Armed Forces", "Ripu Daman Singh", "Male", "35 Y/o", "4 F");
INSERT INTO passenger VALUES (2053, "Student Fares", "Raunaq Bhogal", "Male", "21 Y/o", "14 G");
INSERT INTO passenger VALUES (2054, "Doctors and Nurses", "Roshni Joseph", "Female", "22 Y/o", "10 B");
INSERT INTO passenger VALUES (2055, "Regular", "Ronald Weasley", "Male", 27, "19 B");
INSERT INTO passenger VALUES (2056, "Regular", "Aditi Patil", "Female", 10, "8 C");
INSERT INTO passenger VALUES (2057, "Regular", "Badshah", "Male", 35, "5 B");
INSERT INTO passenger VALUES (2058, "Senior Citizen", "Gaytri Iyengar", "Female", 69, "10 C");
INSERT INTO passenger VALUES (2059, "Regular", "Gurmehar Kaur", "Female", 14, "1 A");
INSERT INTO passenger VALUES (2060, "Regular", "Darwin White", "Male", 16 , "7 A");
INSERT INTO passenger VALUES (2061, "Senior Citizen", "Swaran Kaur", "Female",73, "9 B");

-- Insert values into city table 
INSERT INTO city VALUES (021218, "Bangalore");
INSERT INTO city VALUES (040512, "Delhi");
INSERT INTO city VALUES (190716, "Singapore");
INSERT INTO city VALUES (130101, "Chennai");
INSERT INTO city VALUES (030321, "Kolkata");
INSERT INTO city VALUES (092418, "Rachi");
INSERT INTO city VALUES (092405, "Mangalore");
INSERT INTO city VALUES (180110, "Rajkot");
INSERT INTO city VALUES (021513, "Mumbai");

-- Insert values into booking(ticket) table 
INSERT INTO booking VALUES (9000, 5000, 2050, 040512, 021218, "17-09-2022","","18-10-2022","Window","On-Time");
INSERT INTO booking VALUES (9001, 5001, 2051, 190716, 021218,"12-08-2022","","15-09-2022","Isle","Delayed");
INSERT INTO booking VALUES (9002, 5002, 2052, 130101, 030321,"14-09-2022","","22-11-2022","Window","On-Time");
INSERT INTO booking VALUES (9003, 5000, 2053, 111 , 040512, 021218,"8-09-2022","","09-11-2022","Isle","On-Time");
INSERT INTO booking VALUES (9004, 5000, 2054, 111 , 040512, 021218,"4-09-2022","","10-11-2022","Middle","On-Time");
INSERT INTO booking VALUES (9005, 5000, 2055, 111 , 040512, 021218,"1-09-2022","","18-10-2022","Window","On-Time");
INSERT INTO booking VALUES (9006, 5007, 2056, 111 , 040512, 021218,"6-09-2022","","15-11-2022","Isle","Delayed");
INSERT INTO booking VALUES (9007, 5011, 2057, 123 , 021513, 180110,"18-09-2022","","28-11-2022","Middle","On-Time");
INSERT INTO booking VALUES (9008, 5010, 2058, 121 , 040512, 190716,"19-09-2022","","6-11-2022","Isle","On-Time");
INSERT INTO booking VALUES (9009, 5007, 2059, 111 , 040512, 021218,"4-09-2022","","10-11-2022","Window","Delayed");
INSERT INTO booking VALUES (9010, 5007, 2060, 111 , 040512, 021218,"7-09-2022","","12-11-2022","Window","Delayed");
INSERT INTO booking VALUES (9011, 5012, 2061, 122 , 021513, 092405,"9-09-2022","","29-11-2022","Window","Delayed");


