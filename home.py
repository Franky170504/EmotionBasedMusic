from PIL import Image
import streamlit as st

im = Image.open("C:\laukik\python_projects\EmotionBasedMusic\media\songicon.jpg")
st.set_page_config(	page_title="Emotion based music", 
    page_icon = im,
    layout="wide"
)

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

st.header(r"$\textsf{\large Welcome to Emotion Based Music Recommender}$")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: 
	url("https://i.postimg.cc/xTQnMggs/Screenshot-2024-04-17-232657.png");]
    background-size: 100vw 100vh;
    background-position: fit to page;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

custom_css = """
<style>
.stPageLink {
    font-size: 20px; 
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown(
    """
    ### Scan your emtions and listen the songs based on your mood!!
    """
)
st.markdown(" ")
st.markdown(
"""
    #### But first Don't forget to create your account for free 👇🏽
"""
)

col1, col2 = st.columns(2)
with col1:
    con = col1.container(height=100)
    con.page_link("pages/createaccount.py", label=r"$\textsf{\Large Sign in}$", icon="🏠")
    con.write("Create account")
with col2:
    con = col2.container(height=100)
    con.page_link("pages/login.py", label=r"$\textsf{\Large Log in}$", icon="🔓")
    con.write("Already a user?Login")

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
