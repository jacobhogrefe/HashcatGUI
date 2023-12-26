import customtkinter as ctk

class ResultScreen:
    frame = None
    
    def __init__(self, root, wid, hei):
        super.__init__()
        self.create_widgets(root, wid, hei)
        
    def create_widgets(root, wid, hei):
        global frame
        frame = ctk.CTkFrame(master=root, width = wid, height = hei)
    
    
    def pack_widgets(self):
        frame.pack()