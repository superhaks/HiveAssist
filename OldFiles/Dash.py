import deepface
from deepface import DeepFace
import streamlit as st
import cv2
from retinaface import RetinaFace

from HiveAssist.EyeTracking import *
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

#creating a multiselect for all the students available options
students = ["Hazim", "Elon", "Bill"]
selected_students = selector.multiselect(
    "Select student(s) :",
    students
)


#creating a multiselect for all the attribute description
attributes = ["Face", "Eye", "Description"]
selected_attributes = selector.multiselect(
    "Select attribute :",
    attributes
)


run = camera_in.checkbox('Run')
FRAME_WINDOW = camera_in.image([])
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

m_face = None
m_right_eye = None
m_left_eye = None
m_dominant_emotion = None

while run:
    ret, frame_np = camera.read()  # Read frame
    
    if ret:
        try:
            frame_np = cv2.cvtColor(frame_np, cv2.COLOR_BGR2RGB)  # Convert color space
            FRAME_WINDOW.image(frame_np)            # Display the frame
            faces = RetinaFace.detect_faces(frame_np)
            objs = DeepFace.analyze(img_path=frame_np, actions=['emotion'], detector_backend ="ssd", enforce_detection= False)
            m_face, m_right_eye, m_left_eye = ret_features(faces)
            m_dominant_emotion = ret_emotion(objs)
        except Exception as e:
            st.error(f"Error processing frame: {str(e)}")
    else:
        st.error("Failed to capture frame.")
    

    if not run:
        break

# Release the webcam when done
camera.release()
camera_in.write('Engagement recording halted')




# ------ Display Features ------
selected_options = ["Eye Tracking", "Face Detection", "Emotion Detection"]

# Display selected features
for selected_option in selected_options:
    if selected_option == "Eye Tracking":
        if m_right_eye is not None and m_left_eye is not None:
            camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
        else:
            camera_in.write("Eye tracking data not available.")
    elif selected_option == "Face Detection":
        if m_face is not None:
            camera_in.write(f"Co-ordinates of Face: {m_face}")
        else:
            camera_in.write("Face detection data not available.")
    elif selected_option == "Emotion Detection":
        if m_dominant_emotion is not None:
            camera_in.write(f"Dominant Emotion: {m_dominant_emotion}")
        else:
            camera_in.write("Emotion detection data not available.")


#adding sidebar to the page
st.sidebar.success("")



# import cv2
# import streamlit as st
# from retinaface import RetinaFace
# from deepface import DeepFace
# from Utilities.EyeTracking import *
# from Utilities.ExtractFaceFeatures import *

# # Function to process frames for face detection and emotion analysis
# def process_frame(frame):
#     faces = RetinaFace.detect_faces(frame)
#     objs = DeepFace.analyze(img_path=frame, actions=['emotion'], detector_backend="ssd", enforce_detection=False)
#     m_face, m_right_eye, m_left_eye = ret_features(faces)
#     m_dominant_emotion = ret_emotion(objs)
#     return faces, m_face, m_right_eye, m_left_eye, m_dominant_emotion

# # Main function
# def main():
#     # Setting up the page
#     st.set_page_config(
#         page_title="HiveAssist",
#         page_icon=":honeybee:",
#         layout="wide"
#     )

#     # Page layout
#     a, b, c = st.columns(3)
#     b.title("Hive Monitor")
#     st.divider()

#     # Feature selection
#     features, camera_in, selector = st.columns([0.2, 0.6, 0.2])
#     options = ["Face Detection", "Eye Tracking", "Emotion Detection"]
#     selected_options = features.multiselect("Select the features you want to enable:", options)
#     emotions = ["Happy", "Sad", "Neutral", "Shocked"]
#     selected_emotions = features.multiselect("Select the emotions you want to enable:", emotions)
#     students = ["Hazim", "Elon", "Bill"]
#     selected_students = selector.multiselect("Select student(s):", students)



#     # Frame capture and processing
#     run = camera_in.checkbox('Run')
#     FRAME_WINDOW = camera_in.image([])
#     camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#     while run:
#         ret, frame = camera.read()  # Read frame

#         if ret:
#             try:
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color space
#                 faces, m_face, m_right_eye, m_left_eye, m_dominant_emotion = process_frame(frame)
#                 # Draw bounding boxes for detected faces
#                 for face in faces:
#                     x, y, w, h = face["box"]
#                     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#                 FRAME_WINDOW.image(frame, channels="BGR")  # Display the frame
#             except Exception as e:
#                 print(f"Error processing frame: {str(e)}")
#                 st.error(f"Error processing frame: {str(e)}")
#         else:
#             st.error("Failed to capture frame.")

#         if not run:
#             break

#     # Release the webcam when done
#     camera.release()
#     st.write('Engagement recording halted')

#     # Display selected features
#     for selected_option in selected_options:
#         if selected_option == "Eye Tracking":
#             if m_right_eye is not None and m_left_eye is not None:
#                 camera_in.write(f"Co-ordinates for Left eye: {m_left_eye}, Right eye: {m_right_eye}")
#             else:
#                 camera_in.write("Eye tracking data not available.")
#         elif selected_option == "Face Detection":
#             if m_face is not None:
#                 camera_in.write(f"Co-ordinates of Face: {m_face}")
#             else:
#                 camera_in.write("Face detection data not available.")
#         elif selected_option == "Emotion Detection":
#             if m_dominant_emotion is not None:
#                 camera_in.write(f"Dominant Emotion: {m_dominant_emotion}")
#             else:
#                 camera_in.write("Emotion detection data not available.")

#     st.sidebar.success("")

# if __name__ == "__main__":
#     main()

