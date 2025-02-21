# This is a simple number guessing game where the computer randomly selects a number between 1 and 100.
# The player has to guess the number, and the program provides feedback on whether the guess is too high or too low.
# The game keeps track of the number of attempts and allows the player to play multiple rounds.

import random
import sys

# Generate a random number between 1 and 100
randnumb = random.randint(1, 100)
tries = 0

def randominette():
    global randnumb, tries
    # Prompt the user for their guess
    choix = int(input("quelle est votre guess ? : "))

    # Loop until the user guesses the correct number
    while choix != randnumb:
        if choix > randnumb:
            tries += 1
            choix = int(input("trop grand. re essayer ! : "))
        if choix < randnumb:
            tries += 1
            choix = int(input("trop petit. re essayer ! : "))

    # Inform the user that they guessed correctly and display the number of attempts
    print("bien jouer ! c'est correct ! vous avez prit ", tries, " essayé pour réussir.")

    # Ask the user if they want to play again
    rest: str = input("voulez vous rejouer ? True pour continue, False pour aretter : ")
    if rest.lower() == "true" or rest.lower() == "oui":
        print("ok, rejouons !")
        print()
        # Reset the random number and tries for the new game
        randnumb = random.randint(1, 100)
        tries = 0
        randominette()
    else:
        print("okay ! a plus !")
        sys.exit()

# Start the game
randominette()