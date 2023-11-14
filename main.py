

from feat import Detector

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='xgb',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)

from feat.utils.io import get_test_data_path
from feat.plotting import imshow
import os

# Helper to point to the test data folder
test_data_dir = get_test_data_path()

# Get the full path
single_face_img_path = os.path.join(os.getcwd(), "lebron.png")

# Plot it
imshow(single_face_img_path)

single_face_prediction = detector.detect_image(single_face_img_path)

print(single_face_prediction.emotions)


def is_satisfied():
    return False