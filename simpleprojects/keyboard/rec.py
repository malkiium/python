from pynput import mouse, keyboard
import time

actions = []
last = time.perf_counter()

def record(action):
    global last
    now = time.perf_counter()
    actions.append(f"time.sleep({now - last:.4f})")
    actions.append(action)
    last = now

def on_click(x, y, button, pressed):
    if pressed:
        record(f"pg.click({int(x)}, {int(y)}, button='{button.name}')")

def on_press(key):
    if key == keyboard.Key.esc:
        return False

    name = key.char if hasattr(key, "char") else key.name
    record(f"pg.press({name!r})")

with mouse.Listener(on_click=on_click):
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

with open("macro.py", "w") as f:
    f.write("import pyautogui as pg\n")
    f.write("import time\n\n")
    f.write("pg.PAUSE = 0\n")
    f.write("pg.DARWIN_CATCH_UP_TIME = 0\n")
    f.write("time.sleep(3)\n\n")
    f.write("\n".join(actions))

print("Macro saved!")