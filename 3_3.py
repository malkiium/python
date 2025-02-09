import random

leng = random.randint(0,10)
numbs = [0] * leng

for i in range(len(numbs)):
    numbs[i] = random.randint(0,10)
numbs.sort()

print("\n\n", numbs)

inpnumb = int(input("add a number ? "))
numbs.append(inpnumb)
numbs.sort()

print("\n\n", numbs)