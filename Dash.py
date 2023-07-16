import streamlit as st
import pandas as pd
from camera_input_live import camera_input_live
from streamlit_webrtc import webrtc_streamer


# Adding Header / title of the Dash
st.title('HiveAssist') 


#Adding container for Video Play box in the centre 

#add video playback aligned in the centre
#image = camera_input_live()
#st.image(30)
webrtc_streamer(key="test")
#Create button for facial recognition 

