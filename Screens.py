'''
Contains the classes for all of the screens used in the GUI application.

Author: Jacob Hogrefe
'''
import customtkinter as ctk
from tkinter import filedialog
from tkinter import Text
from HashcatWrapper import build_command, hash_type
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
        hash_entry_label.place(relx=0.05, rely=0.05, anchor=ctk.W)

        self.hash_entry_var = ctk.StringVar()
        hash_entry = ctk.CTkEntry(self, textvariable=self.hash_entry_var)
        hash_entry.place(relx=0.05, rely=0.125, anchor=ctk.W)

        # button to choose the wordlist
        wordlist_file_button = ctk.CTkButton(self, text="Wordlist File", command=self.choose_file)
        wordlist_file_button.place(relx=0.05, rely=0.2, anchor=ctk.W)

        # display the wordlist path
        self.wordlist_file_label = ctk.CTkLabel(self, text="")
        self.wordlist_file_label.place(relx=0.05, rely=0.275, anchor=ctk.W)

        # next button
        next_button = ctk.CTkButton(self, text="Next", command=self.next_screen)
        next_button.place(relx=0.85, rely=0.9, anchor=ctk.CENTER)
        
        # error label for user input
        self.error_label = ctk.CTkLabel(self, text="")
        self.error_label.place(relx=0.05, rely=0.87)

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.wordlist_file_label.configure(text=f"Wordlist File: {file_path}")

    def next_screen(self):
        # pass user input and file path to the next screen
        user_hash = self.hash_entry_var.get()
        wordlist_path = self.wordlist_file_label.cget("text").replace("Wordlist File: ", "")
        
        # check if user provides a hash and wordlist
        if user_hash and wordlist_path:
            # check if the hash entered can be identified by the program
            if hash_type(user_hash) == None:
                self.error_label.configure(text="Hash could not be identified")
            else:
                self.master.show_screen(ResultScreen, user_hash=user_hash, wordlist_path=wordlist_path)
        else:
            # display warning message that both fields need to be filled out
            self.error_label.configure(text="Please enter a hash and choose a wordlist file.")

# screen for displaying the output of hashcat, and showing the result after cracking        
class ResultScreen(ctk.CTkFrame):
    def __init__(self, master=None, user_hash="", wordlist_path="", **kwargs):
        super().__init__(master, **kwargs)
        self.user_hash = user_hash
        self.wordlist_path = wordlist_path
        self.create_widgets()
    
    def create_widgets(self):
        self.output_text = Text(self, height=30, width=100, state=ctk.DISABLED)
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
        output = []
        
        try:
            # capture its output of the subprocess
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            # check for new output
            while True:
                output_line = process.stdout.readline()
                if not output_line:
                    break
                self.update_output(output_line.strip())
                if output_line.strip():
                    output.append(output_line.strip())

            # wait for the process to complete
            process.wait()
            for i in output:
                print(i)
                
            if output and "Stopped" in output[-1]:
                result_label = ctk.CTkLabel(self, text='', width=40)
                hash_result = None
                result = output[len(output) - 20].replace("Status...........: ", "").strip()
                if result == "Exhausted":
                    result_label.configure(text=f"No match found")
                elif result == "Cracked":
                    hash_result = output[len(output) - 22].split(":")[1]
                
                result_label.configure(text=f"Result: {hash_result}")
                result_label.place(relx=0.625, rely=0.88)

        except Exception as e:
            self.update_output(f"Error: {e}")
            print(f"Error: {e}")

    def update_output(self, text):
        # append the new text to the text widget
        self.output_text.config(state=ctk.NORMAL)
        self.output_text.insert(ctk.END, text + "\n")
        self.output_text.config(state=ctk.DISABLED)
        # show newest output
        self.output_text.see(ctk.END)
        # update event loop
        self.update_idletasks()