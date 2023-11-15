1. main.py
Description: This is the entry point of the application. It initializes the system, loads the main screen, and handles the primary loop to check for button presses.

2. config.py
Description: Contains configuration settings for the project, such as GPIO pin assignments for buttons, camera settings, file paths for saving data, and any other constants used across the project.

3. menu_display.py
Description: Manages the display screen. It includes functions to display the menu items on the main screen and update the screen (e.g., showing the thank you message).

4. camera_manager.py
Description: Manages camera operations. This includes initializing the camera, capturing images, and handling any camera-related errors.

5. emotion_detector.py
    Constructor (__init__(self)):
        Initializes EmotionDetector with specific models for face, landmark, action units (AU), emotion, and facepose.
        Inputs: None.
        Returns: None.
        detect_emotions(self, image_path) Method:
    
    detect_emotions(self, image_path) Method:
        Detects emotions in a given image.
        Inputs: image_path (str) - Path to the image.
        Returns: Emotion detection results.
        is_student_happy(self, image_name) Method:

    is_student_happy(self, image_name) Method:
        Determines if the student in an image is happy.
        Inputs: image_path (str) - Image file path.
        Returns: Boolean - True if happy, False otherwise.

6. data_manager.py
    Constructor:
        params: EmotionDetector, csv_path
    
    process_data:
        params: time_info, menu_item, emotion, image_path
        saves info to csv

7. utility.py
    delete_all_images:
        params: directory path
        deletes all files in a directory

8. test/


Create file tree: tree -I 'venv' > contents_tree.txt
