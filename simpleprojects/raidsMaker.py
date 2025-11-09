import random
print("\n\n\n\n\n\n\n\n\n\n\n\n")

disk1 = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0], 
]

disk2 = [
    [0,1,0,1],
    [0,1,1,0],
    [1,1,0,0],
    [1,0,1,0], 
]

disk3 = [
    [0,1,1,1],
    [0,1,1,0],
    [1,1,0,1],
    [1,0,1,1], 
]




def raidZero(disktmg, disktmg2):
    print("\n\n")
    diskFinal = []
    for row in range(len(disktmg)):
        diskFinal.append(disktmg[row])
        diskFinal.append(disktmg2[row])
    return(diskFinal)




def raidOne(disktcp):
    print("\n\n")
    diskCpy = []
    for row in range(len(disktcp)):
        diskCpy.append(disktcp[row])
    return(diskCpy)




def raidTen():
    diskone = raidOne(disk1)
    disktwo = raidOne(disk2)

    diskdone = raidZero(diskone, disktwo)
    print("\n")
    print("-------------------------------- Raid10 : --------------------------------\n")
    print("-------------------------------- raid 0 : --------------------------------")
    for i in range(len(diskdone)):
        print("-----------------------------", diskdone[i], i+1, "-----------------------------")

    print()

    print("-- disk1, ----------- diskOne, ------------- disk2, ------------ diskTwo --")
    for y in range(len(diskone)):
        print(disk1[y], "-------", diskone[y], "-------", disk2[y], "-------", disktwo[y])


raidTen()

print("\n\n")
print("\n\n")
print("\n\n")


print("#############################################################################")

print("\n\n" \
"-------------------------------- Raid4 : --------------------------------")

def raidFour(diskUno, diskDos, diskDres):
    DiskP = []

    bDisk = diskUno
    if len(diskDos) > len(bDisk):
        bDisk = diskDos
    if len(diskDres) > len(bDisk):
        bDisk = diskDres

    for row in range(len(bDisk)):
        DiskP.append([])
        for cell in range(len(bDisk[row])):
            Pbit = diskUno[row][cell] ^ diskDos[row][cell] ^ diskDres[row][cell]
            DiskP[row].append(Pbit)

    print("-- disk1, ------------- disk2, ------------- disk3, ------------- diskP ")
    for i in range(len(DiskP)):
        print(diskUno[i], "-------", diskDos[i], "-------", diskDres[i], "-------", DiskP[i])

    corrupt_choice = random.randint(1, 3)
    corrupted = [[0, 0, 0, 0] for _ in range(len(bDisk))]
    
    if corrupt_choice == 1:
        print("\ncorrupting disk1")
        diskUno = corrupted
    elif corrupt_choice == 2:
        print("\ncorrupting disk2")
        diskDos = corrupted
    else:
        print("\ncorrupting disk3")
        diskDres = corrupted

    print("\nAfter corruption:")
    print("-- disk1, ------------- disk2, ------------- disk3, ------------- diskP")
    for i in range(len(DiskP)):
        print(diskUno[i], "-------", diskDos[i], "-------", diskDres[i], "-------", DiskP[i])

    
    if all(cell == 0 for row in diskUno for cell in row):
        detected_disk = 1
    elif all(cell == 0 for row in diskDos for cell in row):
        detected_disk = 2
    elif all(cell == 0 for row in diskDres for cell in row):
        detected_disk = 3
    else:
        detected_disk = None

    print(f"DETECTED: disk{detected_disk} is corrupted!")

    reconstructed = []
    
    if detected_disk == 1:
        print("\nReconstructing disk1:")
        for row in range(len(bDisk)):
            reconstructed.append([])
            for cell in range(len(bDisk[row])):
                Pbit = diskDos[row][cell] ^ diskDres[row][cell] ^ DiskP[row][cell]
                reconstructed[row].append(Pbit)
        diskUno = reconstructed
        
    elif detected_disk == 2:
        print("\nReconstructing disk2:")
        for row in range(len(bDisk)):
            reconstructed.append([])
            for cell in range(len(bDisk[row])):
                Pbit = diskUno[row][cell] ^ diskDres[row][cell] ^ DiskP[row][cell]
                reconstructed[row].append(Pbit)
        diskDos = reconstructed
        
    elif detected_disk == 3:
        print("\nReconstructing disk3:")
        for row in range(len(bDisk)):
            reconstructed.append([])
            for cell in range(len(bDisk[row])):
                Pbit = diskUno[row][cell] ^ diskDos[row][cell] ^ DiskP[row][cell]
                reconstructed[row].append(Pbit)
        diskDres = reconstructed

    print("\nAfter reconstruction:")
    print("-- disk1, ------------- disk2, ------------- disk3, ------------- diskP")
    for i in range(len(DiskP)):
        print(diskUno[i], "-------", diskDos[i], "-------", diskDres[i], "-------", DiskP[i])


raidFour(disk1, disk2, disk3)