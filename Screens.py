'''
Contains the classes for all of the screens used in the GUI application.

Author: Jacob Hogrefe
'''
import customtkinter as ctk
from tkinter import filedialog
from tkinter import Text
from HashcatWrapper import build_command
import threading
import subprocess

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
            self.wordlist_file_label.configure(text=f"Wordlist File: {file_path}")

    def next_screen(self):
        # pass user input and file path to the next screen
        user_hash = self.hash_entry_var.get()
        wordlist_path = self.wordlist_file_label.cget("text").replace("Wordlist File: ", "")
        if user_hash and wordlist_path:
            self.master.show_screen(ResultScreen, user_hash=user_hash, wordlist_path=wordlist_path)
        else:
            # display warning message that both fields need to be filled out
            feedback_label = ctk.CTkLabel(self, text="Please enter a hash and choose a wordlist file.")
            feedback_label.pack(pady=5)

# screen for displaying the output of hashcat, and showing the result after cracking        
class ResultScreen(ctk.CTkFrame):
    def __init__(self, master=None, user_hash="", wordlist_path="", **kwargs):
        super().__init__(master, **kwargs)
        self.user_hash = user_hash
        self.wordlist_path = wordlist_path
        self.create_widgets()
    
    def create_widgets(self):
        self.output_text = Text(self, height=30, width=100)
        self.output_text.pack(pady=10)

        start_button = ctk.CTkButton(self, text="Start hashcat", command=self.start_process)
        start_button.pack(pady=5)

    def start_process(self):
        # clear text
        self.output_text.delete("1.0", ctk.END)
        
        # start the subprocess in a separate thread
        threading.Thread(target=self.run_subprocess, daemon=True).start()

    def run_subprocess(self):
        command = build_command(self.user_hash, self.wordlist_path)
        
        try:
            # capture its output of the subprocess
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            # Periodically check for new output
            while True:
                output_line = process.stdout.readline()
                if not output_line:
                    break  # No more output
                self.update_output(output_line.strip())

            # wait for the process to complete
            process.wait()

        except Exception as e:
            self.update_output(f"Error: {e}")

    def update_output(self, text):
        # append the new text to the text widget
        self.output_text.insert(ctk.END, text + "\n")
        # show newest output
        self.output_text.see(ctk.END)
        # update event loop
        self.update_idletasks()