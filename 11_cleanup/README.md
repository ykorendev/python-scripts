

# Cleanup Script

## Description
A Python utility that finds files older than a specified number of days and optionally removes them.
The script is **safe by default** and supports configuration via command-line arguments or a config file.

## Features
- Safe **dry-run mode** by default
- Optional **file deletion** with `--delete`
- Optional **logging** with `--log`
- Configurable defaults via `cleanup.ini`
- Automatically creates log directory and file when logging is enabled
- Safe handling of permission errors
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

Command-line options override config file values.

## Configuration File (cleanup.ini)
You may define default behavior using a `cleanup.ini` file placed **next to the script**

Example:
```bash
[cleanup]
days = 14
log = true
```
**Supported keys**

| Key    | Description                       |
| ------ | --------------------------------- |
| `days` | Default age threshold (in days)   |
| `log`  | Enable logging (`true` / `false`) |

If the config file does not exist, built-in defaults are used.

## Examples
Dry-run (no deletion):
```bash
python3 cleanup.py /tmp
```

Delete files older than 14 days:
```bash
python3 cleanup.py /tmp --days 14 --delete 
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

Example:
```bash
2026-01-12 10:04:14 - WOULD DELETE: /path/to/file.txt
```

## Safety behavior 
- Files are **never deleted** unless `--delete` is explicitly provided  
- Errors (permission issues, broken files, etc.) are skipped safely

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


