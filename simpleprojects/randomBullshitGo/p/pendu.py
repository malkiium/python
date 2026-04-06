import os

def predict_word(pattern, word_list, last_predicted_word=None):
    pattern = pattern.lower()
    possible_words = filter(lambda word: len(word) == len(pattern), word_list)
    
    # Now check each character to allow matching of '_'
    for i, char in enumerate(pattern):
        if char != '_':
            possible_words = filter(lambda word: word[i] == char, possible_words)

    # Convert result to list to check the first match
    possible_words = list(possible_words)
    
    # Skip the last predicted word if it matches the current input pattern
    if possible_words:
        for word in possible_words:
            if word != last_predicted_word:
                return word
        return possible_words[0]  # If all predictions are same, return the first
    return "No matching word found."


def load_words(filename):
    if not os.path.exists(filename):
        print(f"Warning: '{filename}' not found. Using default word list.")
        return ["hello", "world", "python", "code"]  # Fallback words
    
    with open(filename, encoding="utf-8") as file:  # Explicitly specify UTF-8
        word_freq = [line.split() for line in file]
        word_freq = [(word, int(freq)) for word, freq in word_freq]
        word_freq.sort(key=lambda x: x[1], reverse=True)
        return [word for word, freq in word_freq]

def main():
    word_list = load_words(r'C:\Users\eliha\vsc\cove\python\en.txt')
    last_predicted_word = None

    while True:
        pattern = input("Enter the pattern (use _ for unknown letters, type 'exit' to quit): ")
        if pattern.lower() == "exit":
            break
        
        predicted_word = predict_word(pattern, word_list, last_predicted_word)
        print(f"Prediction: {predicted_word}")

        # Update the last predicted word
        if predicted_word != "No matching word found.":
            last_predicted_word = predicted_word

if __name__ == "__main__":
    main()