import time


x = int(input("what is the number ? : "))
helf = x/2
sq = 0
timesrt = time.time()

while True:

    sq = helf*helf
    if abs(sq - x) < 0.0000001:
        print("found at : ", helf)
        break
    elif (helf*helf) > x:
        helf-=(helf/2)
    else:
        helf+=(helf/2)

print("this took : ", time.time() - timesrt, "seconds")