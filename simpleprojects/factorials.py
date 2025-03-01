import sys
import time

sys.set_int_max_str_digits(10**6)

def factorial():
    x = 1
    yis = 1
    currenttime = time.time()

    while x<=999-1:
        yis = yis * x
        x += 1
        print(x, "! = ", yis)

    end = time.time()
    print(end-currenttime, "seconds")

factorial()
