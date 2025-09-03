from pynput import mouse, keyboard
import pyautogui
from fractions import Fraction
import time

recording = False
w, h = pyautogui.size()
output_file = "recorded_macro.txt"

# Clear file at start
with open(output_file, "w") as f:
    f.write("# Recorded macro\n\n")

def save_line(line):
    """Append a line to the file with a 0.1s delay"""
    full_line = f"{line}, time.sleep(0.1)"
    print(full_line)
    with open(output_file, "a") as f:
        f.write(full_line + "\n")

def simplify(value, total):
    frac = Fraction(value, total).limit_denominator(100)
    if frac.numerator == 1:
        return f"/{frac.denominator}"
    else:
        return f"*{frac.numerator}/{frac.denominator}"

# --- Mouse callbacks ---
def on_click(x, y, button, pressed):
    if recording and pressed:
        fx = simplify(int(x), w)
        fy = simplify(int(y), h)
        if button == mouse.Button.left:
            save_line(f"pyautogui.click(w{fx}, h{fy}), time.sleep(0.1)")
        elif button == mouse.Button.right:
            save_line(f"pyautogui.rightClick(w{fx}, h{fy}), time.sleep(0.1)")
        elif button == mouse.Button.middle:
            save_line(f"pyautogui.middleClick(w{fx}, h{fy}), time.sleep(0.1)")

def on_scroll(x, y, dx, dy):
    if recording:
        save_line(f"pyautogui.scroll({dy})")

# --- Keyboard callback ---
def on_press(key):
    global recording
    try:
        if key == keyboard.Key.space:
            recording = not recording
            save_line(f"# Recording {'ON' if recording else 'OFF'}")
        elif key == keyboard.Key.esc:
            save_line("# Exiting...")
            return False
        else:
            # Record normal key presses
            if hasattr(key, 'char') and key.char is not None:
                save_line(f"pyautogui.press('{key.char}'), time.sleep(0.1)")
            else:
                # special keys like shift, ctrl, etc.
                save_line(f"pyautogui.press('{key.name}'), time.sleep(0.1)")
    except AttributeError:
        pass

print("Press SPACE to toggle recording. Press ESC to quit.")
print(f"Output saved to {output_file}")

# --- Start listeners ---
with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as ml, \
     keyboard.Listener(on_press=on_press) as kl:
    ml.join()
    kl.join()
