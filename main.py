from src.camera_manager import CameraManager
from src.data_manager import DataManager
from src.emotion_detector import EmotionDetector
from src.MenuDisplay import FullscreenListApp
import src.utility as utils
import cv2

def main():
    # Create and run the application
    app = MenuDisplay()
    app.mainloop()

if __name__=="__main__":
    main()
    cv2.destroyAllWindows()
