import tkinter as tk

class FullscreenListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fullscreen List Application")

        # Make the window fullscreen
        self.attributes("-fullscreen", True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # Title label with larger font size
        title_font_size = 36
        title_label = tk.Label(self, text="Select a menu item to review!", font=('Arial', title_font_size))
        title_label.pack()

        # List of options
        options = ['Grilled Chicken', 'White Rice', 'Brown Rice', 'Pasta', 'Alfredo Sauce', 'Marinara Sauce']

        # Calculate font size for options
        option_font_size = (self.winfo_screenheight() - title_label.winfo_reqheight()) // len(options) // 2
        option_font_size = min(option_font_size, title_font_size - 4)

        # Create a listbox to display the options
        self.listbox = tk.Listbox(self, font=('Arial', option_font_size), width=50, height=len(options))
        self.listbox.pack(expand=True, fill='both')

        # Add options to the listbox
        for option in options:
            self.listbox.insert(tk.END, option)

        # Bind keyboard events
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
        selected_option = self.listbox.get(self.listbox.curselection())
        print(f"Selected: {selected_option}")

# Create and run the application
app = FullscreenListApp()
app.mainloop()
