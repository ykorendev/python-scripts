

# Cleanup Script

## Description
A Python utility that finds and removes files older than a specified number of days.  

## Features
- Safe **dry-run mode** by default
- Optional **file deletion**
- Optional **logging**
- Automatically creates log directory and file when logging is enabled
- Works from any directory

## Requirements
- Python 3.8+  
- Works on Linux / macOS / Windows  

No external dependencies.  

## Usage
```bash
python cleanup.py DIRECTORY [options] 
```
**Options**

| Option     | Description                               |
| ---------- | ----------------------------------------- |
| `--days N` | Files older than N days (default: 7)      |
| `--delete` | Actually delete files (otherwise dry-run) |
| `--log`    | Write actions to a log file               |


## Examples
Dry-run (no deletion):
```bash
python3 cleanup.py /tmp
```

Delete files older than 14 days:
```bash
python3 cleanup.py /tmp --days 14 --delete --log
```

Delete and log actions:
```bash
python3 cleanup.py /tmp --delete --log
```

**Logging**
When `--log` is enabled:
- Logs are written to `logs/cleanup.log`
- Log directory and file are created automatically
- Each entry includes a timestamp

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
python cleanup.py --help
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


