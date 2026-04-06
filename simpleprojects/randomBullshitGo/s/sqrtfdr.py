import time


x = int(input("what is the number ? : "))
helf = x/2
sq = 0
timesrt = time.time()

while abs(sq - x) > 0.0000001:

    sq = helf*helf
    print(helf)
    helf = (helf+(x/helf))/2

print("found at : ", helf)

print("this took : ", time.time() - timesrt, "seconds")