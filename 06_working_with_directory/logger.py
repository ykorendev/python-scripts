

#!/usr/bin/env python3

"""
logger.py

Creates a directory called logs and appends a line to run.log file
"""

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 logger.py \"your log\"")
        return

    log = " ".join(sys.argv[1:])

    base_dir = os.path.dirname(__file__)
    logs_dir = os.path.join(base_dir, "logs")

    os.makedirs(logs_dir, exist_ok= True)

    logs_file = os.path.join(logs_dir,"run.log")

    with open(logs_file, "a") as f:
        f.write(log  + "\n")

if __name__ == "__main__":
    main()