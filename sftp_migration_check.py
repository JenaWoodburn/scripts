# Check SFTP server for files and list any found

# Update check_location to root of the directories you want to check
# Run this script in the directory above check_location
# Any files found will be output to the terminal
# 'outgoing' directories are ignored as they are where we deliver client reports. Set ignore_folder = None to include all folders

from pathlib import Path

# root of folder structure to check
check_location = "SFTP"
search_path = Path(check_location)

# folders to ignore
ignore_folder = "outgoing"

found_files = [
    f for f in search_path.rglob("*") 
    if f.is_file()
    and ignore_folder not in f.parts
    ]
 
# output list of found files in numbered & sorted order
if len(found_files) == 0:
    print("No files found")
else:
    for i, f in enumerate(sorted(found_files), start=1):
        print(f"{i}. {f}")