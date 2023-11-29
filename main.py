from src.camera_manager import CameraManager
from src.data_manager import DataManager
from src.emotion_detector import EmotionDetector
import src.utility as utils
import cv2
import keyboard




def main():
    cam = CameraManager()
    emotion = EmotionDetector()
    print("Camera and Emotion Modules Initialized!")


    while True:
        try:
            # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
            
            #key = cv2.waitKey(1) & 0xFF  # Create a key that will wait for user input and respond based on it
            # if the `q` key was pressed, break from the loop and clean up all windows
            if keyboard.is_pressed('q'):
                print("quit")
                del cam
                break
            elif keyboard.is_pressed('t'):
                print("taking pic")
                frame = cam.take_image()
                cv2.imshow("Frame", frame)  # Display the frame for debug purposes
                cv2.waitKey(1)
                #cv2.imwrite(utils.generate_filename(), frame)
                emotion.analyze_image(frame)
                print("pic taken")
            else:
                pass

        except KeyboardInterrupt:
            # Do a bit of cleanup
            del cam
            
if __name__=="__main__":
    main()
    cv2.destroyAllWindows()
