

#!/usr/bin/env python3

"""
cleanup.py

Remove files older than N days from a target directory.
Supports dry-run, deletion and optional logging, and config files.
"""

import os
import time
import argparse
import configparser
from datetime import datetime

# ---------- Defaults ----------- 
DEFAULT_DAYS = 7
DEFAULT_LOG = False


# ------- Config helper ---------
def load_config(config_path):
    config = configparser.ConfigParser()

    if not os.path.exists(config_path):
        return {}

    config.read(config_path)

    if "cleanup" not in config:
        return {}
    return config["cleanup"]

# ------- Logging helper --------
def log_message(message, enabled):
    if not enabled:
        return
    
    base_dir = os.path.dirname(__file__)
    logs_dir = os.path.join(base_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, "cleanup.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open (log_file, "a") as f:
        f.write(f"{timestamp} - {message}\n")

# --------- Main Logic -----------
def main():

    base_dir = os.path.dirname(__file__)
    default_config_path = os.path.join(base_dir, "cleanup.ini")

   
    # ------- Argument parsing (phase 1: config selection) --------
    parser = argparse.ArgumentParser(description="Cleanup old files")
    parser.add_argument("directory", help="Target directory to clean")
    parser.add_argument("--config", help="Path to config file", default=default_config_path)

    # Temporary parse to know which config file to load
    args, remaining_args = parser.parse_known_args()

    # ---------- Load config -------------
    config = load_config(args.config)
      
    config_days = int(config.get("days", DEFAULT_DAYS))
    config_log = config.get("log", str(DEFAULT_LOG)).lower() == "true"

    # ----------- Argument parsing (phase 2: real options)----------
    parser.add_argument("--days", type=int, default=config_days, help="Files older than this will be affected")
    parser.add_argument("--delete", action="store_true", help="Actually delete files")
    parser.add_argument("--log", action="store_true", default=config_log, help="Enable logging")
   

    args = parser.parse_args()

   

    target_dir = os.path.abspath(args.directory)
    cutoff_time = time.time() - (args.days * 86400)

    for root, dirs, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)

            try:
                file_mtime = os.path.getmtime(file_path)

                if file_mtime < cutoff_time:
                    if args.delete:
                        os.remove(file_path)
                        msg=f"Deleted: {file_path}"
                    else:
                        msg = f"WOULD DELETE: {file_path}"

                    print(msg)
                    log_message(msg, args.log)


            except OSError:
                # Skip files we cannot access
                continue


if __name__ == "__main__":
    main()

