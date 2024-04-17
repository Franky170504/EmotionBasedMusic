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
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

st.title("Create account")
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/xCdR5qR8/bg2.jpg");]
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

db_dir = os.path.join("C:\laukik\python_projects\EmotionBasedMusic\database")
conn = sqlite3.connect(os.path.join(db_dir,"login.db"))
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS users(email_id TEXT,username TEXT,password TEXT)')

create_usertable()
    
def add_userdata(email_id, username, password):
	c.execute('INSERT INTO users(email_id, username, password) VALUES (?,?,?)',(email_id,username,password))
	conn.commit()

def user_exists(email_id,username) -> bool:
    c.execute("SELECT 1 FROM users WHERE (email_id, username) = (?,?)", (email_id,username))
    return c.fetchone() is not None

email_id = st.text_input(r"$\textsf{\large Enter Email ID}$")
username = st.text_input(r"$\textsf{\large Username}$")
password = st.text_input(r"$\textsf{\large Password}$", type = 'password')
pass_confirm = st.text_input(r"$\textsf{\large Confirm Password}$", type = "password" )

if st.button("Create account"):
    if not email_id.endswith("@gmail.com"):
        st.error("Please enter a valid Gmail address ending with @gmail.com")
    elif not(email_id and username and password and pass_confirm):
        st.error("Above Field Cannot be Empty")
    elif password == pass_confirm:
        if add_userdata(email_id, username ,password):
                st.success("Account created! Login")
                st.write("Redirecting to Login page Login with created User id")
                time.sleep(2)
                st.switch_page("pages/login.py")
        elif user_exists(email_id, username):
                st.error("Username already exists")
        
    elif password != pass_confirm:
        st.error("Password and Confirmation does not match")

col1, col2 = st.columns(2)
with col1:
    con = col1.container()
    con.page_link("home.py", label="Home", icon="🏠")
with col2:
    con = col2.container()
    con.page_link("pages/login.py", label="Back", icon="⬅️")
