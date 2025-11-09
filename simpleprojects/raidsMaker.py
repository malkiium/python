print("\n\n\n\n\n\n\n\n\n\n\n\n")

disk1 = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0], 
]

disk2 = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"], 
]

disk3 = [
    [0,1,0,1],
    [0,1,1,0],
    [1,1,0,0],
    [1,0,1,0], 
]


def raidZero(disktmg, disktmg2):
    print("\n\n")
    print("raid 0 of :", disktmg, "and", disktmg2)
    diskFinal = []
    for row in range(len(disktmg)):
        diskFinal.append(disktmg[row])
        diskFinal.append(disktmg2[row])
    for i in range(len(diskFinal)):
        print(diskFinal[i], int((i // 2) + 1))
    return(diskFinal)


def raidOne(disktcp):
    print("\n\n")
    print("raid 1 of :", disktcp)
    diskCpy = []
    for row in range(len(disktcp)):
        diskCpy.append(disktcp[row])
    for i in range(len(diskCpy)):
        print(diskCpy[i], i+1)
    return(diskCpy)


def raidTen():
    diskone = raidOne(disk1)
    disktwo = raidOne(disk2)

    diskdone = raidZero(diskone, disktwo)
    print("\n")

    print("raid 10 output :")
    for i in range(len(diskdone)):
        print(diskdone[i], i+1)

raidTen()