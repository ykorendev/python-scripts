

#!/usr/bin/env python3

"""
logger_with_time.py

Creates a directory called logs and appends a line to run.log file including timestamps
"""

import sys
import os
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 logger_with_time.py \"your log\"")
        return

    log = " ".join(sys.argv[1:])

    base_dir = os.path.dirname(__file__)
    logs_dir = os.path.join(base_dir, "logs")

    os.makedirs(logs_dir, exist_ok= True)

    logs_file = os.path.join(logs_dir,"run.log")

    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(logs_file, "a") as f:
        f.write(f"{formatted_time} {log}\n")

if __name__ == "__main__":
    main()