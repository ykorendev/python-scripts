

# Cleanup Script

## Description
A Python utility that finds files older than a specified number of days and optionally removes them.
The script is **safe by default** and supports configuration via command-line arguments or an optional config file.
Command-line options take precedence over configuration values.

## Features
- Safe **dry-run mode** by default
- Optional **file deletion** with `--delete`
- Optional **logging** with `--log`
- Ability to explicitly disable logging with `--no-log`
- Configurable defaults via a config file
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
| `--no-log` | Disable logging (overrides config)|
| `--config FILE` | Path to configuration file (optional) |

`--log` and `--no-log` are mutually exclusive..
Command-line options override config file values when explicitly provided.


## Configuration File 
By default, the script looks for a file named `cleanup.ini` **next to the script**.

You may override this location using `--config`.

Example `cleanup.ini`:
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

If the config file does not exist or the `[cleanup]` section is missing, built-in defaults are used.

## Configuration Precedence
From lowest to highest priority:

1. Built-in defaults
2. Values from config file
3. Explicit command-line flags

## Examples
Dry-run (no deletion):
```bash
python3 cleanup.py /tmp
```

Delete files older than 14 days:
```bash
python3 cleanup.py /tmp --days 14 --delete 
```

Enable logging explicitly:
```bash
python3 cleanup.py /tmp --log
```
Disable logging even if enabled in config:
```bash
python cleanup.py /tmp --no-log
```

Use a custom config file:
```bash
python cleanup.py /tmp --config /path/to/cleanup.ini
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


