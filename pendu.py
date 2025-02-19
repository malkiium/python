import random

def predict_word(pattern, word_list):
    pattern = pattern.lower()
    possible_words = [word for word in word_list if len(word) == len(pattern)]
    
    for i, char in enumerate(pattern):
        if char != '_':
            possible_words = [word for word in possible_words if word[i] == char]
    
    if possible_words:
        return random.choice(possible_words).upper()
    else:
        return "No prediction possible"

def main():
    word_list = ["asshole", "another", "example", "predict", "pattern", "letters"]
    while True:
        pattern = input("Enter the pattern (use _ for unknown letters): ")
        if pattern.lower() == "exit":
            break
        prediction = predict_word(pattern, word_list)
        print(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()