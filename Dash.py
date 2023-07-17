import streamlit as st
import pandas as pd
from camera_input_live import camera_input_live
from streamlit_webrtc import webrtc_streamer
import av
import cv2

# Adding Header / title of the Dash
st.title('HiveAssist') 


#Adding container for Video Play box in the centre 

#add video playback aligned in the centre
#image = camera_input_live()
#st.image(30)
#webrtc_streamer(key="test")

class ProcessedVideo:
    def rec(self,frame):
        frm = frame.to_ndarray(format="bgr24")

        return av.VideoFormat.from_ndarray(frm, format="bgr24")


webrtc_streamer(key="test",video_processor_factory= ProcessedVideo)


#working code side tracked for better code
#def video_frame_callback(frame):
#   img = frame.to_ndarray(format="bgr24")  
#    return av.VideoFrame.from_ndarray(format="bgr24")
#webrtc_streamer(key="example", video_frame_callback=video_frame_callback)


#Create button for facial recognition 

