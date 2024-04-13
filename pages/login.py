import time
from PIL import Image
import streamlit as st
import sqlite3
import os

im = Image.open("C:\laukik\python_projects\EmotionBasedMusic\media\songicon.jpg")
st.set_page_config(	page_title="Emotion based music", 
    page_icon = im,
    layout="wide"
)
db_dir = os.path.join("C:\laukik\python_projects\EmotionBasedMusic\database")
conn = sqlite3.connect(os.path.join(db_dir,"login.db"))
c = conn.cursor()
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("Streamlit Login App")

def login_user(username,password):
	c.execute('SELECT * FROM users WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button('Login'):
    result = login_user(username,password)
    if result:
        st.success("Logged In as {}".format(username))
        time.sleep(3)
        st.switch_page("pages/music.py")
    else:
        st.warning("Incorrect Username/Password")

