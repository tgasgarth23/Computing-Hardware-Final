1. main.py
Description: This is the entry point of the application. It initializes the system, loads the main screen, and handles the primary loop to check for button presses.

2. config.py
Description: Contains configuration settings for the project, such as GPIO pin assignments for buttons, camera settings, file paths for saving data, and any other constants used across the project.

3. menu_display.py
Description: Manages the display screen. It includes functions to display the menu items on the main screen and update the screen (e.g., showing the thank you message).

4. button_handler.py
Description: Handles button interactions. This script listens for button presses and triggers appropriate actions (like switching to camera feed or taking a picture).

5. camera_manager.py
Description: Manages camera operations. This includes initializing the camera, capturing images, and handling any camera-related errors.

6. emotion_detector.py
Description: Contains the logic for facial emotion detection. It processes the captured images to detect if the student is happy or sad.

7. data_manager.py
Description: Handles data storage and retrieval. It saves feedback results along with time and menu item data to a CSV file and ensures proper handling of data formats.

8. utility.py
Description: Includes utility functions used across the project, such as logging, error handling, and any other shared functionalities.

10. test/
Description: A directory containing test scripts for each component (e.g., test_camera_manager.py, test_button_handler.py). These scripts are used to ensure each component is functioning correctly in isolation before integrating them into the main application.

This structure provides a modular approach, making the project more manageable and maintainable. Each script has a clear responsibility, facilitating easier debugging and potential future expansions or modifications.


Create file tree: tree -I 'venv' > contents_tree.txt
