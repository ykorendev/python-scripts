

#!/usr/bin/env python3

"""
safe_clean.py

Safely clean old files from a directory.
Dry-run by default.
"""

import os
import sys
import time

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 safe_clean.py <dir> <days> [--delete]")
        return
    
    target_dir = sys.argv[1]
    days = int(sys.argv[2])
    delete_mode = "--delete" in sys.argv

    if not os.path.isdir(target_dir):
        print("ERROR: Not a directory")
        return

    now = time.time()
    cutoff = now - (days * 86400)

    deleted = 0
    candidates = 0

    for root, dirs, files in os.walk(target_dir):
        for name in files:
            path = os.path.join(root, name)
            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue
            
            if mtime < cutoff:
                candidates +=1
                age_days = int((now-mtime) / 86400)

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