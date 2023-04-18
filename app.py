import streamlit as st
from create import create
#from database import create_table
from delete import delete
from read import read
from update import update
from queries import query

def main():
    st.title("Airline_ticket_booking_system")
    menu = ["Add", "View", "Edit", "Delete","Query"]
    choice = st.sidebar.selectbox("Menu", menu)
    #create_table()
    if choice == "Add":
        st.subheader("Enter Plane Details:")
        create()
    elif choice == "View":
        st.subheader("View Plane tasks")
        read()
    elif choice == "Edit":
        st.subheader("Update Plane tasks")
        update()
    elif choice == "Delete":
        st.subheader("Delete Plane tasks")
        delete()
    else:
        st.subheader("Enter Query")
        query()
if __name__ == '__main__':
    main()