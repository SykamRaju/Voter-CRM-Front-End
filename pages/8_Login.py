import streamlit as st
from typing import Callable
from PIL import Image

class Login:
    def __init__(self):
        st.title("Voter CRM Admin Portal")
        # Load the Voter CRM logo
        logo = Image.open("voterCRM.jpeg")

        # Display the logo and title next to each other
        col1, col2 = st.columns([1, 1.5])
        with col1:
            st.image(logo, width=125)
        with col2:
            st.markdown("<h1>Voter CRM</h1>", unsafe_allow_html=True)

        st.markdown('-----')

        st.markdown("""
            <style>
                div.stButton>button {
                    border: none;
                    padding: 1rem 2rem;
                    border-radius: 0.5rem;
                    text-align: center;
                    width: 100%;
                }
                div.stButton>button:hover {
                    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
                }
                div.stButton>button:focus {
                    border-bottom-color: #4CAF50;
                    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Create the buttons
        col1, col2 = st.columns(2)
        with col1:
            login_header = st.button("Login", key='login_header')
        with col2:
            sign_up_header = st.button("Sign Up", key='sign_up_header')
        if login_header:
            login_form = st.form(key='login-form')
            with login_form:
                username=st.text_input("Username")
                password=st.text_input("Password",type="password")
                def do_login(uname, pwd):
                    print(uname)
                    print(pwd)
                login_btn = login_form.form_submit_button(label='Login', on_click=do_login(username, password))

        if sign_up_header :
            signup_form = st.form(key='signup-form')
            with signup_form:
                def validate_passwords(passw, cpass):
                    if password != confirm_password:
                        signup_form.form_report_error('Confirm Password', 'Passwords do not match')
                username = signup_form.text_input('Username')
                password = signup_form.text_input('Password', type='password')
                confirm_password = signup_form.text_input('Confirm Password', type='password')
                sign_up = signup_form.form_submit_button(label='Sign Up', on_click=validate_passwords(password, confirm_password))

Login()