import streamlit as st
import cv2 
import numpy as np
import camera_input_live 

# setting up the page icon
st.set_page_config(
    page_title = "HiveAssist",
    page_icon = ":honeybee:"
)

# providing title for the page
st.title("Dashboard")

# adding sidebar to the page
st.sidebar.success("Select a page above.")

#img_file_buffer = 
#st.camera_input("Webcam",key="Web",label_visibility="collapsed")

st.title("Webcam Live Feed")
run = True
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

#image = camera_input_live()

# if image is not None:
#     st.image()
#     bytes_data = image.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

# if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

 