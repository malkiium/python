import random
import sys

randnumb = random.randint(1, 100)
tries = 0

def randominette():
    global randnumb, tries
    choix = int(input("quelle est votre guess ? : "))

    while choix != randnumb:
        if choix > randnumb:
            tries += 1
            choix = int(input("trop grand. re essayer ! : "))
        if choix < randnumb:
            tries +=1
            choix = int(input("trop petit. re essayer ! : "))

    print("bien jouer ! c'est correct ! vous avez prit ", tries, " essayé pour réussir.")

    rest: str = input("voulez vous rejouer ? True pour continue, False pour aretter : ")
    if rest.lower() == "true" or "oui":
        print("ok, rejouons !")
        print()
        randominette()
    else:
        print("okay ! a plus !")
        sys.exit()
randominette()