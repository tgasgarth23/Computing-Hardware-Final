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
            if keyboard.is_pressed('q'):
                print("Application quitting!")
                del cam
                break
            elif keyboard.is_pressed('t'):
                print("Taking a picture...")
                frame = cam.take_image()
                cv2.imshow("Frame", frame)  # Display the frame for debug purposes
                cv2.waitKey(1)
                #cv2.imwrite(utils.generate_filename(), frame)
                emotion.analyze_image(frame)
                print("Picture taken successfully!")
            else:
                pass

        except KeyboardInterrupt:
            del cam
            
if __name__=="__main__":
    main()
    cv2.destroyAllWindows()
