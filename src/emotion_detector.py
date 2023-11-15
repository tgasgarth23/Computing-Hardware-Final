from feat import Detector

class EmotionDetector:
    def __init__(self):
        self.detector = Detector(
            face_model="retinaface",
            landmark_model="mobilefacenet",
            au_model='xgb',
            emotion_model="resmasknet",
            facepose_model="img2pose",
        )

    def detect_emotions(self, image_path):
        return self.detector.detect_image(image_path)

    def is_student_happy(self, image_path):
        user_emotions = self.detect_emotions(image_path).emotions

        positive_factor = user_emotions["happiness"] + user_emotions["surprise"]
        negative_factor = user_emotions["anger"] + user_emotions["disgust"] + user_emotions["sadness"]

        return (positive_factor > negative_factor).bool()

if __name__ == '__main__':
    detector = EmotionDetector()
    happy_test = detector.is_student_happy('test/data/images/TRUE_0.png')
    sad_test = detector.is_student_happy('test/data/images/FALSE_0.jpg')
    if happy_test:
        print('Happy Student PASS')
    else:
        print('Happy Student FAIL')
    if sad_test:
        print('Sad Test FAIL')
    else:
        print('Sad Test PASS')