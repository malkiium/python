# ------user input-------
choise = int(input("- 1 for triangle \n- 2 for square \n- 3 for circle \n :: "))
chosize = int(input("what is the size ? : "))

# ------triangle------
def triang(size):
    wid = 0
    for i in range(1, size):
        wid += 1
        for j in range(wid):
            if j==0 or j==wid-1:
                print(end="*")
            else:
                print(end=" ")
        print()
    print((wid+1)*"*")


# ------square------
def squrt(size):
    print(size*"*")
    for line in range(1, size):
        for wid in range(size):
            if wid==0 or wid==size-1:
                print(end="*")
            else:
                print(end=" ")
        print()
    print(size*"*")

# ------circle------
def crik(size):
    wid=1
    print((size-wid)*" ", size*"*")
    for growth in range(1, size):
        print(end=((size-wid)*" "))
        print(end="*")
        print(end=(size+(2*wid)-2)*" ")
        print(end="*")
        wid +=1
        print()
    for straight in range(1, size+1):
        print(end="*")
        print(end=((size*3-2))*" ")
        print(end="*")
        print()
    for smals in range(1, size):
        wid-=1
        print(end=((size-wid)*" "))
        print(end="*")
        print(end=(size+(2*wid)-2)*" ")
        print(end="*")
        print()
    print((size-wid)*" ", size*"*")



# ------chosenening------
if choise == 1:
    triang(chosize)
elif choise == 2:
    squrt(chosize)
elif choise == 3:
    crik(chosize)
else:
    triang(chosize)
    print()
    squrt(chosize)
    print()
    crik(chosize)