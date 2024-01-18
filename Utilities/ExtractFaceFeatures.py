# -*- coding: utf-8 -*-
"""ExtractFaceFeatures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1URcr855lZjIu8hxGuNajyRtbSoNjayiO
"""


# feat = {
#     "face_1": {
#         "score": 0.9992000460624695,
#         "facial_area": [
#             (314, 159),
#             (477, 359)
#         ],
#         "landmarks": {
#             "right_eye": (360.0255, 229.04474),
#             "left_eye": (438.3108, 232.38853),
#             "nose": (397.82245, 263.40384),
#             "mouth_right": (364.1267, 305.87646),
#             "mouth_left": (426.67773, 308.17273)
#         }
#     }
# }


# Extracting each feature

def extract_features(face_dict):
    score = face_dict["score"]
    facial_area = [int(coord) for coord in face_dict["facial_area"]]
    right_eye = tuple(float(coord) for coord in face_dict["landmarks"]["right_eye"])
    left_eye = tuple(float(coord) for coord in face_dict["landmarks"]["left_eye"])
    nose = tuple(float(coord) for coord in face_dict["landmarks"]["nose"])
    mouth_right = tuple(float(coord) for coord in face_dict["landmarks"]["mouth_right"])
    mouth_left = tuple(float(coord) for coord in face_dict["landmarks"]["mouth_left"])
    
    return score, facial_area, right_eye, left_eye, nose, mouth_right, mouth_left

def ret_features(face_dict):

        # Process input data and call the function for each face
    for face_name, face_data in face_dict.items():
      # Extracting features and assigning to variables
      (
        score,
        facial_area,
        right_eye,
        left_eye,
        nose,
        mouth_right,
        mouth_left
      ) = extract_features(face_data)
    return facial_area, right_eye, left_eye


# Extracting each feature