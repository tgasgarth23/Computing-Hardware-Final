from fer import FER
import cv2

emotion_detector = FER(mtcnn=True)

test_img = cv2.imread("images/test_image.png")
analysis = emotion_detector.detect_emotions(test_img)
print(analysis)