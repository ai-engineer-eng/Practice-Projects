import random

def choose_word():
    words = ["python", "hangman", "developer", "challenge", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    hangman_pics = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =====
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =====
        """
    ]
    
    while incorrect_guesses < max_attempts:
        print(hangman_pics[incorrect_guesses])
        print(display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            incorrect_guesses += 1
            print("Wrong guess!")
        else:
            print("Good guess!")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return
    
    print(hangman_pics[-1])
    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
