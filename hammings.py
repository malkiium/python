word1 = ""
word2 = ""
difletters = 0

def hammingstuff():
    global word2, word1

    word1 = input("what is the first word ? : ")
    word2 = input("what is the second word ? : ")

    if len(word1.lower()) == len(word2.lower()):
        difletters = len(set(word1) ^ set(word2))  # Symmetric difference
        print(f"Number of differing letters: {difletters}")

    else:
        print("-1")

hammingstuff()