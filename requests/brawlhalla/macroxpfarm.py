import time
import keyboard
import mouse  # pip install mouse
import threading

# --- Load macro ---
macro_file = r"C:\Users\eliha\vsc\python\requests\brawlhalla\recorded_keyboard_macro.py"
macro_sequence = []
with open(macro_file, "r") as f:
    exec(f.read())  # defines macro_sequence

print("Replaying macro in 3 seconds... (Loops back to LOOP_START)")
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


# --- Run macro with loop ---
i = 0
loop_start_index = None

while True:
    delay, key = macro_sequence[i]
    time.sleep(delay)

    # --- Special: LOOP_START marker ---
    if key == "LOOP_START":
        loop_start_index = i  # remember this position
        i += 1
        continue

    # --- Special: LOOP_END ---
    if key == "LOOP_END":
        if loop_start_index is not None:
            i = loop_start_index
            continue
        else:
            print("LOOP_END reached but LOOP_START not defined. Stopping macro.")
            break


    # --- Special: WAIT_FOR_DOUBLE_CLICK ---
    if key == "WAIT_FOR_DOUBLE_CLICK":
        if target_coords is None:
            target_coords = wait_for_double_click()
        x, y = target_coords
        mouse.move(x, y)
        mouse.click()
        time.sleep(0.2)
        keyboard.press('c')
        time.sleep(0.1)
        last_key = None
        i += 1
        continue

    # --- Normal key handling ---
    if key.startswith("Key."):
        key_name = key[4:]
    else:
        key_name = key

    if key_name == last_key:
        time.sleep(MIN_BETWEEN_SAME_KEYS)

    keyboard.press(key_name)
    time.sleep(MIN_PRESS_TIME)
    keyboard.release(key_name)

    last_key = key_name
    i += 1

    # --- If end of macro reached, jump back to LOOP_START (if defined) ---
    if i >= len(macro_sequence):
        if loop_start_index is not None:
            i = loop_start_index
        else:
            print("Macro finished (no LOOP_START found).")
            break
