from src.camera_manager import CameraManager
from src.data_manager import DataManager
from src.emotion_detector import EmotionDetector
from display import Display
import src.utility as utils
import cv2
from datetime import datetime


csv_path = 'data/csv/'
menu = utils.get_menu()
cam = CameraManager()
emotion = EmotionDetector()
data_manager = DataManager(emotion, csv_path)


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
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
            image_name = utils.generate_filename(timestamp)
            image_path = f'data/images/{image_name}'
            cam.save_image(frame, image_path)

            menu_item = input()
            data_manager.process_data(image_path, timestamp, menu_item)
            
        
        else:
            pass

    except KeyboardInterrupt:
        # Do a bit of cleanup
        del cam