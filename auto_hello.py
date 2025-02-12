import webbrowser
import time
import pyautogui


webbrowser.open("https://www.twitch.tv/willowsiva")
time.sleep(3)

pyautogui.click(x=2400, y=1375)

time.sleep(0.5)
pyautogui.click(x=2400, y=1375)

pyautogui.write("hello world", interval=0.01)
pyautogui.press("enter")