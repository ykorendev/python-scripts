

#!/usr/bin/enc python3

"""
fs_inspect.py

Inspect a directory:
- count files
- calculate total size
- show disk usage
"""

import os
import sys
import shutil

def main():

    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = "."
    if not os.path.isdir(target_dir):
        print("ERROR: Not a directory")
        return
    
    file_count = 0 
    total_size = 0

    # Walk through directory tree
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            file_count += 1
            file_path = os.path.join(root,name)
            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                pass # ignore unreadable files
    
    total_size_mb = total_size / (1024 * 1024)
    
    # Disk usage
    usage = shutil.disk_usage(target_dir)

    print(f"Directory: {os.path.abspath(target_dir)}")
    print(f"Files: {file_count}")
    print(f"Total size: {total_size_mb:.2f} MB")
    print(f"Disk free: {usage.free / (1024**3):.2f} GB")


if __name__ == "__main__":
    main()