import deepface
from deepface import DeepFace
import streamlit as st
import cv2
from retinaface import RetinaFace

from Utilities.EyeTracking import *

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
options = features.multiselect(
    "Select the features you want to enable :",
    ["Face Detection", "Eye Tracking", "Emotion Detection"] 
)

#creating a multiselect for all the students available options
options = selector.multiselect(
    "Select student(s) :",
    ["Hazim", "Elon", "Bill"] 
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
options = selector.multiselect(
    "Select attribute :",
    ["Face", "Eye", "Description"] 
)

# ------ Camera Operations ------
img_file_buffer = st.camera_input("Take a picture")

resp, objs = image_processing(img_file_buffer)
st.write(resp)
st.write("---")
st.write(objs)
# -----


#adding sidebar to the page
st.sidebar.success("Pages")

#DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")