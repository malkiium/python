import random

leng = random.randint(0,5)
numbs1 = [0] * leng
numbs2 = [0] * leng

for i in range(len(numbs1)):
    numbs1[i] = random.randint(0,10)
for i in range(len(numbs2)):
    numbs2[i] = random.randint(0, 10)
numbs1.sort()
numbs2.sort()

print("numbs1 :", numbs1, "numbs2 :", numbs2)

numbs3 = []
numbs3 = numbs1 + numbs2
numbs3.sort()

print("numbs3 :", numbs3)