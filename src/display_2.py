import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import utility as utils
from camera_manager import CameraManager
from data_manager import DataManager
from emotion_detector import EmotionDetector

class FullscreenListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fullscreen List Application")

        self.cam = CameraManager()
        self.cam.start()
        self.emotion_analyzer = EmotionDetector()
        self.data_manager = DataManager()

        # Make the window fullscreen
        #self.attributes("-fullscreen", True)
        #self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # Title label with larger font size
        title_font_size = 36
        title_label = tk.Label(self, text="Select a menu item to review!", font=('Arial', title_font_size))
        title_label.pack()

        # List of options
        #options = ['Grilled Chicken', 'White Rice', 'Brown Rice', 'Pasta', 'Alfredo Sauce', 'Marinara Sauce']
        options = utils.get_menu_items()

        # Calculate font size for options
        option_font_size = (self.winfo_screenheight() - title_label.winfo_reqheight()) // len(options) // 2
        option_font_size = min(option_font_size, title_font_size - 4)

        # Create a listbox to display the options
        self.listbox = tk.Listbox(self, font=('Arial', option_font_size), width=50, height=len(options))
        self.listbox.pack(expand=True, fill='both')

        # Add options to the listbox
        for option in options:
            self.listbox.insert(tk.END, option)

        # Bind keyboard events for listbox navigation
        self.bind_listbox_navigation()

        # Feedback screen elements (initially hidden)
        self.feedback_screen = tk.Listbox(self, font=('Arial', option_font_size), width=50, height=2)
        feedback_options = ['Take Picture', 'Cancel Feedback']
        for option in feedback_options:
            self.feedback_screen.insert(tk.END, option)

        # Selected option
        self.selected_option = None


    def bind_listbox_navigation(self):
        self.bind("<Up>", self.navigate_up)
        self.bind("<Down>", self.navigate_down)
        self.bind("<Return>", self.select_option)
        self.bind("<Escape>", lambda event: self.destroy())

    def navigate_up(self, event):
        current_index = self.listbox.curselection()
        if current_index:
            new_index = max(current_index[0] - 1, 0)
            self.listbox.selection_clear(current_index)
            self.listbox.selection_set(new_index)
            self.listbox.activate(new_index)

    def navigate_down(self, event):
        current_index = self.listbox.curselection()
        if current_index:
            new_index = min(current_index[0] + 1, self.listbox.size() - 1)
            self.listbox.selection_clear(current_index)
            self.listbox.selection_set(new_index)
            self.listbox.activate(new_index)
        else:
            self.listbox.selection_set(0)
            self.listbox.activate(0)

    def select_option(self, event):
        if self.feedback_screen.winfo_ismapped():
            self.execute_feedback_option()
        else:
            self.selected_option = self.listbox.get(self.listbox.curselection())
            self.show_feedback_screen()

    def show_feedback_screen(self):
        self.cam.show_preview()
        self.listbox.pack_forget()
        self.feedback_screen.pack(expand=True, fill='both')
        self.bind_feedback_navigation()

    def bind_feedback_navigation(self):
        self.bind("<Up>", lambda event: self.feedback_navigate(-1))
        self.bind("<Down>", lambda event: self.feedback_navigate(1))
        self.bind("<Return>", self.select_feedback_option)
        self.bind("<Escape>", self.return_to_main_screen)

    def feedback_navigate(self, direction):
        current_index = self.feedback_screen.curselection()
        if current_index:
            new_index = max(min(current_index[0] + direction, self.feedback_screen.size() - 1), 0)
            self.feedback_screen.selection_clear(current_index)
            self.feedback_screen.selection_set(new_index)
            self.feedback_screen.activate(new_index)
        else:
            self.feedback_screen.selection_set(0)
            self.feedback_screen.activate(0)

    def select_feedback_option(self, event):
        self.execute_feedback_option()

    def execute_feedback_option(self):
        selected_feedback = self.feedback_screen.get(self.feedback_screen.curselection())
        if selected_feedback == 'Take Picture':
            self.take_picture()
        elif selected_feedback == 'Cancel Feedback':
            self.return_to_main_screen()

    def take_picture(self):
        frame = self.cam.take_image()
        cv2.imshow("Frame", frame)  # Display the frame for debug purposes
        cv2.waitKey(1)
        emotions = self.emotion_analyzer.analyze_image(frame)
        print("Emotions are: ")
        print(emotions)

        print(self.selected_option)
        if emotions != []:
            self.data_manager.save_to_csv(emotions, self.selected_option)
            self.return_to_main_screen()
        else:
            messagebox.showinfo("Information", "Face not recognized. Please try again!")

    def return_to_main_screen(self, event = None):
        self.cam.hide_preview()
        self.feedback_screen.pack_forget()
        self.listbox.pack(expand=True, fill='both')
        self.bind_listbox_navigation()

    def update_webcam_feed(self):
        if self.webcam_label.winfo_ismapped():
            _, frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            self.webcam_label.configure(image=img)
            self.webcam_label.image = img
            self.webcam_label.after(10, self.update_webcam_feed)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.cap.release()
            self.destroy()

# Create and run the application
app = FullscreenListApp()
app.mainloop()
