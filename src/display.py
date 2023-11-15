import tkinter as tk
from tkinter import ttk
from datetime import datetime
from data_manager import DataManager
from camera_manager import CameraManager

class Display:
    def __init__(self, camera_manager: CameraManager, data_manager: DataManager, menu_options):
        self.menu_options = menu_options
        self.camera_manager = camera_manager
        self.data_manager = data_manager
        self.camera_frame = None
        self.menu_frame = None
        self.initilize_root()
        self.bind_keys()
        self.initialize_menu_screen()
        self.root.mainloop()
    
    def initilize_root(self):
        self.root = tk.Tk()
        self.root.title("Review Display")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.attributes('-fullscreen', True)

    def bind_keys(self):
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Return>", self.select_option)

    def move_up(self, event):
        if self.menu_listbox.curselection():
            index = self.menu_listbox.curselection()[0]
            if index > 0:
                self.menu_listbox.select_clear(index)
                self.menu_listbox.select_set(index - 1)
                self.menu_listbox.activate(index - 1)

    def move_down(self, event):
        if self.menu_listbox.curselection():
            index = self.menu_listbox.curselection()[0]
            if index < len(self.menu_options) - 1:
                self.menu_listbox.select_clear(index)
                self.menu_listbox.select_set(index + 1)
                self.menu_listbox.activate(index + 1)
        else:
            self.menu_listbox.select_set(0)

    def select_option(self, event):
        self.handle_selection()

    def initialize_menu_screen(self):
        if self.camera_frame is not None:
            self.camera_frame.pack_forget()

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack_forget()

        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        self.menu_listbox = tk.Listbox(self.menu_frame, height=5)
        for item in self.menu_options:
            self.menu_listbox.insert(tk.END, item)
        self.menu_listbox.pack(padx=10, pady=10)

        self.select_button = tk.Button(self.menu_frame, text='Select', command=self.handle_selection)
        self.select_button.pack(pady=10)

    def handle_selection(self):
        selection = self.menu_listbox.curselection()
        if selection:
            selected_option = self.menu_options[selection[0]]
            self.initialize_camera_screen(selected_option)
            print(f'Selected Option: {selected_option}')

    def initialize_camera_screen(self, selected_option):
        # Clear the current frame
        self.menu_frame.pack_forget()

        self.camera_frame = tk.Frame(self.root)
        self.camera_frame.pack(fill=tk.BOTH, expand=True)

        # Live feed display (placeholder label)
        self.live_feed_label = tk.Label(self.camera_frame, text="Live Camera Feed Here")
        self.live_feed_label.pack(padx=10, pady=10)

        # Button to take a picture
        self.capture_button = tk.Button(self.camera_frame, text='Take Picture', command=self.take_picture(selected_option))
        self.capture_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Cancel button
        self.cancel_button = tk.Button(self.camera_frame, text='Cancel', command=self.cancel_camera)
        self.cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def take_picture(self, selected_option):
        # Code to capture the picture using the camera manager
        picture = self.camera_frame.take_image()
        name = datetime.now()
        file_path = f'data/images/{name}'
        self.camera_manager.save_image(picture, file_path)

        self.data_manager.process_data(
            image_path=file_path,
            time_info = name,
            menu_item=selected_option
        )

        self.initialize_menu_screen()

    def cancel_camera(self):
        self.camera_frame.pack_forget()
        self.initialize_menu_screen()

if __name__ == '__main__':
    camera_manager = None
    menu_options = ['Option 1', 'Option 2', 'Option 3']
    app = Display(camera_manager, menu_options)
