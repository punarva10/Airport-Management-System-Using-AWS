import pandas as pd
import streamlit as st
from database import view_all_data, view_only_flight_number,get_flight, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["airlines_id", "airlines_at_id", "r_id", "airlines_name", "airlines_from", "airlines_to", "airlines_total_distance", "airlines_travel_time", "airlines_departure", "airlines_arrival","fare"]) 
    with st.expander("View  Flight"):
        st.dataframe(df)
    list_of_flight = [i[0] for i in view_only_flight_number()]
    selected_flight = st.selectbox("Flight to Edit", list_of_flight)
    selected_result = get_flight(selected_flight)
    # selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        airlines_id =selected_result[0][0]
        airlines_at_id = selected_result[0][1]
        r_id = selected_result[0][2]
        airlines_name = selected_result[0][3]   
        airlines_from=selected_result[0][4]
        airlines_to = selected_result[0][5]
        airlines_total_distance = selected_result[0][6]
        airlines_travel_time = selected_result[0][7]
        airlines_departure = selected_result[0][8]
        airlines_arrival = selected_result[0][9]
        fare = selected_result[0][10]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_airlines_id = st.text_input("Flight ID",airlines_id)
            new_airlines_at_id = st.text_input("Type of airline ID",airlines_at_id)
            new_r_id = st.text_input("Route ID",r_id)
            new_airlines_name = st.text_input("Airline Name",airlines_name)

        with col2:
            new_airlines_from = st.selectbox("Source", ["Bangalore", "Chennai", "Mumbai", "Mangaluru","Delhi", "Rajkot", "Kolkata","Singapore", "Dubai","Kochi","Hubli","Hyderabad","Srinagar","Jaipur","Ranchi","Bhopal","Indore","Paris","Macau","Tokyo","Seol","Lisbon","Rio de Jenario"])
            new_airlines_to = st.selectbox("Destination", ["Bangalore", "Chennai", "Mumbai", "Mangaluru","Delhi","Rajkot", "Kolkata","Singapore", "Dubai","Kochi","Hubli","Hyderabad","Srinagar","Jaipur","Ranchi","Bhopal","Indore","Paris","Macau","Tokyo","Seol","Lisbon","Rio de Jenario"])
            new_airlines_total_distance = st.text_input("Distance Covered",airlines_total_distance)
            new_airlines_travel_time = st.text_input("Time of Flight",airlines_travel_time)
            new_airlines_departure = st.text_input("Departure Time",airlines_departure)
            new_airlines_arrival = st.text_input("Arrival Time",airlines_arrival)
            new_fare = st.text_input("fare",fare)
       
        if st.button("Update"):
            edit_dealer_data(new_airlines_id, new_airlines_at_id, new_r_id, new_airlines_name, new_airlines_from, new_airlines_to, new_airlines_total_distance, new_airlines_travel_time, new_airlines_departure, new_airlines_arrival,float(new_fare),
                               airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival,fare)
            st.success("Successfully updated Availability of train: {}".format(new_airlines_id))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=["airlines_id", "airlines_at_id", "r_id", "airlines_name", "airlines_from", "airlines_to", "airlines_total_distance", "airlines_travel_time", "airlines_departure", "airlines_arrival","fare"])
    with st.expander("Updated Flight data"):
        st.dataframe(df2)