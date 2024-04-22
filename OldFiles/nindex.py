import cv2
import streamlit as st
import numpy as np
from deepface import DeepFace
import streamlit as st
import cv2
from retinaface import RetinaFace
from HiveAssist.Utilities.ExtractEmotion import *
from HiveAssist.Utilities.ExtractFaceFeatures import *


st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    ret, frame_np = camera.read()  # Read frame
    
    if ret:
        try:
            frame_np = cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB)  # Convert color space
            FRAME_WINDOW.image(frame_np)            # Display the frame
            faces = RetinaFace.detect_faces(frame_np)
            objs = DeepFace.analyze(img_path=frame_np, actions=['emotion'], detector_backend ="ssd", enforce_detection= False)
            facial, rey, ley = ret_features(faces)
            dominant = ret_emotion(objs)
        except Exception as e:
            st.error(f"Error processing frame: {str(e)}")
    else:
        st.error("Failed to capture frame.")
    
    if not run:
        break

# Release the webcam when done
camera.release()
st.write('Stopped')


