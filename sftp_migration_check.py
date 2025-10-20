# Check SFTP server for files and list any found

# Update check_location to root of the directories you want to check
# Run this script in the directory above check_location
# Any files found will be output to the terminal

# Add any file extensions to be ignored to list 'ignore_exts'
# Generally we ignore any temporary files etc
# Set ignore_exts = [] to list all files found

# Add any folders to be ignored to the list 'ignore_folders'
# 'outgoing' directories are ignored as they are where we deliver client reports 
# Set ignore_folder = [] to include all folders

# To show files only newer than cutoff_time threshold, use argument 'recent', ie 'sftp_migration_check.py recent'
# Update threshold timedelta(minutes=) in cutoff_time to show only files newer than eg 10 minutes
# To show all files, run file without any arguments


from pathlib import Path
from datetime import datetime, timedelta
from sys import argv

# root of folder structure to check
check_location = "SFTP"
search_path = Path(check_location)

# file types and folders to ignore
ignore_exts = [".tmp", ".partial", ".lock"]
ignore_folders = ["outgoing"]

cutoff_time = datetime.now() - timedelta(minutes=10)

mode_recent = True if len(argv) > 1 else False

found_files = [
    f for f in search_path.rglob("*") 
    if f.is_file()
    and f.suffix not in ignore_exts
    and not any(part in ignore_folders for part in f.parts)
    and datetime.fromtimestamp(f.stat().st_mtime) > cutoff_time if mode_recent
    ]
 
# output list of found files in numbered & sorted order
if len(found_files) == 0:
    print("No files found")
else:
    for i, f in enumerate(sorted(found_files), start=1):
        print(f"{i}. {f}")