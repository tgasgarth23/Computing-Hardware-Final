from feat import Detector
from feat.plotting import imshow
import os


def get_prediction(image_name):
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )

    single_face_img_path = os.path.join(os.getcwd(), image_name)
    return detector.detect_image(single_face_img_path)

def is_satisfied():
    user_emotions = get_prediction("lebronmad.jpg").emotions
    print(user_emotions)

    positive_factor = user_emotions["happiness"] + user_emotions["surprise"]
    negative_factor = user_emotions["anger"] + user_emotions["disgust"] + user_emotions["sadness"]

    return (positive_factor > negative_factor).bool()

if is_satisfied():
    print("User is satisfied by the Val menu options for today!")
else:
    print("User is discontent with the Val menu options for today!")
