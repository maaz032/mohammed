# pages/login.py
import streamlit as st
import time  # Add this import
from config import USER_CREDENTIALS, hash_password

# Function to check if the username and password are correct
def authenticate(username, password):
    hashed_password = hash_password(password)
    if username in USER_CREDENTIALS and hash_password(USER_CREDENTIALS[username]) == hashed_password:
        return True
    return False

def login_page():
    st.subheader('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "Main Content"
            st.session_state.last_activity_time = time.time()  # Update last activity time
            st.rerun()  # Refresh the app to show the main page
        else:
            st.error('Username/password is incorrect')

    if st.button('Sign Up'):
        st.session_state.page = "Sign Up"
        st.rerun()  # Refresh the app to show the sign-up page
