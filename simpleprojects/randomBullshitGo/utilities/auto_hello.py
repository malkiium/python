import webbrowser
import time

import keyboard
import pyautogui


webbrowser.open("https://www.twitch.tv/willowsiva")
time.sleep(3)

pyautogui.click(x=2400, y=1375)

time.sleep(0.5)
pyautogui.click(x=2400, y=1375)

keyboard.write("Hello World !")
pyautogui.press("enter")
time.sleep(1)
keyboard.write("!lurk")
pyautogui.press("enter")