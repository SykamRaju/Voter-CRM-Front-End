from asyncio.windows_events import NULL
import streamlit as st
from typing import Callable
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages

class Login:
    def __init__(self, on_login:Callable[[str,str],bool]):
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

        if 'stage' not in st.session_state:
            st.session_state.stage = 0

        # Create the buttons
        col1, col2 = st.columns(2)
        with col1:
            login_header = st.button("Login", key='login_header')
            if login_header:
                st.session_state.stage = 1
        with col2:
            sign_up_header = st.button("Sign Up", key='sign_up_header')
            if sign_up_header:
                st.session_state.stage = 2
        if st.session_state.stage == 1:
            form = st.form(key='login_form')
            username=form.text_input("Username")
            password=form.text_input("Password",type="password")
            submit_button = form.form_submit_button(label='Submit', on_click=do_login(username, password))
            print(login_header)
            print(submit_button)
            do_login(username, password)

        if st.session_state.stage == 2 :
            signup_form = st.form(key='signup_form')
            with signup_form:
                def validate_passwords(passw, cpass):
                    print(passw)
                    st.session_state.more_stuff = True
                    if password != confirm_password:
                        signup_form.form_report_error('Confirm Password', 'Passwords do not match')
                username = signup_form.text_input('Username')
                password = signup_form.text_input('Password', type='password')
                confirm_password = signup_form.text_input('Confirm Password', type='password')
                sign_up = signup_form.form_submit_button(label='Sign Up', on_click=validate_passwords(password, confirm_password))

def do_login(uname, pwd):
    if uname == 't' and pwd == 'p':
        st.session_state.stage = 0
        switch_page('states')


Login(do_login)