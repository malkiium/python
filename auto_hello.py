import webbrowser
import time
import pyautogui

# Open Google in Chrome
webbrowser.open("https://www.google.com")

# Wait for the browser to load
time.sleep(3)

# Click on the search bar (adjust coordinates if necessary)
pyautogui.click(x=400, y=300)  # Approximate location, may need adjustment

# Type "hello world"
pyautogui.write("hello world", interval=0.1)

# Press Enter
pyautogui.press("enter")
