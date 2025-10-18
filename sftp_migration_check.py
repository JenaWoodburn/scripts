# Check SFTP server for files and list any found

# Update check_location to root of the directories you want to check
# Run this script in the directory above check_location
# Any files found will be output to the terminal

from pathlib import Path

# root of folder structure to check
check_location = "SFTP"
search_path = Path(check_location)

found_files = [f for f in search_path.rglob("*") if f.is_file()]

for i, f in enumerate(sorted(found_files), start=1):
    print(f"{i}. {f}")