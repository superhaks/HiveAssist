import deepface
from deepface import DeepFace
import streamlit as st

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

features, camera_in, selector = st.columns(3)


#adding sidebar to the page
st.sidebar.success("Pages")

#DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")