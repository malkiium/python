import pyautogui as pg
import time

pg.PAUSE = 0
pg.DARWIN_CATCH_UP_TIME = 0

coords = [
    (1200, 600)
]

time.sleep(3)

for _ in range(3000):
    pg.press("a")

pg.click(1150, 575)
time.sleep(0.01)
pg.click(1300, 525)
time.sleep(0.01)
pg.click(1450, 300)
time.sleep(0.01)
pg.click(1400, 475)
time.sleep(0.01)