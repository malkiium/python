import random

leng = random.randint(0,100)
numbs = [0] * leng
hinum = 0
occurences = []


for i in range(len(numbs)):
    numbs[i] = random.randint(0,25)


def ver1(hinum, occurences, numbs, leng):
    print("version 1 :")

    for x in range(len(numbs)):
        if hinum < numbs[x]:
            hinum = numbs[x]

    print(hinum)

def ver2(hinum, occurences, numbs, leng):
    print("\n\n\nversion 2 : ")

    for x in range(len(numbs)):
        if hinum < numbs[x]:
            occurences.clear()
            hinum = numbs[x]
            occurences.append(x)
        elif hinum == numbs[x]:
            occurences.clear()
            occurences.append(x)

    print(hinum, occurences)

def ver3(hinum, occurences, numbs, leng):
    print("\n\n\nversion 3 :")

    for x in range(len(numbs)):
        if hinum < numbs[x]:
            occurences.clear()
            hinum = numbs[x]
            occurences.append(x)

    print(hinum, occurences)

def ver4(hinum, occurences, numbs, leng):
    print("\n\n\nversion 4 :")

    for x in range(len(numbs)):
        if hinum < numbs[x]:
            occurences.clear()
            hinum = numbs[x]
            occurences.append(x)
        elif hinum == numbs[x]:
            occurences.append(x)

    print(hinum, occurences)

ver1(hinum, occurences, numbs, leng)
ver2(hinum, occurences, numbs, leng)
ver3(hinum, occurences, numbs, leng)
ver4(hinum, occurences, numbs, leng)