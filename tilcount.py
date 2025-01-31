import sys
import time

currenttime = time.time()

for i in range(1_000_000_000):
    if i%1000000000 == 0:
        print("yes")

end = time.time()
print(end-currenttime, "seconds")