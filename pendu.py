import random

def predict_word(pattern, word_list):
    pattern = pattern.lower()
    possible_words = [word.lower() for word in word_list if len(word) == len(pattern)]
    
    for i, char in enumerate(pattern):
        if char != '_':
            possible_words = [word for word in possible_words if word[i] == char]
    
    return random.choice(possible_words).upper() if possible_words else "No matching word found."

def load_words(filename):
    try:
        with open(filename) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found. Using default word list.")
        return []

def main():
    word_list = []
    word_list.extend(load_words(r'C:\Users\eliha\vsc\cove\python\sorted_words.txt'))

    while True:
        pattern = input("Enter the pattern (use _ for unknown letters, type 'exit' to quit): ")
        if pattern.lower() == "exit":
            break
        print(f"Prediction: {predict_word(pattern, word_list)}")

if __name__ == "__main__":
    main()
