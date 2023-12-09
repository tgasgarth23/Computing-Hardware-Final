from src.MenuDisplay import MenuDisplay
import src.utility as utils
import cv2

def main():
    # Create and run the application
    app = MenuDisplay()
    app.mainloop()

if __name__=="__main__":
    main()
    cv2.destroyAllWindows()
