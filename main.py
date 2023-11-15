from src.camera_manager import CameraManager
from src.data_manager import DataManager
from src.emotion_detector import EmotionDetector
import src.utility as utils
import cv2

cam = CameraManager()
emotion = EmotionDetector()

while True:
    try:
        # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels

        key = cv2.waitKey(1) & 0xFF  # Create a key that will wait for user input and respond based on it

        # if the `q` key was pressed, break from the loop and clean up all windows
        if key == ord("q"):
            del cam
            break
        elif key == ord("t"):
            frame = cam.take_image()
            cv2.imshow("Frame", frame)  # Display the frame for debug purposes
            cv2.imwrite(utils.generate_filename(), frame)
            emotion.is_student_happy()
        else:
            pass

    except KeyboardInterrupt:
        # Do a bit of cleanup
        del cam
