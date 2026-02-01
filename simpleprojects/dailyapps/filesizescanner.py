import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

SIZE_LIMIT = 2 * (1024^3)  # 10 GB
START_PATH = "C:\\Users\\eliha"  # Update this as needed

print_lock = Lock()


def get_size(path):
    """Calculate the size of a file or folder safely."""
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except (PermissionError, FileNotFoundError, OSError):
            return 0

    total_size = 0
    for root, _, files in os.walk(path, onerror=lambda e: None):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                total_size += os.path.getsize(filepath)
            except (PermissionError, FileNotFoundError, OSError):
                continue
    return total_size


def process_entry(entry):
    """Process a single directory entry: calculate its size and report if large."""
    results = []
    try:
        size = get_size(entry.path)

        if size > SIZE_LIMIT:
            item_type = "File" if entry.is_file() else "Folder"
            results.append((entry.path, size, item_type))

        # Return child directories to be scanned at the next level
        if entry.is_dir(follow_symlinks=False):
            try:
                children = list(os.scandir(entry.path))
                results.append(("__children__", children, None))
            except (PermissionError, FileNotFoundError, OSError):
                pass

    except (PermissionError, FileNotFoundError, OSError):
        pass

    return results


def scan_directory(path, max_workers=8):
    """Scan a directory for large files and folders using a thread pool."""
    try:
        pending = list(os.scandir(path))
    except (PermissionError, FileNotFoundError, OSError):
        print(f"Cannot access: {path}")
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while pending:
            futures = {executor.submit(process_entry, entry): entry for entry in pending}
            pending = []  # Reset for next wave of child directories

            for future in as_completed(futures):
                try:
                    for item in future.result():
                        path_val, data, item_type = item

                        if path_val == "__children__":
                            # data is a list of child DirEntry objects
                            pending.extend(data)
                        else:
                            # data is the size, item_type is "File" or "Folder"
                            with print_lock:
                                print(f"Large {item_type}: {path_val} ({data / (1024**3):.2f} GB)")
                except Exception:
                    continue


if __name__ == "__main__":
    if os.path.isdir(START_PATH):
        scan_directory(START_PATH)
    else:
        print(f"Invalid directory: {START_PATH}")