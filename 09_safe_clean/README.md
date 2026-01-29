# Safe File Cleanup Script

## Description
This script safely cleans old files from a directory based on their age.

By default, it runs in **dry-run mode**, meaning:
- NO files are deleted
- It only prints what *would* be removed

Actual deletion requires an explicit flag.

---

## Usage

### Dry run (recommended)
```bash
python3 safe_clean.py <directory> <days>
```
**Example:**
```bash
python3 safe_clean.py logs 7
```

## Delete files (explicit action)
```bash
python3 safe_clean.py <directory> <days> --delete
```

**Example:**
```bash
python3 safe_clean.py logs 7 --delete
```
⚠️**Warning:** This permanently delets files older than the specified number of days.

## Arguments
- `<directory>` - Directory to scan
- `<days>` – Remove files older than this many days
- `--delete` - Enable deletion (optional)

## Safety Features
- Dry-run mode by default
- No shell commands (`rm -rf` is NOT used)
- Explicit delete flag required
- Prints every affected file

## Notes 
- File age is based on last modification time
- Unreadable files are skipped safely
- Works recursively on subdirectories

## Example Output
```bash
DRY-RUN: logs/system.log (12 days old)

Summary:
Candidates: 1
Deleted: 0
```
