

# Safe Cleaner 

## Description
A small Python CLI tool that scans a directory and finds files older than a specified number of days.  
By default, it only reports what would be deleted.  
With a flag, it can actually delete the files.  

## Requirements
- Python 3.8+  
- Works on Linux / macOS / Windows  

No external dependencies.  

## Usage
```bash
python safe_clean_cli.py DIRECTORY DAYS [--delete]  
```

**Positional Arguments**
`DIRECTORY` Directory to scan (e.g. `logs`)  
`DAYS` Files older than tis many days are considered  

**Optional Flags**
`--delete` Actually delet files (without this, nothing is removed)  

## Examples
**Preview only (safe mode)**
```bash
python safe_clean_cli.py logs 7
```
**Output:**
```bash
OLD FILE: logs/system.log (12 days old)
```
No files are deleted  

**Delete old files**
```bash
python safe_clean_cli.py logs 7 --delete
```

**Output:**
```bash
DELETED: logs/system.log
```
Files older than 7 days are removed.  

## Safety behavior 
- Files are **never deleted** unless `--delete` is explicitly provided  
- Errors (permission issues, broken files, etc.) are skipped safely
- Uses `argparse` for:  
    - Input validation
    - Type checking
    - Helpful error messages
    - `--help` support

## Help
```bash
python safe_clean_cli.py --help
```

Show: 
- usage
- argument descriptions
- available flags

## Notes
- This script uses **file modification time**, not creation time
- Use carefully on system directories
- Recommended to run without `--delete` first

## License 
MIT License — use, modify and share freely.


