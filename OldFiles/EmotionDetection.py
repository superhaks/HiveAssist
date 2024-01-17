import streamlit as st
import pandas as pd
from streamlit_webrtc import webrtc_streamer
import av
from deepface import DeepFace
# Adding Header / title of the Dash
st.title("Emotion Detection") 

#Adding container for Video Play box in the centre 

#add video playback aligned in the centre
# image = ()
# st.image(30)

flip = st.checkbox("Flip")
# gaze = GazeTracking()


# class ProcessedVideo:
#     def rec(self,frame):
#         vframe = frame.to_ndarray(format="bgr24")
#         flipped = vframe[::-1,:,:] if flip else vframe
#         return av.VideoFormat.from_ndarray(flipped,format="bgr24")


# webrtc_streamer(key="test",video_processor_factory= ProcessedVideo)


#working code side tracked for better code
def video_frame_callback(frame):
  vframe = frame.to_ndarray(format="bgr24")
  DeepFace.stream("pages/FaceData")  
  flipped = vframe[::-1,:,:] if flip else vframe
  return av.VideoFrame.from_ndarray(flipped, format='bgr24')


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)


#Create button for facial recognition 

