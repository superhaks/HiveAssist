import deepface
from deepface import DeepFace

import streamlit as st

#setting up the page icon
st.set_page_config(
    page_title="HiveAssist",
    page_icon=":honeybee:"
)

#providing title for the page
st.title("Hive-Monitor")
#adding sidebar to the page
st.sidebar.success("Select a page above.")

DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")