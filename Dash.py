import deepface
from deepface import DeepFace
import streamlit as st
import cv2
from retinaface import RetinaFace

from Utilities.EyeTracking import *
from Utilities.ExtractFaceFeatures import *

#setting up the page icon and page layout
st.set_page_config(
    page_title="HiveAssist",
    page_icon=":honeybee:",
    layout="wide"
)

#Dividing the app interface into columns
a, b, c = st.columns(3)

#providing title for the page
b.title("Hive Monitor")

#Putting a divider in between the Header and the rest of the page
st.divider()
st.write("")

#creating columns to add individual features on that part of the UI
features, camera_in, selector = st.columns([0.2, 0.6, 0.2])

#creating a multiselect for all the feature options available options
options = ["Face Detection", "Eye Tracking", "Emotion Detection"]
selected_options = features.multiselect(
    "Select the features you want to enable :",
    options
)

#making emotions multiselect
emotions = ["Happy", "Sad", "Neutral", "Shocked"]
selected_emotions = features.multiselect(
    "Select the emotions you want to enable :",
    emotions
)

#checking if the selected options are selected or not
#features.write(selected_options)

#creating a multiselect for all the students available options
students = ["Hazim", "Elon", "Bill"]
selected_students = selector.multiselect(
    "Select student(s) :",
    students
)


### For future reference to add a block a space
selector.write("")
selector.write("")
selector.write("")
selector.write("")
selector.write("")
selector.write("")
selector.write("")  
###


#creating a multiselect for all the attribute description
attributes = ["Face", "Eye", "Description"]
selected_attributes = selector.multiselect(
    "Select attribute :",
    attributes
)

# run = True
# FRAME_WINDOW = camera_in.image([])
# camera = cv2.VideoCapture(0)

# while run:
#     _, frame = camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     camera_in.write('Stopped')



# ------ Camera Operations ------
img_file_buffer = camera_in.camera_input("")

#getting Processed features into variables
m_face, m_left_eye, m_right_eye, m_dominant_emotion = image_processing(img_file_buffer)

#cascaded output
camera_in.camera_output("")

#features.write(selected_options)

# if selected_options == (["Eye Tracking"]):
#     camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")

# if selected_options == (["Face Detection"]):
#     camera_in.write(f"Co-ordinates of Face: {m_face}")

# if selected_options == (["Emotion Detection"]):
#     camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )

# if selected_options == (["Eye Tracking","Emotion Detection"]) or selected_options == (["Emotion Detection", "Eye Tracking"]):
#     camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
#     camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )

# if selected_options == (["Eye Tracking", "Face Detection"]) or selected_options == (["Face Detection", "Eye Tracking"]):
#      camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
#      camera_in.write(f"Co-ordinates of Face: {m_face}")

# if selected_options == (["Emotion Detection", "Face Detection"]) or selected_options == (["Face Detection", "Emotion Detection"]):
#     camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )
#     camera_in.write(f"Co-ordinates of Face: {m_face}")

# if selected_options == (["Emotion Detection", "Face Detection", "Eye Tracking"]) or selected_options == (["Eye Tracking", "Face Detection", "Emotion Detection"]) or selected_options == (["Emotion Detection", "Eye Tracking", "Face Detection" ]) or selected_options == (["Eye Tracking", "Emotion Detection", "Face Detection"]) or selected_options == (["Face Detection", "Emotion Detection", "Eye Tracking"]) or selected_options == (["Face Detection", "Eye Tracking", "Emotion Detection"]):
#     camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )
#     camera_in.write(f"Co-ordinates of Face: {m_face}")
#     camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")

def display_eye_tracking_info():
    camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")

def display_face_detection_info():
    camera_in.write(f"Co-ordinates of Face: {m_face}")

def display_emotion_detection_info():
    camera_in.write(f"Dominant Emotion : {m_dominant_emotion}")

# Display selected features
for selected_option in selected_options:
    if selected_option == "Eye Tracking":
        display_eye_tracking_info()
    elif selected_option == "Face Detection":
        display_face_detection_info()
    elif selected_option == "Emotion Detection":
        display_emotion_detection_info()

    
    
# camera_in.write(resp)
# camera_in.write("---")
# camera_in.write(objs)
# -----


#adding sidebar to the page
st.sidebar.success("Pages")

#DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")