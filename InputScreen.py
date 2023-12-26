import customtkinter as ctk
import tkinter as tk
import hashid

class InputScreen:
    frame = None
    attack_mode = tk.IntVar(0)
    hash = None
    dictionary_file_path = None
    
    def __init__(self, root, wid, hei):
        super.__init__()
        self.create_widgets(root, wid, hei)
        
    def create_widgets(self, root, wid, hei):
        global frame
        global attack_mode
        frame = ctk.CTkFrame(master=root, width = wid, height = hei)
        
        hash_text = ctk.CTkLabel(frame, text="Hash Input")
        hash_input
        attack_mode_text = ctk.CTkLabel(frame, text="Attack Mode")

        straight_mode = ctk.CTkRadioButton(master=frame, text="Straight", variable=attack_mode, value=0)
        combination_mode = ctk.CTkRadioButton(master=frame, text="Combination", variable=attack_mode, value=1)
        bruteforce_mode = ctk.CTkRadioButton(master=frame, text="Brute-force", variable=attack_mode, value=3)
        hybrid_mode = ctk.CTkRadioButton(master=frame, text="Hybrid", variable=attack_mode, value=6)
        mode_definitions = ctk.CTkLabel(frame, text="Straight Mode - For dictionary based attacks\nCombination Mode - Combines 2 word lists to create combinations\nBrute-force Mode - Automatically generate all combinations of characters to a specified length\nHybrid Mode - Combination of a dictionary attack and brute-force attack")
    
    def pack_widgets(self):
        frame.pack()
        
    def get_information(self):
        e = 1