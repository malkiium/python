import pyautogui as pg
import time

pg.PAUSE = 0
pg.DARWIN_CATCH_UP_TIME = 0
time.sleep(0.5)

while True :
    time.sleep(0.4570)
    pg.click(1438, 317, button='left')
    time.sleep(0.4081)
    pg.click(1382, 409, button='left')
    time.sleep(0.4333)
    pg.click(1273, 493, button='left')
    time.sleep(0.4923)
    pg.click(1181, 418, button='left')
    time.sleep(0.4248)
    pg.press('e')
    time.sleep(0.4978)
    pg.click(966, 553, button='left')
    time.sleep(0.4853)
    pg.click(1024, 670, button='left')
    time.sleep(0.4917)
    pg.click(1135, 763, button='left')
    time.sleep(0.4997)
    for _ in range(25000):
        pg.press('d')
    time.sleep(2.5)
    pg.click(1172, 587, button='left')
    time.sleep(0.5)
    pg.click(1279, 526, button='left')