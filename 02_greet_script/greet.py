#!/usr/bin/env python3

"""

greet.py

A script that greets the user by name using a command-line argument.
"""

import sys

def main():
    # sys.argv is a list of arguments passed from the command line
    # argv[0] is always the script name
    # argv[1] is the first real argument

    if len(sys.argv) < 2:
        print("Usage: python3 greet.py <name>")
        return
    
    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to Python scripting!")

if __name__ == "__main__":
    main()