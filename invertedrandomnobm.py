import random

def randiminium():
    answer = "nop"
    lwlim = 0
    hilim = 50

    while answer.lower() != "yes":

        randnumb = random.randint(lwlim, hilim)

        print("i will try to guess", end="! ")
        print("is it : ", randnumb, end="?? ")
        answer = input()

        if answer.lower() == "lower":
            hilim = randnumb-1
        elif answer.lower() == "higher":
            lwlim = randnumb+1

    more = str(input("i found it ! hell ye ! want to try again ? "))
    if more.lower() == "yes":
        print()
        randiminium()
    else:
        print("oki ! good bye !")

randiminium()