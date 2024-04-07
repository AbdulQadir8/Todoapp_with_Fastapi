# streamlit_client.py

import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timezone

BASE_URL = "http://0.0.0.0:8080"

st.title("Todo App Projects")

def create_project():
    name = st.text_input("Enter Project Name")
    status = st.text_input("Enter Status")
    time_stamp = datetime.now().isoformat()
    if st.button("Add Project"):
        payload = {"project_name": name,
                   "status": status,
                   "time_stamp": time_stamp
        }
        response = requests.post(f"{BASE_URL}/projects/", json=payload)
        if response.status_code == 200:
            st.success("Project added successfully")

def delete_project():
    project_id = st.number_input("Enter Project ID to delete")
    if st.button("Delete Project"):
        response = requests.delete(f"{BASE_URL}/projects/{project_id}")
        if response.status_code == 200:
            st.success("project deleted successfully")
        if response.status_code == 404:
            st.error(f"Project Not Found with ID:{project_id}")

def display_projects():
    if st.button("Display Projects"):
        response = requests.get(f"{BASE_URL}/projects/")
        if response.status_code == 200:
            projects = response.json()
            for project in projects:

                df = pd.DataFrame(
                            project['project_name'],
                            project['status'],
                            project['time_stamp'],
                            columns=["Title","Status","TimeStamp"]
                      )
            st.dataframe(df)
                # st.write(f"Title: {project['project_name']}, Status: {project['status']}, TimeStamp: {project['time_stamp']}")


def project_page():
    create_project()
    delete_project()
    display_projects()



if __name__ == "__main__":
    project_page()