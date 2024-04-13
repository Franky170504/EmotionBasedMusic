from PIL import Image
import streamlit as st
import os
import sqlite3
import time

im = Image.open("C:\laukik\python_projects\EmotionBasedMusic\media\songicon.jpg")
st.set_page_config(	page_title="Emotion based music", 
    page_icon = im,
    layout="wide"
)
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

def delete_userdata(username):
    c.execute('DELETE FROM users WHERE username=? ', (username,))
    conn.commit()

email_id = st.text_input("Enter Email ID")
username = st.text_input("Enter Username")
password = st.text_input("enter Password", type= "password")
if st.button("Delete account"):
    delete_userdata(username)
    st.success("Successfully deleted your account")
    time.sleep(3)
    st.switch_page("pages/login.py")


st.page_link("home.py", label="Home", icon="🏠")
st.page_link("pages/login.py", label="Back", icon="🔓")