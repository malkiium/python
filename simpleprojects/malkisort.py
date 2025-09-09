import random

mxlength = random.randint(0, 10)
mnlength = 0
unsorted = []

for i in range(mxlength + 1):
    unsorted.append(random.randint(0, mxlength))

def malkisort():
    global mnlength
    middle = (mxlength - mnlength) // 2
    while mxlength - mnlength > 1:
        middle = middle // 2
        print(middle)
        print(unsorted)
        if middle == mnlength:
            if unsorted[middle] > unsorted[middle + 1]:
                unsorted[middle], unsorted[middle + 1] = unsorted[middle + 1], unsorted[middle]
                mnlength += 1
                middle = (mxlength - mnlength)
            else : 
                mnlength += 1
                middle = (mxlength - mnlength)


malkisort()