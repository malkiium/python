import random
guessedNmb = random.randint(1, 100)
isCorrect = False

while isCorrect == False:
    userGuess = int(input("Guess a number between 1 and 100: "))
    if guessedNmb == userGuess:
        print("You guessed it!")
        isCorrect = True
    elif guessedNmb < userGuess:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

print("The number was:", guessedNmb)