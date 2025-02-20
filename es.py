import os

# Function to rename files that start with a number
def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Check if the file starts with a number
        if filename[0].isdigit():
            new_name = "exo" + filename
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed "{filename}" to "{new_name}"')

# Specify the directory path
directory_path = r'C:\Users\eliha\vsc\cove\python'

# Call the function to rename files in the specified directory
rename_files_in_directory(directory_path)
