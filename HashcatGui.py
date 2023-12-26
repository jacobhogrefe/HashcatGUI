'''
This is a simple Hashcat GUI wrapper to make it easier to crack hashes without fussing with a command line.

Author: Jacob Hogrefe
'''

import os
import subprocess as sp
import customtkinter as ctk
import tkinter as tk
import hashid
import regex as r

'''
Returns the output from a command as a list spit by a regular expression.

Author: Jacob Hogrefe
'''
def get_split_subprocess_output(cmd, rex):
    # gets the output from a ran command
    output = sp.check_output(cmd)
    # encode from a byte stream
    output.encode("UTF-8")
    return r.split(rex, output)

'''
Returns the hash mode for hashcat to function in.

Author: Jacob Hogrefe
'''
def get_hash_mode(hash):
    id = hashid.HashID()
    return list(id.identifyHash(hash))

# variable and app initialization
WIDTH, HEIGHT = 720, 480
attack_mode = 0
hash_type = 0
hahs_mode = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry(str(WIDTH) + "x" + str(HEIGHT))
app.title("Hashcat GUI")

# screen intializations
info_screen = ctk.CTkFrame(master=app, width=WIDTH, height=HEIGHT)
status_screen = ctk.CTkFrame(master=app, width=WIDTH, height=HEIGHT)
result_screen = ctk.CTkFrame(master=app, width=WIDTH, height=HEIGHT)

'''
Widget additions to each screen
'''
#info screen
hash_text = ctk.CTkLabel(info_screen, text="Hash Input")
hash_input
attack_mode_text = ctk.CTkLabel(info_screen, text="Attack Mode")

straight_mode
combination_mode
bruteforce_mode
hybrid_mode
mode_definitions = ctk.CTkLabel(info_screen, text="Straight Mode - For dictionary based attacks\nCombination Mode - Combines 2 word lists to create combinations\nBrute-force Mode - Automatically generate all combinations of characters to a specified length\nHybrid Mode - Combination of a dictionary attack and brute-force attack")

#status screen
result_text
passwords_tried_text
percentage_text
est_time_text

#result screen





'''
make gui
get information from user input
assemble command
add frame for hash cracker
'''
# hashcat -a 0 HASHFILENAME PASSWORD LIST -m HASHTYPE
identifier = hashid.HashID()

print(identifier.identifyHash("7196759210defdc0"))

results = list(identifier.identifyHash("7196759210defdc0"))

if results:
    hash_type, hash_algorithm = results[0], results[1]
    print(f"The hash type is: {hash_type}")
    print(f"The hash algorithm is: {hash_algorithm}")
else:
    print("Unknown hash type.")