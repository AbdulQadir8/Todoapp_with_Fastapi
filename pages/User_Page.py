# streamlit_client.py

import streamlit as st
import requests
from datetime import datetime, timezone

BASE_URL = "http://0.0.0.0:8080"

st.title("Todo app Users")

def create_user():
    user_name = st.text_input("Enter User Name")
    user_email = st.text_input("Enter email")
    user_password = st.text_input("Enter Password")
    birthday = datetime.now().isoformat()
    phone_number = st.text_input("Enter Phone Number")
    time_stamp = datetime.now().isoformat()
    if st.button("Add User"):
        payload = {"user_name": user_name,
                   "user_email": user_email,
                   "user_password": user_password,
                   "birthday": birthday,
                   "phone_number": phone_number, 
                   "time_stamp": time_stamp}
        response = requests.post(f"{BASE_URL}/users/", json=payload)
        if response.status_code == 200:
            st.success("User added successfully")

def delete_user():
    user_id = st.number_input("Enter User ID to delete")
    if st.button("Delete User"):
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        if response.status_code == 200:
            st.success("User deleted successfully")
        if response.status_code == 404:
            st.error(f"User Not Found with ID:{user_id}")

def display_users():
    if st.button("Display Users"):
        response = requests.get(f"{BASE_URL}/users/")
        if response.status_code == 200:
            users = response.json()
            for user in users:
                st.write(f"Name: {user['user_name']}, Email: {user['user_email']}, Password: {user['user_password']}, Birthday: {user['birthday']}, PhoneNumber: {user['phone_number']}, TimeStamp: {user['time_stamp']}")


def user_page():
    create_user()
    delete_user()
    display_users()




if __name__ == "__main__":
    user_page()
    