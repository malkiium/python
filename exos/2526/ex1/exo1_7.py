import random

def init() -> int:
    print("\n\n\n\n")
    print("hello ! this is a guessing game. \n you will chose a number, and i will try to gues it ! \n")
    print("good luck !!")
    tries=0
    gameLoop(tries)

def gameLoop(tries: int) -> str:
    ans = None
    min = 1
    max = 1000
    while True:
        chosennumb = random.randint(min, max)
        print("i guess:", chosennumb , "      my max is", max, "my min is", min)
        ans = input("the the number bigger or smaller or the same? : ")
        if ans.isascii():
            tries +=1
            if ans == "bigger":
                min = chosennumb+1
            elif ans == "smaller":
                max = chosennumb-1
            elif ans == "same":
                break
    gameEnd(tries)

def gameEnd(tries: int) -> None:
    print("good job ! you have guessed correctly in", tries, "\n shall i reset the game for you to play again ?")
    yeno = str(input("y/n :"))
    if yeno == "y":
        init()
    else:
        return None

init()