import random

words = ["python", "computer", "internship", "programming", "developer"]
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("=== Hangman Game ===")

while incorrect_guesses < max_incorrect_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter one letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess! Attempts left:", max_incorrect_guesses - incorrect_guesses)
else:
    print("\nGame Over!")
    print("The word was:", word)
