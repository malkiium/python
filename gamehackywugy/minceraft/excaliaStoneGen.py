from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController
import time

mouse = MouseController()
keyboard = KeyboardController()

left_pressed = False
tick_counter = 0

# Touche toggle (AZERTY 'à')
TOGGLE_KEY = KeyCode(char='à')

last_time = time.time()

def on_press(key):
    global left_pressed
    if key == TOGGLE_KEY:
        if not left_pressed:
            mouse.press(Button.left)
            left_pressed = True
            print("Left mouse button held down.")
        else:
            mouse.release(Button.left)
            left_pressed = False
            print("Left mouse button released.")

def on_release(key):
    pass

# Listener clavier
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Press 'à' to toggle left mouse button.")

try:
    while True:
        current_time = time.time()
        if left_pressed and current_time - last_time >= 1:
            last_time = current_time
            tick_counter += 1
            print(f"Held for {tick_counter} seconds")
            if tick_counter == 300:
                keyboard.press(' ')
                time.sleep(0.05)
                keyboard.release(' ')
                tick_counter = 0
        elif not left_pressed:
            tick_counter = 0
        time.sleep(0.01)  # Petit sleep pour CPU
except KeyboardInterrupt:
    print("Program stopped by user")
    if left_pressed:
        mouse.release(Button.left)
