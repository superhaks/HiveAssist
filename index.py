import pickle
from pathlib import Path

from streamlit_webrtc import webrtc_streamer
import av

#pip install streamlit
import streamlit as st 
#pip install streamlit-authenticator
import streamlit_authenticator as stauth

#User Authentication
names = ["Clark Kent", "Bruce Wayne"]
unames = ["superman","batman"]

#load hashed passwords with read binary 
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

#creating a login object which can further be enhanced to save cookies
authenticator = stauth.Authenticate(names, unames, hashed_passwords)

#setting the authenticator to be on the main page
name, authentication_status, unames = authenticator.login("Login","main")

#setting up authentication messages
#if the authentication fails
if authentication_status == False:
    st.error("Username / Password is incorrect")

#if the user has not filled anything
if authentication_status == None:
    st.warning("Please enter your username and password")

#if user is authenticated 
    if authentication_status: 
        #creating logout button in the sidebar
        authenticator.logout("Logout","sidebar")
        st.sidebar.title(f"Welcome {name} ")
        st.sidebar.header("Pages")
        
        #title of the page
        st.title("HiveAssist")

        #making a checkbox to flip the video
        flip = st.checkbox("Flip")

        #making the video input stream
        def video_frame_callback(frame):
            vframe = frame.to_ndarray(format="bgr24")
            flipped = vframe[::-1,:,:] if flip else vframe
            return av.VideoFrame.from_ndarray(flipped, format='bgr24')
        
        webrtc_streamer(key="example", video_frame_callback=video_frame_callback)