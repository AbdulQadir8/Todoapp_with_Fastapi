# streamlit_client.py

import streamlit as st
import requests
from datetime import datetime, timezone

BASE_URL = "http://0.0.0.0:8080"

st.title("Todo App Todos")

def create_todo():
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    status = st.text_input("Enter Status")
    project_id = st.number_input("Enter todo ID")
    due_date = datetime.now().isoformat()
    time_stamp = datetime.now().isoformat()
    if st.button("Add Todo"):
        payload = {"name": title,
                   "body": description,
                   "status": status,
                   "due_date": due_date,
                   "time_stamp": time_stamp, 
                   "project_id": project_id}
        response = requests.post(f"{BASE_URL}/todos/", json=payload)
        if response.status_code == 200:
            st.success("Todo added successfully")

def delete_todo():
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")
        if response.status_code == 404:
            st.error(f"Todo Not Found with ID:{todo_id}")

def display_todos():
    if st.button("Display Todos"):
        response = requests.get(f"{BASE_URL}/todos/")
        if response.status_code == 200:
            todos = response.json()
            for todo in todos:
                st.write(f"Title: {todo['name']}, Description: {todo['body']}, Status: {todo['status']}")

if __name__ == "__main__":
    create_todo()
    delete_todo()
    display_todos()