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
    objs = DeepFace.analyze(img_path=cv2_img, actions=['emotion'], detector_backend ="ssd")

    #sending face data to obtain face, right eye and left eye coordinates
    facial, rey, ley = ret_features(faces)

    #sending emotion data to obtain dominant emotion
    dominant = ret_emotion(objs)


    return facial, rey, ley, dominant
    # return score, right_eye, left_eye 



"""
{
  "face_1": {
    "score": 0.9996453523635864,
    "facial_area": [
      "733",
      "231",
      "877",
      "429"
    ],
    "landmarks": {
      "right_eye": [
        "765.075",
        "315.18317"
      ],
      "left_eye": [
        "832.6366",
        "322.10587"
      ],
      "nose": [
        "790.1954",
        "364.83276"
      ],
      "mouth_right": [
        "767.6766",
        "385.28873"
      ],
      "mouth_left": [
        "819.5719",
        "391.56567"
      ]
    }
  },
  "face_2": {
    "score": 0.9995046854019165,
    "facial_area": [
      "190",
      "141",
      "344",
      "316"
    ],
    "landmarks": {
      "right_eye": [
        "254.0806",
        "214.20403"
      ],
      "left_eye": [
        "320.90222",
        "210.33327"
      ],
      "nose": [
        "300.8719",
        "251.65591"
      ],
      "mouth_right": [
        "263.72058",
        "281.43613"
      ],
      "mouth_left": [
        "311.3579",
        "278.669"
      ]
    }
  }
}


[
  {
    "emotion": {
      "angry": 0.5335289814586661,
      "disgust": 0.00028905909595091197,
      "fear": 6.378231927367219,
      "happy": 8.924463072483173,
      "sad": 0.7254886507405459,
      "surprise": 0.009497332535070773,
      "neutral": 83.42849809783719
    },
    "dominant_emotion": "neutral",
    "region": {
      "x": 710,
      "y": 255,
      "w": 173,
      "h": 173
    },
    "face_confidence": 2.3007331315311603
  }
]
"""


def value_Extractor(faces, objs):
  return faces, objs