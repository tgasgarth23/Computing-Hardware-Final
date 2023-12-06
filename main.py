from src.camera_manager import CameraManager
from src.data_manager import DataManager
from src.emotion_detector import EmotionDetector
import src.utility as utils
import cv2
import keyboard


def main():
    menu = utils.get_menu_items()
    selected_item = 0
    cam = CameraManager()
    emotion_analyzer = EmotionDetector()
    data_manager = DataManager()
    # Validating the user input

    # while not 1 <= selected_item <= len(menu):
    while(True):
        menu = utils.get_menu_items()
        get_camera = False

        # Printing the list of options
        print("Please select a menu item to review:")
        for i, option in enumerate(menu, 1):
            print(f"{i}. {option}")

        # Getting user input with validation for integer input
        try:
            selected_item = int(input("Enter the number of your choice: "))
            if selected_item > len(menu) or selected_item < 1:
                print("Invalid selection. Please try again.")
                selected_item = 0  # Resetting to ensure loop continues
            else:
                get_camera = True
        except ValueError:
            print("Invalid input. Please enter a number.")

        done = False
        while(not done and get_camera):
            done = camera_analysis(menu[selected_item-1], cam, emotion_analyzer, data_manager)
    

def camera_analysis(menu_item, cam, emotion_analyzer, data_manager):
    print(f"To review {menu_item} by taking a picture of your face, press 't'.\nTo cancel the review, press 'q'.")
    while True:
        try:
            # Grab the frame from the threaded video stream and resize it to have a maximum width of 400 pixels
            
            #key = cv2.waitKey(1) & 0xFF  # Create a key that will wait for user input and respond based on it
            # if the `q` key was pressed, break from the loop and clean up all windows
            if keyboard.is_pressed('q'):
                print("quit")
                # del cam
                return True
            elif keyboard.is_pressed('t'):
                frame = cam.take_image()
                cv2.imshow("Frame", frame)  # Display the frame for debug purposes
                cv2.waitKey(1)
                #cv2.imwrite(utils.generate_filename(), frame)
                emotions = emotion_analyzer.analyze_image(frame)
                data_manager.save_to_csv(emotions, menu_item)
                print(f"Thank you for your review of {menu_item}!\nEmotion analysis of your picture:\t{emotions}")
                cv2.destroyAllWindows()  # Close the window showing the frame
                # del cam
                return True
            else:
                pass

        except KeyboardInterrupt:
            print("error")
            # Do a bit of cleanup
            # del cam
            
if __name__=="__main__":
    main()
    cv2.destroyAllWindows()
