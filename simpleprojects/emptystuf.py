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
    print(size)
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
    



# ------chosenening------
if choise == 1:
    triang(chosize)
elif choise == 2:
    squrt(chosize)
else:
    crik(chosize)