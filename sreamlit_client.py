import streamlit as st
from pages import todo_page, user_page, project_page

# Define page navigation
PAGES = {
    "Projects": project_page,
    "Todos": todo_page,
    "Users": user_page
}

# Main function to handle page navigation
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()