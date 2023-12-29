'''
Contains the classes for all of the screens used in the GUI application.

Author: Jacob Hogrefe
'''
import customtkinter as ctk
from tkinter import filedialog

# screen for putting in the given hash and selecting the path for the wordlist
class InputScreen(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()
    
    def create_widgets(self):
        # user input for given hash
        hash_entry_label = ctk.CTkLabel(self, text="Enter the hash you want to crack:")
        hash_entry_label.pack(pady=5)

        self.hash_entry_var = ctk.StringVar()
        hash_entry = ctk.CTkEntry(self, textvariable=self.hash_entry_var)
        hash_entry.pack(pady=5)

        # button to choose the wordlist
        wordlist_file_button = ctk.CTkButton(self, text="Wordlist File", command=self.choose_file)
        wordlist_file_button.pack(pady=10)

        # display the wordlist path
        self.wordlist_file_label = ctk.CTkLabel(self, text="")
        self.wordlist_file_label.pack(pady=5)

        # next button
        next_button = ctk.CTkButton(self, text="Next", command=self.next_screen)
        next_button.pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_label.config(text=f"Wordlist File: {file_path}")

    def next_screen(self):
        # pass user input and file path to the next screen
        user_hash = self.hash_entry_var.get()
        wordlist_path = self.wordlist_file_label.cget("text").replace("Chosen File: ", "")
        self.master.show_screen(ResultScreen, user_hash=user_hash, wordlist_path=wordlist_path)

# screen for displaying the output of hashcat, and showing the result after cracking        
class ResultScreen(ctk.CTkFrame):
    def __init__(self, master=None, user_hash="", wordlist_path="", **kwargs):
        super().__init__(master, **kwargs)
        self.user_hash = user_hash
        self.wordlist_path = wordlist_path
        self.create_widgets()
    
    def create_widgets(self):
        finish_button = ctk.CTkButton(self, text="Finish", command=self.finish)
        finish_button.pack(pady=10)

    def finish(self):
        # Add any actions or cleanup needed before exiting the application
        self.master.destroy()