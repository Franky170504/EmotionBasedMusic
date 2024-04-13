from PIL import Image
import streamlit as st
import sqlite3
import time
import os

im = Image.open("C:\laukik\python_projects\EmotionBasedMusic\media\songicon.jpg")
st.set_page_config(	page_title="Emotion based music", 
    page_icon = im,
    layout="wide"
)
st.title("Create account")
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
db_dir = os.path.join("C:\laukik\python_projects\EmotionBasedMusic\database")
conn = sqlite3.connect(os.path.join(db_dir,"login.db"))
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO users(username,password) VALUES (?,?)',(username,password))
	conn.commit()

username = st.text_input("Enter Username")
password = st.text_input("Enter Password", type = 'password')
pass_confirm = st.text_input("Confirm Password", type = "password" )

if st.button("Create account"):
    if not(username and password and pass_confirm):
        st.error("Above Field Cannot be Empty")
    elif password == pass_confirm:
        add_userdata(username ,password)
        st.success("Account created! Login")
        st.write("Redirecting to Login page Login with created User id")
        time.sleep(2)
        st.switch_page("pages/login.py")
    elif password != pass_confirm:
        st.error("Password and Confirmation does not match")
        
st.page_link("home.py", label="Home", icon="🏠")
st.page_link("pages/login.py", label="Back", icon="🔓")
