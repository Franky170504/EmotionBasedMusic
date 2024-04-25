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
# st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -10em;
        }
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

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

st.title("Login")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/1zcgmfwj/bg2.jpg");
    background-size: 100vw 100vh;
    background-position: fit to page;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

def login_user(username,password):
	c.execute('SELECT * FROM users WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

username = st.text_input(r"$\textsf{\large Enter Username}$")
password = st.text_input(r"$\textsf{\large Enter Password}$", type="password")

if st.button('Login'):
    result = login_user(username,password)
    if result:
        st.success(f"Logged In as {username}")
        time.sleep(3)
        st.switch_page("pages/music.py")
    else:
        st.warning("Incorrect Username/Password")

col1, col2, col3, col4 = st.columns(4)
with col1:
    con = col1.container()
    con.page_link("home.py", label="Home", icon="🏠")
with col2:
    con = col2.container()
    con.page_link("pages/forget_pass.py", label="Forget Password", icon="🔑")
with col3:
    con = col3.container()
    con.page_link("pages/forget_user.py", label="Forget Username", icon="🔐")
with col4:
    con = col4.container()
    con.page_link("pages/delete_acc.py", label="Delete Account", icon="🗑️")