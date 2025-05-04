import os

SIZE_LIMIT = 10 * 1024 * 1024 * 1024  # 10 Go en octets
START_PATH = "C:\\"  # Change ça si besoin

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def scan_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                try:
                    if entry.is_file():
                        size = entry.stat().st_size
                        if size > SIZE_LIMIT:
                            print(f"Large file: {entry.path} ({size / (1024**3):.2f} GB)")
                    elif entry.is_dir():
                        folder_size = get_folder_size(entry.path)
                        if folder_size > SIZE_LIMIT:
                            print(f"Large folder: {entry.path} ({folder_size / (1024**3):.2f} GB)")
                            scan_directory(entry.path)  # Recurse dans le dossier
                except PermissionError:
                    print(f"Permission denied: {entry.path}")
    except PermissionError:
        print(f"Permission denied: {path}")


if os.path.exists(START_PATH) and os.path.isdir(START_PATH):
    scan_directory(START_PATH)
else:
    print(f"Invalid directory: {START_PATH}")
