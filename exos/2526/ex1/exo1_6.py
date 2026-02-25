import random

def init() -> int:
    print("\n\n\n\n")
    print("hello ! this is a guessing game. \n i will chose a number, and you will try to gues it ! \n")
    print("good luck !!")
    tries=0

    chosennumb = random.randint(1, 1000)
    gameLoop(chosennumb, tries)

def gameLoop(chosennumb, tries) -> str:
    numb = -1
    while numb != chosennumb:
        numb = input("your guess :")
        if numb.isdigit():
            numb= int(numb)
            tries +=1
            if numb > chosennumb:
                print("the number is too big.")
            else:
                print("the number is too small.")
        else:
            print("this is not an integer. try again.")
    gameEnd(tries)


def gameEnd(tries):
    print("good job ! you have guessed correctly in", tries, "\n shall i reset the game for you to play again ?")
    yeno = str(input("y/n :"))
    if yeno == "y":
        init()
    else:
        return None

init()