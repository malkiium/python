import os
from PIL import Image

# Unicode characters for brightness levels (can be customized)
UNICODE_CHARS = [
    " ",   # Darkest (empty space)
    "▁",   # 5% block
    "▂",   # 10% block
    "▃",   # 20% block
    "▄",   # 30% block
    "▅",   # 40% block
    "▆",   # 60% block
    "▇",   # 80% block
    "░",   # 50% shade
    "▒",   # 70% shade
    "▓",   # 90% shade
    "█"    # Lightest (full block)
]

# Resize image with corrected aspect ratio for Unicode
def resize_image(image, new_width=100):
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio * 0.6)  # Adjusted for smoother scaling
    return image.resize((new_width, new_height))


# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Convert pixels to Unicode characters
def pixels_to_unicode(image):
    pixels = image.getdata()
    characters = "".join(UNICODE_CHARS[min(pixel // (256 // len(UNICODE_CHARS)), len(UNICODE_CHARS) - 1)] for pixel in pixels)
    return characters

# Generate Unicode art
def image_to_unicode(image_path, new_width=100):
    image = Image.open(image_path)
    image = resize_image(image, new_width)
    image = grayify(image)
    unicode_str = pixels_to_unicode(image)
    img_width = image.width
    unicode_art = "\n".join(
        unicode_str[i: (i + img_width)] for i in range(0, len(unicode_str), img_width)
    )
    return unicode_art

# Input and output
imagefilepath = input("Enter the path of the image to convert (without extension): ").strip()

# List of possible extensions to check
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Check for file existence with possible extensions
image_path = None
for ext in extensions:
    possible_path = imagefilepath + ext
    if os.path.isfile(possible_path):
        image_path = possible_path
        break

if image_path is None:
    print(f"Error: No image found at the specified path with extensions {extensions}.")
else:
    # Get the filename without the extension
    base_filename = os.path.splitext(os.path.basename(image_path))[0]

    # Define the output file path (saving in the specified directory with the same filename and a .txt extension)
    savefilepath = os.path.join(r"C:\Users\eliha\Pictures\unicode_art", f"{base_filename}.txt")

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(savefilepath), exist_ok=True)

    # Generate Unicode art and save to file
    # Generate Unicode art and save to file
    try:
        unicode_art = image_to_unicode(image_path, new_width=200)

        # Open the file with utf-8 encoding to support Unicode characters
        with open(savefilepath, "w", encoding="utf-8") as f:
            f.write(unicode_art)

        print(f"Unicode art has been saved to: {savefilepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
