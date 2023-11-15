from "src/camera_manager.py" import CameraManager
from "src/data_manager.py" import DataManager
from "src/data_manager.py" import EmotionDetector
import cv2

cam = CameraManager()

while True:
    try:
        # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels

        key = cv2.waitKey(1) & 0xFF  # Create a key that will wait for user input and respond based on it

        # if the `q` key was pressed, break from the loop and clean up all windows
        if key == ord("q"):
            del cam 
            break
        elif key == ord("t"):
            cv2.imshow("Frame", cam.take_image())  # Display the frame for debug purposes
        else:
            pass

    except KeyboardInterrupt:
        # Do a bit of cleanup
        del cam
