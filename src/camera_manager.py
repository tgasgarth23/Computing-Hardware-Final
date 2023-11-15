from picamera2 import Picamera2
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage import data, io
import cv2
import imutils
import os

class CameraManager:
    def __init__(self):
        self.cam = Picamera2()

        #CONFIGURE CAMERA
        self.cam.preview_configuration.main.size=(1280,720)
        self.cam.preview_configuration.main.format="RGB888"
        self.cam.preview_configuration.align()
        self.cam.configure("preview")
        self.cam.start()

    def __del__(self):
        cv2.destroyAllWindows()

    # ImagePreProcess: Function defined to handle the pre-processing of the image captured to prepare it as model input.
    def __image_preprocess(self, im_orig):
        im_gray = rgb2gray(im_orig)  # Convert the original image to a grayscale image
        img_gray_u8 = img_as_ubyte(
            im_gray)  # Convert greyscale image to an 8-bit unsigned integer so each pixel value ranges from 0-255

        # Convert grayscale image to binary (black/white) using Otsu's thresholding method
        (thresh, im_bw) = cv2.threshold(img_gray_u8, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Standardize the size of the image by resizing it using OpenCV to 28x28 pixels
        img_resized = cv2.resize(im_bw, (28, 28))

        # Invert the image to effectively reverse the black-and-white colors
        img_gray_invert = 255 - img_resized

        # Reshape the inverted image into a 4-D NumPy array in order to conform to the expected input of the model
        img_final = img_gray_invert.reshape(1, 28, 28, 1)
        return img_final

    def take_image(self):
        frame = self.cam.capture_array()
        frame = imutils.resize(frame, width=400)
        frame = self.__image_preprocess(frame)
        return frame
    

    def save_image(self, frame, file_path):
        """
        Saves the given frame to the specified file path.

        :param frame: The image frame to be saved.
        :param file_path: The path where the image will be saved.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save the image
        cv2.imwrite(file_path, frame)