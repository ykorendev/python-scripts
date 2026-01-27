

#!/usr/bin/env python3

"""
note.py

Take a command-line argument and append it to notes.txt file
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 note.py <text>")
        return
    
    note = sys.argv[1]

    base_dir = os.path.dirname(__file__)
    notes_file = os.path.join(base_dir,"notes.txt")

    
    with open("note.txt", "a") as f:
        f.write(note + "\n")

if __name__ == "__main__":
    main()
