

#!/usr/bin/env python3

"""

organize_files.py

Organizes files in a given folder into subfolders by file extension
"""

import sys
import os 
import shutil

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 organize_files.py <folder_path>")
        return
    
    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path,ext)

            if not os.path.exists(ext_folder):
                os.mkdir(ext_folder)
            
            dest_path = os.path.join(ext_folder,filename)
            shutil.move(file_path,dest_path)
    
    print("Files organized successfully!")

if __name__ == "__main__":
    main()
