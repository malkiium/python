input_file = "recorded_macro1.txt"   # your original file
output_file = "macro_with_delay.txt"  # new file with delays

with open(input_file, "r") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    for line in lines:
        stripped = line.strip()
        # Only add delay to pyautogui action lines
        if stripped.startswith("pyautogui."):
            f.write(stripped + ", time.sleep(0.3)\n")
        else:
            f.write(stripped + "\n")

print(f"Done! File with delays saved as {output_file}")