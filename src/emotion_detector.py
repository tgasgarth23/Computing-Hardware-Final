from tensorflow.keras.models import model_from_json
from tensorflow.python.keras.backend import set_session # not sure if needed
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt

class EmotionDetector:
    
    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]
    
    def __init__(self):
        with open("model.json", "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
        self.loaded_model.load_weights("model_weights.h5")
        
        self.config = tf.compat.v1.ConfigProto()
        self.config.gpu_options.per_process_gpu_memory_fraction = 0.15
        global session
        session = tf.compat.v1.Session(config=self.config)
        set_session(session)
        self.facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        print("Emotion detector initialization complete!\n")
        
    def get_emotion(self, img):
        set_session(session)
        self.preds = self.loaded_model.predict(img)
        print(self.preds)
        return EmotionDetector.EMOTIONS_LIST[np.argmax(self.preds)]
        
    def get_path(self, image_path):
        cwd = os.getcwd()
        idx = cwd.rindex("/")
        return cwd[:idx+1] + image_path
        
    def is_face_happy(self, img, factorize=True):
        emotion = self.get_emotion(img)
        print(emotion)
        if not factorize:
            return True if emotion == "Neutral" or emotion == "Surprise" or emotion == "Happy" else False
            
        preds = self.preds[0]
        positive_factor = preds[3] + preds[4] + preds[6]
        negative_factor = preds[0] + preds[1] + preds[2] + preds[5]
        
        return positive_factor > negative_factor
    
    
    def analyze_image(self, img):
        print("analyzing image")
        gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.facec.detectMultiScale(gray_fr, 1.3, 5)
        print(faces)
        
        for (x, y, w, h) in faces:
            print("face detected")
            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            roi = roi[np.newaxis, :, :, np.newaxis]
            plt.imshow(roi[0])
            plt.show()
            print(self.is_face_happy(roi))
            
    def analyze_image_file(self, image_path):
        #path = self.get_path(image_path)
        img = cv2.imread(image_path)
        self.analyze_image(img)

            

if __name__ == '__main__':
    detector = EmotionDetector()
    happy_test = detector.analyze_image_file("/home/ryantrevor/Computing-Hardware-Final/test/data/images/TRUE_0.png")
    sad_test = detector.analyze_image_file("/home/ryantrevor/Computing-Hardware-Final/test/data/images/FALSE_2.jpg")
    '''
    if happy_test:
        print('Happy Student PASS')
    else:
        print('Happy Student FAIL')
    if sad_test:
        print('Sad Test FAIL')
    else:
        print('Sad Test PASS')
    '''
