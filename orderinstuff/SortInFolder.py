import os
import glob
import shutil

# Base directory where the files are located
base_dir = r"C:\Users\eliha\vsc\cove\python"

# Loop through exo numbers 4 to 9
for exo in range(4, 10):
    folder_name = f"exo{exo}"
    destination_folder = os.path.join(base_dir, folder_name)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Folder created: {destination_folder}")
    else:
        print(f"Folder already exists: {destination_folder}")

    # Define the pattern for files starting with 'exoX_'
    pattern = os.path.join(base_dir, f"exo{exo}_*")

    # Get the list of files matching the pattern
    files_to_move = glob.glob(pattern)

    # Move each file to the destination folder
    for file_path in files_to_move:
        if os.path.isfile(file_path):
            print(f"Moving file: {file_path}")
            shutil.move(file_path, destination_folder)
        else:
            print(f"Skipping non-file: {file_path}")

print("All matching files have been moved.")
