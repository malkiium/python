import sys
import random

answer = "nop"
lwlim = 0
hilim = 50

def randiminium():
    global answer, lwlim, hilim

    while answer.lower() != "yes":
        print("i will try to guess!", end=". ")
        randnumb = random.randint(lwlim, hilim)
        print(" is it : ", randnumb, end="?? ")
        answer = input()
        if answer.lower() == "lower":
            hilim -= 1
        if answer.lower() == "higher":
            lwlim += 1

    more = str = input("i found it ! hell ye ! want to try again ? ")
    if more.lower() == "yes":
        print()
        answer = "anythingnow"
        randiminium()
    else:
        print("oki ! good bye !")
        sys.exit()
randiminium()