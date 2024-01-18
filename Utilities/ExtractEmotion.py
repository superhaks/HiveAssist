#extracting facial emotions and returning the dominant emotion

def extract_emotion_features(face_data):
    emotion_scores = face_data["emotion"]
    dominant_emotion = face_data["dominant_emotion"]
    region_coordinates = face_data["region"]
    face_confidence = face_data["face_confidence"]

    return emotion_scores, dominant_emotion, region_coordinates, face_confidence

def ret_emotion(face_data):
    # Extracting features using the function
    (emotion_score,
    dominant_emotion,
    region_coordinates,
    face_confidence) = extract_emotion_features(face_data[0])

    return dominant_emotion