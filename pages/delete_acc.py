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

st.header(r"$\textsf{\large Delete account}$")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/NMt4Zgqv/Screenshot-2024-04-18-020228.png");]
    background-size: 100vw 100vh;
    background-position: fit to page;  
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

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/63rH0rVj/Untitled-design-3.png");]
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

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

def delete_userdata(username):
    c.execute('DELETE FROM users WHERE username=? ', (username,))
    conn.commit()

email_id = st.text_input(r"$\textsf{\large Enter Email ID}$")
username = st.text_input(r"$\textsf{\large Enter Username}$")
password = st.text_input(r"$\textsf{\large Enter Password}$", type= "password")

if st.button("Delete account"):
    st.warning("Are you sure you want to delete?")
    col1, col2 = st.columns(2)
    if col1.button("Yes"):
        delete_userdata(username)
        st.success("Successfully deleted your account")
        time.sleep(3)
        st.switch_page("pages/login.py")
    elif col2.button("No"):
        st.warning("")

col1, col2 = st.columns(2)
with col1:
    con = col1.container()
    con.page_link("home.py", label=r"$\textsf{\large Home}$", icon="🏠")
with col2:
    con = col2.container()
    con.page_link("pages/login.py",label=r"$\textsf{\large Back}$", icon="⬅️")