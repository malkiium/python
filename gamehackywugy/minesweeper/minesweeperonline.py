import time
import pyautogui
import cv2
import numpy as np
import os

# --- CONFIG ---
ROWS = 9
COLS = 9
CELL_SIZE = None
TLX, TLY = None, None
TEMPLATES = {}
# ---------------

def calibrate():
    global TLX, TLY, CELL_SIZE
    print("Place mouse on TOP-LEFT cell and press Enter...")
    input()
    TLX, TLY = pyautogui.position()
    print(f"Captured top-left: {TLX},{TLY}")

    print("Place mouse on TOP-LEFT of SECOND cell (right of first) and press Enter...")
    input()
    x2, y2 = pyautogui.position()
    CELL_SIZE = x2 - TLX
    print(f"Cell size: {CELL_SIZE}px")

def screenshot_board():
    w = CELL_SIZE * COLS
    h = CELL_SIZE * ROWS
    img = pyautogui.screenshot(region=(TLX, TLY, w, h))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def save_templates():
    """Scan board, crop numbers, and save them as templates"""
    img = screenshot_board()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    os.makedirs("templates", exist_ok=True)

    for r in range(ROWS):
        for c in range(COLS):
            cell = gray[r*CELL_SIZE:(r+1)*CELL_SIZE, c*CELL_SIZE:(c+1)*CELL_SIZE]
            mean = cell.mean()

            # skip empty or dark covered cells
            if mean < 50 or mean > 230:
                continue

            # detect strong edges (likely a number)
            edges = cv2.Canny(cell, 50, 150)
            if edges.sum() < 2000:  # not enough edges
                continue

            # try OCR-like digit clustering
            for n in range(1, 9):
                path = f"templates/{n}.png"
                if not os.path.exists(path):
                    cv2.imwrite(path, cell)
                    print(f"Saved template for {n} → {path}")
                    break

def load_templates():
    global TEMPLATES
    for n in range(1, 9):
        path = f"templates/{n}.png"
        if os.path.exists(path):
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            TEMPLATES[n] = img
    print(f"Loaded templates: {list(TEMPLATES.keys())}")

def classify_cell(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean = gray.mean()
    if mean < 50:
        return "covered"
    if mean > 220:
        return 0

    # match with known templates
    best_score, best_num = 0, None
    for n, tmpl in TEMPLATES.items():
        res = cv2.matchTemplate(gray, tmpl, cv2.TM_CCOEFF_NORMED)
        _, score, _, _ = cv2.minMaxLoc(res)
        if score > best_score:
            best_score, best_num = score, n

    if best_score > 0.6:
        return best_num
    return "unknown"

def read_board():
    img = screenshot_board()
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            cell_img = img[r*CELL_SIZE:(r+1)*CELL_SIZE,
                           c*CELL_SIZE:(c+1)*CELL_SIZE]
            row.append(classify_cell(cell_img))
        board.append(row)
    return board

# --- MAIN ---
if __name__ == "__main__":
    calibrate()

    print("Open a few cells with numbers, then press Enter to auto-generate templates...")
    input()
    save_templates()

    load_templates()
    time.sleep(1)

    board = read_board()
    for row in board:
        print(row)
