from pynput import keyboard, mouse
import time
import threading

# --- Configuration ---
output_file = "recorded_keyboard_macro.py"
recording = True  # start recording immediately
paused = False
last_time = None
macro_sequence = []

# --- Utilities ---
def record_key(key_char):
    global last_time
    now = time.time()
    delay = round(now - last_time, 3) if last_time else 0
    last_time = now
    macro_sequence.append((delay, key_char))
    print(f"Recorded: ({delay}, '{key_char}')")

# --- Keyboard listener ---
def on_press(key):
    if not recording or paused:
        return
    try:
        if hasattr(key, "char") and key.char is not None:
            record_key(key.char)
        else:
            # special keys (shift, ctrl, etc.)
            record_key(str(key))
    except AttributeError:
        pass

# --- Mouse listener ---
def on_click(x, y, button, pressed):
    global recording, paused
    if pressed:
        if button == mouse.Button.left:
            # Stop and save
            recording = False
            with open(output_file, "w") as f:
                f.write("macro_sequence = [\n")
                for step in macro_sequence:
                    f.write(f"    ({step[0]}, '{step[1]}'),\n")
                f.write("]\n")
            print(f"Macro saved to {output_file}. Exiting...")
            return False  # stop mouse listener
        elif button == mouse.Button.right:
            # Toggle pause
            paused = not paused
            print(f"# Recording {'PAUSED' if paused else 'RESUMED'}")

# --- Start listeners ---
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()