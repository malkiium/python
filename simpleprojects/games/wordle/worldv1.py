import random

def gameInit():
    threeLetterWord = ["Cat", "Dog", "Sun", "Sky", "Sea", "Run", "Map", "Pen", "Cup", "Box", "Hat", "Bed", "Car", "Bus", "Toy", "Key", "Ice", "Egg", "Ant",
                       "Bee", "Owl", "Pig", "Cow", "Fox", "Bat", "Man", "Boy", "Day", "Red", "Big", "Hot", "New", "Old", "Low", "Top", "Wet", "Dry", "Sad",
                       "Mad", "Fun", "Win", "Fix", "Try", "Ask", "Get", "Put", "Sit", "Eat", "Air", "Row"]

    fourLetterWord = ["Tree", "Book", "Moon", "Star", "Rock", "Wind", "Fire", "Snow", "Rain", "Ship", "Farm", "Fish", "Bird", "Wolf", "Lion", "Bear",
                      "Road", "Hill", "Lake", "Sand", "Milk", "Corn", "Rice", "Cake", "Desk", "Lamp", "Door", "Wall", "Ring", "Song", "Blue", "Gray",
                      "Pink", "Gold", "Fast", "Slow", "Warm", "Cold", "Hard", "Soft", "Love", "Hate", "Hope", "Fear", "Walk", "Jump", "Swim", "Play",
                      "Work", "Rest"]

    fiveLetterWord = ["Apple", "Bread", "Chair", "Table", "Plant", "Stone", "Cloud", "River", "Beach", "Train", "Plane", "Sweet", "Smile", "Dream",
                      "Light", "Night", "Sound", "Heart", "Brain", "Water", "Flame", "Grass", "Fruit", "Sugar", "Honey", "Drink", "Shirt", "Pants",
                      "Shoes", "Clock", "Brush", "Paper", "Glass", "Mouse", "Horse", "Sheep", "Tiger", "Zebra", "Quick", "Brave", "Calm", "Sharp",
                      "Clean", "Fresh", "Happy", "Angry", "Laugh", "Crying", "Think", "Write"]

    sixLetterWord = ["Planet", "Forest", "Ocean", "Desert", "Island", "Silver", "Golden", "Winter", "Summer", "Spring", "Autumn", "Candle",
                     "Bottle", "Basket", "Window", "Carpet", "Garden", "Bridge", "Castle", "Dragon", "Flower", "Guitar", "Pocket", "Pillow",
                     "Coffee", "Butter", "Cheese", "Tomato", "Banana", "Cherry", "Stream", "Shadow", "Thunder", "Bright", "Gentle", "Strong",
                     "Smooth", "Rough", "Simple", "Clever", "Honest", "Loyal", "Silent", "Active", "Travel", "Wander", "Create", "Build", "Listen",
                     "Wonder"]

    userNumber = int(input("What length of word do you want? 3, 4, 5 or 6: "))

    if userNumber == 3:
        chosenWord = random.choice(threeLetterWord)
    elif userNumber == 4:
        chosenWord = random.choice(fourLetterWord)
    elif userNumber == 5:
        chosenWord = random.choice(fiveLetterWord)
    elif userNumber == 6:
        chosenWord = random.choice(sixLetterWord)
    else:
        print("Invalid choice")
        return

    wordList = ["-"] * len(chosenWord)
    gameLoop(chosenWord, wordList)

def gameLoop(chosenWord: str, wordList: list):
    print("Current word: " + " ".join(wordList))
    userGuess = input("Guess a word: ")

    others = []
    for i in range(len(userGuess)):
        if i < len(chosenWord):
            if userGuess[i].lower() == chosenWord[i].lower():
                wordList[i] = userGuess[i]
            elif userGuess[i].lower() in chosenWord.lower():
                others.append(userGuess[i])

    if "".join(wordList).lower() == chosenWord.lower():
        print(f"Good job, you won! The word was '{chosenWord}'.")
        return
    else:
        if others:
            print("Letters in the word but wrong place:", ", ".join(others))
        gameLoop(chosenWord, wordList)

gameInit()