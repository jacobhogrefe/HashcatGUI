'''
The GUI application.

Author: Jacob Hogrefe
'''
import customtkinter as ctk
from Screens import InputScreen, ResultScreen

WIDTH, HEIGHT = 720, 480

class HashcatGUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hashcat GUI")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.current_screen = None
        self.show_screen(InputScreen)
        
    def show_screen(self, screen_class, **kwargs):
        new_screen = screen_class(self, **kwargs)
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = new_screen
        self.current_screen.pack(fill=ctk.BOTH, expand=True)

app = HashcatGUI()
app.mainloop()    