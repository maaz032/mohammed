# pages/signup.py
import streamlit as st
import time  # Add this import
from config import USER_CREDENTIALS, hash_password

# Function to add a new user
def add_user(username, password):
    USER_CREDENTIALS[username] = hash_password(password)

def signup_page():
    st.subheader('Sign Up')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if st.button('Sign Up'):
        if password != confirm_password:
            st.error('Passwords do not match')
        elif username in USER_CREDENTIALS:
            st.error('Username already exists')
        else:
            add_user(username, password)
            st.success('Account created successfully! You can now log in.')
            st.session_state.page = "Login"
            st.rerun()  # Refresh the app to show the login page
