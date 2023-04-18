import pandas as pd
import streamlit as st
from database import view_all_data, view_only_flight_number, delete_data


def delete():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["airlines_id", "airlines_at_id", "r_id", "airlines_name", "airlines_from", "airlines_to", "airlines_total_distance", "airlines_travel_time", "airlines_departure", "airlines_arrival","fare"]) 
    with st.expander("View all Flight"):
        st.dataframe(df)

    list_of_flight = [i[0] for i in view_only_flight_number()]
    selected_flight = st.selectbox("Flight to Delete", list_of_flight)
    st.warning("Do you want to delete Flight:{}".format(selected_flight))
    if st.button("Delete Flight"):
        delete_data(selected_flight)
        st.success("Flight entry has been deleted successfully")

    new_result = view_all_data()
    df = pd.DataFrame(new_result, columns=["airlines_id", "airlines_at_id", "r_id", "airlines_name", "airlines_from", "airlines_to", "airlines_total_distance", "airlines_travel_time", "airlines_departure", "airlines_arrival","fare"]) 
    with st.expander("Updated Flight data"):
        st.dataframe(df)