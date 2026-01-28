

#!/usr/bin/env python3

"""
system_info.py

Runs a system command to display system information
"""

import subprocess

def main():
    try:
        system_info = subprocess.run(
            ["uname", "-a"],
            capture_output=True,
            text=True,
            check=True
            
        )
        print(system_info.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed!")
        print("Error output:")
        print(e.stderr)

    

if __name__ == "__main__":
    main()
