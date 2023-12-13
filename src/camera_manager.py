from picamera2 import Picamera2, Preview
from libcamera import Transform
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage import data, io
import cv2
import imutils
from .emotion_detector import EmotionDetector
import multiprocessing

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = EmotionDetector()
font = cv2.FONT_HERSHEY_SIMPLEX

class CameraManager(multiprocessing.Process):
    def __init__(self):

        super().__init__()
        self.__cam = Picamera2()

        #CONFIGURE CAMERA
        self.__cam.preview_configuration.main.size=(1280,720)
        self.__cam.preview_configuration.align()
        self.__cam.configure("preview")
        self.__cam.annotate_text = "Testing testing 123"

    def show_preview(self):
        self.__cam.start(show_preview=True)

    def hide_preview(self):
        self.__cam.stop_preview()

    def __del__(self):
        cv2.destroyAllWindows()
        self.__cam.stop_preview()

    def take_image(self):
        frame = self.__cam.capture_array()
        return frame
