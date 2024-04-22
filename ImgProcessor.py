from deepface import DeepFace
from retinaface import RetinaFace
import cv2
import numpy as np
from Utilities.ExtractFaceFeatures import *
from Utilities.ExtractEmotion import *

def image_processing(img_file_buffer):
  

  if img_file_buffer is not None:
    # To read image file buffer with OpenCV:

    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    # st.write(type(cv2_img))
    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    # st.write(cv2_img.shape)
    faces = RetinaFace.detect_faces(cv2_img)
    objs = DeepFace.analyze(img_path=cv2_img, actions=['emotion'], detector_backend ="ssd",enforce_detection= False)

    #sending face data to obtain face, right eye and left eye coordinates
    facial, rey, ley = ret_features(faces)

    #sending emotion data to obtain dominant emotion
    dominant = ret_emotion(objs)

    # return faces,objs


    return facial, rey, ley, dominant
    # return score, right_eye, left_eye 