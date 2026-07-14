import random

# List of predefined words
words = [
    "python",
    "computer",
    "keyboard",
    "internet",
    "program"
]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    # Display guessed letters and hide others
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_wrong_guesses - wrong_guesses)

# If all attempts are used
else:
    print("\nGame Over!")
    print("The correct word was:", word)