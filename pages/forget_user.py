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

def update_password(email_id, new_username):
    c.execute('UPDATE users SET username=? WHERE email_id=?', (new_username, email_id))
    conn.commit()
	
email_id = st.text_input("Enter Email ID")
new_username = st.text_input("Enter New Username")

if st.button("Change Password"):
    if not(email_id and new_username):
        st.error("Above Field Cannot be Empty")
    else:
        update_password(email_id, new_username)
        st.success("Account created! Login")
        st.write("Redirecting to Login page Login with created User id")
        time.sleep(2)
        st.switch_page("pages/login.py")

st.page_link("home.py", label="Home", icon="🏠")
st.page_link("pages/login.py", label="Back", icon="🔓")