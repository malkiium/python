import os

# Function to rename files that start with a number and count them
def rename_and_count_files(directory):
    count = 0  # Initialize count
    
    for filename in os.listdir(directory):
        # Check if the filename starts with a digit
        if filename[0].isdigit():
            new_name = "exo" + filename
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed "{filename}" to "{new_name}"')
            count += 1  # Increment count
    
    print(f'Total files renamed: {count}')

# Function to count files that start with "exo"
def count_files_in_directory(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith("exo"):  # Corrected condition
            count += 1
    return count

# Specify the directory path
directory_path = r'C:\Users\eliha\vsc\cove\python'

# Call the function to rename files
rename_and_count_files(directory_path)

# Count files that start with "exo"
total_files = count_files_in_directory(directory_path)
print(f'Total files that start with "exo": {total_files}')
