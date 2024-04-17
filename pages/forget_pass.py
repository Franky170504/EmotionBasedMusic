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
st.header(r"$\textsf{\large Forget Password}$")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/k4vVZRkQ/Screenshot-2024-04-18-004541.png");]
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
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

def update_password(username, new_password):
    c.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
    conn.commit()
	
username = st.text_input(r"$\textsf{\large Enter Username}$")
new_password = st.text_input(r"$\textsf{\large Enter New Password}$", type = 'password')
new_pass_confirm = st.text_input(r"$\textsf{\large Confirm New Password}$", type = "password" )

if st.button("Change Password"):
    if not(username and new_password and new_pass_confirm):
        st.error("Above Field Cannot be Empty")
    elif new_password == new_pass_confirm:
        update_password(username, new_password)
        st.success("Account created! Login")
        st.write("Redirecting to Login page Login with created User id")
        time.sleep(2)
        st.switch_page("pages/login.py")
    elif new_password != new_pass_confirm:
        st.error("Password and Confirmation does not match")

col1, col2 = st.columns(2)
with col1:
    con = col1.container()
    con.page_link("home.py", label="Home", icon="🏠")
with col2:
    con = col2.container()
    con.page_link("pages/login.py", label="Back", icon="⬅️")