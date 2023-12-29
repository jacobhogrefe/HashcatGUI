'''
A wrapper for the hashcat command line program. All functions relating to hashcat should be implemented in here.

Author: Jacob Hogrefe
'''

import os
import subprocess

# detects the hash provided, and returns the most accurate hashcat mode
def hash_type(hash_value):
    try:
        # run name_that_hash command and captures the first occurance of the "HC:" identifier
        command = f"nth --text '{hash_value}' --accessible | grep -m 1 HC:"
        output = subprocess.check_output(command, shell=True, text=True)
        
        # removes all of the unnecessary characters, giving us just the hashcat mode
        return output.split(":")[1].split(" ")[1].strip()

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

# creates the file the hash will be stored in, as hashcat requires it to be in a text file
def hash_file_path(hash_value):
    # delete the file if it exists
    if os.path.exists('hash.txt'):
        os.remove("hash.txt")

    # create and write to the hash.txt file
    file = open("hash.txt", "x")
    file.write(hash_value)
    file.close()
    return os.path.abspath("hash.txt")

# runs the hashcat command
def run_hashcat(hash, wordlist_path):
    hashcat_command = [
        'hashcat',
        '-a 0',
        '-m', str(hash_type(hash)),
        hash_file_path(hash),
        wordlist_path
    ]
    
    try:
        subprocess.run(hashcat_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")