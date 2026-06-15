import time
import csv
from datetime import datetime
import platform
import psutil
from threading import Thread

# Install this: pip install pynput
from pynput import keyboard, mouse

# macOS App tracking
if platform.system() == "Darwin":
    from AppKit import NSWorkspace
elif platform.system() == "Windows":
    import win32gui
    import win32process

CSV_FILE = "activity_log.csv"

# Initialize CSV file
with open(CSV_FILE, mode="a", newline="") as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["timestamp", "active_app", "keyboard_activity", "mouse_activity", "context", "feeling", "energy_level"])

# Global counters
keyboard_count = 0
mouse_count = 0

# Keyboard listener
def on_key_press(key):
    global keyboard_count
    keyboard_count += 1

kb_listener = keyboard.Listener(on_press=on_key_press)
kb_listener.start()

# Mouse listener
def on_click(x, y, button, pressed):
    global mouse_count
    if pressed:
        mouse_count += 1

def on_move(x, y):
    global mouse_count
    mouse_count += 1  # count movement as activity

mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)
mouse_listener.start()

# Get active app
def get_active_app():
    if platform.system() == "Darwin":
        return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
    elif platform.system() == "Windows":
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in psutil.process_iter(['pid', 'name']):
            if p.info['pid'] == pid:
                return p.info['name']
        return "UnknownApp"
    else:
        return "UnknownApp"

# Prompt user for context and feeling
def prompt_user():
    context = input("What are you doing? ")
    feeling = input("How do you feel? ")
    energy_level = float(input("Enter energy level (0-1): "))
    return context, feeling, energy_level

# Main tracking loop
try:
    while True:
        interval = 60  # seconds
        keyboard_count = 0
        mouse_count = 0
        
        # Wait for interval while counting input
        time.sleep(interval)
        
        active_app = get_active_app()
        
        # Threshold to ask feedback (example: >50 combined events)
        if keyboard_count + mouse_count > 50:
            context, feeling, energy_level = prompt_user()
        else:
            context, feeling, energy_level = "", "", ""
        
        timestamp = datetime.now().isoformat()
        
        # Write to CSV
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, active_app, keyboard_count, mouse_count, context, feeling, energy_level])
        
        print(f"Logged at {timestamp}: App={active_app}, KB={keyboard_count}, Mouse={mouse_count}, Context={context}, Feeling={feeling}")

except KeyboardInterrupt:
    print("Tracking stopped.")
