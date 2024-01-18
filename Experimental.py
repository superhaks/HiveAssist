import cv2
import streamlit as st
import numpy as np

# def main():
#     st.title("Webcam Input in Streamlit")

    # Open a connection to the webcam
cap = cv2.VideoCapture(0)
st.title("Exp")
frame_placeholder = st.empty
stop_button = st.button("Stop")

while cap.isOpened() and not stop_button:
    ret, frame = cap.read()

    if not ret: 
        st.write ("The video has ended.")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame,channels = "RGB")

    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button:
        break

cap.release()
cv2.destroyAllWindows   


#     if not cap.isOpened():
#         st.error("Error: Unable to access the webcam.")
#         return

#     st.success("Camera is ready! You can see the video stream below.")

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             st.error("Error: Failed to capture frame.")
#             break

#         # Display the webcam feed in Streamlit
#         st.image(frame, channels="BGR")

#     # Release the webcam when the app is closed
#     cap.release()

# if __name__ == "__main__":
#     main()
