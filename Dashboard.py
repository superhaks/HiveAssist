import deepface
from deepface import DeepFace
import streamlit as st
import cv2
from retinaface import RetinaFace
import io 
import PIL

from ImgProcessor import *
from Utilities.ExtractFaceFeatures import *

selected_options = None
selected_models = None 
selected_emotions = None


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
emotions = ["Happy", "Sad", "Neutral"]
selected_emotions = features.radio(
    "Select the emotions you want to enable :",
    emotions
)

#checking if the selected options are selected or not
#features.write(selected_options)

#creating a multiselect for all the students available options
models = ["Hazim", "Deepface"]
selected_models = selector.radio(
    "Select model :",
    models
)

def process_models():
    selector.success(selected_models)
    if selected_models == "Hazim":
        st.toast("Model Accuracy = 91%")
    else: 
        st.toast("Model Accuracy = 96%")

def process_attentiveness(dominant_emotion): 
    if selected_emotions == "Happy" and (dominant_emotion == "happy" or dominant_emotion == "surprise"):
        features.text("Attentive")
    elif selected_emotions == "Sad" and (dominant_emotion == "sad" or dominant_emotion == "angry" or dominant_emotion == "fear" or dominant_emotion == "disgust"):
        features.text("Attentive") 
    elif selected_emotions == "Neutral" and dominant_emotion == "neutral":
        features.text("Attentive") 
    elif selected_emotions == "Happy" and (dominant_emotion == "sad" or dominant_emotion == "angry" or dominant_emotion == "fear" or dominant_emotion == "disgust"):
        features.text("Inattentive")
    elif selected_emotions == "Sad" and (dominant_emotion == "happy" or dominant_emotion == "surprise"):
        features.text("Inattentive")  
    elif selected_emotions == "Happy" and dominant_emotion == "neutral":
        features.text("Neutral")
    elif selected_emotions == "Sad" and dominant_emotion == "neutral":
        features.text("Neutral")  




def display_eye_tracking_info(m_left_eye,m_right_eye):
    camera_in.text(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")

def display_face_detection_info(m_face):
    camera_in.text(f"Co-ordinates of Face: {m_face}")

def display_emotion_detection_info(m_dominant_emotion):
    camera_in.text(f"Dominant Emotion : {m_dominant_emotion}")



def process_and_print(selected_option,m_face, m_left_eye, m_right_eye, m_dominant_emotion):
    info =""
    # Display selected features
    for option in selected_option:
        if option == "Eye Tracking":
            display_eye_tracking_info(m_left_eye,m_right_eye)
        elif option == "Face Detection":
            display_face_detection_info(m_face)
        elif option == "Emotion Detection":
            display_emotion_detection_info(m_dominant_emotion)
    

camera = cv2.VideoCapture(0)
run = camera_in.checkbox('Start Video')
FRAME_WINDOW = camera_in.image([])
while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    # Convert NumPy array to file-like object
    img_file_buffer = io.BytesIO()
    PIL.Image.fromarray(frame).save(img_file_buffer, format='JPEG')

    # Seek to the beginning of the buffer
    img_file_buffer.seek(0)

    # img_file_buffer = frame
    # camera_in.write(type(img_file_buffer))
    m_face, m_left_eye, m_right_eye, m_dominant_emotion = image_processing(img_file_buffer)
    process_and_print(selected_options,m_face, m_left_eye, m_right_eye, m_dominant_emotion)
    process_attentiveness(m_dominant_emotion)
    process_models()
    # camera_in.write(info)
else: 
    camera_in.text("Stopped")

# camera_in.write(resp)
# camera_in.write("---")
# camera_in.write(objs)
# -----


#DeepFace.stream("pages/FaceData","VGG-Face","opencv","euclidean_l2")