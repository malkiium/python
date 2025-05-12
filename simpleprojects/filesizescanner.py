import os

SIZE_LIMIT = 10 * 1024 * 1024 * 1024  # 10 GB
START_PATH = "D:\\"  # Update this as needed

def get_size(path):
    """Calculate the size of a file or folder."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    total_size = 0
    for root, _, files in os.walk(path):
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root, file))
            except PermissionError:
                print(f"Permission denied: {os.path.join(root, file)}")
    return total_size

def scan_directory(path):
    """Scan a directory for large files and folders."""
    try:
        for entry in os.scandir(path):
            try:
                size = get_size(entry.path)
                if size > SIZE_LIMIT:
                    item_type = "File" if entry.is_file() else "Folder"
                    print(f"Large {item_type}: {entry.path} ({size / (1024**3):.2f} GB)")
                if entry.is_dir():
                    scan_directory(entry.path)  # Recurse into subdirectories
            except PermissionError:
                print(f"Permission denied: {entry.path}")
    except PermissionError:
        print(f"Permission denied: {path}")

if __name__ == "__main__":
    if os.path.isdir(START_PATH):
        scan_directory(START_PATH)
    else:
        print(f"Invalid directory: {START_PATH}")
