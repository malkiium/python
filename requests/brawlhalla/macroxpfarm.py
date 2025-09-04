import time
import keyboard
import mouse  # pip install mouse
import threading

# --- Load macro ---
macro_file = r"C:\Users\eliha\vsc\python\requests\brawlhalla\recorded_keyboard_macro.py"
macro_sequence = []
with open(macro_file, "r") as f:
    exec(f.read())  # defines macro_sequence

print("Replaying macro in 3 seconds... (One-shot test run)")
time.sleep(3)

MIN_PRESS_TIME = 0.01  # 10 ms
MIN_BETWEEN_SAME_KEYS = 0.01  # 10 ms

last_key = None
target_coords = None  # will store the double click coords


def wait_for_double_click():
    print("Waiting for double click...")
    result = {}

    def handler():
        result['pos'] = mouse.get_position()

    # register a one-time handler
    mouse.on_double_click(handler)
    
    # wait until handler is triggered
    while 'pos' not in result:
        time.sleep(0.01)

    x, y = result['pos']
    print(f"Double click recorded at: {x}, {y}")
    return x, y


# --- Run macro sequence once ---
for delay, key in macro_sequence:
    time.sleep(delay)

    # --- Special macro action: WAIT_FOR_DOUBLE_CLICK ---
    if key == "WAIT_FOR_DOUBLE_CLICK":
        if target_coords is None:
            target_coords = wait_for_double_click()
        x, y = target_coords
        mouse.move(x, y)
        mouse.double_click()
        last_key = None
        continue

    # --- Normal key handling ---
    if key.startswith("Key."):
        key_name = key[4:]
    else:
        key_name = key

    # Ensure repeated keys are registered
    if key_name == last_key:
        time.sleep(MIN_BETWEEN_SAME_KEYS)

    keyboard.press(key_name)
    time.sleep(MIN_PRESS_TIME)
    keyboard.release(key_name)

    last_key = key_name

print("Macro playback finished (test run).")
