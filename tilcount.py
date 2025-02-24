import time

start = time.time()

for i in range(1_000_000_000):
    if i%100000000 == 0:
        print(i)

end = time.time()
print(end-start, "seconds")