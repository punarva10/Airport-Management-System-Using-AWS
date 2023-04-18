import streamlit as st
from database import add_data

def create():
    col1, col2 = st.columns(2)
    with col1:
        airlines_id = st.text_input("Flight ID")
        airlines_at_id = st.text_input("Type of airline ID")
        r_id = st.text_input("Route ID")
        airlines_name = st.text_input("Airline Name")

    with col2:
        airlines_from = st.selectbox("Source", ["Bangalore", "Chennai", "Mumbai", "Mangaluru","Delhi", "Rajkot", "Kolkata","Singapore", "Dubai","Kochi","Hubli","Hyderabad","Srinagar","Jaipur","Ranchi","Bhopal","Indore","Paris","Macau","Tokyo","Seol","Lisbon","Rio de Jenario"])
        airlines_to = st.selectbox("Destination", ["Bangalore", "Chennai", "Mumbai", "Mangaluru","Rajkot", "Kolkata","Singapore", "Dubai","Kochi","Hubli","Hyderabad","Srinagar","Jaipur","Ranchi","Bhopal","Indore","Paris","Macau","Tokyo","Seol","Lisbon","Rio de Jenario"])
        airlines_total_distance = st.text_input("Distance Covered")
        airlines_travel_time = st.text_input("Time of Flight")
        airlines_departure = st.text_input("Departure Time")
        airlines_arrival = st.text_input("Arrival Time")
        fare = st.text_input("Fare")
    if st.button("Add Flight Details"):
        add_data(airlines_id, airlines_at_id, r_id, airlines_name, airlines_from, airlines_to, airlines_total_distance, airlines_travel_time, airlines_departure, airlines_arrival, float(fare) )
        st.success("Successfully added Plane: {}".format(airlines_id))