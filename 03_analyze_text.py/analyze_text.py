

#!/usr/bi/env python3


"""

analyze_text.py


Reads a text file, counts lines and words,
and writes the results to a report file.
"""

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_text.py <input_file>")
        return
    
    input_file = sys.argv[1]
    output_file = "report.txt"

    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: file '{input_file}' not found")
        return
    line_count = len(lines)
    word_count = 0


    for line in lines:
        words = line.split()
        word_count += len(words)

    with open(output_file, "w") as f:
        f.write(f"Lines: {line_count}\n")
        f.write(f"Words: {word_count}\n")

    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()


    
