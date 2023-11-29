from picamera2 import Picamera2, Preview
from libcamera import Transform
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage import data, io
import cv2
import imutils
from .emotion_detector import EmotionDetector

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = EmotionDetector()
font = cv2.FONT_HERSHEY_SIMPLEX

class CameraManager:
    def __init__(self):
        
        #TODO: configure camera to have better lighting
            
        self.cam = Picamera2()

        #CONFIGURE CAMERA
        self.cam.preview_configuration.main.size=(1280,720)
        #self.cam.preview_configuration.main.format="RGB888"
        self.cam.preview_configuration.align()
        self.cam.configure("preview")
        #self.cam.start_preview(Preview.QTGL, x=100, y=200, width=800, height=800, transform=Transform(hflip=1))
        self.cam.annotate_text = "Testing testing 123"
        self.cam.start(show_preview=True)

    def __del__(self):
        cv2.destroyAllWindows()
        self.cam.stop_preview()

    def __image_preprocess(self, im_orig):
        print("Filler")
        '''
        im_gray = rgb2gray(im_orig)  # Convert the original image to a grayscale image
        gray_fr = cv2.cvtColor(im_orig, cv2.COLOR_BGR2GRAY)
        
        img_gray_u8 = img_as_ubyte(
            im_gray)  # Convert greyscale image to an 8-bit unsigned integer so each pixel value ranges from 0-255
        '''
        im_gray = rgb2gray(im_orig)  # Convert the original image to a grayscale image
        gray_fr = cv2.cvtColor(im_orig, cv2.COLOR_BGR2GRAY)
        
        img_gray_u8 = img_as_ubyte(
            im_gray)  # Convert greyscale image to an 8-bit unsigned integer so each pixel value ranges from 0-255

        # Convert grayscale image to binary (black/white) using Otsu's thresholding method
        (thresh, im_bw) = cv2.threshold(img_gray_u8, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Standardize the size of the image by resizing it using OpenCV to 28x28 pixels
        img_resized = cv2.resize(im_gray, (48, 48))

        # Invert the image to effectively reverse the black-and-white colors
        img_gray_invert = 255 - img_resized

        # Reshape the inverted image into a 4-D NumPy array in order to conform to the expected input of the model
        img_final = img_gray_invert.reshape(1, 28, 28, 1)
        return img_resized
        '''
        # Convert grayscale image to binary (black/white) using Otsu's thresholding method
        (thresh, im_bw) = cv2.threshold(img_gray_u8, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Standardize the size of the image by resizing it using OpenCV to 28x28 pixels
        img_resized = cv2.resize(im_gray, (48, 48))

        # Invert the image to effectively reverse the black-and-white colors
        img_gray_invert = 255 - img_resized

        # Reshape the inverted image into a 4-D NumPy array in order to conform to the expected input of the model
        img_final = img_gray_invert.reshape(1, 28, 28, 1)
        return img_resized
        '''
        
    def take_image(self):
        frame = self.cam.capture_array()
        #frame = self.__image_preprocess(frame)
        return frame
