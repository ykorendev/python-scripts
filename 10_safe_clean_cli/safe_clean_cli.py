

#!/usr/bin/env python3

"""
safe_clean_cli.py

Safely clean old files from a directory using argparse.
Dry-run by default.
"""

import os
import time 
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Safely clean old files from a directory"
    )

    parser.add_argument(
        "directory",
        help="Directory to scan"
    )

    parser.add_argument(
        "days",
        type=int,
        help="Delete files older than this many days"
    
    )

    parser.add_argument(
        "--delete",
        action="store_true",
        help="actually delete files (default is dry-run)"
    )

    args = parser.parse_args()

    target_dir = args.directory
    days = args.days
    delete_mode = args.delete

    if not os.path.isdir(target_dir):
        print("ERROR: Not a directory")
        return
    
    now = time.time()
    cutoff = now - (days * 86400)

    candidates = 0
    deleted = 0

    for root, dirs, files in os.walk(target_dir):
        for name in files:
            path = os.path.join(root, name)
            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue
            
            if mtime < cutoff:
                candidates += 1
                age_days = int((now - mtime) / 86400)

                if delete_mode:
                    os.remove(path)
                    deleted += 1
                    print(f"DELETED: {path} ({age_days} days old)")
                else:
                    print(f"DRY-RUN: {path} ({age_days} days old)")
    
    print("\nSummary:")
    print(f"Candidates: {candidates}")
    print(f"Deleted: {deleted}")

if __name__ == "__main__":
    main()