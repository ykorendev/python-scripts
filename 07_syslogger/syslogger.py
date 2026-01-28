

#!/usr/bin/env python3

"""
logger.py

Runs a system command and logs its output with a timestamp.
"""

import sys
import os
import subprocess
from datetime import datetime


def main():
    # Choose command
    if len(sys.argv) > 1:
        command = (" ".join(sys.argv[1:])).split()
    
    else:
        command = ["uname", "-a"]
    
    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log directory from env
    base_dir = os.path.dirname(__file__)
    log_dir_name = os.environ.get("LOG_DIR", "logs")
    logs_dir = os.path.join(base_dir, log_dir_name)
    os.makedirs(logs_dir, exist_ok=True)

    logs_file = os.path.join(logs_dir, "system.log")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip() or "[NO OUTPUT]"
    except FileNotFoundError as e:
        output = f"COMMAND FAILED: {e.filename} ({e.strerror})"

    except subprocess.CalledProcessError as e:
        output = f"COMMAND FAILED: (exit {e.returncode}): {e.stderr.strip()}"

    with open(logs_file,"a") as f:
        f.write(f"{timestamp} - {output}\n")

    print("Logged successfully.")


if __name__ == "__main__":
    main()
