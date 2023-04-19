import mysql.connector

mydb = mysql.connector.connect(
    host="airport1.chf5rsalfcvg.ap-southeast-2.rds.amazonaws.com",
    user="root",
    password="Alexa&katie-220306",
    database="airport1"
)
c = mydb.cursor(buffered=True)


#def create_table():
  #  c.execute('CREATE TABLE IF NOT EXISTS TRAIN(Train_No TEXT, Name TEXT, Train_Type TEXT, Source TEXT, Destination TEXT, Availability TEXT)')


def add_data(airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare):
    c.execute('INSERT INTO airlines(airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM airlines')
    data = c.fetchall()
    return data


def view_only_flight_number():
    c.execute('SELECT airlines_id FROM airlines')
    data = c.fetchall()
    return data

def get_flight(id):
    c.execute("SELECT * FROM airlines WHERE airlines_id='{}'".format(id))
    data = c.fetchall()
    return data

def edit_dealer_data(new_airlines_id, new_airlines_at_id, new_r_id, new_airlines_name, new_airlines_from, new_airlines_to, new_airlines_total_distance, new_airlines_travel_time, new_airlines_departure, new_airlines_arrival,new_fare,
                               airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare):
    c.execute("UPDATE airlines SET airlines_id=%s, airlines_at_id=%s, r_id=%s, airlines_name=%s, airlines_from=%s, airlines_to=%s, airlines_total_distance=%s, airlines_travel_time=%s, airlines_departure=%s, airlines_arrival=%s, fare=%s WHERE airlines_id=%s AND airlines_at_id=%s AND r_id=%s AND airlines_name=%s AND airlines_from=%s AND airlines_to=%s AND airlines_total_distance=%s AND airlines_travel_time=%s AND airlines_departure=%s AND airlines_arrival=%s AND fare=%s",
                 (new_airlines_id, new_airlines_at_id, new_r_id, new_airlines_name, new_airlines_from, new_airlines_to, new_airlines_total_distance, new_airlines_travel_time, new_airlines_departure, new_airlines_arrival,new_fare,
                               airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare))
    mydb.commit()
    c.execute("SELECT airlines_id FROM airlines")
    data = c.fetchall()
    return data


def delete_data(airlines_id):
    c.execute('DELETE FROM airlines WHERE airlines_id="{}"'.format(airlines_id))
    mydb.commit()

def execute_query(q):
    c.execute(q)
    data = c.fetchall()
    return data
