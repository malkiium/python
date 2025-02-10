import random

def fusion(numbs1:list, numbs2:list):
    numbs1.sort()
    numbs2.sort()

    print("numbs1 :", numbs1, "numbs2 :", numbs2)

    numbs3 = []
    numbs3 = numbs1 + numbs2
    numbs3.sort()

    print("numbs 3 :", numbs3, "\n")
    return numbs3

assert fusion([1, 6, 10], [0, 7, 8, 9])
assert fusion([1, 6, 10], [])
assert fusion([], [0, 7, 8, 9])

print("all tests passed ! ")