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


if selected_options == (["Eye Tracking"]):
    camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")

elif selected_options == (["Face Detection"]):
    camera_in.write(f"Co-ordinates of Face: {m_face}")

elif selected_options == (["Emotion Detection"]):
    camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )

elif selected_options == (["Eye Tracking"]) and selected_options == (["Emotion Detection"]):
    camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
    camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )

elif selected_options == (["Eye Tracking", "Face Detection"]):
     camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
     camera_in.write(f"Co-ordinates of Face: {m_face}")

elif selected_options == (["Emotion Detection", "Face Detection"]):
    camera_in.write(f"Dominant Emotion : {m_dominant_emotion}" )
    camera_in.write(f"Co-ordinates of Face: {m_face}")




    
    
# camera_in.write(resp)
# camera_in.write("---")
# camera_in.write(objs)
# -----


#adding sidebar to the page
st.sidebar.success("Pages")

#DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")