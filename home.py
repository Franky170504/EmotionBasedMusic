from PIL import Image
import streamlit as st

im = Image.open("C:\laukik\python_projects\EmotionBasedMusic\media\songicon.jpg")
st.set_page_config(	page_title="Emotion based music", 
    page_icon = im,
    layout="wide"
)
st.header(r"$\textsf{\large Welcome to Emotion Based Music Recommender}$")
st.markdown('''
 

''')
st.page_link("pages/createaccount.py", label="Sign in", icon="🏠")
st.page_link("pages/login.py", label="Login", icon="🔓")

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)