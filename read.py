import pandas as pd
import streamlit as st

from database import view_all_data

def read():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["airlines_id", "airlines_at_id", "r_id", "airlines_name", "airlines_from", "airlines_to", "airlines_total_distance", "airlines_travel_time", "airlines_departure", "airlines_arrival","fare"]) 
    with st.expander("View all Flights"):
        st.dataframe(df)
